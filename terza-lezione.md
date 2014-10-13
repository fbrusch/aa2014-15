Ripartiamo dalla funzione `quadrato`:

in python:

    def quadrato(x):
        return x*x

in C:

    int quadrato(int x)
    {
        return x*x;    
    }

Vediamo in che modi possiamo variare questo semplice *pattern*...

Prima di tutto, cosa possiamo mettere dopo `return`? Un'*espressione*.

Un'*espressione* è un elemento che è possibile *valutare*, dandogli un valore.

Esempi:

    1
    x
    x+1
    x*x+1
    (x+1)*(x*2)

Tutti esempi comprensibili. E' possibile generalizzare? 
(Introdurre magari rappresentazione tramite AST)

Espressione -> AST -> Valutazione

(Far notare, con nonchalance, la ricorsività intrinseca della regola)

Rilassare:
-) una variabile -> n variabili
-) naturali -> interi -> reali (o meglio, razionali)

Nelle espressioni: introdurre la valutazione di altre funzioni -> combinazione
di funzioni:

    f(g(h(x)))
    
Problemi conclusivi impossibili:

-) modulo
-) distanza (con radice quadrata)
-) pari/dispari
