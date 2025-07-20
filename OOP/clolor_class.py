class Color():
    def black ( self ):
        print("black")

    def red ( self ):
        print("red")


color =Color()
color.black()
color.red()

color.blue ="blue" # adding attribute to this object only
print(color.blue)