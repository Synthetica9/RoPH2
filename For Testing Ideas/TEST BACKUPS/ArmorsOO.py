Prefixs=("Normal","Reinforced","Attuned","Lightweight","Masterwork","Rejuvenating")
Materials=("Unobtanium","Silk","Leather","Cotton","Tin","Copper","Bronze","Gold","Cobalt","Tungsten","Shardsteel","Shardiron","Magenium","Steel","Iron","Cazenium","Hevisteel","Heviron","Rozenium","Chrome","Bismuth","Aluminum","Titanium","Silver","Brass","Lead","Orichalc","Platinum")
Armors=("Head","Torso","Arms","Legs","Feet","SmallShield","MediumShield","LargeShield")
Upgrades=("0","1","2","3","4","5","6","7","8","9","10")

ForgeAInputs=[]

for p in Prefixs:
	for m in Materials:
		for a in Armors:
			for u in Upgrades:
				ForgeAInputs.append((p,m,a,u))
class ARMPrefix(object):
	def __init__(self,Name="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell
PRE={}
PRE["Normal"]=ARMPrefix(Name="Normal",PR=1,MR=1,WT=1,Buy=1,Sell=1)
PRE["Masterwork"]=ARMPrefix(Name="Masterwork",PR=2,MR=2,WT=0.25,Buy=2.5,Sell=2.5)
PRE["Lightweight"]=ARMPrefix(Name="Lightweight",PR=0.75,MR=0.75,WT=0.5,Buy=1.5,Sell=1.5)
PRE["Reinforced"]=ARMPrefix(Name="Reinforced",PR=2,MR=1,WT=1.5,Buy=1.5,Sell=1.5)
PRE["Attuned"]=ARMPrefix(Name="Attuned",PR=1,MR=2,WT=1.5,Buy=1.5,Sell=1.5)
PRE["Rejuvenating"]=ARMPrefix(Name="Rejuvenating",PR=1,MR=1,WT=1,Buy=1.5,Sell=1.5)

class ARMMaterial(object):
	def __init__(self,Name="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

MAT={}
#Dummy Material
MAT["Unobtanium"]=ARMMaterial(Name="Unobtanium",PR=1,MR=1,WT=1,Buy=1,Sell=1)
#Tier I, Light
MAT["Silk"]=ARMMaterial(Name="Silk",PR=4,MR=8,WT=4,Buy=100,Sell=50)
MAT["Cotton"]=ARMMaterial(Name="Cotton",PR=5,MR=5,WT=3,Buy=100,Sell=50)
MAT["Leather"]=ARMMaterial(Name="Leather",PR=8,MR=4,WT=8,Buy=100,Sell=50)
#Tier I, Medium
MAT["Copper"]=ARMMaterial(Name="Copper",PR=3,MR=10,WT=10,Buy=120,Sell=60)
MAT["Bronze"]=ARMMaterial(Name="Bronze",PR=6,MR=6,WT=8,Buy=120,Sell=60)
MAT["Tin"]=ARMMaterial(Name="Tin",PR=10,MR=3,WT=12,Buy=120,Sell=60)
#Tier I, Heavy
MAT["Gold"]=ARMMaterial(Name="Gold",PR=4,MR=14,WT=18,Buy=150,Sell=75)
MAT["Cobalt"]=ARMMaterial(Name="Cobalt",PR=8,MR=8,WT=15,Buy=150,Sell=75)
MAT["Tungsten"]=ARMMaterial(Name="Tungsten",PR=14,MR=4,WT=21,Buy=150,Sell=75)

#Tier II, Light
MAT["Magenium"]=ARMMaterial(Name="Magenium",PR=9,MR=18,WT=19,Buy=200,Sell=100)
MAT["Shardiron"]=ARMMaterial(Name="Shardiron",PR=11,MR=11,WT=17,Buy=200,Sell=100)
MAT["Shardsteel"]=ARMMaterial(Name="Shardsteel",PR=18,MR=9,WT=23,Buy=200,Sell=100)
#Tier II, Medium
MAT["Cazenium"]=ARMMaterial(Name="Cazenium",PR=8,MR=24,WT=26,Buy=300,Sell=150)
MAT["Iron"]=ARMMaterial(Name="Iron",PR=14,MR=14,WT=24,Buy=300,Sell=150)
MAT["Steel"]=ARMMaterial(Name="Steel",PR=24,MR=8,WT=30,Buy=300,Sell=150)
#Tier II, Heavy
MAT["Rozenium"]=ARMMaterial(Name="Rozenium",PR=8,MR=30,WT=33,Buy=400,Sell=200)
MAT["Heviron"]=ARMMaterial(Name="Heviron",PR=18,MR=18,WT=31,Buy=400,Sell=200)
MAT["Hevisteel"]=ARMMaterial(Name="Hevisteel",PR=30,MR=8,WT=37,Buy=400,Sell=200)

#Tier III, Light
MAT["Bismuth"]=ARMMaterial(Name="Bismuth",PR=20,MR=40,WT=36,Buy=500,Sell=250)
MAT["Aluminum"]=ARMMaterial(Name="Aluminum",PR=24,MR=24,WT=34,Buy=500,Sell=250)
MAT["Chrome"]=ARMMaterial(Name="Chrome",PR=40,MR=20,WT=38,Buy=500,Sell=250)
#Tier III, Medium
MAT["Silver"]=ARMMaterial(Name="Silver",PR=16,MR=48,WT=40,Buy=600,Sell=300)
MAT["Brass"]=ARMMaterial(Name="Brass",PR=29,MR=29,WT=39,Buy=600,Sell=300)
MAT["Titanium"]=ARMMaterial(Name="Titanium",PR=48,MR=16,WT=45,Buy=600,Sell=300)
#Tier III, Heavy
MAT["Orichalc"]=ARMMaterial(Name="Orichalc",PR=14,MR=54,WT=50,Buy=700,Sell=350)
MAT["Platinum"]=ARMMaterial(Name="Platinum",PR=32,MR=32,WT=47,Buy=700,Sell=350)
MAT["Lead"]=ARMMaterial(Name="Lead",PR=54,MR=14,WT=55,Buy=700,Sell=350)

#Tier IV, Light
MAT["Crystalite"]=ARMMaterial(Name="Crystalite",PR=29,MR=58,WT=55,Buy=800,Sell=400)
MAT["Orionite"]=ARMMaterial(Name="Orionite",PR=35,MR=35,WT=50,Buy=800,Sell=400)
MAT["Adamantite"]=ARMMaterial(Name="Adamantite",PR=58,MR=29,WT=60,Buy=800,Sell=400)
#Tier IV, Medium
MAT["Solite"]=ARMMaterial(Name="Solite",PR=21,MR=62,WT=65,Buy=900,Sell=450)
MAT["Territe"]=ARMMaterial(Name="Territe",PR=37,MR=37,WT=60,Buy=900,Sell=450)
MAT["Lunalite"]=ARMMaterial(Name="Lunalite",PR=62,MR=21,WT=65,Buy=900,Sell=450)
#Tier IV, Heavy
MAT["Sorcium"]=ARMMaterial(Name="Sorcium",PR=19,MR=75,WT=68,Buy=1000,Sell=500)
MAT["Brinieum"]=ARMMaterial(Name="Brinieum",PR=45,MR=45,WT=65,Buy=1000,Sell=500)
MAT["Impervium"]=ARMMaterial(Name="Impervium",PR=75,MR=19,WT=75,Buy=1000,Sell=500)

class Armor(object):
	def __init__(self,Name="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

ARM={}
ARM["Head"]=Armor(Name="Head",PR=0.1,MR=0.1,WT=0.1,Buy=0.1,Sell=0.1)
ARM["Torso"]=Armor(Name="Torso",PR=0.3,MR=0.3,WT=0.3,Buy=0.3,Sell=0.3)
ARM["Arms"]=Armor(Name="Arms",PR=0.15,MR=0.15,WT=0.15,Buy=0.15,Sell=0.15)
ARM["Legs"]=Armor(Name="Legs",PR=0.15,MR=0.15,WT=0.15,Buy=0.15,Sell=0.15)
ARM["Feet"]=Armor(Name="Feet",PR=0.1,MR=0.1,WT=0.1,Buy=0.1,Sell=0.1)
ARM["SmallShield"]=Armor(Name="SmallShield",PR=0.75,MR=0.75,WT=0.75,Buy=0.75,Sell=0.75)
ARM["MediumShield"]=Armor(Name="MediumShield",PR=1,MR=1,WT=1,Buy=1,Sell=1)
ARM["LargeShield"]=Armor(Name="LargeShield",PR=1.25,MR=1.25,WT=1.25,Buy=1.25,Sell=1.25)
class Upgrade(object):
	def __init__(self,Name="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell
UP={}
UP["0"]=Upgrade(Name="0",PR=1,MR=1,WT=1,Buy=1,Sell=1)
UP["1"]=Upgrade(Name="1",PR=1.1,MR=1.1,WT=0.95,Buy=1.1,Sell=1.1)
UP["2"]=Upgrade(Name="2",PR=1.2,MR=1.2,WT=0.9,Buy=1.2,Sell=1.2)
UP["3"]=Upgrade(Name="3",PR=1.3,MR=1.3,WT=0.85,Buy=1.3,Sell=1.3)
UP["4"]=Upgrade(Name="4",PR=1.4,MR=1.4,WT=0.8,Buy=1.4,Sell=1.4)
UP["5"]=Upgrade(Name="5",PR=1.5,MR=1.5,WT=0.75,Buy=1.5,Sell=1.5)
UP["6"]=Upgrade(Name="6",PR=1.6,MR=1.6,WT=0.7,Buy=1.6,Sell=1.6)
UP["7"]=Upgrade(Name="7",PR=1.7,MR=1.7,WT=0.65,Buy=1.7,Sell=1.7)
UP["8"]=Upgrade(Name="8",PR=1.8,MR=1.8,WT=0.6,Buy=1.8,Sell=1.8)
UP["9"]=Upgrade(Name="9",PR=1.9,MR=1.9,WT=0.55,Buy=1.9,Sell=1.9)
UP["10"]=Upgrade(Name="10",PR=2,MR=2,WT=0.5,Buy=2,Sell=2)

def ForgeA(Prefix,Material,Armor,Upgrade):
	PrefixPR=PRE[Prefix].PR
	PrefixMR=PRE[Prefix].MR
	PrefixWT=PRE[Prefix].WT
	PrefixBuy=PRE[Prefix].Buy
	PrefixSell=PRE[Prefix].Sell

	OrePR=MAT[Material].PR
	OreMR=MAT[Material].MR
	OreWT=MAT[Material].WT
	OreBuy=MAT[Material].Buy
	OreSell=MAT[Material].Sell

	SmithPR=ARM[Armor].PR
	SmithMR=ARM[Armor].MR
	SmithWT=ARM[Armor].WT
	SmithBuy=ARM[Armor].Buy
	SmithSell=ARM[Armor].Sell

	UpgradePR=UP[Upgrade].PR
	UpgradeMR=UP[Upgrade].MR
	UpgradeWT=UP[Upgrade].WT
	UpgradeBuy=UP[Upgrade].Buy
	UpgradeSell=UP[Upgrade].Sell

	ProductPR=max(round(((OrePR*SmithPR)*UpgradePR)*PrefixPR),1)
	ProductMR=max(round(((OreMR*SmithMR)*UpgradeMR)*PrefixMR),1)
	ProductWT=max(round(((OreWT*SmithWT)*UpgradeWT)*PrefixWT),1)
	ProductBuy=max(round(((OreBuy*SmithBuy)*UpgradeBuy)*PrefixBuy),1)
	ProductSell=max(round(((OreSell*SmithSell)*UpgradeSell)*PrefixSell),1)
	
	return(ProductPR,ProductMR,ProductWT,ProductBuy,ProductSell)

OmniArmorData={}
for Inputs in ForgeAInputs:
	OmniArmorData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]]=ForgeA(Inputs[0],Inputs[1],Inputs[2],Inputs[3])

