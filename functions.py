# x is never a good variable name to use but in this case it represents nothing tangible.
def rec_multi(x):
    if x == 0:
        return 1
    else:
        return x * rec_multi(x-1)

def do_math():
    operation = input("Addition of subtraction? ")
    def numbers():
        numbers.first_num = float(input("First number: "))
        numbers.second_num = float(input("Second number: "))
    if "add" in operation:
        numbers()
        return numbers.first_num + numbers.second_num
    elif "sub" in operation:
        numbers()
        return numbers.first_num - numbers.second_num
    # there is an implicit return of "None" if the input does not match the if control flow



print(do_math())
