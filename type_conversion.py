oranges_with_me = 5
oranges_you_have = input("how many oranges do you have? ")
# we need to convert it beause input function will read it as a string
total_number_of_oranges = oranges_with_me + int(oranges_you_have)
print(total_number_of_oranges)
# other conversion functions : bool,   float,   str
print("Total number of oranges = " + str(total_number_of_oranges))