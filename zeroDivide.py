def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error its a 0')

print(spam(12.0))
print(spam(12))
print(spam(0))
print(spam(1))