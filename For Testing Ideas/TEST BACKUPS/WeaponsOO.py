Prefixs=("Normal","Reinforced","Attuned","Accurate","Lightweight","Balanced","Masterwork","Festive","Blazing","Breezy","Electric","Icy","Stony")
Materials=("Unobtanium","Ivory","Bone","Wood","Tin","Copper","Bronze","Gold","Cobalt","Tungsten","Shardsteel","Shardiron","Magenium","Steel","Iron","Cazenium","Hevisteel","Heviron","Rozenium","Chrome","Bismuth","Aluminum","Titanium","Silver","Brass","Lead","Orichalc","Platinum")
Weapons=("Knife","Saber","Greatsword","Polearm","Battlestaff","Claw","Whip","Knuckles","Cane","Wand","Talis","Rod","Slicer","Bow","Crossbow","Handbow","TwinPistol","Mechgun","Rifle","Flail","Warhammer","Flute","Guitar","Saxophone","Yoyo","Tome","Battlecannon","Mic","Arrow")
Upgrades=("0","1","2","3","4","5","6","7","8","9","10")

ForgeWInputs=[]

for p in Prefixs:
	for m in Materials:
		for w in Weapons:
			for u in Upgrades:
				ForgeWInputs.append((p,m,w,u))


class WEPPrefix(object):
	def __init__(self,Name="None",PD=0,MD=0,AC=0,WT=0,Buy=0,Sell=0):
		self.PD=PD
		self.MD=MD
		self.AC=AC
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

PRE={}
PRE["Normal"]=WEPPrefix("Normal",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Festive"]=WEPPrefix("Festive",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Breezy"]=WEPPrefix("Breezy",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Blazing"]=WEPPrefix("Blazing",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Electric"]=WEPPrefix("Electric",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Icy"]=WEPPrefix("Icy",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Stony"]=WEPPrefix("Stony",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Sunny"]=WEPPrefix("Sunny",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Lunar"]=WEPPrefix("Lunar",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Stormy"]=WEPPrefix("Stormy",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Voidal"]=WEPPrefix("Voidal",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Temporal"]=WEPPrefix("Temporal",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
PRE["Reinforced"]=WEPPrefix("Reinforced",PD=2,MD=1,AC=0.5,WT=1.5,Buy=1.5,Sell=1.5)
PRE["Attuned"]=WEPPrefix("Attuned",PD=1,MD=2,AC=0.5,WT=1.5,Buy=1.5,Sell=1.5)
PRE["Accurate"]=WEPPrefix("Accurate",PD=0.5,MD=0.5,AC=2,WT=1,Buy=2,Sell=2)
PRE["Lightweight"]=WEPPrefix("Lightweight",PD=0.75,MD=0.75,AC=1,WT=0.5,Buy=1.5,Sell=1.5)
PRE["Balanced"]=WEPPrefix("Balanced",PD=1.25,MD=1.25,AC=1.25,WT=0.75,Buy=1.25,Sell=1.25)
PRE["Masterwork"]=WEPPrefix("Masterwork",PD=2,MD=2,AC=2,WT=0.25,Buy=2.5,Sell=2.5)

class WEPMaterial(object):
	def __init__(self,Name="Unobtanium",PD=0,MD=0,AC=0,WT=0,Buy=0,Sell=0):
		self.PD=PD
		self.MD=MD
		self.AC=AC
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

MAT={}
#Dummy Material
MAT["Unobtanium"]=WEPMaterial("Unobtanium",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
#Tier I, Light
MAT["Ivory"]=WEPMaterial("Ivory",PD=4,MD=8,AC=8,WT=4,Buy=100,Sell=50)
MAT["Wood"]=WEPMaterial("Wood",PD=5,MD=5,AC=8,WT=3,Buy=100,Sell=50)
MAT["Bone"]=WEPMaterial("Bone",PD=8,MD=4,AC=8,WT=8,Buy=100,Sell=50)
#Tier I, Medium
MAT["Copper"]=WEPMaterial("Copper",PD=3,MD=10,AC=4,WT=10,Buy=120,Sell=60)
MAT["Bronze"]=WEPMaterial("Bronze",PD=6,MD=6,AC=6,WT=8,Buy=120,Sell=60)
MAT["Tin"]=WEPMaterial("Tin",PD=10,MD=3,AC=4,WT=12,Buy=120,Sell=60)
#Tier I, Heavy
MAT["Gold"]=WEPMaterial("Gold",PD=4,MD=14,AC=0,WT=18,Buy=150,Sell=75)
MAT["Cobalt"]=WEPMaterial("Cobalt",PD=8,MD=8,AC=2,WT=15,Buy=150,Sell=75)
MAT["Tungsten"]=WEPMaterial("Tungsten",PD=14,MD=4,AC=0,WT=21,Buy=150,Sell=75)

#Tier II, Light
MAT["Magenium"]=WEPMaterial("Magenium",PD=9,MD=18,AC=12,WT=19,Buy=200,Sell=100)
MAT["Shardiron"]=WEPMaterial("Shardiron",PD=11,MD=11,AC=15,WT=17,Buy=200,Sell=100)
MAT["Shardsteel"]=WEPMaterial("Shardsteel",PD=18,MD=9,AC=12,WT=23,Buy=200,Sell=100)
#Tier II, Medium
MAT["Cazenium"]=WEPMaterial("Cazenium",PD=8,MD=24,AC=9,WT=26,Buy=300,Sell=150)
MAT["Iron"]=WEPMaterial("Iron",PD=14,MD=14,AC=12,WT=24,Buy=300,Sell=150)
MAT["Steel"]=WEPMaterial("Steel",PD=24,MD=8,AC=9,WT=30,Buy=300,Sell=150)
#Tier II, Heavy
MAT["Rozenium"]=WEPMaterial("Rozenium",PD=8,MD=30,AC=3,WT=33,Buy=400,Sell=200)
MAT["Heviron"]=WEPMaterial("Heviron",PD=18,MD=18,AC=6,WT=31,Buy=400,Sell=200)
MAT["Hevisteel"]=WEPMaterial("Hevisteel",PD=30,MD=8,AC=3,WT=37,Buy=400,Sell=200)

#Tier III, Light
MAT["Bismuth"]=WEPMaterial("Bismuth",PD=20,MD=40,AC=15,WT=36,Buy=500,Sell=250)
MAT["Aluminum"]=WEPMaterial("Aluminum",PD=24,MD=24,AC=20,WT=34,Buy=500,Sell=250)
MAT["Chrome"]=WEPMaterial("Chrome",PD=40,MD=20,AC=15,WT=38,Buy=500,Sell=250)
#Tier III, Medium
MAT["Silver"]=WEPMaterial("Silver",PD=16,MD=48,AC=12,WT=40,Buy=600,Sell=300)
MAT["Brass"]=WEPMaterial("Brass",PD=29,MD=29,AC=14,WT=39,Buy=600,Sell=300)
MAT["Titanium"]=WEPMaterial("Titanium",PD=48,MD=16,AC=12,WT=45,Buy=600,Sell=300)
#Tier III, Heavy
MAT["Orichalc"]=WEPMaterial("Orichalc",PD=14,MD=54,AC=10,WT=50,Buy=700,Sell=350)
MAT["Platinum"]=WEPMaterial("Platinum",PD=32,MD=32,AC=15,WT=47,Buy=700,Sell=350)
MAT["Lead"]=WEPMaterial("Lead",PD=54,MD=14,AC=10,WT=55,Buy=700,Sell=350)

#Tier IV, Light
MAT["Crystalite"]=WEPMaterial("Crystalite",PD=29,MD=58,AC=25,WT=55,Buy=800,Sell=400)
MAT["Orionite"]=WEPMaterial("Orionite",PD=35,MD=35,AC=35,WT=50,Buy=800,Sell=400)
MAT["Adamantite"]=WEPMaterial("Adamantite",PD=58,MD=29,AC=25,WT=60,Buy=800,Sell=400)
#Tier IV, Medium
MAT["Solite"]=WEPMaterial("Solite",PD=21,MD=62,AC=9,WT=65,Buy=900,Sell=450)
MAT["Territe"]=WEPMaterial("Territe",PD=37,MD=37,AC=12,WT=60,Buy=900,Sell=450)
MAT["Lunalite"]=WEPMaterial("Lunalite",PD=62,MD=21,AC=9,WT=65,Buy=900,Sell=450)
#Tier IV, Heavy
MAT["Sorcium"]=WEPMaterial("Sorcium",PD=19,MD=75,AC=5,WT=68,Buy=1000,Sell=500)
MAT["Brinieum"]=WEPMaterial("Brinieum",PD=45,MD=45,AC=10,WT=65,Buy=1000,Sell=500)
MAT["Impervium"]=WEPMaterial("Impervium",PD=75,MD=19,AC=5,WT=75,Buy=1000,Sell=500)

class Weapon(object):
	def __init__(self,Name="None",PD=0,MD=0,AC=0,WT=0,Buy=0,Sell=0):
		self.PD=PD
		self.MD=MD
		self.AC=AC
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

WEP={}

WEP["Knife"]=Weapon(Name="Knife",PD=0.65,MD=0.65,AC=1.25,WT=0.25,Buy=0.33,Sell=0.33)
WEP["Saber"]=Weapon(Name="Saber",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
WEP["Polearm"]=Weapon(Name="Polearm",PD=1.15,MD=1.15,AC=1.15,WT=1.15,Buy=1.15,Sell=1.15)
WEP["Greatsword"]=Weapon(Name="Greatsword",PD=1.67,MD=1.67,AC=0.67,WT=1.4,Buy=1.67,Sell=1.67)
WEP["Knuckles"]=Weapon(Name="Knuckles",PD=0.5,MD=0.5,AC=1.5,WT=0.25,Buy=0.5,Sell=0.5)
WEP["Warhammer"]=Weapon(Name="Warhammer",PD=1.5,MD=0,AC=0.6,WT=1.4,Buy=1.5,Sell=1.5)
WEP["Flail"]=Weapon(Name="Flail",PD=1.15,MD=0.85,AC=0.85,WT=1.15,Buy=1.15,Sell=1.15)
WEP["Whip"]=Weapon(Name="Whip",PD=1,MD=1,AC=0.7,WT=1.3,Buy=1.25,Sell=1.25)
WEP["Yoyo"]=Weapon(Name="Yoyo",PD=1.25,MD=1.25,AC=0.5,WT=1.5,Buy=1.4,Sell=1.4)
WEP["Cane"]=Weapon(Name="Cane",PD=0.75,MD=1.25,AC=0.7,WT=1.3,Buy=1.15,Sell=1.15)
WEP["Claw"]=Weapon(Name="Claw",PD=0.9,MD=0.9,AC=1.1,WT=0.9,Buy=1,Sell=1)
WEP["Battlestaff"]=Weapon(Name="Battlestaff",PD=1.15,MD=1.15,AC=0.85,WT=1.15,Buy=1.15,Sell=1.15)
WEP["Talis"]=Weapon(Name="Talis",PD=1.15,MD=0.7,AC=1.15,WT=0.33,Buy=0.7,Sell=0.7)
WEP["Wand"]=Weapon(Name="Wand",PD=0,MD=0,AC=3,WT=0.1,Buy=2,Sell=2)
WEP["Rod"]=Weapon(Name="Rod",PD=0.33,MD=1.33,AC=1.33,WT=1.33,Buy=1.5,Sell=1.5)
WEP["Tome"]=Weapon(Name="Tome",PD=0,MD=2,AC=0.6,WT=1.4,Buy=2,Sell=2)
WEP["Slicer"]=Weapon(Name="Slicer",PD=0.67,MD=0.67,AC=0.67,WT=0.67,Buy=0.67,Sell=0.67)
WEP["Bow"]=Weapon(Name="Bow",PD=1.15,MD=1.15,AC=1.15,WT=1.15,Buy=1.15,Sell=1.15)
WEP["Crossbow"]=Weapon(Name="Crossbow",PD=1.33,MD=0.67,AC=1,WT=1.33,Buy=1.33,Sell=1.33)
WEP["Handbow"]=Weapon(Name="Handbow",PD=1.16,MD=0.84,AC=0.84,WT=1.16,Buy=1.1,Sell=1.1)
WEP["TwinPistol"]=Weapon(Name="TwinPistol",PD=0.7,MD=0.7,AC=1,WT=0.85,Buy=1,Sell=1)
WEP["Mechgun"]=Weapon(Name="Mechgun",PD=0.45,MD=0.45,AC=1.25,WT=1.25,Buy=1.2,Sell=1.2)
WEP["Rifle"]=Weapon(Name="Rifle",PD=1.25,MD=0.75,AC=1.5,WT=1.5,Buy=1.5,Sell=1.5)
WEP["Battlecannon"]=Weapon(Name="Battlecannon",PD=2,MD=0,AC=0.75,WT=2,Buy=2.5,Sell=2.5)
WEP["Mic"]=Weapon(Name="Mic",PD=0,MD=0,AC=1.75,WT=0.25,Buy=2,Sell=2)
WEP["Guitar"]=Weapon(Name="Guitar",PD=1,MD=1.25,AC=0.85,WT=1.33,Buy=1.4,Sell=1.4)
WEP["Flute"]=Weapon(Name="Flute",PD=0.25,MD=1.25,AC=1.5,WT=0.1,Buy=1.2,Sell=1.2)
WEP["Saxophone"]=Weapon(Name="Saxophone",PD=0,MD=3,AC=0.6,WT=1.4,Buy=2.5,Sell=2.5)
WEP["Arrow"]=Weapon(Name="Arrow",PD=1,MD=1,AC=1,WT=0,Buy=0.05,Sell=0.05)


class Upgrade(object):
	def __init__(self,Name="None",PD=0,MD=0,AC=0,WT=0,Buy=0,Sell=0):
		self.PD=PD
		self.MD=MD
		self.AC=AC
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

UP={}
UP["0"]=Upgrade(Name="0",PD=1,MD=1,AC=1,WT=1,Buy=1,Sell=1)
UP["1"]=Upgrade(Name="1",PD=1.1,MD=1.1,AC=1.1,WT=0.95,Buy=1.1,Sell=1.1)
UP["2"]=Upgrade(Name="2",PD=1.2,MD=1.2,AC=1.2,WT=0.9,Buy=1.2,Sell=1.2)
UP["3"]=Upgrade(Name="3",PD=1.3,MD=1.3,AC=1.3,WT=0.85,Buy=1.3,Sell=1.3)
UP["4"]=Upgrade(Name="4",PD=1.4,MD=1.4,AC=1.4,WT=0.8,Buy=1.4,Sell=1.4)
UP["5"]=Upgrade(Name="5",PD=1.5,MD=1.5,AC=1.5,WT=0.75,Buy=1.5,Sell=1.5)
UP["6"]=Upgrade(Name="6",PD=1.6,MD=1.6,AC=1.6,WT=0.7,Buy=1.6,Sell=1.6)
UP["7"]=Upgrade(Name="7",PD=1.7,MD=1.7,AC=1.7,WT=0.65,Buy=1.7,Sell=1.7)
UP["8"]=Upgrade(Name="8",PD=1.8,MD=1.8,AC=1.8,WT=0.6,Buy=1.8,Sell=1.8)
UP["9"]=Upgrade(Name="9",PD=1.9,MD=1.9,AC=1.9,WT=0.55,Buy=1.9,Sell=1.9)
UP["10"]=Upgrade(Name="10",PD=2,MD=2,AC=2,WT=0.5,Buy=2,Sell=2)

def ForgeW(Prefix,Material,Weapon,Upgrade):
	PrefixPD=PRE[Prefix].PD
	PrefixMD=PRE[Prefix].MD
	PrefixAC=PRE[Prefix].AC
	PrefixWT=PRE[Prefix].WT
	PrefixBuy=PRE[Prefix].Buy
	PrefixSell=PRE[Prefix].Sell

	OrePD=MAT[Material].PD
	OreMD=MAT[Material].MD
	OreAC=MAT[Material].AC
	OreWT=MAT[Material].WT
	OreBuy=MAT[Material].Buy
	OreSell=MAT[Material].Sell

	SmithPD=WEP[Weapon].PD
	SmithMD=WEP[Weapon].MD
	SmithAC=WEP[Weapon].AC
	SmithWT=WEP[Weapon].WT
	SmithBuy=WEP[Weapon].Buy
	SmithSell=WEP[Weapon].Sell

	UpgradePD=UP[Upgrade].PD
	UpgradeMD=UP[Upgrade].MD
	UpgradeAC=UP[Upgrade].AC
	UpgradeWT=UP[Upgrade].WT
	UpgradeBuy=UP[Upgrade].Buy
	UpgradeSell=UP[Upgrade].Sell

	ProductPD=max(round(((OrePD*SmithPD)*UpgradePD)*PrefixPD),1)
	ProductMD=max(round(((OreMD*SmithMD)*UpgradeMD)*PrefixMD),1)
	ProductAC=max(round(((OreAC*SmithAC)*UpgradeAC)*PrefixAC),1)
	ProductWT=max(round(((OreWT*SmithWT)*UpgradeWT)*PrefixWT),1)
	ProductBuy=max(round(((OreBuy*SmithBuy)*UpgradeBuy)*PrefixBuy),1)
	ProductSell=max(round(((OreSell*SmithSell)*UpgradeSell)*PrefixSell),1)
	
	return(ProductPD,ProductMD,ProductAC,ProductWT,ProductBuy,ProductSell)

OmniWeaponData={}
for Inputs in ForgeWInputs:
	OmniWeaponData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]]=ForgeW(Inputs[0],Inputs[1],Inputs[2],Inputs[3])

