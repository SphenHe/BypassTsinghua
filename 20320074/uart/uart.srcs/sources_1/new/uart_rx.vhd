----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 06/03/2024 08:48:13 AM
-- Design Name: 
-- Module Name: uart_rx - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
--   UART Receiver module
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity uart_rx is
    port (
        clk        : in std_logic;
        rx         : in std_logic;
        rx_data    : out std_logic_vector(7 downto 0);
        rx_done    : out std_logic
    );
end uart_rx;

architecture Behavioral of uart_rx is
    type state_type is (IDLE, START_BIT, DATA_BITS, STOP_BIT, CLEAR);
    signal state : state_type := IDLE;

    signal bit_index : integer range 0 to 7 := 0;
    signal rx_shift_reg : std_logic_vector(7 downto 0) := (others => '0');

    constant clk_frequency : integer := 50000000;
    constant baud_rate : integer := 9600;
    constant ticks_per_bit : integer := clk_frequency / baud_rate;
    constant half_bit_ticks : integer := ticks_per_bit / 2;
    signal tick_counter : integer := 0;
begin
    process(clk)
    begin
        if rising_edge(clk) then
            case state is
                when IDLE =>
                    if rx = '0' then
                        state <= START_BIT;
                        tick_counter <= 0;
                    end if;
                when START_BIT =>
                    if tick_counter = half_bit_ticks then
                        state <= DATA_BITS;
                        bit_index <= 0;
                        tick_counter <= 0;
                    else
                        tick_counter <= tick_counter + 1;
                    end if;
                when DATA_BITS =>
                    if tick_counter = ticks_per_bit then
                        rx_shift_reg(bit_index) <= rx;
                        if bit_index = 7 then
                            state <= STOP_BIT;
                        else
                            bit_index <= bit_index + 1;
                        end if;
                        tick_counter <= 0;
                    else
                        tick_counter <= tick_counter + 1;
                    end if;
                when STOP_BIT =>
                    if tick_counter = ticks_per_bit then
                        state <= CLEAR;
                        rx_done <= '1';
                        rx_data <= rx_shift_reg;
                        tick_counter <= 0;
                    else
                        tick_counter <= tick_counter + 1;
                    end if;
                when CLEAR =>
                    state <= IDLE;
                    rx_shift_reg <= (others => '0');
                    rx_done <= '0';
                    tick_counter <= 0;
            end case;
        end if;
    end process;
end Behavioral;