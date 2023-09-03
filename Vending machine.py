items = {
    "1": {
        "1": 30,
        "2": 30,
        "3": 30,
        "4": 30,
        "5": 30,
        "cost": 20,
    },
    "2": {
        "1": 15,
        "2": 15,
        "3": 15,
        "4": 15,
        "5": 15,
        "cost": 10,
    }
}


def money(costs):
    global total
    total += int(input('How many Tens: '))*10
    if total < costs:
        total += int(input('How many Twenties: '))*20
        if total < costs:
            total += int(input('How many fifty: '))*50
            if total < costs:
                total += int(input('How many hundreds: '))*100
    return change()


def change():
    global profit
    if total > cost:
        profit += cost
        return total-cost
    elif total < cost:
        return -1
    profit += cost
    return 0


def check_items(user_choices):
    items_absent = []
    for j in user_choices:
        items[str(choice)][str(j)] -= 1
        if items[str(choice)][str(j)] < 0:
            items_absent.append(j)
    return tuple(items_absent)


def greeting():
    if choice == 1:
        print("Enjoy Your Drinks.")
    else:
        print("Enjoy Your snack.")
    print("Please Visit Us again next time.")


soft_drink = ["1.Coca-cola", "2.Pepsi    ", "3.Thumbs-up ", "4.String   ", "5.7-Up     "]
snack = ["1.Lays      ", "2.Kurkure   ", "3.Bingo     ", "4.Bhujia    ", "5.Mad Angles"]

profit = 0
total = 0
while True:
    choice = int(input("1)soft_drinks\n2)snacks\nEnter Your Choice : "))
    if choice == 1:
        print("Drinks     \t\t|\tCost")
        for i in soft_drink:
            print(i, "\t-\t", items[str(choice)]["cost"])
    elif choice == 2:
        print("snacks     \t\t|\tCost")
        for i in range(len(snack)):
            print(snack[i], "\t-\t", items[str(choice)]["cost"])
    elif choice == 1298:
        print(f"Profit = {profit}")
    if choice == 1 or choice == 2:
        user_choice = list(map(int, input("Enter What u want in this format(1 1 2 3): ").split()))
        items_absents = check_items(user_choice)
        len_items_absents = len(items_absents)
        cost = items[str(choice)]["cost"] * (len(user_choice) - len_items_absents)
        if len(user_choice) == len_items_absents:
            print("Sorry 😔 we have nothing in our vending machine that u have asked for.")
        elif len_items_absents >= 0:
            if len_items_absents > 0:
                print(f"Sorry 😔 {items_absents} is not present in our vending machine.")
            print(f"Your total bill for ordered items is {cost}")
            money_back = money(cost)
            if money_back == 0:
                greeting()
            elif money_back == -1:
                print(f"Sorry that's not enough money for what is have ordered collect your {total} in return box.")
            else:
                print(f"You have paid {money_back} extra collect your money back in the return box.")
                greeting()

