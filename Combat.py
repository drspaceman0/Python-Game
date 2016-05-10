import math
import Display

class Combat:
	
	#Maybe use this to keep track of session stats?
	def __init__(self):
		self.kills = 0
		#self.stuff...
		
	def collision(self, attacker, defender):
		if math.sqrt(pow((attacker.x) - defender.x, 2) + pow((attacker.y-20) - defender.y, 2)) < attacker.range:
			return True
		
	def attack(self, attacker, defender):
		if self.collision(attacker, defender):
			defender.health -= attacker.damage
			print "%s hit %s for %s damage..." % (attacker.name, defender.name, attacker.damage)
			print "with a %s" % (attacker.currentWeapon.name)
			if defender.health < 0:
				print "%s has been struck dead!" % (defender.name)
				defender.death()
				
	def drawAttack(self, attacker):
		pygame.draw.arc(Display.DISPLAYSURF, )