import random
from collections import defaultdict


# Scrivi una funzione che prenda un dizionario e un valore, 
# e ritorni la prima chiave che corrisponde a quel valore, 
# o None se il valore non è presente.

def cerca_valore_diz (diz: dict, valore):

        for key, value in diz.items():
            if value == valore:
                print (key)
                return key 
        else:
                print(None)
        

dit: dict = {"a":1,"b":2}

cerca_valore_diz(dit,2)
    
# 2. Scrivi una funzione che inverte le chiavi e i valori in un dizionario.
# Se ci sono valori duplicati, scarta i duplicati.

def inverte_valori_dizionario( diz: dict ) -> dict:
    diz_inverso: dict = {}

    for key, value in diz.items():
            diz_inverso[value]= key

            return diz_inverso
    
print (f'{inverte_valori_dizionario(dit)}\n')
      
     
# Scrivi una funzione che riceve una lista di numeri,
#  filtra i numeri pari, e restituisce una nuova 
#  lista con i numeri pari moltiplicati per un fattore dato

def lista_numeri_pari_per_fattore (l1: list[int], fattore: int) -> list:
    l2=[] # liste vuote
    l3= [] # liste vuote
    for elemento in l1 : # per ogni elemento in lista 
        if elemento % 2 == 0: # se l'elemento è divisibile per 2 con resto ugale a 0 PARI
            l2.append(elemento) # aggiungi alla lista gli elementi 

    for i in l2: # cicla eleemnti della lista nuova creata con numeripari 
        l3.append(i*fattore) # aggiungi alla lista l3 tutti gli elementi della lista e moltiplicali per il fatootre 
    
    return l2,l3
          
l1 = [] # creo una lista vuota
for i in range(10): # con una linghezza massima di 10 elementi 
    l1.append(random.randint(0,1000)) # aggingi gli elementi random di numeri tra 0 e 1000

print (f'{l1} {len(l1)}\n')
l5= [7,3,4,5,6,8,10]

print(f'{lista_numeri_pari_per_fattore(l1,2)}\n')

 
# Scrivi una funzione che determina se un numero è 'magico'. 
# Un numero è considerato magico se è 
# divisibile per 4 ma non per 6.

def magic_number (num: int ) -> str : 
    if num % 4 == 0 and  num % 6 != 0 :
        return f'{num} is a magic number'
     
    else:
        return f'{num} is not a magic number'
    
print(f'{magic_number(66)}')

print(f'{magic_number(60)}')

print(f'{magic_number(8)}\n')


# Scrivi una funzione che accetti una lista di numeri
# e ritorni la somma dei numeri che 
# sono divisibili sia per 2 che per 3.

def sum_num (l1: list) -> int:

    lsum = []
    for elemento in l1:
        if elemento % 2 == 0 and elemento % 3 == 0:
            lsum.append(elemento)
        
    return (sum(lsum))

l3=[3,3,4,5,6,7,8,9,10,12,16,18]
l4=[6,16,18]

print(sum_num(l1))

print(sum_num(l3))

print(sum_num(l4))


# Scrivi una funzione che accetti un dizionario
# di prodotti con i prezzi e restituisca un nuovo dizionario 
# con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

def prodotti_sup_20 (diz: dict):
    new_dict: dict= {}
    for key, value in diz.items():
            if value > 20:
                sconto =(value * 10 /100)
                new_dict[key] = value - sconto 
            
 
    return sconto,diz,new_dict
 

store: dict = dict(Maglietta= 18, Jeans = 25, calze= 6, Felpa= 30)

print(prodotti_sup_20(store))

# 7. Scrivi una funzione che prenda in input 
# una lista di dizionari che rappresentano voti 
# di studenti e aggrega i voti per studente 
# in un nuovo dizionario.

def aggrega_voti (li:list) -> dict:
    voti={}
    for i in li:
        studente =i['studente']
        voto = i['voto']
        if studente in voti:
            voti[studente].append(voto)
        else:
            voti[studente]=[voto]
    return voti

lista_voti = [
     {'studente': 'Franca','voto':30},
     {'studente': 'Gino','voto':30},
     {'studente': 'Sonia','voto':30},
     {'studente': 'Dario','voto':18},
     {'studente': 'Sonia','voto':29},
     {'studente': 'Simone','voto':27},
     {'studente': 'Dario','voto':20}   ]


print(aggrega_voti(lista_voti))
 
"""Scrivi una funzione che elimini dalla lista 
dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere 
come chiavi e il numero di volte che devono essere rimossi come valori."""
 
"""9. Scrivi una funzione che converta una lista di
tuple (chiave, valore) in un dizionario.
Se la chiave è già presente, aggiungi 
il valore alla lista di valori già associata alla chiave."""

def roscio (l1:list) -> dict:
    newdict: dict = {}
    for elements in l1:
        if elements[0] in newdict:
             newdict[elements[0]].append(elements[1])
        else:
             newdict[elements[0]]=[elements[1]]
             
    return newdict
####### altro metodo 
def elimina_duplicati(l1:list)-> dict:
    newdict: dict = {}

    for elemento in l1: 
        if elemento[0] not in newdict:
            newdict[elemento[0][0]]=[]
            newdict[elemento[0]].append(elemento[1])
        else: 
            newdict[elemento[0]].append(elemento[1])

    return newdict


# d = defaultdict(list)
# for k in t:
#     d[k[0]].append(k[1])
     
thistuplelist = [ ("a", 1), ("b",2), ("c",3), ("a",4), ("b", 6)]

print(roscio(thistuplelist))
print(elimina_duplicati(thistuplelist))

 
# 10. Scrivi una funzione che prende una lista
#  di numeri e ritorna un dizionario che classifica 
#  i numeri in liste separate per numeri pari e dispari.

def dizPariDispari(l1:list) -> dict:
    diz_num_pari_dispari: dict = {}
    diz_num_pari_dispari["Pari"] = []
    diz_num_pari_dispari["Dispari"]= []
    for i in l1:
        if i %2== 0:
            diz_num_pari_dispari['Pari'].append(i)
        else:    
            diz_num_pari_dispari['Dispari'].append(i)

    return diz_num_pari_dispari

l7=[]
for i in range(20):
    x= random.randint(0,100)
    l7.append(x)

print(l7)

print(dizPariDispari(l7))

"""11. Scrivi una funzione che converte una 
temperatura da gradi Celsius a Fahrenheit 
e viceversa a seconda del parametro. 
Utilizza il concetto di parametri opzionali."""
 
""" Scrivi una funzione che somma tutti i numeri
interi di una lista che sono maggiori di un 
dato valore intero definito threshold."""
 
def threshold(l1:int, fattore: int):
    newlist=[]
    for i in l1:
        if i > fattore:
            newlist.append(i)
    return sum(newlist)

l10=[1,1,1,2,3,3,3,]
l8=[2,3,4,5,6,7,8,9]
print(threshold(l8, 4))
print(threshold(l10, 2))


"""
13. Scrivi una funzione che, data una lista, 
ritorni un dictionary che mappa ogni 
elemento alla sua frequenza nella lista."""
 
"""14. Scrivi una funzione che ritorna un
 dizionario che unisce due dizionari. 
 Se una chiave è presente in entrambi, 
 somma i loro valori nel nuovo dizionario."""
 
# 15. Scrivi una funzione che, dato un insieme
#  e una lista di numeri interi da rimuovere,
# ritorni un nuovo insieme senza i numeri
# specificati nella lista.

def rimuovinumeri():

    pass

 
"""16. Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
 
17. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
 
18. Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
 
19. Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
 
20. Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo.
 
21. Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
 
22. Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
 
23. Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.
 
24.  Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
 
25. Scrivi una funzione che conta quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato da elementi uguali.
 
26. Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

ESEMPIO: create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}

Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

ESEMPIO: update_contact(dict, "Mario Rossi", telefono=123456789)

OUTPUT: {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}
Last modified: Tuesday, 14 May 2024, 4:31 PM"""