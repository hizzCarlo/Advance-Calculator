import math
import tkinter
from tkinter import *
from math import *

root = Tk()
root.title("Advance Calculator")
root.configure(background='black')
root.resizable(width=False, height=False)
root.geometry("417x600+500+90")
calc = Frame(root)
calc.grid()
screen = StringVar(root)
screen.set("0")
A = StringVar(root)
A.set("0")
B = StringVar(root)
B.set("0")
C = StringVar(root)
C.set("0")
history1 = StringVar(root)
history1.set("0")
current = ""
power = ""
Acurrent = ""
Bcurrent = ""
Ccurrent = ""

firstnum = str()
global secondnum
mathsign = str()

nestedsumation = False
othersign = False
defxworking = False
percentt = False
mixfraction = False
negative = False
op = False
inA = False
inB = False
inC = False

def math_button_pressed():
    if mathsign == '+':
        button_plus.config(relief=SUNKEN)
    if mathsign == '-':
        button_minus.config(relief=SUNKEN)
    if mathsign == '*':
        button_multiply.config(relief=SUNKEN)
    if mathsign == '/':
        button_division.config(relief=SUNKEN)
    if othersign == 'mod':
        button_mod.config(relief=SUNKEN)
    if othersign == 'log':
        button_log.config(relief=SUNKEN)
    if othersign == '^':
        button_x.config(relief=SUNKEN)
    if othersign == 'x⁻ⁿ':
        button_negpow.config(relief=SUNKEN)

def math_button_raised():
    button_plus.config(relief=RAISED)
    button_minus.config(relief=RAISED)
    button_multiply.config(relief=RAISED)
    button_division.config(relief=RAISED)
    button_mod.config(relief=RAISED)
    button_log.config(relief=RAISED)
    button_x.config(relief=RAISED)
    button_negpow.config(relief=RAISED)

def is_int(num):
    if float(num):
        return float(num)
    else:
        return float(num)

def number_pressed(butt):
    global current, power, firstnum, secondnum, inA, inB, inC, Acurrent, Bcurrent, Ccurrent

    if mathsign == str() and defxworking == False and inA == False and inB == False and inC == False:
        current = current + str(butt)
        screen.set(current)
        firstnum = float(current)

    elif mathsign != str() and defxworking == False and inA == False and inB == False and inC == False:
        math_button_raised()
        current = current + str(butt)
        screen.set(current)
        secondnum = float(current)

    elif mathsign == str() and defxworking == True and inA == False and inB == False and inC == False:
        power = power + str(butt)
        current = current + str(butt)
        screen.set(current)

    elif mathsign != str and defxworking == True and inA == False and inB == False and inC == False:
        power = power + str(butt)
        current = current + str(butt)
        screen.set(current)
        print(power)
    elif mathsign == str() and defxworking == False and inA == True and inB == False and inC == False:
        Acurrent = Acurrent + str(butt)
        A.set(Acurrent)

    elif mathsign == str() and defxworking == True and inA == True and inB == False and inC == False:
        power = power + str(butt)
        Acurrent = Acurrent + str(butt)
        A.set(Acurrent)

    elif mathsign == str() and defxworking == False and inA == False and inB == True and inC == False:
        Bcurrent = Bcurrent + str(butt)
        B.set(Bcurrent)

    elif mathsign == str() and defxworking == True and inA == False and inB == True and inC == False:
        power = power + str(butt)
        Bcurrent = Bcurrent + str(butt)
        B.set(Bcurrent)

    elif mathsign == str() and defxworking == False and inA == False and inB == False and inC == True:
        Ccurrent = Ccurrent + str(butt)
        C.set(Ccurrent)

    elif mathsign == str() and defxworking == True and inA == False and inB == False and inC == True:
        power = power + str(butt)
        Ccurrent = Ccurrent + str(butt)
        C.set(Ccurrent)


def math_pressed(math):
    global current, power, mathsign, firstnum, secondnum, defxworking, percentt, powrule, negative, op, othersign
    op = True

    if mathsign == str() and defxworking == False and percentt == False and firstnum != str():
        mathsign = str(math)
        math_button_pressed()
        current = ""

    elif mathsign != str() and defxworking == False and percentt == False:
        print(2)
        if mathsign == '+':
            firstnum = float(firstnum) + float(calculation.get())
        if mathsign == '-':
            firstnum = float(firstnum) - float(calculation.get())
        if mathsign == '*':
            firstnum = float(firstnum) * float(calculation.get())
        if mathsign == '/':
            firstnum = float(firstnum) / float(calculation.get())
        if mathsign == 'mod':
            firstnum = round(float(firstnum)) % round(float(calculation.get()))
        if mathsign == 'log':
            firstnum = math.log(float(firstnum), float(calculation.get()))
        if mathsign == '^':
            firstnum = float(firstnum) ** float(calculation.get())
        if mathsign == 'x⁻ⁿ':
            firstnum = firstnum ** round(float(calculation.get()))

        if mathsign == '+' and negative == True:
            firstnum = float(firstnum) + float(-(float(calculation.get())))
        if mathsign == '-' and negative == True:
            firstnum = float(firstnum) - float(-(float(calculation.get())))
        if mathsign == '*' and negative == True:
            firstnum = float(firstnum) * float(-(float(calculation.get())))
        if mathsign == '/' and negative == True:
            firstnum = float(firstnum) / float(-(float(calculation.get())))
        if mathsign == 'mod' and negative == True:
            firstnum = round(float(firstnum)) % round(float(calculation.get()))
        if mathsign == 'log' and negative == True:
            firstnum = math.log(float(firstnum), float(calculation.get()))
        if mathsign == '^' and negative == True:
            firstnum = float(firstnum) ** float(-(float(calculation.get())))
        if mathsign == 'x⁻ⁿ' and negative == True:
            firstnum = firstnum ** round(float(calculation.get()))
        screen.set(firstnum)
        mathsign = str(math)
        math_button_pressed()
        current = ""

def mod():
    global firstnum, secondnum, mathsign, current
    if mathsign == "":
        firstnum = round(firstnum) % round(float(secondnum))

        screen.set(firstnum)
    else:
        secondnum = round(firstnum) % round(float(calculation.get()))
        screen.set(secondnum)
def squareroot():
    global firstnum, secondnum, mathsign, current
    if mathsign == '':
        firstnum = math.sqrt(float(calculation.get()))
        screen.set(is_int(firstnum))

    else:
        secondnum = math.sqrt(float(calculation.get()))
        screen.set(secondnum)

def x():
    global firstnum, secondnum, mathsign, current, defxworking

    if mathsign == str():
        current = str(is_int(firstnum)) + '^'
        screen.set(current)
        defxworking = True

    elif mathsign != str():

        current = str(is_int(secondnum)) + '^'
        screen.set(current)
        defxworking = True

def e():
    global firstnum, secondnum
    if mathsign == '':
        firstnum = math.e
        screen.set(is_int(firstnum))
    else:
        secondnum = math.e
        screen.set(secondnum)

def pi():
    global firstnum, secondnum
    if mathsign == '':
        firstnum = math.pi
        screen.set(is_int(firstnum))
    else:
        secondnum = math.pi
        screen.set(secondnum)

def result():
    global firstnum, secondnum, mathsign, current, power, defxworking, percentt, powrule, othersign, negative
    if defxworking == False and percentt == False:
        if mathsign == '+':
            history1.set(str(firstnum) + " + " + str(float(calculation.get())) + " = " + str(float(firstnum) + float(calculation.get())))
            firstnum = float(firstnum) + float(calculation.get())
        if mathsign == '-':
            history1.set(str(firstnum) + " - " + str(float(calculation.get())) + " = " + str(float(firstnum) - float(calculation.get())))
            firstnum = float(firstnum) - float(calculation.get())
        if mathsign == '*':
            history1.set(str(firstnum) + " x " + str(float(calculation.get())) + " = " + str(float(firstnum) * float(calculation.get())))
            firstnum = float(firstnum) * float(calculation.get())
        if mathsign == '/':
            history1.set(str(firstnum) + " ÷ " + str(float(calculation.get())) + " = " + str(float(firstnum) / float(calculation.get())))
            firstnum = float(firstnum) / float(calculation.get())
        if mathsign == 'mod':
            history1.set(str(round(float(firstnum))) + "mod" + str(round(float(calculation.get()))) + " = " + str(float(firstnum) % float(calculation.get())))
            firstnum = round(float(firstnum)) % round(float(calculation.get()))
        if mathsign == 'log':
            history1.set("log" + str(float(calculation.get())) +"("+ str(firstnum) +")" + " = " + str(float(math.log(firstnum, float(calculation.get())))))
            firstnum = float(math.log(firstnum, float(calculation.get())))
        if mathsign == '^':
            history1.set(str(firstnum) + "^" + str(float(calculation.get())) + " =" + str(float(firstnum) ** float(calculation.get())))
            firstnum = float(firstnum) ** float(calculation.get())
        if mathsign == 'x⁻ⁿ':
            history1.set(str(firstnum) + "^" + str(-(float(calculation.get()))) + " = " + str(float(firstnum) ** -(float(calculation.get()))))
            firstnum = firstnum ** -(float(calculation.get()))
        screen.set(is_int(firstnum))

    mathsign = str()
    current = ""
    power = ""

    if defxworking == False and mathsign == '*' or '/' and percentt == True:
        clear()

def neg():
    global firstnum, secondnum, calculation, powrule, inA, inB, inC, negative, op, Acurrent, Bcurrent, Ccurrent
    if inA == True and inB == False and inC == False:
        process = "-" + (str(btnA.get()))
        Acurrent = process
        A.set(process)

    elif inA == False and inB == True and inC == False:
        process = "-" + (str(btnB.get()))
        Bcurrent = process
        B.set(process)

    elif inA == False and inB == False and inC == True:
        process = "-" + (str(btnC.get()))
        Ccurrent = process
        C.set(process)

    else:
        if op == False:
            firstnum = "-" + (str(calculation.get()))
            screen.set(firstnum)

            negative = False
        else:
            process = "-" + (str(calculation.get()))
            screen.set(process)
            negative = True

def clear():
    global current, firstnum, secondnum, mathsign, power, defxworking, percentt, inA, inB, inC, negative, op, Bcurrent, Acurrent, Ccurrent, nestedsumation, history1, history1current
    screen.set(0)
    A.set(0)
    B.set(0)
    C.set(0)
    history1.set(0)
    current = ""
    power = ""
    Acurrent = ""
    Bcurrent = ""
    Ccurrent = ""
    history1current = ""
    firstnum = str()
    secondnum = str()
    mathsign = str()
    nestedsumation = False
    defxworking = False
    math_button_raised()
    percentt = False
    inA = False
    inB = False
    inC = False
    negative = False
    op = False

def remove():
    global current, firstnum, inA, inB, inC, Acurrent, Bcurrent, Ccurrent
    if inA == True and inB == False and inC == False:
        a = btnA.get()
        btnA.delete(first=len(a) - 1, last="end")
        Acurrent = str(btnA.get())
    elif inA == False and inB == True and inC == False:
        a = btnB.get()
        btnB.delete(first=len(a) - 1, last="end")
        Bcurrent = str(btnB.get())
    elif inA == False and inB == False and inC == True:
        a = btnC.get()
        btnC.delete(first=len(a) - 1, last="end")
        Ccurrent = str(btnC.get())
    else:
        a = calculation.get()
        calculation.delete(first=len(a)-1,last="end")
        current = str(calculation.get())
        firstnum = float(current)

def percent():
    global firstnum, secondnum, current, percentt
    if mathsign == "":
        current = float(calculation.get()) * 0.01
        screen.set(current)
        firstnum = float(current)
        percentt = True
    else:
        current = float(calculation.get()) * 0.01
        screen.set(current)

def factorial():
    global firstnum, current, mathsign
    if mathsign == "":
        current = math.factorial(int(calculation.get()))
        screen.set(current)
        firstnum = current
    else:
        current = math.factorial(int(calculation.get()))
        screen.set(current)

def cuberoot():
    global firstnum, secondnum, history1
    if mathsign == "":
        #firstnum = firstnum ** 0.333333333333333333333
        firstnum = math.cbrt(float(firstnum))
        screen.set(firstnum)
        history1.set(str("∛" + str(float(firstnum)) + "=" + str(math.cbrt(float(firstnum)))))
    else:
        secondnum = math.cbrt(float(calculation.get()))
        screen.set(secondnum)

def ceil():
    global firstnum
    if mathsign == "":
        firstnum = math.ceil(firstnum)
        screen.set(firstnum)
    else:
        secondnum = math.ceil(calculation.get())
        screen.set(secondnum)
def floor():
    global firstnum
    if mathsign == "":
        firstnum = math.floor(firstnum)
        screen.set(firstnum)
    else:
        secondnum = math.floor(calculation.get())
        screen.set(secondnum)

def mixfraction():
    global firstnum, A, B, C, calculation, trinum, history1
    process = float(A.get()) * float(C.get()) + float(B.get())
    firstnum = process / float(C.get())
    screen.set(firstnum)
    history1.set(str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(float(firstnum))))
    sigma_op1()

def powrule():
    global firstnum, A, B, C, calculation, history1
    process = float(A.get())
    process1 = float(B.get()) * float(C.get())
    firstnum = process ** process1
    screen.set(firstnum)
    history1.set(str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(float(firstnum))))
    sigma_op1()
def sigma():
    global firstnum, secondnum, A, B, C, calculation, nestedsumation, Ccurrent
    if nestedsumation == False:
        start1 = int(A.get())
        end1 = int(B.get())
        total = int(C.get())
        firstnum = start1
        secondnum = end1
        Ccurrent = total
        sum = 0
        result = sigma_sum(start1, end1+1, lambda i: sum + total)
        screen.set(result)
        nestedsumation = True
        history1.set(str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(float(result))))
        sigma_op1()
    elif nestedsumation == True:
        start2 = int(A.get())
        end2 = int(B.get())
        sum = int(C.get())
        sumtotal = 0
        for i in range(firstnum, secondnum + 1):
            for j in range(start2, end2 + 1):
                sumtotal = sumtotal + sum
        screen.set(sumtotal)
        history1.set(str("i₁=" + str(float(firstnum)) + " f₁=" + str(float(secondnum)) + " i₂=" + str(float(A.get())) + " f₂=" + str(float(B.get())) + " = " + str(float(sumtotal))))
        firstnum = sumtotal
        nestedsumation = False


def sigma1():
    global firstnum, secondnum, A, B, C, calculation, nestedsumation, Ccurrent
    if nestedsumation == False:
        start1 = int(A.get())
        end1 = int(B.get())
        total = int(C.get())
        firstnum = start1
        secondnum = end1
        Ccurrent = total
        sum = 0
        result = sigma_sum(start1, end1+1, lambda i: sum + total)
        screen.set(result)
        nestedsumation = True
        history1.set(str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(float(result))))
        sigma_op1()
    elif nestedsumation == True:
        start2 = int(A.get())
        end2 = int(B.get())
        sum = int(C.get())
        sumtotal = 0
        for i in range(firstnum, secondnum + 1):
            for j in range(start2, end2 + 1):
                sumtotal = sumtotal + sum + (i ** j)
        screen.set(sumtotal)
        history1.set(str("i₁=" + str(float(firstnum)) + " f₁=" + str(float(secondnum)) + " i₂=" + str(
            float(A.get())) + " f₂=" + str(float(B.get())) + " = " + str(float(sumtotal))))
        firstnum = sumtotal
        nestedsumation = False

def sigma2():
    global firstnum, secondnum, A, B, C, calculation, nestedsumation, Ccurrent
    if nestedsumation == False:
        start1 = int(A.get())
        end1 = int(B.get())
        total = int(C.get())
        firstnum = start1
        secondnum = end1
        Ccurrent = total
        sum = 0
        result = sigma_sum(start1, end1+1, lambda i: sum + total)
        screen.set(result)
        nestedsumation = True
        history1.set(
            str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(
                float(result))))
        sigma_op1()
    elif nestedsumation == True:
        start2 = int(A.get())
        end2 = int(B.get())
        sum = int(C.get())
        sumtotal = 0
        for i in range(firstnum, secondnum + 1):
            for j in range(start2, end2 + 1):
                sumtotal = sumtotal + (sum ** j)
        screen.set(sumtotal)
        history1.set(str("i₁=" + str(float(firstnum)) + " f₁=" + str(float(secondnum)) + " i₂=" + str(
            float(A.get())) + " f₂=" + str(float(B.get())) + " = " + str(float(sumtotal))))
        firstnum = sumtotal
        nestedsumation = False

def sigma3():
    global firstnum, secondnum, A, B, C, calculation, nestedsumation, Ccurrent
    if nestedsumation == False:
        start1 = int(A.get())
        end1 = int(B.get())
        total = int(C.get())
        firstnum = start1
        secondnum = end1
        Ccurrent = total
        sum = 0
        result = sigma_sum(start1, end1+1, lambda i: sum + total)
        screen.set(result)
        nestedsumation = True
        history1.set(
            str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(
                float(result))))
        sigma_op1()
    elif nestedsumation == True:
        start2 = int(A.get())
        end2 = int(B.get())
        sum = int(C.get())
        sumtotal = 0
        for i in range(firstnum, secondnum + 1):
            for j in range(start2, end2 + 1):
                sumtotal = sumtotal + (sum ** i)
        screen.set(sumtotal)
        history1.set(str("i₁=" + str(float(firstnum)) + " f₁=" + str(float(secondnum)) + " i₂=" + str(
            float(A.get())) + " f₂=" + str(float(B.get())) + " = " + str(float(sumtotal))))
        firstnum = sumtotal
        nestedsumation = False

def sigma4():
    global firstnum, secondnum, A, B, C, calculation, nestedsumation, Ccurrent
    if nestedsumation == False:
        start1 = int(A.get())
        end1 = int(B.get())
        total = int(C.get())
        firstnum = start1
        secondnum = end1
        Ccurrent = total
        sum = 0
        result = sigma_sum(start1, end1+1, lambda i: sum + total)
        screen.set(result)
        nestedsumation = True
        history1.set(
            str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(
                float(result))))
        sigma_op1()
    elif nestedsumation == True:
        start2 = int(A.get())
        end2 = int(B.get())
        sum = int(C.get())
        sumtotal = 0
        for i in range(firstnum, secondnum + 1):
            for j in range(start2, end2 + 1):
                sumtotal = sumtotal + sum + (j ** i)
        screen.set(sumtotal)
        history1.set(str("i₁=" + str(float(firstnum)) + " f₁=" + str(float(secondnum)) + " i₂=" + str(
            float(A.get())) + " f₂=" + str(float(B.get())) + " = " + str(float(sumtotal))))
        firstnum = sumtotal
        nestedsumation = False

def sigma5():
    global firstnum, secondnum, A, B, C, calculation, nestedsumation, Ccurrent
    if nestedsumation == False:
        start1 = int(A.get())
        end1 = int(B.get())
        total = int(C.get())
        firstnum = start1
        secondnum = end1
        Ccurrent = total
        sum = 0
        result = sigma_sum(start1, end1+1, lambda i: sum + total)
        screen.set(result)
        nestedsumation = True
        history1.set(
            str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(
                float(result))))
        sigma_op1()
    elif nestedsumation == True:
        start2 = int(A.get())
        end2 = int(B.get())
        sum = int(C.get())
        sumtotal = 0
        for i in range(firstnum, secondnum + 1):
            for j in range(start2, end2 + 1):
                sumtotal = sumtotal + sum + j
        screen.set(sumtotal)
        history1.set(str("i₁=" + str(float(firstnum)) + " f₁=" + str(float(secondnum)) + " i₂=" + str(
            float(A.get())) + " f₂=" + str(float(B.get())) + " = " + str(float(sumtotal))))
        firstnum = sumtotal
        nestedsumation = False

def sigma6():
    global firstnum, secondnum, A, B, C, calculation, nestedsumation, Ccurrent
    if nestedsumation == False:
        start1 = int(A.get())
        end1 = int(B.get())
        total = int(C.get())
        firstnum = start1
        secondnum = end1
        Ccurrent = total
        sum = 0
        result = sigma_sum(start1, end1+1, lambda i: sum + total)
        screen.set(result)
        nestedsumation = True
        history1.set(
            str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(
                float(result))))
        sigma_op1()
    elif nestedsumation == True:
        start2 = int(A.get())
        end2 = int(B.get())
        sum = int(C.get())
        sumtotal = 0
        for i in range(firstnum, secondnum + 1):
            for j in range(start2, end2 + 1):
                sumtotal = sumtotal + sum + i
        screen.set(sumtotal)
        history1.set(str("i₁=" + str(float(firstnum)) + " f₁=" + str(float(secondnum)) + " i₂=" + str(
            float(A.get())) + " f₂=" + str(float(B.get())) + " = " + str(float(sumtotal))))
        firstnum = sumtotal
        nestedsumation = False
def sigma_op1():
    global firstnum, A, B, C, calculation, nestedsumation, Acurrent, Bcurrent, Ccurrent
    A.set(0)
    B.set(0)
    C.set(0)
    Acurrent = ""
    Bcurrent = ""
    Ccurrent = ""

def sigma_sum(start1, end1, expression):
    return sum(expression(i) for i in range(start1, end1))
def log():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.log(float(calculation.get()))
        screen.set(firstnum)
        history1.set(str("log(" + str(float(calculation.get())) + ")" + " = " + str(math.log(float(calculation.get())))))
    else:
        secondnum = math.log(float(calculation.get()))
        screen.set(secondnum)

def log2():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.log2(float(calculation.get()))
        screen.set(firstnum)
        history1.set(
            str("log2(" + str(float(calculation.get())) + ")" + " = " + str(math.log2(float(calculation.get())))))
    else:
        secondnum = math.log2(float(calculation.get()))
        screen.set(secondnum)

def log10():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.log10(float(calculation.get()))
        screen.set(firstnum)
        history1.set(
            str("log10(" + str(float(calculation.get())) + ")" + " = " + str(math.log10(float(calculation.get())))))
    else:
        secondnum = math.log10(float(calculation.get()))
        screen.set(secondnum)

def sin():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.sin(math.radians(float(calculation.get())))
        screen.set(firstnum)
        history1.set(str("sin(" + str(float(calculation.get())) + ")" + " = " + str(math.sin(math.radians(float(calculation.get()))))))
    else:
        secondnum = math.sin(math.radians(float(calculation.get())))
        screen.set(secondnum)

def cos():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.cos(math.radians(float(calculation.get())))
        screen.set(firstnum)
        history1.set(str("cos(" + str(float(calculation.get())) + ")" + " = " + str(math.cos(math.radians(float(calculation.get()))))))
    else:
        secondnum= math.cos(math.radians(float(calculation.get())))
        screen.set(secondnum)

def tan():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.tan(math.radians(float(calculation.get())))
        screen.set(firstnum)
        history1.set(str("tan(" + str(float(calculation.get())) + ")" + " = " + str(
            math.tan(math.radians(float(calculation.get()))))))
    else:
        secondnum = math.tan(math.radians(float(calculation.get())))
        screen.set(secondnum)

def tanh():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.tanh(float(calculation.get()))
        screen.set(firstnum)
    else:
        secondnum = math.tanh(float(calculation.get()))
        screen.set(secondnum)

def cosh():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.cosh(float(calculation.get()))
        screen.set(firstnum)
    else:
        secondnum = math.cosh(float(calculation.get()))
        screen.set(secondnum)

def sinh():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.sinh(float(calculation.get()))
        screen.set(firstnum)
    else:
        secondnum = math.sinh(float(calculation.get()))
        screen.set(secondnum)

def acosh():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.acosh(float(calculation.get()))
        screen.set(firstnum)
    else:
        secondnum = math.acosh(float(calculation.get()))
        screen.set(secondnum)

def asinh():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.asinh(float(calculation.get()))
        screen.set(firstnum)
    else:
        secondnum = math.asinh(float(calculation.get()))
        screen.set(secondnum)

def exp():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = math.exp(float(calculation.get()))
        screen.set(firstnum)
    else:
        secondnum = math.exp(float(calculation.get()))
        screen.set(secondnum)

def exp2():
    global firstnum, secondnum
    if mathsign == "":
        firstnum = (math.e ** 2) * float(calculation.get())
        screen.set(firstnum)
    else:
        secondnum = (math.e ** 2) * float(calculation.get())
        screen.set(secondnum)

def fraction():
    global firstnum, A, B, C
    process = round((float(B.get()))) / round((float(C.get())))
    firstnum = round((float(A.get()))) ** process
    screen.set(firstnum)
    history1.set(
        str("A=" + str(float(A.get())) + " B=" + str(float(B.get())) + " C=" + str(float(C.get())) + " = " + str(
            float(firstnum))))
    sigma_op1()

def buttonA():
    global inA, inB, inC
    inB = False
    inC = False
    inA = True
def buttonB():
    global inB, inA, inC
    inA = False
    inC = False
    inB = True

def buttonC():
    global inC, inA, inB
    inA = False
    inB = False
    inC = True

# Widgets
calculation = Entry(root, textvariable = screen, font=("Verdana", 15, ), bd = 20,
                    insertwidth=4, width=29,  justify=RIGHT)
calculation.grid(columnspan=7)

# Numbers
# 7
button7 = Button(root, text='7', command=lambda: number_pressed(7), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button7.grid(row=3, column=0, )

# 8
button8 = Button(root, text='8', command=lambda: number_pressed(8), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button8.grid(row=3, column=1, )

# 9
button9 = Button(root, text='9', command=lambda: number_pressed(9), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button9.grid(row=3, column=2, )

# 4
button4 = Button(root, text='4', command=lambda: number_pressed(4),  width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button4.grid(row=4, column=0, )

# 5
button5 = Button(root, text='5', command=lambda: number_pressed(5), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button5.grid(row=4, column=1, )

# 6
button6 = Button(root, text='6', command=lambda: number_pressed(6), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button6.grid(row=4, column=2, )

# 3
button1 = Button(root, text='1', command=lambda: number_pressed(1), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button1.grid(row=5, column=0, )

# 2
button2 = Button(root, text='2', command=lambda: number_pressed(2), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button2.grid(row=5, column=1, )

# 3
button3 = Button(root, text='3', command=lambda: number_pressed(3), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button3.grid(row=5, column=2, )

# 0
button0 = Button(root, text='0', command=lambda: number_pressed(0), width=4,
                 height=2, bg="gainsboro",
                 bd=3, pady=1, font=("Helvetica", 14, "bold"))
button0.grid(row=6, column=0, )

# .
button_float = Button(root, text='.', command=lambda: number_pressed('.'), width=4,
                      height=2, bg="gray70",
                      bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_float.grid(row=6, column=1)

#   Math signs
# +
button_plus = Button(root, text='+', command=lambda: math_pressed('+'), width=4,
                     height=2, bg="gray70",
                     bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_plus.grid(row=3, column=3, )

# -
button_minus = Button(root, text='-', command=lambda: math_pressed('-'), width=4,
                      height=2, bg="gray70",
                      bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_minus.grid(row=4, column=3, )

# *
button_multiply = Button(root, text='x', command=lambda: math_pressed('*'), width=4,
                         height=2, bg="gray70",
                         bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_multiply.grid(row=5, column=3, )

# /
button_division = Button(root, text='÷', command=lambda: math_pressed('/'), width=4,
                         height=2, bg="gray70",
                         bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_division.grid(row=2, column=3, )

# =
button_equal = Button(root, text='=', command=lambda: result(), width=4,
                      height=2, bg='orange',
                      bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_equal.grid(row=6, column=3, )

# %
button_percent = Button(root, text='%', command=lambda: percent(), width=4,
                        height=2, bg="gray70",
                        bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_percent.grid(row=6, column=2, )

# Del
button_delete = Button(root, text='DEL', command=lambda: remove(), width=4,
                       height=2, bg='orange',
                       bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_delete.grid(row=2, column=0, )

# CA
button_clear = Button(root, text='AC', command=lambda: clear(), width=4,
                      height=2, bg="orange",
                      bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_clear.grid(row=2, column=1, )

# raise to the power of X
button_x = Button(root, text='^', command=lambda: math_pressed('^'), width=3,
                  height=1, bg="black", fg='white',
                  bd=3, padx=2, pady=1, font=("Helvetica", 19, ))
button_x.grid(row=9, column=0, )

# negation
button_neg = Button(root, text=chr(177), command=lambda: neg(), width=4,
                  height=2, bg="gray70",
                  bd=3, pady=1, font=("Helvetica", 14, "bold"))
button_neg.grid(row=2, column=2, )

# √
button_sqrt = Button(root, text='√', command=lambda: squareroot(), width=3,
                     height=1, bg="black", fg='white',
                     bd=3, padx=2, pady=1, font=("Helvetica", 19, ))
button_sqrt.grid(row=8, column=2, )

# !
button_factorial = Button(root, text='x!', command=lambda: factorial(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_factorial.grid(row=7, column=3, )

# e
button_e = Button(root, text='e', command=lambda: e(), width=3,
                          height=1, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 19, ))
button_e.grid(row=8, column=0, )

# pi
button_pi = Button(root, text='π', command=lambda: pi(), width=3,
                          height=1, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 19, ))
button_pi.grid(row=8, column=1, )

# cuberoot
button_cuberoot = Button(root, text='∛', command=lambda: cuberoot(), width=3,
                          height=1, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 19, ))
button_cuberoot.grid(row=8, column=3, )

# mod
button_mod = Button(root, text='mod', command=lambda: math_pressed('mod'), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_mod.grid(row=7, column=2, )

# ⌈x⌉
button_ceil = Button(root, text='⌈x⌉', command=lambda: ceil(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_ceil.grid(row=7, column=1, )

# ⌊x⌋
button_floor = Button(root, text='⌊x⌋', command=lambda: floor(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_floor.grid(row=7, column=0, )

# sin
button_sin = Button(root, text='sin', command=lambda: sin(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sin.grid(row=9, column=2, )

# tan
button_tan = Button(root, text='tan', command=lambda: tan(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_tan.grid(row=9, column=3, )

# cos
button_cos = Button(root, text='cos', command=lambda: cos(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_cos.grid(row=9, column=1, )

# log
button_log = Button(root, text='log', command=lambda: log(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_log.grid(row=10, column=0, )

# log2
button_log2 = Button(root, text='log2', command=lambda: log2(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_log2.grid(row=9, column=4, )

# log10
button_log10 = Button(root, text='log10', command=lambda: log10(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_log10.grid(row=9, column=5, )

# sinh
button_sinh = Button(root, text='sinh', command=lambda: sinh(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sinh.grid(row=10, column=2, )

# tanh
button_tanh = Button(root, text='tanh', command=lambda: tanh(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_tanh.grid(row=10, column=3, )

# cosh
button_cosh = Button(root, text='cosh', command=lambda: cosh(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_cosh.grid(row=10, column=1, )

# acosh
button_acosh = Button(root, text='acosh', command=lambda: acosh(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_acosh.grid(row=9, column=6, )

# asinh
button_asinh = Button(root, text='asinh', command=lambda: asinh(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_asinh.grid(row=10, column=6, )

# exp
button_exp = Button(root, text='exp', command=lambda: exp(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_exp.grid(row=10, column=4, )

# exp2
button_exp = Button(root, text='exp2', command=lambda: exp2(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_exp.grid(row=10, column=5, )

# logₐ(x)
button_log = Button(root, text='logₐ(x)', command=lambda: math_pressed('log'), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2,  pady=5, font=("Helvetica", 11, "bold"))
button_log.grid(row=5, column=6, )

# a b⁄c
button_mixfrac = Button(root, text='a b⁄c', command=lambda: mixfraction(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=5, font=("Helvetica", 11, "bold"))
button_mixfrac.grid(row=5, column=5, )

# power rule
button_powrule = Button(root, text='aᵇᶜ', command=lambda: powrule(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=5, font=("Helvetica", 11, "bold"))
button_powrule.grid(row=5, column=4, )

# sigma
button_sigma = Button(root, text='∑ₐᵇc', command=lambda: sigma(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=5, font=("Helvetica", 11, "bold"))
button_sigma.grid(row=6, column=4, )

# x⁻ⁿ
button_negpow = Button(root, text='x⁻ⁿ', command=lambda: math_pressed('x⁻ⁿ'), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=5, font=("Helvetica", 11, "bold"))
button_negpow.grid(row=6, column=5, )

# aᵇ∕ᶜ
button_fraction = Button(root, text='aᵇ∕ᶜ', command=lambda: fraction(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=5, font=("Helvetica", 11, "bold"))
button_fraction.grid(row=6, column=6, )

# sigma ∑ₓᵇ∑ₐᵇxᵃ
button_sigma1 = Button(root, text='∑ₐᵇxᵃ', command=lambda: sigma1(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sigma1.grid(row=7, column=5, )

# sigma ∑ₓᵇ∑ₐᵇcᵃ
button_sigma2= Button(root, text='∑ₐᵇcᵃ', command=lambda: sigma2(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sigma2.grid(row=7, column=4, )

# sigma ∑ₓᵇ∑ₐᵇcˣ
button_sigma3 = Button(root, text='∑ₐᵇcˣ', command=lambda: sigma3(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sigma3.grid(row=7, column=6, )

# sigma ∑ₓᵇ∑ₐᵇaˣ
button_sigma4 = Button(root, text='∑ₐᵇaˣ', command=lambda: sigma4(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sigma4.grid(row=8, column=5, )

# sigma ∑ₓᵇ∑ₐᵇa
button_sigma5 = Button(root, text='∑ₐᵇx', command=lambda: sigma5(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sigma5.grid(row=8, column=4, )

# sigma ∑ₓᵇ∑ₐᵇx
button_sigma6 = Button(root, text='∑ₐᵇa', command=lambda: sigma6(), width=5,
                          height=2, bg="black", fg='white',
                          bd=3, padx=2, pady=1, font=("Helvetica", 11, "bold"))
button_sigma6.grid(row=8, column=6, )

btnA = Entry(root, textvariable=A, font=("Verdana", 15, ), bg="black", fg='white', bd = 10,
                    insertwidth=4, width=7, justify=LEFT)
btnA.grid(row=2, column=5, columnspan=2)

btnB = Entry(root, textvariable=B, font=("Verdana", 15, ), bg="black", fg='white',  bd = 10,
                    insertwidth=4, width=7, justify=LEFT)
btnB.grid(row=3, column=5, columnspan=2)

btnC = Entry(root, textvariable=C, font=("Verdana", 15, ), bg="black", fg='white', bd = 10,
                    insertwidth=4, width=7, justify=LEFT)
btnC.grid(row=4, column=5, columnspan=2)

# A btn
lblDisplayA = Button(root, text="A=", command=lambda: buttonA(), width=3,
                    height=1, font=('Bauhaus 93', 20, ),
                    bg='black', fg='white', justify=CENTER)
lblDisplayA.grid(row=2, column=4)

# B btn
lblDisplayB = Button(root, text="B=", command=lambda: buttonB(), width=3,
                    height=1, font=('Bauhaus 93', 20, ),
                    bg='black', fg='white', justify=CENTER)
lblDisplayB.grid(row=3, column=4)

# C btn
lblDisplayC = Button(root, text="C=", command=lambda: buttonC(), width=3,
                    height=1, font=('Bauhaus 93', 20, ),
                   bg='black', fg='white', justify=CENTER)
lblDisplayC.grid(row=4, column=4)

lblDisplay = Label(root, text="B5TA",
                   font=('Bauhaus 93', 60, 'bold'),
                   bg='black', fg='white', justify=CENTER)
lblDisplay.grid(row=1, column=9, rowspan=2, columnspan=3)

his1 = Entry(root, textvariable=history1, font=("Verdana", 15, ), bg="black", fg='white', bd = 10,
                    insertwidth=4, width=30, justify=LEFT)
his1.grid(row=3, column=7, columnspan=7)

#photo = PhotoImage(file="Desktop/logo.jpg")
#label = Label(root, image=photo, width=300, height= 150, bg = "black", fg = "yellow")

menubar = Menu(calc)
def iExit():
    root.destroy()
    return
def calHistory():
    root.resizable(width=False, height=False)
    root.geometry("835x600+500+90")
def closehistory():
    root.resizable(width=False, height=False)
    root.geometry("417x600+500+90")
# ManuBar 1 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='More', menu=filemenu)
filemenu.add_command(label="History", command=calHistory)
filemenu.add_command(label="Standard", command=closehistory)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)


root.config(menu=menubar)
root.mainloop()