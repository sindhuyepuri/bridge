import sys
from matplotlib.pyplot import *
import numpy as np
import argparse

def vert_parabola(x1, y1, x2, y2, x3, y3, STEP):
    # Solve for the coefficients of the parabola
    A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])
    b = np.array([y1, y2, y3])
    a, b, c = np.linalg.solve(A, b)

    # Generate x-values for the parabola
    x = np.linspace(min(x1, x2, x3), max(x1, x2, x3), 100)

    # Generate y-values for the parabola
    y = a*x**2 + b*x + c

    # Plot the parabola
    plot(x, y)

    x_val = []
    y_val = []
    for x_point in np.arange(-210, 0, STEP):
        y_point = a*x_point**2 + b*x_point + c
        x_val.append(x_point)
        y_val.append(y_point)

    index = len(x_val)

    for x_point in np.arange(210, 0, -STEP):
        y_point = a*x_point**2 + b*x_point + c
        x_val.insert(index, x_point)
        y_val.insert(index, y_point)
    
    return x_val, y_val

def horiz_parabola(x1, y1, x2, y2, x3, y3, STEP):
    # Solve for the coefficients of the parabola
    A = np.array([[y1**2, y1, 1], [y2**2, y2, 1], [y3**2, y3, 1]])
    b = np.array([x1, x2, x3])
    a, b, c = np.linalg.solve(A, b)

    # Generate x-values for the parabola
    y = np.linspace(min(y1, y2, y3), max(y1, y2, y3), 100)

    # Generate y-values for the parabola
    x = a*y**2 + b*y + c

    # Plot the parabola
    plot(x, y)

    x_val = []
    y_val = []

    halfway = (min(y1, y2, y3) + max(y1, y2, y3))/2
    for y_point in np.arange(min(y1, y2, y3), halfway, STEP):
        x_point = a*y_point**2 + b*y_point + c
        x_val.append(x_point)
        y_val.append(y_point)
    
    index = len(x_val)

    for y_point in np.arange(max(y1, y2, y3), halfway, -STEP):
        x_point = a*y_point**2 + b*y_point + c
        x_val.insert(index, x_point)
        y_val.insert(index, y_point)

    return x_val, y_val

def generate_pslg():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="output poly file name")
    parser.add_argument("step", type=float, help="step width along bridge")
    args = parser.parse_args()
    STEP = args.step
    OUTPUT = args.filename

    x1_points, y1_points = vert_parabola(-210, 123, 0, 56, 210, 123, STEP)
    x2_points, y2_points = horiz_parabola(210, 71, 163.4, 28, 210, -15, STEP)
    y2_points.reverse()
    x3_points, y3_points = vert_parabola(-210, -67, 0, 0, 210, -67, STEP)
    x3_points.reverse()
    x4_points, y4_points = horiz_parabola(-210, 71, -163.4, 28, -210, -15, STEP)

    # generate pslg
    with open(OUTPUT, 'w') as sys.stdout:
        print("%d 2 0 0" % (len(x1_points) + len(x2_points) + len(x3_points) + len(x4_points)))

        index = 1
        for i in range(len(x1_points)):
            print("    %d   %f %f" % (index, x1_points[i], y1_points[i]))
            index += 1

        for i in range(len(x2_points)):
            print("    %d   %f %f" % (index, x2_points[i], y2_points[i]))
            index += 1

        for i in range(len(x3_points)):
            print("    %d   %f %f" % (index, x3_points[i], y3_points[i]))
            index += 1

        for i in range(len(x4_points)):
            print("    %d   %f %f" % (index, x4_points[i], y4_points[i]))
            index += 1
        index -= 1

        print("%d 0" % (index))
        for i in range(1, index):
            print("    %d   %d %d" % (i, i, i + 1))
        print("    %d   %d %d" % (index, index, 1))
        print(0)
    
def envelope(x1, y1, x2, y2, x3, y3):
    A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])
    b = np.array([y1, y2, y3])
    a, b, c = np.linalg.solve(A, b)

    # Generate x-values for the parabola
    x = np.linspace(min(x1, x2, x3), max(x1, x2, x3), 100)

    # Generate y-values for the parabola
    y = a*x**2 + b*x + c
    return x, y

# x_in, z_in = envelope(-210, 0, 0, 49, 210, 0)
# plot(x_in, z_in, label='extrados')
# x_ex, z_ex = envelope(-140, 0, 0, 28, 140, 0)
# plot(x_ex, z_ex, label='intrados')
# xlabel('x-axis')
# ylabel('z-axis')
# legend()
# show()

generate_pslg()