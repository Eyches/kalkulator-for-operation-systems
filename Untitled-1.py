def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Błąd: Dzielenie przez zero!"

# Funkcja do obsługi kalkulatora
def kalkulator():
    print("Prosty kalkulator")
    print("Dostępne operacje:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz operację (wpisz numer): ")

    if wybor in ('1', '2', '3', '4'):
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            wynik = dodawanie(a, b)
        elif wybor == '2':
            wynik = odejmowanie(a, b)
        elif wybor == '3':
            wynik = mnozenie(a, b)
        elif wybor == '4':
            wynik = dzielenie(a, b)

        print("Wynik: ", wynik)
    else:
        print("Błędny wybór operacji.")

# Uruchamianie kalkulatora
kalkulator()