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
        
        # if exchange_back_dict[500] >= 1:
        #     print(f"\t\tAmount of 500 notes: {str(exchange_back_dict[500])}")
        
        # if exchange_back_dict[100] >= 1:
        #     print(f"\t\tAmount of 100 notes: {str(exchange_back_dict[100])}")
        
        # if exchange_back_dict[50] >= 1:
        #     print(f"\t\tAmount of 50 notes: {str(exchange_back_dict[50])}")
        
        # if exchange_back_dict[20] >= 1:
        #     print(f"\t\tAmount of 20 notes: {str(exchange_back_dict[20])}")
        
        # if exchange_back_dict[10] >= 1:
        #     print(f"\t\tAmount of 10 coins: {str(exchange_back_dict[10])}")
        
        # if exchange_back_dict[5] >= 1:
        #     print(f"\t\tAmount of 5 coins: {str(exchange_back_dict[5])}")

        # if exchange_back_dict[1] >= 1:
        #     print(f"\t\tAmount of 1 coins: {str(exchange_back_dict[1])}")
        


        # loopVars = [500,100,50,20,10,5,1]

        for loopVar in exchange_back_dict:
            if exchange_back_dict[loopVar] >= 1:
                print(f"\t\tAmount of {loopVar} notes: {str(exchange_back_dict[loopVar])}")

main()