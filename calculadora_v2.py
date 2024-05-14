import tkinter as tk

win = tk.Tk()

#configurações gerais
win.title("Calculadora")
win.geometry("240x240")
win.resizable(False,False)
valor_digitado = tk.StringVar(win)
first_result=0
second_result=0
valor_total = 0 

def actionButtonValues(valor):
    if(valor!="="):
        total_caracter = valor_digitado.get() + valor
        valor_digitado.set(total_caracter)
    else:
        try:
            valor_digitado.set(f"{float(eval(valor_digitado.get()))}")
        except Exception:
            valor_digitado.set("Operação Incorreta")

        

field = tk.Entry(win, textvariable=valor_digitado,justify="right")


b9 = tk.Button(win,text="9", width=3, height=2,command=lambda:actionButtonValues("9"))
b8 = tk.Button(win,text="8", width=3, height=2,command=lambda:actionButtonValues("8"))
b7 = tk.Button(win,text="7", width=3, height=2,command=lambda:actionButtonValues("7"))
b6 = tk.Button(win,text="6", width=3, height=2,command=lambda:actionButtonValues("6"))
b5 = tk.Button(win,text="5", width=3, height=2,command=lambda:actionButtonValues("5"))
b4 = tk.Button(win,text="4", width=3, height=2,command=lambda:actionButtonValues("4"))
b3 = tk.Button(win,text="3", width=3, height=2,command=lambda:actionButtonValues("3"))
b2 = tk.Button(win,text="2", width=3, height=2,command=lambda:actionButtonValues("2"))
b1 = tk.Button(win,text="1", width=3, height=2,command=lambda:actionButtonValues("1"))
b0 = tk.Button(win,text="0", width=10, height=2,command=lambda:actionButtonValues("0"))

mais = tk.Button(win,text="+", command=lambda:actionButtonValues("+"),width=3, height=2)
menos = tk.Button(win,text="-", command=lambda:actionButtonValues("-"),width=3, height=2)
mult = tk.Button(win,text="*", command=lambda:actionButtonValues("*"),width=3, height=2)
div = tk.Button(win,text="/", command=lambda: actionButtonValues("/"),width=3, height=2)
igual = tk.Button(win, text="=", width=3, height=2,command=lambda: actionButtonValues("="))

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

win.mainloop()