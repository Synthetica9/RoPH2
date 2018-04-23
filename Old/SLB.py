from WSD import WSD
from Weapons import OmniWeapData
import random as ra
import fileinput

def TwoHitterSingleP(User,Weapon,ENE,CritChance,Damage1,Damage2,Hit,cBST,e,wPD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")

def SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")

def SingleTargetM(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wMD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")

def TwoHitterDualP(User,Weapon,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,cBST,e1,e2,wPD,uELM,e1ELM,e2ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
				
#Whip Skills
def BurningLash(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uMAR=u+"MAR"
	uPAR=u+"PAR"
	uLCK=u+"LCK"
	uWT=u+"WT"
	e=input("Target Enemy is: ")
	eELM=e+"ELM"
	cBST=float(input("User Crit Boost is: "))
	eSTR=e+"STR"
	eSPR=e+"SPR"
	eSKL=e+"SKL"
	eABL=e+"ABL"
	eAGI=e+"AGI"
	eEVA=e+"EVA"
	eTGH=e+"TGH"
	eRES=e+"RES"
	eMAR=e+"MAR"
	ePAR=e+"PAR"
	eLCK=e+"LCK"
	eWT=e+"WT"
	eELM=e+"ELM"
	Damage=(WSD[uSTR]*1.2+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]*1.15)
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	Hit=50-WSD[uAGI]-WSD[uSTR]*0.25+WSD[eEVA]-wAC
	ENE=10
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
	if ra.randint(1,100) >= 80:
		print("---------------")
		print("SUCCESS!! Target is now Burning!")
		print("---------------")
	else:
		print("---------------")
		print("Failure...target is not Burning.")
		print("---------------")				
def SerpentCoil(User,Weapon,Element):
	u=User
	uSTR=u+"STR"
	uELM=Element
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uMAR=u+"MAR"
	uPAR=u+"PAR"
	uLCK=u+"LCK"
	uWT=u+"WT"
	e=input("Target Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	eSTR=e+"STR"
	eSPR=e+"SPR"
	eSKL=e+"SKL"
	eABL=e+"ABL"
	eAGI=e+"AGI"
	eEVA=e+"EVA"
	eTGH=e+"TGH"
	eRES=e+"RES"
	eMAR=e+"MAR"
	ePAR=e+"PAR"
	eLCK=e+"LCK"
	eWT=e+"WT"
	eELM=e+"ELM"
	ENE=15
	Damage=(WSD[uSTR]*1.2+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]*1.15)*1.15
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	Hit=50-WSD[uAGI]-WSD[uSTR]*0.25+WSD[eEVA]-wAC
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
	if ra.randint(1,100) >= 80:
		print("---------------")
		print("SUCCESS!! Target is now Poisoned!")
		print("---------------")
	else:
		print("---------------")
		print("Failure...Target is not Poisoned.")
		print("---------------")

#Flail Skills
def JawbreakerFinisher(User,Weapon):
	u=User
	e=input("Enemy is: ")
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	wPD=OmniWeapData[Weapon][0]
	cBST=float(input("User Crit Boost is: "))
	uLCK=u+"LCK"
	uSTR=u+"STR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	uSTR=u+"STR"
	ENE=10
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	Damage=WSD[uSTR]*1.1+WSD[uABL]*0.25-WSD[eTGH]*0.75-WSD[ePAR]
	Damage2=WSD[uSTR]*1.1+WSD[uABL]*0.25-WSD[eTGH]*0.75
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	Hit=50-WSD[uAGI]*0.5-WSD[uSTR]*0.25-WSD[uABL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC
	print("---------------")
	print(u,"spent 10 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("Critical Hit! Damage dealt to",e,"is",(Damage2*2)+wPD)
		print(e,"is Downed!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 80:
			print("Direct Hit! Armor bypassed! Damage dealt to",e,"is",(Damage2)+wPD)
			print("---------------")
			if ra.randint(1,100) > 80:
				print(e,"is Downed!")
				print("---------------")
			else:
				print(e,"is not Downed...")
				print("---------------")
		else:
			if ra.randint(1,100) >= Hit:
				print("Direct Hit! Damage dealt to",e,"is",(Damage)+wPD)
				print("---------------")
				if ra.randint(1,100) > 80:
					print(e,"is Downed!")
					print("---------------")
				else:
					print(e,"is not Downed...")
					print("---------------")
			else:
				print(u,"missed",e+"!")
				print("---------------")
def FuryTwirlFinisher(User,Weapon):
	u=User
	e=input("Enemy is: ")
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	wPD=OmniWeapData[Weapon][0]
	cBST=float(input("User Crit Boost is: "))
	uLCK=u+"LCK"
	uSTR=u+"STR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	Damage=WSD[uSTR]*1.2+WSD[uABL]*0.25-WSD[eTGH]*0.75-WSD[ePAR]
	Damage2=WSD[uSTR]*1.2+WSD[uABL]*0.25-WSD[eTGH]*0.75
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	Hit=50-WSD[uAGI]*0.5-WSD[uSTR]*0.25-WSD[uABL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("Critical Hit! Armr bypassed! Damage dealt to",e,"is",(Damage2*2)+wPD)
		print(e,"is Downed!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 80:
			print("Direct Hit! Armor bypassed! Damage dealt to",e,"is",(Damage2)+wPD)
			print("---------------")
			if ra.randint(1,100) > 80:
				print(e,"is Downed!")
				print("---------------")
			else:
				print(e,"is not Downed...")
				print("---------------")
		else:
			if ra.randint(1,100) >= Hit:
				print("Direct Hit! Damage dealt to",e,"is",(Damage)+wPD)
				print("---------------")
			else:
				print(u,"missed",e+"!")
				print("---------------")
#Any weapon
def Bodyslam(User):
	u=User
	uSTR=u+"STR"
	uLCK=u+"LCK"
	uWT=u+"WT"
	e=input("Target Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	eEVA=e+"EVA"
	eSTR=e+"STR"
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eWT=e+"WT"
	Damage=int(WSD[uSTR]+WSD[uWT]-WSD[eTGH]-WSD[ePAR])
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit!")
		print("Damage Dealt is",(WSD[uSTR]+WSD[uWT]-WSD[eTGH]-WSD[ePAR])*2)
		print(e,"is Stumbled! If mounted, they are forced off their steed!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 35-WSD[uLCK]-WSD[eSTR]*0.25+WSD[eEVA]:
			print("---------------")
			print(u,"landed a Direct Hit! Damage Dealt is", Damage)
			setattr(WSD[e+"CHP"],'Current',getattr(WSD[e+"CHP"],'Current')-max(0,Damage))
			print(e+"'s current HP is",getattr(WSD[e+"CHP"],'Current'))
			print("---------------")
			if ra.randint(1,100) >= 50-WSD[uWT]+WSD[eWT]:
				print("---------------")
				print(u,"has Stumbled",e+"!")
				print("---------------")
			else:
				print("---------------")
				print(u,"has not Stumbled",e+"!")
				print("---------------")
		else:
			print("---------------")
			print(u,"missed!")
			print("---------------")

def BraveLeap(User,Weapon):
	u=User
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uMAR=u+"MAR"
	uPAR=u+"PAR"
	uLCK=u+"LCK"
	uWT=u+"WT"
	e=input("Target Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	eSTR=e+"STR"
	eSPR=e+"SPR"
	eSKL=e+"SKL"
	eABL=e+"ABL"
	eAGI=e+"AGI"
	eEVA=e+"EVA"
	eTGH=e+"TGH"
	eRES=e+"RES"
	eMAR=e+"MAR"
	ePAR=e+"PAR"
	eLCK=e+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit!")
		print("Damage Dealt is",(WSD[uSTR]+WSD[uWT]-WSD[eTGH]-WSD[ePAR])*2+wPD)
		print(e,"is Stumbled! If mounted, they are forced off their steed!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 35-WSD[uLCK]-WSD[uSTR]*0.25+WSD[eEVA]:
			print("---------------")
			print(u,"landed a Direct Hit!")
			print("Damage Dealt is",(WSD[uSTR]+WSD[uWT]-WSD[eTGH]-WSD[ePAR])+wPD)
			print("---------------")
			if ra.randint(1,100) >= 50-WSD[uWT]:
				print("---------------")
				print(u,"has Stumbled",e+"!")
				print("---------------")
			else:
				print("---------------")
				print(u,"has not Stumbled",e+"!")
				print("---------------")
		else:
			print("---------------")
			print(u,"missed!")
			print("---------------")
#Battlestaff Skills, Tier I

#Knuckles Skills, Tier I
def OldOneTwo(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uSKL=u+"STR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	ENE=12
	eELM=e+"ELM"
	Hit=25-WSD[uAGI]-WSD[uSTR]*0.25-WSD[uLCK]+WSD[eEVA]-wAC
	Damage=round(max(1,(((WSD[uSTR]+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*2)+wPD)*0.1),((WSD[uSTR]+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*2)+wPD)
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
			
#Claw Skills, Tier I
def Twisterush(User,Weapon,Element):
	u=User
	e=input("Target is: ")
	uSTR=u+"STR"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uABL=u+"ABL"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	ENE=20
	uELM=Element
	eELM=e+"ELM"
	Hit=35-WSD[uLCK]-WSD[uAGI]-WSD[uSKL]*0.25+WSD[eEVA]
	Damage=(((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.4)*4)+wPD
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)

def ClawClash(User,Weapon):
	u=User
	e=input("Target is: ")
	uSTR=u+"STR"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uABL=u+"ABL"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print("Opponent is Disarmed, and you take their weapon!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 75-WSD[uLCK]-WSD[uSTR]*0.5+WSD[eEVA]+WSD[uSTR]*0.5:
			print("---------------")
			print("Opponent is Disarmed! Weapon returned to their inventory!")
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
def HeartlessThrust(User,Weapon,Element):
	u=User
	e=input("Target is: ")
	uSTR=u+"STR"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	uSKL=u+"SKL"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uABL=u+"ABL"
	uELM=Element
	eELM=e+"ELM"
	ENE=25
	Hit=45-WSD[uAGI]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC
	Damage=((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.45)+wPD
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
#Claw Skills, Tier II
def BloodySlashes(User,Weapon):
	u=User
	e=input("Target is: ")
	uSTR=u+"STR"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	uSKL=u+"SKL"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 20 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (((WSD[uSKL]*0.65+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*0.75)*2)+wPD)
		print("Hit 2 deals", (((WSD[uSKL]*0.65+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*0.75)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 15-WSD[uAGI]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Hit 1 deals", (((WSD[uSKL]*0.65+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*0.75)*1)+wPD)
			print("Hit 2 deals", (((WSD[uSKL]*0.65+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*0.75)*1)+wPD)
			print("---------------")
		else:
			print("---------------")
			print("You missed! Twice!")
			print("---------------")
#Knife Skills
#Tier I
def PinpointStab(User,Weapon):
	u=User
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	e=input("Target is: ")
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeapData[Weapon][0]
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	Damage=round(WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.75
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	Hit=(15-WSD[uAGI]-WSD[uLCK]-WSD[uSTR]*0.25+WSD[eEVA])-wAC
	Bypass=50-WSD[uLCK]+WSD[eEVA]
	ENE=25
	print("---------------")
	print(u,"spent",ENE,"ENE")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit! Damage dealt is",(Damage-WSD[ePAR])*2)
		print("---------------")
	else:
		if ra.randint(1,100) >= (Hit,Bypass):
			print("---------------")
			print(u,"landed a Direct Hit and Bypassed",e+"'s armor!")
			print("Damage dealt is",Damage-WSD[ePAR])
			print("---------------")
		elif ra.randint(1,100) >= Hit:
			print("---------------")
			print(u,"landed a Direct Hit, but did not bypass armor...")
			print("Damage dealt is",Damage)
			print("---------------")
		else:
			print("---------------")
			print("You missed!")
			print("---------------")
def TripleComboKnife(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 10 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("Hit 2 deals", (((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("Hit 3 deals", (((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 1 deals", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 1!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 2 deals", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 2!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 3 deals", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 3!")
			print("---------------")
#Tier II
def FirstBlood(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 10 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "managed to hit", e, "for a Critical Hit!")
		print("Full HP damage is", (((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.25)*2)+wPD)
		print("Regular damage is", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "managed to hit", e, "for a Direct Hit!")
			print("Full HP damage is", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.25)+wPD)
			print("Regular damage is", (WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
#Single Sword Skills
#Tier I
def TripleComboSword(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 20 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("Hit 2 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("Hit 3 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 35-WSD[uAGI]*0.5-WSD[uABL]*0.5-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 1 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 1!")
			print("---------------")
		if ra.randint(1,100) >= 35-WSD[uAGI]*0.5-WSD[uABL]*0.5-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 2 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 2!")
			print("---------------")
		if ra.randint(1,100) >= 35-WSD[uAGI]*0.5-WSD[uABL]*0.5-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 3 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 3!")
			print("---------------")
#Single Swords
#Tier I
def BeginnersParry(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uAGI=u+"AGI"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Attack deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.15)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 85-WSD[uLCK]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uAGI]+WSD[eEVA]:
			print("---------------")
			print(u, "Landed a direct Arcing Hit against", e+"!")
			print("Attack deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.15)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "Landed a glancing Arcing Hit against", e+"!")
			print("Attack deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.15)+wPD)
			print("---------------")

def SharpBeginnersParry(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uAGI=u+"AGI"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Attack deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.15)*2.25)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 85-WSD[uLCK]-WSD[uSKL]*0.25-WSD[uAGI]+WSD[eEVA]:
			print("---------------")
			print(u, "Landed a direct Arcing Hit against", e+"!")
			print("Attack deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.15)*1.25+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "Landed a glancing Arcing Hit against", e+"!")
			print("Attack deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.15)*1.25+wPD)
			print("---------------")

def TripleComboSword(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 21 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("Hit 2 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("Hit 3 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 1 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 1!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 2 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 2!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 3 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 3!")
			print("---------------")
			
def SharpTripleComboSword(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 21 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)*1.25+wPD)
		print("Hit 2 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)*1.25+wPD)
		print("Hit 3 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*2)*1.25+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 1 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*1.25+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 1!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 2 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*1.25+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 2!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 3 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.85)*1.25+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 3!")
			print("---------------")
			
def FuryThrust(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	Hit=45-WSD[uAGI]*0.5-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uABL]*0.5-WSD[uLCK]+WSD[eEVA]-wAC
	Damage=((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.4)+wPD
	ENE=10
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
#Sword Skills: Sword Sharpener + Sword Sighter.
def BeginnersParrySharpSight(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Attack deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.4)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 70-WSD[uLCK]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uEVA]+WSD[eAGI]:
			print("---------------")
			print(u, "Landed a direct Arcing Hit against", e+"!")
			print("Attack deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.4)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "Landed a glancing Arcing Hit against", e+"!")
			print("Attack deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.4)+wPD)
			print("---------------")
def TripleComboSwordSharpSight(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 21 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]))*2)+wPD)
		print("Hit 2 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]))*2)+wPD)
		print("Hit 3 deals", (((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]))*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 30-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 1 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]))+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 1!")
			print("---------------")
		if ra.randint(1,100) >= 30-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 2 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]))+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 2!")
			print("---------------")
		if ra.randint(1,100) >= 30-WSD[uAGI]-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print("Hit 3 deals", ((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]))+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 3!")
			print("---------------")
def FuryThrustSharpSight(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	Hit=30-WSD[uAGI]*0.5-WSD[uSKL]*0.125-WSD[uSTR]*0.125-WSD[uABL]*0.5-WSD[uLCK]+WSD[eEVA]-wAC
	Damage=((WSD[uSKL]*0.5+WSD[uSTR]*0.5+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*1.65)+wPD
	ENE=10
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
#Greatswords
#Tier I
def BeginnersCounter(User,Weapon):
	u=User
	e=input("Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "rolled within their Critical Range against", e+"!")
		print("Attack deals no damage, but", e, "loses aggro against", u, "and seeks another target.")
		print("---------------")
	else:
		if ra.randint(1,100) >= 70-WSD[uSTR]-WSD[uABL]*0.25+WSD[eTGH]:
			print("---------------")
			print(u, "successfully used Beginner's Counter against", e+"!")
			print("Attack deals no damage, but", e, "backs off and reconsiders how to attack", u)
			print("---------------")
		else:
			print("---------------")
			print("You tried to counter, but failed.")
			print("---------------")
def ChainsawThrust(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Hit=(75-WSD[uLCK]-WSD[uAGI]-wAC+WSD[eEVA])
	Damage=((((WSD[uSTR]*1.25+WSD[uABL]*0.25+wPD-WSD[eTGH])*0.75)*3)+wPD)
	ENE=30
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def ChainsawThrustGrinder(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Hit=(75-WSD[uLCK]-WSD[uAGI]-wAC+WSD[eEVA])
	Damage=((((WSD[uSTR]*1.25+WSD[uABL]*0.25+wPD-WSD[eTGH])*1.25)*3)+wPD)
	ENE=30
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
#Polearms
#Tier I
def TripointBuster(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 12 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*2)+wPD)
		print("Hit 2 deals", (((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*2)+wPD)
		print("Hit 3 deals", (((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 40-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
		if ra.randint(1,100) >= 40-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
		if ra.randint(1,100) >= 40-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
def Cutwo(User,Weapon):
	u=User
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1TGH=e1+"TGH"
	e1EVA=e1+"EVA"
	e1PAR=e1+"PAR"
	e1AGI=e1+"AGI"
	e2TGH=e2+"TGH"
	e2EVA=e2+"EVA"
	e2PAR=e2+"PAR"
	e2AGI=e2+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Damage1=(((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e1TGH]-WSD[e1PAR])*0.5)+wPD)
	Damage2=(((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e2TGH]-WSD[e2PAR])*0.5)+wPD)
	Hit1=(30-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[e1EVA]-wAC)
	Hit2=(30-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[e2EVA]-wAC)
	ENE=8
	TwoHitterDualP(User,Weapon,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,cBST,e1,e2,wPD,uELM,e1ELM,e2ELM)

def TripointPaladin(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	eAGI=e+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	print("---------------")
	print(u,"spent 12 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", ((((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*1.35)*2)+wPD)
		print("Hit 2 deals", ((((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*1.35)*2)+wPD)
		print("Hit 3 deals", ((((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*1.35)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 40-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*1.35+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
		if ra.randint(1,100) >= 40-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*1.35+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
		if ra.randint(1,100) >= 40-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.25)*1.35+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
def CutwoPaladin(User,Weapon):
	u=User
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1TGH=e1+"TGH"
	e1EVA=e1+"EVA"
	e1PAR=e1+"PAR"
	e1AGI=e1+"AGI"
	e2TGH=e2+"TGH"
	e2EVA=e2+"EVA"
	e2PAR=e2+"PAR"
	e2AGI=e2+"AGI"
	uSTR=u+"STR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Damage1=(((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e1TGH]-WSD[e1PAR])*0.5)*1.35+wPD)
	Damage2=(((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e2TGH]-WSD[e2PAR])*0.5)*1.35+wPD)
	Hit1=(30-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[e1EVA]-wAC)
	Hit2=(30-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[e2EVA]-wAC)
	ENE=8
	TwoHitterDualP(User,Weapon,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,cBST,e1,e2,wPD,uELM,e1ELM,e2ELM)
	print("---------------")
	print(u,"spent 8 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e1, "and", e2+"!")
		print("Damage to", e1, "is", (((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e1TGH]-WSD[e1PAR])*0.5)*1.35)*2+wPD)
		print("Damage to", e2, "is", (((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e2TGH]-WSD[eP2AR])*0.5)*1.35)*2+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 30-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[e1EVA]-wAC:
			print("---------------")
			print(u,"landed a direct hit against",e1)
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e1TGH]-WSD[e1PAR])*0.5)*1.35+wPD)
			print("---------------")
		if ra.randint(1,100) >= 30-WSD[uAGI]*0.75-WSD[uABL]*0.25-WSD[uSKL]*0.0875-WSD[uSTR]*0.1625-WSD[uLCK]+WSD[e2EVA]-wAC:
			print("---------------")
			print(u,"landed a direct hit against",e2)
			print("Damage dealt is", ((WSD[uSKL]*0.35+WSD[uSTR]*0.65+WSD[uABL]*0.25-WSD[e2TGH]-WSD[e2PAR])*0.5)*1.35+wPD)
			print("---------------")
#Canes
#Tier I
def Cudgel(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eRES=e+"RES"
	eMAR=e+"MAR"
	eEVA=e+"EVA"
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Hit=40-WSD[uAGI]-WSD[uSTR]*0.125-WSD[uSPR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC
	Damage=((WSD[uSTR]*0.5+WSD[uSPR]*0.25+WSD[uABL]*0.25-WSD[eTGH]*0.75-WSD[eRES]*0.25-WSD[eMAR])*1.1)+wPD
	ENE=10
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def ShatterBlow(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eRES=e+"RES"
	eEVA=e+"EVA"
	eMAR=e+"MAR"
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Hit=(40-WSD[uAGI]-WSD[uSTR]*0.125-WSD[uSPR]*0.125-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=(((WSD[uSTR]*0.5+WSD[uSPR]*0.25+WSD[uABL]*0.25-WSD[eTGH]*0.75-WSD[eRES]*0.25-WSD[eMAR])*1.25)+wPD)
	ENE=25
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
#Bow Skills
#Tier I
def Longshot(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Hit=(40-WSD[uABL]-WSD[uSTR]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=((WSD[uSTR]*0.9+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])+wPD)
	ENE=20
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def Clipshot(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	uAGI=u+"AGI"
	Hit=(50-WSD[uABL]-WSD[uSTR]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=(((WSD[uSTR]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*0.75)+wPD)
	ENE=10
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
#Crossbow Skills
#Tier I
def Holepunch(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	Hit=(75-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH])+wPD)
	ENE=25
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)

def Needleround(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	Hit=(30-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]*0.8-WSD[ePAR]*0.8)+wPD)
	ENE=20
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def CorrectHolepunch(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	uSTR=u+"STR"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	Hit=(55-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH])+wPD)
	ENE=25
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def CorrectNeedleround(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	Hit=(10-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]*0.8-WSD[ePAR]*0.8)+wPD)
	ENE=20
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def CorrectCrusadeCrusherHolepunch(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	uSTR=u+"STR"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	Hit=(55-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=(((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH])*1.15)+wPD)
	ENE=25
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def CorrectCrusadeCrusherNeedleround(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	Hit=(10-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC)
	Damage=((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]*0.8-WSD[ePAR]*0.55)*1.15+wPD)
	ENE=20
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def DoubleXB(User,Weapon):
	u=User
	e=input("Target is: ")
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 30 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e, "with that attack!")
		print("Hit 1 dealt", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]*0.8)*2)+wPD)
		print("Hit 2 dealt", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]*0.8)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e, "with that attack!")
			print("Hit 1 dealt", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]*0.8))+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 1!")
			print("---------------")
		if ra.randint(1,100) >= 35-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e, "with that attack!")
			print("Hit 2 dealt", ((WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR]*0.8)*0.75)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e, "with hit 2!")
			print("---------------")
#Handbow Skills
#Tier I
def TriplePlay(User,Weapon):
	u=User
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e3=input("Enemy 3 is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1TGH=e1+"TGH"
	e1EVA=e1+"EVA"
	e1PAR=e1+"PAR"
	e2TGH=e2+"TGH"
	e2EVA=e2+"EVA"
	e2PAR=e2+"PAR"
	e3TGH=e3+"TGH"
	e3EVA=e3+"EVA"
	e3PAR=e3+"PAR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e1, e2, "and", e3, "!")
		print("Damage dealt is", (((WSD[uSKL]*0.5+WSD[uABL]*0.25-WSD[e1TGH]-WSD[e1PAR])*0.75)*2)+wPD)
		print("Damage dealt is", (((WSD[uSKL]*0.5+WSD[uABL]*0.25-WSD[e2TGH]-WSD[e2PAR])*0.75)*2)+wPD)
		print("Damage dealt is", (((WSD[uSKL]*0.5+WSD[uABL]*0.25-WSD[e3TGH]-WSD[e3PAR])*0.75)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 45-WSD[uABL]*0.75-WSD[uSKL]*0.25-WSD[uLCK]+WSD[e1EVA]-wAC:
			print("---------------")
			print(u,"landed a Direct Hit against", e1, "!")
			print("Damage dealt is", ((WSD[uSKL]*0.5+WSD[uABL]*0.25-WSD[e1TGH]-WSD[e1PAR])*0.75)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e1,"!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uABL]*0.75-WSD[uSKL]*0.25-WSD[uLCK]+WSD[e2EVA]-wAC:
			print("---------------")
			print(u,"landed a Direct Hit against", e1, "!")
			print("Damage dealt is", ((WSD[uSKL]*0.5+WSD[uABL]*0.25-WSD[e2TGH]-WSD[e2PAR])*0.75)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e1,"!")
			print("---------------")
		if ra.randint(1,100) >= 45-WSD[uABL]*0.75-WSD[uSKL]*0.25-WSD[uLCK]+WSD[e3EVA]-wAC:
			print("---------------")
			print(u,"landed a Direct Hit against", e1, "!")
			print("Damage dealt is", ((WSD[uSKL]*0.5+WSD[uABL]*0.25-WSD[e3TGH]-WSD[e3PAR])*0.75)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e3,"!")
			print("---------------")

#Twin Pistol Skills
#Tier I
def ChargeShot(User,Weapon):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	ePAR=e+"PAR"
	uSKL=u+"SKL"
	uLCK=u+"LCK"
	uABL=u+"ABL"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 12 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Damage dealt to",e,"is", ((WSD[uSKL]*0.65+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*2.5)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 45-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u,"landed a Direct Hit against", e+"!")
			print("Damage dealt to",e,"is", ((WSD[uSKL]*0.65+WSD[uABL]*0.35-WSD[eTGH]-WSD[ePAR])*1.5)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u,"missed", e+"!")
			print("---------------")
#Rifle Skills
#Tier I
def PiercingLaser(User,Weapon):
	u=User
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	e1PAR=e1+"PAR"
	e1TGH=e1+"TGH"
	e1EVA=e1+"EVA"
	e2PAR=e2+"PAR"
	e2TGH=e2+"TGH"
	e2EVA=e2+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 20 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e1, "and", e2, "!")
		print("Damage dealt to", e1, "is", ((WSD[uSKL]+WSD[uABL]*0.5-WSD[e1TGH]-WSD[e1PAR])*2)+wPD)
		print("Damage dealt", e2, "is", ((WSD[uSKL]+WSD[uABL]*0.5-WSD[e2TGH]-WSD[e2PAR])*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 15-WSD[uSKL]*0.25-WSD[uABL]+WSD[e1EVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt to", e1, "is", (WSD[uSKL]+WSD[uABL]*0.5-WSD[e1TGH]-WSD[e1PAR])+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
		if ra.randint(1,100) >= 15-WSD[uSKL]*0.25-WSD[uABL]+WSD[e2EVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt to", e1, "is", (WSD[uSKL]+WSD[uABL]*0.5-WSD[e2TGH]-WSD[e2PAR])+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")

#Mechgun Skills
#Tier I
def Drizzle(User,Weapon,Element):
	u=User
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	Damage=round((((WSD[uSKL]+WSD[uABL]*0.25-WSD[ePAR]-WSD[eTGH])*0.3)*0.75)+wPD)
	print("---------------")
	print(u,"spent 10 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Hit 1 deals", (Damage*2))
		print("Hit 2 deals", (Damage*2))
		print("Hit 3 deals", (Damage*2))
		print("---------------")
	else:
		if ra.randint(1,100) >= 0-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Hit 1 deals", (Damage))
			print("Hit 2 deals", (Damage))
			print("Hit 3 deals", (Damage))
			print("---------------")
def DrizzleManiac(User,Weapon):
	u=User
	uSTR=u+"STR"
	e=input("Enemy is: ")
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	ePAR=e+"PAR"
	eTGH=e+"TGH"
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 9 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Damage dealt is", (((((WSD[uSKL]+WSD[uABL]*0.25-WSD[ePAR]-WSD[eTGH])*0.6)*0.75)*3)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 0-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", ((((WSD[uSKL]+WSD[uABL]*0.25-WSD[ePAR]-WSD[eTGH])*0.6)*0.75)*3)+wPD)
			print("---------------")
def BlitzManiac(User,Weapon,Element):
	u=User
	e="DummyFoe"
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-(OmniWeapData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	eEVA=e+"EVA"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 50 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit!!")
		print("Base Damage is", (((((WSD[uSKL]+WSD[uABL]*0.25)*0.6)*0.75)*3)*2)+wPD)
		print("---------------")
	else:
		if ra.randint(1,100) >= 25-WSD[uABL]-WSD[uSKL]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit!!")
			print("Base Damage is", ((((WSD[uSKL]+WSD[uABL]*0.25)*0.6)*0.75)*3)+wPD)
			print("---------------")
		else:
			print("---------------")
			print(u, "missed", e+"!")
			print("---------------")
def CircleSlider(User,Weapon):
	print("Placeheld.")
	
#Offensive Spells
#Flame: Tier I
def Fireball(User,Weapon):
	u=User
	e=input("Target is: ")
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eMAR=e+"MAR"
	eRES=e+"RES"
	eEVA=e+"EVA"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 5 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit against",e+"!")
		print("Damage dealt is",(WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])*2+wMD)
		print(e,"is burning! They take 3% Max HP once per turn, for 3 turns!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-WSD[uABL]-WSD[uSPR]*0.25+WSD[eEVA]-wAC:
			print("---------------")
			print(u,"landed a Direct Hit against",e+"!")
			print("Damage dealt is",(WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])+wMD)
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e+"!")
			print("---------------")
def FlameBlast(User,Weapon):
	u=User
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1MAR=e1+"MAR"
	e1RES=e1+"RES"
	e1EVA=e1+"EVA"
	e2MAR=e2+"MAR"
	e2RES=e2+"RES"
	e2EVA=e2+"EVA"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e1, "and", e2, "!")
		print("Damage dealt to", e1, "is", ((WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e1MAR]-WSD[e1RES])*2)+wMD)
		print("Damage dealt to", e2, "is", ((WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e2MAR]-WSD[e2RES])*2)+wMD)
		print(e1,"and", e2, "are Burning! They take 3% Max HP as damage every turn, for 3 turns!!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 30-WSD[uABL]-WSD[uSPR]*0.25-WSD[uLCK]+WSD[e1EVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e1, " with Flame Blast!!")
			print("Damage dealt to", e1, "is", (WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e1MAR]-WSD[e1RES])+wMD)
			print("---------------")
			if ra.randint(1,100) >= 60-WSD[uLCK]+WSD[e1RES]*0.5:
				print("---------------")
				print(e1,"is Burning! They take damage every turn - 3 turns remaining!")
				print("---------------")
		else:
			print("---------------")
			print("You missed", e1, "this time!")
			print("---------------")
		if ra.randint(1,100) >= 30-WSD[uABL]-WSD[uSPR]*0.25-WSD[uLCK]+WSD[e2EVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e2, "with Flame Blast!")
			print("Damage dealt is", (WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e2MAR]-WSD[e2RES])+wMD)
			print("---------------")
			if ra.randint(1,100) >= 60-WSD[uLCK]+WSD[e2RES]*0.5:
				print("---------------")
				print(e2,"is Burning! They take damage every turn - 3 turns remaining!")
				print("---------------")
		else:
			print("---------------")
			print("You missed", e2, "this time!")
			print("---------------")
			
#Flame: Tier IV
def LavaLaser(User,Weapon):
	u=User
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uMAR=u+"MAR"
	uPAR=u+"PAR"
	uLCK=u+"LCK"
	e=input("Target Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	eSTR=e+"STR"
	eSPR=e+"SPR"
	eSKL=e+"SKL"
	eABL=e+"ABL"
	eAGI=e+"AGI"
	eEVA=e+"EVA"
	eTGH=e+"TGH"
	eRES=e+"RES"
	eMAR=e+"MAR"
	ePAR=e+"PAR"
	eLCK=e+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	print("---------------")
	print(u,"spent 40 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit!")
		print("Damage Dealt is",(WSD[uSPR]*1.5+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*2+wMD)
		print("---------------")
	else:
		if ra.randint(1,00) >= 30-WSD[uLCK]-WSD[uABL]-WSD[uSPR]*0.25+WSD[eEVA]:
			print("---------------")
			print(u,"landed a Direct Hit!")
			print("Damage Dealt is",(WSD[uSPR]*1.5+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])+wMD)
			print("---------------")
		else:
			print("---------------")
			print("You missed!")
			print("---------------")
		
#Earth: Tier I
def EarthenHammer(User,Weapon):
	u=User
	e=input("Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	eMAR=e+"MAR"
	eRES=e+"RES"
	eEVA=e+"EVA"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Damage dealt is", ((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])*2)+wMD)
		print(e,"is Silenced! They cannot use Skills!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-WSD[uABL]-WSD[uSPR]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", (WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])+wMD)
			print("---------------")
			if ra.randint(1,100) >= 75-WSD[uLCK]+WSD[eRES]*0.5:
				print("---------------")
				print(e,"is Silenced! They cannot use Skills!")
				print("---------------")
		else:
			print("---------------")
			print("You missed", e, "this time!")
			print("---------------")
#Wind: Tier I
def WindyWhip(User,Weapon):
	u=User
	e=input("Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	eMAR=e+"MAR"
	eRES=e+"RES"
	eEVA=e+"EVA"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Damage dealt is", ((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])*2)+wMD)
		print(e,"is Clouded! They cannot aggro anyone this turn!!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-WSD[uABL]-WSD[uSPR]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", (WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])+wMD)
			print("---------------")
			if ra.randint(1,100) >= 40-WSD[uLCK]+WSD[eRES]*0.5:
				print("---------------")
				print(e,"is Clouded! They cannot aggro anyone this turn!!")
				print("---------------")
		else:
			print("---------------")
			print("You missed", e, "this time!")
			print("---------------")
#Lightning: Tier I
def StunBolt(User,Weapon):
	u=User
	e=input("Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	eMAR=e+"MAR"
	eRES=e+"RES"
	eEVA=e+"EVA"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Damage dealt is", ((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])*2)+wMD)
		print(e,"is Stunned! They cannot change Zones or Counterattack!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 20-WSD[uABL]-WSD[uSPR]*0.25-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt is", (WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eMAR]-WSD[eRES])+wMD)
			print("---------------")
			if ra.randint(1,100) >= 75-WSD[uLCK]+WSD[eRES]*0.5:
				print("---------------")
				print(e,"is Stunned! They cannot change Zones or Counterattack!")
				print("---------------")
		else:
			print("---------------")
			print("You missed", e, "this time!")
			print("---------------")
#Water: Tier I
def WaterGrenade(User,Weapon):
	u=User
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	uSTR=u+"STR"
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1MAR=e1+"MAR"
	e1RES=e1+"RES"
	e1EVA=e1+"EVA"
	e2MAR=e2+"MAR"
	e2RES=e2+"RES"
	e2EVA=e2+"EVA"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e, "and", e2, "!")
		print("Damage dealt to", e1, "is", ((WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e1MAR]-WSD[e1RES])*2)+wMD)
		print("Damage dealt to", e2, "is", ((WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e2MAR]-WSD[e2RES])*2)+wMD)
		print(e,"is Stunned! They cannot change Zones or Counterattack!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 30-WSD[uABL]-WSD[uSPR]*0.25-WSD[uLCK]+WSD[e1EVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e1, " with Water Grenade!!")
			print("Damage dealt to", e1, "is", (WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e1MAR]-WSD[e1RES])+wMD)
			print("---------------")
			if ra.randint(1,100) >= 10-WSD[uLCK]+WSD[e1RES]*0.5:
				print("---------------")
				print(e1,"is Doused! They're weak to Lightning for 2 Turns!")
				print("---------------")
		else:
			print("---------------")
			print("You missed", e1, "this time!")
			print("---------------")
		if ra.randint(1,100) >= 30-WSD[uABL]-WSD[uLCK]+WSD[e2EVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e2, "with Flame Blast!")
			print("Damage dealt is", (WSD[uSPR]*0.5+WSD[uABL]*0.25-WSD[e2MAR]-WSD[e2RES])+wMD)
			print("---------------")
			if ra.randint(1,100) >= 10-WSD[uLCK]+WSD[e2RES]*0.5:
				print("---------------")
				print(e2,"is Doused! They're weak to Lightning for 2 Turns!")
				print("---------------")
		else:
			print("---------------")
			print("You missed", e2, "this time!")
			print("---------------")

#Support Magic
#Health Restoring: Tier I
def HealthyGlow(User,Weapon):
	u=User
	a1=input("Ally 1 is: ")
	a2=input("Ally 2 is: ")
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	a1HP=float(input("Max HP of Ally 1 is: "))
	a2HP=float(input("Max HP of Ally 2 is: "))
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(a1,"is Critically healed for", ((WSD[uSPR]*0.25+WSD[uABL]+a1HP*0.1)*2)+wMD)
		print(a2,"is Critically healed for", ((WSD[uSPR]*0.25+WSD[uABL]+a2HP*0.1)*2)+wMD)
		print("---------------")
	else:
		print("---------------")
		print(a1,"is healed for", (WSD[uSPR]*0.25+WSD[uABL]+a1HP*0.1)+wMD)
		print(a2,"is healed for", (WSD[uSPR]*0.25+WSD[uABL]+a2HP*0.1)+wMD)
		print("---------------")
def HealthyRay(User,Weapon):
	u=User
	a=input("Ally is: ")
	aHP=float(input("Max HP is: "))
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uSPR=u+"SPR"
	uABL=u+"ABL"
	print("---------------")
	print(u,"spent 15 ENE.")
	print(a,"is healed for", (WSD[uSPR]*0.25+WSD[uABL]*0.25+aHP*0.3)+wMD*0.25)
	print("---------------")
#Status Curing: Tier I
def RestorativeRay(User,Weapon):
	u=User
	a=input("Ally is: ")
	wMD=OmniWeapData[Weapon][1]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	aINF=input(u, "is trying to cure", a, "of this status: ")
	cBST=float(input("User Crit Boost is: "))
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= 100-WSD[uLCK]*0.5-cBST-wMD*0.5:
		print("---------------")
		print(a,"is cured of all negative statuses due to a critical hit!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-WSD[uLCK]-wMD:
			print("---------------")
			print(a,"is cured of", aINF, "!")
			print("---------------")
			
#Monster Skills
#May be learned by players using specific accessories or consuming Monster Meat
#Savage Bite
def SavageBite(User):
	u=User
	uAGI=u+"AGI"
	e=input("Target is: ")
	cBST=float(input("User Crit Chance Boost is: "))
	uSTR=u+"STR"
	eEVA=e+"EVA"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit against",e,"using Savage Bite!")
		print("Damage dealt is", (WSD[uSTR]+WSD[uABL]*0.25-WSD[eTGH]+WSD[ePAR])*2)
		print("---------------")
	else:
		if ra.randint(1,100) >= 75-WSD[uLCK]-WSD[uAGI]+WSD[eEVA]:
			print("---------------")
			print(u,"landed a Direct Hit against",e,"using Savage Bite!")
			print("Damage dealt is", min(10,(WSD[uSTR]+WSD[uABL]*0.25-WSD[eTGH]+WSD[ePAR])))
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e)
			print("---------------")
#Vampire Blade
#Use the Weapon field to boost power by naming Sabers or Knives in it.
def VampireBlade(User,Weapon,Element):
	u=User
	e=input("Target is: ")
	cBST=float(input("User Crit Chance Boost is: "))
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	eRES=e+"RES"
	eMAR=e+"MAR"
	eEVA=e+"EVA"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	Hit=35-WSD[uABL]+WSD[eEVA]-wAC
	Damage=(WSD[uSPR]*1.15+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])+wPD
	ENE=25
	uELM=Element
	eELM=e+"ELM"
	SingleTargetP(User,Weapon,ENE,CritChance,Damage,Hit,cBST,e,wPD,uELM,eELM)
def HPLeech(User,Weapon):
	u=User
	e=input("Target is: ")
	cBST=float(input("User Crit Chance Boost is: "))
	wPD=OmniWeapData[Weapon][0]
	uSTR=u+"STR"
	wAC=OmniWeapData[Weapon][2]+min(0,(WSD[uSTR]-OmniWeapData[Weapon][3]))
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	eRES=e+"RES"
	eMAR=e+"MAR"
	eEVA=e+"EVA"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print(u,"spent 40 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Damage dealt to",e,"is", (WSD[uSPR]*0.5+WSD[uABL]*0.5-WSD[eRES]-WSD[eMAR])*2)
		print("Health stolen is", ((WSD[uSPR]*0.5+WSD[uABL]*0.5-WSD[eRES]-WSD[eMAR])*2)*0.33)
		print("---------------")
	else:
		if ra.randint(1,100) >=70-WSD[uLCK]+WSD[eEVA]-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt to",e,"is", (WSD[uSPR]*0.5+WSD[uABL]*0.5-WSD[eRES]-WSD[eMAR]))
			print("Health stolen is", (WSD[uSPR]*0.5+WSD[uABL]*0.5-WSD[eRES]-WSD[eMAR])*0.33)
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e,"with Health Leech!")
			print("---------------")

def Webshot(User):
	u=User
	e=input("Target is: ")
	cBST=float(input("User Crit Chance Boost is: "))
	uSKL=u+"SKL"
	uABL=u+"ABL"
	eAGI=e+"AGI"
	eEVA=e+"EVA"
	eSTR=e+"STR"
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	uLCK=u+"LCK"
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print("Spent 10 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"scored a Critical Hit! Damage dealt is",(WSD[uSKL]*0.75+WSD[uABL]*0.25-WSD[eTGH]-WSD[ePAR])*2)
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSKL]*0.25-WSD[uABL]+WSD[eEVA]:
			print("---------------")
			print(u,"scored a Direct Hit! Damage daelt is",())
			print("---------------")
			if ra.randint(1,100) >= 65+WSD[eSTR]*0.75:
				print("---------------")
				print(e,"is Snared! They cannot change Zones or Dodge until they break free!")
				print("---------------")
			else:
				print("---------------")
				print("Failed to Snare target.")
				print("---------------")
		else:
			print("---------------")
			print(u,"missed",e+"!")
			print("---------------")

def BreathAttack(User,Element):
	u=User
	e=input("Target is: ")
	cBST=float(input("User Crit Chance Boost is: "))
	telm=e+"ELM"
	uSPR=u+"SPR"
	uABL=u+"ABL"
	uLCK=u+"LCK"
	eRES=e+"RES"
	eMAR=e+"MAR"
	eEVA=e+"EVA"
	ENE=15
	Hit=50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]
	CritChance=(100-WSD[uLCK]*0.5-cBST)
	print("---------------")
	print("Spent 15 ENE.")
	print("---------------")
	if Element == "Aqua" or Element == "Water":
		telm=input("Target element is: ")
		if telm == "Fire" or telm == "Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Elec" or telm == "Lightning":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR]))*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
	elif Element == "Flame" or Element == "Fire":
		telm=input("Target element is: ")
		if telm == "Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Flame" or telm == "Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Aqua" or telm == "Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR]))*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
	elif Element == "Earth":
		telm=input("Target element is: ")
		if telm == "Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Flame" or telm == "Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR]))*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
	elif Element == "Elec" or Element == "Lightning":
		telm=input("Target element is: ")
		if telm == "Aqua" or telm == "Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Elec" or telm == "Lightning":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR]))*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
	elif Element == "Wind":
		telm=input("Target element is: ")
		if telm == "Elec" or telm == "Lightning":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*1.2))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.6))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		elif telm == "Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8)*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])*0.8))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print("Dealt a critical hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR]))*2)
				print("---------------")
			elif ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSPR]*0.25+WSD[eEVA]:
				print("---------------")
				print("Dealt a direct hit!")
				print("Damage dealt is ",((WSD[uSPR]*0.75+WSD[uABL]*0.25-WSD[eRES]-WSD[eMAR])))
				print("---------------")
			else:
				print("---------------")
				print("You missed!")
				print("---------------")