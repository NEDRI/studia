"""Wypełnia rozpakowany wzór sprawozdania (.docx) danymi z pliku dane_Wx.py.
Użycie: python wypelnij_wzor.py <katalog_rozpakowanego_wzoru> <dane_Wx.py> <katalog_z_wykresami>"""
import os, re, runpy, shutil, sys
from PIL import Image
from lxml import etree

d, dane_py, img_dir = sys.argv[1:]
D = runpy.run_path(dane_py)
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
q = lambda tag: f"{{{W}}}{tag}"
doc_path = os.path.join(d, "word", "document.xml")
tree = etree.parse(doc_path)
body = tree.getroot().find("w:body", NS)


def text(el):
    return "".join(el.itertext()).strip()


def set_par_text(p, txt, keep_style_run=None, plain=True):
    """Zastępuje zawartość akapitu jednym przebiegiem z tekstem."""
    rpr = None
    old = p.find("w:r", NS) if keep_style_run is None else keep_style_run
    if old is not None and old.find("w:rPr", NS) is not None:
        rpr = etree.fromstring(etree.tostring(old.find("w:rPr", NS)))
        if plain:  # usuń kursywę i szary kolor podpowiedzi
            for t in ("i", "iCs", "color"):
                for e in rpr.findall(f"w:{t}", NS):
                    rpr.remove(e)
    for r in p.findall("w:r", NS):
        p.remove(r)
    r = etree.SubElement(p, q("r"))
    if rpr is not None:
        r.append(rpr)
    t = etree.SubElement(r, q("t"))
    t.text = txt
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")


# --- obrazy -----------------------------------------------------------------
rels_path = os.path.join(d, "word", "_rels", "document.xml.rels")
rels = open(rels_path, encoding="utf-8").read()
os.makedirs(os.path.join(d, "word", "media"), exist_ok=True)
img_id = [100]


def image_run(png, width_in=4.8):
    img_id[0] += 1
    n = img_id[0]
    name = f"wykres{n}.png"
    shutil.copy(os.path.join(img_dir, png), os.path.join(d, "word", "media", name))
    global rels
    rid = f"rIdImg{n}"
    rels = rels.replace("</Relationships>",
        f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{name}"/></Relationships>')
    w, h = Image.open(os.path.join(img_dir, png)).size
    cx = int(width_in * 914400); cy = int(cx * h / w)
    xml = f'''<w:r xmlns:w="{W}" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
 xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{n}" name="Wykres {n}"/><wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>
<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic><pic:nvPicPr><pic:cNvPr id="{n}" name="{name}"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill><pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>'''
    return etree.fromstring(xml)


def put_image(p, png, width_in=4.8):
    for r in p.findall("w:r", NS):
        p.remove(r)
    p.append(image_run(png, width_in))


# --- wypełnianie --------------------------------------------------------------
pars = list(body.iter(q("p")))
for png, needle, *szer in D["wykresy"]:       # ramki „[Wklej …]”; opcjonalnie szerokość w calach
    p = next(p for p in pars if needle in text(p))
    put_image(p, png, *szer)
    tc = p.getparent()
    if tc.tag == q("tc"):                      # ramka: zdejmij stałą wysokość i przerywane obramowanie
        tbl = tc.getparent().getparent()
        for e in tbl.iter(q("trHeight")):
            e.getparent().remove(e)
        for e in tbl.iter():
            if e.get(q("val")) == "dashed":
                e.set(q("val"), "nil")

for header, rows in D["tabele"]:              # tabele wyników: puste komórki po kolei
    tbl = next(t for t in body.iter(q("tbl")) if text(t.find(".//w:tc", NS)) == header
               and any(not text(tc) for tc in t.iter(q("tc"))))
    vals = [v for row in rows for v in row]
    for tc in tbl.iter(q("tc")):
        if not text(tc) and vals:
            p = tc.find("w:p", NS)
            ref = tbl.find(".//w:tr[2]//w:r", NS)     # styl czcionki jak w wypełnionych komórkach
            set_par_text(p, vals.pop(0), keep_style_run=ref)
            for b in p.iter(q("b")):
                b.getparent().remove(b)
    assert not vals, (header, vals)

odp = list(D["odpowiedzi"])
for p in pars:
    if text(p) == "[odpowiedź]":
        set_par_text(p, odp.pop(0))
    elif text(p).startswith("[3–5 zdań"):
        set_par_text(p, D["wnioski"])
    elif "…" in text(p) and D.get("zamiany"):
        for old, new in D["zamiany"]:
            for t in p.iter(q("t")):
                if t.text and old in t.text:
                    t.text = t.text.replace(old, new)
assert not odp, odp

for p in [p for p in pars if text(p) == "[wykres i odpowiedzi]"]:   # zadania dla chętnych
    png, linie = D["chetne"].pop(0)
    parent, idx = p.getparent(), p.getparent().index(p)
    for i, linia in enumerate(reversed(linie)):
        np_ = etree.fromstring(etree.tostring(p))
        set_par_text(np_, linia)
        parent.insert(idx + 1, np_)
    put_image(p, png, 4.2)
    pPr = p.find("w:pPr", NS)
    jc = etree.Element(q("jc")); jc.set(q("val"), "center")
    rPr = pPr.find("w:rPr", NS)               # kolejność w pPr: jc przed rPr
    if rPr is not None:
        rPr.addprevious(jc)
    else:
        pPr.append(jc)

for p in pars:                                 # zdanie „usuń tę część” przy zadaniach dla chętnych
    if text(p).startswith("Jeśli wykonałeś któreś z tych zadań"):
        p.getparent().remove(p)

# ramka „Jak wypełnić ten wzór” – usuwamy cały element najwyższego poziomu
for child in list(body):
    if any(k in text(child) for k in ("Jak wypełnić ten wzór", "Teksty w [nawiasach kwadratowych]",
                                      "Dwie pierwsze kolumny wypełnij", "Wykres zapiszesz poleceniem",
                                      "Odpowiadaj krótko, własnymi", "Zapisz jako PDF i wgraj")):
        body.remove(child)

tree.write(doc_path, xml_declaration=True, encoding="UTF-8", standalone=True)
open(rels_path, "w", encoding="utf-8").write(rels)
ct_path = os.path.join(d, "[Content_Types].xml")
ct = open(ct_path, encoding="utf-8").read()
if 'Extension="png"' not in ct:
    ct = ct.replace("<Default ", '<Default Extension="png" ContentType="image/png"/><Default ', 1)
    open(ct_path, "w", encoding="utf-8").write(ct)
print("gotowe:", d)
