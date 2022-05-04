import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

print("\n")
print("Masukkan nilai (x1, y1) dan (x2, y2)")
x0 = int(input("Input x1: ")) #Fungsi input nilai x1
y0 = int(input("Input y1: ")) #Fungsi input nilai y1
x1 = int(input("Input x2: ")) #Fungsi input nilai x2
y1 = int(input("Input y2: ")) #Fungsi input nilai y2


print("\n")
print("---------- DIKETAHUI ----------")

x = x0
y = y0

#Menghitung dX dan dY.
dx = x1 - x0
dy = y1 - y0
print("dx = ", dx)
print("dy = ", dy)

#Menghitung gradien garis (m).
m = dy/dx
print("m  = ", m)



 
if (0 <= m <= 1): #Lanjutkan program apabila (0 <= m <= 1).
    
    #Menghitung parameter (p).
    p = (2 * dy) - dx
    print("p  = ", p)
    print("\n")

    #Membuat array untuk setiap nilai X, Y, dan P.
    x_point = []
    y_point = []
    p_point = []
    x_ = []
    y_ = []
    p_ = []
    
    
    print("------------TABEL-------------\n")
    
    for x in range(10): #Membuat kolom hasil sebanyak 10 nilai.
        x_point.append(x)
        y_point.append(y)
        p_point.append(p)
        
        if(p >= 0): #Jalankan looping berikut apabila (p >= 0)
            x = x + 1
            x_.append(x)
            y = y + 1
            y_.append(y)
            p = p - (2 * (dx - dy))
            p_.append(p)
            
        else: #Jalankan looping berikut apabila (p < 0)
            x = x + 1
            x_.append(x)
            y = y
            y_.append(y)
            p = p + (2 * dy)
            p_.append(p)
        
else: #Lanjutkan program apabila (m > 1)

    #Menghitung parameter (p).
    p = (2 * dx) - dy
    print("p  = ", p)
    print("\n")

    #Membuat array untuk setiap nilai X, Y, dan P.
    x_point = []
    y_point = []
    p_point = []
    x_ = []
    y_ = []
    p_ = []
    
    for x in range(10): #Membuat kolom hasil sebanyak 10 nilai.
        x_point.append(x)
        y_point.append(y)
        p_point.append(p)
        
        if(p >= 0): #Jalankan looping berikut apabila (p >= 0)
            x = x + 1
            x_.append(x)
            y = y + 1
            y_.append(y)
            p = p + (2 * (dx - dy))
            p_.append(p)
            
        else: #Jalankan looping berikut apabila (p >= 0)
            x = x 
            x_.append(x)
            y = y + 1
            y_.append(y)
            p = p + (2 * dx)
            p_.append(p)
    

print(pd.DataFrame({"Titik X":x_point,"Titik Y":y_point,"Parameter":p_point})) #Membuat kolom untuk output tabel
plt.scatter(x_point, y_point, color='red') #Membuat titik merah pada setiap titik (x, y)
plt.plot(x_point, y_point)
plt.show() #Menampilkan output keseluruhan