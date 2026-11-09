# INStudy

Everything built for a multi-exam study plan: SSC CGL, IBPS PO, AFCAT, CDS, UPSC Prelims, GATE CSE and campus placements, for a B.Tech CSE (Cyber Security) student.

## What's here

| Path | What it is |
|---|---|
| [app/study-desk.html](app/study-desk.html) | **Study Desk**, the all-in-one study app (single HTML file). Today plan, focus timer, roadmap, exam guides, full syllabus, practice (drills, questions, paper import, flashcards, notes, cyber quest, daily CTF), progress, library, settings. |
| [docs/plan.md](docs/plan.md) | Goal strategy, daily routine, exam dates |
| [docs/roadmap.md](docs/roadmap.md) | 31 steps from zero to exam-ready, with point-by-point study lists |
| [docs/exam-guides.md](docs/exam-guides.md) | Per exam: books in order, how to study, how to practise, past-paper sources |
| [docs/syllabus.md](docs/syllabus.md) | Official syllabus topics for every exam |
| [docs/book-lists.md](docs/book-lists.md) | Books per exam, plus free legal textbooks |
| [docs/decisions.md](docs/decisions.md) | Decisions made along the way, and what's still open |
| [docs/library-contents.md](docs/library-contents.md) | What the downloaded PDF library contains |
| [study-library/](study-library/) | Downloader script for ~80 free, legal PDFs and the library index with a buy-or-borrow list |

## Running the app

The live version is a Claude artifact (https://claude.ai/artifact/UEL2Puk96E1T8A7z2NoahM), where your data syncs to your Claude account and paper import uses Claude.

Opened as a plain file in a browser, `app/study-desk.html` still works and saves to that browser's local storage. Claude-only features (account sync, importing question-paper PDFs) need the artifact version.

## Getting the PDFs

```
py study-library/get_study_pdfs.py C:\Users\<you>\Documents\INStudy_Library
```

The PDFs are not stored in this repo (1.45 GB). Only legal sources are used.
