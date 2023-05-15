# Exchanger 
# in: Amount getting exchanged.
# out: Amount returned in the form of coins and banknotes.

def exchange(amount, banknote):
    return int(amount // banknote) # // does whole numbers not decimal


# get_exchange_dict
# in: Takes the amount paid and the price of the product
# out: returns a dictionary that includes the amount of banknotes/coins in each type of banknote/coin
def get_exchange_dict(inamount, price):
    amount_coins, money_back = 0, 0 

    banknotes_coins_dict = {500: 0,
                            100: 0,
                            50: 0,
                            20: 0,
                            10: 0,
                            5: 0}
    
    # 500 
    money_back = inamount - price 
    amount_coins = exchange(money_back, 500)
    money_back = money_back % 500 
    banknotes_coins_dict[500] = amount_coins
    print(f"\t\tBanknotes back: {str(amount_coins)}")

    return banknotes_coins_dict
