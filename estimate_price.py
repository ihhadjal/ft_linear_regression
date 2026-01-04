import training_module

def code():
    while (1):
        try:
            mileage = float(input("Please enter the mileage wished for your car: "))
            training_module.training_module()
            estimated_price = training_module.teta_0 + (training_module.teta_1 * mileage)
            print('the estimated price for your car is:', estimated_price)
            break
        except ValueError:
            print("enter a valid mileage")

def main():
    code()

if __name__ == "__main__":
    main()