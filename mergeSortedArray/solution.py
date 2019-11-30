class Solution:
    def mergeSortedArray(self, num1, m, num2, n):
        p1 = m - 1
        p2 = n - 1
        p = m + n -1
        while p1 >= 0 and p2 >= 0:
            if num1[p1] <= num2[p2]:
                num1[p] = num2[p2]
                p2 = p2 - 1
            else:
                num1[p] = num1[p1]
                p1 = p1 - 1
            p = p - 1
        return num1

