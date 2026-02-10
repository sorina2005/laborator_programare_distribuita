import requests


def convertor_valutar():
    # definesc url-ul de baza pentru api-ul de schimb valutar
    # folosim varianta de api care nu necesita cheie pentru uz educational
    api_url = "https://api.exchangerate-api.com/v4/latest/"

    try:
        # 1. solicit datele de intrare de la utilizator
        moneda_sursa = input("introdu moneda de provenienta (ex: EUR, USD, RON): ").strip().upper()
        moneda_destinatie = input("introdu moneda de destinatie (ex: EUR, USD, RON): ").strip().upper()

        try:
            suma_initiala = float(input("introdu suma pe care doresti sa o convertesti: "))
            if suma_initiala < 0:
                print("eroare: suma nu poate fi negativa.")
                return
        except ValueError:
            print("eroare: te rog sa introduci o valoare numerica valida pentru suma.")
            return

        # 2. interoghez api-ul pentru a obtine ratele de schimb actuale
        # fac cererea folosind moneda sursa ca baza pentru a simplifica calculul
        raspuns = requests.get(f"{api_url}{moneda_sursa}", timeout=10)

        # verific daca api-ul a returnat un raspuns valid (ex: daca codul monedei exista)
        raspuns.raise_for_status()
        date = raspuns.json()

        # 3. extrag rata de schimb si efectuez calculul conversiei
        # verific daca moneda de destinatie exista in datele primite
        rate_schimb = date.get("rates", {})

        if moneda_destinatie in rate_schimb:
            curs_schimb = rate_schimb[moneda_destinatie]
            suma_finala = suma_initiala * curs_schimb

            # 4. afisez rezultatele procesului de conversie
            print("\n" + "=" * 40)
            print(f"rezultat conversie: {moneda_sursa} -> {moneda_destinatie}")
            print("-" * 40)
            print(f"suma initiala:    {suma_initiala:.2f} {moneda_sursa}")
            print(f"curs de schimb:   1 {moneda_sursa} = {curs_schimb:.4f} {moneda_destinatie}")
            print(f"suma finala:      {suma_finala:.2f} {moneda_destinatie}")
            print("=" * 40)
        else:
            print(f"eroare: moneda de destinatie '{moneda_destinatie}' nu a fost gasita.")

    except requests.exceptions.HTTPError:
        # gestionez cazul in care moneda sursa este gresita sau api-ul are probleme
        print(f"eroare: moneda '{moneda_sursa}' nu este valida sau serverul nu raspunde.")
    except requests.exceptions.ConnectionError:
        # gestionez lipsa conexiunii la internet
        print("eroare: nu s-a putut stabili o conexiune cu serverul de schimb valutar.")
    except Exception as e:
        # captez orice alta eroare neprevazuta pentru siguranta programului
        print(f"a aparut o eroare neasteptata: {e}")


if __name__ == "__main__":
    # pornesc executia aplicatiei
    convertor_valutar()