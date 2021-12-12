# Cicéron
> Crypto, 25 pts
>
> Cicéron c'est pas carré.
>
> En décodant ce challenge, vous allez trouver une chaine : cybnxxxxxxxxxxxxxxxx
>
> Le flag est alors CYBN{XXXXXXXXX}
>
> Auteur : Maestran

Bon, si c'est rond c'est pas carré.
DU COUP APRES 1H A RÉPÉTER CETTE PHRASE, on est parti sur un carré de Polybe

https://fr.wikipedia.org/wiki/Carr%C3%A9_de_Polybe

Certes, c'est carré, pas rond, mais les digits allaient de 1 à 5, et on s'est dit que ça collait plutôt bien.

On a donc rédigé un petit script Python qui retranformait les nombres en lettre:

```py
carre = ["abcde", "fghik", "lmnop", "qrstu", "vwxyz"]  
data = "23 31 31 45 23 43 45 15 15 23 44 11 31 34 42 43 14 54 11 35 35 42 34 15 34 33 14 23 42 43 34 33 11 21 34 33 23 43 11 33 44 15 42 11 33 21 23 33 35 34 45 42 51 34 23 42 43 11 13 13 34 32 35 31 23 42 43 34 33 15 34 42 15 11 23 44 41 45 23 35 11 42 43 45 42 13 42 34 23 44 35 42 34 15 23 44 11 11 45 35 11 54 43 35 45 23 43 41 45 45 33 32 34 23 43 35 31 45 43 44 11 42 14 44 34 45 44 45 33 13 22 11 13 45 33 43 11 13 13 34 42 14 11 23 44 35 34 45 42 33 11 33 44 23 42 31 23 33 44 42 23 21 11 33 44 15 31 45 53 41 45 23 43 34 45 42 14 11 23 44 14 45 35 45 23 44 43 14 45 33 15 34 42 44 35 34 45 51 34 23 42 13 45 42 11 44 23 15 43 45 42 44 34 45 44 11 33 44 23 13 11 44 11 42 42 22 11 31 32 11 23 43 43 11 35 35 31 23 41 45 11 33 44 11 45 43 43 23 11 31 11 31 12 45 21 34 11 31 11 33 13 22 23 31 34 35 43 11 45 53 12 45 12 34 33 43 11 45 53 13 11 31 13 45 31 43 11 45 53 13 22 11 31 11 55 23 34 33 43 11 45 44 42 23 43 32 45 43 11 45 35 23 44 54 42 23 11 43 23 43 11 45 32 11 31 12 31 11 33 13 11 45 35 42 45 42 23 21 34 11 45 32 11 31 13 11 14 45 13 11 45 21 31 34 43 43 11 33 44 22 42 11 53 15 31 11 21 13 54 12 33 12 42 11 51 34 44 34 44 34 31 34 44 34 14 34 14 34"  
data = data.split(" ")  
output = ""  
for e in data:  
    output += carre[int(e[0])-1][int(e[1])-1]  
print(output)
```

Le résultat : `...cybnbravototolotododo`

Flag: `CYBN{bravototolotododo}`

nhy.