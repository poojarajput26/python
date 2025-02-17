import matplotlib.pyplot as plt
import random
import time

# Initializing data lists
time_intervals = []
stock_prices = []

# Set interactive mode for real-time plotting
plt.ion()
fig, ax = plt.subplots()

# Simulating stock price changes over 20 intervals
for t in range(1, 21):  # Time intervals from 1 to 20
    time_intervals.append(t)
    
    # Generating stock price: starting from 100 and fluctuating randomly
    if len(stock_prices) == 0:
        stock_prices.append(100)  # Initial stock price
    else:
        change = random.uniform(-5, 5)  # Random fluctuation
        stock_prices.append(stock_prices[-1] + change)
    
    # Clearing and re-plotting the updated data
    ax.clear()
    ax.plot(time_intervals, stock_prices, marker='o', color='b')
    plt.xlabel('Time (Intervals)')
    plt.ylabel('Stock Price')
    plt.title('Real-Time Stock Price Visualization')
    plt.grid(True)  # Add a grid for better visualization
    plt.pause(0.5)  # Pause for half a second to simulate real-time update

# Stop interactive mode and finalize the plot
plt.ioff()
plt.show()