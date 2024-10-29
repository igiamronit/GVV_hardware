import numpy as np
import matplotlib.pyplot as plt

# Set save paths for the plots
train_save_path = '/home/ronit/github/GVV_hardware/Hardware_assignmentv.2.0/train.png'
valid_save_path = '/home/ronit/github/GVV_hardware/Hardware_assignmentv.2.0/valid.png'

# Function to load data
def load_data(filename):
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1]  # Temperature (T) and Voltage (V)

# Function to fit a quadratic model using least squares
def fit_quadratic_model(T, V):
    # Define design matrix for a quadratic fit: 1, T, T^2
    X = np.vstack([np.ones(len(T)), T, T**2]).T
    # Solve for the coefficients using lstsq
    coefficients, _, _, _ = np.linalg.lstsq(X, V, rcond=None)
    return coefficients  # returns [v, av, bv]

# Function to evaluate the model
def evaluate_model(T, coefficients):
    v, av, bv = coefficients
    return v + av * T + bv * T**2

# Function to plot results
def plot_results(T, V_actual, V_predicted, save_path, title):
    plt.plot(T, V_actual, 'k.', label="Actual Data")
    plt.plot(T, V_predicted, 'r-', label="Model Prediction")
    plt.xlabel('Temperature ($^{\circ}$C)')
    plt.ylabel('Output Voltage (V)')
    plt.title(title)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# Load and fit the training data
T_train, V_train = load_data('training_data.txt')
coefficients = fit_quadratic_model(T_train, V_train)
V_train_predicted = evaluate_model(T_train, coefficients)
plot_results(T_train, V_train, V_train_predicted, train_save_path, 'Training Data Fit')

# Load and evaluate the validation data
T_val, V_val = load_data('validation_data.txt')
V_val_predicted = evaluate_model(T_val, coefficients)
plot_results(T_val, V_val, V_val_predicted, valid_save_path, 'Validation Data Fit')

# Display the model parameters
print("Model coefficients:")
print(f"Intercept (v): {coefficients[0]}")
print(f"Linear term (av): {coefficients[1]}")
print(f"Quadratic term (bv): {coefficients[2]}")

