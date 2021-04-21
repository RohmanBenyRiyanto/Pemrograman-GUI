# Fungsi Global
def kali (a, b) :
  c = a * b 
  return c 

z = kali (10,5)
print(z)

# Fungsi globals
def cetakBonus(daftar=[]) :
  # Fungsi Lokal
  def hitungBonus(gaji) :
    if gaji < 5000000 :
      bonus = 0.05 * gaji
    elif 5000000 <= gaji < 7500000 :
      bonus = 0.10 * gaji
    else :
      bonus = 0.15 * gaji
    return bonus
  
  for nama, gaji in daftar :
    b = hitungBonus(gaji)
    print(f'{nama}\t: {gaji}, {b} ')

data = [
  ('ucok', 4000000),
  ('budi', 6000000),
  ('wagi', 8000000),
]

cetakBonus(data)


# Fungsi Lambda

maks = lambda a, b : a if a > b else b
print(maks (25, 20))

same = lambda a : True if a == 25 else False
print(same (20))