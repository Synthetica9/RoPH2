Sizes=("Tiny","Small","Normal","Large","Huge")
Mods=("Normal","Veteran","Hale","Energized","Strong","Spirited","Skillful","Capable","Agile","Evasive","Tough","Resistant","Lucky","Heavy","Light","Brutish","Wizened","Savvy","Zombie")
Beasts=("Dummy","Hawk","Centaur","Wolf","BigCat","Skeleton","Ogre","Elemental","Jel","Gargoyle","Arachnid")
Levels=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")

MonsterFactoryInputs=[]
for s in Sizes:
	for m in Mods:
		for b in Beasts:
			for l in Levels:
				MonsterFactoryInputs.append((s,m,b,l))

class Size():
	def __init__(self,HP=1,ENE=1,STR=1,SPR=1,SKL=1,ABL=1,AGI=1,EVA=1,TGH=1,RES=1,LCK=1,WT=1):
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
		self.WT=WT

class Mod():
	def __init__(self,ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1):
		self.ModHP=ModHP
		self.ModENE=ModENE
		self.ModSTR=ModSTR
		self.ModSPR=ModSPR
		self.ModSKL=ModSKL
		self.ModABL=ModABL
		self.ModAGI=ModAGI
		self.ModEVA=ModEVA
		self.ModTGH=ModTGH
		self.ModRES=ModRES
		self.ModLCK=ModLCK
		self.ModWT=ModWT

class Beast():
	def __init__(self,HP=100,ENE=100,STR=10,SPR=10,SKL=10,ABL=10,AGI=10,EVA=10,TGH=10,RES=10,LCK=10,WT=0):
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
		self.WT=WT

class Level():
	def __init__(self,LHP=1,LENE=1,LSTR=1,LSPR=1,LSKL=1,LABL=1,LAGI=1,LEVA=1,LTGH=1,LRES=1,LLCK=1,LWT=1):
		self.LHP=LHP
		self.LENE=LENE
		self.LSTR=LSTR
		self.LSPR=LSPR
		self.LSKL=LSKL
		self.LABL=LABL
		self.LAGI=LAGI
		self.LEVA=LEVA
		self.LTGH=LTGH
		self.LRES=LRES
		self.LLCK=LLCK
		self.LWT=LWT

BDT={}
BDT["Dummy"]=Beast()
BDT["Hawk"]=Beast(50,50,10,5,10,10,15,15,5,5,10,5)
BDT["Arachnid"]=Beast(75,75,15,0,15,10,15,25,7,7,10,12)
BDT["Gargoyle"]=Beast(100,100,15,10,5,15,15,15,7,10,5,10)
BDT["Jel"]=Beast(50,50,5,15,0,10,5,15,6,12,10,7)
BDT["Centaur"]=Beast(125,125,10,5,5,10,22,12,10,10,10,50)
BDT["Wolf"]=Beast(75,75,15,5,15,10,20,12,14,7,10,30)
BDT["BigCat"]=Beast(75,75,15,15,5,10,20,12,7,14,10,30)
BDT["Skeleton"]=Beast(100,100,3,15,15,6,15,0,3,3,10,3)
BDT["Ogre"]=Beast(150,150,25,0,0,0,5,0,20,5,10,100)
BDT["Elemental"]=Beast(100,130,0,30,0,5,10,10,1,20,10,15)

MOD={}
MOD["Normal"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Veteran"]=Mod(ModHP=1.25,ModENE=1.25,ModSTR=1.25,ModSPR=1.25,ModSKL=1.25,ModABL=1.25,ModAGI=1.25,ModEVA=1.25,ModTGH=1.25,ModRES=1.25,ModLCK=1.25,ModWT=1.25)
MOD["Hale"]=Mod(ModHP=1.25,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Energized"]=Mod(ModHP=1,ModENE=1.25,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Strong"]=Mod(ModHP=1,ModENE=1,ModSTR=1.25,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Spirited"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1.25,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Skillful"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1.25,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Capable"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1.25,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Agile"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1.25,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Evasive"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1.25,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Tough"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1.25,ModRES=1,ModLCK=1,ModWT=1)
MOD["Resistant"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1.25,ModLCK=1,ModWT=1)
MOD["Lucky"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1.25,ModWT=1)
MOD["Heavy"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1.25)
MOD["Light"]=Mod(ModHP=1,ModENE=1,ModSTR=1,ModSPR=1,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=0.75)
MOD["Brutish"]=Mod(ModHP=1,ModENE=1,ModSTR=1.5,ModSPR=0.5,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=1.5,ModRES=0.5,ModLCK=1,ModWT=1)
MOD["Wizened"]=Mod(ModHP=1,ModENE=1,ModSTR=0.5,ModSPR=1.5,ModSKL=1,ModABL=1,ModAGI=1,ModEVA=1,ModTGH=0.5,ModRES=1.5,ModLCK=1,ModWT=1)
MOD["Savvy"]=Mod(ModHP=1,ModENE=1,ModSTR=0.5,ModSPR=0.5,ModSKL=1.5,ModABL=1.5,ModAGI=1,ModEVA=1,ModTGH=1,ModRES=1,ModLCK=1,ModWT=1)
MOD["Zombie"]=Mod(ModHP=1,ModENE=1,ModSTR=0.75,ModSPR=1.25,ModSKL=0.25,ModABL=0.25,ModAGI=0.5,ModEVA=0,ModTGH=0.25,ModRES=1.25,ModLCK=0,ModWT=0.5)

SZM={}
SZM["Tiny"]=Size(HP=0.7,ENE=0.8,STR=0.25,SPR=1.5,SKL=1.5,ABL=0.75,AGI=1.5,EVA=1.5,TGH=0.5,RES=1,LCK=1,WT=0.5)
SZM["Small"]=Size(HP=0.85,ENE=0.9,STR=0.5,SPR=1.25,SKL=1.25,ABL=1,AGI=1.25,EVA=1.25,TGH=0.75,RES=1,LCK=1,WT=0.75)
SZM["Normal"]=Size(HP=1,ENE=1,STR=1,SPR=1,SKL=1,ABL=1,AGI=1,EVA=1,TGH=1,RES=1,LCK=1,WT=1)
SZM["Large"]=Size(HP=1.15,ENE=1.1,STR=1.25,SPR=0.75,SKL=0.75,ABL=1.25,AGI=0.75,EVA=0.75,TGH=1.25,RES=1,LCK=1,WT=1.25)
SZM["Huge"]=Size(HP=1.3,ENE=1.2,STR=1.5,SPR=0.5,SKL=0.5,ABL=1.5,AGI=0.5,EVA=0.5,TGH=1.5,RES=1,LCK=1,WT=1.5)

LVL={}
LVL["1"]=Level(1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15)
LVL["2"]=Level(1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3)
LVL["3"]=Level(1.45,1.45,1.45,1.45,1.45,1.45,1.45,1.45,1.45,1.45,1.45,1.45)
LVL["4"]=Level(1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6)
LVL["5"]=Level(1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75)
LVL["6"]=Level(1.9,1.9,1.9,1.9,1.9,1.9,1.9,1.9,1.9,1.9,1.9,1.9)
LVL["7"]=Level(2.05,2.05,2.05,2.05,2.05,2.05,2.05,2.05,2.05,2.05,2.05,2.05)
LVL["8"]=Level(2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2,2.2)
LVL["9"]=Level(2.35,2.35,2.35,2.35,2.35,2.35,2.35,2.35,2.35,2.35,2.35,2.35)
LVL["10"]=Level(2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5)
LVL["11"]=Level(2.65,2.65,2.65,2.65,2.65,2.65,2.65,2.65,2.65,2.65,2.65,2.65)
LVL["12"]=Level(2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8,2.8)
LVL["13"]=Level(2.95,2.95,2.95,2.95,2.95,2.95,2.95,2.95,2.95,2.95,2.95,2.95)
LVL["14"]=Level(3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1,3.1)
LVL["15"]=Level(3.25,3.25,3.25,3.25,3.25,3.25,3.25,3.25,3.25,3.25,3.25,3.25)
LVL["16"]=Level(3.4,3.4,3.4,3.4,3.4,3.4,3.4,3.4,3.4,3.4,3.4,3.4)
LVL["17"]=Level(3.55,3.55,3.55,3.55,3.55,3.55,3.55,3.55,3.55,3.55,3.55,3.55)
LVL["18"]=Level(3.7,3.7,3.7,3.7,3.7,3.7,3.7,3.7,3.7,3.7,3.7,3.7)
LVL["19"]=Level(3.85,3.85,3.85,3.85,3.85,3.85,3.85,3.85,3.85,3.85,3.85,3.85)
LVL["20"]=Level(4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0,4.0)

def MonsterFactory(Size,Mod,Beast,Level):
	SizeHP=SZM[Size].HP
	SizeENE=SZM[Size].ENE
	SizeSTR=SZM[Size].STR
	SizeSPR=SZM[Size].SPR
	SizeSKL=SZM[Size].SKL
	SizeABL=SZM[Size].ABL
	SizeAGI=SZM[Size].AGI
	SizeEVA=SZM[Size].EVA
	SizeTGH=SZM[Size].TGH
	SizeRES=SZM[Size].RES
	SizeLCK=SZM[Size].LCK
	SizeWT=SZM[Size].WT
	
	ModHP=MOD[Mod].ModHP
	ModENE=MOD[Mod].ModENE
	ModSTR=MOD[Mod].ModSTR
	ModSPR=MOD[Mod].ModSPR
	ModSKL=MOD[Mod].ModSKL
	ModABL=MOD[Mod].ModABL
	ModAGI=MOD[Mod].ModAGI
	ModEVA=MOD[Mod].ModEVA
	ModTGH=MOD[Mod].ModTGH
	ModRES=MOD[Mod].ModRES
	ModLCK=MOD[Mod].ModLCK
	ModWT=MOD[Mod].ModWT
	
	BaseHP=BDT[Beast].HP
	BaseENE=BDT[Beast].ENE
	BaseSTR=BDT[Beast].STR
	BaseSPR=BDT[Beast].SPR
	BaseSKL=BDT[Beast].SKL
	BaseABL=BDT[Beast].ABL
	BaseAGI=BDT[Beast].AGI
	BaseEVA=BDT[Beast].EVA
	BaseTGH=BDT[Beast].TGH
	BaseRES=BDT[Beast].RES
	BaseLCK=BDT[Beast].LCK
	BaseWT=BDT[Beast].WT
	
	LevelHP=LVL[Level].LHP
	LevelENE=LVL[Level].LENE
	LevelSTR=LVL[Level].LSTR
	LevelSPR=LVL[Level].LSPR
	LevelSKL=LVL[Level].LSKL
	LevelABL=LVL[Level].LABL
	LevelAGI=LVL[Level].LAGI
	LevelEVA=LVL[Level].LEVA
	LevelTGH=LVL[Level].LTGH
	LevelRES=LVL[Level].LRES
	LevelLCK=LVL[Level].LLCK
	LevelWT=LVL[Level].LWT
	
	MonsterHP=round(((BaseHP*ModHP)*SizeHP)*LevelHP)
	MonsterENE=round(((BaseENE*ModENE)*SizeENE)*LevelENE)
	MonsterSTR=round(((BaseSTR*ModSTR)*SizeSTR)*LevelSTR)
	MonsterSPR=round(((BaseSPR*ModSPR)*SizeSPR)*LevelSPR)
	MonsterSKL=round(((BaseSKL*ModSKL)*SizeSKL)*LevelSKL)
	MonsterABL=round(((BaseABL*ModABL)*SizeABL)*LevelABL)
	MonsterAGI=round(((BaseAGI*ModAGI)*SizeAGI)*LevelAGI)
	MonsterEVA=round(((BaseEVA*ModEVA)*SizeEVA)*LevelEVA)
	MonsterTGH=round(((BaseTGH*ModTGH)*SizeTGH)*LevelTGH)
	MonsterRES=round(((BaseRES*ModRES)*SizeRES)*LevelRES)
	MonsterLCK=round(((BaseLCK*ModLCK)*SizeLCK)*LevelLCK)
	MonsterWT=round(((BaseWT*ModWT)*SizeWT)*LevelWT)
	
	return(MonsterHP,MonsterENE,MonsterSTR,MonsterSPR,MonsterSKL,MonsterABL,MonsterAGI,MonsterEVA,MonsterTGH,MonsterRES,MonsterLCK,MonsterWT)

OmniMonsterData={}
for Inputs in MonsterFactoryInputs:
	OmniMonsterData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]]=MonsterFactory(Inputs[0],Inputs[1],Inputs[2],Inputs[3])