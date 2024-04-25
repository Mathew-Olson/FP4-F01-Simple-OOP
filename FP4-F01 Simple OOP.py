class Human:
    
    def __init__(self, first_name, last_name, height, eye_color, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.eye_color = eye_color
        self.gender = gender
    
    def walk(self):
        print(f"{self.first_name} is walking on two legs.")
    
    def info(self):
        print(f'{self.first_name} {self.last_name} is a {self.height} {self.gender} with {self.eye_color} eyes')
        
class Baby(Human):
    
    def walk(self):
        print(f"{self.first_name} can't walk on there legs yet")

###Main code###
Josh = Human('Josh', 'Walkman','6ft 2in', 'blue', 'boy')
James = Baby('James', 'Walkman', '1ft 9in', 'green', 'boy')
Sara = Human('Sara', 'Walkman', '5ft 9in', 'brown', 'girl')

Human.info(Josh)
Human.info(Sara)
Human.walk(Sara)
Baby.info(James)
Baby.walk(James)