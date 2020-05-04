if __name__ == '__main__':
    a = int(input())
    b = int(input())

    c = a // b # Divide left operand by the right one (always results into float)
    d = a / b # Floor division - division that results into whole number adjusted to the left in the number line
    
    print(c)
    print(d)