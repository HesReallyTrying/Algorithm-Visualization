import turtle as t

from shapes import house

def main():
	t.speed(0)
	t.hideturtle()
	t.up()
	h1 = house.House(80, 100, 'black', 'red');
	h1.draw(50, 50)
	t.mainloop()
if __name__ == "__main__":
	main()