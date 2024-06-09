----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 05/20/2024 10:37:47 AM
-- Design Name: 
-- Module Name: pwm - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- A program that make my four led's produce a breath effect and running horse effect
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

entity pwm is
    port(
        clk : in std_logic;
        rst : in std_logic;
        pwm : out std_logic_vector(3 downto 0)
    );
end pwm;

architecture Behavioral of pwm is
    signal cnt : std_logic_vector(31 downto 0) := (others => '0');
    signal pwm_cnt : std_logic_vector(7 downto 0) := (others => '0');

    signal pwm_duty_0 : std_logic_vector(7 downto 0) := "00000000";
    signal pwm_duty_1 : std_logic_vector(7 downto 0) := "10000000";
    signal pwm_duty_2 : std_logic_vector(7 downto 0) := "11111111";
    signal pwm_duty_3 : std_logic_vector(7 downto 0) := "10000000";
    signal pwm_dir_0 : std_logic := '1';
    signal pwm_dir_1 : std_logic := '1';
    signal pwm_dir_2 : std_logic := '0';
    signal pwm_dir_3 : std_logic := '0';

    constant pwm_period : std_logic_vector(7 downto 0) := "11111111"; -- Maximum PWM period
    constant cnt_max : std_logic_vector(31 downto 0) := "00000000000000111111111111111111"; -- Adjust for breathing speed

begin
    process(clk, rst)
    begin
        if rst = '0' then
            cnt <= (others => '0');
            pwm_cnt <= (others => '0');
            pwm_duty_0 <= "00000000";
            pwm_duty_1 <= "10000000";
            pwm_duty_2 <= "11111111";
            pwm_duty_3 <= "10000000";
            pwm_dir_0 <= '1';
            pwm_dir_1 <= '1';
            pwm_dir_2 <= '0';
            pwm_dir_3 <= '0';
        elsif rising_edge(clk) then
            -- Main counter for PWM period
            if cnt = cnt_max then
                cnt <= (others => '0');
                
                -- Adjust PWM duty cycle to create breathing effect

                if pwm_dir_0 = '1' then
                    if pwm_duty_0 = pwm_period then
                        pwm_dir_0 <= '0';
                    else
                        pwm_duty_0 <= pwm_duty_0 + 1;
                    end if;
                else
                    if pwm_duty_0 = "00000000" then
                        pwm_dir_0 <= '1';
                    else
                        pwm_duty_0 <= pwm_duty_0 - 1;
                    end if;
                end if;

                if pwm_dir_1 = '1' then
                    if pwm_duty_1 = pwm_period then
                        pwm_dir_1 <= '0';
                    else
                        pwm_duty_1 <= pwm_duty_1 + 1;
                    end if;
                else
                    if pwm_duty_1 = "00000000" then
                        pwm_dir_1 <= '1';
                    else
                        pwm_duty_1 <= pwm_duty_1 - 1;
                    end if;
                end if;

                if pwm_dir_2 = '1' then
                    if pwm_duty_2 = pwm_period then
                        pwm_dir_2 <= '0';
                    else
                        pwm_duty_2 <= pwm_duty_2 + 1;
                    end if;
                else
                    if pwm_duty_2 = "00000000" then
                        pwm_dir_2 <= '1';
                    else
                        pwm_duty_2 <= pwm_duty_2 - 1;
                    end if;
                end if;

                if pwm_dir_3 = '1' then
                    if pwm_duty_3 = pwm_period then
                        pwm_dir_3 <= '0';
                    else
                        pwm_duty_3 <= pwm_duty_3 + 1;
                    end if;
                else
                    if pwm_duty_3 = "00000000" then
                        pwm_dir_3 <= '1';
                    else
                        pwm_duty_3 <= pwm_duty_3 - 1;
                    end if;
                end if;

            else
                cnt <= cnt + 1;
            end if;

            -- PWM counter
            if pwm_cnt = pwm_period then
                pwm_cnt <= (others => '0');
            else
                pwm_cnt <= pwm_cnt + 1;
            end if;
        end if;

    end process;

    -- LED output control with phase difference
    pwm(0) <= '1' when unsigned(pwm_cnt) < unsigned(pwm_duty_0) else '0';
    pwm(1) <= '1' when unsigned(pwm_cnt) < unsigned(pwm_duty_1) else '0';
    pwm(2) <= '1' when unsigned(pwm_cnt) < unsigned(pwm_duty_2) else '0';
    pwm(3) <= '1' when unsigned(pwm_cnt) < unsigned(pwm_duty_3) else '0';

end Behavioral;
