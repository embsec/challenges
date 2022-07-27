# Rev engineering
# 
# 
# Technology is a large part of our lives. The world now could not function without
# these tools, so it is important they are designed well. Reverse engineering can help 
# ensure this by assisting us in locating vulnerabilities that may need to be addressed
# and letting us look at system behavior and previous designs to improve the functionality of systems.  
# 
# ### Challenge Name: rev_engineering (/embsec/rev_engineering/rev_engineering)
# 
# 
# For this challenge we will look into basic concepts associated with ELF files 
# (executable and linkable files). 
# 
# To start, let's open up a new terminal within Jupyter Labs by going to File > New > Terminal.
# For this challenge, we're going to be looking at the file 'arm1.exe'. 
# We want to enter into the directory where our file is contained using cd followed
# by our filepath to set that as our 'current directory'. 
# 
# Now we can start to examine the file! Start with the 'file' <filename> command to
# learn what type of file it is. 
# 
# You should notice that the file is ELF. How many bits is this version? You'll need
# that information later.
# 
# Now let's use readelf -h <filename> to  view the headers. Do you see the magic numbers?
# Look here: https://wiki.osdev.org/ELF#Tables
# to learn more about what they mean and use this site to figure out which byte tells
# you endianness and if this file uses little or big endian formatting.
# Feel free to use readelf -a <filename> (-a for all) to get more information on this file.
# 
# Finally, in the code block, write to the serial device a number (as an integer) that concatenates 
# the number of bits of this version ELF and the value associated with the byte that determines 
# endianness to retrieve the flag for this challenge.
# 
# 
from embsec import Serial

def rev_engineering():
    ser = Serial("/embsec/rev_engineering/rev_engineering")
    # Your code goes here!

rev_engineering()
### Challenge Name: static_analysis_challenge (/embsec/rev_engineering/static_analysis_challenge)
# 
# 
# 
# For this challenge we will be using static binary analysis to determine what a program is doing
# and from that, what we need to send to our device.
# 
# Static binary analysis involves deeply examining a file and what it does without executing
# it ourselves. This can help when we have access to a file, but don't necessarily want to run
# it on our system before knowing exactly what it will do. We definitely don't want to 
# run some kind of corrupt file that will harm our device!
# 
# In Jupyter Labs, open a new terminal. Navigate the current directory (cd) to this challenge
# folder so we have access to the files we need (for this challenge we will be using 'static'). 
# First, we can use commands similar to those used in our Rev Engineering challenge. Use 
# those and other basic commands to analyze basic information about the file.
# 
# Now that we've seen some basics, let's enter into our gdb debugger. 
# Use gdb ./<filename> to set this up. Now we can use 'disass main' to observe the assembly 
# instructions contained within this file.
# 
# As you look at the assembly code, track the instructions to figure out what is going on in the program. 
# The goal is to find the data to send the device in the code block (as a string of the appropriate 
# number of bytes) to produce the correct flag. 
# 
# Good luck! And remember, you can use any approach you want to discover the data, you are
# not limited to those described above.
# 
# 
# 
from embsec import Serial

def static_analysis_challenge():
    ser = Serial("/embsec/rev_engineering/static_analysis_challenge")
    # Your code goes here!

static_analysis_challenge()
### Challenge Name: dynamic_analysis_challenge (/embsec/rev_engineering/dynamic_analysis_challenge)
# 
# 
# 
# This challenge requires us to use dynamic binary analysis to do some reverse engineering work.
# Dynamic binary analysis involves somehow running a program to observe its behavior.
# We will be looking into the file 'dynamic' and using the gdb debugger to step through the code. 
# 
# This is an executable file that we are going to have to properly interact with to find the 
# flag for the challenge. 
# 
# To get a sense of what is going on within the program, go ahead and enter ./dynamic to run the program.
# 
# Now that you've seen it in action, let's enter into gdb by typing gdb. 
# 
# As a review, some helpful commands in gdb include:
# 
#     - b 0xNNNN... : places a breakpoint at adress 0xNNNN...
# 
#     - r : runs until breakpoint or end of program
# 
#     - c : continues running the program until the next breakpoint
# 
#     - bt : prints stack trace, use u and d to go up/down a level in the stack
#     
#     - info registers : shows what the registers contain at that time
# 
#     - p 'var' : prints current value of var
# 
# To view documentation for all gdb commands, look here: https://visualgdb.com/gdbreference/commands/
# 
# You may find the ASCII table useful, which can be found here: https://ascii-tables.com/
# 
# 
# 
from embsec import Serial

def dynamic_analysis_challenge():
    ser = Serial("/embsec/rev_engineering/dynamic_analysis_challenge")
    # Your code goes here!

dynamic_analysis_challenge()
### Challenge Name: reverse_engineering_challenge (/embsec/rev_engineering/reverse_engineering_challenge)
# 
# 
# 
# Using everything you've learned from the previous challenges in this lesson, now
# is the time to put your true reverse engineering skills to the test!
# 
# For this challenge, you will need to access the following files:
#     
#     - locked.c
# 
#     - locked (the execuatable for locked.c)
# 
#     - ReverseEngineeringChallenge.c
# 
#     - rev_eng (the executable for ReverseEngineeringChallenge.c)
# 
# Use your reverse engineering skills as you see fit to determine what these files contain,
# what they're trying to accomplish, and what your task is here. 
# 
# Good luck!
# 
# Hint: to start, go ahead and run the file you have access to by entering ./locked into a new terminal. 
# ReverseEngineeringChallenge.c is password-protected and you will not be able to open it without retrieving the
# password from looking through locked.c and what that program does.
# 
# You'll likely have to download the protected.zipx folder to access the files within it, including ReverseEngineeringChallenge.c.
# 
# 
# 
from embsec import Serial

def reverse_engineering_challenge():
    ser = Serial("/embsec/rev_engineering/reverse_engineering_challenge")
    # Your code goes here!

reverse_engineering_challenge()
