teta_0 = 0
teta_1 = 0

def estimate_price(mileage):
    return  teta_0 + (teta_1 * mileage)

def normalize(inp):
    lst = []
    for i in inp:
        i = (i - min(inp)) / (max(inp) - (min(inp)))
        lst.append(i)
    return lst

def train():
    global teta_0, teta_1

    km = []
    price = []
    with open('data.csv', 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            km.append(float(parts[0]))
            price.append(float(parts[1]))
    lenght = len(km)

    km = normalize(km)
    price = normalize(price)

    for _ in range(30):
        teta_0_temp = 0.01 * (1/lenght) * sum(
            (estimate_price(km[i]) - price[i])
            for i in range(lenght)
        )
        teta_1_temp = 0.01 * (1/lenght) * sum(
            (estimate_price(km[i]) - price[i]) * km[i]
            for i in range(lenght)
        )
    teta_0 = teta_0 - teta_0_temp
    teta_1 = teta_1 - teta_1_temp
    
    with open('train.txt', 'w') as file:
        file.write(str(teta_0))
        file.write('\n')
        file.write(str(teta_1))
    
def main():
    train()

if __name__ == '__main__':
    main()