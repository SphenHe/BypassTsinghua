----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 06/03/2024 10:12:52 AM
-- Design Name: 
-- Module Name: uart_loopback - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
--   Serial UART Loopback
--   1 Serial UART loopback
--     Send a character from the computer side and get immediate feedback from the board side.
--   2 Case converter
--     Computer sends a letter, board completes case conversion
--     Feedback '@' for non-alphabetic messages.
--   3 Serial Transmitter Module with Buffering
--     This module can buffer up to 256 bytes of data.
--     This module caches up to 256 bytes of data and sends them one by one from the serial port to the computer.
--     Test method: 
--       Press A, send “ABCDEFG”; press B, send “abcdefg”;
--       Press C, send “1234567”; press D, send “!” #$%^&*()”
--    
--   We use 8 data bits and 1 stop bit, no parity bit.
-- 
-- Dependencies:  
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity uart_loopback is
    port (
        clk : in std_logic;
        rx : in std_logic;
        btnA : in std_logic;
        btnB : in std_logic;
        btnC : in std_logic;
        btnD : in std_logic;
        tx : out std_logic
    );
end uart_loopback;

architecture Behavioral of uart_loopback is
    signal rx_data : std_logic_vector(7 downto 0);
    signal rx_done : std_logic := '0';
    signal tx_start : std_logic := '0';
    signal tx_busy : std_logic := '0';
    signal tx_data : std_logic_vector(7 downto 0);

    type buffer_type is array (255 downto 0) of std_logic_vector(7 downto 0);
    signal buffers : buffer_type := (others => (others => '0'));
    signal buffer_head : integer range 0 to 255 := 0;
    signal buffer_tail : integer range 0 to 255 := 0;

    type state_type is (key_A, key_B, key_C, key_D, key_idle, key_wait);
    signal state: state_type := key_idle;
    signal delay_time: integer range 0 to 10000000 := 0;
    signal A_pressed_time: integer range 0 to 100000000 := 0;
    signal B_pressed_time: integer range 0 to 100000000 := 0;
    signal C_pressed_time: integer range 0 to 100000000 := 0;
    signal D_pressed_time: integer range 0 to 100000000 := 0;
    signal free_time: integer range 0 to 5000000 := 0;

    constant time50ms: integer := 2500000; -- 50ms
    constant time100ms: integer := 5000000; -- 100ms

begin
    -- Instantiate UART receiver
    uart_rx_inst : entity work.uart_rx
        port map (
            clk => clk,
            rx => rx,
            rx_data => rx_data,
            rx_done => rx_done
        );

    -- Instantiate UART transmitter
    uart_tx_inst : entity work.uart_tx
        port map (
            clk => clk,
            tx_start => tx_start,
            tx_data => tx_data,
            tx => tx,
            tx_busy => tx_busy
        );

    process(clk)
    begin
        if rising_edge(clk) then
            -- loopback and case conversion
            if rx_done = '1' then
                if (rx_data >= "01000001" and rx_data <= "01011010") then
                    buffers(buffer_head) <= std_logic_vector(unsigned(rx_data) + 32);
                elsif (rx_data >= "01100001" and rx_data <= "01111010") then
                    buffers(buffer_head) <= std_logic_vector(unsigned(rx_data) - 32);
                else
                    buffers(buffer_head) <= "01000000";
                end if;
                buffer_head <= (buffer_head + 1) mod 256;
            end if;
            -- Button press handling
            case state is 
            when key_wait =>
                if (delay_time > time100ms) then -- key press delay for 100ms
                    delay_time <= 0;
                    state <= key_idle;
                elsif (btnA = '0' or btnB = '0' or btnC = '0' or btnD = '0') then
                    delay_time <= 0;
                else
                    delay_time <= delay_time + 1;
                end if;
            when key_idle =>
                if btnA = '0' then
                    A_pressed_time <= A_pressed_time + 1;
                elsif btnB = '0' then
                    B_pressed_time <= B_pressed_time + 1;
                elsif btnC = '0' then
                    C_pressed_time <= C_pressed_time + 1;
                elsif btnD = '0' then
                    D_pressed_time <= D_pressed_time + 1;
                else
                    free_time <= free_time + 1;
                end if;
                if free_time > time50ms then
                    if (A_pressed_time > time50ms) then
                        state <= key_A;
                    elsif (B_pressed_time > time50ms) then
                        state <= key_B;
                    elsif (C_pressed_time > time50ms) then
                        state <= key_C;
                    elsif (D_pressed_time > time50ms) then
                        state <= key_D;
                    end if;
                    -- reset all timers
                    A_pressed_time <= 0;
                    B_pressed_time <= 0;
                    C_pressed_time <= 0;
                    D_pressed_time <= 0;
                    free_time <= 0;
                end if;
            when key_A =>
                buffers(buffer_head) <= "01000001"; -- A
                buffers(buffer_head + 1) <= "01000010"; -- B
                buffers(buffer_head + 2) <= "01000011"; -- C
                buffers(buffer_head + 3) <= "01000100"; -- D
                buffers(buffer_head + 4) <= "01000101"; -- E
                buffers(buffer_head + 5) <= "01000110"; -- F
                buffers(buffer_head + 6) <= "01000111"; -- G
                buffer_head <= (buffer_head + 7) mod 256;
                state <= key_wait;
            when key_B =>
                buffers(buffer_head) <= "01100001"; -- a
                buffers(buffer_head + 1) <= "01100010"; -- b
                buffers(buffer_head + 2) <= "01100011"; -- c
                buffers(buffer_head + 3) <= "01100100"; -- d
                buffers(buffer_head + 4) <= "01100101"; -- e
                buffers(buffer_head + 5) <= "01100110"; -- f
                buffers(buffer_head + 6) <= "01100111"; -- g
                buffer_head <= (buffer_head + 7) mod 256;
                state <= key_wait;
            when key_C =>
                buffers(buffer_head) <= "00110001"; -- 1
                buffers(buffer_head + 1) <= "00110010"; -- 2
                buffers(buffer_head + 2) <= "00110011"; -- 3
                buffers(buffer_head + 3) <= "00110100"; -- 4
                buffers(buffer_head + 4) <= "00110101"; -- 5
                buffers(buffer_head + 5) <= "00110110"; -- 6
                buffers(buffer_head + 6) <= "00110111"; -- 7
                buffer_head <= (buffer_head + 7) mod 256;
                state <= key_wait;
            when key_D =>
                buffers(buffer_head) <= "00100001"; -- !
                buffers(buffer_head + 1) <= "00100011"; -- #
                buffers(buffer_head + 2) <= "00100100"; -- $
                buffers(buffer_head + 3) <= "00100101"; -- %
                buffers(buffer_head + 4) <= "01011110"; -- ^
                buffers(buffer_head + 5) <= "00100110"; -- &
                buffers(buffer_head + 6) <= "00101010"; -- *
                buffers(buffer_head + 7) <= "00101000"; -- (
                buffers(buffer_head + 8) <= "00101001"; -- )
                buffer_head <= (buffer_head + 9) mod 256;
                state <= key_wait;
            when others =>
                state <= key_idle;
            end case;
        end if;
    end process;

    -- Transmit data from buffer
    process (clk)
    begin
        if rising_edge(clk) then
            if tx_busy = '1' then
                tx_start <= '0';
            elsif tx_busy = '0' and tx_start = '0' and buffer_head /= buffer_tail then
                tx_data <= buffers(buffer_tail);
                buffer_tail <= (buffer_tail + 1) mod 256;
                tx_start <= '1';
            end if;
        end if;
    end process;
end Behavioral;
