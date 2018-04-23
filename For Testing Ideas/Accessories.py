class Accessory():
	def __init__(self,Level=0,HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0):
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
		self.Level=Level
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

ACC={}
ACC["IronBangle"]=Accessory(HP=0,ENE=0,STR=2,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["SilkSash"]=Accessory(HP=0,ENE=0,STR=0,SPR=2,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["GlassMonocle"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=2,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["HUDImplant"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=2,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["HeelWheels"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=2,EVA=0,TGH=0,RES=0,LCK=0)
ACC["PredictionImplant"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=2,TGH=0,RES=0,LCK=0)
ACC["LatticeShieldP"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=2,RES=0,LCK=0)
ACC["LatticeShieldM"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=2,LCK=0)
ACC["LuckySash"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=2)
ACC["ReflectiveCoating"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0-2,TGH=0,RES=0,LCK=0)
ACC["SnowshoeWebbing"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=3,AGI=3,EVA=3,TGH=0,RES=0,LCK=0)
ACC["OpalBrooch"]=Accessory(HP=0,ENE=0,STR=3,SPR=3,SKL=3,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["FurHemwork"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=3,RES=3,LCK=3)
ACC["MuscleShirt"]=Accessory(HP=0,ENE=0,STR=8,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["BloodstoneBrooch"]=Accessory(HP=0,ENE=0,STR=8,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["ExtraFinger"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=8,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["AncientScroll"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=8,AGI=0,EVA=0,TGH=0,RES=0,LCK=0)
ACC["ExtraToe"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=8,EVA=0,TGH=0,RES=0,LCK=0)
ACC["MadScientistGoggles"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=8,TGH=0,RES=0,LCK=0)
ACC["WerewolfFur"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=8,RES=0,LCK=0)
ACC["MummyWrap"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=8,LCK=0)
ACC["LuckyCoinNecklace"]=Accessory(HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=8)

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