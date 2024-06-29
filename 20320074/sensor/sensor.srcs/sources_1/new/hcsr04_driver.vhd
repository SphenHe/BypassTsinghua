----------------------------------------------------------------------------------
-- Company: Tsinghua University
-- Engineer: SphenHe
-- 
-- Create Date: 06/10/2024 12:58:26 PM
-- Design Name: 
-- Module Name: hcsr04_driver - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
--   This is a driver for HC-SR04 ultrasonic sensor. It sends a 10us trigger pulse and receives the echo signal to calculate the distance.
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

entity hcsr04_driver is
    port (
        clk : in std_logic; -- Main clock
        echo_pin : in std_logic; -- Echo pin from HC-SR04
        trig_pin : out std_logic; -- Trigger pin to HC-SR04
        distance : out integer; -- Distance output
        measure_done : out std_logic; -- Measurement done signal
        tick_out : out integer -- Tick counter output (for debugging)
    );
end hcsr04_driver;

architecture Behavioral of hcsr04_driver is
    type state_type is (idle, waiting, measure, timeout);
    signal state : state_type := idle;

    constant clk_frequency : integer := 50000000; -- 50MHz clock/1s
    constant time10us : integer := 500; -- 10us trigger pulse
    constant time60ms : integer := 3000000; -- 60ms refresh rate
    constant cnt2cm : integer := clk_frequency / (340 * 1000); -- Count for 1mm (approx 1470.58)

    signal tick_counter : integer range 0 to 10000000 := 0; -- Counter for timing
    signal distance_counter : integer range 0 to 10000000 := 0; -- Counter for distance
begin
    process(clk)
    begin
        if rising_edge(clk) then
            case state is
            when idle =>
                trig_pin <= '1'; -- Start trigger pulse
                if tick_counter >= time10us then
                    trig_pin <= '0'; -- End trigger pulse after 10us
                    tick_counter <= 0;
                    state <= waiting;
                else
                    tick_counter <= tick_counter + 1;
                end if;

            when waiting =>
                if echo_pin = '1' then
                    tick_counter <= 0; -- Start counting echo time
                    state <= measure;
                elsif tick_counter >= time60ms then
                    distance <= 65535; -- Timeout, no echo signal received
                    measure_done <= '1';
                    state <= timeout;
                else
                    tick_counter <= tick_counter + 1;
                end if;

            when measure =>
                if echo_pin = '0' then
                    distance <= tick_counter / (cnt2cm * 2); -- Calculate distance
                    measure_done <= '1';
                    state <= timeout;
                elsif tick_counter >= time60ms then
                    distance <= 32863; -- Timeout, no echo signal received
                    measure_done <= '1';
                    state <= timeout;
                else
                    tick_counter <= tick_counter + 1;
                end if;

            when timeout =>
                if tick_counter >= time60ms then
                    distance <= 0; -- Reset distance
                    measure_done <= '0'; -- Reset measurement done signal
                    tick_counter <= 0;
                    state <= idle; -- Return to idle state
                else
                    tick_counter <= tick_counter + 1;
                end if;
            end case;
        end if;
        tick_out <= tick_counter; -- Output tick counter for debugging
    end process;
end Behavioral;
