from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Dukes"}
orders = []
def coffee_bot():
    welcome_message()
    order_taking(orders)
    receipt(orders)

    name = input("\nCan I get your name please? ")

    print("\nThanks, {}! Please proceed to the pick up counter for your order!".format(name))

#Welcome Message, called in main function
@app.get("welcome_message()")
async def welcome_message():
    print("Welcome to the Starbucks! \n\nToday's specials are Cherry Blossom Frappuccino and Nitro Cold Brew.")

#Order Taking, called in main function
@app.get("order_taking(orders")
async def order_taking(orders):
    size = get_size()
    temp_type = get_temp()
    drink_type = get_drink_type()
    cup_type = get_cup()
    quantity = get_quantity()
    orders.append([quantity, size, temp_type, drink_type, cup_type])
    print("\n" + str(orders))
    print("\nAlright, that\'s {} {} {} {} {}!".format(quantity, size, temp_type, drink_type, cup_type))
    addon_prompt()

#For Additional Orders, called in Order Taking function
@app.get("addon_prompt()")
async def addon_prompt():
    res = input("\nDo you wish to add another order? \n[a] Yes \n[b] No \n> ")
    res = res.lower()
    if res == "a":
        print("\nAlright, taking your new order!")
        return order_taking(orders)
    else:
        print("\nAlright, processing your orders now!")

#Error Message, used for invalid input
@app.get("error_message()")
async def error_message():
    print("\nI'm sorry, I did not understand your selection.\n\nPlease enter the corresponding letter for your response.")

#Order Summary, called in main function
@app.get("receipt(orders)")
async def receipt(orders):
    total_orders = range(1, (len(orders)+1))
    print("\nYou have placed " + str((len(orders))) + " orders. Your orders are: ")
    for order in orders:
        print(*order)

#Size Choice, called in Order Taking function
@app.get("get_size()")
async def get_size():
    res = input('\nWhat size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    res = res.lower()
    if res == "a":
        return "Small"
    elif res == "b":
        return "Medium"
    elif res == "c":
        return "Large"
    else:
        error_message()
        return get_size()

#Drink Choice, called in Order Taking function
@app.get("get_drink_type())")
def get_drink_type():
    res = input("\nWhat type of drink would you like?\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
    res = res.lower()
    if res == "a":
        return "Brewed Coffee"
    elif res == "b":
        return "Mocha"
    elif res == "c":
        return order_latte()
    else:
        error_message()
        return get_drink_type()

#Milk Component, called in Get_Drink_Type function
@app.get("order_latte()")
async def order_latte():
    res = input("\nAnd what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
    res = res.lower()
    if res == "a":
        return "Latte"
    elif res == "b":
        return "Non-fat Latte"
    elif res == "c":
        return "Soy Latte"
    else:
        error_message()
        return order_latte()

#Temp Choice, called in Order Taking function
@app.get("get_temp()")
async def get_temp():
    res = input("\nHow would you like your drink? \n[a] Hot \n[b] Iced \n> ")
    res = res.lower()
    if res == "a":
        return "Hot"
    elif res == "b":
        return "Iced"
    else:
        error_message()
        return get_temp()

#Cup choice, called in Order Taking function
@app.get("get_cup()")
async def get_cup():
    res = input("\nWhat type of cup would you like to use?\n[a] Dine-in Cup \n[b] Takeaway Cup \n[c] Your own Reusable Cup \n> ")
    res = res.lower()
    if res == "a":
        return "in a dine-in cup"
    elif res == "b":
        return "in a takeaway cup."
    elif res == "c":
        return "in your reusable cup."
    else:
        error_message()
        return get_cup()

#Quantity choice, called in Order Taking function
@app.get("get_quantity()")
async def get_quantity():
    res = input("\nWhat is quantity for this order? > ")
    try:
        res = int(res)
        return res
    except ValueError:
        print("\nInvalid input. Please enter a value quantity.")
        return get_quantity()

coffee_bot()

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
