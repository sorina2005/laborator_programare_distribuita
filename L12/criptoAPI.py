import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def obtine_date_cripto():
    # definesc url-urile pentru api si pentru scraping
    url_preturi = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    url_stiri = "https://www.coindesk.com/"

    # setez un header pentru a simula un browser real la scraping
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # 1. interogarea api-ului coingecko pentru preturi
    try:
        raspuns_api = requests.get(url_preturi, timeout=10)
        raspuns_api.raise_for_status()
        date_preturi = raspuns_api.json()

        # pregatesc datele pentru tabel
        tabel_preturi = [
            ["Bitcoin", f"${date_preturi['bitcoin']['usd']:,}"],
            ["Ethereum", f"${date_preturi['ethereum']['usd']:,}"]
        ]

        print("\n--- preturi actuale cripto ---")
        print(tabulate(tabel_preturi, headers=["Moneda", "Pret (USD)"], tablefmt="grid"))

    except requests.exceptions.RequestException as e:
        # gestionez erorile de retea pentru api
        print(f"eroare la accesarea api-ului coingecko: {e}")
    except KeyError:
        # gestionez cazul in care structura json s-a modificat
        print("eroare: datele despre preturi nu au putut fi extrase corect.")

    # 2. web scraping pentru ultimele 5 stiri de pe coindesk
    try:
        raspuns_stiri = requests.get(url_stiri, headers=headers, timeout=10)
        raspuns_stiri.raise_for_status()

        # parsez continutul html folosind beautifulsoup
        soup = BeautifulSoup(raspuns_stiri.text, 'html.parser')

        # caut elementele care contin titlurile stirilor (selector specific coindesk)
        # nota: selectorii se pot schimba daca site-ul isi modifica structura
        stiri = []
        elemente_stiri = soup.find_all('h3', limit=10)  # caut h3-uri, apoi le filtram pe cele relevante

        for el in elemente_stiri:
            titlu = el.get_text().strip()
            # incerc sa gasesc link-ul parinte sau copil
            link_tag = el.find('a') or el.find_parent('a')

            if link_tag and link_tag.get('href'):
                href = link_tag.get('href')
                # ma asigur ca am un link complet
                link_complet = href if href.startswith('http') else f"https://www.coindesk.com{href}"

                if titlu and link_complet not in [s[1] for s in stiri]:
                    stiri.append((titlu, link_complet))

            # ma opresc cand am 5 stiri valide
            if len(stiri) == 5:
                break

        print("\n--- ultimele 5 stiri coindesk ---")
        if not stiri:
            print("nu s-au putut extrage stiri. structura site-ului s-ar putea sa fie modificata.")
        else:
            for i, (titlu, link) in enumerate(stiri, 1):
                print(f"{i}. {titlu}")
                print(f"   Link: {link}\n")

    except requests.exceptions.RequestException as e:
        # gestionez erorile de retea pentru site-ul de stiri
        print(f"eroare la accesarea coindesk: {e}")
    except Exception as e:
        # captez orice alta eroare neprevazuta in timpul parsarii
        print(f"a aparut o eroare la extragerea stirilor: {e}")


if __name__ == "__main__":
    obtine_date_cripto()