import random # The module is used to generate random number 
import time  # This module is used to check the cpu running.
import matplotlib.pyplot as plt
array_size_str=input("array_size"'\n') # Input size from the user 
array_size=int(array_size_str) # converting the string into interger 
my_array=[] # This the array 

for _ in range(array_size):
    rand=random.randint(1,1000) # To generate the random value from the 1 to 500 
    my_array.append(rand) # To add the random generated number to array 

input_sizes = [1000] # Example input sizes
execution_times = []

# selection sort alogirthim 
def sel(a):
    n=len(a) # this not required when we give input from the user. it is required when we  give the pre defined value to the computer
    i=0 # starting value of i we mention it as 0. This can also be consider for the min index
    for i in range(n-1):
        
        for j in range (i+1,n):
            if my_array[j]<my_array[i]:
                my_array[i],my_array[j]=my_array[j],my_array[i] # we are swaping the element using temp variable 
            
def out_val(arr):
    for value in arr:
        print(value,end=" ")
    print()
         
if __name__ == "__main__":
    
    print(out_val(my_array))  
    start_time =time.perf_counter() 
    sel(my_array)
    end_time= time.perf_counter()
    print(out_val(my_array))
    execution_times.append(end_time - start_time)

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b',markersize='50')
plt.title('Selection Sort CPU Time vs. Input Size')
plt.xlabel('Input Size (n)')
plt.ylabel('CPU Time (seconds)')
plt.grid(True)
plt.show()