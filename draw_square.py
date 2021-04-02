import turtle

def drawSquare(porky):
	for _ in range(4):
		porky.forward(100)
		porky.right(90)

def art():
	window = turtle.Screen()
	window.bgcolor("white")

	porky = turtle.Turtle()
	porky.speed(5)
	porky.pensize(2)
	porky.color('black')

	for _ in range(36):
		drawSquare(porky)
		porky.right(10)

	window.clickOnExit()




if __name__ == "__main__":
	art()


