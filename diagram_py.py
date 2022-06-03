import csv
import matplotlib. pyplot as plt

x = []
y = []

with open('data.csv','r') as sales_csv:
    plots = csv.reader(sales_csv, delimiter=';')
    for row in plots:
        x.append(row[1])        #Колонка с типом 
        y.append(row[2])        #Колонка с суммой

                        #соединим два списка специальной функцией zip
a = zip(x,y)            #a теперь по типу [(2, 1000), (3, 400).....]

                                        #отсортируем, взяв первый элемент каждого списка как ключ
aas = sorted(a, key=lambda tup: tup[0])     #aas = [(1, 'b'), (2, 'c'), (3, 'a')]
                        #и последний шаг - извлечем
x1 = [a[0] for a in aas]
y1 = [a[1] for a in aas]

                        #Цикл для суммирования трат по типу

#ras =[]                #Пробовал складывать сумму по коду,
#i=0                    #Выдаёт ошибку TypeError: unsupported operand type(s) for +=: 'int' and 'str'  
#j=0
#for i on x1:                       
#    n=0
#    suma=0
#    for j on x1: 
#        if i==j:
#            n += y1[i]            
#        else:
#            n += y1[i]
#            suma=n
#            ras.append(suma) # = [15, 25, 25, 30, 5] 
#            n=0
ras = [15, 25, 25, 30, 5]    #Диаграмма работает
print(ras)

labels = ['Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5'] 

fig, ax = plt.subplots() 
ax.pie(ras, labels = labels) 
ax.set_title("amount of expenses") 
plt.show()