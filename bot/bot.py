import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv')

price = df['Close'].iloc[-10000:-1:10].to_numpy()
size = price.shape


direction = np.zeros(size, dtype=int)

prev = 0
for idx, value in enumerate(price):
    if value > prev:
        direction[idx] = 255
    prev = value


fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(price)
ax2.plot(direction)

