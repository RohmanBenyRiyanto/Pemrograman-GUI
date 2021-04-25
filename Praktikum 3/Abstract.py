from abc import ABCMeta,abstractmethod

class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass

class SegiEmpat(DuaDimensi):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    
    def luas(self):
        return self.panjang * self.lebar

class Segitiga(DuaDimensi):
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    
    def luas(self):
        return (self.alas * self.tinggi) / 2

class Lingkaran(DuaDimensi):
    def __init__(self, r):
        self.jari2 = r
    
    def luas(self):
        import math
        return math.pi * (self.jari2 ** 2)

segitiga = Segitiga(2,4)
print(segitiga.luas())
segiEmpat = SegiEmpat(5,5)
print(segiEmpat.luas())
lingkaran = Lingkaran(10)
print(lingkaran.luas())
