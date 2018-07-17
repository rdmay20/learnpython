def collatz(number):
    modNumber = number % 2
    if modNumber == 0:
        evenNumber = number // 2
        print(evenNumber)
        return evenNumber
    elif modNumber % 2 == 1:
        oddNumber = 3 * number +1
        print(oddNumber)
        return(oddNumber)

print('Enter a number')
try:
    userNumber = int(input())
except NameError:
    print('enter a number')
    

while userNumber != 1:
    userNumber = collatz(userNumber)



