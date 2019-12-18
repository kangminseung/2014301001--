from matplotlib import pyplot as plt

f = open('C:/Users/Administrator/Desktop/오랑우탄/final_project/Result/accession_rate.csv', 'r', encoding='cp949')
f2 = open('C:/Users/Administrator/Desktop/오랑우탄/final_project/Result/result.csv', 'r', encoding='cp949')

x = f.readline().split(',')
y = f.readline().split(',')
z = f2.readline().split(',')

for i in range(len(y)):
    y[i] = float(y[i])
    z[i] = float(z[i])

del z[len(z)-1]


plt.title('result')
plt.subplot(1, 2, 1)
plt.ylim(60, 61)
plt.bar(x, y, width=0.3, color='blue', label='accesion rate')
plt.legend(loc='upper right')

plt.subplot(1, 2, 2)
plt.ylim(10, 50)
plt.bar(x, z, width=0.3, color='red', label='total of counting')
plt.legend(loc='upper right')

plt.show()
