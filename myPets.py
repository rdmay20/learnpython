myPets = ['bob' , 'Jane', 'John']
print('enter pet name')
name = input()
if name not in myPets:
    print('I do not have this pet named '+ name)
else:
    print(name + ' is my pet')