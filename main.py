import matplotlib.pyplot as plt

# Melakukan inisialisasi list untuk titik-titik yang akan digambar
titikX = []
titikY = []
titikP = []
minX = []
minY = []

# Melakukan Input jari-jari
r = int(input("Masukkan jari-jari lingkaran: "))

# Menentukan nilai awal di setiap titik lingkaran
titikX.append(0)
titikY.append(r)
titikP.append(1-r)

i = 0

while titikX[i] < titikY[i]:
    #Rumus Bresenham
    # Jika titikP[i] kurang dari 0
    if titikP[i] < 0:
        titikY.append(titikY[i] )
        titikX.append(titikX[i] + 1)
        titikP.append(titikP[i] + 2 * titikX[i+1] + 1)
    # Lainnya
    # Atau Jika titikP[i] lebih dari 0
    else:
        titikX.append(titikX[i] + 1)
        titikY.append(titikY[i] - 1)
        titikP.append(titikP[i] + ((2 * titikX[i+1]+1) - (2*titikY[i+1])))
    i += 1 # Melakukan perulangan iterasi

# Membalikan nilai titikX dan titikY
reversed_titikX = list(reversed(titikX))
reversed_titikY = list(reversed(titikY))

# Memasukan nilai yang telah dibalikan ke list
titikX.extend(reversed_titikY)
titikY.extend(reversed_titikX)

# Memasukan nilai titikX dan titikY ke list minX dan minY
minX.extend([-val for val in titikX])  # Menciptakan versi yang terbalik dari minX di titikX
minY.extend([-val for val in titikY]) # Menciptakan versi yang terbalik dari minY di titikY

# Meng Print titik-titik yang akan digambar
print("Titik X :", titikX)
print("Titik Y :", titikY)
print("Titik P :", titikP)
print("minX :", minX)
print("minY :", minY)

# Membuat figure dengan lebar 16 dan tinggi 9
plt.figure(figsize=(16, 8))

# Grafik dengan 2 baris, 2 kolom dan posisi 1 ke kiri atas 
# Dengan menggunakan grid 
plt.subplot(2,2,1)
plt.plot(titikX , titikY , label='X dan Y' , color='cyan')
plt.scatter(titikX, titikY, color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham Algorithm X dan Y')
plt.legend()
plt.grid(True)# Mengaktifkan grid

# Grafik dengan 2 baris, 2 kolom dan posisi 2 ke kanan atas 
# Dengan menggunakan grid 
plt.subplot(2,2,2)
plt.plot(minX , titikY , label='-X dan Y' , color='pink')
plt.scatter(minX, titikY, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham Algorithm -X dan Y')
plt.legend()
plt.grid(True)# Mengaktifkan grid

# Grafik dengan 2 baris, 2 kolom dan posisi 3 ke kiri bawah 
# Dengan menggunakan grid 
plt.subplot(2,2,3)
plt.plot(titikX , minY , label='X dan -Y' , color='purple')
plt.scatter(titikX, minY, color='gray')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham Algorithm X dan -Y')
plt.legend()
plt.grid(True)# Mengaktifkan grid

# Grafik dengan 2 baris, 2 kolom dan posisi 4 ke kiri atas 
# Dengan menggunakan grid 
plt.subplot(2,2,4)
plt.plot(minX , minY , label='-X dan -Y' , color='yellow')
plt.scatter(minX, minY, color='orange')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham Algorithm -X dan -Y')
plt.legend()
plt.grid(True)# Mengaktifkan grid

# Menampilkan grafik
plt.tight_layout()
plt.show()

# Menggabungkan titik titik X dan Y
plt.plot(titikX,titikY, label='X dan y', color='pink')
plt.plot(minX,titikY, label='-X dan y', color='cyan')
plt.plot(titikX,minY, label='X dan -y', color='purple')
plt.plot(minX,minY, label='-X dan -y', color='yellow')

# Menambah scatter untuk menggambarkan titik
plt.scatter(titikX, titikY, color='pink')
plt.scatter(minX, titikY, color='cyan')
plt.scatter(titikX, minY, color='purple')
plt.scatter(minX, minY, color='yellow')

# Menampilkan grafik dan menambah label untuk ditamplikan
plt.xlabel('X-axis')
plt.xlabel('Y-axis')
plt.title("Bresenham Algorithm")
plt.legend()
plt.grid(True)
plt.show()
