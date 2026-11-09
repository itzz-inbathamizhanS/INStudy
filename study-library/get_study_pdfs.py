#!/usr/bin/env python3
"""
INStudy PDF library downloader (legal, free sources only).

Run on your own computer:
    python3 get_study_pdfs.py            # downloads into ./INStudy_Library
    python3 get_study_pdfs.py D:\\Books   # or any folder you choose

Needs only Python 3.8+ (no extra packages). Safe to re-run: files already
downloaded are skipped, so you can stop and resume any time.
NCERT books arrive as .zip (one PDF per chapter); the script unzips them.
Anything that fails is listed in _failed.txt with its source page so you can
grab it by hand (official sites sometimes move files).
"""
import os, sys, time, zipfile, urllib.request, urllib.error

NC = "https://ncert.nic.in/textbook/pdf/{}dd.zip"   # NCERT full-book zip pattern
OSTEP = "https://pages.cs.wisc.edu/~remzi/OSTEP/{}.pdf"

# (folder, filename, url)  -- folders are numbered in roadmap order
ITEMS = []

def ncert(folder, code, name):
    ITEMS.append((folder, name + ".zip", NC.format(code)))

# ---------- Phase 1: Foundation (SSC CGL, IBPS PO, AFCAT, CDS, UPSC) ----------
F1 = "01_Foundation_NCERT_6-10"
for code, name in [
    ("gess1", "C7_History_Our_Pasts_II"), ("gess2", "C7_Geography_Our_Environment"),
    ("gess3", "C7_Social_Political_Life_II"),
    ("hess2", "C8_History_Our_Pasts_III"), ("hess4", "C8_Geography_Resources_Development"),
    ("hess3", "C8_Social_Political_Life_III"), ("hesc1", "C8_Science"),
    ("iess3", "C9_History_India_Contemporary_World_I"), ("iess1", "C9_Geography_Contemporary_India_I"),
    ("iess4", "C9_Polity_Democratic_Politics_I"), ("iess2", "C9_Economics"),
    ("iesc1", "C9_Science"), ("iemh1", "C9_Maths"),
    ("jess3", "C10_History_India_Contemporary_World_II"), ("jess1", "C10_Geography_Contemporary_India_II"),
    ("jess4", "C10_Polity_Democratic_Politics_II"), ("jess2", "C10_Economics_Understanding_Development"),
    ("jesc1", "C10_Science"), ("jemh1", "C10_Maths"),
]:
    ncert(F1, code, name)

# ---------- Phase 2: GS core (UPSC Prelims, CDS, AFCAT GA, SSC GA depth) ----------
F2 = "02_GS_Core_NCERT_11-12"
for code, name in [
    ("kehs1", "C11_History_Themes_in_World_History"),
    ("kegy1", "C11_Geography_Fundamentals_Physical"), ("kegy2", "C11_Geography_India_Physical_Environment"),
    ("keps1", "C11_Polity_Indian_Constitution_at_Work"), ("keps2", "C11_Polity_Political_Theory"),
    ("keec1", "C11_Economics_Indian_Economic_Development"),
    ("kefa1", "C11_Art_An_Introduction_to_Indian_Art"),
    ("lehs1", "C12_History_Themes_Indian_History_I"), ("lehs2", "C12_History_Themes_Indian_History_II"),
    ("lehs3", "C12_History_Themes_Indian_History_III"),
    ("legy1", "C12_Geography_Fundamentals_Human"), ("legy2", "C12_Geography_India_People_Economy"),
    ("leps1", "C12_Polity_Contemporary_World_Politics"), ("leps2", "C12_Polity_Politics_in_India_since_Independence"),
    ("leec1", "C12_Economics_Macroeconomics"), ("leec2", "C12_Economics_Microeconomics"),
    ("lebo1", "C12_Biology_(Ecology_chapters_for_Environment)"),
    ("kemh1", "C11_Maths"), ("lemh1", "C12_Maths_Part1"), ("lemh2", "C12_Maths_Part2"),
]:
    ncert(F2, code, name)

# ---------- Phase 4: GATE CSE core (free, author-released textbooks) ----------
F4 = "04_GATE_CSE_Free_Textbooks"
ITEMS += [
    (F4, "Discrete_Math_MIT_Mathematics_for_Computer_Science.pdf",
     "https://courses.csail.mit.edu/6.042/spring18/mcs.pdf"),
    (F4, "Probability_Grinstead_Snell.pdf", "https://math.dartmouth.edu/~prob/prob/prob.pdf"),
    (F4, "Algorithms_Jeff_Erickson.pdf",
     "https://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf"),
    (F4, "Data_Structures_Open_Data_Structures_Java.pdf", "https://opendatastructures.org/ods-java.pdf"),
    (F4, "Data_Structures_Open_Data_Structures_CPP.pdf", "https://opendatastructures.org/ods-cpp.pdf"),
    (F4, "TOC_Maheshwari_Smid_Theory_of_Computation.pdf",
     "https://cglab.ca/~michiel/TheoryOfComputation/TheoryOfComputation.pdf"),
    (F4, "Compilers_Wirth_Compiler_Construction.pdf",
     "https://people.inf.ethz.ch/wirth/CompilerConstruction/CompilerConstruction1.pdf"),
]
# OSTEP (Operating Systems: Three Easy Pieces) - free per chapter, in book order
for i, ch in enumerate([
    "intro", "cpu-intro", "cpu-api", "cpu-mechanisms", "cpu-sched", "cpu-sched-mlfq",
    "cpu-sched-lottery", "cpu-sched-multi", "vm-intro", "vm-api", "vm-mechanism",
    "vm-segmentation", "vm-freespace", "vm-paging", "vm-tlbs", "vm-smalltables",
    "vm-beyondphys", "vm-beyondphys-policy", "threads-intro", "threads-api", "threads-locks",
    "threads-locks-usage", "threads-cv", "threads-sema", "threads-bugs", "file-devices",
    "file-disks", "file-raid", "file-intro", "file-implementation", "file-ffs",
    "file-journaling", "file-lfs",
], start=1):
    ITEMS.append((F4 + "/OS_OSTEP_chapters", f"{i:02d}_{ch}.pdf", OSTEP.format(ch)))

UA = "Mozilla/5.0 (study-library-downloader)"

def fetch(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest + ".part", "wb") as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)
    os.replace(dest + ".part", dest)

def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "INStudy_Library")
    os.makedirs(root, exist_ok=True)
    failed = []
    for n, (folder, name, url) in enumerate(ITEMS, 1):
        d = os.path.join(root, folder)
        os.makedirs(d, exist_ok=True)
        dest = os.path.join(d, name)
        unz = dest[:-4] if dest.endswith(".zip") else None
        if os.path.exists(dest) or (unz and os.path.isdir(unz)):
            print(f"[{n}/{len(ITEMS)}] skip  {name}")
            continue
        print(f"[{n}/{len(ITEMS)}] get   {name}")
        for attempt in range(3):
            try:
                fetch(url, dest)
                break
            except Exception as e:
                err = e
                time.sleep(2 * (attempt + 1))
        else:
            print(f"        FAILED ({err})")
            failed.append(f"{folder}/{name}\t{url}\t{err}")
            continue
        if unz:
            try:
                with zipfile.ZipFile(dest) as z:
                    z.extractall(unz)
                os.remove(dest)
            except zipfile.BadZipFile:
                failed.append(f"{folder}/{name}\t{url}\tnot a zip (site may have changed)")
    with open(os.path.join(root, "_failed.txt"), "w") as f:
        f.write("\n".join(failed) + ("\n" if failed else "Everything downloaded.\n"))
    print(f"\nDone. {len(ITEMS) - len(failed)} ok, {len(failed)} failed. Library: {root}")
    if failed:
        print("See _failed.txt; open the source page in README.md for those.")

if __name__ == "__main__":
    main()
