
## Computer

Implemented as follows:

![memchips](../img/05_computer.png "Computer")

- Each bus is a collection of 15 (address) or 16 (control, data) wires. So 15 or 16 bits can be passed through these buses simultaneously; this number is called **bus width**.
- IRL a different architecture is common: address bus is used to address RAM / ROM, data bus is used for getting both data and instructions, and [control bus](https://en.wikipedia.org/wiki/Control_bus) has signal wires on it - like WR (write signal), RD (read signal), or others like IORQ (I/O request), MEMRQ (memory request), etc.
- Address bus works only in one way - from CPU to RAM/ROM. Contrary to that, data bus works in both ways, so sometimes CPU is source and memory is destination, and sometimes memory is source and CPU is destination. 
- Width of data bus is what they mean when they say "this is a 32bit CPU" or "this is a 64bit CPU". That's a maximum size (in bits) of data that CPU can receive or transmit at a given moment.
- However, when they say "32bit OS" or "64 bit OS" - that typically means the amount of RAM addresses reachable by that particular OS. While 32bit OS technically can reach 2^32 addresses, the 64bit one can work with 2^64 addresses.
