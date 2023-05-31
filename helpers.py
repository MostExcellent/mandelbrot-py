from PIL import Image


def linterp(myA, myB, myF):
    """
    Interpolates two values myA and myB with a fraction myF.
    """
    return (1 - myF) * myA + myF * myB


def mapRange(v, min1, max1, min2, max2):
    """
    Maps a value v from the range [min1, max1] to the range [min2, max2].
    """
    return (v - min1) / (max1 - min1) * (max2 - min2) + min2


def imgFromTuples(mode, size, data):
    """
    Creates an image from a list of RGB tuples.
    """
    img = Image.new(mode, size)
    img.putdata(data)
    return img


def colorMap(mnic):
    """
    Converts a mapped normalized iteration count for a pixel of a Mandelbrot plot into an RGB tuple.
    """
    return (255 - mnic, abs(128 - mnic), mnic)
