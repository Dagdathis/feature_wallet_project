import csv
import matplotlib. pyplot as plt

x = []
y = []

with open('data.csv','r') as sales_csv:
    plots = csv.reader(sales_csv, delimiter=';')
    for row in plots:
        x.append(row[2])        #Колонка с типом 
        y.append(row[3])        #Колонка с суммой

#соединил два списка функцией zip                        
a = zip(x,y)                            #a теперь по типу [(2, 1000), (3, 400).....]

#сортируем, взяв первый элемент каждого списка как ключ
aas = sorted(a, key=lambda tup: tup[0])     #aas = [(1, 'b'), (2, 'c'), (3, 'a')]

#извлечем
x1 = [a[0] for a in aas]
y1 = [a[1] for a in aas]

# перевод из string в int
x2 = []  
for item in x1:
    x2.append(int(item))
print(x2)

# перевод из string в float
y2 = []
for item in y1: 
    y2.append(float(item))
print(y2)

#Цикл для суммирования трат по типу
#ras =[]                             
#for i in range(len(x2)):
#    n=0
#    suma=0
#    for j in range(i + 1, len(x2)):
#        if x2[i] != x2[j]:
#            n += y2[i]
#            suma+=n
#            ras.append(suma) # тестовые значения = [3700, 1700, 40, 9000] 
#            n=0
#            break
#        else:   
#            n += y2[j]

#print(ras)      #проверка массива
ras =[3700, 1700, 40, 9000]
#Создание диаграмы
labels = ['Type 2', 'Type 3', 'Type 4', 'Type 5'] 

fig, ax = plt.subplots() 
ax.pie(ras, labels = labels) 
ax.set_title("amount of expenses") 
plt.show()