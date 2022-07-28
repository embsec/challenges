#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <stdint.h>

void print_mem(uint8_t * buffPtr, int rows){
	
	// Calculate section positions

	// Align start addr to a multiple of 16 by chopping off the least significant 4 bits
	uint8_t * startAddr = (uint8_t *)((((uint32_t)(buffPtr)) >> 4) << 4);
	uint8_t * echoNameFrameAddr = buffPtr + 0x14;
	uint8_t * mainFrameAddr = buffPtr + 0x24;
	uint8_t * changeMeAddr = buffPtr + 0x20;

	int startColor = 30; //black
	int buffColor = 34; //light blue
	int echoNameFrameColor = 94; //blue
	int retAddrColor = 36; //light green
	int mainFrameColor = 32; //green
	
	int curColor = startColor;
	uint8_t * rowAddr = startAddr;

    printf("            0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f\n");
	
	for(int i = 0; i < rows; i ++){

		//Print address at start of line (in white)
		printf("\e[0m%p: ", rowAddr);

		//Print each byte in a row
		for(int j = 0; j < 0x10; j ++){

			//Check if we need to switch colors
			if(rowAddr + j == echoNameFrameAddr){
				// Since the stack grows downward, hitting the address of echoName's stack frame actually mains we have *passed the end* and hit the start of main's stack frame
				curColor = mainFrameColor;
			}else if(rowAddr + j == buffPtr){
				// Apply the color for buff
				curColor = buffColor;	
			}else if(rowAddr + j == buffPtr + 12){
				// Switch to the echoName stack frame color after 12 bytes of buff
				curColor = echoNameFrameColor;
			}else if(rowAddr + j == echoNameFrameAddr - 4){
				// Apply the color for the return address from echoName to main (last 4 bytes of echoName's stack frame)
				curColor = retAddrColor;
			}
			
			// Apply color
			printf("\e[%dm", curColor);
			
			// Print one byte
			printf("%02x  ", *(rowAddr + j));
		}

		printf("\n");

		rowAddr += 0x10;
	}

	printf("\e[0m\nColor key:\n");
	printf("\e[%dmbuff (in echoName's stack frame)\n", buffColor);
	printf("\e[%dmchangeMe (in echoName's stack frame)\n", echoNameFrameColor);
	printf("\e[%dmReturn address from echoName to main (in echoName's stack frame)\n", retAddrColor);
	printf("\e[%dmmain's stack frame\n", mainFrameColor);

	// Reset colors
	printf("\e[0m\n");
}

void printName(char * name){
	printf("Hi, %s!\n", name);
	return; // The address returned to here is stored in the link register, so it can't be overflowed
}

void echoName(){
	volatile int changeMe = INT_MAX;
	char buff[12];
	printf("Enter your name: ");
	gets(buff);
	printName(buff);

	if(changeMe == 0x31337){
		printf("You changed the variable!\n");
		exit(1);
	}else if(changeMe != INT_MAX){
		printf("Almost! You changed the variable, but you got the wrong value (%x).\n", changeMe);
	}

	print_mem((uint8_t *)&buff, 2);
	return; // Since this isn't the most recent call, the address returned to here is moved onto the stack and therefore can be overflowed by buff.
}

void redirectToMe(){
	printf("You redirected control flow!\n");
	exit(-1);
}

int main(int argc, char *argv[]){
	echoName();
	return 0;	
}