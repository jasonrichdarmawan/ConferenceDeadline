You are an expert in conferences and journals in Artificial Intelligence category.

Your task is to fill `data/Conference-Deadline.csv`.

- Get the list of journals and conferences listed in China Computer Federation (CCF) ranking.

  Get it from `data/Conferences-Journals-CCF.csv` or get it with:
  - `python -m ccf_catalog.main --name="International Conference on Machine Learning"` or `--acronym=ICML` to search for conferences or journals name. The search is case insensitive.
  - or `python -m ccf_catalog.main --category "Artificial Intelligence" --rank=A` to get list of conferences and journals of Artificial Intelligence with rank CCF A.

To avoid looking up the same conferences/journals that have been recorded:

- Get the list of journals and conferences recorded locally.

  Get it from `data/Conference-Deadline.csv` or get it with:
  - `python -m conference_by_motn.main --acronym=ICML` to get list of journals/ocnferences with open application.
    possible key:
    - `--name=ACM Conference`. This is inexact match.
    - `--rank=A`. This filter out non-CCF A journals/conferences.