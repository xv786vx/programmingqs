class GameSettings:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            return super(GameSettings, cls).__new__(cls)

    
    def __init__(self):
            if not hasattr(self, 'initialized'):
                self.initialized = True
                self.volume = None
                self.difficulty = None
                self.resolution = None
                
        