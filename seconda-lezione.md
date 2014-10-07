*) questioni logistiche
    -) esame: leggere codice e scrivere codice
    -) laboratorio: squadre, etc
    -) esercitazioni: portatevi il pc
    -) libri: programmazione C

## funzioni intere come soluzione a tutti i problemi dell'umanità
Se tutta l'informazione che ci interessa è codificabile con dei numeri, cosa
vuol dire elaborarla?
Qualche esempio:
    1) tradurre un testo
    2) prevedere che tempo farà
    3) data una foto, identificare di chi è il volto (o quanti anni ha il tipo
    della foto) 
    4) guidare la macchina?
    5) photoshoppare la foto di vostra cugina al saggio di danza, per farla
    somigliare a Shakira
    (chiedere a loro altri esempi)

In tutti questi casi, l'elaborazione consuma un numero intero e produce un
numero intero. In alcuni casi la produzione significativa è una tantum, in altri
è continua, ma abbiamo sempre N -> N.

Primo modello di elaborazione dell'informazione da parte di un calcolatore:
calcolo di funzioni intere. Come abbiamo visto, la cosa non è per niente restrittiva.

Prima accezione di "programmazione": spiegare al calcolatore come calcolare una
certa funzione intera.

Ci sono tantissimi linguaggi, ciascuno con sue caratteristiche proprie e
peculiari. Il linguaggio principale studiato in questo corso è il C. Il C è un
linguaggio particolare e molto potente, perché consente di scrivere programmi
molto "veloci", ma alcune cose sono un po' "difficili" da fare. Per
questo, ci "appoggeremo" a volte a qualche altro linguaggio, che consente di
esprimere alcune cose più facilmente. Questo servirà anche a capire che di
linguaggi ce ne sono tanti, e che saper scegliere quello giusto senza
spaventarsi è una leva potente. Il linguaggio a cui ci appoggeremo
principalmente è python.

Qual è la funzione in assoluto più semplice?

La costante: qualsiasi valore in ingresso, ritorna sempre lo stesso valore in
uscita.

Without further ado, ecco la funzione costante, in python:

    def f(x):
        return 0

