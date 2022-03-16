import matplotlib.pyplot as plt
import numpy as np


def surface_plot(x, y, z, function_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='turbo')
    plt.title(f'{function_name} surface plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def contour_plot(x, y, z, function_name):
    fig, ax = plt.subplots()
    ax.contourf(x, y, z, 50, cmap='turbo')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f'{function_name} contour plot')
    plt.show()


def himmelblau_function():
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    x, y = np.meshgrid(x, y)
    result = (x**2+y-11)**2 + (x+y**2-7)**2
    surface_plot(x, y, result, 'Himmelblau')
    contour_plot(x, y, result, 'Himmelblau')


def ackley_function():
    x = np.arange(-35, 35, 0.1)
    y = np.arange(-35, 35, 0.1)
    x, y = np.meshgrid(x, y)
    result = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x) +
                                                                               np.cos(2 * np.pi * y))) + np.e + 20
    surface_plot(x, y, result, 'Ackley')
    contour_plot(x, y, result, 'Ackley')


himmelblau_function()
ackley_function()