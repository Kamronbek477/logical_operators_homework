def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return 100<=a<1000 and (a//100+a%10+a%100//10)%2!=0
print(main(264))