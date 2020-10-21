import random, os, sys
try:
	from colorama import init, Fore, Back
except:
	print('copy code ini: python -m pip install colorama')


class Pmanager:

	RED   = "\033[1;31m"  
	BLUE  = "\033[1;34m"
	CYAN  = "\033[1;36m"
	GREEN = "\033[0;32m"
	RESET = "\033[0;0m"
	BOLD    = "\033[;1m"
	REVERSE = "\033[;7m"

	init()


	def __init__(self):
		c ='hpqrstu345780!@#%'
		self.len  = 0
		self.char = [str(i) for i in c]
		self.file = open('encrypt.dat','a')
		self.readf = open('encrypt.dat','r')

	def coloring(self,color):
		return sys.stdout.write(color)
		pass

	def write(self,text): 
		file = open('encrypt.dat','a')
		file.write(str(text))
		file.close()

	def readfile(self):
		f = open('encrypt.dat','r')
		r = f.read().split('\n')
		self.cls()
		for i in r:
			s = i.split('|')
			self.coloring(Back.GREEN)
			print('[*]{} => {}'.format(s[0].lower(),s[1]))
		f.close()

	def pcount(self):
		file = open('encrypt.dat','r').read().split('\n')
		return file

	def get_password(self,len):
		p = []
		s = '' 
		q = str(input('pasword untuk?: '))
		for i in range(self.len):
			p.append(self.char[random.randrange(0,16)])
		s = s.join(p)
		self.write('\n{}|{}'.format(s.upper(),q.upper()))
		return s

	def submenu(self):
		self.coloring(Fore.GREEN)
		menu = input('(m) untuk kembali dan (e) untuk keluar: ')
		if menu == 'e':
			return 0
		self.coloring(Fore.RESET)

	def cls(self):
		return os.system('cmd /c "cls"')
		pass

	def get_len(self):
		try:
			self.coloring(Fore.GREEN)
			print('''
=====================
[] Membuat Pasword []
=====================
				''')
			lenght = int(input('panjang pasword: '))
			return lenght 
			self.coloring(Fore.RESET)
		except:
			print('pastikan yang dimasukkan angka')

	def mainmenu(self):
		self.cls()
		self.coloring(Fore.BLUE)
		print('''

=====================
(1)Buat pasword
(2)Lihat Pasword[{}]
(3)keluar
=====================
pilih:
			'''.format(str(len(self.pcount()))))

		self.coloring(Fore.RESET)
		self.coloring(Back.BLUE)
		menu = int(input('[User]: '))
		self.coloring(Back.RESET)

		if menu == 1:
			self.cls()
			self.len = self.get_len()
			p = self.get_password(self.len)
			print('[*]Pasword: {}'.format(p))
			submenu = self.submenu()
			if submenu == 0:
				return 0

		elif menu == 3:
			self.cls()
			return 0

		else:#2
			self.readfile()
			self.coloring(Back.RESET)
			print('=========================')
			submenu = self.submenu()
			if submenu == 0:
				return 0

	def main(self):
		while True:
			menu = self.mainmenu()
			if menu == 0:
				break



Pmanager().main()

