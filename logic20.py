def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    return  0<n<100000 and n%10%2+n%100//10%2+n%1000//100%2+n%10000//1000%2+n//10000%2>(n%10+1)%2+(n%100//10+1)%2+(n%1000//100+1)%2+(n%10000//1000+1)%2+(n//10000+1)%2
print(main(11100))