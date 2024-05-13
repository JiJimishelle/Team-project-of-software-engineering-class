Question
-------------------------------------

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Function Definition:
-------------------------------------------
This code defines a function named singleNumber that takes a list of integers nums as input.
Inside the function, a variable result is initialized to 0.
The function then iterates over each number num in the input list nums.
For each num, it performs a bitwise XOR operation (^=) between the current value of result and num, and assigns the result back to result. This effectively cancels out duplicate numbers because XORing a number with itself results in 0, leaving only the single number that appears once.
Finally, the function returns the result, which holds the single number that appears only once in the input list.


Taking User Input:
---------------------------------
This part of the code prompts the user to enter a list of integers separated by spaces.
The input() function is used to accept user input.
The input string is split using the split() method, which splits the string at whitespace characters and returns a list of substrings.
The map() function is then used to convert each substring into an integer using the int() function, and the list() function is used to convert the resulting map object into a list.
The resulting list of integers is assigned to the variable nums.


Function Invocation and Output:
--------------------------------------------
This part of the code simply prints the input list nums entered by the user.
It then calls the singleNumber function with the input list nums as an argument and prints the output, which is the single number that appears only once in the input list.


Example
---------------------------------
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1




Halstead calculation result
----------------------------------
Halstead Length (N): 8

Halstead Volume (V): 21.15685424949238




