----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 06/10/2024 12:37:07 PM
-- Design Name: 
-- Module Name: sensor - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
--   A tool to measure distance between the ultrasound sensor and the object and display it on the 7-segment display.
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

entity sensor is
    port(
        clk : in std_logic;
        -- uart communication
        rx : in std_logic;
        tx : out std_logic;
        -- HC_SR04 ultrasonic sensor
        HC_SR04_echo_pin : in std_logic;
        HC_SR04_trig_pin : out std_logic
    );
end sensor;

architecture Behavioral of sensor is
    -- UART communication signals
    signal rx_data : std_logic_vector(7 downto 0);
    signal rx_done : std_logic := '0';
    signal tx_start : std_logic := '0';
    signal tx_busy : std_logic := '0';
    signal tx_data : std_logic_vector(7 downto 0);

    -- Data buffers
    type buffer_type is array (255 downto 0) of std_logic_vector(7 downto 0);
    signal buffers : buffer_type := (others => (others => '0'));
    signal buffer_head : integer range 0 to 255 := 0;
    signal buffer_tail : integer range 0 to 255 := 0;

    -- Measurement signals
    signal measure_done : std_logic := '0';
    signal distance : integer range 0 to 88888 := 0;

    -- Constants for UART communication
    constant num0 : std_logic_vector(7 downto 0) := "00110000";
    constant num1 : std_logic_vector(7 downto 0) := "00110001";
    constant num2 : std_logic_vector(7 downto 0) := "00110010";
    constant num3 : std_logic_vector(7 downto 0) := "00110011";
    constant num4 : std_logic_vector(7 downto 0) := "00110100";
    constant num5 : std_logic_vector(7 downto 0) := "00110101";
    constant num6 : std_logic_vector(7 downto 0) := "00110110";
    constant num7 : std_logic_vector(7 downto 0) := "00110111";
    constant num8 : std_logic_vector(7 downto 0) := "00111000";
    constant num9 : std_logic_vector(7 downto 0) := "00111001";
    constant chrE : std_logic_vector(7 downto 0) := "01000101";
    constant chrR : std_logic_vector(7 downto 0) := "01010010";
    constant chrO : std_logic_vector(7 downto 0) := "01001111";
    constant chrM : std_logic_vector(7 downto 0) := "01001101";
    constant chrSpace : std_logic_vector(7 downto 0) := "00100000";
    type num_type is array (0 to 9) of std_logic_vector(7 downto 0);
    signal num : num_type := (num0, num1, num2, num3, num4, num5, num6, num7, num8, num9);

    signal distance_mem : integer range 0 to 88888 := 0;
    signal time_cnt : integer range 0 to 50000000 := 0;
    constant time1s : integer := 50000000;

    -- Debugging signals
    signal tick_out : integer range 0 to 10000000 := 0;

begin
    -- UART RX instance
    uart_rx_inst : entity work.uart_rx
        port map (
            clk => clk,
            rx => rx,
            rx_data => rx_data,
            rx_done => rx_done
        );

    -- UART TX instance
    uart_tx_inst : entity work.uart_tx
        port map (
            clk => clk,
            tx_start => tx_start,
            tx_data => tx_data,
            tx => tx,
            tx_busy => tx_busy
        );

    -- HC-SR04 driver instance
    hcsr04_driver_inst : entity work.hcsr04_driver
        port map (
            clk => clk,
            echo_pin => HC_SR04_echo_pin,
            trig_pin => HC_SR04_trig_pin,
            distance => distance,
            measure_done => measure_done,
            tick_out => tick_out
        );

    -- RX process
    process(clk)
    begin
        if rising_edge(clk) then
            if rx_done = '1' then
                if (rx_data = num0) then
                    buffers(buffer_head) <= num0;
                elsif (rx_data = num1) then
                    buffers(buffer_head) <= num(distance / 10000);
                elsif (rx_data = num2) then
                    buffers(buffer_head) <= num(distance / 1000 mod 10);
                elsif (rx_data = num3) then
                    buffers(buffer_head) <= num(distance / 100 mod 10);
                elsif (rx_data = num4) then
                    buffers(buffer_head) <= num(distance / 10 mod 10);
                elsif (rx_data = num5) then
                    buffers(buffer_head) <= num(distance mod 10);
                elsif (rx_data = num6) then
                    buffers(buffer_head) <= num(tick_out / 1470000);
                elsif (rx_data = num7) then
                    buffers(buffer_head) <= num(tick_out / 147000 mod 10);
                elsif (rx_data = num8) then
                    buffers(buffer_head) <= num(tick_out / 14700 mod 10);
                elsif (rx_data = num9) then
                    buffers(buffer_head) <= num(tick_out / 1470 mod 10);
                elsif (rx_data >= "01000001" and rx_data <= "01011010") then -- A-Z
                    buffers(buffer_head) <= std_logic_vector(unsigned(rx_data) + 32);
                elsif (rx_data >= "01100001" and rx_data <= "01111010") then -- a-z
                    buffers(buffer_head) <= std_logic_vector(unsigned(rx_data) - 32);
                else -- other characters: to @
                    buffers(buffer_head) <= "01000000";
                end if;
                buffer_head <= (buffer_head + 1) mod 256;
            end if;
            if time_cnt = time1s then
                -- print the distance.
                case distance is 
                when 65535 =>
                    buffers(buffer_head) <= chrE;
                    buffers(buffer_head + 1) <= chrR;
                    buffers(buffer_head + 2) <= chrR;
                    buffers(buffer_head + 3) <= chrO;
                    buffers(buffer_head + 4) <= chrR;
                when 32863 =>
                    buffers(buffer_head) <= chrO;
                    buffers(buffer_head + 1) <= chrO;
                    buffers(buffer_head + 2) <= chrM;
                    buffers(buffer_head + 3) <= chrE;
                    buffers(buffer_head + 4) <= chrM;
                when others =>
                    buffers(buffer_head) <= num(distance / 10000);
                    buffers(buffer_head + 1) <= num(distance / 1000 mod 10);
                    buffers(buffer_head + 2) <= num(distance / 100 mod 10);
                    buffers(buffer_head + 3) <= num(distance / 10 mod 10);
                    buffers(buffer_head + 4) <= num(distance mod 10);
                end case;
                buffers(buffer_head + 5) <= chrSpace;
                buffer_head <= (buffer_head + 6) mod 256;
                time_cnt <= 0;
            else 
                time_cnt <= time_cnt + 1;
            end if;
        end if;
    end process;

    -- TX process
    process(clk)
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
