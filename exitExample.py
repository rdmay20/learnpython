import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()                  #exits on exit
    print('you typed ' +response)
