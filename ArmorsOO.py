Prefixs=("Normal","Reinforced","Attuned","Lightweight","Masterwork","Rejuvenating")
Materials=("Unobtanium","Silk","Leather","Cotton","Tin","Copper","Bronze","Gold","Cobalt","Tungsten","Shardsteel","Shardiron","Magenium","Steel","Iron","Cazenium","Hevisteel","Heviron","Rozenium","Chrome","Bismuth","Aluminum","Titanium","Silver","Brass","Lead","Orichalc","Platinum","Crystalite","Orionite","Adamantite","Solite","Lunalite","Territe","Sorcium","Brinium","Impervium")
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
	def __init__(self,Name="None",WTClass="Feather",OreType="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell
		self.Name=Name
		self.WTClass=WTClass
		self.OreType=OreType

MAT={}
#Dummy Material
MAT["Unobtanium"]=ARMMaterial(Name="Unobtanium",PR=0,MR=0,WT=0,Buy=0,Sell=0,WTClass="Feather",OreType="B")
#Tier I, Light
MAT["Silk"]=ARMMaterial(Name="Silk",PR=4,MR=8,WT=4,Buy=100,Sell=50,WTClass="Light",OreType="M")
MAT["Cotton"]=ARMMaterial(Name="Cotton",PR=5,MR=5,WT=3,Buy=100,Sell=50,WTClass="Light",OreType="B")
MAT["Leather"]=ARMMaterial(Name="Leather",PR=8,MR=4,WT=8,Buy=100,Sell=50,WTClass="Light",OreType="P")
#Tier I, Medium
MAT["Copper"]=ARMMaterial(Name="Copper",PR=3,MR=10,WT=10,Buy=120,Sell=60,WTClass="Medium",OreType="M")
MAT["Bronze"]=ARMMaterial(Name="Bronze",PR=6,MR=6,WT=8,Buy=120,Sell=60,WTClass="Medium",OreType="B")
MAT["Tin"]=ARMMaterial(Name="Tin",PR=10,MR=3,WT=12,Buy=120,Sell=60,WTClass="Medium",OreType="P")
#Tier I, Heavy
MAT["Gold"]=ARMMaterial(Name="Gold",PR=4,MR=14,WT=18,Buy=140,Sell=70,WTClass="Heavy",OreType="M")
MAT["Cobalt"]=ARMMaterial(Name="Cobalt",PR=10,MR=10,WT=16,Buy=140,Sell=70,WTClass="Heavy",OreType="B")
MAT["Tungsten"]=ARMMaterial(Name="Tungsten",PR=14,MR=4,WT=21,Buy=140,Sell=70,WTClass="Heavy",OreType="P")

#Tier II, Light
MAT["Magenium"]=ARMMaterial(Name="Magenium",PR=9,MR=18,WT=19,Buy=200,Sell=100,WTClass="Light",OreType="M")
MAT["Shardiron"]=ARMMaterial(Name="Shardiron",PR=11,MR=11,WT=17,Buy=200,Sell=100,WTClass="Light",OreType="B")
MAT["Shardsteel"]=ARMMaterial(Name="Shardsteel",PR=18,MR=9,WT=23,Buy=200,Sell=100,WTClass="Light",OreType="P")
#Tier II, Medium
MAT["Cazenium"]=ARMMaterial(Name="Cazenium",PR=8,MR=24,WT=26,Buy=300,Sell=160,WTClass="Medium",OreType="M")
MAT["Iron"]=ARMMaterial(Name="Iron",PR=14,MR=14,WT=24,Buy=300,Sell=160,WTClass="Medium",OreType="B")
MAT["Steel"]=ARMMaterial(Name="Steel",PR=24,MR=8,WT=30,Buy=300,Sell=160,WTClass="Medium",OreType="P")
#Tier II, Heavy
MAT["Rozenium"]=ARMMaterial(Name="Rozenium",PR=8,MR=30,WT=33,Buy=400,Sell=200,WTClass="Heavy",OreType="M")
MAT["Heviron"]=ARMMaterial(Name="Heviron",PR=18,MR=18,WT=31,Buy=400,Sell=200,WTClass="Heavy",OreType="B")
MAT["Hevisteel"]=ARMMaterial(Name="Hevisteel",PR=30,MR=8,WT=37,Buy=400,Sell=200,WTClass="Heavy",OreType="P")

#Tier III, Light
MAT["Bismuth"]=ARMMaterial(Name="Bismuth",PR=20,MR=40,WT=36,Buy=500,Sell=260,WTClass="Light",OreType="M")
MAT["Aluminum"]=ARMMaterial(Name="Aluminum",PR=24,MR=24,WT=34,Buy=500,Sell=260,WTClass="Light",OreType="B")
MAT["Chrome"]=ARMMaterial(Name="Chrome",PR=40,MR=20,WT=38,Buy=500,Sell=260,WTClass="Light",OreType="P")
#Tier III, Medium
MAT["Silver"]=ARMMaterial(Name="Silver",PR=16,MR=48,WT=40,Buy=600,Sell=300,WTClass="Medium",OreType="M")
MAT["Brass"]=ARMMaterial(Name="Brass",PR=29,MR=29,WT=39,Buy=600,Sell=300,WTClass="Medium",OreType="B")
MAT["Titanium"]=ARMMaterial(Name="Titanium",PR=48,MR=16,WT=45,Buy=600,Sell=300,WTClass="Medium",OreType="P")
#Tier III, Heavy
MAT["Orichalc"]=ARMMaterial(Name="Orichalc",PR=14,MR=54,WT=50,Buy=700,Sell=360,WTClass="Heavy",OreType="M")
MAT["Platinum"]=ARMMaterial(Name="Platinum",PR=32,MR=32,WT=47,Buy=700,Sell=360,WTClass="Heavy",OreType="B")
MAT["Lead"]=ARMMaterial(Name="Lead",PR=54,MR=14,WT=55,Buy=700,Sell=360,WTClass="Heavy",OreType="P")

#Tier IV, Light
MAT["Crystalite"]=ARMMaterial(Name="Crystalite",PR=29,MR=58,WT=55,Buy=800,Sell=400,WTClass="Light",OreType="M")
MAT["Orionite"]=ARMMaterial(Name="Orionite",PR=35,MR=35,WT=50,Buy=800,Sell=400,WTClass="Light",OreType="B")
MAT["Adamantite"]=ARMMaterial(Name="Adamantite",PR=58,MR=29,WT=60,Buy=800,Sell=400,WTClass="Light",OreType="P")
#Tier IV, Medium
MAT["Solite"]=ARMMaterial(Name="Solite",PR=21,MR=62,WT=65,Buy=900,Sell=460,WTClass="Medium",OreType="M")
MAT["Territe"]=ARMMaterial(Name="Territe",PR=37,MR=37,WT=60,Buy=900,Sell=460,WTClass="Medium",OreType="B")
MAT["Lunalite"]=ARMMaterial(Name="Lunalite",PR=62,MR=21,WT=65,Buy=900,Sell=460,WTClass="Medium",OreType="P")
#Tier IV, Heavy
MAT["Sorcium"]=ARMMaterial(Name="Sorcium",PR=19,MR=75,WT=68,Buy=1000,Sell=500,WTClass="Heavy",OreType="M")
MAT["Brinium"]=ARMMaterial(Name="Brinium",PR=45,MR=45,WT=65,Buy=1000,Sell=500,WTClass="Heavy",OreType="B")
MAT["Impervium"]=ARMMaterial(Name="Impervium",PR=75,MR=19,WT=75,Buy=1000,Sell=500,WTClass="Heavy",OreType="P")

class Armor(object):
	def __init__(self,Name="None",PR=0,MR=0,WT=0,Buy=0,Sell=0):
		self.PR=PR
		self.MR=MR
		self.WT=WT
		self.Buy=Buy
		self.Sell=Sell

ARM={}
ARM["Head"]=Armor(Name="Head",PR=0.15,MR=0.15,WT=0.15,Buy=0.15,Sell=0.15)
ARM["Torso"]=Armor(Name="Torso",PR=0.3,MR=0.3,WT=0.3,Buy=0.3,Sell=0.3)
ARM["Arms"]=Armor(Name="Arms",PR=0.2,MR=0.2,WT=0.2,Buy=0.2,Sell=0.2)
ARM["Legs"]=Armor(Name="Legs",PR=0.2,MR=0.2,WT=0.2,Buy=0.2,Sell=0.2)
ARM["Feet"]=Armor(Name="Feet",PR=0.15,MR=0.15,WT=0.15,Buy=0.15,Sell=0.15)
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
	OreClass=MAT[Material].WTClass
	OreType=MAT[Material].OreType

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
	
	if OreClass=="Feather":
		ProductPR=max(round(((OrePR*SmithPR)*UpgradePR)*PrefixPR),0)
		ProductMR=max(round(((OreMR*SmithMR)*UpgradeMR)*PrefixMR),0)
		ProductWT=max(round(((OreWT*SmithWT)*UpgradeWT)*PrefixWT),0)
		ProductBuy=max(round(((OreBuy*SmithBuy)*UpgradeBuy)*PrefixBuy),0)
		ProductSell=max(round(((OreSell*SmithSell)*UpgradeSell)*PrefixSell),0)
	elif OreClass=="Light":
		ProductPR=round((max(OrePR*SmithPR,1)*UpgradePR)*PrefixPR)
		ProductMR=round((max(OreMR*SmithMR,1)*UpgradeMR)*PrefixMR)
		ProductWT=round((max(OreWT*SmithWT,1)*UpgradeWT)*PrefixWT)
		ProductBuy=round((max(OreBuy*SmithBuy,1)*UpgradeBuy)*PrefixBuy)
		ProductSell=round((max(OreSell*SmithSell,1)*UpgradeSell)*PrefixSell)
	elif OreClass=="Medium":
		if OreType=="P":
			ProductPR=round((max(OrePR*SmithPR,3)*UpgradePR)*PrefixPR)
			ProductMR=round((max(OreMR*SmithMR,2)*UpgradeMR)*PrefixMR)
			ProductWT=round((max(OreWT*SmithWT,3)*UpgradeWT)*PrefixWT)
			ProductBuy=round((max(OreBuy*SmithBuy,3)*UpgradeBuy)*PrefixBuy)
			ProductSell=round((max(OreSell*SmithSell,3)*UpgradeSell)*PrefixSell)
		elif OreType=="B":
			ProductPR=round((max(OrePR*SmithPR,2)*UpgradePR)*PrefixPR)
			ProductMR=round((max(OreMR*SmithMR,2)*UpgradeMR)*PrefixMR)
			ProductWT=round((max(OreWT*SmithWT,2)*UpgradeWT)*PrefixWT)
			ProductBuy=round((max(OreBuy*SmithBuy,2)*UpgradeBuy)*PrefixBuy)
			ProductSell=round((max(OreSell*SmithSell,2)*UpgradeSell)*PrefixSell)
		elif OreType=="M":
			ProductPR=round((max(OrePR*SmithPR,2)*UpgradePR)*PrefixPR)
			ProductMR=round((max(OreMR*SmithMR,3)*UpgradeMR)*PrefixMR)
			ProductWT=round((max(OreWT*SmithWT,3)*UpgradeWT)*PrefixWT)
			ProductBuy=round((max(OreBuy*SmithBuy,3)*UpgradeBuy)*PrefixBuy)
			ProductSell=round((max(OreSell*SmithSell,3)*UpgradeSell)*PrefixSell)
	elif OreClass=="Heavy":
		if OreType=="P":
			ProductPR=round((max(OrePR*SmithPR,5)*UpgradePR)*PrefixPR)
			ProductMR=round((max(OreMR*SmithMR,1)*UpgradeMR)*PrefixMR)
			ProductWT=round((max(OreWT*SmithWT,5)*UpgradeWT)*PrefixWT)
			ProductBuy=round((max(OreBuy*SmithBuy,5)*UpgradeBuy)*PrefixBuy)
			ProductSell=round((max(OreSell*SmithSell,5)*UpgradeSell)*PrefixSell)
		elif OreType=="B":
			ProductPR=round((max(OrePR*SmithPR,3)*UpgradePR)*PrefixPR)
			ProductMR=round((max(OreMR*SmithMR,3)*UpgradeMR)*PrefixMR)
			ProductWT=round((max(OreWT*SmithWT,3)*UpgradeWT)*PrefixWT)
			ProductBuy=round((max(OreBuy*SmithBuy,3)*UpgradeBuy)*PrefixBuy)
			ProductSell=round((max(OreSell*SmithSell,3)*UpgradeSell)*PrefixSell)
		elif OreType=="M":
			ProductPR=round((max(OrePR*SmithPR,1)*UpgradePR)*PrefixPR)
			ProductMR=round((max(OreMR*SmithMR,5)*UpgradeMR)*PrefixMR)
			ProductWT=round((max(OreWT*SmithWT,3)*UpgradeWT)*PrefixWT)
			ProductBuy=round((max(OreBuy*SmithBuy,5)*UpgradeBuy)*PrefixBuy)
			ProductSell=round((max(OreSell*SmithSell,5)*UpgradeSell)*PrefixSell)
	return(ProductPR,ProductMR,ProductWT,ProductBuy,ProductSell)

OmniArmorData={}
for Inputs in ForgeAInputs:
	OmniArmorData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]]=ForgeA(Inputs[0],Inputs[1],Inputs[2],Inputs[3])

