----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 05/16/2024 11:36:55 PM
-- Design Name: 
-- Module Name: led - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- A project that blinks 4 LEDs per secend on the board
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

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity led is
    port(
        clk : in std_logic;
        rst : in std_logic;
        led : out std_logic_vector(3 downto 0)
    );
end led;

architecture Behavioral of led is
    signal counter : integer range 0 to 50000000 := 0;
    signal led_print : std_logic_vector(3 downto 0) := "0000";

begin
    process(clk, rst)
    begin
        if rst = '0' then
            counter <= 0;
            led_print <= "0000";
        elsif rising_edge(clk) then
            if counter = 50000000 then
                counter <= 0;
                led_print <= not led_print;
            else
                counter <= counter + 1;
            end if;
        end if;
    end process;

    led <= led_print;

end Behavioral;
