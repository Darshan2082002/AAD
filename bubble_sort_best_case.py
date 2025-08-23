
import time  # This module is used to check the cpu running.
import matplotlib.pyplot as plt
 
my_array=[1,10,20,30,40,50,60,70,80,100] # This the array 


input_sizes = [500] # Example input sizes
execution_times = []

def bubble(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break


        
def out_val(arr):
    for value in arr:
        print(value,end=" ")
    print() 
if __name__ == "__main__":
    
    print(out_val(my_array))  
    start_time =time.perf_counter() 
    bubble(my_array)
    end_time= time.perf_counter()
    print(out_val(my_array))
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b',markersize='50')
plt.title('Selection Sort CPU Time vs. Input Size')
plt.xlabel('Input Size (n)')
plt.ylabel('CPU Time (seconds)')
plt.grid(True)
plt.show()




    