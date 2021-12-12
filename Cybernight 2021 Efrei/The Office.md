# The Office
> Stégano, 50 pts
> 
> Dwight Schrute vous a envoyé un étrange mémo. Le texte a l'air de contenir des petits symboles, peut-être un résidu de ses années en tant qu'adjoint au shériff volontaire. Trouvez le message caché dans son mémo.
> **Explication du flag**
> Vous trouverez un texte, le flag est écrit dedans entre les mots `FLAG`. Par exemple, si vous trouvez le texte:
> 
*CECI EST UN TEXTE EXEMPLE FLAG CH4LL3NGECYB3RN1GHT FLAG ET VOICI LA FIN DU TEXTE*
>
Le flag vous permettant de valider sera :
CYBN{CH4LL3NGECYB3RN1GHT}
>
Auteur : Magnitude

Un fichier est joint. On trouve dedans un texte accentué de manière exagérée.

![[img/Pasted image 20211212084409.png]]

Après un peu de réflexion, l'idée que chaque accent représente un caractère de code morse germe. On enlève donc tout les caractères qui n'ont pas d'accent ou de point au dessus d'eux (coucou i et j). Cela nous laisse : 

![[img/Pasted image 20211212084732.png]]

On rédige ensuite un script qui transforme les accents neutres en trait, les points en point, les ~ en espaces, et les accents aigus en /.

```py
text = "ėēȦȧãėīĩéẽȯōėẽėẽȧēōiẽĪēāãōiãėėȯẽėĩíẽiãȦȧiẽēẽéãėėẽĪȯīėẽȯėõáẽīāãiāĩėiẽȯėėĩóĩiīȯiẽėõíõēẽėĩēiiīõāãȯãóẽėõiȯėãēẽéẽīãėāȯĩȧãȧiėẽéẽȯōėiãōēīĩēȦãīōȧĩéẽȧŌāiĩiẽėiōãēãéĩȧĩēõȧāȯãiõáĩiėōiẽiāẽiėāãōĩéĩȧȯãėāȯiÃíõīẽiīȯĩōīāãėiōãiȯėāẽėẽiēiẽéẽėiāõīȧãiẽáĩāĨȯẽīėēėĩȯėȧėẽīėẽėėĩēēȯōõėėēĩėãóĩȧāīȮĩȧīiėõėėīĩȯėėõéẽėĩėėāėãȧȯōėẽȯȧẽāėīėẽȧāõēȯēiẽiãéĩėȧȯĩȧȧẽēȧẽīāēõīėõíẽēãėȧōãóẽȯīėĩėėĩȯiȯĩīēȯēĩiiēẽėõȯiėãíẽēėėĩóĩāėīīẽáãėāōȯĩȯīẽėėiõėiiõȯẽėēȯõáõiīōȧãȯāėȯẽiėōõȯėėĩíẼīȧėãiẽéẽiėēēīẽėȯėėīĩáãėiėȧõėẽȯȧēãȯōėẽėõėiȯõéãīãȯėīõéĩīȦīōãéẽėãȧėėõáõėēīȯĩȧōiõėẽėiėĩōīȯīẽėėīẽėõíãėĩēȧĩōiāėẽēāēĩiōėĩiãéõōēėōĩėėēẽȯãėīȧiẽōēȧōẽėėēẽiõiiėÕéĩėõėȯōėõȧȧīȯẽōīāãȯēiẽīõiȯėẽóãȯȧēėẽiēėėãiōãōāėĩéõēōĨēāēōāãȧēiãėėȧõėãōiēȯõēīīēōẽēȧėÃȯĩėēāēōẽėȯȧẽiėōȧẽȧȯōẽīiẽāȯėȧõiȯōẽōãȧẽėėiēãȧėėēōẽōȧĩāȧėȦẽȧõōẽāãȯẽȧīiẽiīēẽȧēāēāõāẽėiiȯãȯiiĩāõiĩēīėẽėėȧȯēĩāȦẽāāōāōẽáẽȯėēėẽiīȯȧĩȯēõāīȧẽáẽīėȧėẽiȧẽėõēȯãéãiēōāẽāīāĩėiōẽȧõéãōĩȧėīẽéãȧīĩȧȧėĩáẽīõėēȧõīīīãȯȧīãiėiāãȯĩóãiẽiėėãōãéẽēīīẽāėãíĩȯēȧėãėãóãȯēōāōĩȯēēāāõíÃīėȮẽȧẽāėāȧãȧĩīēẽōȯiȧẽėēȦãėẽíẽāēōẽėȯīãóãiōȧȧẽȧĩóõȯēīāōẽiȧīīēãéĩīȯȧãjȯẽēėāėõėẽēōãēȯȧėãȯōiãė"  
output = ""  
charsetDot = "ėȦȧȯiȮj"  
charsetDash = "āēīōĪŌ"  
charsetTilde = "ãĩẽõẼÃÕĨ"  
charsetAccent = "óíéá"  
for char in text:  
    if char in charsetDot:  
        output += "."  
    elif char in charsetDash:  
        output += "-"  
    elif char in charsetTilde:  
        output += " "  
    elif char in charsetAccent:  
        output += "/"  
    else:  
        output += "X" + char + "X"  
 
print(output)
```

Ce qui nous donne : 
```txt
.-.. .- / .-. . .--. --- -. ... . / . ... - / .. -.-. .. / -- .- .. ... / .-.. . / - . -..- - . / . ... - / - .-. . ... / .-.. --- -. --. / .--. . ..- - / . - .-. . / ..-. .- ..- - / .. .-.. / - .-. --- ..- ...- . .-. / ..- -. . / - . -.-. .... -. .. --.- ..- . / .--. .-.. ..- ... / . ..-. ..-. .. -.-. .- -.-. . / ... .. -. --- -. / - ..- / .-. .. ... --.- ..- . ... / -.. / -.-- / .--. .- ... ... . .-. / .--. .-.. ..- ... / -.. . / ..--- ....- / .... . ..- .-. . ... / - ..- / -.-- / . ... / .--. .-. . ... --.- ..- . / . -. -.-. --- .-. . / --.- ..- . .-.. --.- ..- . ... / . ..-. ..-. --- .-. - ... / ..-. .-.. .- --. / -- ----- .-. ... . -.-. ----- -.. . .---- ... ..-. ..- -. -... ..- - . ...- ...-- -. -... . - - . .-. .-- .---- - .... ... - . --. ....- -. ----- / ..-. .-.. .- --. / -... .. . -. / .--- --- ..- . / - ..- / .- ... / - .-. --- ..- ...- . / . ... - / --- -. / .-.. . / .---- .---- / -.. . -.-. . -- -... .-. . / --- ..- / .-.. . / .---- ..--- / -.. .. -.-. . -- -... .-. .
```

Après décodage, on obtient `LA REPONSE EST ICI MAIS LE TEXTE EST TRES LONG PEUT ETRE FAUT IL TROUVER UNE TECHNIQUE PLUS EFFICACE SINON TU RISQUES D Y PASSER PLUS DE 24 HEURES TU Y ES PRESQUE ENCORE QUELQUES EFFORTS FLAG M0RSEC0DE1SFUNBUTEV3NBETTERW1THSTEG4N0 FLAG BIEN JOUE TU AS TROUVE EST ON LE 11 DECEMBRE OU LE 12 DICEMBRE`

flag: `CYBN{M0RSEC0DE1SFUNBUTEV3NBETTERW1THSTEG4N0}`

nhy.