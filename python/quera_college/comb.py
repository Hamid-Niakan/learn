def comb(n, k):
    def factorial(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    if k > n:
        return 0
    return (factorial(n) / (factorial(k) * factorial(n - k)))
