# Smileyð
> Crypto, 50 pts
> 
> ð¤£ ð¤£ ð¤£ ð¤£ et tu brute ð¤£ ð¤£ ð¤£ ð¤£
>
> Auteur : Langley

`ð·ðð¶ðð¯ð¾¨¢ðð¨ðð§ðð©ð¢ð¥ðð¤ðð§ðð¾·¢ð±`

Bon.
P'tite recherche Google.
"et tu brute"
Paroles prononcÃ©es par CÃ©sar.
Donc code cÃ©sar.
On prend l'unicode des smileys, et on applique un code cÃ©sar.
Pour connaitre le dÃ©calage, on va convertir le premier en un C, car le flag commence par CYBN{.
On obtient un dÃ©calage de `0x1f3f4`

On automatise tout Ã§a :

```py
text = "ð·ðð¶ðð¯ð¾¨¢ðð¨ðð§ðð©ð¢ð¥ðð¤ðð§ðð¾·¢ð±"  
out = ""  
for e in text:  
    out += chr(ord(e) - 0x1f3f4)  
print(out)
```

On obtient ce cher
flag: `CYBN{ð®_4V3_un1c0d3_ð§®}`

Langley jtm pa
nhy.