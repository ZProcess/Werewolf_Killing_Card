#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame,sys,random
from pygame.locals import *
class MyCard(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.master_image=None
		self.width=0
		self.hight=0
		self.columns=1
		self.numb=0

	def _getpos(self):
		return self.rect.topleft
	def _setpos(self,pos):
		self.rect.topleft=pos
	position=property(_getpos,_setpos)

	def load(self,filename):
		self.master_image=pygame.image.load(filename).convert_alpha()
		self.width,self.hight=self.master_image.get_size()
		self.master_image=pygame.transform.smoothscale(self.master_image,(self.width//2,self.hight//2))
		self.rect=Rect(0,0,self.width,self.hight)

	def update(self):
		self.image=self.master_image

	def set_mouse(self,image,x=0,y=0,width=60,hight=60):
		self.master_image=image
		self.width=width
		self.hight=hight
		self.rect=Rect(x,y,width,hight)
		


def shuffle_role():
	role=[1,1,1,2,2,2,3,4]
	random.shuffle(role)
	random.shuffle(role)
	random.shuffle(role)
	return role
	

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Werewolf Killing Card")
font=pygame.font.Font(None,34)

bx=80
by=100
cnumb=0
cgroup=pygame.sprite.Group()

for n in range(0,2):
	for m in range(0,4):
		cbg=MyCard()
		cbg.load("cbg.jpg")
		cbg.position=(bx,by)
		cbg.numb=cnumb
		bx=bx+160
		cnumb=cnumb+1
		cgroup.add(cbg)
	by=by+250
	bx=80
cgroup.update()
cgroup.draw(screen)
pygame.display.update()

role_group=pygame.sprite.Group()


role=shuffle_role()
rnumb=1
role_group=[]

for n in role:
	if n==1:
		langren=MyCard()
		langren.load("langren.jpg")
		langren.numb=rnumb
		role_group.append(langren)
	if n==2:
		pingmin=MyCard()
		pingmin.load("pingmin.jpg")
		pingmin.numb=rnumb
		role_group.append(pingmin)
	if n==3:
		nvwu=MyCard()
		nvwu.load("nvwu.jpg")
		nvwu.numb=rnumb
		role_group.append(nvwu)
	if n==4:
		yyj=MyCard()
		yyj.load("yyj.jpg")
		yyj.numb=rnumb
		role_group.append(yyj)
	rnumb=rnumb+1

mx=0
my=0
mouse_is_down=False
cursor=MyCard()
image=pygame.Surface((10,10)).convert_alpha()
cursor.set_mouse(image)

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			sys.exit()
		if event.type==MOUSEBUTTONDOWN:
			mx,my=event.pos
			cursor.position=(mx,my)
			mouse_is_down=True
	keys=pygame.key.get_pressed()
	if keys[K_ESCAPE]:
		sys.exit()
	collide_list=pygame.sprite.spritecollide(cursor,cgroup,False)
	if  collide_list and mouse_is_down:
		now=collide_list.pop()
		current=role_group[now.numb]
		current.rect=now.rect
		current_group=pygame.sprite.Group()
		current_group.add(current)
		current_group.update()
		current_group.draw(screen)

	pygame.display.update()















	




