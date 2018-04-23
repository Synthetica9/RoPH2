from WSD import WSD
import random as ra

def Walnut(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"restored 30MHP!")
	print("---------------")
	
def CandyCane(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"restored 30ENE!")
	print("---------------")
	
def HerbalBandage(User,Target):
	u=User
	t=input("Target is: ")
	uMHP=u+"MHP"
	tMHP=t+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"used the Herbal Bandage!",t,"is healed for",WSD[tMHP]*0.3)
	print("---------------")
	
def TomatoJuice(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"drank the Tomato Juice! They regain",WSD[uENE]*0.3,"ENE!")
	print("---------------")

def FreshOrange(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"ate the Fresh Orange! They feel refreshed.")
	print(u,"recovers ",WSD[uMHP]*0.15+"MHP and",WSD[uENE]*0.15+"ENE!")
	print("---------------")
def SweetOrange(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"ate the Sweet Orange! They feel nice.")
	print(u,"recovers ",WSD[uMHP]*0.3+"MHP and",WSD[uENE]*0.3+"ENE!")
	print("---------------")
def TheFreshestOrange(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"ate The Freshest Orange! They feel exceptionally refreshed!")
	print(u+"'s MHP is now",WSD[uMHP],"and their ENE is",WSD[uENE]+"!")
	print("---------------")
def TheSweetestOrange(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"ate The Sweetest Orange! They feel exceptionally nice!")
	print(u,"recovers ",WSD[uMHP]*0.6+"MHP and",WSD[uENE]*0.6+"ENE!")
	print("---------------")

def RedApple(User):
	u=User
	uMHP=u+"MHP"
	print("---------------")
	print(u,"ate the Red Apple! They regain",WSD[uMHP]*0.15+"MHP!")
	print(u,"is cured of a negative Status Effect!")
	print("---------------")
def GreenApple(User):
	u=User
	uENE=u+"ENE"
	print("---------------")
	print(u,"ate the Green Apple! They regain",WSD[uENE]*0.15+"ENE!")
	print(u,"is cured of a negative Status Effect!")
	print("---------------")
def GoldenApple(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"ate the Golden Apple! They regain",WSD[uMHP]*0.33+"MHP and",WSD[uENE]*0.33+"ENE!")
	print(u,"is also cured of all negative Statuses!")
	print("---------------")

def HealtMHPotion(User):
	u=User
	uMHP=u+"MHP"
	print("---------------")
	print(u,"drank the Health Potion! They regain",WSD[uMHP]*0.3+"MHP!")
	print("---------------")
def EnergyPotion(User):
	u=User
	uENE=u+"ENE"
	print("---------------")
	print(u,"drank the Energy Potion! They regain",WSD[uENE]*0.3+"ENE!")
	print("---------------")
def SuperPotion(User):
	u=User
	uMHP=u+"MHP"
	uENE=u+"ENE"
	print("---------------")
	print(u,"drank the Super Potion! They regain",WSD[uMHP]*0.5+"MHP and",WSD[uENE]*0.5+"ENE!")
	print("---------------")

def ThrowingStar(User):
	u=User
	uSTR=u+"STR"
	e=input("Target is: ")
	uLCK=u+"LCK"
	uSKL=u+"SKL"
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	if ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uSKL]-WSD[uSTR]*0.25+WSD[eEVA]:
		print("---------------")
		print(u,"landed a Direct Hit!",e,"is hit for",WSD[uSTR]*1.15-WSD[eTGH]-WSD[ePAR],"damage!")
		print("---------------")
	else:
		print("---------------")
		print(u,"missed",e+"!")
		print("---------------")
def HandGrenade(User):
	u=User
	uSKL=u+"SKL"
	e=input("Target is: ")
	uLCK=u+"LCK"
	eTGH=e+"TGH"
	ePAR=e+"PAR"
	eEVA=e+"EVA"
	uABL=u+"ABL"
	if ra.randint(1,100) >= 50-WSD[uLCK]-WSD[uABL]-WSD[uSKL]*0.25+WSD[eEVA]:
		print("---------------")
		print(u,"landed a Direct Hit!",e,"is hit for",WSD[uSKL]-WSD[eTGH]-WSD[ePAR],"damage!")
		print("---------------")
	else:
		print("---------------")
		print(u,"missed",e+"!")
		print("---------------")