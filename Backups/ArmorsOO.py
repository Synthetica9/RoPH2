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
PRE["Rejuvenating"]=ARMPrefix(Name="Rejuvenating",PR=1,MR=1,WT=1,Buy=1.33,Sell=1.33)

class ARMMaterial(object):
	def __init__(self,Name="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

MAT={}
#Dummy Material
MAT["Unobtanium"]=ARMMaterial(Name="Unobtanium",PR=0,MR=0,WT=0,Buy=0,Sell=0)
#Tier I, Light
MAT["Silk"]=ARMMaterial(Name="Silk",PR=3,MR=6,WT=6,Buy=100,Sell=50)
MAT["Cotton"]=ARMMaterial(Name="Cotton",PR=4,MR=4,WT=10,Buy=100,Sell=50)
MAT["Leather"]=ARMMaterial(Name="Leather",PR=6,MR=3,WT=10,Buy=100,Sell=50)
#Tier I, Medium
MAT["Tin"]=ARMMaterial(Name="Tin",PR=8,MR=4,WT=8,Buy=120,Sell=60)
MAT["Copper"]=ARMMaterial(Name="Copper",PR=4,MR=8,WT=6,Buy=120,Sell=60)
MAT["Bronze"]=ARMMaterial(Name="Bronze",PR=7,MR=7,WT=7,Buy=120,Sell=60)
#Tier I, Heavy
MAT["Gold"]=ARMMaterial(Name="Gold",PR=6,MR=12,WT=13,Buy=150,Sell=75)
MAT["Cobalt"]=ARMMaterial(Name="Cobalt",PR=10,MR=10,WT=10,Buy=150,Sell=75)
MAT["Tungsten"]=ARMMaterial(Name="Tungsten",PR=12,MR=6,WT=13,Buy=150,Sell=75)

#Tier II, Light
MAT["Shardsteel"]=ARMMaterial(Name="Shardsteel",PR=16,MR=8,WT=8,Buy=200,Sell=100)
MAT["Magenium"]=ARMMaterial(Name="Magenium",PR=8,MR=16,WT=8,Buy=200,Sell=100)
MAT["Shardiron"]=ARMMaterial(Name="Shardiron",PR=13,MR=13,WT=13,Buy=200,Sell=100)
#Tier II, Medium
MAT["Steel"]=ARMMaterial(Name="Steel",PR=24,MR=12,WT=20,Buy=300,Sell=150)
MAT["Cazenium"]=ARMMaterial(Name="Cazenium",PR=12,MR=24,WT=15,Buy=300,Sell=150)
MAT["Iron"]=ARMMaterial(Name="Iron",PR=18,MR=18,WT=18,Buy=300,Sell=150)
#Tier II, Heavy
MAT["Hevisteel"]=ARMMaterial(Name="Hevisteel",PR=30,MR=15,WT=25,Buy=400,Sell=200)
MAT["Rozenium"]=ARMMaterial(Name="Rozenium",PR=15,MR=30,WT=21,Buy=400,Sell=200)
MAT["Heviron"]=ARMMaterial(Name="Heviron",PR=24,MR=24,WT=23,Buy=400,Sell=200)

#Tier III, Light
MAT["Chrome"]=ARMMaterial(Name="Chrome",PR=20,MR=10,WT=10,Buy=500,Sell=250)
MAT["Bismuth"]=ARMMaterial(Name="Bismuth",PR=10,MR=20,WT=10,Buy=500,Sell=250)
MAT["Aluminum"]=ARMMaterial(Name="Aluminum",PR=15,MR=15,WT=5,Buy=500,Sell=250)
#Tier III, Medium
MAT["Titanium"]=ARMMaterial(Name="Titanium",PR=30,MR=15,WT=30,Buy=600,Sell=300)
MAT["Silver"]=ARMMaterial(Name="Silver",PR=15,MR=30,WT=25,Buy=600,Sell=300)
MAT["Brass"]=ARMMaterial(Name="Brass",PR=22,MR=22,WT=22,Buy=600,Sell=300)
#Tier III, Heavy
MAT["Lead"]=ARMMaterial(Name="Lead",PR=40,MR=20,WT=40,Buy=700,Sell=350)
MAT["Orichalc"]=ARMMaterial(Name="Orichalc",PR=20,MR=40,WT=30,Buy=700,Sell=350)
MAT["Platinum"]=ARMMaterial(Name="Platinum",PR=30,MR=30,WT=35,Buy=700,Sell=350)

#Tier IV, Light
MAT["Adamantite"]=ARMMaterial(Name="Adamantite",PR=30,MR=15,WT=30,Buy=800,Sell=400)
MAT["Crystalite"]=ARMMaterial(Name="Crystalite",PR=15,MR=30,WT=25,Buy=800,Sell=400)
MAT["Orionite"]=ARMMaterial(Name="Orionite",PR=20,MR=20,WT=20,Buy=800,Sell=400)
#Tier IV, Medium
MAT["Lunalite"]=ARMMaterial(Name="Lunalite",PR=44,MR=22,WT=40,Buy=900,Sell=450)
MAT["Solite"]=ARMMaterial(Name="Solite",PR=22,MR=44,WT=35,Buy=900,Sell=450)
MAT["Territe"]=ARMMaterial(Name="Territe",PR=33,MR=33,WT=30,Buy=900,Sell=450)
#Tier IV, Heavy
MAT["Impervium"]=ARMMaterial(Name="Impervium",PR=50,MR=25,WT=50,Buy=1000,Sell=500)
MAT["Sorcium"]=ARMMaterial(Name="Sorcium",PR=25,MR=50,WT=40,Buy=1000,Sell=500)
MAT["Brinieum"]=ARMMaterial(Name="Brinieum",PR=45,MR=45,WT=45,Buy=1000,Sell=500)

class Armor(object):
	def __init__(self,Name="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

ARM={}
ARM["Head"]=Armor(Name="Head",PR=0.1,MR=0.1,WT=0.1,Buy=0.1,Sell=0.1)
ARM["Torso"]=Armor(Name="Torso",PR=0.5,MR=0.5,WT=0.5,Buy=0.5,Sell=0.5)
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

