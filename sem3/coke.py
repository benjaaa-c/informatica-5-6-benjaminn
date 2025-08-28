def main() :
    price = 50
    total_paid = 0
    vending_machine(price, total_paid)



def vending_machine(price, total_paid):
    while price > 0:
        print(f"Amount due: {price, total_paid}")
        pay = int(input("insert coin: "))

        if pay == 25 or pay == 10 or pay == 5:
            price = price - pay 
            total_paid = total_paid + pay
        else:
            print("Not a coin")

    if total_paid >= 50:
        print("thanks buddy")
        print(f"here is your change: {total_paid-50}")
       
main()