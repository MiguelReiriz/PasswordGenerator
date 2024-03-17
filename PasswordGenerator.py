from tkinter import *
import tkinter as tk
import random
import string #Import para cadenas de caracteres


Letters = string.ascii_letters
Digits = string.digits
Puntuation = string.punctuation

caracteres = string.ascii_letters + string.digits + string.punctuation

def lettersPassword(longitud):

    contrasena = ''.join(random.choice(Letters) for i in range(longitud))
    return contrasena

def digitsPassword(longitud):
    contrasena = ''.join(random.choice(Digits) for i in range(longitud))
    return contrasena

def lettersDigitsPassword(longitud):
    contrasena = ''.join(random.choice(Letters + Digits) for i in range(longitud))
    return contrasena


# Crear contrasena compuesto de letras min y may, numeros y signos, Seleccionados de forma aleatoria por random.choice y dependiendo del numero de caracteres(longitud)
def completePassword(longitud):
     contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
     return contrasena

def generar_y_mostrar_contrasena():
    longitud = entry_longitud.get()

    ValorVariableLetters =   Variablecontrol1.get()
    
    ValorVariableDigits =   VariablecontrolDigits.get()

    ValorVariablePuntuation = VariablecontrolPuntuation.get()

    if longitud.isdigit():
        longitud = int(longitud)
        if ValorVariableLetters == True and ValorVariableDigits == False and ValorVariablePuntuation == False:
            lettersPassword(longitud)
            contrasena_generada = lettersPassword(longitud)
        elif ValorVariableDigits == True and ValorVariableLetters == False and ValorVariablePuntuation == False:
            digitsPassword(longitud)
            contrasena_generada = digitsPassword(longitud)
        elif ValorVariableDigits == True and ValorVariableLetters == True and ValorVariablePuntuation == False:
            lettersDigitsPassword(longitud)
            contrasena_generada = lettersDigitsPassword(longitud)
        elif ValorVariableDigits == False and ValorVariableLetters == False and ValorVariablePuntuation == False:
            completePassword(longitud)
            contrasena_generada = completePassword(longitud)

        elif ValorVariableDigits == False and ValorVariableLetters == True and ValorVariablePuntuation == True:
            contrasena_generada = ''.join(random.choice(Letters + Puntuation) for i in range(longitud))
        elif ValorVariableDigits == True and ValorVariableLetters == False and ValorVariablePuntuation == True:
            contrasena_generada = ''.join(random.choice(Digits + Puntuation) for i in range(longitud))  

        elif ValorVariableDigits == False and ValorVariableLetters == False and ValorVariablePuntuation == True:
            label_contrasena.config(text="Marca alguna casilla mas")
        
        elif ValorVariableDigits == True and ValorVariableLetters == True and ValorVariablePuntuation == True:
            completePassword(longitud)
            contrasena_generada = completePassword(longitud)
        
        label_contrasena.config(text="Password Generated: " + contrasena_generada)
    else:
        label_contrasena.config(text="Invalid input. Please enter a valid number for password length.")




# Crear la ventana principal
ventana = Tk()
ventana.title("Safe Password Generator")
ventana.maxsize(350,250)
ventana.minsize(350,250)
# Crear y colocar los widgets
label_longitud = tk.Label(ventana, text="Longitud de la contrasena:")
label_longitud.grid(row=0, column=0, padx=10, pady=10)

entry_longitud = tk.Entry(ventana)
entry_longitud.grid(row=0, column=1, padx=10, pady=10)

#Variable de contorl
Variablecontrol1 = BooleanVar()
Variablecontrol1.set(False)

VariablecontrolDigits = BooleanVar()
VariablecontrolDigits.set(False)

VariablecontrolPuntuation = BooleanVar()
VariablecontrolPuntuation.set(False)

#Creacion boton Letters
#onvalue=True / offvalue=False
# sticky=W Centra el boton en su celda (N, E, S, W, NE, NW, SE, and SW)

checkbutton_letters = Checkbutton(ventana, text="Letters ",  variable=Variablecontrol1, onvalue= True, offvalue=False)
checkbutton_letters.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky=W)

checkbutton_digits = Checkbutton(ventana, text="Digits",variable=VariablecontrolDigits, onvalue= True, offvalue= False)
checkbutton_digits.grid(row=2, column=0, columnspan=1, padx=10, pady=10,sticky=W)

checkbutton_punctuation = Checkbutton(ventana, text="Punctuation",variable=VariablecontrolPuntuation, onvalue= True, offvalue= False)
checkbutton_punctuation.grid(row=3, column=0, columnspan=1, padx=10, pady=10,sticky=W)

boton_generar = Button(ventana, text="Generate Password", command=generar_y_mostrar_contrasena)
boton_generar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)



label_contrasena = Label(ventana, text="")
label_contrasena.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar el bucle principal
ventana.mainloop()