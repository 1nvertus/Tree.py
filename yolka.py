import turtle								#library								
											#
t = turtle.Pen()							#
											#
t.speed("fastest")           				#speed from 0.5 to 1
											#
def star(n):								#
	'''draws an star'''						#
	t.left(90)								#
	t.forward(3*n)							#
	t.color("orange","yellow")				#pencil color, fill color			
	t.begin_fill()							#start filling
	t.left(126)								#
	for i in range(5):						#
		t.forward(n/5)						#
		t.right(144)						#
		t.forward(n/5)						#
		t.left(72)							#
	t.end_fill()							#end filling
	t.right(126)							#
											#	
											#
def tree(d, s):								#
	'''draw the tree'''						#
	if d <= 0: return						#
	t.forward(s)							#
	tree(d-1, s*.8)							#
	t.right(120)							#
	tree(d-3, s*.5)							#
	t.right(120)							#
	tree(d-3, s*.5)							#
	t.right(120)							#
	t.backward(s)							#
											#
turtle.bgcolor('#001F77')					#
star(100)									#
t.color("dark green")						#
t.backward(100*4.8)							#
tree(15, 100)								#
t.backward(100/2)							#
											#
turtle.mainloop()							#so as not to lag			
turtle.done()								#
