class PersegiPanjang:
    # Variable biasa
    counter = 0

    # Constructor
    def __init__(self, p, l):
        # Instance/object variable
        self.panjang = p
        self.lebar = l

    # Encapsulation
    # Setter
    def ubahPanjang(self, p):
        self.panjang = p

    def ubahLebar(self, l):
        self.lebar = l

    # -- End Encapsulation

    def hitungLuas(self):
        return self.panjang * self.lebar

    def hitungKeliling(self):
        return 2 * (self.panjang + self.lebar)

    def cetakLuas(self):
        print(f'Luas persegi Panjang\t: {self.hitungLuas()} ')

    def cetakKeliling(self):
        print(f'Keliling persegi Panjang\t: {self.hitungKeliling()} ')


objekPP1 = PersegiPanjang(10, 8)

objekPP2 = PersegiPanjang(9, 8)

objekPP3 = PersegiPanjang(8, 8)

objekPP1.cetakLuas()

objekPP1.cetakKeliling()

objekPP1.counter = 10