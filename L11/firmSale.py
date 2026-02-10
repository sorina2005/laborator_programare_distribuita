import numpy as np


def simuleaza_date_vanzari():
    try:
        # setez o samanta pentru reproductibilitatea datelor generate
        np.random.seed(42)

        zile = 60
        date_simulare = []

        for zi in range(1, zile + 1):
            # 1. generez un numar aleatoriu de produse vandute in aceasta zi (intre 5 si 15)
            nr_produse = np.random.randint(5, 16)

            # 2. generez preturile folosind o distributie normala (media=40, deviatie=8)
            preturi = np.random.normal(40, 8, nr_produse)
            # ma asigur ca nu avem preturi negative din cauza distributiei
            preturi = np.maximum(preturi, 5)

            # 3. generez cantitatile folosind o distributie uniforma (intre 1 si 10)
            cantitati = np.random.randint(1, 11, nr_produse)

            # 4. simulez promotiile cu o probabilitate de 30% (distributie binomiala)
            # daca se aplica promotia, pretul scade cu 20%
            promotie_aplicata = np.random.binomial(1, 0.3, nr_produse)
            factor_reducere = 1 - (promotie_aplicata * 0.2)
            preturi_finale = preturi * factor_reducere

            # 5. calculez totalul vanzarilor per tranzactie si apoi per zi
            vanzari_tranzactii = preturi_finale * cantitati
            total_vanzari_zi = np.sum(vanzari_tranzactii)

            # 6. calculez profitul presupunand o marja de 30% din pretul de vanzare
            profit_zi = total_vanzari_zi * 0.3

            # stochez datele pentru analize ulterioare
            date_simulare.append({
                'zi': zi,
                'preturi': preturi_finale,
                'cantitati': cantitati,
                'vanzari': total_vanzari_zi,
                'profit': profit_zi
            })

        # extrag liste plane pentru a calcula statistici generale pe tot dataset-ul
        toate_preturile = np.concatenate([d['preturi'] for d in date_simulare])
        toate_cantitatile = np.concatenate([d['cantitati'] for d in date_simulare])
        toate_profiturile = np.array([d['profit'] for d in date_simulare])
        toate_vanzarile = np.array([d['vanzari'] for d in date_simulare])

        # 7. calculul statisticilor generale (media, max, min)
        print("--- statistici generale dataset (60 zile) ---")
        print(
            f"pret: medie={np.mean(toate_preturile):.2f}, max={np.max(toate_preturile):.2f}, min={np.min(toate_preturile):.2f}")
        print(
            f"cantitate: medie={np.mean(toate_cantitatile):.2f}, max={np.max(toate_cantitatile):.2f}, min={np.min(toate_cantitatile):.2f}")
        print(
            f"profit zilnic: medie={np.mean(toate_profiturile):.2f}, max={np.max(toate_profiturile):.2f}, min={np.min(toate_profiturile):.2f}")

        # 8. totaluri pe intreaga perioada
        print("\n--- rezultate agregate ---")
        print(f"total vanzari perioada: {np.sum(toate_vanzarile):.2f}")
        print(f"total profit perioada: {np.sum(toate_profiturile):.2f}")

    except ValueError as ve:
        # gestionez erori legate de parametrii functiilor numpy
        print(f"eroare la generarea distributiilor: {ve}")
    except Exception as e:
        # gestionez orice alta eroare neprevazuta
        print(f"a aparut o eroare in timpul simularii: {e}")


if __name__ == "__main__":
    simuleaza_date_vanzari()