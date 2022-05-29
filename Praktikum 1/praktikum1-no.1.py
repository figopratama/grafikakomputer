#===== PRAKTIKUM 1, NO.1 =====#
#===== No.1 (A) =====#
import matplotlib.pyplot as plt

x = [-5,-4,-3,-2,-1,0,1]
m = -0.5
b = 7.5

y = [b+m*x1 for x1 in x]
print("Nilai y1", y)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")


#===== No.1 (B) =====#
import matplotlib.pyplot as plt

x = [4,5,6,7,8]
m = -1.25
b = 8

y = [b+m*x1 for x1 in x]
print("Nilai y1", y)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")


#===== No.1 (C) =====#
import matplotlib.pyplot as plt

x = [2,3,4,5]
m = 0
b = 3

y = [b+m*x1 for x1 in x]
print("Nilai y1", y)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")


#===== No.1 (D) =====#
import matplotlib.pyplot as plt

x = [2,2,2]
m = 0
b = 3

y = [b+m*x1 for x1 in x]
print("Nilai y1", y)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")


#===== No.1 (E) =====#
import matplotlib.pyplot as plt

x = [6,5,4,3,2]
m = 0.75
b = -0.5

y = [b+m*x1 for x1 in x]
print("Nilai y1", y)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
