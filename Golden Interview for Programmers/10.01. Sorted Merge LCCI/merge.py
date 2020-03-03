class Solution(object):
    def merge(self, A, m, B, n):
        """
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(0,len(B)):
                A[i] = B[i]
            return
        len_A = len(A)
        i = 1
        while i <= m:
            A[len_A - i] = A[m - i]
            i += 1
        p0 = len_A - m
        p1 = 0
        p2 = 0
        while p2 < m + n:
            if p0 == m+n:
                A[p2] = B[p1]
                p1 += 1
            elif p1 == n:
                A[p2] = A[p0]
                p0 += 1
            else:
                if A[p0] > B[p1]:
                    A[p2] = B[p1]
                    p1 += 1
                else:
                    A[p2] = A[p0]
                    p0 += 1
            p2 += 1
