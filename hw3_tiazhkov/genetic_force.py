import random as random # Импортируем библиотку генерации случайных значений
import numpy as np # Импортируем библиотеку numpy
import streamlit as st
import numexpr as ne
import ast




def getSurvPopul(
        popul,
        val,
        nsurv,
        reverse
):
    newpopul = []  # Двумерный массив для новой популяции
    sval = sorted(val, reverse=reverse)  # Сортируем зачения в val в зависимости от параметра reverse
    for i in range(nsurv):  # Проходимся по циклу nsurv-раз (в итоге в newpopul запишется nsurv-лучших показателей)
        index = val.index(sval[i])  # Получаем индекс i-того элемента sval в исходном массиве val
        newpopul.append(popul[index])  # В новую папуляцию добавляем элемент из текущей популяции с найденным индексом
    return newpopul, sval  # Возвращаем новую популяцию (из nsurv элементов) и сортированный список



def getParents(
        curr_popul,
        nsurv
):
    indexp1 = random.randint(0, nsurv - 1)  # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
    indexp2 = random.randint(0, nsurv - 1)  # Случайный индекс второго родителя в диапазоне от 0 до nsurv - 1
    # random.randint(A, B) генерит случайное целое число включающее ОБЕ границы, поэтому nsurv - 1

    botp1 = curr_popul[indexp1]  # Получаем первого бота-родителя по indexp1
    botp2 = curr_popul[indexp2]  # Получаем второго бота-родителя по indexp2
    return botp1, botp2  # Возвращаем обоих полученных ботов




def crossPointFrom2Parents(
        botp1,
        botp2,
        j
):
    pindex = random.random()  # Получаем случайное число в диапазоне от 0 до 1

    # Если pindex меньше 0.5, то берем значения от первого бота, иначе от второго
    if pindex < 0.5:
        x = botp1[j]
    else:
        x = botp2[j]
    return x  # Возвращаем значние бота

st.title('Это приложение для вычисления корней уравнения при помощи генетического алгоритма')
n = 100  # Размер популяции
nsurv = 20  # Количество выживших (столько лучших переходит в новую популяцию)
nnew = n - nsurv  # Количество новых (столько новых ботов создается)
l = 8  # Длина бота
epohs = int(st.number_input('Введите количество эпох в виде целого положительного числа, не равного 0'))  # Количество эпох

mut = st.number_input('Введите коэффициент мутации в формате десятичной дроби, в качестве разделителя используйте точку')  # Коэфициент мутаций

formula = st.text_input("Введите уравнение в формате многочлена в синтаксисе python без знака 'равно'")

popul = []  # Двумерный массив популяции, размерностью [n, l]. 100 ботов по 8 компонентов каждый
val = []  # Одномерный массив значений этих ботов

result = st.button('Начать процесс подбора корней уравнения')
if result:

    for i in range(n):
        popul.append([])
        for j in range(l):
            popul[i].append(random.random())  # В каждый компонент бота записываем рандомное значение

    for it in range(epohs):
        val = []

        for i in range(n):
            bot = popul[i]  # Берем очередного бота

            x = bot[0] + 5 * bot[1] + 10 * bot[2] + 25 * bot[3]  # первые 4 значения отводим для Х
            y = bot[4] + 5 * bot[5] + 10 * bot[6] + 25 * bot[7]  # вторые 4 значения - для Y
            f = eval(formula)  # для кодирования применяем эту функцию
            val.append(abs(f))  # добавляем модуль значения в список на эпоху
        # в этой задаче будем искать 0 функции

        newpopul, sval = getSurvPopul(popul, val, nsurv, 0)  # Получаем новую популяцию и сортированный список значнией
        print(it, " ", [round(s, 8) for s in sval[0:5]])  # Выводим 5 лучших ботов

        for i in range(nnew):  # Проходимся в цикле nnew-раз
            botp1, botp2 = getParents(newpopul, nsurv)  # Из newpopul(новой популяции) получаем двух случайных родителей-ботов
            newbot = []  # Массив для нового бота
        # проходимся по длине бота и осуществляем смешивание/скрещивание от родителей
            for j in range(l):  # Проходим по всей длине бота
                x = crossPointFrom2Parents(botp1, botp2, j)  # Получаем значение для j-ого компонента бота
                x += mut * (2 * random.random() - 1.0)  # Добавялем к значению бота случайную величину, зависящую от коэфециента мутации
                newbot.append(x)  # Добавялем новое значение в бота
            newpopul.append(newbot)  # Добавляем бота в новую популяцию
        # (таким образом к nsurv-лучших ботов предыдующей популяции добавится nnew-новых ботов)

        popul = newpopul  # Записываем в popul посчитанную новую популяцию

    bot = popul[0] # Берем первого (лучшего) бота в финальной популяции
    x = bot[0] + 5*bot[1] + 10*bot[2] + 25*bot[3] # Считаем x
    y = bot[4] + 5*bot[5] + 10*bot[6] + 25*bot[7] # Считаем y
    f = eval(formula) # Считаем значение функции
    st.write(bot) # Выводим бота (8 компонент)
    st.write("x =",x, "y =", y) # Выводим значения x и y
    st.write("f =", f )






