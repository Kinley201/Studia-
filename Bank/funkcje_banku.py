from klient import Klient


def przywitanie():
    print("WITAMY W APLIKACJI NASZEGO BANKU GABRYS S.A")
    print("Aby wyświetlić liste klientów kliknij -      [1]")
    print("Aby zalogowac sie na konto klienta kliknij - [2]")
    print("Aby wyjśc kliknij -                          [3]")

def stworz_klientow():
    klient1 = Klient("andrzej","sieruta", 10000)
    klient2 = Klient("marcin", "kobala", 500)
    klient3 = Klient("kacper","maluch", 17000)
    klient4 = Klient("krystyna", "blachowicz", 10)
    klient5 = Klient("ania","Githubowa", 9000)

    klienci = [klient1, klient2, klient3, klient4, klient5]

    return klienci


def odpowiedz():
    try:
        odp = int(input())
    except ValueError:
        None
    return odp