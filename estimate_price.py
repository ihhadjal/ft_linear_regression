import training_module


def estimate_price(mileage):
    with open('train.txt', 'r') as file:
        lines = file.readline()
        teta_0 = float(lines[0].strip())
        teta_1 = float(lines[1].strip())
        return teta_0 + (teta_1 * mileage)

def code():
    while(1):
        try:
            mileage = float(input("insert a mileage: "))
            estimate = float(estimate_price(mileage))
            print("The estimated price is:")
            break
        except ValueError:
            print("please insert a valid value!")

def main():
    code()
if __name__ == "__main__":
    main()