import matplotlib.pyplot as plt
import numpy as np
import random


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


def himmelblau_plot():
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    x, y = np.meshgrid(x, y)
    result = (x**2+y-11)**2 + (x+y**2-7)**2
    surface_plot(x, y, result, 'Himmelblau')
    contour_plot(x, y, result, 'Himmelblau')


def ackley_plot():
    x = np.arange(-35, 35, 0.1)
    y = np.arange(-35, 35, 0.1)
    x, y = np.meshgrid(x, y)
    result = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x) +
                                                                               np.cos(2 * np.pi * y))) + np.e + 20
    surface_plot(x, y, result, 'Ackley')
    contour_plot(x, y, result, 'Ackley')


def ackley_calculator(values):  # calculate function value for the list of two arguments
    x = values[0]
    y = values[1]
    result = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x) +
                                                                               np.cos(2 * np.pi * y))) + np.e + 20
    return result


def himmelblau_calculator(values):  # calculate function value for the list of two arguments
    x = values[0]
    y = values[1]
    result = (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2
    return result


def check_arguments(arguments, min_value, max_value):  # check that arguments are inside given range
    check_status = True
    for i in range(len(arguments)):
        if arguments[i] < min_value or arguments[i] > max_value:
            check_status = False
    return check_status


def hooke_jeeves(step, minimal_step, step_decrease, initial_arguments, current_arguments, function, number_of_iterations, min_value, max_value, no_min_found_iteration=1):

    if step < minimal_step:  # if current step lower than minimal_step - stop of algorithm loop
        print("--------------------------------------------------------")
        print("Step value is lower than minimal step")
        print(f"Total iterations: {number_of_iterations}")
        print(f"Iteration number that found lowest value: {no_min_found_iteration}")
        print(f"Initial arguments x:{initial_arguments[0]}, y:{initial_arguments[1]} = {function(initial_arguments)}")
        print(f"Current arguments x:{current_arguments[0]}, y:{current_arguments[1]} = {function(current_arguments)}")
        print(f"The result is better of: {function(initial_arguments)-function(current_arguments)}")
        app_menu()

    else:
        arguments = current_arguments[:]
        print("-----------------------------------------------------------------------------")
        print(f"Initial iteration no.{number_of_iterations} arguments x:{current_arguments[0]}, "
              f"y:{current_arguments[1]}. Function Value: {function(current_arguments)}")
        number_of_iterations += 1  # increase number of iterations
        new_arguments = arguments[:]  # temporary variable for list of arguments
        print("Exploratory moves:")
        for i in range(2):  # 2 directions - x and y arguments
            plus_arguments = new_arguments[:]  # variable for list of increased arguments
            minus_arguments = new_arguments[:]  # variable for list of decreased arguments
            plus_arguments[i] += step  # increase argument by the step
            minus_arguments[i] -= step   # decrease argument by the step
            function_value_minus = function(minus_arguments)  # calculate function value for decreased/increased arguments
            function_value_plus = function(plus_arguments)
            print(f"Function value for arguments x:{plus_arguments[0]} y:{plus_arguments[1]} = {function_value_plus}")
            print(f"Function value for arguments x:{minus_arguments[0]} y:{minus_arguments[1]} = {function_value_minus}")

            # check that arguments are in given range and new value is lower than previous value
            if function_value_plus < function(new_arguments) and check_arguments(plus_arguments, min_value, max_value):
                new_arguments = plus_arguments[:]
            if function_value_minus < function(new_arguments) and function_value_minus < function_value_plus and\
                    check_arguments(minus_arguments, min_value, max_value):
                new_arguments = minus_arguments[:]

        # if arguments are the same like previously - decrease step and run function again with new step
        if new_arguments == arguments:
            step /= step_decrease
            print(f"No better result in the given range. New step: {step}")
            hooke_jeeves(step, minimal_step, step_decrease, initial_arguments, arguments, function, number_of_iterations, min_value, max_value, no_min_found_iteration)

        working_step = []
        for i in range(2):
            working_step.append(new_arguments[i]-current_arguments[i])  # calculate values of working step
        print("-----------------------------------------------------------------------------")
        print("Pattern moves:")
        while True:
            working_step_arguments = [new_arguments[0]+working_step[0], new_arguments[1]+working_step[1]]  # Make pattern move
            function_value_after_ws = function(working_step_arguments)  # calculate function value after pattern move
            # print(f"Function arguments before Working Step: x:{new_arguments[0]}, y:{new_arguments[1]} = {function(new_arguments)}")
            # print(f"Function arguments after Working Step: x:{working_step_arguments[0]}, y:{working_step_arguments[1]} = {function_value_after_ws}")
            if function(new_arguments) <= function_value_after_ws:  # if value after pattern move is not lower - break the loop
                print("Working step failed! Function value is higher or equal")
                break
            else:  # if value after pattern move is lower - make next pattern move
                if check_arguments(working_step_arguments, min_value, max_value):
                    print(f"Working step passed. Function value is lower")
                    new_arguments = working_step_arguments[:]
                else:
                    print("Working step failed. Arguments are not in given range")
                    break
        # make next exploratory search after move:
        hooke_jeeves(step, minimal_step, step_decrease, initial_arguments, new_arguments, function, number_of_iterations, min_value, max_value, number_of_iterations-1)


def app_menu():
    while True:
        print("MENU")
        print("1. Plot Himmelblau function")
        print("2. Plot Ackley function")
        print("3. Calculate Himmelblau function")
        print("4. Calculate Ackley function")
        print("5. Hooke-Jeeves - Himmelblau optimization")
        print("6. Hooke-Jeeves - Ackley optimization")
        choice = input("Your choice: ")

        if choice == '1':
            himmelblau_plot()
        elif choice == '2':
            ackley_plot()
        elif choice == '3':
            print(himmelblau_calculator([3, 2]))
        elif choice == '4':
            print(ackley_calculator([0, 0]))
        elif choice == '5':
            hooke_jeeves(10, 0.01, 2, random.sample(range(-5, 5), 2), random.sample(range(-5, 5), 2), himmelblau_calculator, 1, -5, 5)
        elif choice == '6':
            hooke_jeeves(70, 0.01, 1.01, random.sample(range(-35, 35), 2), random.sample(range(-35, 35), 2), ackley_calculator, 1, -35, 35)
        else:
            break


app_menu()
