from PIL import Image 

def linterp(myA, myB, myF):
	# interpolates two values myA and myB with a fraction myF
	return float((1-myF) * myA + myF * myB)

def mapRange(v, min1, max1, min2, max2):
	# value is the value to map
	# min1 is the minimum value of the range n is in and max1 is its maximum value
	# min2 is the minimum value of the range n is to be mapped to and max1 is its maximum value
	return float(v-min1)/float(max1-min1)*float(max2-min2)+min2

def imgFromTuples(m,s,d):
	# s is a (width,height) tuple
	# d is a list of RGB tuples
	# m is the desired PIL mode
	img = Image.new(m,s)
	img.putdata(d)
	return img

def colorMap(mnic):
	# turns a mapped normalized iteration count for a pixel of a mandelbrot plot into an RGB tuple
	return (255-mnic,abs(128-mnic),mnic)