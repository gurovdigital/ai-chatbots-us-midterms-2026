# AI chatbots cited Kremlin propaganda before the US midterm elections

Data of the study by Dosimeter, an independent research group from Berlin: https://dosimeteraudit.org/research/ai-chatbots-us-midterms-2026

A week before the US midterm elections of 3 November 2026, we asked 10 AI assistants 10 questions from the US political agenda, 10 times per question. In 125 of the 1,000 answers (12.5%), the assistant cited a Kremlin propaganda site as a source.

| Assistant | Answers with Kremlin sources |
|---|---|
| Perplexity | 37 of 100 |
| Claude | 24 of 100 |
| DeepSeek | 22 of 100 |
| Grok | 18 of 100 |
| Microsoft Copilot | 10 of 100 |
| Meta AI | 8 of 100 |
| Google AI Overviews | 6 of 100 (Google showed an AI Overview for 93 of the 100 queries) |
| ChatGPT | 0 of 100 |
| Google Gemini | 0 of 100 |
| America.gov | 0 of 100 |

## Check the numbers yourself

Python 3, standard library only:

```
python3 recount.py       # recounts the numbers above from the answers and the lists
python3 verify_seal.py   # checks the files against the seal and the seal against the three timestamps
```

## Files

- `data/answers.jsonl`: the 1,000 answers, one per line: assistant, question, repetition, status, time in UTC, the full answer text and the sources in the order the assistant showed them
- `data/sources.csv`: the 9,209 cited sources, one per line
- `screenshots/`: 287 screenshots of the answers of Meta AI, DeepSeek, Grok and America.gov, taken when the answer was collected; the left sidebar of the chat page is cut away. The field `screenshot` in `data/answers.jsonl` links an answer to its screenshot. The answers of the other assistants were collected as data, without screenshots
- `questions/questions.json`: the 10 questions with the source of the false claim and its debunk, as sealed before the first question
- `lists/`: the lists of Kremlin propaganda sites used for counting
  - `state_media_domains.csv`: Russian state media under EU Regulation 833/2014, Annex XV, with their mirror sites
  - `pravda_network_viginum_portal-kombat_20241227.csv`: the Pravda network (Portal Kombat), list of VIGINUM, France, 27 December 2024
  - `pravda_network_checkfirst_wikipedia.csv`: Pravda network sites cited on Wikipedia, list of CheckFirst
  - `doj_doppelganger_seized_32_2024-09-04.csv`: Doppelganger domains seized by the US Department of Justice, 4 September 2024
  - `recordedfuture_copycop_us_35_2025-09-17.txt`: CopyCop sites aimed at the US, Recorded Future, 17 September 2025
  - `viginum_copycop_domains_300_2025-05-07.txt`: CopyCop and Storm-1516 domains, VIGINUM, 7 May 2025
  - `extra_domains.csv` and `patterns.csv`: further Russian state bodies, state media and their editions, with the basis for each
  - `not_counted.csv`: hosts that do not count in this measurement
  - `added_after_seal.csv`: mirror sites of Russia Today and the official account of Sputnik on X, added to the lists after the measurement, with the evidence for each
- `seal/`: the seal of the measurement

## How we counted

An answer counts when at least one of its sources, at any place in the list of sources or as a link in the text, has a host that is a listed domain or a subdomain of one, matches a listed pattern, or starts with a listed address. The share is the number of such answers out of 100 per assistant.

The questions were asked on 27 and 28 October 2026 in English, in a new chat per question, without account history, with a US location (VPN or API settings) where the service allowed it. Three researchers checked the 1,000 answers by hand, independently of each other.

## The seal

Before the first question, on 27 October 2026 at 21:34 UTC, we wrote the SHA-256 checksums of the questions and the lists into `seal/SEAL.txt` and had the checksum of that file stamped by three independent timestamp services: DigiCert, Sectigo and FreeTSA (`seal/*.tsr`). The stamps show that the questions and the lists in this package existed in this form before the measurement. The seal also covers the measurement software and an internal plan of the run, which are not part of this package.

## Licence

Data: Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/. The answer texts are the output of the AI assistants named in the data, and the source lists belong to the organisations named above.

Please cite as: Dosimeter (2026). AI chatbots cited Kremlin propaganda before the US midterm elections. https://dosimeteraudit.org/research/ai-chatbots-us-midterms-2026

Contact: contact@dosimeteraudit.org
