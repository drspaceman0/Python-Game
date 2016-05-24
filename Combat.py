import math
import Display
import pygame
import functions



def attack(attacker, defender, isPlayerAttacking):
	# use player's attack rectangle 
	if attacker.name == "Hero":
		if functions.rectCollision(attacker.attackRect, defender.rect):
			defender.health -= attacker.damage
			knockBack(attacker, defender)
			print "%s hit %s for %s damage..." % (attacker.name, defender.name, attacker.damage)
			print "with a %s" % (attacker.currentWeapon.name)
		if defender.health <= 0:
			print "%s has been struck dead!" % (defender.name)
			defender.death()
	else:
		if functions.rectCollision(attacker.rect, defender.rect):
			defender.health -= attacker.damage
			knockBack(attacker, defender)
			print "%s hit %s for %s damage..." % (attacker.name, defender.name, attacker.damage)
			print "with a %s" % (attacker.currentWeapon.name)
		if defender.health <= 0:
			print "%s has been struck dead!" % (defender.name)
			defender.death()

def knockBack(attacker, defender):
	if defender.knocksBack:
		if attacker.x < defender.x: #attacker is to the left
			defender.x += attacker.damage + 100 - defender.size
		elif attacker.x > defender.x: #attacker is to the right
			defender.x -= attacker.damage + 100 - defender.size
		if attacker.y < defender.y: #attacker is above
			defender.y += attacker.damage + 100 - defender.size
		elif attacker.y > defender.y: #attacker is bellow
			defender.y -= attacker.damage + 100 - defender.size

		