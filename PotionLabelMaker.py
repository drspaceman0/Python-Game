
class PotionLabelMaker:
	adjectives = []
	types = []
	skills = []
	
	
	def __init__(self):
		#Regular
		self.adjectives.append("weak")
		self.adjectives.append("meager")
		#special
		self.adjectives.append("smelly")
		self.adjectives.append("superfruit")
		self.adjectives.append("soapy")
		
		#regular
		self.types.append("of health")
		self.types.append("of stamina")
		#special
		self.types.append("of poison")
		self.types.append("of gigantism")
		self.types.append("of dwarfism")
		
		#regular
		self.skills.append("of archery")
		self.skills.append("of strength")
		self.skills.append("of quickness")
		#special
		self.skills.append("of smelly farts")