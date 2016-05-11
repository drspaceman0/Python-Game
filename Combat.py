import math
import Display

class Combat:
	
	#Maybe use this to keep track of session stats?
	def __init__(self):
		self.kills = 0
		#self.stuff...
		
	def collision(self, attacker, defender):
		if attacker.isPlayer() == True:
			if math.sqrt(pow((attacker.weaponx) - defender.x, 2) + pow((attacker.weapony) - defender.y, 2)) <= attacker.rangeAfterSize:
				return True
			elif math.sqrt(pow((attacker.x) - defender.x, 2) + pow((attacker.y) - defender.y, 2)) <= attacker.rangeAfterSize:
				return True
			else:
				return False
	def attack(self, attacker, defender):
			defender.health -= attacker.damage
			print "%s hit %s for %s damage..." % (attacker.name, defender.name, attacker.damage)
			print "with a %s" % (attacker.currentWeapon.name)
			if defender.health < 0:
				print "%s has been struck dead!" % (defender.name)
				defender.death()
				
	def drawAttack(self, attacker):
		pygame.draw.arc(Display.DISPLAYSURF, )