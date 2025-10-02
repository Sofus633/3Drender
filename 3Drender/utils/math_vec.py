
def intersection(focale, droite, point):
	# droite(A, B) A(5, 2) B(1, 0)
	# droite(C, D) C(6, 5), D(0, 0)
	
	#a = 	

	#ax + b - z = 0
	#a1x1 + b1 -z1 = 0 
	#ax +b - x - (a1x1 + b1 - z1) = 0
	b = (droite[1].y - droite[0].y)/ (droite[1].x - droite[0].x)
	a = (droite[0].y - b) / droite[0].x
	
	if ((a * point.position.x + b - point.position.y) == 0):
		pass	
	
	
	
