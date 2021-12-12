# Hardware to hell
>Hardware,  50 pts
>
>Votre ami Brian s'est amusé avec des portes logiques et a décidé de vous proposer un petit défi ! Un générateur de lettre en ASCII émet le flag sur un bus 8 bit ! À vous de retrouver le mot initial écrit !
>
(Edit : Visiblement, le fichier se lit mal avec le lecteur de Windows. Ouvrez le avec VLC svp)
>
Auteur : Maestran

Dans cette vidéo, on a un circuit sur Multisim (<3) et on doit retrouver les valeurs des bits de base, en se basant sur les afficheurs hexa.

On se rend compte que dans ce circuit compliqué, il y a finalement deux type de sous circuits : 
![](https://i.imgur.com/HNrhzuB.png)

Après simplification, on se rend compte que le groupe bleu retourne toujours 1, et le vert toujours 0.
On peut donc simplifier les entrées du premier compteur en : m6, m5, m4, m3; et celles du second compteur en m2, m1, m0, m7.

Finalement, on a juste à passer le bit de droite (m7) tout à gauche.

On va donc regarder la vidéo et relever les valeurs des compteurs hexa.

`86 B2 84 9C F6 62 4E DA BE 60 DC BE E8 D0 66 DE 90 62 CE D0 EE 68 F2 BE E8 DE BE D0 66 D8 98 FA`

Puis rédiger un script qui effectue le déplacement de bit.

```py
output = ""  
data = "86 B2 84 9C F6 62 4E DA BE 60 DC BE E8 D0 66 DE 90 62 CE D0 EE 68 F2 BE E8 DE BE D0 66 D8 98 FA"
data = data.split(" ")
for e in data:  
    lebyte = '{0:08b}'.format(int(e, 16))  # on le transforme en 8 bits
    lebyteF = lebyte[-1] + lebyte[:-1]  # on effectue le décalage
    output += chr(int(lebyteF, 2))  # on transforme en caractère
print(output)
```

Et hop !

![](https://i.imgur.com/MPboKft.png)

flag: `CYBN{1'm_0n_th3oH1ghw4y_to_h3lL}`

nhy.