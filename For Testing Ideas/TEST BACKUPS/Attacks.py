from WSD2 import WSD
from WSD2 import Unit
from WSD2 import Weapon
from WSD2 import Equipment
import random as ra
from WeaponsOO import OmniWeaponData
def ProcSingle(User,e,uELM,eELM):
	u=User
	if uELM=="Flame" or uELM=="Fire" and eELM!="Flame" or eELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and eELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and eELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM!="Lightning" or eELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM!="Water" or eELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
def ProcDouble(User,e1,e2,uELM,e1ELM,e2ELM):
	u=User
	if uELM=="Flame" or uELM=="Fire" and e1ELM!="Flame" or e1ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e1ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e1ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM!="Lightning" or e1ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM!="Water" or e1ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Doggo
	if uELM=="Flame" or uELM=="Fire" and e2ELM!="Flame" or e2ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e2ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e2ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM!="Lightning" or e2ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM!="Water" or e2ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
def ProcTriple(User,e1,e2,e3,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	if uELM=="Flame" or uELM=="Fire" and e1ELM!="Flame" or e1ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e1ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e1ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM!="Lightning" or e1ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM!="Water" or e1ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Doggo
	if uELM=="Flame" or uELM=="Fire" and e2ELM!="Flame" or e2ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e2ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e2ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM!="Lightning" or e2ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM!="Water" or e2ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Catto
	if uELM=="Flame" or uELM=="Fire" and e3ELM!="Flame" or e3ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e3ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e3ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM!="Lightning" or e3ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM!="Water" or e3ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")

def SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM):
	u=User
	choice=input("Which Attack Type are you using today?\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
	if choice == "Q" or choice == "q":
		print("---------------")
		print(u,"spent",qENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round((Damage*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	elif choice == "N" or choice == "n":
		print("---------------")
		print(u,"spent",nENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	elif choice == "H" or choice == "h":
		print("---------------")
		print(u,"spent",hENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round((Damage*1.25)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	ProcSingle(User,e,uELM,eELM)

def SingleChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,cBST,e,wMD,uELM,eELM):
	u=User
	choice=input("Which Attack Type are you using today?\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
	if choice == "Q" or choice == "q":
		print("---------------")
		print(u,"spent",qENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round((Damage*0.75)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*0.75)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	elif choice == "N" or choice == "n":
		print("---------------")
		print(u,"spent",nENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
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
				if ra.randint (1,100) >= nHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	elif choice == "H" or choice == "h":
		print("---------------")
		print(u,"spent",hENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round(((Damage*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage dealt is",round((Damage*1.25)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage dealt is",round((Damage*1.25)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	ProcSingle(User,e,uELM,eELM)

def BattlecannonElement(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	choice=input("Which Attack Type are you using today?\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
	if choice == "Q" or choice == "q":
		print("---------------")
		print(u,"spent",qENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1/3)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/3)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2/3)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/3)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3/3)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/3)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	elif choice == "N" or choice == "n":
		print("---------------")
		print(u,"spent",nENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1/2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1/2)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2/2/3)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2/2/3)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3/2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3/2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3/2)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	elif choice == "H" or choice == "h":
		print("---------------")
		print(u,"spent",hENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT1:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
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
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	ProcTriple(User,e1,e2,e3,uELM,e1ELM,e2ELM,e3ELM)

def DualChoiceM(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,e1,e2,wMD,uELM,e1ELM,e2ELM):
	u=User
	choice=input("Which Attack Type are you using today?\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
	if choice == "Q" or choice == "q":
		print("---------------")
		print(u,"spent",qENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*0.75)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2*0.75)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
	elif choice == "N" or choice == "n":
		print("---------------")
		print(u,"spent",nENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
	elif choice == "H" or choice == "h":
		print("---------------")
		print(u,"spent",hENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*1.25)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2*1.25)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
	ProcDouble(User,e1,e2,uELM,e1ELM,e2ELM)

def DualChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,e1,e2,wPD,uELM,e1ELM,e2ELM):
	u=User
	choice=input("Which Attack Type are you using today?\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
	if choice == "Q" or choice == "q":
		print("---------------")
		print(u,"spent",qENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
	elif choice == "N" or choice == "n":
		print("---------------")
		print(u,"spent",nENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				print("Damage dealt is",round((Damage2*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
	elif choice == "H" or choice == "h":
		print("---------------")
		print(u,"spent",hENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*1.25)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
	ProcDouble(User,e1,e2,uELM,e1ELM,e2ELM)

def TripleChoiceM(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wMD,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	choice=input("Which Attack Type are you using today?\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
	if choice == "Q" or choice == "q":
		print("---------------")
		print(u,"spent",qENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*0.75)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2*0.75)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3*0.75)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	elif choice == "N" or choice == "n":
		print("---------------")
		print(u,"spent",nENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2*0.75)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	elif choice == "H" or choice == "h":
		print("---------------")
		print(u,"spent",hENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*1.25)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3*1.25)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	ProcTriple(User,e1,e2,e3,uELM,e1ELM,e2ELM,e3ELM)

def TripleChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	choice=input("Which Attack Type are you using today?\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
	if choice == "Q" or choice == "q":
		print("---------------")
		print(u,"spent",qENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round((Damage2*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*0.75)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	elif choice == "N" or choice == "n":
		print("---------------")
		print(u,"spent",nENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT1:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				if ra.randint (1,100) >= nHIT2:
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
				print("Damage dealt is",round((Damage2*0.75)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= qHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*0.75)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	elif choice == "H" or choice == "h":
		print("---------------")
		print(u,"spent",hENE,"ENE.")
		print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Earth" and e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Wind" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round(((Damage1*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e1+"!")
				print("Damage dealt is",round((Damage1*1.25)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT1:
					print("---------------")
					print(u,"landed a Direct Hit against",e1+"!")
					print("Damage dealt is",round((Damage1*1.25)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e1+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Earth" and e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Wind" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e2+"!")
				print("Damage dealt is",round(((Damage2*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= hHIT2:
					print("---------------")
					print(u,"landed a Direct Hit against",e2+"!")
					print("Damage dealt is",round((Damage2*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e2+"!")
					print("---------------")
		if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Earth" and e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Wind" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round(((Damage3*1.25)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e3+"!")
				print("Damage dealt is",round((Damage3*1.25)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= nHIT3:
					print("---------------")
					print(u,"landed a Direct Hit against",e3+"!")
					print("Damage dealt is",round((Damage3*1.25)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e3+"!")
					print("---------------")
	ProcTriple(User,e1,e2,e3,uELM,e1ELM,e2ELM,e3ELM)

#Magic Weapons
def Tome(User,Weapon,Element):
	u=User
	e=input("Target is: ")
	uELM=Element
	eELM=WSD[e].Element
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	eMDEF=WSD[e].MDEF
	wMD=OmniWeaponData[Weapon][1]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	Damage=round((uSPR*1.1+uABL*0.25-eMDEF*0.85))
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=(35-uABL-uSPR*0.25-uLCK+eEVA-wAC)
	qENE=15
	nHIT=(50-uABL-uSPR*0.25-uLCK+eEVA-wAC)
	nENE=25
	hHIT=(65-uABL-uSPR*0.25-uLCK+eEVA-wAC)
	hENE=35
	SingleChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,cBST,e,wMD,uELM,eELM)

def UnlearnedTome(User,Weapon,Element):
	u=User
	e=input("Target is: ")
	uELM=Element
	eELM=WSD[e].Element
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	eMDEF=WSD[e].MDEF
	wMD=OmniWeaponData[Weapon][1]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	Damage=round((uSPR*1.1+uABL*0.25-eMDEF*0.85)*0.5)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=(35-uABL-uSPR*0.25-uLCK+eEVA-wAC)
	qENE=15
	nHIT=(50-uABL-uSPR*0.25-uLCK+eEVA-wAC)
	nENE=25
	hHIT=(65-uABL-uSPR*0.25-uLCK+eEVA-wAC)
	hENE=35
	SingleChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,cBST,e,wMD,uELM,eELM)
#Wands
def WandRay(User,Weapon,Element):
	u=User
	uELM=Element
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	e=input("Target is: ")
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	eELM=WSD[e].Element
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	Damage=round((uSPR*0.5+uABL*0.25-eRES)*0.75)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-30-uABL-uSPR*0.25-eEVA-wAC
	qENE=10
	nHIT=0-15-uABL-uSPR*0.25-eEVA-wAC
	nENE=20
	hHIT=0-uABL-uSPR*0.25-eEVA-wAC
	hENE=30
	SingleChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,cBST,e,wMD,uELM,eELM)

def UnlearnedWandRay(User,Weapon,Element):
	u=User
	uELM=Element
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	e=input("Target is: ")
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	eELM=WSD[e].Element
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	Damage=round(((uSPR*0.5+uABL*0.25-eRES)*0.75)*0.5)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-30-uABL-uSPR*0.25-eEVA-wAC
	qENE=3
	nHIT=0-15-uABL-uSPR*0.25-eEVA-wAC
	nENE=9
	hHIT=0-uABL-uSPR*0.25-eEVA-wAC
	hENE=12
	SingleChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,cBST,e,wMD,uELM,eELM)

#Card Blast: Magic Attack for Talises
def CardBlast(User,Weapon,Element):
	u=User
	uELM=Element
	wMD=OmniWeaponData[Weapon][1]
	wAC=OmniWeaponData[Weapon][2]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1=input("Target is: ")
	uLCK=WSD[u].LCK
	e1ELM=WSD[e1].Element
	e1MAR=WSD[e1].MAR
	e1RES=WSD[e1].RES
	e1EVA=WSD[e1].EVA
	e2ELM=WSD[e2].Element
	e2MAR=WSD[e2].MAR
	e2RES=WSD[e2].RES
	e2EVA=WSD[e2].EVA
	e3ELM=WSD[e3].Element
	e3MAR=WSD[e3].MAR
	e3RES=WSD[e3].RES
	e3EVA=WSD[e3].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	Damage1=round(uSPR*0.65+uABL*0.35-WSD[e1RES]-WSD[e1MAR])
	Damage2=round(uSPR*0.65+uABL*0.35-WSD[e2RES]-WSD[e2MAR])
	Damage3=round(uSPR*0.65+uABL*0.35-WSD[e3RES]-WSD[e3MAR])
	CritChance=(100-uLCK*0.5-cBST)
	q1HIT=20-uABL*1.25-uLCK+e1EVA-wAC
	q2HIT=20-uABL*1.25-uLCK+e2EVA-wAC
	q3HIT=20-uABL*1.25-uLCK+e3EVA-wAC
	qENE=5
	n1HIT=35-uABL*1.25-uLCK+e1EVA-wAC
	n2HIT=35-uABL*1.25-uLCK+e2EVA-wAC
	n3HIT=35-uABL*1.25-uLCK+e3EVA-wAC
	nENE=10
	h1HIT=50-uABL*1.25-uLCK+e1EVA-wAC
	h2HIT=50-uABL*1.25-uLCK+e2EVA-wAC
	h3HIT=50-uABL*1.25-uLCK+e3EVA-wAC
	hENE=15
	TripleChoiceM(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wMD,uELM,e1ELM,e2ELM,e3ELM)

def UnlearnedCardBlast(User,Weapon,Element):
	u=User
	uELM=Element
	wMD=OmniWeaponData[Weapon][1]
	wAC=OmniWeaponData[Weapon][2]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1=input("Target is: ")
	uLCK=WSD[u].LCK
	e1ELM=WSD[e1].Element
	e1MAR=WSD[e1].MAR
	e1RES=WSD[e1].RES
	e1EVA=WSD[e1].EVA
	e2ELM=WSD[e2].Element
	e2MAR=WSD[e2].MAR
	e2RES=WSD[e2].RES
	e2EVA=WSD[e2].EVA
	e3ELM=WSD[e3].Element
	e3MAR=WSD[e3].MAR
	e3RES=WSD[e3].RES
	e3EVA=WSD[e3].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	Damage1=round(uSPR*0.65+uABL*0.35-WSD[e1RES]-WSD[e1MAR])*0.5
	Damage2=round(uSPR*0.65+uABL*0.35-WSD[e2RES]-WSD[e2MAR])*0.5
	Damage3=round(uSPR*0.65+uABL*0.35-WSD[e3RES]-WSD[e3MAR])*0.5
	CritChance=(100-uLCK*0.5-cBST)
	q1HIT=20-uABL*1.25-uLCK+e1EVA-wAC
	q2HIT=20-uABL*1.25-uLCK+e2EVA-wAC
	q3HIT=20-uABL*1.25-uLCK+e3EVA-wAC
	qENE=5
	n1HIT=35-uABL*1.25-uLCK+e1EVA-wAC
	n2HIT=35-uABL*1.25-uLCK+e2EVA-wAC
	n3HIT=35-uABL*1.25-uLCK+e3EVA-wAC
	nENE=10
	h1HIT=50-uABL*1.25-uLCK+e1EVA-wAC
	h2HIT=50-uABL*1.25-uLCK+e2EVA-wAC
	h3HIT=50-uABL*1.25-uLCK+e3EVA-wAC
	hENE=15
	TripleChoiceM(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wMD,uELM,e1ELM,e2ELM,e3ELM)
#Rod Shot: Magic Blasts for Rods
def RodShot(User,Weapon,Element):
	u=User
	uELM=Element
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eMAR=WSD[e].MAR
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	uABL=WSD[u].ABL
	Damage=round(uSPR*1.25+uABL*0.25-eRES-eMAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=30-uABL-uSPR*0.25-wAC-uLCK+eEVA
	qENE=15
	nHIT=45-uABL-uSPR*0.25-wAC-uLCK+eEVA
	nENE=20
	hHIT=60-uABL-uSPR*0.25-wAC-uLCK+eEVA
	hENE=25
	SingleChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,cBST,e,wMD,uELM,eELM)

def UnlearnedRodShot(User,Weapon,Element):
	u=User
	uELM=Element
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eMAR=WSD[e].MAR
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	Damage=round(uSPR*1.25+uABL*0.25-eRES-eMAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=40-uABL-uSPR*0.25-wAC-uLCK+eEVA
	qENE=15
	nHIT=55-uABL-uSPR*0.25-wAC-uLCK+eEVA
	nENE=20
	hHIT=70-uABL-uSPR*0.25-wAC-uLCK+eEVA
	hENE=25
	SingleChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,cBST,e,wMD,uELM,eELM)

def Battlecannon(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Target 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Target 2 is: ")
	e2ELM=WSD[e2].Element
	e3=input("Target 3 is: ")
	e3ELM=WSD[e3].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	wPD=OmniWeaponData[Weapon][0]
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	Damage1=round((uSKL*1.5+uABL*0.25-e1TGH-e1PAR))
	Damage2=round((uSKL*1.5+uABL*0.25-e2TGH-e2PAR))
	Damage3=round((uSKL*1.5+uABL*0.25-e3TGH-e3PAR))
	qENE=15
	nENE=25
	hENE=35
	qHIT1=30-uSKL*0.25-uABL+e1EVA-wAC
	qHIT2=30-uSKL*0.25-uABL+e2EVA-wAC
	qHIT3=30-uSKL*0.25-uABL+e3EVA-wAC
	nHIT1=40-uSKL*0.25-uABL+e1EVA-wAC
	nHIT2=40-uSKL*0.25-uABL+e2EVA-wAC
	nHIT3=40-uSKL*0.25-uABL+e3EVA-wAC
	hHIT1=50-uSKL*0.25-uABL+e1EVA-wAC
	hHIT2=50-uSKL*0.25-uABL+e2EVA-wAC
	hHIT3=50-uSKL*0.25-uABL+e3EVA-wAC
	BattlecannonElement(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM)

def UnlearnedBattlecannon(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Target 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Target 2 is: ")
	e2ELM=WSD[e2].Element
	e3=input("Target 3 is: ")
	e3ELM=WSD[e3].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	wPD=OmniWeaponData[Weapon][0]
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	Damage1=round((uSKL*1.5+uABL*0.25-e1TGH-e1PAR)*0.5)
	Damage2=round((uSKL*1.5+uABL*0.25-e2TGH-e2PAR)*0.5)
	Damage3=round((uSKL*1.5+uABL*0.25-e3TGH-e3PAR)*0.5)
	qENE=15
	nENE=25
	hENE=35
	qHIT1=30-uSKL*0.25-uABL+e1EVA-wAC
	qHIT2=30-uSKL*0.25-uABL+e2EVA-wAC
	qHIT3=30-uSKL*0.25-uABL+e3EVA-wAC
	nHIT1=40-uSKL*0.25-uABL+e1EVA-wAC
	nHIT2=40-uSKL*0.25-uABL+e2EVA-wAC
	nHIT3=40-uSKL*0.25-uABL+e3EVA-wAC
	hHIT1=50-uSKL*0.25-uABL+e1EVA-wAC
	hHIT2=50-uSKL*0.25-uABL+e2EVA-wAC
	hHIT3=50-uSKL*0.25-uABL+e3EVA-wAC
	BattlecannonElement(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM)

def Warhammer(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	wPD=OmniWeaponData[Weapon][0]
	uABL=WSD[u].ABL
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	uAGI=WSD[u].AGI
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	eELM=WSD[e].Element
	Damage=round((uSTR*1.5+uABL*0.25-eTGH-ePAR))
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=(40-uAGI-uSTR*0.25+eEVA-wAC)
	qENE=10
	nHIT=(55-uAGI-uSTR*0.25+eEVA-wAC)
	nENE=15
	hHIT=(70-uAGI-uSTR*0.25+eEVA-wAC)
	hENE=20
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	
def UnlearnedWarhammer(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	wPD=OmniWeaponData[Weapon][0]
	uABL=WSD[u].ABL
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	uAGI=WSD[u].AGI
	eEVA=WSD[e].EVA
	eELM=WSD[e].Element
	uLCK=WSD[u].LCK
	Damage=round((uSTR*1.5+uABL*0.25-eTGH-ePAR))*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=(40-uAGI-uSTR*0.25+eEVA-wAC)
	qENE=10
	nHIT=(55-uAGI-uSTR*0.25+eEVA-wAC)
	nENE=15
	hHIT=(70-uAGI-uSTR*0.25+eEVA-wAC)
	hENE=20
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	
def Whip(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	wPD=OmniWeaponData[Weapon][0]
	uABL=WSD[u].ABL
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	uAGI=WSD[u].AGI
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	Damage=round((uSTR*1.2+uABL*0.25-eTGH-ePAR)*1.15)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=40-uAGI-uSTR*0.25+eEVA-wAC
	qENE=4
	nHIT=50-uAGI-uSTR*0.25+eEVA-wAC
	nENE=6
	hHIT=60-uAGI-uSTR*0.25+eEVA-wAC
	hENE=8
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	
def Whip(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	wPD=OmniWeaponData[Weapon][0]
	uABL=WSD[u].ABL
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	uAGI=WSD[u].AGI
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	Damage=round((uSTR*1.2+uABL*0.25-eTGH-ePAR)*1.15)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=40-uAGI-uSTR*0.25+eEVA-wAC
	qENE=4
	nHIT=50-uAGI-uSTR*0.25+eEVA-wAC
	nENE=6
	hHIT=60-uAGI-uSTR*0.25+eEVA-wAC
	hENE=8
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Instrument Abilities
def Mic(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1MAR=e1+"MAR"
	e1RES=e1+"RES"
	e1EVA=WSD[e1].EVA
	e2MAR=e2+"MAR"
	e2RES=e2+"RES"
	e2EVA=WSD[e2].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage1=round(uSPR-WSD[e1RES]-WSD[e1MAR])
	Damage2=round(uSPR-WSD[e2RES]-WSD[e2MAR])
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0
	qENE=5
	nHIT=0-uABL-uSPR*0.25-uLCK+e1EVA-wAC
	nENE=10
	hHIT=15-uABL-uSPR*0.25-uLCK+eEVA-wAC
	hENE=15
	DualChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,cBST,e,wMD)
	
def UnlearnedMic(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1MAR=e1+"MAR"
	e1RES=e1+"RES"
	e1EVA=WSD[e1].EVA
	e2MAR=e2+"MAR"
	e2RES=e2+"RES"
	e2EVA=WSD[e2].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage1=round((uSPR-WSD[e1RES]-WSD[e1MAR]))*0.5
	Damage2=round((uSPR-WSD[e2RES]-WSD[e2MAR]))*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0
	qENE=5
	nHIT=0-uABL-uSPR*0.25-uLCK+e1EVA-wAC
	nENE=10
	hHIT=15-uABL-uSPR*0.25-uLCK+eEVA-wAC
	hENE=15
	DualChoiceM(User,qENE,nENE,hENE,CritChance,Damage,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,cBST,e,wMD)
	
#Knuckles: No Traits
def Knuckles(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSTR+uABL*0.35-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=1
	nHIT=15-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=3
	hHIT=30-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=5
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	
def UnlearnedKnuckles(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSTR+uABL*0.35-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=1
	nHIT=15-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=3
	hHIT=30-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=5
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Knuckles: Bareknuckle Boxer. Damage +20%.
def BareKnuckles(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(((uSTR+uABL*0.35-eTGH-ePAR))*1.2)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=(0-uABL-uSTR*0.25-uLCK+eEVA-wAC)
	qENE=1
	nHIT=(15-uABL-uSTR*0.25-uLCK+eEVA-wAC)
	nENE=3
	hHIT=(30-uABL-uSTR*0.25-uLCK+eEVA-wAC)
	hENE=5
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Knives: No Traits
def Knife(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uAGI-uLCK-uSTR*0.25+eEVA-wAC
	qENE=2
	nHIT=15-uAGI-uLCK-uSTR*0.25+eEVA-wAC
	nENE=5
	hHIT=30-uAGI-uLCK-uSTR*0.25+eEVA-wAC
	hENE=10
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	if ra.randint(1,100) >= 70:
		print("---------------")
		print(e,"is Bleeding!")
		print("---------------")
	
#Knives: Unlearned.
def UnlearnedKnife(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSKL*0.75+uABL*0.25-eTGH-ePAR))*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	qENE=2
	nHIT=15-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	nENE=5
	hHIT=30-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	hENE=10
	if ra.randint(1,100) >= 70:
		print("---------------")
		print(e,"is Bleeding!")
		print("---------------")
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Knives: Serrated Knife User. Bleed +30%.
def SerratedKnife(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	qENE=2
	nHIT=15-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	nENE=5
	hHIT=30-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	hENE=10
	if ra.randint(1,100) >= 40:
		print("---------------")
		print(e,"is Bleeding!")
		print("---------------")
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Knives: Knife Sharpener: Boosts Damage by 30%.
def SharpKnife(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round((uSKL*0.75+uABL*0.25-eTGH-ePAR))*1.3
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	qENE=2
	nHIT=15-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	nENE=5
	hHIT=30-uAGI-uLCK-uSTR*0.25-wAC+eEVA-wAC
	hENE=10
	print("---------------")
	print(u,"spent 2 ENE.")
	print("---------------")
	if ra.randint(1,100) >= 70:
		print("---------------")
		print(e,"is Bleeding!")
		print("---------------")
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

#Sabers: No Traits taken
def Saber(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=20-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=5
	nHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=10
	hHIT=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=15
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

def UnlearnedSaber(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=20-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=5
	nHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=10
	hHIT=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=15
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

#Sabers: Saber Sharpener. Damage +25%.
def SharpSaber(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR))*1.25
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=20-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=5
	nHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=10
	hHIT=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=15
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
			
#Sabers: Sharp Saber Sighter. Damage +25%, Accuracy +15%.
def SharpSaberSighter(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR))*1.25
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=5-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=5
	nHIT=20-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=10
	hHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=15
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Flails: No traits
def Flail(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	wPD=OmniWeaponData[Weapon][0]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSTR*1.1+uABL*0.25-eTGH*0.9-ePAR)
	Damage2=round(uSTR*1.1+uABL*0.25-eTGH*0.9)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=65-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=20
	if ra.randint >= 90:
		print("---------------")
		print("You bypass",e+"'s armor!")
		print("Quick Damage dealt is",(Damage2)*0.75+wPD)
		print("Normal Damage dealt is",(Damage2)+wPD)
		print("Hard Damage dealt is",(Damage2)*1.25+wPD)
		print("---------------")
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
		
def UnlearnedFlail(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	wPD=OmniWeaponData[Weapon][0]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSTR*1.1+uABL*0.25-eTGH*0.9-ePAR)*0.5
	Damage2=round(uSTR*1.1+uABL*0.25-eTGH*0.9)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=65-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=20
	if ra.randint >= 90:
		print("---------------")
		print("You bypass",e+"'s armor!")
		print("Quick Damage dealt is",(Damage2)*0.75+wPD)
		print("Normal Damage dealt is",(Damage2)+wPD)
		print("Hard Damage dealt is",(Damage2)*1.25+wPD)
		print("---------------")
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Flails: Flail Finisher. Ignore 15% more TGH.
def FlailFinisher(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	wPD=OmniWeaponData[Weapon][0]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSTR*1.1+uABL*0.25-eTGH*0.75-ePAR)
	Damage2=round(uSTR*1.1+uABL*0.25-eTGH*0.75)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=65-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=20
	if ra.randint >= 90:
		print("---------------")
		print("You bypass",e+"'s armor!")
		print("Quick Damage dealt is",(Damage2)*0.75+wPD)
		print("Normal Damage dealt is",(Damage2)+wPD)
		print("Hard Damage dealt is",(Damage2)*1.25+wPD)
		print("---------------")
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
		
def SixthFlail(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	wPD=OmniWeaponData[Weapon][0]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSTR*1.1+uABL*0.25-eTGH*0.75-ePAR)
	Damage2=round(uSTR*1.1+uABL*0.25-eTGH*0.75)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=35-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=65-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=20
	if ra.randint >= 60:
		print("---------------")
		print("You bypass",e+"'s armor!")
		print("Quick Damage dealt is",(Damage2)+wPD)
		print("Normal Damage dealt is",(Damage2)+wPD)
		print("Hard Damage dealt is",(Damage2)+wPD)
		print("---------------")
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

#Greatswords: No traits
def Greatsword(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	e3=input("Enemy 3 is: ")
	e3ELM=WSD[e3].Element
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	qENE=9
	nENE=18
	hENE=27
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round(((uSTR*1.25+uABL*0.25-e1TGH-e1PAR))*0.33)
	Damage2=round(((uSTR*1.25+uABL*0.25-e2TGH-e2PAR))*0.33)
	Damage3=round(((uSTR*1.25+uABL*0.25-e3TGH-e3PAR))*0.33)
	qHIT1=40-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	qHIT2=40-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	qHIT3=40-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	nHIT1=50-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	nHIT2=50-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	nHIT3=50-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	hHIT1=60-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	hHIT2=60-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	hHIT3=60-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	TripleChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,cBST,e,wPD)

def UnlearnedGreatsword(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	e3=input("Enemy 3 is: ")
	e3ELM=WSD[e3].Element
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	qENE=9
	nENE=18
	hENE=27
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round(((uSTR*1.25+uABL*0.25-e1TGH-e1PAR))*0.33)*0.5
	Damage2=round(((uSTR*1.25+uABL*0.25-e3TGH-e3PAR))*0.33)*0.5
	Damage3=round(((uSTR*1.25+uABL*0.25-e3TGH-e3PAR))*0.33)*0.5
	qHIT1=40-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	qHIT2=40-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	qHIT3=40-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	nHIT1=50-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	nHIT2=50-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	nHIT3=50-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	hHIT1=60-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	hHIT2=60-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	hHIT3=60-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	TripleChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,cBST,e,wPD)

#Greatswords: Greatsword Grinder. Damage +50%!
def GreatswordGrinder(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e3=input("Enemy 3 is: ")
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	e1ELM=WSD[e1].Element
	e2ELM=WSD[e2].Element
	e3ELM=WSD[e3].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	qENE=9
	nENE=18
	hENE=27
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round((((uSTR*1.25+uABL*0.25-e1TGH-e1PAR))/3)*1.5)
	Damage2=round((((uSTR*1.25+uABL*0.25-e3TGH-e3PAR))/3)*1.5)
	Damage3=round((((uSTR*1.25+uABL*0.25-e3TGH-e3PAR))/3)*1.5)
	qHIT1=40-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	qHIT2=40-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	qHIT3=40-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	nHIT1=50-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	nHIT2=50-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	nHIT3=50-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	hHIT1=60-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	hHIT2=60-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	hHIT3=60-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	TripleChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM)
#Polearms: no traits taken.
def Polearm(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	Damage=round(uSKL*0.35+uSTR*0.65+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=25-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=8
	nHIT=40-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=16
	hHIT=55-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=24
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
def UnlearnedPolearm(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	Damage=round(uSKL*0.35+uSTR*0.65+uABL*0.25-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=25-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=8
	nHIT=40-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=16
	hHIT=55-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=24
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Polearms: Polearm Paladin, Damage +35%
def PolearmPaladin(User,Weapon,Element):
	u=User
	e=input("Target is: ")
	uELM=Element
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	Damage=round(((uSKL*0.35+uSTR*0.65+uABL*0.25-eTGH-ePAR))*1.35)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=25-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=8
	nHIT=40-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=16
	hHIT=55-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=24
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

#Battlestaff, Battlestaves: no traits
def Staff(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round(uSTR+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=35-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=4
	nHIT=50-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=8
	hHIT=65-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=12
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	
def UnlearnedStaff(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round(uSTR+uABL*0.25-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=35-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=4
	nHIT=50-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=8
	hHIT=65-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=12
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

#Battlestaff Basher - Damage+30% with all Battlestaff attacks.
def StaffBash(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round((uSTR+uABL*0.25-eTGH-ePAR))*1.3
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=35-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	qENE=4
	nHIT=50-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	nENE=8
	hHIT=65-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	hENE=12
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

#Claws: no traits
def Claw(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	eSTR=WSD[e].STR
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=15-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	qENE=3
	nHIT=30-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	nENE=6
	hHIT=45-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	hENE=9
	if ra.randint(1,100) > 80:
		print("---------------")
		print(u,"Disarmed",e+"!")
		print("---------------")
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

def UnlearnedClaw(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	eSTR=WSD[e].STR
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=15-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	qENE=3
	nHIT=30-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	nENE=6
	hHIT=45-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	hENE=9
	if ra.randint > 80:
		print("---------------")
		print(u,"Disarmed",e+"!")
		print("---------------")
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Claws: Claw Clash. Disarm Rate +20%.
def ClawClash(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	e=input("Target is: ")
	uELM=Element
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	eSTR=WSD[e].STR
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=15-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	qENE=3
	nHIT=30-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	nENE=6
	hHIT=45-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	hENE=9
	if ra.randint > 60:
		print("---------------")
		print(u,"Disarmed",e+"!")
		print("---------------")
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Claws: Claw Cutter, damage +30%
def ClawCut(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	e=input("Target is: ")
	uELM=Element
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	eSTR=WSD[e].STR
	Damage=round((uSKL*0.75+uABL*0.25-eTGH-ePAR))*1.3
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=15-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	qENE=3
	nHIT=30-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	nENE=6
	hHIT=45-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	hENE=9
	if ra.randint > 80:
		print("---------------")
		print(u,"Disarmed",e+"!")
		print("---------------")
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
	else:
		SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Canes: No Traits Taken
def Cane(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round((uSTR*0.5+uSPR*0.25+uABL*0.25-eTGH*0.75-eRES*0.25-eMAR))
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=40-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	qENE=1
	nHIT=55-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	nENE=4
	hHIT=70-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	hENE=7
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

def UnlearnedCane(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round((uSTR*0.5+uSPR*0.25+uABL*0.25-eTGH*0.75+wPD-eRES*0.25-eMAR)*0.5)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=40-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	qENE=1
	nHIT=55-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	nENE=4
	hHIT=70-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	hENE=7
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Canes: Cane Crusher, Damage+30%
def CaneCrush(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round((uSTR*0.5+uSPR*0.25+uABL*0.25-eTGH*0.75+wPD-eRES*0.25-eMAR))*1.3
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=40-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	qENE=1
	nHIT=55-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	nENE=4
	hHIT=70-uAGI-uSPR*0.25-uLCK+eEVA-wAC
	hENE=7
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Bows: Standard, No Traits
def Bow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round(uSTR*0.75+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=20-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=12
	nHIT=35-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=50-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=18
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
def UnlearnedBow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round(uSTR*0.75+uABL*0.25-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=20-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=12
	nHIT=35-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=50-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=18
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Bows: Bow Braver, Damage+25%
def BraveBow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round((uSTR*0.75+uABL*0.25-eTGH-ePAR))*1.25
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=20-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=12
	nHIT=35-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=50-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=18
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Bows: Bow Hunter, Accuracy +25%
def BowHunter(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round(uSTR*0.75+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-5-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=12
	nHIT=10-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=25-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=18
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Bows: Bow Hunter & Bow Braver taken - BraveBowHunter! Damage & Accuracy +25% each.
def BraveBowHunter(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round((uSTR*0.75+uABL*0.25-eTGH-ePAR))*1.25
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-5-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=12
	nHIT=10-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=15
	hHIT=25-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=18
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Crossbows: No traits taken
def Crossbow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR*0.75)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=30-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=40-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=20
	hHIT=50-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=30
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

def UnlearnedCrossbow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR*0.75)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=30-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=40-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=20
	hHIT=50-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=30
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Crossbows: Crossbow Crusher. Armor Pierce +25%.
def CrossbowCrush(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR*0.5)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=30-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=40-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=20
	hHIT=50-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=30
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Crossbows: Crossbow Corrector. Accuracy +25%.
def CrossbowCorrecter(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR*0.75)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=5-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=15-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=20
	hHIT=25-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=30
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Crossbows - Crossbow Crusader. Damage+15%.
def CrossbowCrusader(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR*0.75)*1.15
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=30-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=40-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=20
	hHIT=50-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=30
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Crossbows: Crusader + Correcter. Damage +15%, Accuracy +25.
def CorrectCrossbowCrusader(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR*0.75)*1.15
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=5-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=15-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=20
	hHIT=25-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=30
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Correction + Crusader + Crusher: Crushing Correction Crusader. Ugh. Does all 3 abilities.
def CrushingCrossbowCorrectionCrusader(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR*0.5)*1.15
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=5-uABL-uSTR*0.25-uLCK+eEVA-wAC
	qENE=10
	nHIT=15-uABL-uSTR*0.25-uLCK+eEVA-wAC
	nENE=20
	hHIT=25-uABL-uSTR*0.25-uLCK+eEVA-wAC
	hENE=30
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Handbow
def Handbow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.5+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=15-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	qENE=7
	nHIT=30-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	nENE=10
	hHIT=45-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	hENE=13
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

def UnlearnedHandbow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round(uSKL*0.5+uABL*0.25-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=15-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	qENE=7
	nHIT=30-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	nENE=10
	hHIT=45-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	hENE=13
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Handbows: Handbow Harmer. Damage+20%
def HandbowHarmer(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Damage=round((uSKL*0.5+uABL*0.25-eTGH-ePAR))*1.2
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=15-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	qENE=7
	nHIT=30-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	nENE=10
	hHIT=45-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	hENE=13
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Talis
def Talis(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	Damage=round(uSTR*0.5+uSPR*0.25+uABL*0.25-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	qENE=4
	nHIT=20-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	nENE=8
	hHIT=40-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	hENE=12
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

def UnlearnedTalis(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	Damage=round(uSTR*0.5+uSPR*0.25+uABL*0.25+wPD-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	qENE=4
	nHIT=20-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	nENE=8
	hHIT=40-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	hENE=12
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Talises: Talis Tosser. Damage +20%.
def TalisToss(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	Damage=round((uSTR*0.5+uSPR*0.25+uABL*0.25+wPD-eTGH-ePAR))*1.2
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	qENE=4
	nHIT=20-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	nENE=8
	hHIT=40-uABL*0.75-uSTR*0.25-uLCK+eEVA-wAC
	hENE=12
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Slicer
def Slicer(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	e1TGH=WSD[e1].TGH
	e1EVA=WSD[e1].EVA
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e1ELM=WSD[e1].Element
	e2ELM=WSD[e2].Element
	uSTR=WSD[u].STR
	uLCK=WSD[u].LCK
	Damage1=round(uSTR*0.75+uABL*0.25-e1TGH-e1PAR)
	Damage2=round(uSTR*0.75+uABL*0.25-e2TGH-e2PAR)
	CritChance=(100-uLCK*0.5-cBST)
	qENE=8
	nENE=12
	hENE=16
	qHIT1=0-uABL-uSTR*0.25+e1EVA+wAC
	nHIT1=10-uABL-uSTR*0.25+e1EVA+wAC
	hHIT1=20-uABL-uSTR*0.25+e1EVA+wAC
	qHIT2=0-uABL-uSTR*0.25+e2EVA+wAC
	nHIT2=10-uABL-uSTR*0.25+e2EVA+wAC
	hHIT2=20-uABL-uSTR*0.25+e2EVA+wAC
	DualChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,e1,e2,wPD,uELM,e1ELM,e2ELM)

def UnlearnedSlicer(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	e1TGH=WSD[e1].TGH
	e1EVA=WSD[e1].EVA
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	uSTR=WSD[u].STR
	uLCK=WSD[u].LCK
	Damage1=round(uSTR*0.75+uABL*0.25-e1TGH-e1PAR)*0.5
	Damage2=round(uSTR*0.75+uABL*0.25-e2TGH-e2PAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qENE=8
	nENE=12
	hENE=16
	qHIT1=8-uABL-uSTR*0.25+e1EVA+wAC
	nHIT1=12-uABL-uSTR*0.25+e1EVA+wAC
	hHIT1=16-uABL-uSTR*0.25+e1EVA+wAC
	qHIT2=8-uABL-uSTR*0.25+e2EVA+wAC
	nHIT2=12-uABL-uSTR*0.25+e2EVA+wAC
	hHIT2=16-uABL-uSTR*0.25+e2EVA+wAC
	DualChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,cBST,e,wPD)
#Pistol
def Pistol(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e1PAR=WSD[e1].PAR
	e1TGH=WSD[e1].TGH
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1EVA=WSD[e1].EVA
	e2PAR=WSD[e2].PAR
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	uSKL=WSD[u].SKL
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	e1ELM=WSD[e1].Element
	e2ELM=WSD[e2].Element
	Damage1=round(uSKL*0.65+uABL*0.35-e1TGH-e1PAR)
	Damage2=round(uSKL*0.65+uABL*0.35-e2TGH-e2PAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT1=15-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	qHIT2=15-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	qENE=8
	nHIT1=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nHIT2=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nENE=12
	hHIT1=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hHIT2=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hENE=16
	DualChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,e1,e2,wPD,uELM,e1ELM,e2ELM)

def UnlearnedPistol(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e1PAR=WSD[e1].PAR
	e1TGH=WSD[e1].TGH
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1EVA=WSD[e1].EVA
	e2PAR=WSD[e2].PAR
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	uSKL=WSD[u].SKL
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	Damage1=round(uSKL*0.65+uABL*0.35-e1TGH-e1PAR)*0.5
	Damage2=round(uSKL*0.65+uABL*0.35-e2TGH-e2PAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT1=15-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	qHIT2=15-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	qENE=8
	nHIT1=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nHIT2=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nENE=12
	hHIT1=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hHIT2=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hENE=16
	DualChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,cBST,e,wPD)
#Pistols: Pistol Preserver. ENE Cost -50%.
def PistolPreserver(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e1PAR=WSD[e1].PAR
	e1TGH=WSD[e1].TGH
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1EVA=WSD[e1].EVA
	e2PAR=WSD[e2].PAR
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	uSKL=WSD[u].SKL
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	Damage1=round(uSKL*0.65+uABL*0.35-e1TGH-e1PAR)
	Damage2=round(uSKL*0.65+uABL*0.35-e2TGH-e2PAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT1=15-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	qHIT2=15-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	qENE=4
	nHIT1=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nHIT2=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nENE=6
	hHIT1=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hHIT2=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hENE=8
	DualChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,cBST,e,wPD)
#Pistols: Pistol Packer. Damage +25%
def PistolPacker(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e1PAR=WSD[e1].PAR
	e1TGH=WSD[e1].TGH
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	e1EVA=WSD[e1].EVA
	e2PAR=WSD[e2].PAR
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	uSKL=WSD[u].SKL
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	Damage1=round((uSKL*0.65+uABL*0.35-e1TGH-e1PAR))*1.25
	Damage2=round((uSKL*0.65+uABL*0.35-e2TGH-e2PAR))*1.25
	CritChance=(100-uLCK*0.5-cBST)
	qHIT1=15-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	qHIT2=15-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	qENE=8
	nHIT1=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nHIT2=30-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nENE=12
	hHIT1=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hHIT2=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hENE=16
	DualChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT1,qHIT2,nHIT1,nHIT2,hHIT1,hHIT2,cBST,e,wPD)
#Mechgun
def Mechgun(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy is: ")
	e2=e1
	e3=e1
	e1ELM=WSD[e1].Element
	e2ELM=WSD[e2].Element
	e3ELM=WSD[e3].Element
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage1=round(((uSKL+uABL*0.25-ePAR)-eTGH)*0.3)
	Damage2=round(((uSKL+uABL*0.25-ePAR)-eTGH)*0.5)
	Damage3=round(((uSKL+uABL*0.25-ePAR)-eTGH)*0.7)
	CritChance=(100-uLCK*0.5-cBST)
	q1HIT=20-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	q2HIT=20-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	q3HIT=20-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	qENE=3
	n1HIT=40-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	n2HIT=40-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	n3HIT=40-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	nENE=6
	h1HIT=60-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	h2HIT=60-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	h3HIT=60-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	hENE=9
	TripleChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,cBST,e,wMD,uELM,e1ELM,e2ELM,e3ELM)

def UnlearnedMechgun(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy is: ")
	e2=e1
	e3=e1
	e1ELM=WSD[e1].Element
	e2ELM=WSD[e2].Element
	e3ELM=WSD[e3].Element
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage1=round(((uSKL+uABL*0.25-ePAR)-eTGH)*0.3)*0.5
	Damage2=round(((uSKL+uABL*0.25-ePAR)-eTGH)*0.5)*0.5
	Damage3=round(((uSKL+uABL*0.25-ePAR)-eTGH)*0.7)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	q1HIT=20-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	q2HIT=20-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	q3HIT=20-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	qENE=3
	n1HIT=40-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	n2HIT=40-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	n3HIT=40-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	nENE=6
	h1HIT=60-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	h2HIT=60-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	h3HIT=60-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	hENE=9
	TripleChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,cBST,e,wMD,uELM,e1ELM,e2ELM,e3ELM)
#Mechguns: Mechgun Maniac. Damage Reduction -30%.
def MechgunManiac(User,Weapon,Element):
	u=User
	uSTR=WSD[u].STR
	uELM=Element
	e1=input("Enemy is: ")
	e2=e1
	e3=e1
	e1ELM=WSD[e1].Element
	e2ELM=WSD[e2].Element
	e3ELM=WSD[e3].Element
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage1=round(((uSKL+uABL*0.25-e1PAR)-e1TGH)*0.6)
	Damage2=round(((uSKL+uABL*0.25-e2PAR)-e2TGH)*0.8)
	Damage3=round((uSKL+uABL*0.25-e3PAR)-e3TGH)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT1=20-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	qHIT2=20-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	qHIT3=20-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	qENE=3
	nHIT1=70-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	nHIT2=70-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	nHIT3=70-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	nENE=6
	hHIT1=60-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	hHIT2=60-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	hHIT3=60-uABL*0.75-uSKL*0.25-uLCK+e3EVA-wAC
	hENE=9
	TripleChoiceP(User,qENE,nENE,hENE,CritChance,Damage1,Damage2,Damage3,qHIT1,qHIT2,qHIT3,nHIT1,nHIT2,nHIT3,hHIT1,hHIT2,hHIT3,e1,e2,e3,wMD,uELM,e1ELM,e2ELM,e3ELM)
#Rifle
def Rifle(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage=round(uSKL+uABL*0.5-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-50-uSKL*0.5-uABL*0.5+eEVA-wAC
	qENE=15
	nHIT=0-25-uSKL*0.5-uABL*0.5+eEVA-wAC
	nENE=30
	hHIT=0-uSKL*0.5-uABL*0.5+eEVA-wAC
	hENE=45
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)

def UnlearnedRifle(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage=round(uSKL+uABL*0.5-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-50-uSKL*0.5-uABL*0.5+eEVA-wAC
	qENE=15
	nHIT=0-25-uSKL*0.5-uABL*0.5+eEVA-wAC
	nENE=30
	hHIT=0-uSKL*0.5-uABL*0.5+eEVA-wAC
	hENE=45
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Rifles: Rifle Gripper. Damage +25%
def RifleGripper(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage=round((uSKL+uABL*0.5-eTGH-ePAR))*1.25
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-50-uSKL*0.5-uABL*0.5+eEVA-wAC
	qENE=15
	nHIT=0-25-uSKL*0.5-uABL*0.5+eEVA-wAC
	nENE=30
	hHIT=0-uSKL*0.5-uABL*0.5+eEVA-wAC
	hENE=45
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Rifles: Scoped Sightline. Accuracy +30%.
def ScopedRifle(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage=round(uSKL+uABL*0.5-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-80-uSKL*0.5-uABL*0.5+eEVA-wAC
	qENE=15
	nHIT=0-55-uSKL*0.5-uABL*0.5+eEVA-wAC
	nENE=30
	hHIT=0-30-uSKL*0.5-uABL*0.5+eEVA-wAC
	hENE=45
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)
#Rifles: Scoped Rifle Gripper. Damage+25%, Accuracy+30%.
def ScopedRifleGripper(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	Damage=round((uSKL+uABL*0.5-eTGH-ePAR))*1.25
	CritChance=(100-uLCK*0.5-cBST)
	qHIT=0-80-uSKL*0.5-uABL*0.5+eEVA-wAC
	qENE=15
	nHIT=0-55-uSKL*0.5-uABL*0.5+eEVA-wAC
	nENE=30
	hHIT=0-30-uSKL*0.5-uABL*0.5+eEVA-wAC
	hENE=45
	SingleChoiceP(User,qENE,nENE,hENE,CritChance,Damage,qHIT,nHIT,hHIT,e,wPD,uELM,eELM)