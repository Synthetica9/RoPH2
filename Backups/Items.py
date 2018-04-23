from WSD2 import WSD
import random as ra

def Walnut(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"restored 30HP!")
	print("---------------")
def CandyCane(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"restored 30ENE!")
	print("---------------")
	
def HerbalBandage(User):
	u=User
	t=input("Target is: ")
	tHP=WSD[t].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"used the Herbal Bandage!",t,"is healed for",tHP*0.3)
	print("---------------")

def HotCocoa(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"drank the Hot Cocoa! They regain",uENE*0.25,"ENE and,",uHP*0.25+"HP!")
	print("---------------")
def TomatoJuice(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"drank the Tomato Juice! They regain",uENE*0.3,"ENE!")
	print("---------------")
def OrangeJuice(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"drank the Orange Juice! They regain",uENE*0.3,"ENE and,",uHP*0.3+"HP!")
	print("---------------")

def FreshOrange(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"ate the Fresh Orange! They feel refreshed.")
	print(u,"recovers ",uHP*0.15+"HP and",uENE*0.15+"ENE!")
	print("---------------")
def SweetOrange(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"ate the Sweet Orange! They feel nice.")
	print(u,"recovers ",uHP*0.3+"HP and",uENE*0.3+"ENE!")
	print("---------------")
def TheFreshestOrange(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"ate The Freshest Orange! They feel exceptionally refreshed!")
	print(u+"'s HP is now",uHP,"and their ENE is",uENE+"!")
	print("---------------")
def TheSweetestOrange(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"ate The Sweetest Orange! They feel exceptionally nice!")
	print(u,"recovers ",uHP*0.6+"HP and",uENE*0.6+"ENE!")
	print("---------------")

def RedApple(User):
	u=User
	uHP=WSD[u].HP
	print("---------------")
	print(u,"ate the Red Apple! They regain",uHP*0.15+"HP!")
	print(u,"is cured of a negative Status Effect!")
	print("---------------")
def GreenApple(User):
	u=User
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"ate the Green Apple! They regain",uENE*0.15+"ENE!")
	print(u,"is cured of a negative Status Effect!")
	print("---------------")
def GoldenApple(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"ate the Golden Apple! They regain",uHP*0.33+"HP and",uENE*0.33+"ENE!")
	print(u,"is also cured of all negative Statuses!")
	print("---------------")

def HealtHPotion(User):
	u=User
	uHP=WSD[u].HP
	print("---------------")
	print(u,"drank the Health Potion! They regain",uHP*0.3+"HP!")
	print("---------------")
def EnergyPotion(User):
	u=User
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"drank the Energy Potion! They regain",uENE*0.3+"ENE!")
	print("---------------")
def SuperPotion(User):
	u=User
	uHP=WSD[u].HP
	uENE=WSD[u].ENE
	print("---------------")
	print(u,"drank the Super Potion! They regain",uHP*0.5+"HP and",uENE*0.5+"ENE!")
	print("---------------")

def ThrowingStar(User):
	u=User
	uSTR=WSD[u].STR
	e=input("Target is: ")
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	if ra.randint(1,100) >= 10-uLCK-uSKL-uSTR*0.25+eEVA:
		print("---------------")
		print(u,"landed a Direct Hit!",e,"is hit for",uSTR*1.15-eTGH-ePAR*1.15,"damage!")
		print("---------------")
	else:
		print("---------------")
		print(u,"missed",e+"!")
		print("---------------")
def HandGrenade(User):
	u=User
	uSKL=WSD[u].SKL
	e=input("Target is: ")
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uABL=WSD[u].ABL
	if ra.randint(1,100) >= 50-uLCK-uSKL-uABL*0.25+eEVA:
		print("---------------")
		print(u,"landed a Direct Hit!",e,"is hit for",uABL*1.25-eTGH*0.75-ePAR,"damage!")
		print("---------------")
	elif ra.randint(1,100) >= 25-uLCK-uSKL-uABL*0.25+eEVA*0.5:
		print("---------------")
		print(u,"landed a Glancing Hit!",e,"is hit for",(uABL*1.25-eTGH*0.75-ePAR)*0.5,"damage!")
		print("---------------")
	else:
		print("---------------")
		print(u,"missed",e+"!")
		print("---------------")