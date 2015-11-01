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
    if operation.startswith("add"):
        numbers()
        return numbers.first_num + numbers.second_num
    elif operation.startswith("sub"):
        numbers()
        return numbers.first_num - numbers.second_num
    # there is an implicit return of "None" if the input does not match the if control flow

def echo(message, times=1):
    for i in range(times):
        print(message)

# This breaks if the user enters anything but a non-negative whole number.
num = int(input("Please enter a non-negative, whole number: "))
print("Your answer is: " + str(rec_multi(num)))

result = do_math()
if result == None:
    print("That choice is not recognized.")
else:
    print(result)

echo("Hello")
echo("Echo..", 3)
# echo(3, "bla")
