# AI chatbots cited Kremlin propaganda before the US midterm elections

Data of the study by Dosimeter, an independent research group from Berlin: https://dosimeteraudit.org/research/ai-chatbots-us-midterms-2026

The same data are on Hugging Face, where the tables can be read and searched in the browser: https://huggingface.co/datasets/DosimeterAudit/ai-chatbots-us-midterms-2026

A week before the US midterm elections of 3 November 2026, Dosimeter asked 10 AI assistants 10 questions from the US political agenda, 10 times per question. In 125 of the 1,000 answers (12.5%), the assistant cited a Kremlin propaganda site as a source.

| Assistant | Answers with Kremlin sources |
|---|---|
| Perplexity | 37 of 100 |
| Claude | 24 of 100 |
| DeepSeek | 22 of 100 |
| Grok | 18 of 100 |
| Microsoft Copilot | 10 of 100 |
| Meta AI | 8 of 100 |
| Google AI Overviews | 6 of 100 (Google showed an AI Overview for 93 of the 100 queries) |

## Check the numbers yourself

Python 3, standard library only:

```
python3 recount.py   # recounts the numbers above from the answers and the lists
```

## Files

- `data/answers.jsonl`: the 1,000 answers, one per line: assistant, question, repetition, status (`answered`, and for Google AI Overviews `AI Overview shown` or `no AI Overview shown`), the full answer text and the sources in the order the assistant showed them
- `data/sources.csv`: the 9,209 cited sources, one per line
- `screenshots/`: 287 screenshots of the answers of Meta AI, DeepSeek, Grok and America.gov, taken when the answer was collected; the left sidebar of the chat page is cut away. The field `screenshot` in `data/answers.jsonl` links an answer to its screenshot. The answers of the other assistants were collected as data, without screenshots
- `questions/questions.json`: the 10 questions, the page where each claim appeared and a page that checks it
- `lists/`: the lists of Kremlin propaganda sites used for counting
  - `state_media_domains.csv`: Russian state media under EU Regulation 833/2014, Annex XV, with their mirror sites
  - `pravda_network_viginum_portal-kombat_20241227.csv`: the Pravda network (Portal Kombat), list of VIGINUM, France, 27 December 2024
  - `pravda_network_checkfirst_wikipedia.csv`: Pravda network sites cited on Wikipedia, list of CheckFirst (domain column only)
  - `doj_doppelganger_seized_32_2024-09-04.csv`: Doppelganger domains seized by the US Department of Justice, 4 September 2024
  - `recordedfuture_copycop_us_35_2025-09-17.txt`: CopyCop sites aimed at the US, Recorded Future, 17 September 2025
  - `viginum_copycop_domains_300_2025-05-07.txt`: CopyCop and Storm-1516 domains, VIGINUM, 7 May 2025
  - `extra_domains.csv` and `patterns.csv`: further Russian state bodies, state media and their editions, with the basis for each
  - `extra_entries.csv`: mirror sites of Russia Today and the official account of Sputnik on X, with the evidence for each
  - `not_counted.csv`: hosts that do not count in this measurement

## Counting

An answer counts when at least one of its sources, at any place in the list of sources or as a link in the text, has a host that is a listed domain or a subdomain of one, matches a listed pattern, or starts with a listed address. The share is the number of such answers out of 100 per assistant.

The questions were asked on 27 and 28 October 2026 in English, in a new chat per question, without account history. Location: United States. Three researchers checked the 1,000 answers by hand, independently of each other.

## Licence

Scripts: MIT OR EUPL-1.2, at your choice ([LICENSE-MIT](LICENSE-MIT), [LICENSE](LICENSE)). Data, screenshots, lists and documentation: CC BY 4.0 ([LICENSE-DATA.md](LICENSE-DATA.md)).

Please cite as: Dosimeter (2026). AI chatbots cited Kremlin propaganda before the US midterm elections: data and verification package. Zenodo. https://doi.org/10.5281/zenodo.23748831

Contact: contact@dosimeteraudit.org
