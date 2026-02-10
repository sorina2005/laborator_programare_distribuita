import requests
from tabulate import tabulate


def proceseaza_date_utilizatori():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # trimit cererea get catre api pentru a prelua lista de utilizatori
        raspuns = requests.get(url, timeout=10)

        # verific daca cererea a avut succes (cod status 200)
        raspuns.raise_for_status()

        # decodez continutul json primit intr-o lista de dictionare
        utilizatori = raspuns.json()

        # pregatesc o lista pentru stocarea datelor prelucrate sub forma de randuri
        date_tabel = []

        for u in utilizatori:
            # extrag datele solicitate, inclusiv cele din dictionare imbricate (adresa, companie)
            rand = [
                u.get('id'),
                u.get('name'),
                u.get('username'),
                u.get('email'),
                u.get('address', {}).get('city'),
                u.get('company', {}).get('name'),
                u.get('phone'),
                u.get('website')
            ]
            date_tabel.append(rand)

        # definesc antetele pentru tabelul final
        headere = ["id", "nume", "username", "email", "oras", "companie", "telefon", "website"]

        # afisez toti utilizatorii intr-un format tabelar curat
        print("\n--- lista completa a utilizatorilor ---")
        print(tabulate(date_tabel, headers=headere, tablefmt="grid"))

        # filtrare date: afisez doar utilizatorii din orasul 'gwenborough'
        oras_tinta = "gwenborough"
        date_filtrate = [rand for rand in date_tabel if rand[4].lower() == oras_tinta.lower()]

        print(f"\n--- utilizatori filtrati dupa orasul: {oras_tinta} ---")
        if date_filtrate:
            print(tabulate(date_filtrate, headers=headere, tablefmt="grid"))
        else:
            print(f"nu s-au gasit utilizatori in orasul {oras_tinta}.")

    except requests.exceptions.HTTPError as errh:
        # gestionez erorile de tip http (ex: 404, 500)
        print(f"eroare http: {errh}")
    except requests.exceptions.ConnectionError:
        # gestionez problemele de conectivitate la internet sau dns
        print("eroare: nu s-a putut stabili conexiunea cu serverul.")
    except requests.exceptions.Timeout:
        # gestionez situatia in care serverul raspunde prea greu
        print("eroare: cererea a expirat (timeout).")
    except requests.exceptions.RequestException as e:
        # captez orice alta exceptie legata de biblioteca requests
        print(f"eroare neprevazuta la interogarea api: {e}")
    except Exception as e:
        # masura de siguranta pentru erori de logica sau prelucrare
        print(f"a aparut o eroare generala: {e}")


if __name__ == "__main__":
    # pornesc executia scriptului
    proceseaza_date_utilizatori()