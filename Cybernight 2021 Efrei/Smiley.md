# Smiley😃
> Crypto, 50 pts
> 
> 🤣 🤣 🤣 🤣 et tu brute 🤣 🤣 🤣 🤣
>
> Auteur : Langley

`🐷👍🐶👂👯𾨢👓🐨👊🐧👓👩👢🐥👗🐤👘🐧👓𾷢👱`

Bon.
P'tite recherche Google.
"et tu brute"
Paroles prononcées par César.
Donc code césar.
On prend l'unicode des smileys, et on applique un code césar.
Pour connaitre le décalage, on va convertir le premier en un C, car le flag commence par CYBN{.
On obtient un décalage de `0x1f3f4`

On automatise tout ça :

```py
text = "🐷👍🐶👂👯𾨢👓🐨👊🐧👓👩👢🐥👗🐤👘🐧👓𾷢👱"  
out = ""  
for e in text:  
    out += chr(ord(e) - 0x1f3f4)  
print(out)
```

On obtient ce cher
flag: `CYBN{😮_4V3_un1c0d3_🧮}`

Langley jtm pa
nhy.