"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt




def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<=30 or >=250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  
    data = []

    # open file and read into the `data` list
    
    file = open(filename)
    # read string in file
    for line in file:
    #appending data to a new list called data    
        data.append(line)
    file.close()
    

    # using filters_nondigits to remove nondidgits 
    data = filter_nondigits (data)

    #using filter_outliers to find vaules <=30 or >=250
    data = filter_outliers (data)

    # using metics funtions to find max,average & st.dev of heart rate data

    max = window_max (data,6)

    avg = window_average(data,6)

    stdev = window_stddev(data,6) 

  # plotting and saving graphs for max,average & st.dev
  
    fig,ax = plt.subplots()
    ax.plot(max)
    plt.savefig("images/maximums.png")


    fig,ax = plt.subplots()
    ax.plot(avg)
    plt.savefig("images/averages.png")
    
    fig,ax = plt.subplots()
    ax.plot(stdev)
    plt.savefig("images/stddev.png")

    return max,avg,stdev

    





    
    #print (data_file)
    


    # return all 3 lists
    ...


if __name__ == "__main__":
    run("data/data1.txt")
