from random import *
s=[]
def arvud_loendis():
    """ sisestame andme, kutsume funktsioonid ja näitame vastus
    """
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=(int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:#mini=100, maxi=5 -> mini=5, maxi=100
        mini,maxi=vahetus(mini,maxi)
    generator(n,s,mini,maxi):
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort(s)
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol):
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos):
    lisamine(s,kesk):
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg):
    lisamine(s,kesk):
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    print(s)

def vahetus(a:int,b:int):
    """kui mini suurem kui maxi, siis vahetame neid omavahel
    :param int a: minimaalne arv, mis on suurem kui maxi
    :param int b: maximaalne arv, mis on väiksem kui mini
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """ lisame erinevaid arvud listisse
    :param int n: numbrite arv
    :param list loend: list numbritega
    :param int a: mini
    :param int b: maxi
    :rtype: list
    """
    for i in range (n):
        loend.append(randint(a,b))
  
        
def jagamine(loend:list,p:list,n:list,nol:list):
    """ lisame listisse ja teeme tingimused
    :param list loend: list numbritega
    :param list p: list arvudega
    :param list n: list arvudega
    :param list nol: list nulliväärtusega 
    :rtype list:
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list,n:):
    """leijame keskmine väärtus
    :param list loend: list arvudega
    :param list p: list negotiivsega ja positiivsedega arvudega
    :rtype: float
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
            kesk=round(sum/n,2)
            return kesk

def lisamine(loend:list,el:flost):
    """ lisame listise keskmine väärtus ja sorteerime
    :param list loend: list arvudega
    :param float el: keskmine väärtus
    :rtype: list
    loend(append(el))
    loend(sort())

arvud_loendis()

