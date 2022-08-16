#Learn and practice 5 functions of math and statistics library.

#Math Library
#Python has a built-in module that you can use for mathematical tasks

1#Pi
import math #Import Math Library
print(math.pi)  #Print the value of Pi

2#Tau
import math #Import from Math Library
#It is defined as the ratio of the circumference to the radius of a circle.
#Tau is a circle constant and the value is equivalent to 2π
print(math.tau) #Print the value of tau

3#Euler's
import math #Import math library
print(math.e)  #Print the value of E

4#floating-point positive infinity
import math # Import math Library
print (math.inf)    # Print the positive infinity
print (-math.inf)   # Print the positive infinity

5#floating-point nan (Not a Number) value. This value is not a legal number
import math # Import math Library
print (math.nan)    # Print the value of nan

print('---Math Library finish---')
print('---Statistics Library Starts---')

#Statistics Library
#Python has a built-in module that you can use to calculate mathematical statistics of numeric data.

1#Mean
#The statistics.mean() method calculates the mean (average) of the given data set.
#Tip: Mean = add up all the given values, then divide by how many values there are.

import statistics   # Import statistics Library
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))     # Calculate average values

2#Median
#The statistics.median() method calculates the median (middle value) of the given data set.
#This method also sorts the data in ascending order before calculating the median
#The mathematical formula for Median is: Median = {(n + 1) / 2}th value,where n is the number of values in a set of data
#The median is the number in the middle.
import statistics   # Import statistics Library
print(statistics.median([1, 3, 5, 7, 9, 11, 13]))   # Calculate middle values

3#Mode
#The statistics.mode() method calculates the mode (central tendency) of the given numeric or nominal data set.
import statistics   # Import statistics Library
print(statistics.mode([1, 1, 3, -5, 7, -9, 11]))    # Calculate the mode

4#Standard Deviation
#The statistics.stdev() method calculates the standard deviation from a sample of data
#Standard deviation is a measure of how spread out the numbers are
#Standard deviation is the square root of sample variance.
import statistics   # Import statistics Library
print(statistics.stdev([1, 3, 5, 7, 9, 11]))    ## Calculate the standard deviation from a sample of data

5#Variance
#The statistics.variance() method calculates the variance from a sample of data (from a population)
#A large variance indicates that the data is spread out, - a small variance indicates that the data is clustered closely around the mean.
import statistics   # Import statistics Library
print(statistics.variance([1, 3, 5, 7, 9, 11])) #Calculate the variance from a sample of data
