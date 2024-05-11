import time

def add_message(func):
    def inner():
        now = time.time()
        func()
        print(time.time() - now)
    return inner

@add_message
def gaaay():
    print('lool')
    time.sleep(1)

gaaay()