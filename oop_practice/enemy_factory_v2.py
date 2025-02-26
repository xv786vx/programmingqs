class Enemy:
    def __init__(self, health, speed, atk_power):
        self.health = health
        self.speed = speed
        self.atk_power = atk_power
        
    def get_health(self):
        return self.health
        
    def get_speed(self):
        return self.speed

    def get_atk_power(self):
        return self.atk_power
    
    def get_type(self):
        return self.__class__.__name__

        
    
class Zombie(Enemy):
    def __init__(self, health=1, speed=1, atk_power=1):
        super().__init__(health, speed, atk_power)   
    
class Vampire(Enemy):
    def __init__(self, health=2, speed=2, atk_power=2):
        super().__init__(health, speed, atk_power)   
    
class Werewolf(Enemy):
    def __init__(self, health=3, speed=3, atk_power=3):
        super().__init__(health, speed, atk_power)   

class EnemyFactory:
    def create_enemy(self, difficulty):
        if difficulty == 'Easy':
            return Zombie()
        
        elif difficulty == 'Medium':
            return Vampire()
            
        elif difficulty == 'Hard':
            return Werewolf()