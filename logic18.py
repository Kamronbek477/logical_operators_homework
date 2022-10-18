def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return 10000<=a<100000 and (a%10)>(a%100//10)>(a%1000//100)>(a%10000//1000)>(a//10000)
print(main(23569))