import time
from core import Core

def timer(func):
    def inner():
        now = time.time()
        func()
        print(time.time() - now)
    return inner

implant = Core("Kostya", 4, 30, 50, 35, 'Good')
implant.activate()
implant.show_mood()
implant.teleport(15,44,144)
implant.shock()
implant.show_mood()