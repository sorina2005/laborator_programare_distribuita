import pandas as pd


def analiza_vanzari_csv(cale_fisier):
    try:
        # incarc datele din fisierul csv specificat
        df = pd.read_csv(cale_fisier)

        # verific daca toate coloanele din fisierul tau sunt prezente
        coloane_necesare = ['Produs', 'Cantitate', 'Pret', 'Data']
        for col in coloane_necesare:
            if col not in df.columns:
                raise KeyError(f"coloana '{col}' lipseste din fisier.")

        # convertesc coloana Data la format datetime (formatul din fisier: m/d/y)
        df['Data'] = pd.to_datetime(df['Data'])

        # calculez venitul pentru fiecare tranzactie (cantitate * pret)
        df['Venit_Total'] = df['Cantitate'] * df['Pret']

        # extrag luna si anul sub forma de perioada pentru grupari statistice
        df['Luna_An'] = df['Data'].dt.to_period('M')

        # 1. cele mai vandute produse pe luna (dupa cantitate)
        # grupez datele si caut indexul valorii maxime pentru fiecare perioada
        grup_cantitate = df.groupby(['Luna_An', 'Produs'])['Cantitate'].sum().reset_index()
        top_produse = grup_cantitate.loc[grup_cantitate.groupby('Luna_An')['Cantitate'].idxmax()]

        print("--- cele mai vandute produse pe luna ---")
        print(top_produse)

        # 2. venitul total pe fiecare produs
        # fac suma veniturilor pentru fiecare categorie de produs
        venit_produs = df.groupby('Produs')['Venit_Total'].sum().sort_values(ascending=False)
        print("\n--- venitul total pe fiecare produs ---")
        print(venit_produs)

        # 3. filtrare pentru intervalul 01.01.2023 - 31.03.2023 (primul trimestru)
        # aplic o masca booleana pentru a filtra randurile din intervalul dorit
        masca_t1 = (df['Data'] >= '2023-01-01') & (df['Data'] <= '2023-03-31')
        vanzari_filtrate = df[masca_t1]
        print("\n--- vanzari filtrate (trimestrul 1 2023) ---")
        print(vanzari_filtrate)

        # 4. venitul mediu lunar pe intreaga perioada
        # calculez totalul pe fiecare luna si apoi fac media acestor sume
        total_venit_lunar = df.groupby('Luna_An')['Venit_Total'].sum()
        venit_mediu = total_venit_lunar.mean()
        print(f"\nvenitul mediu lunar: {venit_mediu:.2f}")

    except FileNotFoundError:
        # gestionez cazul in care fisierul nu se afla in folderul de lucru
        print(f"eroare: nu am putut gasi fisierul '{cale_fisier}'.")
    except ValueError:
        # gestionez erori de conversie a datelor (ex: text in loc de numere)
        print("eroare: datele din fisier au un format invalid pentru calcule.")
    except Exception as e:
        # captez orice alta eroare neprevazuta pentru siguranta executiei
        print(f"a aparut o problema neasteptata: {e}")


# apelez functia de procesare
if __name__ == "__main__":
    analiza_vanzari_csv('vanzari_companie.csv')