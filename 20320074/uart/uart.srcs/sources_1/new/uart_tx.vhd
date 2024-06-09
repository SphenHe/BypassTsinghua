----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 06/03/2024 08:48:13 AM
-- Design Name: 
-- Module Name: uart_tx - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
--   UART Transmitter module
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

entity uart_tx is
    port (
        clk        : in std_logic;
        tx_start   : in std_logic;
        tx_data    : in std_logic_vector(7 downto 0);

        tx         : out std_logic;
        tx_busy    : out std_logic
    );
end uart_tx;

architecture Behavioral of uart_tx is
    type state_type is (IDLE, START_BIT, DATA_BITS, STOP_BIT, CLEAR);
    signal state : state_type := IDLE;

    signal bit_index : integer range 0 to 7 := 0;
    signal tx_shift_reg : std_logic_vector(7 downto 0);

    constant clk_frequency : integer := 50000000;
    constant baud_rate : integer := 9600;
    constant ticks_per_bit : integer := clk_frequency / baud_rate;
    signal tick_counter : integer := 0;
begin
    tx_busy <= '1' when state /= IDLE else '0';
    process(clk)
    begin
        if rising_edge(clk) then
            case state is
                when IDLE =>
                    if tx_start = '1' then
                        state <= START_BIT;
                        tx_shift_reg <= tx_data;
                        tick_counter <= 0;
                    end if;
                when START_BIT =>
                    tx <= '0';
                    if tick_counter = ticks_per_bit then
                        state <= DATA_BITS;
                        bit_index <= 0;
                        tick_counter <= 0;
                    else
                        tick_counter <= tick_counter + 1;
                    end if;
                when DATA_BITS =>
                    tx <= tx_shift_reg(bit_index);
                    if tick_counter = ticks_per_bit then
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
                    tx <= '1';
                    if tick_counter = ticks_per_bit then
                        state <= CLEAR;
                        tick_counter <= 0;
                    else
                        tick_counter <= tick_counter + 1;
                    end if;
                when CLEAR =>
                    state <= IDLE;
                    tx <= '1';
                    tick_counter <= 0;
            end case;
        end if;
    end process;
end Behavioral;