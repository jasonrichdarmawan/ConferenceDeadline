# CCF Artificial Intelligence submission check

Checked on **2026-10-01**, using the local 2026 CCF catalog and official conference, publisher, and journal-specific submission pages.

## CSV conventions

- Updated the existing `data/Conference-Deadline.csv`; no second plural-named file was created.
- Dates are `DD/MM/YY`. Existing historical and non-AI records were retained.
- Added only verified submission routes. A published future CFP does not establish that its submission window is already open.
- Journal entries must represent specific special-issue or collection Calls for Papers with verified submission deadlines, not ordinary rolling submissions. The initial regular-submission entries were removed following clarification of the requirement.
- Missing journal acronyms remain blank, matching the CCF catalog. Journal and conference names distinguish shared acronyms such as AAMAS and EAAI.
- TACL's ordinary monthly submission cycle was also removed: it is not a special-issue CFP. No Python code was changed.

## Open conference paper submissions

| Venue | Abstract | Paper | Notes |
| --- | --- | --- | --- |
| AAMAS 2027 | 01/10/26 | 08/10/26 | Mandatory abstract registration. OpenReview window started 12/08/26. |
| ALT 2027 | — | 12/10/26 | Official submission instructions invite electronic submissions on OpenReview. |
| COLING 2027 | — | 12/10/26 | October ARR cycle. Commitment is separately 23/12/26. |
| NAACL 2027 | — | 12/10/26 | Same October ARR cycle. Commitment is separately 23/12/26. |
| FG 2027 | 09/10/26 | 16/10/26 | Submission portal opened 25/09/26. |

All five use **23:59 Anywhere on Earth (UTC-12)** deadlines. AAMAS and NAACL were already recorded and were not duplicated. NAACL and COLING cannot receive simultaneous commitments of the same paper.

Additional official evidence:

- [ALT submission instructions](https://algorithmiclearningtheory.org/alt2027/submission-instructions/).
- [October ARR submission portal](https://openreview.net/group?id=aclweb.org/ACL/ARR/2026/October).
- [AAMAS submission portal](https://openreview.net/group?id=ifaamas.org/AAMAS/2027/Conference).

Workshop-organizer proposal rows were relabeled; their dates must not be interpreted as research-paper deadlines.

## Published future calls not added as confirmed open

| Venue | Announced deadlines | Reason |
| --- | --- | --- |
| [CVPR 2027](https://cvpr.thecvf.com/Conferences/2027/CallForPapers) | Registration 10/11/26, paper 16/11/26 | Active submission window unverified. |
| [ACL 2027](https://2027.aclweb.org/calls/main/) | Latest eligible ARR cycle 04/01/27 | January window not yet verified open. Earlier ARR cycles are eligible. |
| [ICAPS 2027](https://icaps27.icaps-conference.org/calls/cfp/) | Abstract 07/12/26, paper 14/12/26 | Active submission window unverified. |
| [IJCAI 2027](https://2027.ijcai.org/) | Abstract 04/01/27, paper 11/01/27 | Schedule announced, active main-paper submission unverified. |
| [IJCNN 2027](https://ijcnn.org/2027/authors/call-for-papers) | Paper 31/01/27 | CFP and portal link exist, but accepting-now status unverified. |
| [IJCB 2027](https://ijcb2027.ieee-biometrics.org/call-for-papers/) | Paper 09/04/27 | Submissions explicitly open 15/03/27. |

Other exclusions and cautions:

- [AISTATS 2027](https://virtual.aistats.org/Conferences/2027/CallForPapers): paper deadline 06/10/26, but mandatory abstract deadline 29/09/26 passed. Only previously registered papers can continue.
- [ICDAR 2027 CFP](https://icdar2027.org/call-for-papers) says paper deadline 20/02/27, while [important dates](https://icdar2027.org/important-dates) says 28/02/27. Do not choose a date until clarified. Its journal-track deadline is 15/11/26, but submission access was marked forthcoming.
- [GECCO 2027 CFP](https://gecco-2027.sigevo.org/Call+for+Papers) still contains GECCO 2026 dates; no extrapolation was made.
- NAACL industry CFP and rendered portal deadlines disagree; excluded pending clarification. System demonstrations open 01/11/26, not yet open on the check date.
- ACML encore and DAI sister-conference tracks concern already accepted/published work, not new original papers. AAAI journal-track dates conflict and concern presentation of published journal papers.
- No confirmed open new-paper call was established for ICCV, COLT, ECAI, ICCBR, KR, UAI, PPSN, CEC, ICTAI, IROS, ILP, KSEM, PRICAI or the next editions of the other closed conference series. This is not proof that no open call exists.

## Journal evidence and remaining gaps

The initial research verified regular submission routes rather than dated journal Calls for Papers. All 30 regular-submission rows were subsequently removed; no journal CFP was added. The notes below describe unresolved research, not confirmed CFP opportunities.

Access failures prevented confirmation of TAP, Evolutionary Computation, TEC, TFS, TNNLS, Neural Computation and many rank-C journals. These were not added speculatively. In particular, Machine Translation, Neural Processing Letters, International Journal of Intelligent Systems and the IET journals remain pending status checks.

Cambridge provides submission instructions under **Natural Language Processing**, but continuity with the catalog's **Natural Language Engineering (NLE)** was not verified; no renamed entry was added. The IEEE society uses **TASLPRO** for the current audio/speech/language journal; the CSV retains the supplied catalog acronym **TASLP**.

No future special-issue deadline was sufficiently verified to add. Retrieval failure is not evidence of journal closure.