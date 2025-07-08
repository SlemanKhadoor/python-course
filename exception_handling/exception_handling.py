a = 5
try:
    print(t)
except:
    print("Something went wrong")
print("#-----------------------------------#")

a = 5
try:
    print(a)
except:
    print("Something went wrong")
print("#-----------------------------------#")

a = 5
try:
    print(y)
except NameError:
    print("Y is not defined")
except:
    print("Something went wrong")
print("#-----------------------------------#")

a = 5
try:
    print(a)
except:
    print("Something went wrong")
else:
    print("nothing went wrong")

print("#-----------------------------------#")
a = 5
try:
    print(j)
except:
    print("Something went wrong")
finally:
    print("finished")

print("#-----------------------------------#")

a = 5
b = 0
try:
    z=a/b
    print(z)
except ZeroDivisionError as e: 
    print(f"exception we faced {e} ")
except Exception as e:  # we used parent class Exception as we don't know what type we are gonna face
    print(f"exception we faced {e} ")
else:
    print("nothing went wrong")
finally:
    print("finished")


# if we know thar we may face different types of exceptions in the code we can use each one of them in an except block and provide the code needed to be done 