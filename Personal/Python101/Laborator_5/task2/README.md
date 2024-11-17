# **TASK 02**

## Cerinta

Daca in exercitiul anterior au fost extrase citate asociate unor autori, in acesta, trebuie extrase informatiile cartilor gasite pe site-ul [books.toscrape.com](https://books.toscrape.com/) si stocate in mod similar, intr-un dictionar.
Se observa ca fiecare carte are asociata o pagina.

#### Rezolvati folosind <strong><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" style="font-size: 17px;">BeautifulSoup</a></strong>

## TASK <big>2.0</big>

#### > informatiile <big> **primei** </big> carti
> Dictionarul va avea urmatoarele campuri, **in ordine**: 'title', 'price', 'stock', 'no_stars', 'UPC'.

## TASK <big>2.1</big>

#### > informatiile **tuturor cartilor** de pe <big> **prima** </big> **pagina**

> Se vor parcurge paginile fiecarei carti, luand informatiile aflate la task-ul anterior, si stocand dictionarul obtinut intr-un dictionar mai mare care sa contina toate cartile ( *biblioteca* ).

> Cheia catre fiecare dictionar va arata astfel: 'Book_ID', unde *ID* este numarul cartii (prima carte va avea cheia: 'Book_0').

### Exemplu:
#### Dictionarul primei carti:
```
{'title': 'A Light in the Attic', 'price': 51.77, 'stock': 22, 'no_stars': 'Three', 'UPC': 'a897fe39b1053632'}
```
#### Dictionarul final :
```
{
'Book_0': {'title': 'A Light in the Attic', 'price': 51.77, 'stock': 22, 'no_stars': 'Three', 'UPC': 'a897fe39b1053632'}
}
```

## TASK <big>2.2</big>

#### > informatiile **tuturor cartilor** de pe <big> **primele 5** </big> **pagini**

> <big>**! ATENTIE !** </big>

- Cheile cartilor vor fi pastrate in aceeasi maniera! 
- **Hint**: Cartile de pe pagina a doua vor avea cheia cuprinsa intre 'Book20' si 'Book_39'; regula ce se va continua si pentru restul paginilor.

## TASK <big>2.3</big>

#### > informatiile tuturor cartilor de pe primele 5 pagini **si stocarea lor** intr-un <big> **fisier CSV** </big>.

> **Hint** :
- Primul rand contine campurile, **in ordine**: 'Title', 'Price', 'In Stock', 'No. Stars', 'UPC'.
- Sub acestea se vor regasi informatiile corespunzatoare fiecarei carti.

> <big>**! ATENTIE !** </big>

``` Book_ID sa NU apara in fisierul CSV. ```

## Rulare | Testare

Pentru testare:
-  direct din IDE -> rulare script
-  in terminal -> rulare comanda:

    ```
    ./checker.py 
    ```

 In cazul in care <big>**nu** se poate rula din cauza permisiunilor</big>, folositi comanda:

```
sudo chmod +x checker.py
```
apoi rulati iar scripul pentru testare.