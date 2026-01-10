import numpy as np
import pandas
import matplotlib.pyplot as plt

teta_0 = 0
teta_1 = 0

ecart = 0
average = 0

def estimate_price(mileage):
    return  teta_0 + (teta_1 * mileage)

def normalize(inp):
    global ecart, average

    inp = np.array(inp)
    ecart = np.std(inp)
    average = np.mean(inp)

    return (inp - average) / ecart

def train():
    global teta_0, teta_1

    km = []
    price = []
    try:
        df = pandas.read_csv("data.csv")
        df["km"] = pandas.to_numeric(df["km"], errors="raise")
        df["price"] = pandas.to_numeric(df["price"], errors="raise")
    except (ValueError, pandas.errors.EmptyDataError):
        print("the value inserted in the dataset is not valid / it's empty")
        exit(1)
    with open('data.csv', 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            km.append(float(parts[0]))
            price.append(float(parts[1]))
    lenght = len(km)
    km_normalized= normalize(km)
    km_ecart = ecart
    km_average = average

    price_normalized = normalize(price)
    price_ecart = ecart
    price_average = average

    for _ in range(10000):
        teta_0_temp = 0.1 * (1/lenght) * sum(
            (estimate_price(km_normalized[i]) - price_normalized[i])
            for i in range(lenght)
        )
        teta_1_temp = 0.1 * (1/lenght) * sum(
            (estimate_price(km_normalized[i]) - price_normalized[i]) * km_normalized[i]
            for i in range(lenght)
        )
        teta_0 = teta_0 - teta_0_temp
        teta_1 = teta_1 - teta_1_temp
    
    predicted_prices = []

    for i in range(lenght):
        price_normalized_predicted = estimate_price(km_normalized[i])
        real_price = (price_normalized_predicted * price_ecart) + price_average
        predicted_prices.append(real_price)

    plt.scatter(km, price, color='blue', label='Données réelles')
    plt.plot(km, predicted_prices, color='red', label="régression linéaire")
    plt.xlabel('kilometrage')
    plt.ylabel('prix')
    plt.legend()
    plt.show()

    with open('train.txt', 'w') as file:
        file.write(str(teta_0) + '\n')
        file.write(str(teta_1) + '\n')
        file.write(str(km_ecart) + '\n')      
        file.write(str(km_average) + '\n')    
        file.write(str(price_ecart) + '\n')   
        file.write(str(price_average))
    
def main():
    train()

if __name__ == '__main__':
    main()
