# Function to read valid numeric number from user
def read_number_input(sentence):
    """
    The function Prompts the user to enter a number. Repeats until valid input is provided.
    It handles non numerical values, negative values and empty values
    It returns A valid float number
    """
    while (True):
        num = input(sentence).strip()
        try:
            result = float(num)
            if result < 0:
                print("<!> You entered a negative number. Please enter a non-negative number.")
                continue
        except ValueError:
            print("<!> Your did not enter a number ")
        else:
            break
    return result


#----------------------------------------------------------------------

# Function to greet users when they start using the app
def greet_user():
    print("---------------------------------------------")
    print("  Welcome to your Dorm Budget Assistant ^_^")
    print("---------------------------------------------")
    student_name = input("Please Enter your full name:  ")
    print("")
    print(f"Thank you {student_name}, I am gonna help you with your budget planning")
    print("")
    return student_name


#----------------------------------------------------------------------
# Function to collect the amount spent on each category and it returns a list 
def collect_expenses(categories):
    print("How much did you spend on these categories: ")
    expenses = {}
    for category in categories:
        expense = read_number_input(f"{category}: ")
        expenses [category] = expense
    return expenses

#----------------------------------------------------------------------
#This function set the categories users spent their money on
def get_categories():
    default_categories = ["Food", "Transportation", "Rent or Housing", "Internet and Utilities", "Entertainment"]
    categories =[]
    print("These are the default categories: ")
    print("Food, Transportation, Rent or Housing, Internet and Utilities, Entertainment")
    choice = input("Do you want to add new categories instead ?    (y or n)    ").strip().lower()
    if choice == "n":
        return default_categories
    else:
        print("\nPlease Enter your categories one by one. Type 'done' when finished.")
        while True:
            category = input("> ").strip()
            if category.lower()== "done":
                break
            elif category != "":
                categories.append(category)
            else:
                print("Category name cannot be empty")
    if len(categories) == 0:
        print("You didn't enter your categories so we are gonna use the default ones")
        return default_categories
    return categories

#----------------------------------------------------------------------

student_name = greet_user()
monthly_budget = read_number_input("Please Enter your monthly budget:  ")
print("")
categories = get_categories()
expenses = collect_expenses(categories)
print("")
total_amount_spent = sum(expenses.values())
remaining_balance = monthly_budget - total_amount_spent
print("")
print (f"Total amount spent: {total_amount_spent:.2f}")
print (f"Remaining balance : {remaining_balance:.2f}")
print("")
if remaining_balance >= (0.2 * monthly_budget):
    print("^_^  Great job you are still within the budget")
elif remaining_balance >= 0:
    print("<<!>> WARNING : You are approaching within your budget limit")
else:
    print("<<X>> You’ve exceeded your budget. Be cautious!")
