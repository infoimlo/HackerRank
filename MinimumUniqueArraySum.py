# Task: Increment any duplicate elements until all elements are unique
# Sum of its elements must be minimum possible within rules
# Sources: https://www.geeksforgeeks.org/making-elements-distinct-sorted-array-minimum-increments/


#arr = [3,2,1,2,7]

# sorted(): Function to get unique values
# # set(): Function to remove duplicate values

# Sorts array
#print(sorted(arr))


#def minUnique(arr):
 #   for  in arr:
  #      print(sorted(arr))

#minUnique(arr)


# Remove duplicates
#print(set(arr))

# Iteration by position - square each element in list
#for i in range(len(arr)):
 #   arr[i] = arr[i] ** 2

#for i in range(len(arr)):
 #    set(arr)

# Make elements distinct in sorted array by minimum increments

# Input = array with duplicates
# Output = int with sum of unique values

# Make sorted array elements distinct by incrementing elements and keeping sum to minimum
def minSum(arr, n):
    sm = arr[0]

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            j = i
            while j < n and arr[j] <= arr[j - 1]:
                arr[j] = arr[j] + 1
                j += 1
    sm = sm + arr[i]

    return sm

# Driver code
arr = [2, 2, 3, 5, 6]
n = len(arr)


# Given an integer, perform the following conditional actions:
# Array of integer values 
x = [8, 10, 15, 24, 48, 50, 53, 81]

print(len(x)) 
print(minSum(arr, n))

# Function takes in two values 
def inval(x, y): 
  if x % 2: 
   return y 


