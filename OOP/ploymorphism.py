#parent class
class Animal():

    def move(self):
        print("walk")
    
    def sound(self):
        pass


# child class
class Dog(Animal):
    #override
    def move(self):
        print("run")
    
    def sound(self):
        print("bark")

    
# child class
class Snake(Animal):
    #override
    def move(self):
        print("crawl")

    def sound(self):
        print("hiss")

dog = Dog()
snake = Snake()
dog.move()
dog.sound()
snake.move()
snake.sound()
print("#-----------------#")
