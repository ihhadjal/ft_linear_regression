# Linear Regression - Price Estimation

A simple linear regression implementation to predict car prices based on mileage.

## Description

This project implements a linear regression algorithm from scratch to estimate car prices using mileage data. The model uses gradient descent with feature normalization for training.

## Files

- `training_module.py` - Training algorithm and normalization functions
- `estimate_price.py` - Price estimation interface
- `data.csv` - Training dataset (mileage and price pairs)
- `train.txt` - Saved model parameters

## Usage

### Training the Model

```bash
python training_module.py
```

This reads the dataset from `data.csv` and saves the trained parameters to `train.txt`.

### Estimating Prices

```bash
python estimate_price.py
```

Enter a mileage value when prompted to get the estimated price.

## Algorithm

The implementation uses:
- Feature normalization (standardization) for both input and output
- Gradient descent optimization
- 10,000 training iterations
- Learning rate of 0.1

## Model Parameters

The trained model saves:
- theta_0: intercept
- theta_1: slope coefficient
- Normalization parameters (mean and standard deviation for mileage and price)
