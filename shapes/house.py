import turtle as t

class House:
	def __init__(self, x, y, body, roof):
		self.x = x
		self.y = y
		self.body = body
		self.roof = roof

	def draw(self, xPos, yPos):
		t.teleport(xPos - self.x / 2, yPos + self.y / 2)
		t.right(90)
		t.color(self.body)
		t.down()
		t.forward(self.y)
		t.left(90)
		t.forward(self.x)
		t.left(90)
		t.forward(self.y)
		t.up()
		t.teleport(xPos - self.x * 5 / 8, yPos + self.y / 2)
		t.right(90)
		t.color(self.roof)
		t.down()
		t.forward(self.x * 5 / 4)
		t.left(120)
		t.forward(self.x * 5 / 4)
		t.left(120)
		t.forward(self.x * 5 / 4)
		t.up()
