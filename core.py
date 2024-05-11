class Core:# коментов не будет, сам пытайся разобраться лох
    def __init__(self, name: str, strength: int, stealth: int, mind: int, speed: int, mood: str) -> None:
        self.name = name
        self.strength = strength
        self.stealth = stealth
        self.mind = mind
        self.speed = speed
        self.mood = mood
        self.history = []
        self.position = {'x': 0, 'y': 0, 'z': 0}
        self.activation = False

    def activate(self):
        self.activation = True
        print(f'Hello! My name is {self.name.capitalize()}, i have a {self.mood.lower()} mood.')

    def show_mood(self):
        print(f'I have a {self.mood.lower()} mood. Thank you for your care!')

    def shock(self):
        self.history.append('shocked')
        self.mood = 'shocked'
        print('I`ve been shocked!')

    def teleport(self, x: int, y: int, z: int):
        self.position['x'] = x
        self.position['y'] = y
        self.position['z'] = z
        print(f'My new coordinates: {self.position}')
