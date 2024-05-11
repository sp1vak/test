def add_message(func):
    def inner():
        print('fantastic')
        func()
        print('cocacolastic')
    return inner

@add_message
def gaaay():
    print('amma gaaay')

gaaay()