# Treść do sprawozdania W2 (wyniki z notatnika W2/W2.ipynb)

wykresy = [
    ("zadanie1.png", "[Wklej rysunek z trzema wykresami"),
    ("zadanie2.png", "[Wklej wykres sinusów 2 Hz i 10 Hz"),
    ("zadanie3.png", "[Wklej zdjęcie rysunku pięciu klatek", 6.3),
    ("zadanie4.png", "[Wklej wykres impulsu i próbek"),
    ("zadanie5.png", "[Wklej wykres próbek przed i po kwantyzacji"),
]

tabele = [
    ("fₛ [Hz]", [  # N, Ts, t7, ostatnia, próbek na okres
        ["24", "0,0833", "0,583", "1,917", "4"],
        ["48", "0,0417", "0,292", "1,958", "8"],
        ["96", "0,0208", "0,146", "1,979", "16"],
    ]),
    ("f [Hz]", [   # te same?, przeciwne?, f − k·fs, znak
        ["tak", "nie", "2 − 0·12 = 2", "+"],
        ["nie", "tak", "10 − 1·12 = −2", "−"],
        ["tak", "nie", "14 − 1·12 = 2", "+"],
        ["tak", "nie", "26 − 2·12 = 2", "+"],
    ]),
    ("tc [s]", [
        ["1,00", "1,00"],
        ["0,35", "0,90"],
        ["0 (brak impulsu)", "1,00"],
    ]),
    ("Liczba bitów B", [  # q, q/2, błąd, ≤ q/2
        ["0,25", "0,125", "0,1248", "tak"],
        ["0,0625", "0,03125", "0,0310", "tak"],
        ["0,00781", "0,00391", "0,00387", "tak"],
        ["0,00781", "0,00391", "0,2339", "nie"],
    ]),
]

zamiany = [("Odstęp w t_zle wynosi … s.", "Odstęp w t_zle wynosi 0,087 s.")]

odpowiedzi = [
    # zadanie 1
    "Po zwiększeniu fₛ próbki leżą gęściej (4, 8 i 16 na okres) i coraz lepiej odwzorowują kształt sinusa. Sam sygnał się nie zmienił – nadal ma 3 Hz; zmieniło się tylko to, jak często go mierzymy.",
    "np.linspace(0, 2, 24) dołącza także punkt końcowy 2 s, więc 24 punkty dzielą przedział na 23 odcinki: 2/23 ≈ 0,087 s. Prawidłowe chwile pomiaru daje np.arange(N)/fs, gdzie ostatnia próbka jest w 1,917 s.",
    # zadanie 2
    "Nie – przy D = 20 s porównanie dało dokładnie te same wyniki. W każdej chwili pomiaru szybszy sinus wykonuje całkowitą liczbę dodatkowych obrotów, więc próbki są identyczne niezależnie od długości zapisu.",
    # zadanie 3
    "9 · 360° / 10 = 324°, czyli tyle samo co 36° w przeciwną stronę.",
    "Na zdjęciach znacznik cofa się co klatkę o 36° (0°, 324°, 288°, 252°, 216°), więc koło wydaje się kręcić wolno do tyłu, z prędkością 36° · 10 / 360° = 1 obrót/s.",
    "Przy 10 obr/s koło między zdjęciami robi pełny obrót, więc wydaje się stać w miejscu. Przy 11 obr/s obraca się o 396° = 36° do przodu, więc widać wolny obrót do przodu, 1 obrót/s.",
    # zadanie 4
    "Przy fₛ = 20 Hz i tc = 0,225 s żadna próbka (co 50 ms: 0,20 s i 0,25 s) nie wypadła w czasie trwania impulsu (0,205–0,245 s), więc wszystkie zapisane wartości wynoszą 0.",
    "Przy fₛ = 200 Hz próbki są co 5 ms (0,210 s i 0,215 s), a szczyt jest w 0,213 s – najbliższa próbka jest 2 ms od szczytu, więc zapisuje wartość 1 − 2/20 = 0,9.",
    "Nie – zerowe próbki oznaczają tylko, że w chwilach pomiaru nic nie było; krótki impuls mógł wystąpić między próbkami.",
    # zadanie 5
    "Nie – przy 3 bitach krok wynosi 0,25 V i wszystkie próbki od ok. 0,76 do 0,93 V trafiają na ten sam poziom 0,875 V. Przetwornik zaokrągla wartości, ale ich nie ucina.",
    "Przy amplitudzie 1,2 część próbek wychodzi poza zakres ±1 V. Przetwornik zapisuje je jako skrajny poziom (±0,996 V), więc błąd wynosi do ok. 0,23 V – to błąd przesterowania, a nie kwantyzacji.",
]

chetne = [
    ("zadanie6.png", [
        "Przy fₛ = 20 Hz oba ciągi próbek to na przemian +0,5 i −0,5 (np.allclose = True), więc z samych próbek nie da się odróżnić sinusa o amplitudzie 1 od sinusa o amplitudzie 0,5.",
        "Po zmianie fₛ na 25 Hz próbki są różne (allclose = False).",
        "Przy fₛ = 2·f próbki wypadają co pół okresu i wynoszą na zmianę A·sin φ i −A·sin φ, więc znamy tylko iloczyn A·sin φ, a nie amplitudę i fazę osobno. Dlatego warunek próbkowania ma znak >, a nie ≥.",
    ]),
    ("zadanie7.png", [
        "Okno 10 µs: fₛ = 1 GSa/s, f_N = 500 MHz – sinus 1,001 MHz jest pokazany prawdziwie.",
        "Okna 10 ms i 20 ms: fₛ = 1 MSa/s i 500 kSa/s, f_N = 500 kHz i 250 kHz – sygnał 1,001 MHz jest powyżej f_N, więc ekran pokazuje alias 1 kHz (np.allclose z sinusem 1 kHz = True w obu przypadkach).",
        "Nie – po wydłużeniu okna dwa razy częstotliwość na ekranie się nie zmieniła, a mimo to odczyt był fałszywy. Pewność daje dopiero krótkie okno (szybkie próbkowanie) i sprawdzenie fₛ.",
    ]),
    ("zadanie8.png", [
        "Po zmianie fₛ na 24 Hz składowa 15 Hz trafia na 15 − 24 = −9 Hz, czyli na ujemny sinus 9 Hz o tej samej amplitudzie, który znosi prawdziwą składową 9 Hz.",
        "Bez filtru zostaje sam sinus 2 Hz (np.allclose = True). Z filtrem błąd względem s + a wynosi ok. 0,02.",
        "Filtr trzeba zastosować przed odrzuceniem próbek, bo potem alias jest już zapisany w tych samych liczbach co prawdziwy sygnał i żaden filtr go nie oddzieli.",
    ]),
]

wnioski = ("Ćwiczenia pokazały, że próbkowanie zachowuje tylko wartości w chwilach pomiaru, a wszystko, co dzieje się między nimi, "
           "jest tracone. Najbardziej zaskakujący był aliasing: sinusy 2, 14 i 26 Hz dają przy fₛ = 12 Hz dokładnie te same "
           "liczby i dłuższy zapis w niczym nie pomaga – stąd bierze się też koło kręcące się na filmie do tyłu. Krótki impuls "
           "może całkowicie zniknąć między próbkami, więc zerowe próbki nie dowodzą, że nic się nie stało. Kwantyzacja daje błąd "
           "nie większy niż q/2, ale tylko wtedy, gdy sygnał mieści się w zakresie przetwornika – przesterowanie daje błąd wielokrotnie większy.")
