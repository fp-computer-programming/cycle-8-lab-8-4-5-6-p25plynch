#Author: PJ Lynch
# lab_8-5

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        # Use recursion to calculate the factorial
        return num * factorial(num - 1)

# Example usage
if __name__ == "__main__":
    input_num = int(input("Enter a number: "))
    result = factorial(input_num)
    print(f"The factorial of {input_num} is: {result}")
