class Klient():

    def __init__(self, imie , nazwisko , saldo):
        """Stwórz klienta oraz ustaw jego imie, nazwisko oraz saldo konta"""

        # Załadowanie informacji z tworzenia obiektu do obiektu
        self.imie = imie.title()
        self.nazwisko = nazwisko.title()
        self.saldo = saldo

    def przelew(self, kwota, odbiorca):
        """Prześlij środki z aktualnego konta do innego klienta"""

        if kwota <= self.saldo:
            try:
                self.saldo = self.saldo - kwota
                odbiorca.saldo = odbiorca.saldo + kwota
                print(self.saldo)
                print("Przelew został wykonany prawidłowo")
            except NameError:
                print("Nie ma takiego konta")
        else:
            print("Przepraszamy: przelew nie mógł zostac zrealizowany")



