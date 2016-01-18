"""Final Project Members:
Agustin Mendoza 26220244 
Roger Moute 
Matthew Nicoletti
"""




import pygame
import time
import math 

pygame.init()
white = (255,255,255)
IntroGreen = (0, 147, 68)
StartButton = pygame.image.load('StartButton.gif')
InstructionsButton = pygame.image.load('InstructionsButton.gif')
Instrcutions = pygame.image.load('instructions.gif')
gameDisplay = pygame.display.set_mode((480,480))
pygame.display.set_caption ('Billiards')
PoolStickIntro = pygame.image.load("PoolStickBig.gif")
white = (255,255,255)
gameDisplay = pygame.display.set_mode((480,480))
pygame.display.set_caption ('Billiards') 
clock = pygame.time.Clock()
CueBallImg = pygame.image.load('CueBall.gif').convert_alpha()
PoolTableImg = pygame.image.load('Pool_Table.gif').convert_alpha()
PoolStickImg = pygame.image.load('Poolstick.gif').convert_alpha() 
Ball1 = pygame.image.load('Ball1.gif').convert_alpha()
Ball2 = pygame.image.load('Ball2.gif').convert_alpha()
Ball3 = pygame.image.load('Ball3.gif').convert_alpha()
pos_list = [[347, 240], [50, 200], [50, 250], [50, 280]]
V_list = [[0, 0], [0, 0], [0, 0], [0, 0]]
Holes = ((20,89),(240, 88),(455, 96),(453, 381),(238,295),(20, 386))
#Holes
#some simple functions for vectors (where a vector is a list of length two)

def add_vectors(vector1, vector2):
    return [vector1[0]+ vector2[0], vector1[1]+ vector2[1]]
def subtract_vectors(vector1, vector2):
    return [vector1[0]- vector2[0], vector1[1]- vector2[1]]
def magnitude(V):
    return math.sqrt((V[0]**2) + (V[1]**2))
def scalar_multiple(scalar, vector):
    return [scalar* x for x in vector]
def dot_product(V1, V2):
    return V1[0]*V2[0]+V1[1]*V2[1]
def normalize(V):
    return scalar_multiple(1/magnitude(V), V)


def touching(r1, r2):
    if magnitude(subtract_vectors(r1, r2))< (Ball1.get_width()):
        return True
    else:
        return False

def detect_collision():
    touchinglist=[]
    for i in range(len(pos_list)):
        for j in range(i+1, len(pos_list)):
            if touching(pos_list[i], pos_list[j]):
                touchinglist.append([i, j])
    return touchinglist

def apply_impulse(x, y):  #x and y are the indices of the balls colliding
    Avel= V_list[x]
    Bvel= V_list[y]
    #calculate relative velocity
    rv= subtract_vectors(Avel, Bvel)
    #calculate component of relative velocity in normal direction
    n= normalize(subtract_vectors(pos_list[y], pos_list[x]))
    velAlongNormal= dot_product(rv, n)

    #calculate restitution
    e= .93
    #calculate impulse scalar
    m=.19
    j= -(1+e)*velAlongNormal
    j/= 2/m
    #apply impulse
    impulse= scalar_multiple(j, n)
    Avel =add_vectors(Avel, scalar_multiple(1/m, impulse)) 
    Bvel =subtract_vectors(Bvel, scalar_multiple(1/m, impulse))
    V_list[x]= Avel
    V_list[y]= Bvel


def n(pos_a, pos_b):
    return subtract_vectors(pos_b, pos_a)


def PoolTable (x,y):
	x -= PoolTableImg.get_width()/2
	y -= PoolTableImg.get_height()/2
	gameDisplay.blit(PoolTableImg,(x,y))


def PoolStick(x,y):
	x -= PoolStickImg.get_width()/2
	y -= PoolStickImg.get_height()/2
	gameDisplay.blit(PoolStickImg,(x,y))


def CueBall(x,y):
	x -= CueBallImg.get_width()/2
	y -= CueBallImg.get_height()/2
	gameDisplay.blit(CueBallImg,(x,y))

PoolSticklead_x = 360
PoolSticklead_y = 240
PoolSticklead_angle = 0
PoolStickX_change = 0 
PoolStickY_change = 0
pygame.mouse.set_visible(True)


def dist_between(x1, y1, x2, y2):
	return math.sqrt((x2-x1)**2 + (y2- y1)**2)

def text_objects(text, font):
	textSurface = font.render(text, True, (255,255,255))
	return textSurface, textSurface.get_rect()

def game_intro(): 
	intro = True 

	while intro: 
		_Mouse = pygame.mouse.get_pos()
		Click = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if 306 > _Mouse[0] > 170 and 305 > _Mouse[1] > 170:
				if Click[0] == 1:
					game_loop()
			elif 439 > _Mouse[0] > 303 and 438 > _Mouse[1] > 303:
				if Click[0] == 1:
					instructions_menu()


		gameDisplay.fill(IntroGreen)
		largeText = pygame.font.Font('freesansbold.ttf', 50)
		TextSurf, TextRect = text_objects("CS10 Billiards", largeText)
		TextRect.center = (180, 90)
		gameDisplay.blit(TextSurf, TextRect)
		gameDisplay.blit(PoolStickIntro, (10,110))
		gameDisplay.blit(StartButton, (170, 170))
		gameDisplay.blit(InstructionsButton, (303,303))
		pygame.display.update()
		clock.tick(15)

def instructions_menu():
	in_instructions = True
	while in_instructions:
		_Mouse = pygame.mouse.get_pos()
		Click = pygame.mouse.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if 439 > _Mouse[0] > 303 and 456 > _Mouse[1] > 320:
				if Click[0] == 1:
					game_loop()


		gameDisplay.fill(IntroGreen)
		gameDisplay.blit(Instrcutions, (0,0))
		gameDisplay.blit(StartButton, (303,320))

		pygame.display.update()
		clock.tick(15)

def game_loop():
	

	def PoolTable (x,y):
		x -= PoolTableImg.get_width()/2
		y -= PoolTableImg.get_height()/2
		gameDisplay.blit(PoolTableImg,(x,y))


	def PoolStick(x,y):
		x -= PoolStickImg.get_width()/2
		y -= PoolStickImg.get_height()/2
		gameDisplay.blit(PoolStickImg,(x,y))


	def CueBall(x,y):
		x -= CueBallImg.get_width()/2
		y -= CueBallImg.get_height()/2
		gameDisplay.blit(CueBallImg,(x,y))


	PoolStickImg = pygame.image.load('Poolstick.gif') 

	PoolSticklead_x = 360
	PoolSticklead_y = 240
	delta_theta = 0
	crashed = False
	Mouseposition = [0, 0]
	PoolStick(200, 200)
	max_power = 40
	pos_list = [[347, 240], [50, 200], [50, 250], [50, 280]]
	V_list = [[0, 0], [0, 0], [0, 0], [0, 0]]
	Holes = [[20,89],[241, 88],[454, 96],[457, 389],[238,393],[24, 384]]

	def add_vectors(vector1, vector2):
		return [vector1[0]+ vector2[0], vector1[1]+ vector2[1]]
	def subtract_vectors(vector1, vector2):
	    return [vector1[0]- vector2[0], vector1[1]- vector2[1]]
	def magnitude(V):
	    return math.sqrt((V[0]**2) + (V[1]**2))
	def scalar_multiple(scalar, vector):
	    return [scalar* x for x in vector]
	def dot_product(V1, V2):
	    return V1[0]*V2[0]+V1[1]*V2[1]
	def normalize(V):
	    return scalar_multiple(1/magnitude(V), V)

	def touching(r1, r2):
	    if magnitude(subtract_vectors(r1, r2))< (Ball1.get_width()):
	        return True
	    else:
	        return False

	def detect_collision():
	    touchinglist=[]
	    for i in range(len(pos_list)):
	        for j in range(i+1, len(pos_list)):
	            if touching(pos_list[i], pos_list[j]):
	                touchinglist.append([i, j])
	    return touchinglist

	def apply_impulse(x, y):  #x and y are the indices of the balls colliding
	    Avel= V_list[x]
	    Bvel= V_list[y]
	    #calculate relative velocity
	    rv= subtract_vectors(Avel, Bvel)
	    #calculate component of relative velocity in normal direction
	    n= normalize(subtract_vectors(pos_list[y], pos_list[x]))
	    velAlongNormal= dot_product(rv, n)

	    #calculate restitution
	    e= .93
	    #calculate impulse scalar
	    m=.19
	    j= -(1+e)*velAlongNormal
	    j/= 2/m
	    #apply impulse
	    impulse= scalar_multiple(j, n)
	    Avel =add_vectors(Avel, scalar_multiple(1/m, impulse)) 
	    Bvel =subtract_vectors(Bvel, scalar_multiple(1/m, impulse))
	    V_list[x]= Avel
	    V_list[y]= Bvel

	def n(pos_a, pos_b):
	    return subtract_vectors(pos_b, pos_a)

	PoolSticklead_x = 360
	PoolSticklead_y = 240
	PoolSticklead_angle = 0
	PoolStickX_change = 0 
	PoolStickY_change = 0
	pygame.mouse.set_visible(True)
	plotball = True
	plotball1 = True
	plotball2 = True
	plotball3 = True

	while not crashed:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				crashed=True
			if event.type == pygame.MOUSEMOTION:
				x, y = pygame.mouse.get_pos()
				Mouseposition = [(x), (y)]

			if event.type == pygame.MOUSEBUTTONUP:
				d = dist_between(PoolSticklead_x, PoolSticklead_y, pos_list[0][0], pos_list[0][1])
				u = min(d/100, 1)
				V_list[0] = scalar_multiple(u* max_power, normalize(n([PoolSticklead_x, PoolSticklead_y], pos_list[0])))
		PoolStickImg = pygame.image.load('Poolstick.gif')
		PoolStickImg = pygame.transform.rotate(PoolStickImg, 180)
		angle0 = math.atan2(PoolSticklead_y - pos_list[0][1], PoolSticklead_x - pos_list[0][0])
		PoolSticklead_x = Mouseposition[0]
		PoolSticklead_y = Mouseposition[1]
		angle1 = math.atan2(PoolSticklead_y - pos_list[0][1], PoolSticklead_x - pos_list[0][0])
		delta_theta = delta_theta + (angle0 - angle1)*180/math.pi
		PoolStickImg = pygame.transform.rotate(PoolStickImg, delta_theta)
		gameDisplay.fill(white)
		PoolTable(240, 240)
		
		PoolStick(PoolSticklead_x, PoolSticklead_y)	 
		
		V_list = [scalar_multiple(.98, v) for v in V_list]	

		for i in range(4):
			if (pos_list[i][0]) > 430.05 or (pos_list[i][0]) < 28.95:
				V_list[i][0] *= -1
			if (pos_list[i][1]) > 367.05 or (pos_list[i][1]) < 95.95:
				V_list[i][1] *= -1 

		if len(detect_collision())!=0:
			collidingballs= detect_collision()
			[apply_impulse(x[0], x[1]) for x in collidingballs]

		for i in range(4):
			pos_list[i] = add_vectors(pos_list[i], V_list[i])
			
		for r in Holes:
			if dist_between(pos_list[1][0], pos_list[1][1], r[0], r[1]) < 12:
				plotball1 = False
			if dist_between(pos_list[2][0], pos_list[2][1], r[0], r[1]) < 12:
				plotball2 = False
			if dist_between(pos_list[3][0], pos_list[3][1], r[0], r[1]) < 12:
				plotball3 = False
				

		if plotball == True:
			CueBall(pos_list[0][0], pos_list[0][1])
		if plotball1 == True:
			gameDisplay.blit(Ball1,(pos_list[1][0], pos_list[1][1]))
		if plotball2 == True:
			gameDisplay.blit(Ball2,(pos_list[2][0], pos_list[2][1]))
		if plotball3 == True:
			gameDisplay.blit(Ball3,(pos_list[3][0], pos_list[3][1]))
		

		pygame.display.update()
		clock.tick(10)

    
game_intro()  
game_loop()
pygame.quit()
quit()
	