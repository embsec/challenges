# Dpa lab
# 
# 
# Practice DPA! We'll be using the Matplotlib library: https://matplotlib.org/stable/index.html
# ### Challenge Name: aes_plot (/embsec/dpa_lab/aes_plot)
# 
# 
# The code below shows you how to read in AES traces, how to plot a single trace, and
# how to access the ciphertext for a trace. Note that the ciphertext is contained in
# the attribute `meta`, and has type `bytes`.
# 
# Your task is to send the ciphertext from the 3rd trace to the grader.
# 
# Additionally, plot a few traces and take a note of the AES structure - what do you see?
# 
# Note that these traces record a decryption operation.
# 
# 
# 

from embsec import Serial
from dpa_utils import *
import numpy as np
import binascii
import h5py
import matplotlib.pyplot as plt
import os


def aes_plot():

    ser = Serial("/embsec/dpa_lab/aes_plot")
    
    traces = read_traces('/home/jovyan/lib/datasets/aes_decrypt_test.hdf5', trace_limit = 10 )
    
    t1 = traces[0]
    t1.plot_dataset()
    t1_ct = t1.meta
    print(t1_ct)
    #ser.write(b'
') <-- not needed in this example, but is needed when you write your solution!

aes_plot()

### Challenge Name: partition_random (/embsec/dpa_lab/partition_random)
# 
#  
# For this challenge, put the first 100 AES traces into one group, and the next 100 traces into another.
# Take the difference of means of these groups and plot the result.
# 
# What do you see? Why does the result look like this?
# 
# What is the absolute maximum value of the difference of means trace? Send this to the grader using the
# code stub provided.
# 
# 
# 

from embsec import Serial
from dpa_utils import read_traces
import numpy as np
import binascii
import h5py
import matplotlib.pyplot as plt
import random

def partition_random():        
    ser = Serial('/embsec/dpa_lab/partition_random')
    traces = read_traces('/home/jovyan/lib/datasets/aes_decrypt_test.hdf5', trace_limit=200)
       
    # Your code here

    max_abs_difference_of_means = # your value here! 
    ser.write(f'{max_abs_difference_of_means}\n'.encode())

    # Do not modify
    plt.figure(figsize=(12,8))
    plt.xlabel("Sample Number")
    plt.ylabel("Relative Power")
    display(plt.plot(averaged_data_1, color = "red"))
    display(plt.plot(averaged_data_2, color = "green"))
    display(plt.plot(difference_of_means, color = "blue"))
    plt.legend(["averaged_data_1", "averaged_data_2", "difference_of_means"], loc = "lower right")
    plt.show()

partition_random()


### Challenge Name: s_box_partition (/embsec/dpa_lab/s_box_partition)
# 
#  
# For this challenge you are given the first byte of the round 10 sub-key.
# Use this to partition 1000 traces into two groups, performing the `Add-Round-Key` and `Sub-Bytes` steps on each trace,
# and calculating the hamming weight of the first byte of the cipher state post s-box. Remember this is decryption, so use the inverse s-box!
# Put traces into a group if the hamming weight is > 4, a different group if < 4, and ignore the trace if the hamming weight is == 4. For the hamming weight calculation,
# use the `hamming()` function. For more information on s-boxes, check out the DPA slideshow starting at page 27, or this site: https://projectfpga.com/aes/sbox.php
# 
# To check you are calculating s-box output correctly, send the s_box output for the first trace to the grader and
# get a flag.
# 
# The code below shows you how to index the s-box. After this, you will need to plot the difference of means.
# 
# ```
# 
# row = ...  # top 4 bits of the input
# col = ...  # bottom 4 bits of the input
# 
# s_box_output = inv_s_box[row*16+col]
# 
# ```
# 
# Plot the difference of means - what do you see? In this part of your code, the `average_traces(trace_list)` function might speed things up!
# 
# Try running your code with an incorrect sub-key byte. What happens? Why? How is this related to the `partition random` challenge, above?
# 
# You can set `trace_trim` to 10000 in `read_traces()` to speed things up.
# 
# 
# 

from embsec import Serial
from dpa_utils import read_traces
from dpa_utils import hamming
from dpa_utils import average_traces
from dpa_utils import inv_s_box
import numpy as np
import binascii
import h5py
import matplotlib.pyplot as plt
import random

def s_box_partition(): 
    ser = Serial("/embsec/dpa_lab/s_box_partition")
    r_10_subkey_0 = 0xed
    traces = read_traces('/home/jovyan/lib/datasets/aes_decrypt_test.hdf5', trace_limit=1000, trace_trim = 10000)


    # Do not modify
    plt.figure(figsize=(12,8))
    plt.xlabel("Sample Number")
    plt.ylabel("Relative Power")
    display(plt.plot(averaged_data_1, color = "red"))
    display(plt.plot(averaged_data_2, color = "green"))
    display(plt.plot(difference_of_means, color = "blue"))
    display(plt.plot(abs_max, color = "orange"))
    plt.legend(["averaged_data_1", "averaged_data_2", "difference_of_means", "abs_max"], loc = "lower right")
    plt.show()

s_box_partition()

### Challenge Name: dpa (/embsec/dpa_lab/dpa)
# 
#  
# In this challenge you will have to perform full DPA. Deduce the round 10 sub-key, and then use the reverse
# keyschedule function (`reverse_ks(round_10_key)`) to get the original key. Send this key to the grader.
# 
# You'll be adding to and modifying the code below. Refer back to the DPA slides if you need help.
# 
# 
# 

from embsec import Serial
from dpa_utils import read_traces
from dpa_utils import inv_s_box
from dpa_utils import hamming
from dpa_utils import average_traces
from dpa_utils import reverse_ks
import numpy as np
import binascii
import h5py
import matplotlib.pyplot as plt
import random

def dpa(): 
    ser = Serial("/embsec/dpa_lab/dpa")
    traces = read_traces('/home/jovyan/lib/datasets/aes_decrypt_test.hdf5', trace_limit=200, trace_trim = 6000)

    
    for key_candidate in range(236,240): 
        list_1=[]
        list_2=[]
        for trace in traces: 
            trace_meta = trace.meta
            trace_meta = trace_meta[0]
            input_val = trace_meta ^ key_candidate
            row = (input_val & 0xF0) >> 4 # top 4 bits of the input
            col = input_val & 0x0F # bottom 4 bits of the input

            s_box_output = inv_s_box[row*16+col]

            partition_value = hamming(s_box_output)
            
            if partition_value < 4: 
                list_1.append(trace)
            if partition_value > 4: 
                list_2.append(trace)
            else: 
                pass

        averaged_data_1 = average_traces(list_1)

        averaged_data_2 = average_traces(list_2)

        difference_of_means = averaged_data_2 - averaged_data_1

        abs_difference_of_means = np.abs(difference_of_means)

        max_of_abs = np.max(abs_difference_of_means)
        
        ser.write(int.to_bytes(r0_key, length=16, byteorder='big')) # Use r0_key as the name of the original key
        
        plt.figure(figsize=(10,8))
        plt.xlabel("Sample Number")
        plt.ylabel("Relative Power")
        display(plt.plot(averaged_data_1, color = "red"))
        display(plt.plot(averaged_data_2, color = "green"))
        display(plt.plot(difference_of_means, color = "blue"))
        display(plt.plot(abs_difference_of_means, color = "orange"))
        plt.legend(["averaged_data_1", "averaged_data_2", "difference_of_means","abs_difference_of_means"],
        loc = "lower right")
    plt.show()
       
dpa()
