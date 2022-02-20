
import funkcje_banku as fb


def main():
    odp = 0
    klienci = fb.stworz_klientow()

    while odp != 3:
        fb.przywitanie()


        a = 2
        odp = fb.odpowiedz()
        if odp == 1:
            for klient in klienci:
                print(f"{klient.imie} {klient.nazwisko} Saldo: {klient.saldo} \n")
        elif odp == 2:
            numer_konta = int(input("prosze podać numer konta 1 - 5")) - 1
            chce = int(input("Czy chcesz wykonać przelew? 1 - tak / 2 - nie"))
            if chce == 1:
                odbiorca = int(input(f"do kogo od 1 - 5| oprócz {numer_konta + 1}"))
                ilosc = int(input("Ile mamony byczku"))
                klienci[numer_konta].przelew(ilosc, klienci[odbiorca - 1])

        elif odp == 3:
            print("Do widzenia oraz dziekujemy za skorzystanie z usług naszego banku")
        else:
            print("Prosze podać odpowiedz z zakresu 1 - 3 ")




main()



