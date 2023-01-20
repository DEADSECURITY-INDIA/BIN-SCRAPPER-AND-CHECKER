import random,os,sys,requests
import sys
from time import sleep
from colorama import init, Fore

#COLORS
init()
n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
colors = [lg, r, w, cy, ye, gr]
Ba = 0
G = '0123456789'
TY = '123456789'

print(gr+'\nWELCOME TO DEADSECURITY INDIA (@deadsec0_0darky)\n')
print(r+'-'*40)
print(cy+' CHOOSE AN OPTION ')
print(r+'-'*40)
bw = input(ye+'(1) GET BIN   \n(2) GET BIN INFORMATION \n(3) GENERATE     \n\nCHOOSE => ')
print(r+'-'*40)
if bw == '1':
	os.system('clear')
	print(gr+'WELCOME TO DEADSECURITY INDIA (@deadsec0_0darky)')
	print(r+'-'*40)
	token = ('YOUR BOT TOKEN HERE')
	ID = ('CHAT ID')
    
	while True:
		ml = '3'+str(''.join((random.choice(G) for i in range(5))))
		xc = '4'+str(''.join((random.choice(G) for i in range(5))))
		za = [ml,xc]
		v = (random.choice(za))
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		response = reg.text
		if '"country"' in response:
		  	f = requests.get(api)
		  	res = f.json()
		  	z = res['country']['emoji']
		  	m = res['scheme']
		  	k = res['country']['name']
		  	g = res['country']['currency']
		  	u = v
		  	p = k +' '+z
		  	tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=
🇮🇳DEADSECURITY INDIA🇮🇳
---------------------------------
💳BIN =>  {u}
🌐COUNTRY =>  {p}
📤CARD TYPE => {m}
💸CURRECY => {g}
---------------------------------
 🥰DEV : @deadsec0_0darky''')

		  	i = requests.post(tlg)
		  	print(cy+'Available =>  '+v)
		  	print(k+' '+z)
		  	print(g)
		  	print(m)
		else:
			print(r+'Not Available =>  '+v)
if bw == '2':
	token = ('YOUR BOT TOKEN HERE')
	ID = ('CHAT ID')
	while True:
		v = input(ye+'ENTER YOUR BIN =>  ')
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		res = reg.json()
		z = res['country']['emoji']
		m = res['scheme']
		k = res['country']['name']
		g = res['country']['currency']
		print(cy+k+z)
		print(cy+m)
		print(cy+g)
		u = v
		p = k +' '+z
		print('Done Sent to  https://t.me/DARKY_BINS_SCRAPPER ! ')
		print(r+'-'*40)
		tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=
🇮🇳DEADSECURITY INDIA🇮🇳
---------------------------------
💳BIN =>  {u}
🌐COUNTRY =>  {p}
📤CARD TYPE => {m}
💸CURRENCY => {g}
---------------------------------
 🥰DEV : @deadsec0_0darky''')
 
		i = requests.post(tlg)
if bw == '3':
	os.system('clear')
	print(gr+'    WELCOME TO DEADSECURITY INDIA (@deadsec0_0darky) \n')
  
	print(ye+'  CHOOSE AN OPTION      ')
	print('')
	
	os.system(f'rm -rf deadsecurity.txt')
	B = input(cy+'(1) RANDOM  \n(2) GENERATE FROM BIN   \nCHOOSE => ')	
def bae():
	print(r+'-'*40)
	if B == '2':
		ba = input('\033[1;31m'+'YOUR BIN 5 o尺 6 ? => ')
		if ba == '6':
			bi = input(ye+'ENTER YOUR BIN  => ')
		if ba == '5':
			bi = input(ye+'ENTER YOUR BIN  => ')
	G = '0123456789'
	Z = ['2023','2024','2025','2026','2027','2028']
	Ba = 0
	while Ba < 20:
	   		if B == '1':
    				v = str(''.join((random.choice(G) for i in range(16))))
    				b = str(''.join((random.choice(TY) for i in range(2))))
    				a = str(''.join((random.choice(G) for i in range(3))))
    				p = str(random.choice(Z))
    				h = v+'|'+'0'+b+'|'+p+'|'+a
    				print(cy+'CARD ==> '+'\033[2;36m'+h)
    				g = open('deadsecurity.txt', 'a')
    				g.write(h+ '\n')
    				tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={h} + \n''')
    				i = requests.post(tlg)
    				Ba = Ba + 1
	   		if B == '2':
	   			if ba == '5':
    					v = str(''.join((random.choice(G) for i in range(11))))
    					b = str(''.join((random.choice(TY) for i in range(2))))
    					a = str(''.join((random.choice(G) for i in range(3))))
    					p = str(random.choice(Z))
    					h = bi+v+'|'+'0'+b+'|'+p+'|'+a
    					print(X+'VISA ==> '+'\033[2;36m'+h)
    					g = open('deadsecurity.txt', 'a')
    					g.write(h+ '\n')
    					Ba = Ba + 1
    					tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={h} + \n''')
    					i = requests.post(tlg)
	   			if ba == '6':
	   				v = str(''.join((random.choice(G) for i in range(10))))
	   				b = str(''.join((random.choice(TY) for i in range(1))))
	   				a = str(''.join((random.choice(G) for i in range(3))))
	   				p = str(random.choice(Z))
	   				h = bi+v+'|'+'0'+b+'|'+p+'|'+a
	   				print(X+'CARD ==> '+'\033[2;36m'+h)
	   				g = open('deadsecurity.txt', 'a')
	   				g.write(h+ '\n')
	   				Ba = Ba + 1
	   				tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={h} + \n''')
           
	   				i = requests.post(tlg)
	   		

bae()  				
