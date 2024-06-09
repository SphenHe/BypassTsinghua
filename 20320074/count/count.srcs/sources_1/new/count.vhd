----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 05/20/2024 05:54:10 PM
-- Design Name: 
-- Module Name: count - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
--   This is a 8-bit counter and it is shown with 4 LEDs.
--   When I click A, the counter will increase by 1.
--   When I click B, the counter will decrease by 1.
--     If I click C, the LEDs will switch bewteen the high 4 bits and the low 4 bits.
--     If I press C for longer than 1 second, the value will be set to 0.
--   When I click D, the counter will be reset.
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

entity count is
    port(
        clk: in std_logic; -- Clock
        rst: in std_logic; -- D
        add: in std_logic; -- A
        sub: in std_logic; -- B
        func: in std_logic; -- C
        led: out std_logic_vector(3 downto 0) -- LED
    );
end count;

architecture Behavioral of count is
    signal cnt_mode: std_logic := '0'; -- '0': low 4 bits; '1': high 4 bits
    signal cnt_reg: std_logic_vector(7 downto 0) := (others => '0'); -- Counter value
    signal cnt_led: std_logic_vector(3 downto 0) := (others => '0'); -- LED value
    type state_type is (key_add, key_sub, key_switch, key_clear, key_idle, key_wait);
    signal state: state_type := key_idle;

    signal delay_time: integer range 0 to 10000000 := 0;
    signal add_pressed_time: integer range 0 to 100000000 := 0;
    signal sub_pressed_time: integer range 0 to 100000000 := 0;
    signal func_pressed_time: integer range 0 to 100000000 := 0;
    signal free_time: integer range 0 to 5000000 := 0;

    constant time50ms: integer := 2500000; -- 50ms
    constant time100ms: integer := 5000000; -- 100ms
    constant time1000ms: integer := 50000000; -- 1000ms

begin
    process(clk, rst)
    begin
        if (rst = '0') then -- Asynchronous Reset
            cnt_mode <= '0';
            cnt_reg <= (others => '0');
            state <= key_idle;

            delay_time <= 0;
            add_pressed_time <= 0;
            sub_pressed_time <= 0;
            func_pressed_time <= 0;
            free_time <= 0;
        elsif (rising_edge(clk)) then -- Clock Edge
            case state is
            when key_wait => -- wait for some time after key press
                if (delay_time > time100ms) then -- key press delay for 100ms
                    delay_time <= 0;
                    state <= key_idle;
                elsif (add = '0' or sub = '0' or func = '0') then
                    delay_time <= 0;
                else
                    delay_time <= delay_time + 1;
                end if;
            when key_idle => -- main function - find out the key press
                if (add = '0') then -- press A / add
                    add_pressed_time <= add_pressed_time + 1;
                elsif (sub = '0') then -- press B / sub
                    sub_pressed_time <= sub_pressed_time + 1;
                elsif (func = '0') then -- press C / func - switch/clear
                    func_pressed_time <= func_pressed_time + 1;
                elsif (add = '1' and sub = '1' and func = '1') then -- free time
                    free_time <= free_time + 1;
                end if;
                if (free_time > time50ms) then
                    if (add_pressed_time > time50ms) then -- short press - add
                        state <= key_add;
                    elsif (sub_pressed_time > time50ms) then -- short press - sub
                        state <= key_sub;
                    elsif (func_pressed_time > time1000ms) then -- long press - clear
                        state <= key_clear;
                    elsif (func_pressed_time > time50ms) then -- short press - switch
                        state <= key_switch;
                    end if;
                    -- reset
                    add_pressed_time <= 0;
                    sub_pressed_time <= 0;
                    func_pressed_time <= 0;
                    free_time <= 0;
                end if;
            when key_add =>
                cnt_reg <= cnt_reg + 1;
                state <= key_wait;
            when key_sub =>
                cnt_reg <= cnt_reg - 1;
                state <= key_wait;
            when key_switch =>
                cnt_mode <= not cnt_mode;
                state <= key_wait;
            when key_clear =>
                cnt_reg <= (others => '0');
                state <= key_wait;
            when others =>
                state <= key_idle;
            end case;
        end if;
    end process;

    process(cnt_mode, cnt_reg)
    begin
        if cnt_mode = '0' then
            cnt_led <= cnt_reg(3 downto 0);
        else
            cnt_led <= cnt_reg(7 downto 4);
        end if;
    end process;

    led <= not cnt_led;

end Behavioral;
