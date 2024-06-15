from tkinter import *

# Funções para operações matemáticas
def limpar_tela():
    tela.delete(0, END)

def adicao():
    global num1
    global operador
    num = float(tela.get())
    operador = "+"
    num1 = num
    limpar_tela()

def subtracao():
    global num1
    global operador
    num = float(tela.get())
    operador = "-"
    num1 = num
    limpar_tela()

def multiplicacao():
    global num1
    global operador
    num = float(tela.get())
    operador = "*"
    num1 = num
    limpar_tela()

def divisao():
    global num1
    global operador
    num = float(tela.get())
    operador = "/"
    num1 = num
    limpar_tela()

def porcentagem():
    num = float(tela.get())
    result = num / 100
    limpar_tela()
    tela.insert(END, str(result))

def igual():
    global num1
    num2 = float(tela.get())
    limpar_tela()
    if operador == "+":
        tela.insert(END, str(num1 + num2))
    elif operador == "-":
        tela.insert(END, str(num1 - num2))
    elif operador == "*":
        tela.insert(END, str(num1 * num2))
    elif operador == "/":
        if num2 == 0:
            tela.insert(END, "Erro: Divisão por zero!")
        else:
            tela.insert(END, str(num1 / num2))

# Configurando a janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")

# Definindo cores
cor1= "#2c2e2d" #preto fosco
cor2= "#feffff" #branco
cor3= "#38576b" #Azul carregado
cor4= "#ECEFF1" #cinza
cor5= "#FFAB40" #LARANJA

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=310)
frame_corpo.grid(row=1, column=0)

# Tela da calculadora
tela = Entry(frame_tela, font=("Arial", 20))
tela.grid(row=0, column=0, columnspan=4)

# Criando botões
b_1 = Button(frame_corpo, text="C", width=10, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=limpar_tela)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=divisao)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "7"))
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "8"))
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "9"))
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=multiplicacao)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "4"))
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "5"))
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "6"))
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=subtracao)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "1"))
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "2"))
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, text="3", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "3"))
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=adicao)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "0"))
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor4, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: tela.insert(END, "."))
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE, command=igual)
b_18.place(x=177, y=208)

janela.mainloop()