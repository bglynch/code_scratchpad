# ========================  SLICING LISTS  ======================== #

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

# get item from the list
print(my_list[5])
# >>> 5

# get range from a list
print(my_list[0:6])     # >>> [0, 1, 2, 3, 4, 5]
print(my_list[1:-7])    # >>> [1, 2]
print(my_list[-7:-2])   # >>> [3, 4, 5, 6, 7]

# get range from item to start/end of the list
print(my_list[2:])     # >>> [2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[:-4])     # >>> [0, 1, 2, 3, 4, 5]

# get range with a step
print(my_list[2:-1:2])      # >>> [2, 4, 6, 8]

# get range backwards by using a negative step
print(my_list[-1:2:-1])     # >>> [9, 8, 7, 6, 5, 4, 3]
print(my_list[::-1])        # >>> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print('')
# ========================  SLICING STRINGS  ======================== #
sample_url = 'http://bglynch.com'

# Reverce the url
print(sample_url[::-1])     # >>> moc.hcnylgb//:ptth

# Get the top level domain
print(sample_url[-4:])      # >>> .com

# Print url without http://
print(sample_url[7:])       # >>> bglynch.com

# Print url without http:// or .com
print(sample_url[7:-4])     # >>> bglynch
