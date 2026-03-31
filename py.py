import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Weryfikacja parametrów: Używamy klasycznego trójkąta 3-4-5 dla idealnej czytelności
R = 4.0  # Rezystancja [Ohm] - oś rzeczywista
X = 3.0  # Reaktancja [Ohm] - oś urojona
Z_complex = R + 1j * X # Impedancja zespolona

# Inicjalizacja wykresu
fig, ax = plt.subplots(figsize=(10, 6))

# Rysowanie głównych osi płaszczyzny zespolonej
ax.axhline(0, color='black', linewidth=1.5)
ax.axvline(0, color='black', linewidth=1.5)

# Funkcja pomocnicza do rysowania wektorów
def draw_vector(start_x, start_y, end_x, end_y, color, label, text_offset_x=0, text_offset_y=0):
    ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                arrowprops=dict(arrowstyle='->', color=color, lw=3))
    mid_x = (start_x + end_x) / 2
    mid_y = (start_y + end_y) / 2
    ax.text(mid_x + text_offset_x, mid_y + text_offset_y, label, 
            color=color, fontsize=13, weight='bold', ha='center', va='center',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

# --- RYSOWANIE TRÓJKĄTA IMPEDANCJI ---
draw_vector(0, 0, R, 0, 'firebrick', 'R (Rezystancja)', text_offset_x=0, text_offset_y=-0.5)
draw_vector(R, 0, R, X, 'darkorange', 'X (Reaktancja)', text_offset_x=0.9, text_offset_y=0)
# POPRAWKA: Usunięto \underline, używamy zwykłego Z w notacji matematycznej
draw_vector(0, 0, R, X, 'royalblue', r'$Z$ (Impedancja)', text_offset_x=-0.8, text_offset_y=0.5)

# --- DODATKI GEOMETRYCZNE I EDUKACYJNE ---
theta = np.degrees(np.arctan2(X, R))
arc = patches.Arc((0, 0), 1.5, 1.5, angle=0, theta1=0, theta2=theta, color='black', lw=1.5)
ax.add_patch(arc)
ax.text(0.9, 0.25, r'$\phi$', fontsize=16, weight='bold')

rect = patches.Rectangle((R - 0.2, 0), 0.2, 0.2, linewidth=1.5, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# POPRAWKA: Usunięto \underline ze wzorów
info_text = (
    "LEGENDA I WZORY:\n\n"
    r"$Z = R + jX$" + "  (Postać algebraiczna)\n"
    r"$|Z| = \sqrt{R^2 + X^2}$" + "  (Moduł / Prawo Pitagorasa)\n"
    r"$\phi = \arctan\left(\frac{X}{R}\right)$" + "  (Kąt fazowy)"
)
props = dict(boxstyle='round,pad=0.5', facecolor='aliceblue', alpha=0.95, edgecolor='steelblue')
ax.text(0.03, 0.95, info_text, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# --- KONFIGURACJA WYGLĄDU WYKRESU ---
ax.set_xlim(-1, R + 2.5)
ax.set_ylim(-1, X + 1.5)
ax.set_title('Trójkąt Impedancji na Płaszczyźnie Zespolonej', fontsize=15, weight='bold', pad=15)
# POPRAWKA: Dodano literkę 'r' przed stringami z \Omega
ax.set_xlabel(r'Oś Rzeczywista (Re) [$\Omega$]', fontsize=12)
ax.set_ylabel(r'Oś Urojona (Im) [$\Omega$]', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)

ax.set_aspect('equal', adjustable='box') 

plt.tight_layout()
plt.show()