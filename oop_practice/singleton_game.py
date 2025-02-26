# User will implement the GameSettings class as a Singleton
class GameSettings:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameSettings, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.volume = None
            self.difficulty = None
            self.resolution = None
    
    
    def  set_volume(self, value): 
        self.volume = value

    def  set_difficulty(self, value): 
        self.difficulty = value

    def  set_resolution(self, value): 
        self.resolution = value

    def  get_volume(self): 
        return self.volume

    def  get_difficulty(self): 
        return self.difficulty

    def  get_resolution(self): 
        return self.resolution


        
    

def main():
    settings = GameSettings() # Ensure singleton instance

    while True:
        try:
            command = input().strip().split()

            if command[0] == "set_volume":
                settings.set_volume(int(command[1]))
            elif command[0] == "set_difficulty":
                settings.set_difficulty(command[1])
            elif command[0] == "set_resolution":
                settings.set_resolution(command[1])
            elif command[0] == "get_volume":
                print(settings.get_volume())
            elif command[0] == "get_difficulty":
                print(settings.get_difficulty())
            elif command[0] == "get_resolution":
                print(settings.get_resolution())
        except EOFError:
            break

if __name__ == "__main__":
    main()