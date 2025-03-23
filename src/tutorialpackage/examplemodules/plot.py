import matplotlib.pyplot as plt
import numpy as np


def quickplot_sine():
    # Generate the data for the plot.
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    # Setup and display the plot.
    fig, ax = plt.subplots()
    fig.suptitle('A simple sine wave')
    ax.plot(x, y)
    ax.set_xlabel('Angle [rad]')
    ax.set_ylabel('Amplitude')
    plt.show()