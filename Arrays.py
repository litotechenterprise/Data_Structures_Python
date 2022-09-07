
# creating an array 
nums = [1,2,30,4,50]

#random indexing ----> o(1) get items if we know the index
# print(nums[2])

# changing the value of an array
#nums[2] = 2000

# using a for-loop with arrays
#for n in nums:
    #print(n)

# using indices with arrays
#for i in range(len(nums)):
 # the i print out the index of where we are within the array 
   # print(i)
# Using Nums[i] we are able to print out the value at the specific position
    #print(nums[i])


# Splice notation
# What if we only wanted to print the first two items within an array?
# name of the namedArray[ startingIndex : UpUntilThisIndex ]
#print(nums[0:2])

#what if we dont want to print the last item?
# we can use this sintax
#print(nums[:-1])

#Last Two items??
#print(nums[:-2])


# what if we wanted to find the Max Value within array

# O(N) search running time complexity
max = 0
for n in nums:
    if (n > max):
        max = n

print(max)
