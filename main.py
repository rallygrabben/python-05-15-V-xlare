import os 
import exchanger

def main():
    os.system("cls" if os.name != "NT" else "clear")

    print("\n\t------------------------------Exchange------------------------------")

    price = input("\n\t\tInput the price of the product:")

    os.system("cls" if os.name != "NT" else "clear")
    print("\n\t------------------------------Exchange------------------------------")

    print(f"\n\t\t{price} kr")
    payment = input("\n\t\tInput the amount paid:")

    exchangeNow(int(price), int(payment))


def exchangeNow(price, payment):
    if price > payment:
        print("\n\t\t You paid too little")

    else:
        exchange_back_dict = exchanger.get_exchange_dict(payment, price)
        print("\n\n\t\tExchange back:")
        print(f"\t\tAmount of 500: {str(exchange_back_dict[500])}")
        


main()