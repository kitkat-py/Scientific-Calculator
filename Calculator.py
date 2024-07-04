from tkinter import * # importa il modulo per manipolare elementi dell'interfaccia grafica

def premi_btn(num): # definisce la funzione per trasformare l'input dei bottoni dei numeri in testo; "num" è un parametro
    global equazione_testo # una variabile globale può essere manovrata nella funzione
    global testo
    equazione_testo += str(num) # converte in stringa il parametro (num) che ottiene, che siano o meno degli integrali (necessario per mostrare il testo)
    testo += str(num) # aggiunge al testo il parametro inserito
    equazione_etichetta.set(testo) # il testo dell'etichetta corrisponde ai numeri premuti

def premi_sym(sym): # definisce la funzione per trasformare l'input dei bottoni dei simboli in testo
    global equazione_testo
    global testo
    global testo_piccolo
    equazione_testo += str(sym) # aggiunge il simbolo all'equazione
    testo_piccolo = equazione_testo # per aggiornare il piccolo testo in alto
    equazione_etichetta.set("") # elimina il testo sotto
    testo_eticchetta.set(testo_piccolo) # aggiorna il testo piccolo in alto
    testo = "" # elimina il testo grande che c'era

def btn_delete(): # definisce la funzione per rimuovere l'ultimo elemento inserito
    global equazione_testo
    global testo
    testo = testo[:-1] # rimuove l'ultimo elemento dell'equazione
    equazione_testo = testo_piccolo + testo # aggiorna l'equazione
    equazione_etichetta.set(testo) # applica la modifica anche al testo mostrato

def check(): # funzione per modificare il risultato e mostrarlo
    global equazione_testo
    global risultato
    global testo_piccolo
    if risultato.__contains__("j"): # j è usato per indicare la parte immaginaria dei numeri complessi in python: per evitare di ottenere come risultato un numero complesso, controlla se è presente la j nel risultato
        equazione_etichetta.set("Numeri complessi") # in caso il risultato sia un numero complesso, dà errore
        equazione_testo = ""
        testo_piccolo = ""
    else:
        if risultato.__contains__("e"): # in caso il risultato sia già scritto come potenza di 10
            risultato = list(risultato)
            potenza = risultato.index("e") # trova l'index della potenza di 10
            risultato[potenza] = "x10^" # trasforma "e" in "x10^"
            if risultato[-2] == "0" and int(len(risultato[potenza:])) == 4: # controlla se il penultimo numero della potenza è 0 e se ci sono quattro cifre dalla potenza in poi 
                risultato.pop(-2) # in tal caso lo elimina (per evitare che compaiano potenze come "^03")
            if potenza == 1: # se non ci sono i decimali, li aggiunge
                risultato.insert(1, ".")
                risultato.insert(2, "0")
                risultato.insert(3, "0")
            if potenza == 3: # se manca il secondo decimale, lo aggiunge
                risultato.insert(3, "0")
            if len(risultato[2:potenza]) > 2 and risultato[0] != "-": # controlla se il decimale ha più di due numeri dopo la virgola
                del risultato[4:(potenza)] # elimina le cifre tra il terzo decimale e l'ultimo (che ha l'index di "e" diminuito di 1: l'indicazione "da:a" non comprende l'ultimo elemento) 
            elif len(risultato[3:potenza]) > 2:
                del risultato[5:(potenza)]
            if risultato.__contains__("+"): # non mostra il + dell'elevazione a potenza positiva
                segno = risultato.index("+")
                risultato.pop(segno)
            risultato = "".join(risultato) # trasforma la lista in stringa
        elif float(risultato) >= 100000000 or float(risultato) <= -100000000: # controlla se il risultato è maggiore o uguale a 100000000 opure se è minore o uguale a -100000000
            if float(risultato).is_integer(): # controlla se il risultato è un numero intero
                risultato = list(risultato) # trasforma la stringa in una lista
                if risultato.__contains__("."): # in caso il risultato sia scritto in forma n.0
                    del risultato[-2:] # elimina .0
            elif float(risultato) > 0: # se invece non è un numero intero, considera solo gli elementi prima del punto, quindi prima dei decimali
                risultato = list(risultato)
                decimali = risultato.index(".") # trova l'index del punto
                del risultato[decimali:] # elimina dalla lista tutti gli elementi dal punto in poi
            numero = 1 # pone inizialmente che il numero è positivo
            if risultato.__contains__("-"): # controlla se il numero è negativo
                risultato.pop(0) # rimuove il meno
                numero = -1 # cambia la variabile in un numero negativo
            if int(risultato[3]) > 5: # se la cifra successiva a quella da approssimare è maggiore di 5, allora procedi
                if int(risultato[2]) != 9: # se la cifra da approssimare è diversa da 9
                    risultato[2] = int(risultato[2]) + 1 # aumenta il valore della cifra da approssimare di 1
                elif int(risultato[1]) != 9: # se la cifra prima di quella da approssimare è diversa da 9
                    risultato[2] = "0" # la cifra da approssimare è uguale a 0
                    risultato[1] = int(risultato[1]) + 1 # aumenta il valore della cifra prima di quella da approssimare di 1
                elif int(risultato[0]) != 9:
                    risultato[2] = "0"
                    risultato[1] = "0"
                    risultato[0] = int(risultato[0]) + 1
                else: # nel caso tutte le cifre prima di quella da approssimare siano uguali a 9
                    risultato[2] = "0"
                    risultato[1] = "0"
                    risultato[0] = "0"
                    risultato.insert(0, "1") # aggiunge la cifra all'inizio della lista, quindi aggiunge un 1 all'inizio del numero
            risultato = str(risultato[0]) + "." + str(risultato[1]) + str(risultato[2]) + "x10^" + str(len(risultato)-1) # riscrive il numero come potenza di 10
            if numero < 0: # se il numero iniziale è negativo
                risultato = "-" + risultato # allora aggiunge un meno all'inizio
        elif float(risultato).is_integer(): # controlla se il risultato è un numero intero
            pass
        elif (float(risultato) >= 1 or float(risultato) <= -1) and len(risultato[(risultato.index(".") - 1):]) > 10: # controlla che il numero abbia più di 10 cifre e che sia maggiore-uguale a 1 oppure minore-uguale a -1
            numero = 1 # pone inizialmente che il numero è positivo
            if risultato.__contains__("-"): # controlla se il numero è negativo
                risultato = list(risultato)
                risultato.pop(0) # rimuove il meno
                risultato = "".join(risultato) # converte la lista in stringa
                numero = -1 # cambia la variabile in un numero negativo
            if int(risultato[11]) > 5 and int(risultato[10]) != 9: # controlla che la cifra da approssimare sia diversa da 9 e che quella dopo sia maggiore di 5
                risultato = list(risultato) # converte la stringa del risultato in lista per poterne manipolare gli elementi
                risultato[10] = str(int(risultato[10]) + 1) # la cifra da approssimare aumenta il suo valore di 1
                risultato = "".join(risultato)
            risultato = risultato[:11] # tronca il risultato
            if numero < 0: # se il numero iniziale è negativo
                risultato = "-" + risultato  # allora aggiunge un meno all'inizio
        elif 0.95 < float(risultato) < 1:
            risultato = 1.0
        elif -1 < float(risultato) < -0.95:
            risultato = -1.0
        elif -1 < float(risultato) < 1 and float(risultato) != 0: # se il risultato è compreso tra 1 e -1 ma diverso da 0
            risultato = list(risultato)
            numero = 1 # pone inizialmente che il numero è positivo
            if risultato[0] == "-": # controlla se il numero è negativo
                risultato.pop(0) # rimuove il meno
                numero = -1 # cambia la variabile in un numero negativo
            del risultato[:2] # elimina "0."
            cifra = next((index for index, value in enumerate(risultato) if value != "0"), None) # trova l'index della prima cifra diversa da 0
            if len(risultato[cifra:]) >= 5: # controlla che dopo la prima cifra diversa da zero ci siano almeno 4 cifre
                del risultato[(cifra + 4):] # elimina dalla quarta cifra dopo quella diversa da 0 in poi
            if len(risultato[cifra:]) == 4: # controlla che ci siano esattamente 4 cifre a partire dalla prima cifra diversa da 0
                if int(risultato[cifra + 3]) > 5: # se la cifra successiva a quella da approssimare è maggiore di 5, allora procedi
                    if int(risultato[cifra + 2]) != 9: # se la cifra da approssimare è diversa da 9
                        risultato[cifra + 2] = int(risultato[cifra + 2]) + 1 # aumenta il valore della cifra da approssimare di 1
                    elif int(risultato[cifra + 1]) != 9: # se la cifra prima di quella da approssimare è diversa da 9
                        risultato[cifra + 2] = "0" # la cifra da approssimare è uguale a 0
                        risultato[cifra + 1] = int(risultato[cifra + 1]) + 1 # aumenta il valore della cifra prima di quella da approssimare di 1
                    elif int(risultato[cifra]) != 9:
                        risultato[cifra + 2] = "0"
                        risultato[cifra + 1] = "0"
                        risultato[cifra] = int(risultato[cifra]) + 1
                    else: # nel caso in cui tutte le cifre prima di quella da approssimare siano uguali a 9
                        risultato[cifra + 3] = "0"
                        risultato[cifra + 2] = "0"
                        risultato[cifra + 1] = "0"
                        risultato[cifra] = "0"
                        risultato.insert((cifra - 1), "1") # aggiunge la cifra all'inizio della lista, quindi aggiunge un 1 all'inizio del numero
                        cifra -= 1 # index dell'1 appena aggiunto, cioè un numero in meno a prima
                        del risultato[(cifra + 4):] # elimina l'ultima cifra del numero
                risultato = str(risultato[cifra]) + "." + str(risultato[cifra + 1]) + str(risultato[cifra + 2]) + "x10^-" + str(len(risultato)-3) # mostra il risultato come potenza di 10
            elif len(risultato[cifra:]) == 3:
                risultato = str(risultato[cifra]) + "." + str(risultato[cifra + 1]) + str(risultato[cifra + 2]) + "x10^-" + str(len(risultato)-2)
            elif len(risultato[cifra:]) == 2:
                risultato = str(risultato[cifra]) + "." + str(risultato[cifra + 1]) + "0x10^-" + str(len(risultato)-1)
            else:
                risultato = str(risultato[cifra]) + ".00x10^-" + str(len(risultato))
            if numero < 0: # se il numero iniziale è negativo
                risultato = "-" + risultato # allora aggiunge un meno all'inizio
        equazione_etichetta.set(risultato)
        testo_eticchetta.set(equazione_testo) # testo piccolo in alto aggiornato
        equazione_testo = risultato # per riutilizzare il risultato
        testo_piccolo = ""

def uguale(): # definisce la funzione per l'uguale
    global equazione_testo
    global risultato
    global testo_piccolo
    try: # serve ad evitare errori
        risultato = str(eval(equazione_testo.replace("x", "*").replace("÷", "/").replace("^", "**"))) # eval (sta per evaluation) analizza l'equazione che gli viene presentata
        check() # richiama la funzione per sistemare il risultato
    except ZeroDivisionError: # se c'è un'eccezione in "try" allora le stringhe di codice di "except" vengono eseguite
        equazione_etichetta.set("Arithmetic error") # fa apparire l'avvertimento di errore
        equazione_testo = ""
        testo_piccolo = ""
    except SyntaxError:
        equazione_etichetta.set("Syntax error") # fa apparire l'avvertimento di errore
        equazione_testo = ""
        testo_piccolo = ""

def radice_quadrata(): # definisce la funzione per fare la radice quadrata di un numero
    global equazione_testo
    global testo_piccolo
    global risultato
    try:
        risultato = str(eval(equazione_testo.replace("x", "*").replace("÷", "/").replace("^", "**")+'**(1/2)')) # fa la radice del numero che gli viene posto davanti
        check()
    except ZeroDivisionError:
        equazione_etichetta.set("Arithmetic error")
        equazione_testo = ""
        testo_piccolo = ""
    except SyntaxError:
        equazione_etichetta.set("Syntax error")
        equazione_testo = ""
        testo_piccolo = ""

def rimuovi(): # cancella il testo presente nella casella di testo
    global equazione_testo
    global testo
    equazione_etichetta.set("")
    testo_eticchetta.set("")
    equazione_testo = ""
    testo = ""

finestra = Tk() # GUI (Graphical User Interface); crea l'oggetto finestra
finestra.geometry("420x710") # definisce le dimensioni della finestra in pixel
finestra.config(bg="black") # cambia il colore dello sfondo della finestra
finestra.title("Calcolatrice di Kat") # nome della finestra
finestra.resizable(False, False) # impedisce di modificare la grandezza della finestra per le assi X e Y
finestra.iconbitmap("calc-icon.ico") # icona della finestra

equazione_testo = "" # stringa basica di calcolo; all'inizio appare vuota
risultato = "" # per il pulsante Ans; cambia in base al risultato dell'equazione precedente
testo = "" # testo che appare più grande
testo_piccolo = "" # testo nella parte in alto

testo_eticchetta = StringVar() # l'etichetta (label) serve a visualizzare un'immagine o un testo con cui l'utente non interagisce
etic = Label(finestra, textvariable=testo_eticchetta, font=("Arial", 20), bg="black", width=23, height=1, anchor="se", fg="white") # aggiunge l'etichetta alla finestra, definisce il testo, aggiunge un colore per lo sfondo
etic.pack(pady=(25, 0)) # la funzione pack() organizza i widget in blocchi

equazione_etichetta = StringVar()
etichetta = Label(finestra, textvariable=equazione_etichetta, font=("Arial", 30), bg="black", width=16, height=1, anchor="se", fg="white")
etichetta.pack()

frame = Frame(finestra) # serve a suddividere la finestra: qui andranno i bottoni
frame.config(bg="black")
frame.pack()

# immagini dei bottoni
btn_num = PhotoImage(file="btn_num.png")
btn_func = PhotoImage(file="btn_func.png")
btn_sym = PhotoImage(file="btn_sym.png")
btn_zero = PhotoImage(file="btn_0.png")

# serie di bottoni per i numeri
btn_1 = Button(frame, compound="center", text=1, font=("Arial", 20), fg="white", image=btn_num, command=lambda: premi_btn(1), bg="#000000", activebackground="black", activeforeground="white", border="0") # lambda si riferisce alla funzione senza richiamarla immediatamente
btn_1.grid(row=4, column=0, pady=(0, 10), padx=(0, 10)) # grid() serve a posizionare il bottone nel frame
btn_2 = Button(frame, compound="center", text=2, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(2), fg="white", border="0")
btn_2.grid(row=4, column=1, pady=(0, 10), padx=(0, 10))
btn_3 = Button(frame, compound="center", text=3, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20),  command=lambda: premi_btn(3), fg="white", border="0")
btn_3.grid(row=4, column=2, pady=(0, 10), padx=(0, 10))
btn_4 = Button(frame, compound="center", text=4, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(4), fg="white", border="0")
btn_4.grid(row=3, column=0, pady=(0, 10), padx=(0, 10))
btn_5 = Button(frame, compound="center", text=5, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(5), fg="white", border="0")
btn_5.grid(row=3, column=1, pady=(0, 10), padx=(0, 10))
btn_6 = Button(frame, compound="center", text=6, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(6), fg="white", border="0")
btn_6.grid(row=3, column=2, pady=(0, 10), padx=(0, 10))
btn_7 = Button(frame, compound="center", text=7, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(7), fg="white", border="0")
btn_7.grid(row=2, column=0, pady=(0, 10), padx=(0, 10))
btn_8 = Button(frame, compound="center", text=8, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(8), fg="white", border="0")
btn_8.grid(row=2, column=1, pady=(0, 10), padx=(0, 10))
btn_9 = Button(frame, compound="center", text=9, image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(9), fg="white", border="0")
btn_9.grid(row=2, column=2, pady=(0, 10), padx=(0, 10))
btn_0 = Button(frame, compound="center", text=0, image=btn_zero, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn(0), fg="white", border="0")
btn_0.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=(0, 10))

# serie di bottoni per i simboli
btn_più = Button(frame, text="+", compound="center", image=btn_sym, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_sym("+"), fg="white", border="0")
btn_più.grid(row=4, column=3, pady=(0, 10))
btn_meno = Button(frame, text="-", compound="center", image=btn_sym, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_sym("-"), fg="white", border="0")
btn_meno.grid(row=3, column=3, pady=(0, 10))
btn_per = Button(frame, text="x", compound="center", image=btn_sym, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_sym("x"), fg="white", border="0")
btn_per.grid(row=2, column=3, pady=(0, 10))
btn_div = Button(frame, text="÷", compound="center", image=btn_sym, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_sym("÷"), fg="white", border="0")
btn_div.grid(row=1, column=3, pady=(0, 10))
btn_uguale = Button(frame, text="=", compound="center", image=btn_sym, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=uguale, fg="white", border="0")
btn_uguale.grid(row=5, column=3)
btn_decimali = Button(frame, text=".", compound="center", image=btn_num, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=lambda: premi_btn("."), fg="white", border="0")
btn_decimali.grid(row=5, column=2, padx=(0, 10))
btn_rimuovi = Button(frame, text="C", compound="center", image=btn_func, bg="#000000", activebackground="black", activeforeground="black", font=("Arial", 20), command=rimuovi, fg="black", border="0")
btn_rimuovi.grid(row=0, column=0, pady=(15, 10), padx=(0, 10))
btn_potenza = Button(frame, text="xⁿ", compound="center", image=btn_func, bg="#000000", activebackground="black", activeforeground="black", font=("Arial", 20), command=lambda: premi_sym("^"), fg="black", border="0")
btn_potenza.grid(row=0, column=2, pady=(15, 10), padx=(0, 10))
btn_aperta = Button(frame, text="(", compound="center", image=btn_func, bg="#000000", activebackground="black", activeforeground="black", font=("Arial", 20), command=lambda: premi_sym("("), fg="black", border="0")
btn_aperta.grid(row=1, column=1, pady=(0, 10), padx=(0, 10))
btn_chiusa = Button(frame, text=")", compound="center", image=btn_func, bg="#000000", activebackground="black", activeforeground="black", font=("Arial", 20), command=lambda: premi_sym(")"), fg="black", border="0")
btn_chiusa.grid(row=1, column=2, pady=(0, 10), padx=(0, 10))
btn_del = Button(frame, text="⌫", compound="center", image=btn_sym, bg="#000000", activebackground="black", activeforeground="white", font=("Arial", 20), command=btn_delete, fg="white", border="0")
btn_del.grid(row=0, column=3, pady=(15, 10))
btn_rad = Button(frame, text="\u221A(x)", compound="center", image=btn_func, bg="#000000", activebackground="black", activeforeground="black", font=("Arial", 20), command=radice_quadrata, fg="black", border="0")
btn_rad.grid(row=0, column=1, pady=(15, 10), padx=(0, 10))
btn_ans = Button(frame, text="Ans", compound="center", image=btn_func, bg="#000000", activebackground="black", activeforeground="black", font=("Arial", 20), command=lambda: premi_btn(risultato), fg="black", border="0")
btn_ans.grid(row=1, column=0, pady=(0, 10), padx=(0, 10))

# input della tastiera
finestra.bind("1", lambda x: premi_btn(1))
finestra.bind("2", lambda x: premi_btn(2))
finestra.bind("3", lambda x: premi_btn(3))
finestra.bind("4", lambda x: premi_btn(4))
finestra.bind("5", lambda x: premi_btn(5))
finestra.bind("6", lambda x: premi_btn(6))
finestra.bind("7", lambda x: premi_btn(7))
finestra.bind("8", lambda x: premi_btn(8))
finestra.bind("9", lambda x: premi_btn(9))
finestra.bind("0", lambda x: premi_btn(0))
finestra.bind("+", lambda x: premi_sym("+"))
finestra.bind("-", lambda x: premi_sym("-"))
finestra.bind("*", lambda x: premi_sym("x"))
finestra.bind(":", lambda x: premi_sym("÷"))
finestra.bind("<Return>", lambda x: uguale()) # <Return> indica il tasto Enter
finestra.bind(".", lambda x: premi_btn("."))
finestra.bind("<Delete>", lambda x: rimuovi()) # <Delete> indica il tasto "canc"
finestra.bind("^", lambda x: premi_sym("^"))
finestra.bind("(", lambda x: premi_sym("("))
finestra.bind(")", lambda x: premi_sym(")"))
finestra.bind("<BackSpace>", lambda x: btn_delete())
finestra.bind("v", lambda x: radice_quadrata())
finestra.bind("V", lambda x: radice_quadrata())
finestra.bind("=", lambda x: premi_btn(risultato))

finestra.mainloop() # loop per tenere aperta la finestra fino a che non viene chiusa