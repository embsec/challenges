# Buffer overflow
# 
# 
# Welcome to the Buffer Overflow lesson! 
# 
# 
# ## Info that applies to all challenges:
# 
# ### Getting set up and debugging
# - Open two new terminals
#     - Click the blue "+" button in the upper left or use *File -> New Launcher*
#     - Arrange the panes into a somewhat sane configuration. For example, the instructions and one terminal top/bottom on the left, the second terminal on the right.
#     - You'll want one of the terminals to be as large as possible because this is where we'll be using GDB.
#     - If you have multiple monitors, now is a great time to open another Jupyterlab instance on another monitor for more real estate.
# - Navigate both terminals to `/host/courses/embsec/embsec_student/lessons/buffer_overflow`
# - In the small terminal, launch the binary in debug mode in QEMU with `debug-arm-user ./target`
# - In the large terminal, connect GDB with `gdb-remote`
# - Run `file target` to load source code and debug information. It will ask if you want to change symbols while debugging, say yes.
# - Set a breakpoint at the beginning of `main` with `break main`
# - Run until the breakpoint with `continue`
# 
# ### Target binary source code
# ```c
# #include <stdio.h>
# #include <stdlib.h>
# #include <limits.h>
# #include <stdint.h>
# 
# void print_mem(uint8_t * buffPtr, int rows){
# 	// The contents of this function are not important for the challenge.
#     // Code is omitted here to remove unnecessary complexity.
# }
# 
# void printName(char * name){
# 	printf("Hi, %%s!\n", name);
# 	return;
# }
# 
# void echoName(){
# 	volatile int changeMe = INT_MAX;
# 	char buff[12];
# 	printf("Enter your name: ");
# 	gets(buff);
# 	printName(buff);
# 
# 	if(changeMe == 0x31337){
# 		printf("You changed the variable!\n");
# 		exit(1);
# 	}else if(changeMe != INT_MAX){
# 		printf("Almost! You changed the variable, but you got the wrong value (%%x).\n", changeMe);
# 	}
# 
# 	print_mem((uint8_t *)&buff, 2);
# 	return;
# }
# 
# void redirectToMe(){
# 	printf("You redirected control flow!\n");
# 	exit(-1);
# }
# 
# int main(int argc, char *argv[]){
# 	echoName();
# 	return 0;	
# }
# ```
# 
# ### Useful GDB commands:
# - `break functionName`: Set a breakpoint at the beginning of a function
#     - `break *0x1337` to set a breakpoint at a specific address
# - `info break`: View currently set breakpoints
# - `delete 2`: Delete breakpoint 2 (Numbers shown in `info break`)
#     - `delete`: Delete all breakpoints
# - `continue`: Run program until the next breakpoint
# - `si` (step instruction): Step forward one assembly instruction, stepping into function calls
# - `ni` (next instruction): Step forward one assembly instruction, stepping over function calls
# 
# - `print functionName`: Print information about a function, including its address
# - `info frame`: Get information on the current and previous stack frames
# - `up`: Move view up one level in the call stack without changing execution state
# - `down`: Move view down one level in the call stack without changing execution state
# - `inspect variableName`: View the contents of a variable
#     - `inspect &variableName` to view the variable's address
# - `x/64bx 0x1337`: Display 64 bytes of memory starting at address 0x1337
#     - First `x` means eXamine memory
#     - 64 is length, 0x1337 is address (these can of course be whatever you want)
#     - `b` specifies unit size of a byte.
#         - `h`: halfword (2 bytes)
#         - `w`: word (4 bytes)
#     - second `x` specifies to print data in hexadecimal rather than the default format: decimal
# 
# - `disass functionName`: Jump disassembly view to a function
# - `refresh`: Sometimes the screen will get a little wonky in GDB. This will reset the interface to how it's supposed to be.
# 
# ## Passing hex values into stdin:
# - `echo -ne "\xab\xcd" | ./target`: Send two raw bytes (ab, cd) to the binary.
#     - In contrast, `echo "abcd" | ./target` would send the target "abcd" encoded in ASCII, which in raw bytes is `61, 62, 63, 64`.
#     - `echo -ne "\xab\xcd" | debug-arm-user ./target` to use GDB on the binary while it runs with your custom input.
# 
# ### Challenge Name: crash_me (/embsec/buffer_overflow/crash_me)
# 
# 
# Often, a good first step to finding a vulnerability in a binary or system is simply to get it to crash. See if you can do that to the target binary by entering an input it's not expecting.
# 
# 

### Challenge Name: change_variable (/embsec/buffer_overflow/change_variable)
# 
# 
# Now that you've gotten it to crash, try to understand why and how it broke. Can you exploit that vulnerability to perform a more controlled attack? Try to set the `changeMe` variable in `echoName` to 0x31337.
# 
# 

### Challenge Name: redirect_control_flow (/embsec/buffer_overflow/redirect_control_flow)
# 
# 
# You've changed a variable, but what if you could actually change the execution path of the program? Control flow manipulation is just a hop, skip, and a jump from remote code execution. Try to get the program to run the `redirectToMe` function, which is in the binary but never called.
# 
# 

