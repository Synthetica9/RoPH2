import Bosses
import Allies
import Players
import Enemies
import importlib
import EnergyBar
from WSD2 import WSD

running = 1
while running == 1:
	choice=input("Select a Unit Type!\n [P]layers!\n [A]llies!\n [E]nemies!\n [T]urn Actions!\n")
	if choice == "P" or choice == "p":
		choice=input("Select a Unit!\n [GM] Brad!\n [KM] Jango!\n [ST] Saint Clips!\n ")
		if choice == "GM" or choice == "Gm" or choice == "gm":
			Players.Brad("Brad")
		elif choice == "KM" or choice == "Km" or choice == "km":
			Players.Jango("Jango")
		elif choice == "ST" or choice == "st":
			Players.StClips("StClips")
	elif choice == "A" or choice == "a":
		choice=input("Select an Ally!\n [R]eintaur!\n [S]ix!\n [Z]ombie Renfield!\n ")
		if choice == "R" or choice == "r":
			Allies.Reintaur("Reintaur")
		elif choice == "S" or choice == "s":
			Allies.Six("Six")
		elif choice == "Z" or choice == "z":
			Allies.Renfield("Renfield")
	elif choice == "E" or choice == "e":
		choice=input("Select your Bandit!\n [L]ieutenant Higgins!\n [C]orporal Marshal!\n [S]oldier Todd!\n [H]ooded Freak!\n ")
		if choice == "L" or choice == "l":
			Allies.Higgins("Higgins")
	elif choice == "T" or choice == "t":
		choice=input("Select an Action!\n [E]nergy Regen!\n ")
		if choice == "E" or choice == "e":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\EnergyBar.py','a+') as f:
				importlib.reload(EnergyBar)
				print("JangoENE="+str(min(WSD["Jango"].ENE,EnergyBar.JangoENE+round(WSD["Jango"].ENE*0.1))),file=f)
				print("ReintaurENE="+str(min(WSD["Reintaur"].ENE,EnergyBar.ReintaurENE+round(WSD["Reintaur"].ENE*0.1))),file=f)
				print("SixENE="+str(min(WSD["Six"].ENE,EnergyBar.SixENE+round(WSD["Six"].ENE*0.1))),file=f)
				print("HigginsENE="+str(min(WSD["Higgins"].ENE,EnergyBar.HigginsENE+round(WSD["Higgins"].ENE*0.1))),file=f)
				print("BradENE="+str(min(WSD["Brad"].ENE,EnergyBar.BradENE+round(WSD["Brad"].ENE*0.1))),file=f)
				print("RenfieldENE="+str(min(WSD["Renfield"].ENE,EnergyBar.RenfieldENE+round(WSD["Renfield"].ENE*0.1))),file=f)