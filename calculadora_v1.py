import tkinter as tk

win = tk.Tk()

win.title("Caculation")
win.geometry("235x235")
win.resizable(False,False)



#botoes
valor_digitado = tk.StringVar(win)
total_resultado = 0
temp = 0

somar = False
subtrair = False
dividir = False
multiplicar = False
def actionButton(valor):
    global total_resultado,temp,somar, subtrair,dividir, multiplicar
    
    if valor == "+":
       if total_resultado == 0:
            total_resultado = temp
       somar = True
       valor_digitado.set("")
       temp = 0
    elif valor =="-":
        if total_resultado == 0:
            total_resultado = temp
        subtrair = True
        valor_digitado.set("")
        temp = 0
    elif valor =="*":
        if total_resultado == 0:
            total_resultado = temp
        multiplicar = True
        valor_digitado.set("")
        temp = 0
    elif valor == "/":
        if total_resultado == 0:
            total_resultado = temp
        dividir = True
        valor_digitado.set("")
        temp = 0
    else:
        temp = ( temp * 10 ) + int(valor)
        valor_digitado.set(str(temp))

def actionCalc():
    global total_resultado,temp, somar,subtrair,multiplicar,dividir

    if somar == True:
        total_resultado += int(valor_digitado.get())
       
        valor_digitado.set(str(total_resultado))

    elif subtrair == True:
        total_resultado -= int(temp)
        valor_digitado.set(str(total_resultado))
    
    elif multiplicar == True:
        total_resultado *= int(temp)
        valor_digitado.set(str(total_resultado)) 

    elif dividir == True:
        total_resultado /= int(temp)
        valor_digitado.set(str(total_resultado))

   
    somar =False
    multiplicar = False
    subtrair = False
    dividir = False

field = tk.Entry(win, textvariable=valor_digitado)

b9 = tk.Button(win,text="7", width=3, height=2,command=lambda:actionButton("7"))
b8 = tk.Button(win,text="8", width=3, height=2,command=lambda:actionButton("8"))
b7 = tk.Button(win,text="9", width=3, height=2,command=lambda:actionButton("9"))
b6 = tk.Button(win,text="4", width=3, height=2,command=lambda:actionButton("4"))
b5 = tk.Button(win,text="5", width=3, height=2,command=lambda:actionButton("5"))
b4 = tk.Button(win,text="6", width=3, height=2,command=lambda:actionButton("6"))
b3 = tk.Button(win,text="1", width=3, height=2,command=lambda:actionButton("1"))
b2 = tk.Button(win,text="2", width=3, height=2,command=lambda:actionButton("2"))
b1 = tk.Button(win,text="3", width=3, height=2,command=lambda:actionButton("3"))
b0 = tk.Button(win,text="0", width=10, height=2,command=lambda:actionButton("0"))
mais = tk.Button(win,text="+", command=lambda:actionButton("+"),width=3, height=2)
menos = tk.Button(win,text="-", command=lambda:actionButton("-"),width=3, height=2)
mult = tk.Button(win,text="*", command=lambda:actionButton("*"),width=3, height=2)
div = tk.Button(win,text="/", command=lambda:actionButton("/"),width=3, height=2)
igual = tk.Button(win, text="=", width=3, height=2, command=actionCalc)

field.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
b7.grid(row=1,column=0,padx=2)
b8.grid(row=1,column=1,padx=2)
b9.grid(row=1,column=2,padx=2)
div.grid(row=1,column=3,padx=2)
b4.grid(row=2,column=0,padx=2)
b5.grid(row=2,column=1,padx=2)
b6.grid(row=2,column=2,padx=2)
mult.grid(row=2,column=3,padx=2)
b1.grid(row=3,column=0,padx=2)
b2.grid(row=3,column=1,padx=2)
b3.grid(row=3,column=2,padx=2)
menos.grid(row=3, column=3,padx=2)
b0.grid(row=4,column=0, columnspan=2,padx=2)
mais.grid(row=4,column=3,padx=2)
igual.grid(row=4,column=2,padx=2)
#operacoes

win.mainloop()