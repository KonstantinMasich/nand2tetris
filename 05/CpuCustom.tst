// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/05/CPU.tst

load CPU.hdl,
output-file CpuCustom.out,
compare-to CpuCustom.cmp,
output-list time%S0.4.0 inM%D0.6.0 instruction%B0.16.0 reset%B2.1.2 outM%D1.6.0 writeM%B3.1.3 addressM%D0.5.0 pc%D0.5.0 DRegister[]%D1.6.1;


set instruction %B0011000000111001, // @12345
tick, output;
tock, output;

set instruction %B1110110000010000, // D=A
tick, output;
tock, output;

set instruction %B0101101110100000, // @23456
tick, output;
tock, output;

set instruction %B1110000111110000, // AD=A-D
tick, output;
tock, output;

set instruction %B0000001111101011, // @1003
tick, output;
tock, output;

set instruction %B1110001100001000, // M=D
tick, output;
tock, output;
