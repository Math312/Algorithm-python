class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        p0 = m - 1
        p1 = n - 1
        p2 = m + n - 1
        while p2 >= 0:
            if p0 < 0:
                A[p2] = B[p1]
                p1 -= 1
            elif p1 < 0:
                A[p2] = A[p0]
                p0 -= 1
            else:
                if A[p0] < B[p1]:
                    A[p2] = B[p1]
                    p1 -= 1
                else:
                    A[p2] = A[p0]
                    p0 -= 1
            p2 -= 1
