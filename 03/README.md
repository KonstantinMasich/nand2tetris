### Note

Memory units in Nand2Tetris project seem to be *falling-edge triggered*. This means that if we load a value into them during a _tick_ part of the clock cycle, their output does not change; it will change only on a _tock_ part of that clock cycle. 

## Flip-Flops

A nice DIY tryout with latches and flip-flops:
* [How Do Computers Remember?](https://youtu.be/I0-izyq6q5s)

Recommended videos about flip-flops and clock:
* [How Flip Flops Work - The Learning Circuit](https://youtu.be/Hi7rK0hZnfc)
* [What is a D Flip-Flop? FPGA concepts](https://youtu.be/8Rbg-pm8LiE)

There are different kinds of flip-flops, not just DFF ("data flip-flop") but also SR (set-reset) and others.

## Basic memory chips

Implemented like this:

![memchips](../img/03_basic_memory.png "Memory chips")

The rest of the memory chips of higher order are implemented in the similar manner.

We use demultiplexer to send the `load` bit to its destination according to the provided `address`, and we wire the 16-bit input value to all of the memory elements of the chip. One of them will store this value (if `load` is set to HIGH) while all the other memory elements will simply ignore the input value because they will necessarily receive 0 on their `load` input. 

After that we use multiplexer to get values from all the memory elements in the chip, and we'll ignore all the values except for the one that comes from one certain memory element - as defined by the `address` input.

## SRAM

What we've built here is called [SRAM](https://en.wikipedia.org/wiki/Static_random-access_memory) - **S**tatic **R**andom **A**ccess **M**emory. This kind of memory uses latching circuitry like flip-flops to store data. It's fast and relatively expensive, and it's mostly used for CPU cache and registers.

Other kinds of RAM exist. For example, flash memory uses floating gates to store values. [DRAM](https://en.wikipedia.org/wiki/Dynamic_random-access_memory) (Dynamic RAM) uses memory cells consisting of a tiny capacitor and transistor. Capacitor can be charged or discharged, which represents its stored value (1 or 0). Capacitor loses its charge over time, so an external *memory refresher* circuit periodically restores capacitors to their original state, effectively refreshing stored data.
