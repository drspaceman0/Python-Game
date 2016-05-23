#shopkeeper sells stuff to hero. For gold. Sweet sweet gold....
import functions
import NPC
import random
import Coin



class Shopkeeper(NPC.NPC):
	
	def __init__(self, x, y, roomObj, text):
		self.store = []
		self.gold = 50
		self.dialogue = text
		self.collisionx = x
		self.collisiony = y
		self.width = 48
		self.height = 48
		self.range = 48
		self.roomObj = roomObj
		pass
		
	
	def trade(self):
		if functions.playerInventory:
			gold = Coin.Coin()
			counter = 0
			for item in functions.playerInventory:
				if self.gold >= 0:
					self.store.append(item)
					functions.playerInventory.remove(item)
					gold.value += random.randint(1,3)
					self.gold -= 1
					counter += 1
			functions.playerCoins.append(gold)
			print "Traded %s items for %s gold" % (counter, gold.value)
			
		
	def update(self):
		self.drawNPC()
		if self.checkPlayerCollision():
			self.roomObj.text = self.dialogue
			if self.roomObj.playerObj.isTrading == True:
				self.trade()
		else:
			self.roomObj.text = ""