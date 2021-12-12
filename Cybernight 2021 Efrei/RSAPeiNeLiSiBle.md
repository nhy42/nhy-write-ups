# RSAPeiNeLiSiBle
> Crypto, 125 pts
> 
> Mince, vous avez mis votre clé privée RSA à la machine à laver, et une partie n'est plus visible ! Réussirez vous à retrouver le secret que vous aviez chiffré ?
>
Auteur : Maestran

Un challenge franchement super intéressant.
On possède une clé privée à laquelle il manque quelques parcelles.

![](https://i.imgur.com/uXihazg.png	)

Le but va être de reconstituer une clé privée valide, qui va nous permettre de déchiffrer secret.msg.enc

Après quelques recherches sur comment retrouver une clé privée en en connaissant une partie, j'ai trouvé ceci.

https://blog.cryptohack.org/twitter-secrets

C'est un article de blog très intérressant sur la manière dont une clé privée partiellement censurée à été retrouvée. On va appliquer une méthode similaire.

Pour commencer, on va passer de la version base64 de la clé à de l'hexadécimal. Après conversion, on a :

![](https://i.imgur.com/Vc7hGBS.png)

On a pu constaté que la clé était dans un fichier .pem. Ce type de fichier défini une structure claire pour les clés RSA, structure qui est la suivante :

```txt
RSAPrivateKey ::= SEQUENCE {
  version           Version,
  modulus           INTEGER,  -- n
  publicExponent    INTEGER,  -- e
  privateExponent   INTEGER,  -- d
  prime1            INTEGER,  -- p
  prime2            INTEGER,  -- q
  exponent1         INTEGER,  -- d mod (p-1)
  exponent2         INTEGER,  -- d mod (q-1)
  coefficient       INTEGER,  -- (inverse of q) mod p
  otherPrimeInfos   OtherPrimeInfos OPTIONAL
}
```

On peut lire dans l'article de blog : 
![](https://i.imgur.com/tu5fkIE.png)

Les données sont donc séparées `02 82` et une longueur pour les données.
Recherchons donc ces séparateurs :

![](https://i.imgur.com/9GkuFWX.png)

En lisant les deux bytes qui suivent ces séparateurs, on peut donc savoir la longueur des données, ce qui donne ceci.

![](https://i.imgur.com/K0vlxAE.png)

En se référant à la structure du fichier PEM, on a donc :
- N en vert
- e en rouge
- d en rose
- p en bleu
- q en orange

On aura pas besoin du reste car on a p, q et e, les trois seuls indispensables pour calculer tout le reste.

On a donc :
```py
q = 0x00c456582c0523d990a0dcd092f3f38e70f9ad48622f20db688a4e8d493dd470d43b311d21f4b9111184e291ca89f1cd1dffc79239c7dd067c2f432ed981c48e62064ff12899817461cab13a22c161c012b67166cf6a16d1d4e5785e867b913f6c8a4b4d196de44dec537855804d11fb2029659b97edf37894712a3c60a1d24e4bf7db7dba530a88a472a39d6f084c052c1b6f825fd9da47e2d569a48b78ad32bc928827c1fa5da94a04fa34be538a9be92139601903eff4e9c6e884a527ec3797a685dfc6c0b6c06a36b40f4e70c24ec2708962662be8dfc5527ab38c54535888e69eaa27a837ea22617085fda56609581943c895c28f0920a083f59806baf5e1  
 
p = 0x00e2bfc3879868bc51372b017766442bc4961d8b389e254daa653d1e9ddb33b8e2e2c42c7074965d6bd10a342d01155d650aac31a0d38af928a0847a2d1843995697bb7fe48f9ef05bcfc516eff2cb79b26f93460c4721a9385c77245878fd36e7c4a1df05be22b536030f18503ffc741790feed41379836fa0522472d0fd9ff290b24f5f900ec5dbc767a941429cfe9639b55e4f31c7242157299a5e9f6c2723e4d69a1c921a0644b48dfba9cc84577b06b8063cb9ca84f79ac4d5a3f60d6e330957f55a40ad4247dc362a3935898991c75cbd81889b740f550bbde93a9c769847197e16e28bbc8a312aa8bfab8e182016bb2b067a6b6ba8eb9279b65103c033f  
e = 65537
```

De là, on peut simplement calculer une clé en python :

```py
from Crypto.PublicKey import RSA  
  
q = 0x00c456582c0523d990a0dcd092f3f38e70f9ad48622f20db688a4e8d493dd470d43b311d21f4b9111184e291ca89f1cd1dffc79239c7dd067c2f432ed981c48e62064ff12899817461cab13a22c161c012b67166cf6a16d1d4e5785e867b913f6c8a4b4d196de44dec537855804d11fb2029659b97edf37894712a3c60a1d24e4bf7db7dba530a88a472a39d6f084c052c1b6f825fd9da47e2d569a48b78ad32bc928827c1fa5da94a04fa34be538a9be92139601903eff4e9c6e884a527ec3797a685dfc6c0b6c06a36b40f4e70c24ec2708962662be8dfc5527ab38c54535888e69eaa27a837ea22617085fda56609581943c895c28f0920a083f59806baf5e1  
p = 0x00e2bfc3879868bc51372b017766442bc4961d8b389e254daa653d1e9ddb33b8e2e2c42c7074965d6bd10a342d01155d650aac31a0d38af928a0847a2d1843995697bb7fe48f9ef05bcfc516eff2cb79b26f93460c4721a9385c77245878fd36e7c4a1df05be22b536030f18503ffc741790feed41379836fa0522472d0fd9ff290b24f5f900ec5dbc767a941429cfe9639b55e4f31c7242157299a5e9f6c2723e4d69a1c921a0644b48dfba9cc84577b06b8063cb9ca84f79ac4d5a3f60d6e330957f55a40ad4247dc362a3935898991c75cbd81889b740f550bbde93a9c769847197e16e28bbc8a312aa8bfab8e182016bb2b067a6b6ba8eb9279b65103c033f  
N = p * q  
e = 65537  
phi = (p - 1) * (q - 1)  
d = pow(e, -1, phi)  
  
key = RSA.construct((N, e, d, p, q))  
pem = key.export_key('PEM')  
print(pem.decode())
```

On obtient : 
```txt
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```

On peut ensuite déchiffrer le message en utilisant cette clé :

![](https://i.imgur.com/MT8nYkw.png)

flag: `CYBN{P4rt14l_K3y_4r3_3Z_T0_D1sc0v3r}`

nhy.