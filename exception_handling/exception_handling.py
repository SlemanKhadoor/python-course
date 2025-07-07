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