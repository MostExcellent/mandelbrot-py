from PIL import Image
from helpers import *
from math import log, sqrt
from datetime import datetime
from argparse import ArgumentParser

def mandelbrot(myX, myY, zoom, width, height):
    """
    Generates a Mandelbrot set image based on the specified parameters.

    Args:
        myX (float): X coordinate of the center of the plot.
        myY (float): Y coordinate of the center of the plot.
        zoom (int): Zoom level of the plot.
        width (int): Width of the plot.
        height (int): Height of the plot.

    Returns:
        PIL.Image.Image: Image representing the Mandelbrot set.

    """
    maxiter = zoom * 50  # number of iterations before escape
    xFocus = (myX + (1.75 / zoom))
    yFocus = -(myY + (-1 / zoom))
    pixels = []
    for i in range(height):
        for n in range(width):
            cX = mapRange(n, 0, width, -3.5 / zoom, 0) + xFocus
            cY = mapRange(i, 0, height, -2 / zoom, 0) + yFocus
            x = 0
            y = 0
            iteration = 0
            while x * x + y * y < 2 * 2 and iteration < maxiter:
                xtemp = x * x - y * y + cX
                y = 2 * x * y + cY
                x = xtemp
                iteration += 1
            if iteration == maxiter:
                pixels.append((0, 0, 0))
            else:
                mu = float(iteration) - log(log(sqrt(x * x + y * y))) / log(2) + 1  # normalized iteration count
                iCpct = float(mu / maxiter)
                iC = iCpct * 254
                c1 = int(iC)
                c2 = c1 + 1
                t = int(mapRange(linterp(c1, c2, int(mu % 1)), 0, 256, 1, 255))
                pixels.append(colorMap(t))
    return imgFromTuples('RGB', (width, height), pixels)

if __name__ == '__main__':
    ts = datetime.now()
    parser = ArgumentParser()
    parser.add_argument("x", type=float, help="x coordinate of the center of the plot", nargs='?', default=-0.75)
    parser.add_argument("y", type=float, help="y coordinate of the center of the plot", nargs='?', default=0.0)
    parser.add_argument("zoom", type=int, help="Zoom level of the plot", nargs='?', default=1)
    parser.add_argument("w", type=int, help="Width of the plot", nargs='?', default=480)
    parser.add_argument("h", type=int, help="Height of the plot", nargs='?', default=720)
    parser.add_argument("filename", type=str, help="Specify a filename for the output", nargs='?', default="mandelbrot")
    args = parser.parse_args()
    print(str(args.x) + ", " + str(args.y) + ", " + str(args.zoom) + ", " + str(args.w) + ", " + str(
        args.h) + ", " + args.filename + ".tiff")
    plot = mandelbrot(args.x, args.y, args.zoom, args.w, args.h)
    plot.save(args.filename + ".tiff")
    print("Done!")
    print("Finished in {} milliseconds".format(int((datetime.now() - ts).total_seconds() * 1000)))
