import math
import Display
import pygame
import functions



def attack(attacker, defender, isPlayerAttacking):
	# use player's attack rectangle 
	if isPlayerAttacking:
		if functions.rectCollision(attacker.attackRect, defender.rect):
			defender.health -= attacker.damage
			print "%s hit %s for %s damage..." % (attacker.name, defender.name, attacker.damage)
			print "with a %s" % (attacker.currentWeapon.name)
		if defender.health <= 0:
			print "%s has been struck dead!" % (defender.name)
			defender.death()
	else:
		if functions.rectCollision(attacker.rect, defender.rect):
			defender.health -= attacker.damage
			print "%s hit %s for %s damage..." % (attacker.name, defender.name, attacker.damage)
			print "with a %s" % (attacker.currentWeapon.name)
		if defender.health <= 0:
			print "%s has been struck dead!" % (defender.name)
			defender.death()
