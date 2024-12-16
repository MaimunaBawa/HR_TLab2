## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[During the data collection process they could have temporary signal loss which could be the cause of the "NO SIGNAL" message in our data. Ignoring these vaules could lead to risk such as having reduced sample size, less accurate data which could results in distorted relationship which could have misleading conclusions. ]

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

[The standard deviation describes the average distance of data points from the mean (average). In this context, the standard deviation indicates how much the heart rate values vary over time. A higher standard deviation suggests that the heart rate values are more spread out and fluctuate significantly, while a lower standard deviation indicates that the heart rate values are more consistent and closer to the mean.]

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

[From x-values 10 to 30 we can observe a drastic spike in average of heart rate data. This suggests the heart rate is elevated during this period.]

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

[Yes there is a corresponding difference in values in the "stdevs.png, the differece is present from 10 to 30 as wells which indicate the vaules are widely spread. ]
