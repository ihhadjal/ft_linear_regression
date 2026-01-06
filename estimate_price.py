import training_module as train
import numpy as np

def estimate_price(mileage):
    with open('train.txt') as file:
        lst = file.readlines()

    teta_0 = float(lst[0])
    teta_1 = float(lst[1])
    ecart = float(lst[2])
    average = float(lst[3])

    normalized_mileaged = (mileage - average) / ecart

    normalized_price_est = teta_0 + (teta_1 * normalized_mileaged)

    real_price = (normalized_price_est * ecart) + average

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