ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()  # To sort the list
print(ages)
minimum = min(ages)  # To find min of list
maximum = max(ages)  # To find max of list
print(minimum)  # Printing min of list
print(maximum)  # Printing max of list
ages.append(minimum)  # To add min to list
ages.append(maximum)  # To add max to list
print(ages)  # Printing list after adding min,max
length = len(ages)  # To find a length of list
a = (length - 1) // 2
median = (ages[a] + ages[a + 1]) / 2  # To find median of list
print(median)  # To print the median
print((sum(ages) / length))  # To print the  average
print(maximum - minimum)  # To print the  range