class Enemy:
    def __init__(self, health, speed, attack_power):
        self.health = health
        self.speed = speed
        self.attack_power = attack_power
        
    def get_health(self):
        return self.health
    
    def get_speed(self):
        return self.speed
        
    def get_attack_power(self):
        return self.attack_power
    
    def get_type(self):
        return self.__class__.__name__
    
    

class Zombie(Enemy):
    def __init__(self, health=50, speed=2, attack_power=10):
        super().__init__(health, speed, attack_power)
    
class Vampire(Enemy):
    def __init__(self, health=30, speed=4, attack_power=15):
        super().__init__(health, speed, attack_power)
    
class Werewolf(Enemy):
    def __init__(self, health=80, speed=6, attack_power=25):
        super().__init__(health, speed, attack_power)


class EnemyFactory:
    def create_enemy(self, difficulty):
        if difficulty == 'Easy':
           return Zombie() 
        elif difficulty == 'Medium':
            return Vampire()
        elif difficulty == 'Hard':
            return Werewolf()
            
def main():
    # Input: Difficulty level
    difficulty = "Hard"
    
    factory = EnemyFactory()

    # Call the user's factory method to create the enemy
    enemy = factory.create_enemy(difficulty)

    # Output in the specified format
    if enemy is not None:
        print(f"Enemy Type: {enemy.get_type()}")
        print(f"Health: {enemy.get_health()}")
        print(f"Speed: {enemy.get_speed()}, Attack Power: {enemy.get_attack_power()}")

if __name__ == "__main__":
    main()  