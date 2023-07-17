def sol(arr):
      ans = []
      m, n = len(arr[0]), len(arr)
      t, l = 0, 0
      r, b = len(arr[0]), len(arr)
      while l <= r and t <= b:
          # top
          for i in range(l, r):
              ans.append(arr[t][i])
          t += 1
          # right
          for num in range(t, b):
              ans.append(arr[num][r - 1])
          r -= 1
         
          for num in reversed(range(l, r)):
              ans.append(arr[b - 1][num])
          b -= 1
          # left
          for num in reversed(range(t, b)):
              ans.append(arr[num][l])
          l += 1
      return ans[: m * n]


# time O(m*n) | space O(m*n)

#also as leetcode solution
