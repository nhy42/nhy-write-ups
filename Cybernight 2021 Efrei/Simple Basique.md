# Simple Basique
> Crypto, 50 pts
> 
[Vous n'avez pas les bases](https://www.youtube.com/watch?v=2bjk26RwjyU)
>
Auteur : Maestran

D'après le titre du challenge, ça va être une histoire de base.

On regarde les données, et on se rend compte que pour chaque "nombre", on peut former un groupe de 8 digit. Le premier ressemble à du binaire, le second à du ternaire, etc...
Ca concorde avec le titre du challenge, on le programme donc en python :
```py
data = ['01000011', '00010022', '00001002', '00000303', '00000323', '00000204', '00000061', '00000132', '00000102',  
 '000000A4', '00000043', '0000008A', '00000036', '0000007B', '0000005F', '0000006E', '00000069', '00000050',  
 '00000051', '0000005A', '00000047', '0000004B', '0000004I', '0000001O', '00000046', '0000003M', '0000001N',  
 '00000049']  
output = ""
for i in range(28):  # il y a 28 caractères
    output += chr(int(data[i], i + 2))  
print(output)
```
Chaque nombre sera donc d'une base supérieure par rapport au précédent.
On obtient : `CYBN{f1nfr3r0t_tu_es_gr1ng3}`

nhy.