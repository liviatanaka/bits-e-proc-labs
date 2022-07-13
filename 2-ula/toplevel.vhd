-- File: toplevel.vhd
-- Generated by MyHDL 0.11
-- Date: Wed Jul 13 11:52:48 2022


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_011.all;

entity toplevel is
    port (
        LEDR: out unsigned(9 downto 0);
        SW: in unsigned(9 downto 0);
        KEY: in unsigned(3 downto 0);
        HEX0: out unsigned(6 downto 0);
        HEX1: out unsigned(6 downto 0);
        HEX2: out unsigned(6 downto 0);
        HEX3: out unsigned(6 downto 0);
        HEX4: out unsigned(6 downto 0);
        HEX5: out unsigned(6 downto 0)
    );
end entity toplevel;


architecture MyHDL of toplevel is



type t_array_hex0_ is array(0 to 7-1) of std_logic;
signal hex0_: t_array_hex0_;
type t_array_hex1_ is array(0 to 7-1) of std_logic;
signal hex1_: t_array_hex1_;
type t_array_hex2_ is array(0 to 7-1) of std_logic;
signal hex2_: t_array_hex2_;
type t_array_hex3_ is array(0 to 7-1) of std_logic;
signal hex3_: t_array_hex3_;
type t_array_hex4_ is array(0 to 7-1) of std_logic;
signal hex4_: t_array_hex4_;
type t_array_hex5_ is array(0 to 7-1) of std_logic;
signal hex5_: t_array_hex5_;
type t_array_ledr_ is array(0 to 10-1) of std_logic;
signal ledr_: t_array_ledr_;

begin





ledr_(1) <= (SW(0) xor SW(0));
ledr_(0) <= stdl(bool(SW(0)) and bool(SW(0)));

TOPLEVEL_COMB: process (hex4_, ledr_, hex1_, hex0_, hex2_, hex5_, hex3_) is
begin
    for i in 0 to 10-1 loop
        LEDR(i) <= ledr_(i);
    end loop;
    for i in 0 to 7-1 loop
        HEX0(i) <= hex0_(i);
        HEX1(i) <= hex1_(i);
        HEX2(i) <= hex2_(i);
        HEX3(i) <= hex3_(i);
        HEX4(i) <= hex4_(i);
        HEX5(i) <= hex5_(i);
    end loop;
end process TOPLEVEL_COMB;

end architecture MyHDL;
