# Assembly
# 
# 
# In this lesson you will learn the basics of writing and interpreting assembly code, the instructions executed by a CPU in order 
# to complete tasks. All of the exercises will use the ARM assembly Language and instruction set. Knowledge of assembly
# will help you discover security vulnerabilities and secrets in each team's design during the eCTF.
# 
# In order for you to be able to write assembly code directly in this Jupyter notebook, we're using iARM, an ARM interpreter for 
# the ARMv6 Thumb instruction set (Thumb is a compressed version of the ARM instruction set). There are slight differences between writing code using iARM and writing ARM anywhere else, so 
# please read our instructions carefully.
# 
# ### Conceptual Introduction to ARM
# First, what are instruction sets? Think of them as a list of things the CPU can do. We use a combination of these instructions to modify data and create programs.
# We are able to execute our instructions directly on the chip using assembly. In fact, all programs (written in languages like C, C++, Python, etc.) that you write are eventually translated to 
# assembly before being executed. It is important to understand how these programs work at the assembly level since this is exactly 
# how they are executing on the processor. 
# 
# Note that different types of processors have different instruction sets. For example, assembly written 
# for an Intel CPU will not run on an ARM processor, and vice versa. Intel CPUs are CISC (Complex Instruction Set Computing), meaning they have more 
# instructions that they are capable of executing, but that also makes the hardware more complex. CISC processors are often used in PCs, servers, and 
# consoles. ARM processors are RISC (Reduced Instruction Set Computing), and have a smaller instruction set. The smaller instruction set 
# means that programs need to be written with efficiency in mind, while a CISC program may be shorter, since it has more pre-defined 
# functions. Additionally, CISC processors have a lot of memory management instructions, so accessing areas of memory is common. While CISC 
# processors have registers, RISC processors have more and operate using values loaded into these registers. Therefore, the only 
# memory management instructions available to RISC are 'load' and 'store' (load a value to a register or store that value to memory).
# ### Challenge Name: math_challenge_one (/embsec/assembly/math_challenge_one)
# 
# 
# ### The ARM Instruction Set 
# So, what parts are there in line of ARM assembly? Take a look at this general instruction:
# 
# MNEMONIC{S}{condition} {Rd}, Operand1, Operand2
#     
# - MNEMONIC: The short name for the instruction
# - {S}: An optional suffix for the instruction, it could modify how the instruction executes
# - {condition}: An optional qualifier for the instruction. If the condition is met, the instruction is executed.
# - {Rd}: Register where the result of the operation (instruction) is stored.
# - Operand1: This can be a register or a constant value.
# - Operand2: Also a register or constant value.
# 
# Here is an example of a basic instruction:<br>
# `ADD R1, R0, #5`
# 
# ADD is the instruction, R1 is the destination register (where the result of the addition is stored), R0 is a register whose value 
# we are using in our computation, and #5 is an integer used in our computation.
# 
# Note: an integer <= 255 must be preceded by a '#' and can be put into a register using MOV. Moving a constantly defined value into a register like this is
# called immediate addressing. Otherwise, if the number is greater than 255 (meaning the register is too small to store it), the number is preceded by '=' and must be loaded into
# memory using the LDR instruction. This is called direct addressing. We'll discuss memory more soon.
# 
# The ARM processor includes 16 easily accessible registers, numbered R0 through R15. Each register stores a single 32-bit number.
# 
# ![arm instructions](https://azeria-labs.com/wp-content/uploads/2017/03/registers.png)
# 
# Here's a table of common instructions that we'll use throughout this lesson and in the BWSI course:<br>
# 
# ![arm instructions](https://azeria-labs.com/wp-content/uploads/2017/03/basic_instructions.png)
# 
# __Challenge time!__ Now you can try your hand at writing lines of assembly. Please reference the table of common instructions above, but note that
# you'll need to append 'S' to each instruction (ADD -> ADDS) except "LDR", a requirement of iARM. When writing assembly, the extra 'S' means that the
# APSR (Application Processor Status Register) will be updated depending on the outcome of the instruction.
# 
# Complete the following steps in the cell below:
# 
# 1. Load 300 into register R0 (hint: use LDR as the instruction, we'll talk about this later)
# 2. Divide value in R0 by 2, store result in R0
# 3. Move 50 into R1
# 4. Add values in R0 and R1, store result in R2
# 5. Move 2 into R3
# 5. Multiply value in R1 by value in R3, store result in R3
# 6. Subtract value in R3 from R0, store result in R4
# 
# 
# 
from embsec import Serial
import iarm.arm
import struct

interp = iarm.arm.Arm()

interp.evaluate("""
    ; Write your code here!
""")


#DO NOT TOUCH
interp.run()
ser = Serial("/embsec/assembly/math_challenge_one")
for key in interp.register:
    if(key == "APSR" or key == "PC" or key == "R15"):
        continue
    else:
        print(key, ":", interp.register[key])
        ser.write(struct.pack('H', interp.register[key]))
ser.read_until()### Challenge Name: sum_challenge (/embsec/assembly/sum_challenge)
# 
# 
# ### Conditionals
# Now let's look at conditional statements.
# 
# ARM processors have a Current Program Status Register (CPSR) that monitors the current program status. It contains information about a carry 
# bit, whether the processor is doing addition, whether an overflow occurred during an operation, and whether or not an operation resulted in a 0. 
# The last status bit (in the bit pattern that a register holds) is known as the zero bit. It can be set to zero when comparing two values. For example, if you wanted to check whether or not two values
# were equal, you could subtract one from the other. If your result was zero, the zero bit would be set to 1. If they were not equal, 
# the zero flag would be set to 0. A decision can then be made about the program based on this zero flag.
# 
# ARM processors use a set of condition codes that compare two provided values and then check these status bits. If the conditions are met, then the instruction 
# will execute. The condition codes are added as suffixes to the instruction. Here is a list of conditional 
# codes in ARM assembly:
# 
# ![arm instructions](https://azeria-labs.com/wp-content/uploads/2017/03/condition_codes.png)
# 
# To compare two values, use the CMP instruction. This instruction sets flags in the CPSR, and following instructions, will use these flags 
# to conditionally execute. Here's an example using the ADDLT instruction (ADD + LT (signed less than)):
# 
# ```asm
# MOV R0, #5 ; Put integer into register R0
# CMP R0, #8 ; Compare value in R0 to 8, Negative bit gets set to 1
# ADDLT R0, R0, #5 ; Increase value at R0 if the value was determined to be lower than 8
# ```
# 
# ### Structure of an Assembly Program
# So far, we've been looking at assembly in stand-alone blocks of code. However, just like in programs written in C, Python, or other languages, there are different parts to an
# assembly program. Generally, we can break down an assembly program into 3 parts: data, bss, and text. The data section is where program data is, so, initialized data and/or constants for example. 
# This data is not modified at runtime. The bss section is where variables are declared, however, it does not occupy any space in the object file, it is only a placeholder. Finally, the text section is where the machine
# code is. Take a look at this example program:
# 
# ```asm
# .data          ; The .data section is dynamically created and its addresses cannot be easily predicted 
# var1: .word 3  ; Variable called 'var1', '.word' allocates a word-sized amount of storage in memory, '3' is the value
# var2: .word 4  ; Another variable created, see comment above
# 
# .text          ; Start of the text (code) section 
# .global _start
# 
# _start:
#     ldr r0, adr_var1  ; Load the memory address of var1 via label adr_var1 into R0  
#     ldr r1, adr_var2  ; Load the memory address of var2 via label adr_var2 into R1  
#     ldr r2, [r0]      ; Load the value (0x03) at memory address found in R0 to register R2  
#     str r2, [r1]      ; Store the value found in R2 (0x03) to the memory address found in R1  
#     bkpt             
# 
# adr_var1: .word var1  ; Address to var1 stored here 
# adr_var2: .word var2  ; Address to var2 stored here 
# ```
# 
# ### Branches and Subroutines
# Branching allows a program to "jump" to another part of the program (a subroutine) and start executing instructions from there. In a program there is a main routine and a set of other subroutines. In reality, 
# a subroutine is just a memory address where the compiler starts executing code, but you can reference the subroutine by its name. This is similar to how you can call functions in
# higher level programming lamguages. The primary instruction that helps us achieve this with assembly is 'B'. For your next challenge, you'll also
# find certain suffixes handy, like 'L', 'X', and 'GT'. 'L' is for branching and linking. This allows us to branch to another section of instructions, run those, and then return
# to where we came from. In ARM, the Branch and Link instruction (BL) is used to Branch to subroutine. 'GT' can be used to branch to another
# subroutine based on the result of comparing two values (as discussed earlier in the conditionals section). Adding 'X' after 'B' means branch and change instruction
# sets (like from ARM to Thumb mode). When a subroutine has completed its task, the processor needs to branch back to the instruction that invoked the subroutine. This is done by moving the
# value stored in the link register to program counter. Specifically, 'BX LR' is used. Take a look at this example:
# 
# ```asm
# .global main
# 
# main:
#         mov     r1, #2     /* setting up initial variable a */
#         mov     r2, #3     /* setting up initial variable b */
#         cmp     r1, r2     /* comparing variables to determine which is bigger */
#         blt     r1_lower   /* jump to r1_lower in case r2 is bigger (N==1) */
#         mov     r0, r1     /* if branching/jumping did not occur, r1 is bigger (or the same) so store r1 into r0 */
#         b       end        /* proceed to the end */
# r1_lower: /* this is a subroutine! */
#         mov r0, r2         /* We ended up here because r1 was smaller than r2, so move r2 into r0 */
#         b end              /* proceed to the end */
# end:
#         bx lr              /* THE END */
# ```
# 
# __Let's try another challenge!__. In this one, you'll write assembly code that will add up all the numbers from 1-10 (otherwise known as computing the factorial of 10). You'll
# need to use your knowledge of conditional instructions, branching, and subroutines.
# 
# Feel free to change the structure below (by adding or removing subroutines) if that is what your solution requires. However, please be sure to store
# your result in R1. Note that the iARM subroutine syntax is a little different from normal ARM syntax.
# There should be no ':' following your subroutine name, as shown below. And, as before, instructions should be in all caps and 'S' should be added to
# the instruction if it is an operation like ADD, MUL, etc. (so, not needed with branching instructions or CMP).
# 
# 
from embsec import Serial
import iarm.arm
import struct

interp = iarm.arm.Arm()

interp.evaluate("""
    ; Write your code below!
    B main ; Branch to the main code
    
loop
            ; Your code here...
end
            ; ... and here ...
main
            ; ... and here 
              
""")

#DO NOT TOUCH
interp.run()
ser = Serial("/embsec/assembly/sum_challenge")
for key in interp.register:
    if(key == "R1"):
        print(key, ":", interp.register[key])
        ser.write(struct.pack('H', interp.register[key]))
ser.read_until()### Challenge Name: memory_challenge (/embsec/assembly/memory_challenge)
# 
# 
# ### Memory Instructions 
# In ARM assembly we read information from memory to a register, do some processing on it, and store it back in memory. To do this, you'll need to
# get comfortable using the load (LDR) and store (STR) instructions. 
# 
# Here's an example of incrementing a value from memory. The address of the value is currently stored in R0 (Register 0) and the brackets denote that the register
# holds an address that we want to read from or write to.<br>
# 
# ```asm
# LDR R1, [R0]
# ADD R1, R1 #1
# STR R1, [R0]
# ```
# 
# There are a few different ways to do addressing:
# Offset: [r1, #2] This will add 2 to the address held in r1, but r1 will remain unmodified.
# 
# Pre-indexed: [r1, #4]! This is the same as offset, the address will be the value in r1 plus 4, but now r1 will be updated to be r1+4.
# 
# Post-indexed: [r1], #4 This will use the address held in r1, but after the instruction, r1 will be updated to be r1+4
# 
# ### The Stack
# When a computer is executing a program, it may not know how much space it will need to store all its variables and information. To solve this, it uses 
# a growing data structure called the stack. A stack is able consume information, and when asked, will return the most recent thing it was given. Think 
# about a stack of plates, you can add more and more plates, but can only remove the top plate (never the bottom). This is a FILO process
# (first in, last out). Removing an item from the stack is called 'popping,' and adding an item is called 'pushing.' 
# 
# In reality, a stack is just a sequential space in memory, sort of like an array. Since we have a limited amount of registers, we can't remember every 
# address of data that we add, but we can give the stack that data, and come back to it when we need it. To achieve this, we use a register called the 
# Stack Pointer (SP). Depending on whether the stack is growing up or down, when we push a value onto the stack, the stack pointer will increase or 
# decrease to the next available memory address. We also have the Frame Pointer (FP). When the assembly code jumps to another function, a section of the stack is set aside in 
# anticipation for any local variables that are created in that function. At the bottom of the frame, meaning the frame will grow above it, exists the 
# address where the FP points. Just below that is where the LR (link register, mentioned earlier in this lesson) points, to assist in returning to the calling function. The memory in the frame is used 
# to store local values, and they can be referenced by using an offset address with the FP. The creation of frames on the stack help functions stay 
# organized.
# 
# This is a simple example program that shows how we can use the stack to temporarily store data, then recover it when we need it:<br>
# 
# ```asm
# mov   r0, #2  ; Set up r0 
# push  {r0}   ; Save r0 onto the stack 
# mov   r0, #3  ; Overwrite r0 
# pop   {r0}    ; Restore r0 to it's initial state 
# bx    lr      ; Finish the program 
# ```
# 
# __In this next challenge__, the goal is to have you practice using the PUSH, POP, and STR instructions. Your program should determine the
# largest integer out of a group of 3 integers and have it stored in R4 by the time your program terminates. Here is a list of 
# requirements/steps to guide you:
# 
# 1. Place 3 integers into registers R0-R2 and then push the values onto the stack
# 2. One by one, pop each value off and compare to the largest value so far 
# 3. If the newly popped value is the largest value so far, store the previous "largest" value to memory and then update the largest value
# 4. If the newly popped value is smaller than the largest value so far, store the value anywhere in memory
# 5. hint: create a main loop where you can then branch to other subroutines from based on your integer comparison results
# 
# 
# 
from embsec import Serial
import iarm.arm
import struct

interp = iarm.arm.Arm()

interp.evaluate("""
    ; Write your code below!
    ; Reference the previous challenge if you need to be reminded of the proper indentation, it matters!
    
              
""")

#DO NOT TOUCH
interp.run()
ser = Serial("/embsec/assembly/memory_challenge")
for key in interp.register:
    print(key, ":", interp.register[key])
    if(key == "R0" or key == "R1" or key == "R2" or key == "R4"):
        encoded = key.encode()
        ser.write(struct.pack('<2sH', encoded, interp.register[key]))
ser.read_until()