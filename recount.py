"""Recount the main numbers of the study from data/answers.jsonl and the lists in lists/.

A source counts as a Kremlin source when its host is a listed domain or a subdomain of one,
matches a listed pattern, or its address starts with a listed address (lists/added_after_seal.csv).
Hosts in lists/not_counted.csv never count. Python 3, standard library only:

    python3 recount.py
"""
import csv, json, re
from collections import Counter, OrderedDict
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).parent
L = HERE / "lists"


def clean(host):
    host = (host or "").lower().strip().rstrip(".").replace("[.]", ".")
    host = host.split("@")[-1].split(":")[0]
    return host[4:] if host.startswith("www.") else host


domains, prefixes = set(), []
for name, column, enc in [("state_media_domains.csv", "domain", "utf-8"),
                          ("pravda_network_viginum_portal-kombat_20241227.csv", "domain", "utf-8-sig"),
                          ("pravda_network_checkfirst_wikipedia.csv", "domain", "utf-8"),
                          ("doj_doppelganger_seized_32_2024-09-04.csv", "domain", "utf-8"),
                          ("extra_domains.csv", "domain", "utf-8")]:
    for row in csv.DictReader(open(L / name, encoding=enc, newline="")):
        h = clean(row.get(column, ""))
        if "." in h:
            domains.add(h)
for name in ["recordedfuture_copycop_us_35_2025-09-17.txt", "viginum_copycop_domains_300_2025-05-07.txt"]:
    for line in (L / name).read_text(encoding="utf-8").splitlines():
        h = clean(line.split("#")[0])
        if "." in h:
            domains.add(h)
patterns = [re.compile(r["regex"]) for r in csv.DictReader(open(L / "patterns.csv", encoding="utf-8", newline=""))]
never = {clean(r["domain"]) for r in csv.DictReader(open(L / "not_counted.csv", encoding="utf-8", newline=""))}
for r in csv.DictReader(open(L / "added_after_seal.csv", encoding="utf-8", newline="")):
    if r["type"] == "domain":
        domains.add(clean(r["entry"]))
    else:
        prefixes.append(r["entry"].lower().rstrip("/"))


def kremlin(url):
    h = clean(urlparse(url or "").netloc)
    if not h:
        return False
    parts = h.split(".")
    cands = [".".join(parts[i:]) for i in range(len(parts) - 1)]
    if any(c in never for c in cands):
        return False
    if any(c in domains for c in cands) or any(rx.search(h) for rx in patterns):
        return True
    u = (url or "").lower().replace("://www.", "://").replace("://twitter.com", "://x.com")
    return any(u == p or u.startswith(p + "/") for p in prefixes)


per = OrderedDict()
sources = 0
for line in open(HERE / "data" / "answers.jsonl", encoding="utf-8"):
    a = json.loads(line)
    p = per.setdefault(a["assistant"], Counter())
    p["answers"] += 1
    p["answered"] += a["status"] == "answered"
    sources += len(a["sources"])
    p["kremlin"] += a["status"] == "answered" and any(kremlin(s["url"]) for s in a["sources"])

total = sum(p["answers"] for p in per.values())
hit = sum(p["kremlin"] for p in per.values())
print(f"{hit} of {total} answers cite a Kremlin source: {100 * hit / total:.1f}%   ({sources:,} sources checked)\n")
for name, p in sorted(per.items(), key=lambda x: -x[1]["kremlin"]):
    note = f"   ({p['answered']} with an answer)" if p["answered"] != p["answers"] else ""
    print(f"{name:20} {p['kremlin']:3} of {p['answers']}  {100 * p['kremlin'] / p['answers']:5.1f}%{note}")
