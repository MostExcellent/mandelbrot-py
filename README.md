# Mandelbrot Set Generator

This program generates a visual representation of the Mandelbrot set based on user-defined parameters.

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library)

## Usage
To generate a Mandelbrot set image, run the following command:

    python mandelbrot.py [x] [y] [zoom] [width] [height] [filename]
    
Replace the arguments within brackets with your desired values:

x: X coordinate of the center of the plot (default: -0.75)
y: Y coordinate of the center of the plot (default: 0.0)
zoom: Zoom level of the plot (default: 1)
width: Width of the plot (default: 480)
height: Height of the plot (default: 720)
filename: Specify a filename for the output (default: "mandelbrot")

# Example:
    
    python mandelbrot.py -0.5 0.0 2 800 600 fractal_image
    
The generated image will be saved as fractal_image.tiff in the current directory.
