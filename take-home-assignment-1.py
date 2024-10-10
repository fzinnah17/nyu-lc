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
