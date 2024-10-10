## Farnaz Zinnah
## NYU Leetcode bootcamp
## Take home assignment 1

- [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

```python

def twoSum(numbers, target):
      left, right = 0, len(numbers) - 1
      while left < right:
          curr = numbers[left] + numbers[right]
          if curr > target:
              right -= 1
          elif curr < target:
              left += 1
          else:
              return [left + 1, right + 1]

# Time Complexity: O(n) for using a while loop with two pointers

```



[Products of array discluding self](https://leetcode.com/problems/product-of-array-except-self/description/)

```python

def productExceptSelf(nums):
  
  """
  Array and Hashing: Store all the data in a list and retrieve the data from the list
  for this problem, it is giving us an array, we have to return an array that for each ith place we have the product of other nums -> retrieve the products of others nums from the array
  
  Pseudocode:
  in =  [ 1, 2,  3, 4]
  out = [24, 12, 8, 6]
  
  regular prefix = [] -> [1] -> [1, 2] -> [1,2,3] -> [1,2,3, 4]
  regular postfix = [1,2,3,4] -> [2,3,4] -> [3,4] -> [4] -> []
  
  multiplied prefix = [1] -> -> [1,1*2 = 2] -> [1,2, 1*1*2*3 = 6] -> [1,2,6, 1*1*2*3*4 = 24]  
  -> [1,1,2,6,24]
  multiplied postfix = [1*2*3*4 = 24] -> [2*3*4 = 24] -> [3*4 = 12] -> [4] -> []  
  -> [24,24,12,4,1]
  
 [ 1,  1,  2,  6, 24]
     x   x   x   x
 [24, 24, 12, 4,   1]
 
 [24, 12, 8, 6]
 
 how to do this zigzag multiplication?
 
  """
  n = len(nums)
  preList = [1] * n
  postList = [1] * n
      
  for i in range(1,n):
      preList[i] = preList[i - 1] * nums[i - 1]

  for i in range(n - 2, -1, -1):
      postList[i] = postList[i+1] * nums[i + 1]
  
  result = []
  
  for i in range(n):
      result.append(preList[i] * postList[i])
  
  return result
            
```
