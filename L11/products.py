import numpy as np
import matplotlib.pyplot as plt


def analizeaza_performanta_vanzari(date_simulare):
    try:
        # ma asigur ca am primit date pentru procesare
        if not date_simulare:
            raise ValueError("lista de date pentru simulare este goala.")

        # 1. evolutia veniturilor si profitului pe zile
        zile = np.array([d['zi'] for d in date_simulare])
        venituri_zilnice = np.array([d['vanzari'] for d in date_simulare])
        profituri_zilnice = np.array([d['profit'] for d in date_simulare])

        # pregatesc datele pentru vizualizare cronologica
        print("--- date pentru evolutia zilnica ---")
        print(f"zile procesate: {len(zile)}")
        print(f"venit maxim inregistrat intr-o zi: {np.max(venituri_zilnice):.2f}")

        # 2. distributia preturilor si cantitatilor
        # concatenez toate datele din liste pentru a avea o viziune de ansamblu
        toate_preturile = np.concatenate([d['preturi'] for d in date_simulare])
        toate_cantitatile = np.concatenate([d['cantitati'] for d in date_simulare])

        # calculez distributia (histograma) pentru preturi
        frecvente_preturi, margini_preturi = np.histogram(toate_preturile, bins=10)

        print("\n--- distributia preturilor (frecvente per interval) ---")
        print(frecvente_preturi)

        # 3. vizualizarea si impactul promotiilor
        impact_promotii = []
        for d in date_simulare:
            # identific daca pretul a fost influentat de promotie
            # (stim ca pretul original era in jur de 40, fara reducerea de 20%)
            # aici verificam logica aplicata in simularea anterioara
            preturi_zi = d['preturi']
            # consideram o zi cu promotii daca exista preturi sub pragul teoretic minim normal
            # sau folosim logica de comparatie directa daca am fi salvat flag-ul de promotie

            # calculez reducerea medie in ziua respectiva
            reducere_medie = np.mean(preturi_zi)
            impact_promotii.append(reducere_medie)

        print("\n--- analiza impactului promotiilor ---")
        print("datele au fost organizate pentru generarea graficelor.")

        # generarea vizualizarilor (matplotlib)
        # folosesc subplots pentru a prezenta totul intr-o singura figura academica
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

        # grafic pentru evolutia veniturilor si profitului
        ax1.plot(zile, venituri_zilnice, label='venit total', color='blue', marker='o')
        ax1.plot(zile, profituri_zilnice, label='profit total', color='green', linestyle='--')
        ax1.set_title('evolutia financiara pe 60 de zile')
        ax1.set_xlabel('ziua')
        ax1.set_ylabel('valoare monetara')
        ax1.legend()
        ax1.grid(True)

        # histograma pentru distributia preturilor
        ax2.hist(toate_preturile, bins=15, color='orange', edgecolor='black')
        ax2.set_title('distributia preturilor finale de vanzare')
        ax2.set_xlabel('pret unitar')
        ax2.set_ylabel('frecventa aparitiei')

        plt.tight_layout()
        plt.show()

    except KeyError as ke:
        # gestionez cazul in care dictionarul de date nu are cheile asteptate
        print(f"eroare: structura datelor de intrare este incorecta: {ke}")
    except Exception as e:
        # captez orice alta eroare de calcul sau vizualizare
        print(f"a aparut o eroare la analiza datelor: {e}")

