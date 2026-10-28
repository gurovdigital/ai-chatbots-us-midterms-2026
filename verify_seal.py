"""Check the seal of the measurement: the files in this package against seal/SEAL.txt, and SEAL.txt against
the three timestamp tokens (DigiCert, Sectigo, FreeTSA). Python 3, standard library only:

    python3 verify_seal.py

The script checks that the SHA-256 of SEAL.txt is inside each token. To check the signatures of the
timestamp services as well, use OpenSSL, for example:

    openssl ts -reply -in seal/freetsa.tsr -text
    openssl ts -verify -data seal/SEAL.txt -in seal/freetsa.tsr -CAfile <the FreeTSA root certificate>
"""
import hashlib
from pathlib import Path

HERE = Path(__file__).parent
SEAL = HERE / "seal" / "SEAL.txt"
# where the sealed files are in this package (the seal lists the paths of the working folder)
HERE_AS = {"questions.json": "questions/questions.json"}

digest = hashlib.sha256(SEAL.read_bytes()).digest()
print("SEAL.txt  sha256", digest.hex())
for tsr in sorted((HERE / "seal").glob("*.tsr")):
    print(f"  {tsr.name:12} {'contains this hash' if digest in tsr.read_bytes() else 'DOES NOT contain this hash'}")
print()
for line in SEAL.read_text(encoding="utf-8").splitlines():
    parts = line.split("  ", 1)
    if len(parts) != 2 or len(parts[0]) != 64 or not parts[1].strip():
        continue
    want, path = parts[0], parts[1].strip()
    name = path.rsplit("/", 1)[-1]
    local = HERE / HERE_AS.get(name, "lists/" + name)
    if not local.exists():
        print(f"  not in this package   {path}")
        continue
    ok = hashlib.sha256(local.read_bytes()).hexdigest() == want
    print(f"  {'same as sealed' if ok else 'CHANGED':15} {local.relative_to(HERE)}")
