# Activities & Practices

# 01 "Larger Sum"
# We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

# 1. Define the function to accept two input parameters: [lst1] and [lst2]
# 2. Create two variables to record the two sums
# 3. Loop through the first list and add up all of the numbers
# 4. Loop through the second list and add up all of the numbers
# 5. Compare the first and second sum and return the list with the greater sum

# Create a function named [larger_sum()] that takes two lists of numbers as parameters named [lst1] and [lst2].
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return [lst1].

print("'Larger Sum' challenge")
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))    
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 02 "Over 9000"
# We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this, we will need the following steps:

# 1. Define the function to accept a list of numbers
# 2. Create a variable to keep track of our sum
# 3. Iterate through every element in our list of numbers
# 4. Within the loop, add the current number we are looking at to our sum
# 5. Still within the loop, check if the sum is greater than 9000. If it is, end the loop
# 6. Return the value of the sum when we ended our loop

# Create a function named [over_nine_thousand()] that takes a list of numbers named [lst] as a parameter.
# The function should sum the elements of the list until the sum is greater than [9000]. When this happens, the function should return the sum. If the sum of all of the elements is never greater than [9000], the function should return total sum of all the elements. If the list is empty, the function should return [0].
# For example, if [lst] was [[8000, 900, 120, 5000]], then the function should return [9020].

print("'Over 9000' challenge")
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))  
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 03 "Max Num"
# Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the [max()] function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

# 1. Define the function to accept a list of numbers called [nums]
# 2. Set our default maximum value to be the first element in the list
# 3. Loop through every number in the list of numbers
# 4. Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
# 5. Return the maximum number

# Create a function named [max_num()] that takes a list of numbers named nums as a parameter.
# The function should return the largest number in [nums]

print("'Max Num' challenge")
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 04 "Same Values"
# In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index. These are the steps we need to accomplish this:

# 1. Define our function to accept two lists of numbers
# 2. Create a new list to store our matching indices
# 3. Loop through each index to the end of either of our lists
# 4. Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
# 5. Return our list of indices

# Write a function named [same_values()] that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in [lst1] and [lst2].
# For example, the following code should return [0, 2, 3]
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

print("'Same Values' challenge")
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah

# 05 "Reversed List"
# For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list. Here is what you need to do:

# 1. Define a function that has two input parameters for our lists
# 2. Loop through every index in one of the lists from beginning to end
# 3. Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return [False]
# 4. If the loop ended successfully, then we know the lists are reversed and we can return [True].

# Create a function named [reversed_list()] that takes two lists of the same size as parameters named [lst1] and [lst2].
# The function should return [True] if [lst1] is the same as [lst2] reversed. The function should return [False] otherwise.
# For example, [reversed_list([1, 2, 3], [3, 2, 1])] should return [True].

print("'Reversed List' challenge")
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

# #Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
print("--------------------------------")

# Note: I didn't even thinking how to solve the problem and clicked on "View Solution", I'll revision over all the content of the course for meet requirements of "Effective Study Sessions"
# "How things work" > "wasting time especially on introductory course"
# applying different technique for study, I'll discuss this later In Sha Allah
