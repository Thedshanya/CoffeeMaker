MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit=0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    
}


def billForCoffee(drink):
    print(f"Bill for {drink}:")
    penny=int(input("How many penny?")) * 0.01
    dime=int(input("How many Dime?")) * 0.10
    nickel=int(input("How many Nickel?")) * 0.05
    quarter=int(input("How many Quarter?")) * 0.25
    amount=penny+dime+nickel+quarter
    rate=MENU[drink]["cost"]
    if amount<rate:
        return f"Money is insufficient to fetch {drink}.Your money is refunded"
    elif amount>rate:
        # profit+=rate
        return f"Your balance amount is ${amount-rate}. Enjoy ur {drink}"
    else:
        return f"Enjoy your {drink}"
         




def check_resource(drink,resources,MENU):
    for ing in MENU[drink]["ingredients"]:
        # print(MENU[drink]["ingredients"])
        if resources[ing]<MENU[drink]["ingredients"][ing]:
            print(resources[ing],MENU[drink]["ingredients"][ing])
            # print(f"{resources[ing]}:{MENU[drink]["ingredients"][ing]}")
            return (f"{ing} is not sufficient to make {drink}")
        
    for ing in resources:
        if ing in MENU[drink]["ingredients"]:
            resources[ing]-=MENU[drink]["ingredients"][ing]
            # print("***")
            # print(resources[ing],MENU["latte"]["ingredients"][ing])
            # print("***")
    return billForCoffee(drink)
        

    


avail_drinks=[]
avail_drinks=["espresso","latte","cappuccino"]


tocontinue=True

while tocontinue:

    choice=input("What would you like to have (espresso/latte/cappuccino): ").lower()
    if choice=="report":
        for key in resources:
            print(f"{key}:{resources[key]}")
        print(f"profit:{profit}")
    elif choice not in avail_drinks:
        print("sorry. The drink is not available")
    else:
        profit+=MENU[choice]["cost"]
        # print(profit)
        print(check_resource(choice,resources,MENU))
    # for ing in resources:
    #     print(f"{ing}:{resources[ing]}")

