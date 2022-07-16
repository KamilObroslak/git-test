# for i in range(5):
#     print(i)
#
# a=[1,2,3,4,5]
# for b in a:
#     print(b)
#
# for a in range(1,6):
#     print(a)
#
# x = 0
# while x < 5:
#     x = x + 1 # x += 1
#     print (x)
#
# x = 0
# while True:
#     if x==5:
#         break
#         x=x+1
#         print(x)

# ------------------------------------------------------

# zad 3

# l1 = 6
# l2 = 0
# i = 0
#
# print(l1)
#
# while i < 4:
#     l1 = l1 + 6
#     print(l1)
#     i += 1
#
# a = 0
# for i in range(5):
#     a = a + 6
#     print(a)
#
# a = [6,12,18,24,30]
# for num in a:
#     print(num)

# for a in range(1,8):
#     if a == 5:
#         print("Znalazłem 5!")
#     else:
#         print(a)

# --------------------------

# for i in range(1,4):
#     for j in 'abc':
#         print(i, j)

# ------------------------

# a=list(range(1,9))
# print(a)
# print(a[2])

# -----------------------------------------

# a = list(range(1,9))
# print("Moja lista: ", a)
# print("------------------")

# for i in a:
#     #print(a[i-1])
#     if i ==5:
#         break
#     print(i)

# ---------------------------------

# i = 4
# while i < 19:
#     print(i)
#     i += 2

# ------------------------------------

# list = ['AA', 'BBB', 'CCC', 'DDDDD']
#
# for i in list:
#     print(i)
#
# print("Lista sie skonczyła")

# for i in range(1,21):
#     if i%3 == 0:
#         print(i)

# --------------------------------

# liczba = 1
#
# print(liczba)
# while liczba < 21:
#     liczba = liczba + 5
#     print(liczba)

# liczba = 10
#
# while liczba >= 0:
#     print(liczba)
#     liczba = liczba - 1
#

# def funkcja(start, stop):
#     while start < stop:
#         print(start)
#         start = start + 1
#
# funkcja(4,9)

# def rocketstart(start, stop):
#     while start > stop:
#         print(start)
#         start = start - 1
#         if start == stop:
#             print("Rakieta startuje!!!")
#
# rocketstart(5,0)

# lista1 = ["KKKK", "GGGG", "HHHH"]
# lista2 = ["563-12", "363-AB"]
#
# for i in lista1:
#     for j in lista2:
#         print(i, j)
#     print("----------")

# ---------------------------------

# zmienna1 = input("Proszę wpisać literkę n lub c ")
#
# if zmienna1 == "n" or zmienna1 == "c":
#     print("Dziękuję!")
# else:
#     print("Błąd!")

# zmienna = 0
#
# while zmienna != "n" or zmienna != "c":
#     zmienna = input("Proszę wpisać literkę n lub c")
#     if zmienna == "n" or zmienna == "c":
#         print("Dziękuję!")
#         break
#     if zmienna != "n" or zmienna != "c":
#         print("Błąd!")

# lista = [17, 21, 18]
#
# for i in lista:
#     print(i)
#     print("kolejna zmienna")
#     print("AAA")

# lista1 = [17, 21, 18]
# lista2 = ["Adrian", "Paula"]
#
# for i in lista1:
#     print(i)
#     for j in lista2:
#         print(j)

##lista = [["CA","NV","UT"], ["NJ","NY","DE"]]

# for i in lista:
#     for j in i:
#         print(j)

# licznik = 0
#
# for i in range(5):
#     liczba = int(input("Wprowadź dowolną liczbę od 1 do 10: "))
#     if liczba == 5:
#         licznik = licznik + 1
#
# print("Użytkownik wybrał ", licznik, " razy liczbę ", 5)

# wzor = "*"
#
# for i in range(1,5):
#         print(i*wzor)
#
# lista = []
#

# -----------------------------------

# for i in range(2000,3200):
#     if i%7 == 0 and i%5 != 5:
#         lista.append(str(i))
#
# print(','.join(lista))

# ---------------------------------

# from Tools.scripts.treesync import raw_input
#
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
# x=int(input("Wpisz jakąkolwiek liczbę: " ))
# print(fact(x))

#---------------------------------------

# n = int(input())
# d = dict()
# for i in range(1+n*1):
#     d[i] = i * i
#
# print(d)

#---------------------------------------

# for i in "Polska":
#     print(i)

# wyrazy = ["raz", "dwa", "trzy"]
#
# for i in wyrazy:
#     print(i)

#------------------------------------------
#
# for i in range(4):
#     print("Witamy!")

#-----------------------------------------

#
# lista = ["Adrian", "Piotrek", "Ewa", "Bonifacy"]
#
# for i in lista:
#     print(i, len(i))

#-----------------------------------------

# 32

# lista = ["Adrian", "Piotrek", "Ewa"]
#
# for i in range(3):
#     print(i, lista[i])

# for i in range(1,11):
#     if (i%9 != 0) and (i%8 != 0) and (i%3 != 0):
#         print(i)

# for i in range(5):
#     if i != 2:
#         print(i)

#---------------------------------------------

# x = 0
#
# while x < 5:
#     x = x +1
#     print(x)

#----------------------------------------------

# a = [42,4,9,6,14,43]
#
# # while a:
# #     print(a[0])
# #     del a[0]
#
# for i in a:
#     print(i)

# c = 1
#
# while c <= 18:
#     print(c)
#     c += 3

#---------------------------------------

#c = 5

# while c >= 0:
#     print(c)
#     c -= 1

#------------------------------------------

# c = 5
#
# for i in range(6):
#     print(c)
#     c -= 1

#-------------------------------------------

# s = 0
# w = 1
#
# print("Proszę wprowadzić kolejną wartość.")
# print("Jeżeli wprowadzić 0 to kończymy procedurę.")
#
# while w != 0:
#     print("Curent sum:", s)
#     w = float(input("Wprowadź wartość: "))
#     s = s + w
#     if w == 0:
#         break
# print("Procedura zatrzymana")
# print("Łączna wartość wprowadzonych liczb to: ", s)

#------------------------------------------------------------

# z = 3

# for i in range(6):
#     print(z)
#     z = z + 3

# for i in range(3, 20, 4):
#     print(i)

#-----------------------------------------------------------

# for i in range(4):
#     print(i)
# else:
#     print("Koniec")

#-----------------------------------------------------------

# lista = ["AAA", "BBB"]
# lista2 = [1,2,3]
#
# for i in lista:
#     for j in lista2:
#         print(i, j)

#-----------------------------------------------------------


# liczba = 0
#
# while liczba <= 15:
#     print("Kolejna liczba: ", liczba)
#     liczba += 3
# print("Teraz KONIEC")

#----------------------------------------------------------


# liczba = int(input("Wprowadź wartość: "))
# i = 0
# w = 0
#
# while i <= liczba:
#     w = w + i
#     i = i + 1
# print("Suma liczb wynosi: ", w)

#------------------------------------------------------

# ile = int(input("Ile razy chcesz powiedzieć HURA! "))
# i = 1
#
# while i <= ile:
#     print("Hura!")
#     i= i + 1
# print("Koniec już tego ...")

#--------------------------------------------


# k = ["Agaton", "zapiecek", "bekon", "Renata", "Wojtek"]
# j = 1
#
# for i in k:
#     print(j, i)
#     j += 1

#-------------------------------------------
#
# k = 0
#
# while True:
#     print(k)
#     k = k + 1
#     if k >= 5:
#         break

#------------------------------------------------


# k = 0
#
# while k < 5:
#     print(k)
#     k = k + 1
#
# print("Dotarliśmy do liczby: ", k)

#----------------------------------------------------

# for i in range(1,5):
#     print(i)
#     i = i + 1
# print("Kamil")
#
# for i in range(1, 10):
#     if (i%5 == 0):
#         print("Kamil")
#         break
#     print(i)


#-------------------------------------------

#
# for i in range(1,4):
#     print("Witamy ", i, " raz")
#
# for i in "123":
#     print("Witamy ", i, " raz")

#----------------------------------------------

# i = 1
# j = 2
#
# while i >= 1:
#     a = " " *j+ "*" *i+ " " *j
#     print(a)
#     i = i+2
#     j = j-1
#     if i>5:
#         break
# i = 3
# j = 1
# while i>=1:
#     a = " " *j+ "*" *i+ " " *j
#     print(a)
#     i = i-2
#     j = j+1


#-----------------------------------------


# i = 1
#
# while i <= 3:
#     print("Witamy ", i, " raz")
#     i = i+1


# licznik = 1
# liczba = 6
#
# while licznik <= 5:
#     wynik = liczba * licznik
#     licznik = licznik + 1
#     print(wynik)

# i = 1
# while i <= 5:
#     print(6*i)
#     i = i+1

#--------------------------------------------

# for i in range(1,7):
#     print("h = ", i)


# i = 1
#
# while i <= 6:
#     print("h = ", i)
#     i += 1

#

# liczba = int(input("Wprowadź wartość: "))
# a = 1
# if liczba == 0:
#     print("Silnia 0 jest rowna 1")
# else:
#     while liczba >= 1:
#         a = a * liczba
#         liczba = liczba - 1
#     print("Silnia wynosi: ",a)

#---------------------------------------------


# lista = ["ARA", "BereKA", "GONabEACH"]
#
# print("To są wyrazy do wyboru: ", lista[0], lista[1], lista[2])
# liczba = int(input("Wybierz numer wyrazu, który ma być przeliterowany?"
#                    " Podaj liczbę: 1, 2 lub 3: "))
# liczba = liczba - 1
# print("Wybrałeś słowo: ", lista[liczba])
# for i in lista[liczba]:
#     print(i)

#------------------------------------------------

# lista = ["salad", "pasta", "pizza", "nachos"]
# licznik = 1
#
# for i in lista:
#     print(licznik, i)
#     licznik = licznik + 1

# lista = ["salad", "pasta", "pizza", "nachos"]
# for indeks, element_listy in enumerate(lista, start = 1):
#     print(indeks, element_listy)


#-------------------------------------------------
#
# wyraz = "Puk "
#
# for i in range(1,5):
#     print(i)
#     print(i*wyraz)


#===================================================


# g = ["Kamil1", "Kamil2", "Kamil3", "Kamil4"]
# l = 1
#
# for i in g:
#     print(l, i)
#     l+=1

#------------------------------------------------------


# def wiliczanie_listy(g):
#     l = 1
#     for i in g:
#         print(l, i)
#         l+=1
#
# wiliczanie_listy(["Kamil1", "Kamil2", "Kamil3", "Kamil4"])
# a = ["Element 1", "Element 2", "Element 3", "Element 4"]
# wiliczanie_listy(a)

#---------------------------------------------------------
#61


# def suma_skumulowana(l):
#     w = 1
#     for i in l:
#         w *= i
#         print(w)
#
# lista = [1,2,12,2]
# suma_skumulowana(lista)

#----------------------------------------------------------


# x = 0
# y = 1
#
# for i in [2,4,6]:
#     x = x + y*i
#     y = y + 1
# print(x)

#--------------------------------------------------------

# lista1 = ["Wojciech", "Tomasz", "Adam"]
# lista2 = ["szop", "zając", "krowa"]
#
# def funkcja(l):
#     for i in l:
#         print(i, end=" ")
#         print()
#     print("Witamy w naszym zespole!")
#
# funkcja(lista1)
# print()
# funkcja(lista2)

#--------------------------------------------------


# lista = ["Ewa", "Darek", "Piotrek"]
#
# for i in lista:
#     print("Cześć ", i, " Zapraszam na moje urodziny!")
#

#-------------------------------------------------

# import sys
#
# print("Pamiętaj: a > b")
# a = int(input("Wpisz a:"))
# b = int(input("Wpisz b:"))
#
# if a > b:
#     print("-------------------------")
#     print("Dobrze")
#     sys.exit(0)
# else:
#     while a <= b:
#         print("Źle! Powtórz!")
#         a = int(input("Wpisz a:"))
#         b = int(input("Wpisz b:"))
#
#     print("-------------------------")
#     print("Dobrze")

#------------------------------------------------

#---- Zad 66 ---------------------------------


#for i in range(6):
#    print("Dwa do potęgi ", i, 2**i)

# def funkcja(a):
#     for i in range(a):
#         print("Dwa do potęgi ", i, 2 ** i)
#
# funkcja(14)

#--------------------------------------------------

# odp = 0
# pytanie = "Odpowiedz na pytanie: tak lub nie ? "
#
# while odp != "tak":
#     odp = input(pytanie)
# else:
#     print("Dziękuję za odpowiedz")

#-----------------------------------------------------


# for i in range(1,5):
#     print("próba nr: ", i)

#---------------------------------------------------


# for i in range(10,41):
#     if i%5 != 0 and i%3 != 0 and i%2 != 0:
#         print(i)

# def funkcja(a, b, c, d, e):
#     for i in range(a, b):
#         if i%c != 0 and i%d !=0 and i%e != 0:
#             print(i)
#
# funkcja(10, 40, 5, 3, 2)

#--------------------------------------------------


# licznik = 4
#
# print(licznik)
# for i in range (1,4):
#     licznik = licznik + 4
#     print(licznik)
# print("Zadanie wykonane")


# licznik = 4
#
# while licznik <= 16:
#     licznik = licznik + 4
#     print(licznik)
# print("Zadanie wykonane")

#---------------------------------------------


# for i in range(10, 21):
#     print(i)
#     if i == 14:
#         break

# def funkcja(a, b, c):
#     for i in range(a, b):
#      print(i)
#      if i >= c:
#          break
#
# funkcja(10, 21, 14)

#---------------------------------------------------

# liczba = 0
#
# for i in range(1,7):
#     print("Kolejna liczba ma nr: ", liczba)
#     liczba = liczba + 5

# for i in range(5, 30, 5):
#     print("Kolejna liczba ma nr: ", i)


#------------------------------------------

# for i in range(0,6):
#     for j in range(i):
#         print(i, j)

# results = []
# for a in range(6):
#     for b in range(a):
#         results.append((a, b))
#         print(a,b)
#
# from itertools import cycle
#
# numbers = [0, 2, 4, 6, 8]
#
# numbers_iterator = cycle(numbers)
#
# max_nums = 10
#
# for i in range(9):
#     print(next(numbers_iterator))

#-------------------------------------------

#
# def parz(a):
#     for i in a:
#         if i % 2 == 0:
#             print(i)
#
# parz([7,14,2,7])
# c=[12,5,2,8,7,17]
# parz(c)


#---------------------------------------------------

#
# for i in range(0,13):
#     for j in [00,15,30,45]:
#         print(i, " : ", j, " PM")

#----------------------------------------------------


# for i in range(3,8):
#     print(i)

# a = 3
#
# while a <= 7:
#     print(a)
#     a = a + 1


#--------------------------------------------


# def malejace(a, b):
#     print("Zakres pomiędzy ", a, " a ", b, " to ")
#     while b >= a:
#         print(b)
#         b = b - 1
#
# malejace(15,17)


# def zakres(a,b):
#     a = a + 1
#     while a > b:
#         a = a - 1
#         print(a)
#
# #zakres(112,101)
# a = 17
# b = 15
# zakres(a,b)

#---------------------------------------------------







