class Character(object):
    
    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter


class Enemy(Character):
    
    def __init__(self, x, y, img_file, speed):
        Character.__init__(self, x, y, img_file, speed, life_counter=5)
        self.message = "I'm here to protect my master"


class Player(Character):
    
    def __init__(self, x, y, img_file, speed=56, life_counter=6):
        Character.__init__(self, x, y, img_file, speed, life_counter)


class DifficultEnemy(Enemy):
    
    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, speed=80)


class EasyEnemy(Enemy):
    
    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, speed=40)
        self.life_counter = 1  # EasyEnemies have 1 life by default instead of 5