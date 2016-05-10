

class WeaponLabelMaker:
	#ll stands for low level - 1-5
	#ml stands for medium level - 5-10
	#hl stands for high level - 10-15
	#eg stands for end game - 15+
	lladjectives = [] #None to little effect on damage
	mladjectives = [] #None to small effect on damage
	hladjectives = [] #None to medium effect on damage
	egadjectives = [] #Guarenteed effect on damage
	
	
	llnouns = []
	mlnouns = []
	hlnouns = []
	egnouns = []
	
	#These might need prepositions
	llverbs = [] #None but the weakest status effects (smoldering, numbing, sparking, stinking etc)
	mlverbs = [] #Slight status effects (frosting, embering, shocking, sickening, etc)
	hlverbs = [] #Some status effect ( numb < chill < freeze) contaminating, burning, etc.
	egverbs = [] #Best status effects (scorching, freezing, etc.)
	
	
	#Materials are just what the sword is made of... impact?	
	llmaterial = []
	mlmaterial = []
	hlmaterial = []
	egmaterial = []
	
	def __init__(self):
		#Harmful - Damages player or has weird status
		self.lladjectives.append("Tainted") #Hurts player with each attack
		self.lladjectives.append("Chaotic") #Deals random damage to player and enemy
		#Regular - Damage in low level range - TBD with testing
		self.lladjectives.append("Brittle") #Template
		self.lladjectives.append("Rusty") #Template
		self.lladjectives.append("Decayed") #Template
		self.lladjectives.append("Worn") #Template
		self.lladjectives.append("Weathered") #Template
		self.lladjectives.append("Crumbling") #Template
		self.lladjectives.append("Frangible") #Template Why not teach english while we play...? :D 
		self.lladjectives.append("Weak") #Template 
		self.lladjectives.append("Powerless") #Template 
		self.lladjectives.append("Frail") #Template 
		
		#Helpful - Boost power or gives status 
		#Effects
		self.lladjectives.append("Rotten") #Slight DOT - poison
		self.lladjectives.append("Moldy") #Slight DOT - poison
		self.lladjectives.append("Sharp") #Slight DOT - bleed
		self.lladjectives.append("Ancient") #Slight damage boost - magic
		
		#MidLevel - Regular damage for mid-level
		#Harmful
		self.mladjectives.append("Tainted") #Hurts the attacker with each attack
		self.mladjectives.append("Chaotic") #Deals random range of heavy damage to attacked, less to attacker
		self.mladjectives.append("Heavy") #Slows self
		#Regular damage in mid-level range
		self.mladjectives.append("Trusty") #Template
		self.mladjectives.append("Honerable") #Template
		self.mladjectives.append("Dueling") #Template
		self.mladjectives.append("Foul") #Template
		self.mladjectives.append("Stained") #Template
		self.mladjectives.append("Conditioned") #Template
		self.mladjectives.append("Tempered") #Template
		
		#Helpful - Boost attack power or gives status 
		self.mladjectives.append("Honed") #Increases damage
		self.mladjectives.append("Quick") #Increases speed
		self.mladjectives.append("Relic") #Increase damage - Magic
		self.mladjectives.append("Rancid") #DOT - poison
		self.mladjectives.append("Barbed") #DOT - bleed
		self.mladjectives.append("") #Template
		
		#High level add later if this works... 
		
		
		#Materials
		self.llmaterial.append("Wood") #Template
		self.llmaterial.append("Iron") #Template
		self.llmaterial.append("Copper") #Template
		self.llmaterial.append("Glass") #Template
		
		#Verbs - Effects
		self.llverbs.append("of smoldering")#Template
		self.llverbs.append("of numbing")#Template
		self.llverbs.append("of sparking")#Template
		self.llverbs.append("of mild stink")#Template
		
		#Melee nouns
		self.llnouns.append("straightsword") #Base weapon
		self.llnouns.append("axe") #Base weapon
		self.llnouns.append("dagger") #Base weapon
		self.llnouns.append("mace") #Base weapon
		self.llnouns.append("katana") #Base weapon
		self.llnouns.append("broadsword") #Base weapon
		self.llnouns.append("longsword") #Base weapon
		self.llnouns.append("cudgel") #Base weapon
		
		self.mlnouns.append("greatsword") #Base weapon
		self.mlnouns.append("staff") #Base weapon
		self.mlnouns.append("twinblade") #Base weapon
		self.mlnouns.append("shiv") #Base weapon
		self.mlnouns.append("club") #Base weapon
		self.mlnouns.append("greatclub") #Base weapon
		self.mlnouns.append("hammer") #Base weapon
		
		
		
		
		