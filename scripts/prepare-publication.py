"""Validate tracked public files and stage only the GitHub Pages payload."""

import argparse
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COUNTRY = r"(?:at|bg|cz|de|es|fr|hr|hu|ie|pl|ro|si|sk)"
DOCUMENT = r"(?:op|otkaz|privacy|reklamace|gewaehrleistung|online-widerrufen|unternehmen|versand)"
SITE = re.compile(
    rf"(?:index\.html|\.nojekyll|"
    rf"assets/legal-(?:loader|parent)\.js|"
    rf"{COUNTRY}/(?:{DOCUMENT}(?:-current)?\.html|index\.html|version\.txt|"
    rf"(?:reklamacni-formular|reklamacny-formular|reklamationsformular|formulyar-reklamatsiya|"
    rf"formulario-reclamacion|formulaire-reclamation|reklamacijski-obrazac|"
    rf"formularz-reklamacyjny|formular-reclamatie|reklamacijski-obrazec)\.docx)|"
    rf"de/(?:eu-gewaehrleistung-de\.svg|iframe-(?:{DOCUMENT}\.txt|op\.html))|"
    rf"privacy/iframe-{COUNTRY}\.txt|embed/global-script\.txt|demo/iframe-layout\.html|"
    rf"archive/{COUNTRY}/{DOCUMENT}-(?:\d{{4}}-\d{{2}}-\d{{2}}(?:-v\d+(?:\.\d+)*)?|"
    rf"before-[A-Za-z0-9_-]+|\d{{4}}-\d{{2}}-\d{{2}}-pre-idu)\.html|"
    rf"archive/ie/\d{{4}}-\d{{2}}-\d{{2}}/{DOCUMENT}\.html)"
)
TECHNICAL = re.compile(
    r"(?:README\.md|scripts/(?:legal-catalogue|render-de|prepare-publication)\.py|"
    r"tests/legal-frame\.mjs|\.github/workflows/(?:pages|build-reklamacny-formular)\.yml|"
    r"de/(?:customer-pages-source|op-source)\.json|"
    r"\.build/sk-reklamacny-formular/(?:build|part\d{2}[a-z]?|chunk\d{2}[a-z]))"
)
INTERNAL_MARKER = re.compile(r"(?:^|[-_/])(?:draft|internal|interni|review|notes)(?:[-_/.]|$)", re.I)
SECRET = re.compile(
    rb"-----BEGIN (?:[A-Z]+ )*PRIVATE KEY-----|"
    rb"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{25,}|"
    rb"(?:AKIA|ASIA)[0-9A-Z]{16}|AIza[A-Za-z0-9_-]{35}|"
    rb"sk-(?:proj-)?[A-Za-z0-9_-]{25,}|glpat-[\w-]{20,}|xox[baprs]-[A-Za-z0-9-]{15,})\b|"
    rb"(?i:\bBearer\s+[A-Za-z0-9_.=-]{18,}|https?://[^\s:/@<>]+:[^\s/@<>]+@)"
)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).split(b"\0")
    payload = []
    violations = []
    for raw in filter(None, paths):
        name = raw.decode()
        path = ROOT / name
        on_site = SITE.fullmatch(name)
        if INTERNAL_MARKER.search(name) or not (on_site or TECHNICAL.fullmatch(name)):
            violations.append(f"Path outside publication policy: {name}")
            continue
        if path.is_symlink() or not path.is_file():
            violations.append(f"Unsupported tracked entry: {name}")
            continue
        if SECRET.search(path.read_bytes()):
            violations.append(f"Potential credential: {name}")
            continue
        if on_site:
            payload.append(name)
    if violations:
        raise SystemExit("\n".join(violations))

    if args.output:
        args.output.mkdir(parents=True, exist_ok=False)
        for name in [*payload, "catalogue.json"]:
            destination = args.output / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)
    print(f"Validated {len(payload)} Pages paths.")


if __name__ == "__main__":
    main()
