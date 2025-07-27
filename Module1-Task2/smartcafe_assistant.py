import json
import re

# ResearchAgent Class
class ResearchAgent():
    # constructor
    def __init__( self, data_file ="cafe_data.json" ):
        try:
            with open(data_file,'r') as file:
                self.data = json.load(file)

        except Exception as e:
            print(f"Error Loading data: {e} ")
            self.data = {}

    # find item name (case-insensitive lookups)
    def find_item_name(self, item_name):
        # Return correct-cased item from menu, or None
        item_name = item_name.strip().lower()
        for name in self.data.get("menu", {}):
            if name.lower() == item_name:
                return name
        return None
    
    # get ingrediants of an item
    def get_ingredients(self,item):
        item = self.find_item_name(item)
        return self.data.get("menu",{}).get(item,{}).get("ingredients",None)

    # get price of an item
    def get_price(self,item):
        item = self.find_item_name(item)
        return self.data.get("menu",{}).get(item,{}).get("price_usd",None)
    
    # get calories of an item
    def get_calories(self,item):
        item = self.find_item_name(item)
        return self.data.get("menu",{}).get(item,{}).get("nutrition",{}).get("calories",None)
    
    # get how much sugar in an item
    def get_sugar(self,item):
        item = self.find_item_name(item)
        return self.data.get("menu",{}).get(item,{}).get("nutrition",{}).get("sugar_g",None)
    

    # get all working hours
    def get_all_hours(self):
        return self.data.get("opening_hours",None)
    
    # get working hours of a day
    def get_hours(self,day):
        day = day.capitalize()
        return self.data.get("opening_hours",{}).get(day,None)
    
    # get drinks
    def get_drinks(self):
        return self.data.get("drinks",[])
    

#------------------------------------------------------------------------

class ChatBotAgent:
    def __init__(self, researcher):
        self.researcher = researcher
        self.running = True

    # greet user at the beginning
    def greet_user(self):
        print("\n Welcome to SmartCafe Assistant!")
        print(" Feel Free to ask me about our menu items, prices, calories, sugar, ingredients, or working hours.")
        print(" Type 'exit' or 'quit' to leave.")

    # run the agent till the customer type exit or quit
    def run(self):
        self.greet_user()
        while self.running:
            query = input("\nYou: ").strip()
            if query.lower() in ["exit", "quit"]:
                self.running = False
                print("\n Goodbye! Enjoy your coffee!")
                return
            self.handle_query(query)

    #handle customer query
    def handle_query(self, query):

        # Full menu
        if re.search(r"(what|which)(?: [\w]+)* (products|items|menu)", query, re.IGNORECASE):
            items = self.researcher.get_drinks()
            print("\n Our menu includes:")
            for item in items:
                print(f" - {item}")
            return
        
        # Ingredients
        match = re.search(r"what(?:'s| is)? in (?:a |an )?(?P<item>[\w\s]+)", query, re.IGNORECASE)
        if match:
            item = match.group("item").title()
            ingredients = self.researcher.get_ingredients(item)
            if ingredients:
                print(f"\n {item} includes: {', '.join(ingredients)}.")
            else:
                print(f"\n Sorry, I couldn’t find ingredients for {item}.")
            return

        # Calories
        match = re.search(r"how many calories.*(?:in|for)\s+(?P<item>[\w\s]+)", query, re.IGNORECASE)
        if match:
            item = match.group("item").title()
            calories = self.researcher.get_calories(item)
            if calories is not None:
                print(f"\n {item} has {calories} calories.")
            else:
                print(f"\n Sorry, I couldn’t find calorie info for {item}.")
            return

        # Sugar
        match = re.search(r"how much sugar.*(?:in|for)\s+(?P<item>[\w\s]+)", query, re.IGNORECASE)
        if match:
            item = match.group("item").title()
            sugar = self.researcher.get_sugar(item)
            if sugar is not None:
                print(f"\n {item} contains {sugar}g of sugar.")
            else:
                print(f"\n Sorry, I couldn’t find sugar info for {item}.")
            return

        # Price
        match = re.search(r"(?:how much(?: does| is)?|what(?:'s| is) the price(?: of)?)\s+(?:a|an|the)?\s*(?P<item>[\w\s]+?)\s*(?:cost|price)?[?.!]*$", query, re.IGNORECASE)
        if match:
            item = match.group("item").title()
            price = self.researcher.get_price(item)
            if price is not None:
                print(f"\n The price of {item} is ${price:.2f}.")
            else:
                print(f"\n Sorry, I couldn’t find the price for {item}.")
            return

        # Single-day hours
        match = re.search(r"(when|what time).*?(open|work).*?\b(?:on\s)?(?P<day>monday|tuesday|wednesday|thursday|friday|saturday|sunday)", query, re.IGNORECASE)

        if match:
            day = match.group("day").capitalize()
            hours = self.researcher.get_hours(day)
            if hours:
                print(f"\n We’re open on {day} from {hours}.")
            else:
                print(f"\n Sorry, I couldn’t find hours for {day}.")
            return

        # All weekly hours
        if re.search(r"(what|which)? ?(working|opening)? ?hours", query, re.IGNORECASE):
            hours = self.researcher.get_all_hours()
            print("\n Our full weekly hours are:")
            for day, time in hours.items():
                print(f"  {day}: {time}")
            return

        # Available drinks
        if re.search(r"(what|which) drinks.*(have|available)", query, re.IGNORECASE):
            drinks = self.researcher.get_drinks()
            print(" \n We serve the following drinks:")
            for d in drinks:
                print(f" - {d}")
            return

        print(" Sorry, I didn’t understand that. Try asking about ingredients, calories, prices, or hours.")
              

    
#-------------------------------------------------------------------------

if __name__ == "__main__":
    # agent = ResearchAgent("cafe_data.json")
    # print(agent.data)  
    # print("")
    # print(agent.get_ingredients("carAmel latte"))
    # print (agent.get_calories("MAtcha Latte"))
    # print( agent.get_all_hours())
    # print(agent.get_hours("tHursDaY"))
    # print(agent.get_drinks())
    researcher = ResearchAgent("cafe_data.json")
    chatbot = ChatBotAgent(researcher)
    chatbot.run()