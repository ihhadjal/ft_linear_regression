teta_0 = 0
teta_1 = 0

def training_module(mileage):
    with open('data.csv', 'r') as file:
        for line in file:
            parts = line.split(',')
            km = parts[0]
            price = parts[1]

def estimate_price():
    while (1):
        try:
            mileage = int(input("Please enter the mileage wished for your car: "))
            training_module(mileage)
            break
        except ValueError:
            print("enter a valid mileage")

def main():
    estimate_price()

if __name__ == "__main__":
    main()