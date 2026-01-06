import training_module as train
import numpy as np

def estimate_price(mileage):
    with open('train.txt') as file:
        lst = file.readlines()

    teta_0 = float(lst[0])
    teta_1 = float(lst[1])
    km_ecart = float(lst[2])
    km_average = float(lst[3])
    price_ecart = float(lst[4])
    price_average = float(lst[5])

    normalized_mileage = (mileage - km_average) / km_ecart

    normalized_price = teta_0 + (teta_1 * normalized_mileage)
    
    real_price = (normalized_price * price_ecart) + price_average

    return real_price

def code():
    while(1):
        try:
            mileage = float(input("insert a mileage: "))
            estimate = estimate_price(mileage)
            print("The estimated price is:", estimate)
            break
        except ValueError:
            print("please insert a valid value!")

def main():
    code()
if __name__ == "__main__":
    main()