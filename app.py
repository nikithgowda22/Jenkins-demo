def is_even(number):
    return number % 2 == 0

if __name__ == "__main__":
    num = 4
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
