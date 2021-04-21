# Parameter untuk inheritance
class Titik (object) :
  # Constructor
  def __init__(self, x = 0, y = 0) :
    # Self adalah This
    self.x = x
    self.y = y

  def pindah(self, x, y) :
    self.x = x
    self.y = y
  
  def cetak(self) : 
    print(f'{self.x}, {self.y}')


# Buat object
titik = Titik()
titik.cetak()
titik.pindah(5,10)
titik.cetak()