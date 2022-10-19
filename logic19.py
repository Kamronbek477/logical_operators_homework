def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    if 9<x<1000 and x//100==0:
        return x%100//10+x%10*10==x 
    else:
        return x%10*100+x%100//10*10+x//100==x
        
print(main(22))