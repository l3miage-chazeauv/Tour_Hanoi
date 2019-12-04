from turtle import*

def init(n):
	poteau_g = []
	poteau_c = []
	poteau_d = []

	vargd = []
	grandeur_disque = []
	bord_select = [20]
	h = 20
	m = n

	while n!=0:
		poteau_g.append(n)
		#poteau_c.append(n) 
		vargd.append(n)
		n = n-1

	for k in range(0,m):
		g = ((vargd[k])*30)-10
		grandeur_disque.append(g)

	for k in range(0,m-1):
		h = h +15
		bord_select.append(h)

	grandeur_disque.sort()
	bord_select.sort(reverse=True)
	return poteau_g,poteau_c,poteau_d,grandeur_disque,bord_select

def nombre_disques(n,p):

	varinit = init(n) #variables définies dans init
	l = varinit[p] #Variable l qui prend l'un des poteaux en parametres
	#print(len(l))

def disque_superieur(n):

	varinit = init(n) #variables définies dans init
	dsup = []


	for ntour in range(0,3):
		a = varinit[ntour]
		if (a != []):
			a = a[-1]
			dsup.append(a)
		else:
			dsup.append(0)

	return dsup
def pos_disque(n,numdisque):

	varinit = init(n) #variables définies dans init
	
	if numdisque in varinit[0]:
		print("Le disque n°", numdisque, "est dans la tour gauche.")
	elif numdisque in varinit[1]:
		print("Le disque n°", numdisque, "est dans la tour centre.")
	elif numdisque in varinit[2]:
		print("Le disque n°", numdisque, "est dans la tour droite.")
	else:
		print("Le numéro de disque n'existe pas.")

def verif_deplacement(n,nt1,nt2):
	ldsup = disque_superieur(n) #liste des plus hauts disques de chaque tour
	if ldsup[nt1]<ldsup[nt2] and (ldsup[nt1]!=0 or ldsup[nt2]==0):
		print("VAS Y PASSE")
	else:
		print("BOUFFON TU FOUS QUOI DEGAGE")

def verifier_victoire(n):
	varinit = init(n)
	nt2 = varinit[2]
	if len(nt2) == n:
		print("GG")
	else:
		print("PAS GG")


#TURTLE
hideturtle()
speed(0)
def dessine_plateau(n):
	
	#bgpic("C:\Users\lazer\Desktop\HanoiPowa\wallpaper.gif")
	# print(bgpic())

	dim_grd_disque = 20 + ((n-1)*30) 					#Diamètre du plus grand disque disque
	bord = (dim_grd_disque/2)+15						#Espace entre les tours gauche et droite avec les extremités du plateau
	dim_plateau = dim_grd_disque*3 + 80					#Longueur plateau
	htour = n*20 + 20									#Hauteur tour

	up()
	goto(-300,-200)
	down()

	for k in range (0,2):
		begin_fill()
		forward(dim_plateau)
		left(90)
		forward(30)
		left(90)
		end_fill()

	up()
	goto(-(300-bord),-170)
	down()

	begin_fill()

	for k in range (0,3):
		left(90)
		forward(htour)
		right(90)
		forward(10)
		right(90)
		forward(htour)
		left(90)

		up()
		forward(dim_grd_disque+10)
		down()
	end_fill()

	up()
	goto(-300,-200)
	down()

def dessine_disque(numdisque,n):
	varinit = init(n)
	grandeur_disque = varinit[3]  #Variable donnant la longueur du disque sélectionné
	bord_select = varinit[4]	  #Variable donnant l'écart entre le disque sélectionné et les bordures du plateau

	a = varinit[0]
	b = varinit[1]
	c = varinit[2]

	fillcolor("white")
	begin_fill()

	if numdisque in a:										#Test la tour dans laquelle est le disque

		
		up()
		goto(-300+bord_select[numdisque-1],-189+20*a[numdisque-1])
		down()
			
		for k in range(0,2):								#Boucle dessin disque
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)
		
	elif numdisque in b:
		if numdisque == b[0]:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-169)
			down()

		else:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-189+20*a[numdisque-1])
			down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

	elif numdisque in c:
		if numdisque == c[0]:
			up()
			goto(-300+3*bord_select[numdisque-1]+2*grandeur_disque[numdisque-1],-189)
			down()

		else:
			up()
			goto(-280+2*bord_select[numdisque-1],-189+20*a[numdisque-1])
			down()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

	end_fill()

def efface_disque(numdisque,n):
	varinit = init(n)
	grandeur_disque = varinit[3]
	bord_select = varinit[4]

	a = varinit[0]
	b = varinit[1]
	c = varinit[2]

	if numdisque in a:

		if numdisque == a[0]:
			up()
			goto(-300+bord_select[numdisque-1],-169)
			down()

		else:
			up()
			goto(-300+bord_select[numdisque-1],-189+20*a[numdisque-1])
			down()
			
		color("white")
		begin_fill()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		end_fill()
		forward((grandeur_disque[numdisque-1]/2)-5)
		color("black")
		begin_fill()

		for k in range(0,2):
			forward(10)
			left(90)
			forward(20)
			left(90)

		end_fill()
		
	elif numdisque in b:
		if numdisque == b[0]:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-189)
			down()

		else:
			up()
			goto(-300+2*bord_select[numdisque-1]+grandeur_disque[numdisque-1],-189+20*a[numdisque-1])
			down()

		color("white")								#Blanc pour effacer le disque
		begin_fill()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		end_fill()
		forward((grandeur_disque[numdisque-1]/2)-5)			#Positionnement disque pour retracer la tour
		color("black")										#Couleur tour
		begin_fill()

		for k in range(0,2):								#Bloucle dessin tour
			forward(10)
			left(90)
			forward(20)
			left(90)

		end_fill()

	elif numdisque in c:
		if numdisque == c[0]:
			up()
			goto(-300+3*bord_select[numdisque-1]+2*grandeur_disque[numdisque-1],-169)
			down()

		else:
			up()
			goto(-280+2*bord_select[numdisque-1],-189+20*a[numdisque-1])
			down()

		color("white")
		begin_fill()

		for k in range(0,2):
			forward(grandeur_disque[numdisque-1])
			left(90)
			forward(20)
			left(90)

		end_fill()
		forward((grandeur_disque[numdisque-1]/2)-5)
		color("black")
		begin_fill()

		for k in range(0,2):
			forward(10)
			left(90)
			forward(20)
			left(90)

		end_fill()

def dessine_config(n):
	for k in range(0,n+1):
		dessine_disque(k,n)

def efface_tout(n):
	for k in range(0,n):
		efface_disque(k,n)

dessine_plateau(5)
#dessine_disque(5,5)
#efface_disque(5,5)
dessine_config(5)
efface_tout(5)
#init(5)
mainloop()

#nombre_disques(int(input("Entrez un nombre de disque : ")),(int(input("Selectionner la tour (gauche = 0, centre = 1, droite = 2): "))))
#disque_superieur(int(input("Entrez un nombre de disque : ")))
#pos_disque(int(input("Entrez un nombre de disque : ")),(int(input("Entrez le numéro de disque souhaité: "))))
#verif_deplacement(int(input("Entrez le nombre de disque:")),int(input("Entrez la tour de départ (0 à 2):")),int(input("Entrez le numéro de la tour d'arrivée:")))