# Coffre Faible
> Web, 25 pts
>-   Là, je vois pas d'autre solution que du bruteforce Francis...
>-   T'es malade Hervé ?! Ça ferait plusieurs millions de millions de tentatives !
>-   Des millions de millions ? Tu sais c'que c'est déjà un million Francis ?
>
>Auteur : Pedro

Ce challenge était un challenge de web, avec un script javascript à étudier.
Le script était le suivant :
```javascript
function validate(evt) {
    //Prevents writing something else than numbers in the field
    var theEvent = evt || window.event;
  
    // Handle paste
    if (theEvent.type === 'paste') {
        key = event.clipboardData.getData('text/plain');
    } else {
    // Handle key press
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    }
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
  }
function ord(str){return str.charCodeAt(0);}


function verifyCode(){

    let input = document.getElementById("pinCodeInput").value
    let errorBox = document.getElementById("decoded")
    verdict = decode(encoded_secret, input);

    errorBox.innerHTML = "<p>The decoded version is : " + verdict + "</p>"
}
encoded_secret = [4229017489054368000, 8423440829015654000, 8327295314625036000, 12300356615676100000, 23274382044212232000, 17659868544248054000, 12865978863389245000, 28379983391804620000, 35947115262209163000, 16648862929583604000, 35945819711094130000, 39760570450349920000, 47674280884184285000, 41147021077870805000, 26232960198658490000, 64856694827717230000, 47105112917629990000, 56910435851813520000, 68102959469426640000, 52306587032009834000, 33294452887929225000, 83393419978106470000, 38590981526287024000, 90644339846325200000, 77875051992532910000, 88531365307065830000, 43256654458991410000, 105146179582762680000, 89854832644372560000, 78189286574595770000, 52462374678475830000, 119648019319200150000, 123273479253309520000, 96001806167873420000, 54479749198550925000, 132983338542110340000, 81467145141763440000, 150007782858351970000, 119804284273971690000, 134432840646746180000, 68855758728361670000, 140990194266700510000, 134558466292670530000, 177340802748383230000]

function getCoefficients(passcode){
    return [
        passcode[7]**(passcode[12]*4) + 18,
        21*(passcode[12]**passcode[7] + 83),
        7*(passcode[7]**passcode[7]**passcode[12])
    ]
}

function decode(encoded_secret, passcode){
    decoded_secret = ""
    coeffs = getCoefficients(passcode)
    a = coeffs[0], b = coeffs[1], c = coeffs[2]

    for ( i = 2 ; i < encoded_secret.length + 2 ; i++ ){
        x = encoded_secret[i-2]
        x = x/(c*(a*i+b))
        if( (x < 32)){
            x = 33 //replace by '!' if the caracter is not printable
        }
        decoded_secret+=String.fromCharCode(x)
    }

    return(decoded_secret)
}
```

En suivant le champ passcode, on se rend compte que le seul emplacement où il est utilisé est dans la fonction getCoefficients, et que dans cette fonction, seul les digits 7 et 12 sont utilisés.
On va donc simplement tester les 100 possibilités.

```javascript
// on garde le script précédent
encoded_secret = [4229017489054368000, 8423440829015654000, 8327295314625036000, 12300356615676100000, 23274382044212232000, 17659868544248054000, 12865978863389245000, 28379983391804620000, 35947115262209163000, 16648862929583604000, 35945819711094130000, 39760570450349920000, 47674280884184285000, 41147021077870805000, 26232960198658490000, 64856694827717230000, 47105112917629990000, 56910435851813520000, 68102959469426640000, 52306587032009834000, 33294452887929225000, 83393419978106470000, 38590981526287024000, 90644339846325200000, 77875051992532910000, 88531365307065830000, 43256654458991410000, 105146179582762680000, 89854832644372560000, 78189286574595770000, 52462374678475830000, 119648019319200150000, 123273479253309520000, 96001806167873420000, 54479749198550925000, 132983338542110340000, 81467145141763440000, 150007782858351970000, 119804284273971690000, 134432840646746180000, 68855758728361670000, 140990194266700510000, 134558466292670530000, 177340802748383230000]

function getCoefficients(passcode){
    return [
        passcode[7]**(passcode[12]*4) + 18,
        21*(passcode[12]**passcode[7] + 83),
        7*(passcode[7]**passcode[7]**passcode[12])
    ]
}

function decode(encoded_secret, passcode){
    decoded_secret = ""
    coeffs = getCoefficients(passcode)
    a = coeffs[0], b = coeffs[1], c = coeffs[2]

    for ( i = 2 ; i < encoded_secret.length + 2 ; i++ ){
        x = encoded_secret[i-2]
        x = x/(c*(a*i+b))
        if( (x < 32)){
            x = 33 //replace by '!' if the caracter is not printable
        }
        decoded_secret+=String.fromCharCode(x)
    }

    return(decoded_secret)
}

// la partie bruteforce

for(var i_ = 0; i_ <= 9; i_++) {
	for(var j_ = 0; j_ <= 9; j_++) {
		let passcode = "0000000" + i_ + "0000" + j_ + "0000000" 
		console.log(decode(encoded_secret, passcode))
	}
}
```

En sortie, on peut trouver dans la console notre flag :
![](https://i.imgur.com/CtZWLPF.png)
flag: `CYBN{P3dr0_alW4yS_lO0s3s_h1s_P4ssW0rDz_h4ha}`

nhy.