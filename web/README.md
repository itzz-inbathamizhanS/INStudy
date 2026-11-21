# Study Desk website

A static build of Study Desk that anyone can open in a browser.

- Each visitor picks their exams on first open, so they only see those syllabus pages.
- Progress is saved privately in that visitor's browser. Settings has a backup you can copy and paste to move it to another device.
- Free, openly licensed books open from their official sites. Purchased books are not hosted here; the app says "Use your own copy" for those.

Deploy: point a Vercel project at this repo with root directory `web` and no build step.

## Books hosted on the site

These openly licensed books are split into the daily-plan page ranges under `books/` and open in the built-in reader:

| Book | Licence |
|---|---|
| Jeff Erickson, *Algorithms* | CC BY 4.0 |
| Pat Morin, *Open Data Structures (Java)* | CC BY 2.5 |
| Lehman, Leighton & Meyer, *Mathematics for Computer Science* | CC BY-SA 3.0 |
| Grinstead & Snell, *Introduction to Probability* | GNU FDL |

Other free books (NCERT, OSTEP, Maheshwari & Smid, Wirth) are free to read but not licensed for re-hosting, so the site links to their official copies. Purchased books are never hosted.

For any book that is read by page range (purchased books included), a visitor can tap **Add my PDF** and pick their own copy. It is stored only in that browser (IndexedDB) and never uploaded; after that, **Read here** opens just the plan's pages from it.
