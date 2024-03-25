import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 5  # Number of bits
Vref = 5.0  # Reference voltage
Vin_max = Vref  # Maximum input voltage
Vin_min = 0.0  # Minimum input voltage

# Generate input voltages
Vin_values = np.linspace(Vin_min, Vin_max, 2**N)

# Generate ideal output codes
ideal_codes = np.arange(2**N)

# Generate simulated output codes
simulated_codes = np.zeros_like(ideal_codes)

# Simulate Flash ADC operation
for i, Vin in enumerate(Vin_values):
    code = 0
    for j in range(N):
        if Vin >= (j + 0.5) * (Vref / 2**N):
            code |= 1 << (N - 1 - j)
    simulated_codes[i] = code

# Calculate INL and DNL
ideal_digital_output = Vin_values * ((2**N) / Vref)
INL = simulated_codes - ideal_digital_output
DNL = np.diff(INL)

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# INL plot
axs[0].plot(Vin_values, INL)
axs[0].set_title('Integral Non-Linearity (INL)')
axs[0].set_xlabel('Input Voltage (V)')
axs[0].set_ylabel('INL (LSBs)')
axs[0].grid(True)

# DNL plot
axs[1].stem(Vin_values[:-1], DNL, markerfmt='bo', basefmt='k-')
axs[1].set_title('Differential Non-Linearity (DNL)')
axs[1].set_xlabel('Input Voltage (V)')
axs[1].set_ylabel('DNL (LSBs)')
axs[1].grid(True)

plt.tight_layout()
plt.show()