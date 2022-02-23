"""
Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234.

def general_poly (L):
    "" 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    ""
    #YOUR CODE HERE
"""

def general_poly(L):
    def inside(x):
        total = 0
        for i in range(len(L)):
            k = (len(L)-1) - i 
            total += (L[i] * (x**k))
        return total
    return inside