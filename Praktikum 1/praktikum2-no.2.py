#===== PRAKTIKUM 1, NO.2 =====#
#===== No.2 (A) =====#
from matplotlib import pyplot as plt

def DDA(x0, y0, x1, y1):
	dx = abs(x0 - x1)
	dy = abs(y0 - y1)
    
	steps = max(dx, dy)
    xinc = dx/steps
	yinc = dy/steps

	x = float(x0)
	y = float(y0)

	x_coorinates = []
	y_coorinates = []

	for i in range(steps):
		x_coorinates.append(x)
		y_coorinates.append(y)
		x = x + xinc
		y = y + yinc
        
	plt.plot(x_coorinates, y_coorinates, marker = "o", markersize = 1, markerfacecolor = "green")
	plt.show()


if __name__ == "__main__":

	x0, y0 = -3, 3
	x1, y1 = -1, 3
	DDA(x0, y0, x1, y1)

#===== No.2 (B) =====#
from matplotlib import pyplot as plt

def DDA(x0, y0, x1, y1):

	dx = abs(x0 - x1)
	dy = abs(y0 - y1)

	steps = max(dx, dy)

	xinc = dx/steps
	yinc = dy/steps

	x = float(x0)
	y = float(y0)

	x_coorinates = []
	y_coorinates = []

	for i in range(steps):
		x_coorinates.append(x)
		y_coorinates.append(y)

		x = x + xinc
		y = y + yinc

	plt.plot(x_coorinates, y_coorinates, marker = "o", markersize = 1, markerfacecolor = "green")
	plt.show()


if __name__ == "__main__":

	x0, y0 = 7, -1
	x1, y1 = -4, -6
	DDA(x0, y0, x1, y1)

#===== No.2 (C) =====#
from matplotlib import pyplot as plt

def DDA(x0, y0, x1, y1):

	dx = abs(x0 - x1)
	dy = abs(y0 - y1)

	steps = max(dx, dy)

	xinc = dx/steps
	yinc = dy/steps

	x = float(x0)
	y = float(y0)

	x_coorinates = []
	y_coorinates = []

	for i in range(steps):
		x_coorinates.append(x)
		y_coorinates.append(y)

		x = x + xinc
		y = y + yinc

	plt.plot(x_coorinates, y_coorinates, marker = "o", markersize = 1, markerfacecolor = "green")
	plt.show()


if __name__ == "__main__":

	x0, y0 = -3, 3
	x1, y1 = -1, -3
	DDA(x0, y0, x1, y1)