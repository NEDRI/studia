# Treść do sprawozdania W1 (wyniki z notatnika W1/W1.ipynb)

wykresy = [
    ("zadanie1.png", "[Wklej rysunek z pięcioma wykresami"),
    ("zadanie2.png", "[Wklej rysunek z czterema sygnałami"),
    ("zadanie3.png", "[Wklej rysunek z czterema wariantami"),
    ("zadanie4.png", "[Wklej rysunek ze składowymi"),
    ("zadanie5.png", "[Wklej zdjęcie rysunku x(t) i z[n]"),
]

tabele = [
    ("Wariant", [  # T, min, max, x(0)
        ["0,333", "−2", "2", "0"],
        ["0,333", "−1", "1", "0"],
        ["0,167", "−2", "2", "0"],
        ["0,333", "−2", "2", "2"],
        ["0,333", "−1", "3", "1"],
    ]),
    ("Sygnał", [   # t = −0,5; 0; 0,5; 1; 2
        ["0", "1", "1", "1", "1"],
        ["0", "1", "1", "0", "0"],
        ["0", "0", "0,5", "1", "2"],
        ["0", "1", "0,368", "0,135", "0,018"],
    ]),
    ("Wariant", [  # szczyt, przedział > 0, zgodność
        ["0", "−1 < t < 1", "tak"],
        ["1", "0 < t < 2", "tak"],
        ["0", "−0,5 < t < 0,5", "tak"],
        ["0", "−1 < t < 1", "tak"],
    ]),
    ("x(0)", [["2", "−1", "2", "0"]]),
]

odpowiedzi = [
    # zadanie 1
    "Amplituda A określa, jak daleko sygnał odchyla się od swojego poziomu środkowego: przy A = 1 sinus mieści się w przedziale od −1 do 1 zamiast od −2 do 2.",
    "Częstotliwość f mówi, ile pełnych okresów przypada na sekundę; po zmianie z 3 Hz na 6 Hz okres skrócił się z 0,333 s do 0,167 s, a kształt i zakres wartości się nie zmieniły.",
    "Faza φ przesuwa sinus w czasie, czyli zmienia, w którym miejscu okresu zaczyna się wykres; przy φ = π/2 sygnał startuje od szczytu, więc x(0) = 2.",
    "Przesunięcie C podnosi cały wykres do góry o stałą wartość: przy C = 1 sinus drga wokół 1 (od −1 do 3), a jego amplituda nadal wynosi 2.",
    # zadanie 2
    "Żaden z tych czterech sygnałów nie jest okresowy, bo żaden fragment wykresu nie powtarza się w nieskończoność.",
    "Bez końca rośnie tylko rampa r(t) = t dla t ≥ 0; skok zatrzymuje się na 1, a prostokąt i sygnał wykładniczy wracają do zera.",
    "p(1) = 0, ponieważ prostokąt jest określony warunkiem 0 ≤ t < 1, więc sama chwila t = 1 już do niego nie należy.",
    # zadanie 3
    "Przewidywania zgodziły się z wykresami. Najłatwiej o pomyłkę przy s(t − 1): mimo minusa w nawiasie trójkąt przesuwa się w prawo, bo szczyt jest tam, gdzie t − 1 = 0, czyli w t = 1.",
    "Trójkąt jest symetryczny względem t = 0, więc odbicie względem osi pionowej nic nie zmienia: s(−t) = s(t). Taki sygnał nazywamy parzystym.",
    # zadanie 4
    "0,5 s – w tym czasie sinus 2 Hz wykonuje dokładnie jeden okres, a sinus 6 Hz dokładnie trzy, więc obie składowe wracają do tych samych wartości.",
    "Powolny wzrost daje składowa d = 0,2·t, a „górkę” w okolicy t = 2 s daje składowa g (impuls gaussowski o szerokości ok. 0,15 s).",
    "Nie – trend d stale rośnie, a górka g występuje tylko raz, więc przesunięcie sygnału o 0,5 s go nie odtwarza (w notatniku porównanie x(t + 0,5) z x(t) dało False).",
    "Tak – każda składowa jest opisana wzorem bez losowości, więc wartość x w dowolnej chwili można dokładnie obliczyć.",
    # zadanie 5
    "Nie – z[n] jest sygnałem dyskretnym i ma wartości tylko dla całkowitych n. Sygnał x(t) jest natomiast sygnałem ciągłym i ma wartość w każdej chwili, także w miejscach skoków.",
]

chetne = [
    ("zadanie6.png", [
        "Średnia szumu wyniosła −0,0087, a odchylenie 0,2966 – blisko 0 i 0,3, ale nie dokładnie, bo 1000 losowych liczb to tylko skończona próbka rozkładu.",
        "Generator z tym samym ziarnem 42 dał identyczny szum (np.array_equal = True), a z ziarnem 43 inny (False).",
        "Ziarno ustawia się po to, żeby „losowy” eksperyment dało się powtórzyć i uzyskać te same wyniki, np. przy sprawdzaniu ćwiczeń lub porównywaniu algorytmów.",
    ]),
    ("zadanie7.png", [
        "Przed uruchomieniem: a(t) jest okresowy z okresem 1 s (2 okresy składowej 2 Hz i 3 okresy składowej 3 Hz), a b(t) nie jest okresowy.",
        "Wynik: dla a(t) różnica po przesunięciu o 1 s i 2 s wynosi ok. 1e−14, czyli zero; dla b(t) przy każdym T zostaje różnica 0,5–1.",
        "Dla b(t) nie ma okresu, bo 2 i √2 nie mają wspólnej wielokrotności – żaden czas T nie mieści całkowitej liczby okresów obu składowych.",
    ]),
    ("zadanie8.png", [
        "x: średnia 0, RMS 0,707. Dla 2·x średnia nadal wynosi 0, a RMS rośnie dwukrotnie do 1,414.",
        "Sygnał y = sin(2π·2·t + 1) ma tę samą średnią (0) i RMS (0,707), ale jest przesunięty w czasie, więc wygląda inaczej.",
        "Średnia równa zero nie oznacza braku sygnału – sinus ma średnią 0, choć ma dużą amplitudę. Dwie liczby nie opisują kształtu sygnału.",
    ]),
]

wnioski = ("Ćwiczenia pokazały, że każdy parametr sinusoidy odpowiada za inną cechę wykresu: A za zakres drgań, f za tempo, "
           "φ za położenie w czasie, a C za poziom środkowy. Przekształcenia s(t − 1), s(2t) i s(−t) najłatwiej przewidzieć, "
           "szukając chwili, w której wyrażenie w nawiasie jest równe zero. Zaskakujące było to, że minus w s(t − 1) przesuwa "
           "sygnał w prawo, a także to, że suma dwóch sinusoid nie zawsze jest okresowa. Najwięcej uwagi wymagało pilnowanie "
           "granic przedziałów (≤ czy <), od których zależą wartości w punktach skoku, np. p(1) = 0.")
