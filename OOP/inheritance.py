#parent class
class Animal():

    def move(self):
        print("walk")
    
    def sound(self):
        pass
# child class
class Dog(Animal):
    pass
# child class
class Snake(Animal):
    def move(self):
        print("crawl")

dog = Dog()
snake = Snake()
dog.move()
snake.move()