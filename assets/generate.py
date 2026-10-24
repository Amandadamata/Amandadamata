"""Generates the SVG images used in the profile README.

Run from the repository root:  python3 assets/generate.py
Edit the PROJECTS and HERO data below when a number or a description changes.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent

THEMES = {
    "dark": {"bg": "#0F1F17", "border": "#2D6A4F", "title": "#D8F3DC", "text": "#B7E4C7",
             "muted": "#74C69D", "chip_bg": "#1B4332", "chip_text": "#D8F3DC"},
    "light": {"bg": "#F3FBF5", "border": "#A8D5BA", "title": "#1B4332", "text": "#2D6A4F",
              "muted": "#52796F", "chip_bg": "#D8F3DC", "chip_text": "#1B4332"},
}
LANG_COLOR = {"Java": "#B07219", "Python": "#3572A5"}
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

PROJECTS = {
    "pulseops": {
        "name": "PulseOps", "lang": "Python",
        "en": ("Checks if APIs are up and opens an", "incident after 3 failures in a row.", "251 tests · GitHub Actions"),
        "pt": ("Verifica se APIs estão no ar e abre", "incidente após 3 falhas seguidas.", "251 testes · GitHub Actions"),
        "chips": ["FastAPI", "PostgreSQL", "Docker"],
    },
    "banking": {
        "name": "Banking System", "pt_name": "Sistema Bancário", "lang": "Java",
        "en": ("Checking and savings accounts with", "overdraft, interest and transfers.", "135 tests · GitHub Actions"),
        "pt": ("Conta corrente e poupança, com cheque", "especial, rendimento e transferências.", "135 testes · GitHub Actions"),
        "chips": ["BigDecimal", "SQLite", "JUnit 6"],
    },
    "vetcare": {
        "name": "VetCare Scheduler", "lang": "Java",
        "en": ("Books vet appointments, refuses", "double bookings, sorts by urgency.", "123 tests · GitHub Actions"),
        "pt": ("Agenda consultas veterinárias, recusa", "horário duplicado e ordena por urgência.", "123 testes · GitHub Actions"),
        "chips": ["Java 21", "Gson", "JUnit 6"],
    },
}

HERO = {
    "en": [("name", "Amanda da Mata"), ("role", "Back-End developer · Java and Python"),
           ("based in", "Goiânia, Brazil · open to remote work"), ("speaks", "Portuguese and English"),
           ("before", "English teacher for 2 years"), ("studying", "ADS at UNINTER, 1st semester"),
           ("looking for", "an internship or a junior role")],
    "pt": [("nome", "Amanda da Mata"), ("área", "Back-End · Java e Python"),
           ("mora em", "Goiânia (GO) · aberta a vagas remotas"), ("idiomas", "português e inglês"),
           ("antes", "professora de inglês por 2 anos"), ("estuda", "ADS na UNINTER, 1º semestre"),
           ("procura", "estágio ou vaga júnior")],
}


def card(key: str, lang: str, theme: str) -> str:
    p, t = PROJECTS[key], THEMES[theme]
    name = p.get("pt_name", p["name"]) if lang == "pt" else p["name"]
    line1, line2, footer = p[lang]
    chips, x = [], 24
    for chip in p["chips"]:
        w = 20 + len(chip) * 8.6
        chips.append(f'<rect x="{x}" y="145" width="{w:.0f}" height="28" rx="14" fill="{t["chip_bg"]}"/>'
                     f'<text x="{x + w / 2:.0f}" y="163.5" text-anchor="middle" class="chip">{escape(chip)}</text>')
        x += w + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="400" height="220" viewBox="0 0 400 220" role="img" aria-label="{escape(name)}">
<style>
.name{{font:700 26px {SANS};fill:{t["title"]}}}
.desc{{font:400 17.5px {SANS};fill:{t["text"]}}}
.lang{{font:600 15px {SANS};fill:{t["muted"]}}}
.chip{{font:600 14px {SANS};fill:{t["chip_text"]}}}
.foot{{font:500 15px {MONO};fill:{t["muted"]}}}
</style>
<rect x="1" y="1" width="398" height="218" rx="16" fill="{t["bg"]}" stroke="{t["border"]}" stroke-width="2"/>
<circle cx="31" cy="33" r="7" fill="{LANG_COLOR[p["lang"]]}"/>
<text x="46" y="38.5" class="lang">{p["lang"]}</text>
<text x="24" y="76" class="name">{escape(name)}</text>
<text x="24" y="106" class="desc">{escape(line1)}</text>
<text x="24" y="128" class="desc">{escape(line2)}</text>
{"".join(chips)}
<line x1="24" y1="187" x2="376" y2="187" stroke="{t["border"]}" stroke-width="1"/>
<text x="24" y="208" class="foot">{escape(footer)}</text>
<text x="376" y="208" text-anchor="end" class="foot">→</text>
</svg>
'''


def hero(lang: str) -> str:
    rows = HERO[lang]
    height = 92 + len(rows) * 30 + 40
    command = "java AboutMe.java" if lang == "en" else "java SobreMim.java"
    lines = []
    for i, (label, value) in enumerate(rows):
        y = 112 + i * 30
        delay = 1.1 + i * 0.35
        lines.append(f'<g class="row" style="animation-delay:{delay:.2f}s">'
                     f'<text x="32" y="{y}" class="key">{escape(label)}</text>'
                     f'<text x="178" y="{y}" class="val">{escape(value)}</text></g>')
    cursor_y = 112 + len(rows) * 30
    end = 1.1 + len(rows) * 0.35
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="720" height="{height}" viewBox="0 0 720 {height}" role="img" aria-label="Amanda da Mata, Back-End developer, Java and Python">
<style>
.bar{{font:500 13px {SANS};fill:#74C69D}}
.cmd{{font:500 17px {MONO};fill:#D8F3DC}}
.prompt{{font:700 17px {MONO};fill:#A8D5BA}}
.key{{font:500 16px {MONO};fill:#74C69D}}
.val{{font:600 16px {MONO};fill:#F3FBF5}}
.typed{{clip-path:inset(0 100% 0 0);animation:type 0.9s steps(17,end) 0.2s forwards}}
.row{{opacity:0;animation:show 0.3s ease-out forwards}}
.cursor{{opacity:0;animation:show 0s {end:.2f}s forwards, blink 1s step-end {end:.2f}s infinite}}
@keyframes type{{to{{clip-path:inset(0 0 0 0)}}}}
@keyframes show{{to{{opacity:1}}}}
@keyframes blink{{50%{{fill:transparent}}}}
@media (prefers-reduced-motion: reduce){{.typed,.row,.cursor{{animation:none;opacity:1;clip-path:none}}}}
</style>
<rect x="1" y="1" width="718" height="{height - 2}" rx="14" fill="#1B4332" stroke="#2D6A4F" stroke-width="2"/>
<path d="M1 15a14 14 0 0 1 14-14h690a14 14 0 0 1 14 14v25H1z" fill="#2D6A4F"/>
<circle cx="24" cy="21" r="6" fill="#F4A6A6"/><circle cx="44" cy="21" r="6" fill="#F6E3A1"/><circle cx="64" cy="21" r="6" fill="#A8D5BA"/>
<text x="360" y="25.5" text-anchor="middle" class="bar">amanda@github: ~</text>
<text x="32" y="74" class="prompt">$</text>
<text x="52" y="74" class="cmd typed">{command}</text>
{"".join(lines)}
<rect x="32" y="{cursor_y - 15}" width="10" height="19" fill="#A8D5BA" class="cursor"/>
</svg>
'''


if __name__ == "__main__":
    for lang in ("en", "pt"):
        (OUT / f"hero-{lang}.svg").write_text(hero(lang), encoding="utf-8")
        for key in PROJECTS:
            for theme in THEMES:
                (OUT / f"card-{key}-{lang}-{theme}.svg").write_text(card(key, lang, theme), encoding="utf-8")
    print("generated", len(list(OUT.glob("*.svg"))), "SVG files")
