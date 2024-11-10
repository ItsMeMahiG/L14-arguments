def cube(number):
    return number * number * number
def divby3(num)  :
    if num % 3 == 0 :
        return cube (num)
    else :
        return False

print(divby3(27))
print(divby3(428))