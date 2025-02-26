class Operation:
    def execute(self, string, index):
        raise NotImplementedError
    
class F(Operation):
    def __init__(self, steps):
        self.steps = steps
        
    def execute(self, string, index):
        new_i = min(index + self.steps, len(string)-1)
        return string, new_i
        
    
class B(Operation):
    def __init__(self, steps):
        self.steps = steps
    
    def execute(self, string, index):
        new_i = max(index - self.steps, 0)
        return string, new_i
    
class R(Operation):
    def __init__(self, char):
        self.char = char

    def execute(self, string, index):
        string[index] = self.char
        return string, index
    

class OperationHandler:
    def __init__(self):
        self.operations = []
    
    def parse_cmds(self, cmd_str):
        for i in range(len(cmd_str)):
            if cmd_str[i] == 'F':
                steps = 0
                while cmd_str[i].isdigit():
                    steps += int(cmd_str[j])
                    i += 1
                self.operations.append(F(steps))
            elif cmd_str[i] == 'B':
                steps = 0
                while cmd_str[i].isdigit():
                    steps += int(cmd_str[j])
                    i += 1
                self.operations.append(B(steps))
            elif cmd_str[i] == 'R':
                self.operations.append(R(cmd_str[i+1]))
                i += 1
    
    def apply_cmds(self, string):
        current_str, current_i = string, 0
        for cmd in self.operations:
            current_str, current_i = cmd.execute(current_str, current_i)
        return current_str
