import statistics
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(statistics.mean(my_list))      # Mean
print(statistics.median(my_list))    # Median
print(statistics.mode(my_list))      # Mode
print(statistics.stdev(my_list))     # Standard Deviation
print(statistics.variance(my_list))  # Variance

#also we can use statistics as s or any short keyword
import statistics as s
print(s.mean(my_list))      # Mean  
print(s.median(my_list))    # Median
print(s.mode(my_list))      # Mode
print(s.stdev(my_list))     # Standard Deviation
print(s.variance(my_list))  # Variance
