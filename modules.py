'''import math

absolute = 5
floor_test = 198.42

result1 = math.fabs(absolute)
result2 = math.floor(floor_test)

print(result1, " is the absolute value of ", absolute)
print(result2, " is the flow of ", floor_test)'''

def checkvalue(valuetocheck):
    assert (type(valuetocheck) is int), "You must enter a number"
    assert (valuetocheck > 0), "Value entered must be grater than 0"
    if valuetocheck > 4:
        print("Value is greater than 4")

var = int(input("Enter a number greater than 0: "))
checkvalue(var)


#acabas de crear un error