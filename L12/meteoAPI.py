import requests


def obtine_vremea():
    # cer utilizatorului numele orasului
    oras = input("introdu numele orasului pentru prognoza: ").strip()

    # verific daca input-ul este valid
    if not oras:
        print("eroare: numele orasului nu poate fi gol.")
        return

    # url-ul pentru api-ul wttr.in cu format json (j1)
    url = f"https://wttr.in/{oras}?format=j1"

    try:
        # incerc sa fac cererea get cu verificarea ssl activata initial
        raspuns = requests.get(url, timeout=10)
        raspuns.raise_for_status()

    except requests.exceptions.SSLError:
        # daca apare o eroare de ssl, incerc din nou fara verificarea certificatului
        print("avertisment: eroare ssl detectata. incerc conectarea fara verificare...")
        try:
            raspuns = requests.get(url, timeout=10, verify=False)
            raspuns.raise_for_status()
        except Exception as e:
            print(f"eroare critica la conectarea fara ssl: {e}")
            return

    except requests.exceptions.HTTPError:
        print(f"eroare: orasul '{oras}' nu a fost gasit sau api-ul este indisponibil.")
        return
    except Exception as e:
        print(f"eroare la conectarea la api: {e}")
        return

    try:
        # procesez datele primite in format json
        date_meteo = raspuns.json()

        # extrag informatiile cerute din structura specifica wttr.in
        conditie = date_meteo['current_condition'][0]['lang_ro'][0]['value'] if 'lang_ro' in \
                                                                                date_meteo['current_condition'][0] else \
        date_meteo['current_condition'][0]['weatherDesc'][0]['value']
        temperatura = date_meteo['current_condition'][0]['temp_C']
        viteza_vant = date_meteo['current_condition'][0]['windspeedKmph']
        directia_vant = date_meteo['current_condition'][0]['winddir16Point']

        # afisez datele intr-un format academic si clar
        print("\n" + "=" * 30)
        print(f"starea vremii in {oras.upper()}")
        print("-" * 30)
        print(f"conditii:    {conditie}")
        print(f"temperatura: {temperatura} grade celsius")
        print(f"vant:        {directia_vant} cu viteza de {viteza_vant} km/h")
        print("=" * 30)

    except (KeyError, IndexError):
        # gestionez situatia in care structura json nu este cea asteptata
        print("eroare: datele primite de la api au un format neasteptat.")
    except Exception as e:
        print(f"a aparut o eroare la prelucrarea datelor: {e}")


if __name__ == "__main__":
    # pornesc programul
    obtine_vremea()