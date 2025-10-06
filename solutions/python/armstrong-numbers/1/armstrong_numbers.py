def is_armstrong_number(number):
    num_str = str(number)
    pow = len(num_str)
    return sum(int(ch) ** pow for ch in num_str) == number
