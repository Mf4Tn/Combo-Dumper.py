import requests
from colorama import Fore
import os
bnr = "Tool By MF4 @FFQ_Q"
print(Fore.GREEN+"Tool By MF4 @FFQ_Q\n"+Fore.RESET)
print(Fore.YELLOW +"[1] Combo 5k\n[2] Combo 25k\n[3] Combo 100k \n[4] Combo Infini\n[99] Exit\n "+Fore.RESET)
mf = int(input(Fore.GREEN+ "root@mf4:~$ "))
def k():
	os.system("clear")
	print(Fore.GREEN + bnr+"\n\nDumping...\n")
	for i in range(16):
		r = requests.get("https://combolist.org/generate")
		mf41 = r.text.split("<textarea id=combolist spellcheck=false>")[1]
		mf42 = mf41.split("</textarea>")[0]
		with open("combo 5k.txt","a")as mfa:
			mfa.write(mf42+"\n")
	print(Fore.BLUE+"Done Dumped Combo 5k And Saved In [Combo 5k.txt]\n"+Fore.RESET)
	input("Press Enter To Exit ...")
def vin():
	os.system("clear")
	print(Fore.GREEN + bnr+"\n\nDumping...\n")
	for i in range(83):
		r = requests.get("https://combolist.org/generate")
		mf44 = r.text.split("<textarea id=combolist spellcheck=false>")[1]
		mf45 = mf44.split("</textarea>")[0]
		with open("combo 25k.txt","a")as mfa:
			mfa.write(mf45+"\n")
	print(Fore.BLUE+"Done Dumped Combo 25k And Saved In [Combo 25k.txt]\n"+Fore.RESET)
	input("Press Enter To Exit ...")
def cent():
	os.system("clear")
	print(Fore.GREEN + bnr+"\n\nDumping...\n")
	for i in range(333):
		r = requests.get("https://combolist.org/generate")
		mf49 = r.text.split("<textarea id=combolist spellcheck=false>")[1]
		mf4b = mf49.split("</textarea>")[0]
		with open("combo 100k.txt","a")as mfa:
			mfa.write(mf4b+"\n")
	print(Fore.BLUE+"Done Dumped Combo 100k And Saved In [Combo 100k.txt]\n"+Fore.RESET)
	input("Press Enter To Exit ...")
def infini():
	os.system("clear")
	print(Fore.GREEN + bnr+"\n\nDumping...\n\n[!] Dumped Combo Saved Auto In [Combo infini.txt]\n\n")
	while True:
		try:
			r = requests.get("https://combolist.org/generate")
			mf4h = r.text.split("<textarea id=combolist spellcheck=false>")[1]
			mf4k = mf4h.split("</textarea>")[0]
			pass
		except:
			print(Fore.RED + "Tool Cannot Start Work !")
		with open("combo infini.txt","a")as mfa:
			mfa.write(mf4k+"\n")
	input("Press Enter To Exit ...")
if mf == 1:
	k()
elif mf ==2:
	vin()
elif mf == 3:
	cent()
elif mf == 4:
	infini()
elif mf == 99:
	print(Fore.YELLOW + "\nExiting ... ")
	exit()

	
