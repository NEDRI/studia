# Wyniki symulacji – zadania 3 i 4

**Wynik: 13/13 porównań XOR = 0 dla wszystkich 16 kombinacji A, B, C, D – wszystkie układy zgodne.**

Model `Bramki_zad1_4.slx`, 16 symulacji (wszystkie kombinacje A, B, C, D). Wartości odczytane z zalogowanych wyjść podsystemów. Tabela pokazuje tylko zmienne, z których korzysta dany podpunkt.

## 3a)  F = ¬A·B + A·¬B + A·B   =   A + B

| A | B | F | F_upr | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 3b)  F = ¬A·¬B·C + ¬A·B·C + A·¬B·C + A·B·C   =   C

| A | B | C | F | F_upr | XOR |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 8 kombinacji, układy zgodne**

## 3c)  F = (A + ¬B)·(¬A + B)·(A + B)   =   A·B

| A | B | F | F_upr | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 3d)  F = A·B·C·¬(A·¬B·C)·(A + B + C)   =   A·B·C

| A | B | C | F | F_upr | XOR |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 8 kombinacji, układy zgodne**

## 3e)  F = ¬A·B·¬C·D + ¬A·B·C·D + A·B·¬C·D + A·B·C·D   =   B·D

| A | B | C | D | F | F_upr | XOR |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 16 kombinacji, układy zgodne**

## 3f)  F = ¬((A + B)·(¬B + A))   =   ¬A

| A | B | F | F_upr | XOR |
|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 3g)  F = (A ⊕ B) + A·B   =   A + B

| A | B | F | F_upr | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 4a)  OR z AND i NOT:   A + B = ¬(¬A·¬B)

| A | B | Y | Y_wz | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 4b)  AND z OR i NOT:   A·B = ¬(¬A + ¬B)

| A | B | Y | Y_wz | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 4c)  NAND z AND i NOT:   ¬(A·B)

| A | B | Y | Y_wz | XOR |
|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 4d)  XOR z OR, AND i NOT:   A ⊕ B = ¬A·B + A·¬B

| A | B | Y | Y_wz | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 4e)  AND z XOR i OR:   A·B = (A + B) ⊕ (A ⊕ B)

| A | B | Y | Y_wz | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

## 4f)  XOR z samych NAND (4 bramki)

| A | B | Y | Y_wz | XOR |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 |

Wynik kontroli: **XOR = 0 dla wszystkich 4 kombinacji, układy zgodne**

