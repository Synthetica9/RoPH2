class Accessory():
	def __init__(self,LVL=0,HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0,Crit=0,Hit=0,Buy=0,Sell=0):
		self.HP=HP
		self.ENE=ENE
		self.STR=STR
		self.SPR=SPR
		self.SKL=SKL
		self.ABL=ABL
		self.AGI=AGI
		self.EVA=EVA
		self.TGH=TGH
		self.RES=RES
		self.LCK=LCK
		self.LVL=LVL
		self.Crit=Crit
		self.Hit=Hit
		self.Buy=Buy
		self.Sell=Sell
	@property
	def HPPlus(self):
		if self.HP >= 1:
			return self.HP
		else:
			return 0
	@property
	def HPMinus(self):
		if self.HP <= 0-1:
			return self.HP
		else:
			return 0
	@property
	def ENEPlus(self):
		if self.ENE >= 1:
			return self.ENE
		else:
			return 0
	@property
	def ENEMinus(self):
		if self.ENE <= 0-1:
			return self.ENE
		else:
			return 0
	@property
	def STRPlus(self):
		if self.STR >= 1:
			return self.STR
		else:
			return 0
	@property
	def STRMinus(self):
		if self.STR <= 0-1:
			return self.STR
		else:
			return 0
	@property
	def SPRPlus(self):
		if self.SPR >= 1:
			return self.SPR
		else:
			return 0
	@property
	def SPRMinus(self):
		if self.SPR <= 0-1:
			return self.SPR
		else:
			return 0
	@property
	def SKLPlus(self):
		if self.SKL >= 1:
			return self.SKL
		else:
			return 0
	@property
	def SKLMinus(self):
		if self.SKL <= 0-1:
			return self.SKL
		else:
			return 0
	@property
	def ABLPlus(self):
		if self.ABL >= 1:
			return self.ABL
		else:
			return 0
	@property
	def ABLMinus(self):
		if self.ABL <= 0-1:
			return self.ABL
		else:
			return 0
	@property
	def AGIPlus(self):
		if self.AGI >= 1:
			return self.AGI
		else:
			return 0
	@property
	def AGIMinus(self):
		if self.AGI <= 0-1:
			return self.AGI
		else:
			return 0
	@property
	def EVAPlus(self):
		if self.EVA >= 1:
			return self.EVA
		else:
			return 0
	@property
	def EVAMinus(self):
		if self.EVA <= 0-1:
			return self.EVA
		else:
			return 0
	@property
	def TGHPlus(self):
		if self.TGH >= 1:
			return self.TGH
		else:
			return 0
	@property
	def TGHMinus(self):
		if self.TGH <= 0-1:
			return self.TGH
		else:
			return 0
	@property
	def RESPlus(self):
		if self.RES >= 1:
			return self.RES
		else:
			return 0
	@property
	def RESMinus(self):
		if self.RES <= 0-1:
			return self.RES
		else:
			return 0
	@property
	def LCKPlus(self):
		if self.LCK >= 1:
			return self.LCK
		else:
			return 0
	@property
	def LCKMinus(self):
		if self.LCK <= 0-1:
			return self.LCK
		else:
			return 0
	@property
	def LVLPlus(self):
		if self.LVL >= 1:
			return self.LVL
		else:
			return 0
	@property
	def LVLMinus(self):
		if self.LVL <= 0-1:
			return self.LVL
		else:
			return 0
	@property
	def CritPlus(self):
		if self.Crit >= 1:
			return self.Crit
		else:
			return 0
	@property
	def CritMinus(self):
		if self.Crit <= 0-1:
			return self.Crit
		else:
			return 0
	@property
	def HitPlus(self):
		if self.Hit >= 1:
			return self.Hit
		else:
			return 0
	@property
	def HitMinus(self):
		if self.Hit <= 0-1:
			return self.Hit
		else:
			return 0

ACC = {
	"SturdyBangle": Accessory(STR=4,Buy=400,Sell=200),
	"MagicSash": Accessory(SPR=4,Buy=400,Sell=200),
	"GlassMonocle": Accessory(SKL=4,Buy=400,Sell=200),
	"HUDImplant": Accessory(ABL=4,Buy=400,Sell=200),
	"HeelWheels": Accessory(AGI=4,Buy=400,Sell=200),
	"PredictionImplant": Accessory(EVA=4,Buy=400,Sell=200),
	"LatticeShieldP": Accessory(TGH=4,Buy=400,Sell=200),
	"LatticeShieldM": Accessory(RES=4,Buy=400,Sell=200),
	"LuckySash": Accessory(LCK=4,Buy=400,Sell=200),
	"SnowshoeWebbing": Accessory(ABL=3, AGI=3, EVA=3,Buy=900,Sell=450),
	"OpalBrooch": Accessory(STR=3, SPR=3, SKL=3,Buy=900,Sell=450),
	"FurHemwork": Accessory(TGH=3, RES=3, LCK=3,Buy=900,Sell=450),
	"MuscleShirt": Accessory(STR=8,Buy=800,Sell=400),
	"BloodstoneBrooch": Accessory(STR=8,Buy=800,Sell=400),
	"ExtraFinger": Accessory(SKL=8,Buy=800,Sell=400),
	"AncientScroll": Accessory(ABL=8,Buy=800,Sell=400),
	"ExtraToe": Accessory(AGI=8,Buy=800,Sell=400),
	"MadScientistGoggles": Accessory(EVA=8,Buy=800,Sell=400),
	"WerewolfFur": Accessory(TGH=8,Buy=800,Sell=400),
	"MummyWrap": Accessory(RES=8,Buy=800,Sell=400),
	"LuckyCoinNecklace": Accessory(LCK=8,Buy=800,Sell=400),
	"AttackPackage": Accessory(STR=2,SPR=2,SKL=2,Buy=600,Sell=300),
	"DefensePackage": Accessory(EVA=2,TGH=2,RES=2,Buy=600,Sell=300),
	"SturdyBracer": Accessory(STR=6,Buy=600,Sell=300),
	"QuartzRing": Accessory(SPR=6,Buy=600,Sell=300),
	"WhiteGloves": Accessory(SKL=6,Buy=600,Sell=300),
	"DangerImplant": Accessory(ABL=6,Buy=600,Sell=300),
	"RocketHeels": Accessory(AGI=6,Buy=600,Sell=300),
	"InstinctImplant": Accessory(EVA=6,Buy=600,Sell=300),
	"DenseLatticeP": Accessory(TGH=6,Buy=600,Sell=300),
	"DenseLatticeM": Accessory(RES=6,Buy=600,Sell=300),
	"MilitaryAttackProgram": Accessory(STR=4,SPR=4,SKL=4,Buy=1200,Sell=600),
	"MilitaryDefenseProgram": Accessory(EVA=4,TGH=4,RES=4,Buy=1200,Sell=600),
	"Leveliser": Accessory(LVL=1,Buy=100,Sell=50),
	"ZoomGoggles": Accessory(Crit=5,Buy=1000,Sell=500),
}

class Wiggles():
	def __init__(self,Level=1):
		self.Level=Level
		self.Change=Level*5
	@property
	def HPPlus(self):
		return 0
	@property
	def HPMinus(self):
		return 0
	@property
	def ENEPlus(self):
		return 0
	@property
	def ENEMinus(self):
		return 0
	@property
	def STRPlus(self):
		return self.Change
	@property
	def STRMinus(self):
		return 0
	@property
	def SPRPlus(self):
		return self.Change
	@property
	def SPRMinus(self):
		return 0
	@property
	def SKLPlus(self):
		return self.Change
	@property
	def SKLMinus(self):
		return 0
	@property
	def ABLPlus(self):
		return self.Change
	@property
	def ABLMinus(self):
		return 0
	@property
	def AGIPlus(self):
		return self.Change
	@property
	def AGIMinus(self):
		return 0
	@property
	def EVAPlus(self):
		return self.Change
	@property
	def EVAMinus(self):
		return 0
	@property
	def TGHPlus(self):
		return self.Change
	@property
	def TGHMinus(self):
		return 0
	@property
	def RESPlus(self):
		return self.Change
	@property
	def RESMinus(self):
		return 0
	@property
	def LCKPlus(self):
		return self.Change
	@property
	def LCKMinus(self):
		return 0
