import math
import Display
import pygame

class Combat:
	
	#Maybe use this to keep track of session stats?
	def __init__(self):
		self.total_kills = 0
	
	def attack(self, attacker, defender):
		defender.health -= attacker.damage
		print "%s hit %s for %s damage..." % (attacker.name, defender.name, attacker.damage)
		print "with a %s" % (attacker.currentWeapon.name)
		if defender.health <= 0:
			print "%s has been struck dead!" % (defender.name)
			defender.death()
