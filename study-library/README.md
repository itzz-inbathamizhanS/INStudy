# INStudy Library: every book and note you need, in roadmap order

Exams: SSC CGL, IBPS PO, AFCAT, CDS, UPSC Prelims, GATE CSE, placements.
Only legal sources: free official PDFs, author-released textbooks, and a "buy or borrow" list for paid books.

## How to get the PDFs

1. Install Python 3 if you don't have it (python.org).
2. Download `get_study_pdfs.py` from this folder.
3. Run `python3 get_study_pdfs.py` (Windows: `py get_study_pdfs.py`). It creates `INStudy_Library/` with numbered folders and fetches about 80 books/chapters (roughly 2–3 GB). Re-run any time; it skips what you already have.
4. Anything it can't fetch goes into `_failed.txt`. Use the source pages in section C for those.
5. To keep it on Google Drive, drag the `INStudy_Library` folder into Drive (or use Drive for Desktop).

## A. Which folder serves which exam

| Folder (roadmap order) | SSC CGL | IBPS PO | AFCAT | CDS | UPSC Pre | GATE CSE | Placements |
|---|---|---|---|---|---|---|---|
| 01 Foundation NCERT 6–10 (History, Geo, Polity, Eco, Science, Maths) | ✅ | ✅ (GA, Quant basics) | ✅ | ✅ | ✅ | – | Quant basics |
| 02 GS core NCERT 11–12 + Fine Arts + Biology ecology | GA depth | – | GA depth | ✅ | ✅ | Maths 11–12 | – |
| 03 Govt documents (links below) | Polity/eco | Banking awareness | – | ✅ | ✅ | – | – |
| 04 GATE CSE free textbooks (Discrete, Probability, Algorithms, DS, OS, TOC, Compilers) | – | – | – | – | – | ✅ | ✅ (DSA, OS) |
| 05 Previous papers (official sites, links below) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | – |

Suggested order: 01 → 02 alongside daily Quant/Reasoning practice → 03 (current affairs, keep running weekly) → 04 for GATE + placements → 05 every weekend from month 2.

Note: NCERT revised Classes 6–7 books in 2024–25 (new titles like "Exploring Society: India and Beyond"). The script fetches the long-standing editions, which most coaching and UPSC prep still use. Get the new ones from the NCERT textbook page if you want both.

## B. What the script downloads (all free and legal)

**01 Foundation (NCERT, official zips):** Class 7–10 History, Geography, Social & Political Life / Democratic Politics, Economics, Science (8–10), Maths (9–10).

**02 GS core (NCERT):** Class 11 Themes in World History, Physical Geography, India Physical Environment, Indian Constitution at Work, Political Theory, Indian Economic Development, An Introduction to Indian Art. Class 12 Themes in Indian History I–III, Human Geography, India People & Economy, Contemporary World Politics, Politics in India since Independence, Macro & Micro Economics, Biology (ecology chapters for Environment). Maths 11–12.

**04 GATE CSE (author-released free books):**
- Discrete Maths: *Mathematics for Computer Science* (MIT, Lehman/Leighton/Meyer)
- Probability: *Introduction to Probability* (Grinstead & Snell)
- Algorithms: *Algorithms* (Jeff Erickson)
- Data Structures: *Open Data Structures* (Pat Morin), Java and C++ editions
- Operating Systems: *OSTEP* (Arpaci-Dusseau), all 33 core chapters, in book order
- Theory of Computation: *Introduction to Theory of Computation* (Maheshwari & Smid)
- Compilers: *Compiler Construction* (Niklaus Wirth)

## C. Free sources to open in your browser (pages, not single files)

| What | Where | For |
|---|---|---|
| NCERT all textbooks (also new 2024–25 editions) | ncert.nic.in/textbook.php | All GS |
| NIOS Senior Secondary: Indian Culture & Heritage (223), History, Geography, Economics, Political Science | nios.ac.in → Online Course Material | UPSC art & culture, CDS |
| Constitution of India (official, updated) | legislative.gov.in → Constitution of India | Polity |
| Economic Survey + Budget at a Glance | indiabudget.gov.in | UPSC, IBPS, SSC economy |
| PIB releases (current affairs) | pib.gov.in | All GA |
| RBI publications: Annual Report, Monetary Policy statements | rbi.org.in | IBPS PO banking awareness |
| UPSC previous papers (Prelims, CDS, also CAPF) | upsc.gov.in → Examinations → Previous Question Papers | UPSC, CDS |
| SSC notices and official answer keys (papers come with keys) | ssc.gov.in | SSC CGL |
| AFCAT syllabus and sample/test pattern | afcat.cdac.in | AFCAT |
| GATE CSE previous papers + keys | current GATE organising IIT's site → "Previous Question Papers" (search "GATE 2027 official site") | GATE |
| NPTEL lecture notes and videos (DBMS, COA, CN, OS, TOC, Compilers, Discrete Maths, Linear Algebra) | nptel.ac.in | GATE |
| *Computer Networks: A Systems Approach* (free online) | book.systemsapproach.org | GATE CN |
| *Dive into Systems* (free online, COA + C + OS) | diveintosystems.org | GATE COA |
| *Security Engineering* (Ross Anderson; chapters free) | cl.cam.ac.uk/~rja14/book.html | Your cyber degree |
| MIT OCW 18.06 Linear Algebra (Strang lectures + notes) | ocw.mit.edu | GATE Maths |
| Striver A2Z DSA sheet + SDE sheet | takeuforward.org | Placements |

## D. Buy or borrow (no legal free PDF exists)

Cheapest legal route, in order: your college or district library → seniors' used copies / OLX / local second-hand market → Amazon "used" or Kindle edition → Indian low-price student edition (Pearson/Wiley/McGraw Hill India). Approx new prices.

| Book | Exams | ~New price |
|---|---|---|
| Lucent's General Knowledge | SSC, IBPS, AFCAT, CDS | ₹250 |
| R.S. Aggarwal, Quantitative Aptitude | SSC, IBPS, AFCAT, CDS, placements | ₹600 |
| R.S. Aggarwal, A Modern Approach to Verbal & Non-Verbal Reasoning | SSC, IBPS, AFCAT | ₹600 |
| Wren & Martin, High School English Grammar | SSC, IBPS, AFCAT, CDS | ₹500 |
| Norman Lewis, Word Power Made Easy | SSC, IBPS, CDS | ₹150 |
| M. Laxmikanth, Indian Polity | UPSC, CDS, SSC | ₹750 |
| Spectrum (Rajiv Ahir), A Brief History of Modern India | UPSC, CDS | ₹400 |
| G.C. Leong, Certificate Physical and Human Geography | UPSC, CDS | ₹450 |
| Ramesh Singh, Indian Economy (or NCERT + Economic Survey only) | UPSC | ₹800 |
| Shankar IAS, Environment | UPSC | ₹400 |
| Kiran / Arihant SSC CGL & IBPS PO chapter-wise previous papers | SSC, IBPS | ₹350 each |
| Arihant AFCAT / Pathfinder CDS | AFCAT, CDS | ₹500 |
| Cormen et al., CLRS (Introduction to Algorithms) | GATE, placements | ₹900 (PHI edition) |
| Galvin, Operating System Concepts (OSTEP above covers most of it free) | GATE | ₹800 |
| Korth, Database System Concepts | GATE | ₹900 |
| Kurose & Ross, Computer Networking | GATE | ₹800 |
| Morris Mano, Digital Logic & Computer Design | GATE | ₹500 |
| Hamacher / Patterson-Hennessy, Computer Organization | GATE | ₹800 |
| Peter Linz, Formal Languages and Automata | GATE | ₹600 |
| Kenneth Rosen, Discrete Mathematics | GATE | ₹900 |
| Aho et al., Compilers (Dragon book) — optional, Wirth above is free | GATE | ₹900 |
| Gayle McDowell, Cracking the Coding Interview | Placements | ₹600 |

Tip: you don't need every paid book. Minimum buy list: Lucent, RS Aggarwal Quant, Laxmikanth, Spectrum, one previous-papers book per exam, CLRS. Everything else has a free substitute above.

## What's not here, and why

No copyrighted books as PDFs from unofficial sites. Those are pirated copies, often outdated editions, and sometimes carry malware. Coaching "notes" PDFs circulating on Telegram are mostly the same.
