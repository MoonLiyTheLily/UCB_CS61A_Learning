def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    #def right(currentx,currenty):
    #    if currentx>m or currenty>n:
    #        return 0
    #    if currentx==m and currenty==n:
    #        return 1
    #    if currentx==m:
    #        return 0
    #    if currentx>m:
    #        return 0
    #    return up(currentx+1,currenty)+right(currentx+1,currenty)
    #def up(currentx,currenty):
    #    if currentx>m or currenty>n:
    #        return 0
    #    if currentx==m and currenty==n:
    #        return 1
    #    if currenty==n:
    #        return 0
    #    if currenty>n:
    #        return 0
    #    return up(currentx,currenty+1)+right(currentx,currenty+1)
    #return (right(1,1)+up(1,1))//2
    if m==1 or n==1:
        return 1
    else:
        return paths(m-1,n)+paths(m,n-1)
    #This method by an github user
#the code above have passed doctest    

def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    #max_prod=1
    #if len(s)==0:
    #    return 1
    #elif len(s)==1:
    #    return 1
    #elif len(s)==2:
    #    return 1
    #elif len(s)==3:
    #    return max(s[0]*s[2],s[1])
    #elif s[0]*max_product(s[2:])>max_prod or s[1]*max_product(s[3:])>max_prod:
    #    max_prod=max(s[0]*max_product(s[2:]),s[1]*max_product(s[3:]))
    #else:
    #    return 1
    #return max_prod
    if len(s)==0:
        return 1
    if len(s)==1:
        return s[0]
    return max(s[0]*max_product(s[2:]),max_product(s[1:]))
    #this method by a github user
#the code above have passed doctest

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result + [ [k]+rest for rest in sums(n-k,m) if rest == [] or rest[0]!=k ]
    return result
#the code above have passed doctest