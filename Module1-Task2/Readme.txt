SmartCafe Assistant is a console-based chatbot that answers customer questions about menu items, ingredients, nutrition, prices,
 and working hours using only local data from a JSON file. It simulates a multi-agent design using Object-Oriented Programming.

##################
ResearchAgent Class
##################
Handles all interactions with the cafe_data.json file. It acts as the "data brain" of the assistant.

Key Methods:

__init__(): Loads and parses the local JSON file.

find_item_name(): Finds the correct item name (case-insensitive).

get_ingredients(): Returns the list of ingredients for a menu item.

get_price(): Returns the price in USD.

get_calories(): Returns calorie content.

get_sugar(): Returns sugar content in grams.

get_all_hours(): Returns the full weekly schedule.

get_hours(day): Returns opening hours for a specific day.

get_drinks(): Returns the list of available drinks.


##################
ChatBotAgent Class
##################

Handles the user interface — taking input from the user, parsing it, and displaying the correct responses by querying the ResearchAgent.

Key Methods:

__init__(): Initializes the agent and connects it with a ResearchAgent instance.

greet_user(): Prints a welcome message when the assistant starts.

run(): Main loop that keeps the bot running until the user types exit or quit.

handle_query(query): Uses regex to detect the user's input, then calls the right method from ResearchAgent.

ex:   
# in the Full menu check
if re.search(r"(what|which)(?: [\w]+)* (products|items|menu)", query, re.IGNORECASE)

The pattern is explained as follows:
(what|which)           # must include "what" or "which"
(?: [\w]+)*            # optionally followed by any number of words (like "are", "your", etc.)
(products|items|menu)  # must include "products", "items", or "menu"
So this section answers questions like:
This section answers questions like:

“What products do you have?”

“Which items are on the menu?”

“What menu options are available?”


# Sleman Khadoor
