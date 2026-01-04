teta_0 = 0
teta_1 = 0

def estimate_price(mileage):
    return teta_0 + (teta_1 * mileage)

def training_module():
    global teta_0, teta_1
    km = []
    price = []
    with open('data.csv', 'r') as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            km.append(float(parts[0]))
            price.append(float(parts[1]))
    size = len(km)
    for _ in range(1000):
        error_teta0 = 0.001 * (1/size) * sum(
            estimate_price(km[i]) - price[i]
            for i in range(size)
        )
        error_teta1 = 0.001 * (1/size) * sum(
            estimate_price((km[i]) - price[i]) * km[i]
            for i in range(size)
        )
        teta_0 = teta_0-error_teta0
        teta_1 = teta_1-error_teta1
    print(teta_0)
    print(teta_1)
    return (teta_0, teta_1)
