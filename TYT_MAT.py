import matplotlib.pyplot as plt

list_x = [0,1,2,3,4]
list_y = [33.75,32.75,32.0,30.75,33.25]

plt.axhline(y = 40,linewidth = 1,color = 'r',label = "Max Net")
plt.xlabel("Deneme Sayısı")
plt.ylabel("Net")
plt.legend(['Hedef'])
plt.title("TYT MAT DENEME")
plt.grid(True)
plt.plot(list_x,list_y,'ro')

plt.show()
