PrefixTypes=("Normal","Reinforced","Attuned","Lightweight","Masterpiece","Rejuvenating")
Materials=("Unobtanium","Silk","Leather","Cotton","Wood","Tin","Copper","Bronze","Gold","Cobalt","Tungsten","Shardsteel","Shardiron","Magenium","Steel","Iron","Cazenium","Hevisteel","Heviron","Rozenium")
ArmorTypes=("Head","Torso","Arms","Legs","Feet","Smallshield","Mediumshield","Largeshield")
Upgrades=("0","1","2","3","4","5","6","7","8","9","10")

ForgeAInputs=[]

for p in PrefixTypes:
	for m in Materials:
		for a in ArmorTypes:
			for u in Upgrades:
				ForgeAInputs.append((p,m,a,u))

PRE={}
PRE["NormalPD"]=1
PRE["NormalMD"]=1
PRE["NormalAC"]=1
PRE["NormalPR"]=1
PRE["NormalMR"]=1
PRE["NormalWT"]=1
PRE["NormalBuy"]=1
PRE["NormalSell"]=1
PRE["NormalSpecial"]="It's completely normal."

PRE["ReinforcedPD"]=1
PRE["ReinforcedMD"]=1
PRE["ReinforcedAC"]=1
PRE["ReinforcedPR"]=2
PRE["ReinforcedMR"]=1
PRE["ReinforcedWT"]=1
PRE["ReinforcedBuy"]=2
PRE["ReinforcedSell"]=2
PRE["ReinforcedSpecial"]="It's heavily Reinforced, so it has double the usual Physical Resistance."

PRE["AttunedPD"]=1
PRE["AttunedMD"]=1
PRE["AttunedAC"]=1
PRE["AttunedPR"]=1
PRE["AttunedMR"]=2
PRE["AttunedWT"]=1
PRE["AttunedBuy"]=2
PRE["AttunedSell"]=2
PRE["AttunedSpecial"]="It's incredibly Attuned, so it has double the usual Magical Resistance."

PRE["LightweightPD"]=1
PRE["LightweightMD"]=1
PRE["LightweightAC"]=1
PRE["LightweightPR"]=1
PRE["LightweightMR"]=1
PRE["LightweightWT"]=0.5
PRE["LightweightBuy"]=2
PRE["LightweightSell"]=2
PRE["LightweightSpecial"]="It's pretty Lightweight, so it has half the usual Weight."

PRE["MasterpiecePD"]=2
PRE["MasterpieceMD"]=2
PRE["MasterpieceAC"]=2
PRE["MasterpiecePR"]=2
PRE["MasterpieceMR"]=2
PRE["MasterpieceWT"]=0.5
PRE["MasterpieceBuy"]=4
PRE["MasterpieceSell"]=4
PRE["MasterpieceSpecial"]="It's a total Masterpiece. All its stats are doubled except Weight, which is halved."

PRE["RejuvenatingPD"]=1
PRE["RejuvenatingMD"]=1
PRE["RejuvenatingAC"]=1
PRE["RejuvenatingPR"]=1
PRE["RejuvenatingMR"]=1
PRE["RejuvenatingWT"]=1
PRE["RejuvenatingBuy"]=1
PRE["RejuvenatingSell"]=1
PRE["RejuvenatingSpecial"]="It's enchanted to give the wearer more energy, so it boosts ENE Regen by 10%!"

MAT={}
MAT["UnobtaniumPD"]=0
MAT["UnobtaniumMD"]=0
MAT["UnobtaniumAC"]=0
MAT["UnobtaniumPR"]=0
MAT["UnobtaniumMR"]=0
MAT["UnobtaniumWT"]=0
MAT["UnobtaniumBuy"]=0
MAT["UnobtaniumSell"]=0
MAT["UnobtaniumSpecial"]=" made of Unobtanium.\n"
#===================================
#TIER I START
#===================================
#Ivory & Silk
#Magical Lightweight Material
MAT["SilkPD"]=3
MAT["SilkMD"]=6
MAT["SilkAC"]=10
MAT["SilkPR"]=3
MAT["SilkMR"]=6
MAT["SilkWT"]=3
MAT["SilkBuy"]=100
MAT["SilkSell"]=50
MAT["SilkSpecial"]="made of Silk.\n"

#Cotton & Wood
#Balanced Lightweight Material
MAT["CottonPD"]=4
MAT["CottonMD"]=4
MAT["CottonAC"]=10
MAT["CottonPR"]=4
MAT["CottonMR"]=4
MAT["CottonWT"]=6
MAT["CottonBuy"]=100
MAT["CottonSell"]=50
MAT["CottonSpecial"]="made of Cotton.\n"
MAT["WoodPD"]=4
MAT["WoodMD"]=4
MAT["WoodAC"]=10
MAT["WoodPR"]=4
MAT["WoodMR"]=4
MAT["WoodWT"]=6
MAT["WoodBuy"]=100
MAT["WoodSell"]=50
MAT["WoodSpecial"]="made of Wood.\n"

#Bone & Leather
#Physical Lightweight Material
MAT["LeatherPD"]=6
MAT["LeatherMD"]=3
MAT["LeatherAC"]=10
MAT["LeatherPR"]=6
MAT["LeatherMR"]=3
MAT["LeatherWT"]=5
MAT["LeatherBuy"]=100
MAT["LeatherSell"]=50
MAT["LeatherSpecial"]="made of Leather.\n"

#Midweight
#Tin, Midweight Physical material
MAT["TinPD"]=8
MAT["TinMD"]=4
MAT["TinAC"]=6
MAT["TinPR"]=8
MAT["TinMR"]=4
MAT["TinWT"]=8
MAT["TinBuy"]=120
MAT["TinSell"]=160
MAT["TinSpecial"]="made of Tin.\n"
#Copper, Midweight Magical Material
MAT["CopperPD"]=4
MAT["CopperMD"]=8
MAT["CopperAC"]=6
MAT["CopperPR"]=4
MAT["CopperMR"]=8
MAT["CopperWT"]=6
MAT["CopperBuy"]=120
MAT["CopperSell"]=60
MAT["CopperSpecial"]="made of Copper.\n"
#Bronze, Balanced midweight material
MAT["BronzePD"]=7
MAT["BronzeMD"]=7
MAT["BronzeAC"]=7
MAT["BronzePR"]=7
MAT["BronzeMR"]=7
MAT["BronzeWT"]=8
MAT["BronzeBuy"]=120
MAT["BronzeSell"]=60
MAT["BronzeSpecial"]="made of Bronze.\n"

#Gold
#Magical Heavyweight Material
MAT["GoldPD"]=6
MAT["GoldMD"]=12
MAT["GoldAC"]=0
MAT["GoldPR"]=6
MAT["GoldMR"]=12
MAT["GoldWT"]=13
MAT["GoldBuy"]=150
MAT["GoldSell"]=75
MAT["GoldSpecial"]="made of Gold.\n"
#Cobalt
#Balanced Heavyweight Material
MAT["CobaltPD"]=10
MAT["CobaltMD"]=10
MAT["CobaltAC"]=0
MAT["CobaltPR"]=10
MAT["CobaltMR"]=10
MAT["CobaltWT"]=10
MAT["CobaltBuy"]=150
MAT["CobaltSell"]=75
MAT["CobaltSpecial"]="made of Cobalt.\n"
#Tungsten
#Physical Heavyweight Material
MAT["TungstenPD"]=12
MAT["TungstenMD"]=6
MAT["TungstenAC"]=0
MAT["TungstenPR"]=12
MAT["TungstenMR"]=6
MAT["TungstenWT"]=13
MAT["TungstenBuy"]=150
MAT["TungstenSell"]=75
MAT["TungstenSpecial"]="made of Tungsten.\n"
#===================================
			#Tier II
#===================================
#Shardsteel: Physical Lightweight
MAT["ShardsteelPD"]=16
MAT["ShardsteelMD"]=8
MAT["ShardsteelAC"]=12
MAT["ShardsteelPR"]=16
MAT["ShardsteelMR"]=8
MAT["ShardsteelWT"]=8
MAT["ShardsteelBuy"]=200
MAT["ShardsteelSell"]=100
MAT["ShardsteelSpecial"]="made of Shardsteel.\n"
#Magenium: Magical Lightweight
MAT["MageniumPD"]=8
MAT["MageniumMD"]=16
MAT["MageniumAC"]=12
MAT["MageniumPR"]=8
MAT["MageniumMR"]=16
MAT["MageniumWT"]=8
MAT["MageniumBuy"]=200
MAT["MageniumSell"]=100
MAT["MageniumSpecial"]="made of Magenium.\n"
#Shardiron: Balanced Lightweight
MAT["ShardironPD"]=13
MAT["ShardironMD"]=13
MAT["ShardironAC"]=13
MAT["ShardironPR"]=13
MAT["ShardironMR"]=13
MAT["ShardironWT"]=6
MAT["ShardironBuy"]=200
MAT["ShardironSell"]=100
MAT["ShardironSpecial"]="made of Shardiron.\n"

#Steel: Physical Midweight
MAT["SteelPD"]=24
MAT["SteelMD"]=12
MAT["SteelAC"]=8
MAT["SteelPR"]=24
MAT["SteelMR"]=12
MAT["SteelWT"]=20
MAT["SteelBuy"]=300
MAT["SteelSell"]=150
MAT["SteelSpecial"]="made of Steel.\n"
#Cazenium: Magical Midweight
MAT["CazeniumPD"]=12
MAT["CazeniumMD"]=24
MAT["CazeniumAC"]=8
MAT["CazeniumPR"]=12
MAT["CazeniumMR"]=24
MAT["CazeniumWT"]=15
MAT["CazeniumBuy"]=300
MAT["CazeniumSell"]=150
MAT["CazeniumSpecial"]="made of Cazenium.\n"
#Iron: Balanced Midweight
MAT["IronPD"]=18
MAT["IronMD"]=18
MAT["IronAC"]=8
MAT["IronPR"]=18
MAT["IronMR"]=18
MAT["IronWT"]=18
MAT["IronBuy"]=300
MAT["IronSell"]=150
MAT["IronSpecial"]="made of Iron.\n"

#Hevisteel: Physical Heavyweight
MAT["HevisteelPD"]=30
MAT["HevisteelMD"]=15
MAT["HevisteelAC"]=5
MAT["HevisteelPR"]=30
MAT["HevisteelMR"]=15
MAT["HevisteelWT"]=28
MAT["HevisteelBuy"]=400
MAT["HevisteelSell"]=200
MAT["HevisteelSpecial"]="made of Hevisteel.\n"
#Rozenium: Magical Heavyweight
MAT["RozeniumPD"]=15
MAT["RozeniumMD"]=30
MAT["RozeniumAC"]=5
MAT["RozeniumPR"]=15
MAT["RozeniumMR"]=30
MAT["RozeniumWT"]=22
MAT["RozeniumBuy"]=400
MAT["RozeniumSell"]=200
MAT["RozeniumSpecial"]="made of Rozenium.\n"
#Heviron: Balanced Heavyweight
MAT["HevironPD"]=26
MAT["HevironMD"]=26
MAT["HevironAC"]=5
MAT["HevironPR"]=26
MAT["HevironMR"]=26
MAT["HevironWT"]=22
MAT["HevironBuy"]=400
MAT["HevironSell"]=200
MAT["HevironSpecial"]="made of Heviron.\n"
#===================================
			#Tier III
#===================================
#Chrome: Physical Lightweight
MAT["ChromePD"]=20
MAT["ChromeMD"]=10
MAT["ChromeAC"]=15
MAT["ChromePR"]=20
MAT["ChromeMR"]=10
MAT["ChromeWT"]=10
MAT["ChromeBuy"]=500
MAT["ChromeSell"]=250
MAT["ChromeSpecial"]="made of Chrome.\n"
#Bismuth: Magical Lightweight
MAT["BismuthPD"]=10
MAT["BismuthMD"]=20
MAT["BismuthAC"]=15
MAT["BismuthPR"]=10
MAT["BismuthMR"]=20
MAT["BismuthWT"]=10
MAT["BismuthBuy"]=500
MAT["BismuthSell"]=250
MAT["BismuthSpecial"]="made of Bismuth.\n"
#Aluminum: Balanced Lightweight
MAT["AluminumPD"]=15
MAT["AluminumMD"]=15
MAT["AluminumAC"]=20
MAT["AluminumPR"]=15
MAT["AluminumMR"]=15
MAT["AluminumWT"]=6
MAT["AluminumBuy"]=500
MAT["AluminumSell"]=250
MAT["AluminumSpecial"]="made of Aluminum.\n"

#Titanium: Physical Midweight
MAT["TitaniumPD"]=30
MAT["TitaniumMD"]=15
MAT["TitaniumAC"]=12
MAT["TitaniumPR"]=30
MAT["TitaniumMR"]=15
MAT["TitaniumWT"]=30
MAT["TitaniumBuy"]=600
MAT["TitaniumSell"]=300
MAT["TitaniumSpecial"]="made of Titanium.\n"
#Silver: Magical Midweight
MAT["SilverPD"]=15
MAT["SilverMD"]=30
MAT["SilverAC"]=12
MAT["SilverPR"]=15
MAT["SilverMR"]=30
MAT["SilverWT"]=24
MAT["SilverBuy"]=600
MAT["SilverSell"]=300
MAT["SilverSpecial"]="made of Silver.\n"
#Brass: Balanced Midweight
MAT["BrassPD"]=22
MAT["BrassMD"]=22
MAT["BrassAC"]=15
MAT["BrassPR"]=22
MAT["BrassMR"]=22
MAT["BrassWT"]=20
MAT["BrassBuy"]=600
MAT["BrassSell"]=300
MAT["BrassSpecial"]="made of Brass.\n"

#Lead: Physical Heavyweight
MAT["LeadPD"]=40
MAT["LeadMD"]=20
MAT["LeadAC"]=10
MAT["LeadPR"]=40
MAT["LeadMR"]=20
MAT["LeadWT"]=40
MAT["LeadBuy"]=700
MAT["LeadSell"]=350
MAT["LeadSpecial"]="made of Lead.\n"
#Orichalc: Magical Heavyweight
MAT["OrichalcPD"]=20
MAT["OrichalcMD"]=40
MAT["OrichalcAC"]=10
MAT["OrichalcPR"]=20
MAT["OrichalcMR"]=40
MAT["OrichalcWT"]=37
MAT["OrichalcBuy"]=700
MAT["OrichalcSell"]=350
MAT["OrichalcSpecial"]="made of Orichalc.\n"
#Platinum: Balanced Heavyweight
MAT["PlatinumPD"]=35
MAT["PlatinumMD"]=35
MAT["PlatinumAC"]=12
MAT["PlatinumPR"]=35
MAT["PlatinumMR"]=35
MAT["PlatinumWT"]=35
MAT["PlatinumBuy"]=700
MAT["PlatinumSell"]=350
MAT["PlatinumSpecial"]="made of Platinum.\n"
#===================================
			#Tier IV
#===================================
#Adamantite: Physical Lightweight. An ore discovered at the beneath active volcanoes. The danger of mining the stuff drives its scarcity, causing it to be expensive.
#Crystalite: Magical Lightweight. An ore discovered in subterranean deserts, it conducts magic like no other ore of this world.
#Orionite: Balanced Lightweight. An ore discovered in a surprisingly hollow mountain. The name comes from the constellation, which could be seen through a hole in the dome of the mountain at the time of discovery.

#Lunalite: Physical Midweight. A rare ore discovered during a deep-sea drilling operation. It reflects light just like the moon.
#Solite: Magical Midweight. A rare ore discovered in the belly of a slain Phoenix. It's warm to the touch, but its origins are mysterious.
#Territe: Balanced Midweight. An ore discovered by a humble farmer who mined his own metal and forged his own tools. He named it after the soil he works with.

#Impervium: Physical Heavyweight. An ore discovered deep below Phoenix Hill itself. Has incredible protective properties.
#Sorcium: Magical Heavyweight. An ore discovered beneath abandoned Phoenix nests. Named after Sorcery itself due to its incredible magical potential.
#Brinieum: Balanced Heavyweight. An ore discovered in craggy cliffsides near the floor of the seas of the world. Possesses a salty taste and a stinging cut.

ARM={}

ARM["HeadPR"]=0.05
ARM["HeadMR"]=0.05
ARM["HeadWT"]=0.05
ARM["HeadBuy"]=0.05
ARM["HeadSell"]=0.05
ARM["HeadSpecial"]="Headgear"

ARM["TorsoPR"]=0.5
ARM["TorsoMR"]=0.5
ARM["TorsoWT"]=0.5
ARM["TorsoBuy"]=0.5
ARM["TorsoSell"]=0.5
ARM["TorsoSpecial"]="Torsogear"

ARM["ArmsPR"]=0.15
ARM["ArmsMR"]=0.15
ARM["ArmsWT"]=0.15
ARM["ArmsBuy"]=0.15
ARM["ArmsSell"]=0.15
ARM["ArmsSpecial"]="Armwear"

ARM["LegsPR"]=0.25
ARM["LegsMR"]=0.25
ARM["LegsWT"]=0.25
ARM["LegsBuy"]=0.25
ARM["LegsSell"]=0.25
ARM["LegsSpecial"]="Legwear"

ARM["FeetPR"]=0.05
ARM["FeetMR"]=0.05
ARM["FeetWT"]=0.05
ARM["FeetBuy"]=0.05
ARM["FeetSell"]=0.05
ARM["FeetSpecial"]="Feetwear"

ARM["SmallshieldPR"]=0.75
ARM["SmallshieldMR"]=0.75
ARM["SmallshieldWT"]=0.75
ARM["SmallshieldBuy"]=0.75
ARM["SmallshieldSell"]=0.75
ARM["SmallshieldSpecial"]="A Small Shield "

ARM["MediumshieldPR"]=1
ARM["MediumshieldMR"]=1
ARM["MediumshieldWT"]=1
ARM["MediumshieldBuy"]=1
ARM["MediumshieldSell"]=1
ARM["MediumshieldSpecial"]="A Medium Shield "

ARM["LargeshieldPR"]=1.25
ARM["LargeshieldMR"]=1.25
ARM["LargeshieldWT"]=1.25
ARM["LargeshieldBuy"]=1.5
ARM["LargeshieldSell"]=1.5
ARM["LargeshieldSpecial"]="A Large Shield "

UP={}
UP["0PR"]=1.0
UP["1PR"]=1.1
UP["2PR"]=1.2
UP["3PR"]=1.3
UP["4PR"]=1.4
UP["5PR"]=1.5
UP["6PR"]=1.6
UP["7PR"]=1.7
UP["8PR"]=1.8
UP["9PR"]=1.9
UP["10PR"]=2.0

UP["0MR"]=1.0
UP["1MR"]=1.1
UP["2MR"]=1.2
UP["3MR"]=1.3
UP["4MR"]=1.4
UP["5MR"]=1.5
UP["6MR"]=1.6
UP["7MR"]=1.7
UP["8MR"]=1.8
UP["9MR"]=1.9
UP["10MR"]=2.0

UP["0AC"]=1.0
UP["1AC"]=1.1
UP["2AC"]=1.2
UP["3AC"]=1.3
UP["4AC"]=1.4
UP["5AC"]=1.5
UP["6AC"]=1.6
UP["7AC"]=1.7
UP["8AC"]=1.8
UP["9AC"]=1.9
UP["10AC"]=2.0

UP["0PR"]=1.0
UP["1PR"]=1.1
UP["2PR"]=1.2
UP["3PR"]=1.3
UP["4PR"]=1.4
UP["5PR"]=1.5
UP["6PR"]=1.6
UP["7PR"]=1.7
UP["8PR"]=1.8
UP["9PR"]=1.9
UP["10PR"]=2.0

UP["0MR"]=1.0
UP["1MR"]=1.1
UP["2MR"]=1.2
UP["3MR"]=1.3
UP["4MR"]=1.4
UP["5MR"]=1.5
UP["6MR"]=1.6
UP["7MR"]=1.7
UP["8MR"]=1.8
UP["9MR"]=1.9
UP["10MR"]=2.0

UP["0WT"]=1.0
UP["1WT"]=0.95
UP["2WT"]=0.9
UP["3WT"]=0.85
UP["4WT"]=0.8
UP["5WT"]=0.75
UP["6WT"]=0.7
UP["7WT"]=0.65
UP["8WT"]=0.6
UP["9WT"]=0.55
UP["10WT"]=0.5

UP["0Buy"]=1.0
UP["1Buy"]=1.1
UP["2Buy"]=1.2
UP["3Buy"]=1.3
UP["4Buy"]=1.4
UP["5Buy"]=1.5
UP["6Buy"]=1.6
UP["7Buy"]=1.7
UP["8Buy"]=1.8
UP["9Buy"]=1.9
UP["10Buy"]=2.0

UP["0Sell"]=1.0
UP["1Sell"]=1.1
UP["2Sell"]=1.2
UP["3Sell"]=1.3
UP["4Sell"]=1.4
UP["5Sell"]=1.5
UP["6Sell"]=1.6
UP["7Sell"]=1.7
UP["8Sell"]=1.8
UP["9Sell"]=1.9
UP["10Sell"]=2.0

UP["0Special"]=" It has been upgraded 0 times."
UP["1Special"]=" It has been upgraded 1 times."
UP["2Special"]=" It has been upgraded 2 times."
UP["3Special"]=" It has been upgraded 3 times."
UP["4Special"]=" It has been upgraded 4 times."
UP["5Special"]=" It has been upgraded 5 times."
UP["6Special"]=" It has been upgraded 6 times."
UP["7Special"]=" It has been upgraded 7 times."
UP["8Special"]=" It has been upgraded 8 times."
UP["9Special"]=" It has been upgraded 9 times."
UP["10Special"]=" It has been upgraded 10 times."

def ForgeA(PrefixType,Material,ArmorType,UpgradeLevel):
	"""The ForgeA function Forges armor from its base components into a defensive tool."""

	#Get the appropriate material stats...
	OrePR=MAT[Material+"PR"]
	OreMR=MAT[Material+"MR"]
	OreWT=MAT[Material+"WT"]
	OreBY=MAT[Material+"Buy"]
	OreSL=MAT[Material+"Sell"]
	OreSP=MAT[Material+"Special"]

	#And weapon type stats...
	SmithPR=ARM[ArmorType+"PR"]
	SmithMR=ARM[ArmorType+"MR"]
	SmithWT=ARM[ArmorType+"WT"]
	SmithBY=ARM[ArmorType+"Buy"]
	SmithSL=ARM[ArmorType+"Sell"]
	SmithSP=ARM[ArmorType+"Special"]

	#And apply the upgrade...
	UpgradePR=UP[UpgradeLevel+"PR"]
	UpgradeMR=UP[UpgradeLevel+"MR"]
	UpgradeWT=UP[UpgradeLevel+"WT"]
	UpgradeBY=UP[UpgradeLevel+"Buy"]
	UpgradeSL=UP[UpgradeLevel+"Sell"]
	UpgradeSP=UP[UpgradeLevel+"Special"]

	PrefixPR=PRE[PrefixType+"PR"]
	PrefixMR=PRE[PrefixType+"MR"]
	PrefixWT=PRE[PrefixType+"WT"]
	PrefixBY=PRE[PrefixType+"Buy"]
	PrefixSL=PRE[PrefixType+"Sell"]
	PrefixSP=PRE[PrefixType+"Special"]

	#Then, add them all together.
	ProductPR=max(round(((OrePR*SmithPR)*UpgradePR)*PrefixPR),1)
	ProductMR=max(round(((OreMR*SmithMR)*UpgradeMR)*PrefixMR),1)
	ProductWT=max(round(((OreWT*SmithWT)*UpgradeWT)*PrefixWT),1)
	ProductBY=max(round(((OreBY*SmithBY)*UpgradeBY)*PrefixBY),1)
	ProductSL=max(round(((OreSL*SmithSL)*UpgradeSL)*PrefixSL),1)
	ProductSP=(SmithSP+OreSP+PrefixSP+UpgradeSP)

	return(ProductPR,ProductMR,ProductWT,ProductBY,ProductSL,ProductSP)

OmniArmorData={}

for Inputs in ForgeAInputs:
	OmniArmorData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]] = ForgeA(Inputs[0],Inputs[1],Inputs[2],Inputs[3])
