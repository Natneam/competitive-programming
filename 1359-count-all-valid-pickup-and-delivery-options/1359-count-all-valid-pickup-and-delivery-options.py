class Solution:
    def countOrders(self, n: int) -> int:
        """
        f(n) = n*(2n - 1) * (n - 1)*f(n-1)
        """
        def calc(n):
            if n == 1:
                return 1

            return n * (2*n - 1) * calc(n - 1)
        
        return calc(n) % (10**9 + 7)