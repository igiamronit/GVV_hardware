import numpy as np

# Example data as arrays
temperatures = [25.8, 31.4, 35.1, 44.8, 55.5, 67.8, 79.4]
voltages = [4.61, 4.62, 4.62, 4.63, 4.64, 4.65, 4.66]

# Combine into a 2D array (each row is a [temperature, voltage] pair)
data = np.column_stack((temperatures, voltages))

# Save the data to a text file
np.savetxt('valid_data.txt', data, fmt='%.2f')

