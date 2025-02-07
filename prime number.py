#determine if number is a prime number
number = int(input("Enter a number: "))
for x in range (2,number):
    if (number % x )== 0:
        print(number,"is not a prime number")
        break

else :
    print(number,"is a prime number")



