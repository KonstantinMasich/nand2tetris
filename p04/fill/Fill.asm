// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


// Help:
//      * R0 holds the color code (0 or -1)
//      * R1 holds current working address (SCREEN + x)
//      * Register 32 holds the last pressed key code
(ENTRY)
    @KBD            // Optimization: compare KBD(t) == KBD(t-1) ?
    D=M
    @32
    D=D-M
    @ENTRY          // Optimization: if KBD(t) == KBD(t-1), just do nothing
        D;JEQ
    @KBD            // Save KBD into register 32
    D=M
    @32
    M=D
    @SET_COLOR_BLACK 
        D;JGT       // Set color: 0 or -1

    // This section is like SET_COLOR_WHITE:
    @R0
    M=0
    @LOOP
        0;JMP

(SET_COLOR_BLACK)
    @R0
    M=-1

(LOOP)
    // Setup:
    @SCREEN
    D=A
    @R1
    M=D
    (DRAW_16PIXELS)
        @R0         // 1. Get the current color into accumulator D
        D=M
        @R1         // 2. Increment the current working address in R1
        M=M+1
        A=M-1       // 3. Go to current working address (SCREEN + x)
        M=D         // 4. Set pixels color
        @R1         // 5. Check whether we need to draw 16 pixels once more      
        D=M
        @24576
        D=D-A
        @DRAW_16PIXELS
            D;JNE
    @ENTRY
        0;JMP