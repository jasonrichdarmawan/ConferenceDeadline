# Task

You are an expert in conferences and journals in Artificial Intelligence category.

Your task is to fill `data/Conference-Deadline.csv`.

- Get the list of journals and conferences listed in China Computer Federation (CCF) ranking.

  Get it with:
  - `python -m ccf_catalog.main --category "Artificial Intelligence" --rank=A` to get list of conferences and journals of Artificial Intelligence with rank CCF A.
  - or `python -m ccf_catalog.main --name="International Conference on Machine Learning"` or `--acronym=ICML` to search for conferences or journals name. The search is case insensitive.

To avoid looking up the same journals/conferences that have been recorded:

- Get the list of journals/conferences that have been recorded locally.

  Get it from `data/Conference-Deadline.csv` or get it with:
  - `python -m conference_by_motn.main --acronym=ICML` to get list of journals/ocnferences with open application.
    possible key:
    - `--name=ACM Conference`. This is inexact match.
    - `--rank=A`. This filter out non-CCF A journals/conferences.

# Note

- Record journal's Call for Papers.
  Most academic journals accept regular submissions year-round with no fixed deadlines, though exceptions exist for special issues.
- Adding regular journal submissions (rolling) is not useful.
  User can use `python -m ccf_catalog.main -m category "Artificial Intelligence"` to get the list.