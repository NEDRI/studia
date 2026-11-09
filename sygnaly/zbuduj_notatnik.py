"""Uruchamia komórki zadań, zapisuje wykresy PNG i notatnik .ipynb z wynikami.
Użycie: python zbuduj_notatnik.py komorki_W1.py W1
Plik komórek dzieli komórki liniami '# %%' (kod) i '# %% [markdown]' (tekst)."""
import base64, contextlib, io, json, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

src, outdir = sys.argv[1], sys.argv[2]
os.chdir(outdir)
cells, cur, kind = [], [], None
for line in open(os.path.join("..", src), encoding="utf-8").read().split("\n"):
    if line.startswith("# %%"):
        if kind: cells.append((kind, "\n".join(cur).strip("\n")))
        kind, cur = ("markdown" if "[markdown]" in line else "code"), []
    else:
        cur.append(line)
if kind: cells.append((kind, "\n".join(cur).strip("\n")))

ns, nb_cells, count = {}, [], 0
plt.show = lambda *a, **k: None          # wykresy zbieramy sami
for kind, text in cells:
    lines = [l + "\n" for l in text.split("\n")]; lines[-1] = lines[-1].rstrip("\n")
    if kind == "markdown":
        nb_cells.append({"cell_type": "markdown", "metadata": {},
                         "source": [l[2:] if l.startswith("# ") else l.lstrip("#") for l in lines]})
        continue
    count += 1
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(text, f"<komórka {count}>", "exec"), ns)
    outputs = []
    if buf.getvalue():
        outputs.append({"output_type": "stream", "name": "stdout", "text": buf.getvalue()})
        print(f"--- komórka {count}\n{buf.getvalue()}", end="")
    for num in plt.get_fignums():
        b = io.BytesIO(); plt.figure(num).savefig(b, format="png", dpi=90)
        outputs.append({"output_type": "display_data", "metadata": {},
                        "data": {"image/png": base64.b64encode(b.getvalue()).decode(), "text/plain": "<Figure>"}})
    plt.close("all")
    nb_cells.append({"cell_type": "code", "execution_count": count, "metadata": {},
                     "outputs": outputs, "source": lines})
nb = {"cells": nb_cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
      "language_info": {"name": "python"}}, "nbformat": 4, "nbformat_minor": 5}
json.dump(nb, open(f"{outdir}.ipynb", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("zapisano", f"{outdir}/{outdir}.ipynb")
