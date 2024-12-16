def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    #Find the max within the moving average
       
    maximums = []

    for i in range (0,len(data),n):
           
           maximum = data[i:i + n]
           maximums.append(max(maximum))
    return maximums   
           

    
    
    

#Computes the average of elements in a dataset over non-overlapping windows of size n.

def window_average(data: list, n: int) -> list:
    results = []
    for i in range (0,len(data),n ):
        window = data[i:i + n]
        window_average = sum(window)/len(window)
        results.append(round(window_average, 2))
    return results





#Computes the standard deviation of elements in a dataset over non-overlapping windows of size n.

def window_stddev(data: list, n: int) -> list:
 results =  []
 for i in range (0,len(data),n):
     window = data[i:i + n]
     if len(window) == 1:
         continue
     mean = sum(window) / len(window)
     variance = sum((i - mean) **2 for i in window) / (len(window)-1)
     stdev = variance ** 0.5
#returns a list of standard deviations (rounded to 2 decimal places) for each window.
 
     results.append(round(stdev,2))
 return results 


     
     
                 

