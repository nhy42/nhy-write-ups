# Golden Cipher

> Crypto, 50pts
>
Selon le principe de Kerckhoffs, la sécurité d'un système cryptographique ne dépend pas de la méthode de chiffrement mais de la clé elle même.
>
Ainsi, si je prends un nombre infini pour clé et que je le XOR, mon secret est parfait !
>
Il ne me reste plus qu'à trouver un nombre infini...
>
Auteur : Maestran

On a donc une image qui a été XORée avec une clé d'une longueur infinie. On a donc naturellement pensé à Pi, sqrt(2), ou encore le nombre d'or, qui rappelle étrangement le titre.

Pour vérifier notre hypothèse, on va commencer à décoder l'image. En effet, comme c'est un PNG, elle possède normalement des magic bytes au début du fichier.
Dans le fichier chiffré, les premiers bits sont `99 42 4D 60`, et on cherche à obtenir `89 50 4E 47`, les magic bytes des PNG. En les passant dans un XOR, (à la main oscour jsuis trop stupide), on obtient une parcelle de la clé, `00010000 00010010 00000011 00100111`, qui, convertie en base 10, donne `16 18 03 39`.
Sachant que le nombre d'or commence par 1.6180339..., on en déduit que la clé est bel et bien ce nombre. 
Il ne reste plus qu'à récupérer quelques 20000 décimales de ce nombre, et de XORer la photo avec.

Un script python plus tard...
```py
with open("chall.encoded.png", "rb") as f:  
    content = f.read(9000)  
with open("phi.txt", "r") as f:  
    key = f.readline()  
content = list(content)  
output = []  
  
for i in range(len(content)):  
    output.append(content[i] ^ int(key[i*2:i*2+2]))
	# juste un XOR très moche ^
with open("outpou.png", "wb") as f:  
    f.write(bytearray(output))
```

On récupère une image, qui contient le flag
![[img/outpou.png]]

flag: `CYBN{3uClId3_Le_BoSs_D3s_N0mbR3s}`


Euclide, on t'aime.
nhy.