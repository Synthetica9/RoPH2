from WSD2 import WSD
import random as ra
import importlib
import HealthBar
import EnergyBar
def StrawberryCandy(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Heal=HPMAX*0.07
	Restore=ENEMAX*0.07
	print("---------------")
	print(u,"restored",round(HPMAX*0.07),"HP!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	print(u,"restored",round(ENEMAX*0.07),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
		
	print("---------------")

def SoothingSalve(User):
	u=User
	print("---------------")
	print(u,"is cured of a negative Status Effect!")
	print("---------------")

def PearlOintment(User):
	Target=input("Who are we using this on?\n ")
	print("---------------")
	print(Target,"had their TGH and RES boosted by 15 for this Turn!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\WSD2.py','a+') as f:
		print(setattr(WSD[Target],str(WSD[Target].StatPlus[8]),+15), file=f)
		print(setattr(WSD[Target],str(WSD[Target].StatPlus[9]),+15), file=f)
	print("---------------")

def Walnut(User):
	u=User
	uHP=u+"HP"
	HPMAX=WSD[u].HP
	Heal=30
	print("---------------")
	print(u,"restored 30HP!")
	print("---------------")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
def CandyCane(User):
	u=User
	uENE=u+"ENE"
	ENEMAX=WSD[u].ENE
	Restore=30
	print("---------------")
	print(u,"restored 30ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
	
def HerbalBandage(User):
	u=User
	t=input("Target is: ")
	HPMAX=WSD[t].HP
	tHP=t+"HP"
	Heal=HPMAX*0.3
	print("---------------")
	print(u,"used the Herbal Bandage!",t,"is healed for",HPMAX*0.3)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(t+"HP="+str(min(HPMAX,getattr(HealthBar,tHP)+round(Heal))),file=f)
	print("---------------")

def HotCocoa(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Heal=HPMAX*0.25
	Restore=ENEMAX*0.25
	print("---------------")
	print(u,"drank the Hot Cocoa! They regain",round(ENEMAX*0.25),"ENE and",round(HPMAX*0.25),"HP!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
def TomatoJuice(User):
	u=User
	uENE=u+"ENE"
	ENEMAX=int(WSD[u].ENE)
	Restore=ENEMAX*0.3
	print("---------------")
	print(u,"drank the Tomato Juice! They regain",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
def OrangeJuice(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Restore=ENEMAX*0.4
	Heal=HPMAX*0.4
	print("---------------")
	print(u,"drank the Orange Juice! They regain",round(Restore),"ENE and",round(Heal),"HP!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")

def FreshOrange(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Heal=HPMAX*0.15
	Restore=ENEMAX*0.15
	print("---------------")
	print(u,"ate the Fresh Orange! They feel refreshed.")
	print(u,"recovers ",round(Heal),"HP and",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
def SweetOrange(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Heal=HPMAX*0.3
	Restore=ENEMAX*0.3
	print("---------------")
	print(u,"ate the Sweet Orange! They feel nice.")
	print(u,"recovers ",round(Heal),"HP and",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
def TheFreshestOrange(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	print("---------------")
	print(u,"ate The Freshest Orange! They feel exceptionally refreshed!")
	print(u,"'s HP is now",HPMAX,"and their ENE is",ENEMAX,"from consuming The Freshest Orange!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(HPMAX),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(ENEMAX),file=f)
	print("---------------")
def TheSweetestOrange(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	uHP=u+"HP"
	Heal=HPMAX*0.6
	Restore=ENEMAX*0.6
	print("---------------")
	print(u,"ate The Sweetest Orange! They feel exceptionally nice!")
	print(u,"recovers",round(Heal),"HP and",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")

def RedApple(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	uMAX=WSD[u].HP
	Heal=round(uMAX*0.15)
	uHP=u+"HP"
	print("---------------")
	print(u,"ate the Red Apple! They regain",Heal,"HP!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	print(u,"is cured of a negative Status Effect!")
	print("---------------")
def GreenApple(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	ENEMAX=WSD[u].ENE
	Restore=ENEMAX*0.15
	print("---------------")
	print(u,"ate the Green Apple! They regain",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print(u,"is cured of a negative Status Effect!")
	print("---------------")
def GoldenApple(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	uMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Heal=HPMAX*0.33
	Restore=ENEMAX*0.33
	print("---------------")
	print(u,"ate the Golden Apple! They regain",round(Heal),"HP and",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print(u,"is also cured of all negative Statuses!")
	print("---------------")

def HealthPotion(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	Heal=HPMAX*0.25
	print("---------------")
	print(u,"drank the Health Potion! They regain",round(Heal),"HP!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	print("---------------")
def EnergyPotion(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	ENEMAX=WSD[u].ENE
	Restore=ENEMAX*0.25
	print("---------------")
	print(u,"drank the Energy Potion! They regain",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
def HealthPotionPlus(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	Heal=HPMAX*0.5
	print("---------------")
	print(u,"drank the Health Potion! They regain",round(Heal),"HP!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	print("---------------")
def EnergyPotionPlus(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	ENEMAX=WSD[u].ENE
	Restore=ENEMAX*0.5
	print("---------------")
	print(u,"drank the Energy Potion! They regain",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
def SuperPotion(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Heal=HPMAX*0.25
	Restore=ENEMAX*0.25
	print("---------------")
	print(u,"drank the Super Potion! They regain",round(Heal),"HP and",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")
def SuperPotionPlus(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	HPMAX=WSD[u].HP
	ENEMAX=WSD[u].ENE
	Heal=HPMAX*0.5
	Restore=ENEMAX*0.5
	print("---------------")
	print(u,"drank the Super Potion! They regain",round(Heal),"HP and",round(Restore),"ENE!")
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
		importlib.reload(HealthBar)
		print(u+"HP="+str(min(HPMAX,getattr(HealthBar,uHP)+round(Heal))),file=f)
	with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\EnergyBar.py','a+') as f:
		importlib.reload(EnergyBar)
		print(u+"ENE="+str(min(ENEMAX,getattr(EnergyBar,uENE)+round(Restore))),file=f)
	print("---------------")

def ThrowingStar(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	uSTR=WSD[u].STR
	e=input("Target is: ")
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	eHP=e+"HP"
	damage=round(uSTR*1.15-eTGH-ePAR*1.15)
	if ra.randint(1,100) >= 10-uLCK-uSKL-uSTR*0.25+eEVA:
		print("---------------")
		print(u,"landed a Direct Hit!",e,"is hit for",damage,"damage!")
		with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
			importlib.reload(HealthBar)
			print(e+"HP="+str(max(0,getattr(HealthBar,eHP)-round(damage))),file=f)
		print("---------------")
	else:
		print("---------------")
		print(u,"missed",e+"!")
		print("---------------")
def HandGrenade(User):
	u=User
	uHP=u+"HP"
	uENE=u+"ENE"
	uSKL=WSD[u].SKL
	e=input("Target is: ")
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uABL=WSD[u].ABL
	eHP=e+"HP"
	damage=round(uABL*1.25-eTGH*0.75-ePAR)
	if ra.randint(1,100) >= 50-uLCK-uSKL-uABL*0.25+eEVA:
		print("---------------")
		print(u,"landed a Direct Hit!",e,"is hit for",round(damage),"damage!")
		with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
			importlib.reload(HealthBar)
			print(e+"HP="+str(max(0,getattr(HealthBar,eHP)-round(damage))),file=f)
		print("---------------")
	elif ra.randint(1,100) >= 25-uLCK-uSKL-uABL*0.25+eEVA*0.5:
		print("---------------")
		print(u,"landed a Glancing Hit!",e,"is hit for",round((damage*0.5)),"damage!")
		with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\For Testing Ideas\\HealthBar.py','a+') as f:
			importlib.reload(HealthBar)
			print(e+"HP="+str(max(0,getattr(HealthBar,eHP)-round(damage*0.5))),file=f)
		print("---------------")
	else:
		print("---------------")
		print(u,"missed",e+"!")
		print("---------------")