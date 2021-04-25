class Aritmatika:

    @staticmethod
    def tambah(a, b):
        return a + b

    @staticmethod
    def kurang(a, b):
        return a - b

    @staticmethod
    def bagi(a, b):
        return a / b

    @staticmethod
    def bagi_int(a, b):
        return a // b

    @staticmethod
    def pangkat(a, b):
        return a ** b


print(Aritmatika.tambah(5, 5))

objekA = Aritmatika()

print(objekA.pangkat(2, 3))