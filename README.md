# Linear Regression - Price Estimation

A simple linear regression implementation to predict car prices based on mileage.

## Description

This project implements a linear regression algorithm from scratch to estimate car prices using mileage data. The model uses gradient descent with feature normalization for training, and includes visualization of the regression line against the actual data points.

## Files

- `training_module.py` - Training algorithm with normalization and visualization
- `estimate_price.py` - Price estimation interface
- `data.csv` - Training dataset (mileage and price pairs)
- `train.txt` - Saved model parameters
- `requirements/req.txt` - Project dependencies

## Requirements

Install the required dependencies:

```bash
pip install -r requirements/req.txt
```

Dependencies include:

- numpy
- pandas
- matplotlib

## Usage

### Training the Model

```bash
python training_module.py
```

This reads the dataset from `data.csv`, trains the model, and:

- Displays a visualization showing the data points and regression line
- Saves the trained parameters to `train.txt`

### Estimating Prices

```bash
python estimate_price.py
```

Enter a mileage value when prompted to get the estimated price. The program will:

- Load the trained model parameters
- Normalize the input using saved statistics
- Return the denormalized price prediction

## Algorithm

The implementation uses:

- **Feature normalization** (standardization) for both input and output
  - Normalizes mileage and price using mean and standard deviation
  - Improves gradient descent convergence
- **Gradient descent optimization**
  - 10,000 training iterations
  - Learning rate of 0.1
- **Visualization**
  - Scatter plot of actual data points
  - Linear regression line overlay

## Model Parameters

The trained model saves to `train.txt`:

- `theta_0`: intercept (in normalized space)
- `theta_1`: slope coefficient (in normalized space)
- `km_ecart`: standard deviation of mileage
- `km_average`: mean of mileage
- `price_ecart`: standard deviation of price
- `price_average`: mean of price

## Visualization

The training module generates a graph showing:

- Blue scatter points: actual data (mileage vs price)
- Red line: fitted linear regression model
- Axes labeled in French: "kilometrage" (mileage) and "prix" (price)
