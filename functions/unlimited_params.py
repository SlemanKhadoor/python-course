def print_hello(*names):
    for name in names:
        print(f"hellp {name} ")
        print(names[0])


print_hello("first-test","ali","ahmed")

print("---------------")

print_hello("second-test","ali","ahmed","john","yousef")

