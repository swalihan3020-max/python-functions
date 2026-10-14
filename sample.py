def exponention(number,power):
    result=1
    for i in range(abs(power)):
        result*=number
    if power<0:
            return 1/result
    return result

def square_root(number):
    return number** 0.5

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number* factorial(number-1)

print("Exponention",exponention(3,5))
print("squareroot",square_root(25))
print("factorial",factorial(4))