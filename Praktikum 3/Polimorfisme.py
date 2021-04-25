from abc import ABCMeta,abstractmethod  

# kelas abstract  

class DuaDimensi(metaclass=ABCMeta):  

	@abstractmethod  

	def luas(self):  

		pass  

# Kelas segiEmpat turunan dari kelas duaDimensi  

class SegiEmpat(DuaDimensi):  

	def __init__(self, p, l):  

		self.panjang = p  

		self.lebar = l  

# implementasi metode luas()  

	def luas(self):  

		return self.panjang * self.lebar  

# Kelas Segitiga turunan dari kelas DuaDimensi  

class Segitiga(DuaDimensi):  

	def __init__(self, a, t):  

		self.alas = a  

		self.tinggi = t  

   # implementasi metode luas()  

	def luas(self):  

		return (self.alas * self.tinggi) / 2  

# Kelas Lingkaran turunan dari kelas DuaDimensi  

class Lingkaran(DuaDimensi):  

	def __init__(self, r):  

		self.jari2 = r  

# implementasi metode luas()  

	def luas(self):  

		import math  

		return math.pi * (self.jari2 ** 2)  

# Membuat list kosong  

mylist = []  

# menambahkan objek segiEmpat ke dalam mylist  

mylist.append(SegiEmpat(10, 8))  

# menambahkan objek Segitiga ke dalam mylist  

mylist.append(Segitiga(3, 5))  

# menambahkan objek Lingkaran ke dalam mylist  

mylist.append(Lingkaran(4))  

#Cek semua elemen mylist dan memanggil metode luas dari setiap objek yang ada di dalam mylist  

for obj in mylist:  

	if not issubclass(obj.__class__, DuaDimensi):  

		raise TypeError('objek harus turunan dari DuaDimensi') 

	if isinstance(obj,SegiEmpat):  

		print('Luas Segi empat = ', end='')  

	elif isinstance(obj, Segitiga):  

		print('Luas Segitiga = ', end='')  

	else:  

		print('Luas Lingkaran = ', end='')  

	print(obj.luas()) 