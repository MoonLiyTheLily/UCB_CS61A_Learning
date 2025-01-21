def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n%10)
        swipe(n//10)
        print(n%10)
#The code above have passed the doctest.

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n-2<0:
        return 1
    else:
        return n * skip_factorial(n - 2)
#The code above have passed the doctest.

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    assert n>1
    k=n-1

    def any_divide(x):
        """To find if there is any number that can divide given n.
        Turned a loop into a recursive process.
        """
        if x==0:
            return True
        elif n%x==0 and x!=1:
            return False
        else:
            return any_divide(x-1)

    if n%k==0 and k!=1:
        return False
    else:
        return any_divide(k-1)
#The code above have passed the doctest.

def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1+hailstone(n//2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if n==1:
        return 1
    else:
        return 1+hailstone(3*n+1)

#With help of chatgpt. Man it's really so hard for me!