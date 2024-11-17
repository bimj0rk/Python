# **TASK 01**

## <ins>Cerinta</ins>

> Vrem sa luam informatiile de pe `quotes.toscrape.com`.

> Pe acest site putem observa ca sunt prezentate mai multe citate, impreuna cu autorii lor.

> Dorim sa stocam intr-un dictionar, pentru fiecare autor, toate citatele sale.
#### Dorim sa folosim <ins><strong>[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)</strong></ins>.

## <ins>Exemplu</ins>
### [https://quotes.toscrape.com](https://quotes.toscrape.com) :
```
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” by Albert Einstein (about) 

“It is our choices, Harry, that show what we truly are, far more than our abilities.” by J.K. Rowling (about)

“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.” by Albert Einstein (about)

```

### Dictionar :
```
{
    'Albert Einstein': ['The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.', 'There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.'],
    'J.K. Rowling' : ['It is our choices, Harry, that show what we truly are, far more than our abilities.']
}
```

## <ins>TASK 1.1</ins>
#### Dorim sa retinem toate citatele de pe <strong><ins>prima</ins></strong> pagina.

## <ins>TASK 1.2</ins>
#### Dorim sa retinem toate citatele de pe <strong><ins>toate</ins></strong> paginile.
> Pentru a efectua asta, vom trece la urmatoarea pagina pana nu mai putem.


## <ins>Rulare | Testare</ins>

> Pentru testare, puteți rula script-ul direct din IDE sau puteți rula în terminal comanda:

```
./checker.py
```

> In cazul in care nu puteti rula acest script din cauza permisiunilor, folositi mai intai urmatoarea comanda:

```
sudo chmod +x checker.py
```
