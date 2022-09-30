#with a def and creating a "n" you can ask the user the amount of numbers they 
#which to enter to get the prime value of the desired numbers

# Display all the prime numbers between 1 to 250 and Store the results
lowvalue = 0
uppervalue = 250
result = []

print("The prime numbers are: ")
for number in range (lowvalue, uppervalue +1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
            result.append(str(number))
# Create a txt file with results
with open("prime_value.txt", "w") as file:
    file.writelines('\n'.join(result))
# Save script and make a note of its location(absolute path)