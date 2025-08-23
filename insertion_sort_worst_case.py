
import time  # This module is used to check the cpu running.
import matplotlib.pyplot as plt
my_array=[100,90,80,70,60,50,40,30,20,10,1]
input_sizes = [500] # Example input sizes
execution_times = []

def inst(array):
    n=len(array)
    if n<=1:
        return
    for i in range(1,n):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]  # Shift elements to the right
            j -= 1
        array[j+1] =key
        
def out_val(arr):
    for value in arr:
        print(value,end=" ")
    print() 
if __name__ == "__main__":
    
    print(out_val(my_array))  
    start_time =time.perf_counter() 
    inst(my_array)
    end_time= time.perf_counter()
    print(out_val(my_array))
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b',,markersize='50')
plt.title('Selection Sort CPU Time vs. Input Size')
plt.xlabel('Input Size (n)')
plt.ylabel('CPU Time (seconds)')
plt.grid(True)
plt.show()