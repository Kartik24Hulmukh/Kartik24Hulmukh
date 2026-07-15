#!/usr/bin/env python3
"""Deterministic light/dark editorial panels for the Verified Noticeboard."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / "assets"
A.mkdir(exist_ok=True)


def make(kind, dark, w=1200, h=520):
    paper = "#141310" if dark else "#efe6d3"
    ink = "#f3ead8" if dark else "#1c1b18"
    muted = "#b9ad98" if dark else "#675f53"
    red = "#e16654" if dark else "#a93629"
    blue = "#83a9d5" if dark else "#315a8a"
    rule = "#4a4439" if dark else "#b8ad98"

    if kind == "masthead":
        # Keep the display name on the left and the identity copy fully
        # inside the right column so nothing collides at 1200px.
        body = f'''
<text x="54" y="62" font-family="Arial" font-size="13" fill="{muted}" letter-spacing="2">MUMBAI / PUBLIC WORK / JULY 2026</text>
<line x1="54" y1="82" x2="1146" y2="82" stroke="{rule}"/>
<text x="50" y="220" font-family="Georgia" font-size="92" font-weight="700" fill="{ink}">KARTIK</text>
<text x="50" y="330" font-family="Georgia" font-size="92" font-weight="700" fill="{ink}">HULMUKH</text>
<text x="700" y="160" font-family="Georgia" font-size="26" fill="{red}">Software for people nearby.</text>
<text x="700" y="204" font-family="Georgia" font-size="26" fill="{ink}">Systems that don't ask for trust.</text>
<line x1="700" y1="236" x2="1146" y2="236" stroke="{rule}"/>
<text x="700" y="278" font-family="Arial" font-size="16" fill="{muted}">FOUNDER · RGIT ROZGAR</text>
<text x="700" y="310" font-family="Arial" font-size="16" fill="{muted}">BUILDER · VERIFIABLE AI SYSTEMS</text>
<text x="700" y="372" font-family="Arial" font-size="15" fill="{blue}">build → test → publish the boundary</text>
<text x="700" y="398" font-family="Arial" font-size="15" fill="{blue}">→ invite challenge</text>
<text x="54" y="480" font-family="Arial" font-size="12" fill="{muted}">ISSUE 01 · THINGS BUILT, TESTED, AND STILL UNCERTAIN</text>
'''
    elif kind == "rgit":
        body = f'''
<text x="54" y="60" font-family="Arial" font-size="13" fill="{red}" letter-spacing="2">FIELD NOTE 01 / COMMUNITY SOFTWARE</text>
<text x="54" y="155" font-family="Georgia" font-size="50" fill="{ink}">A useful campus should not require</text>
<text x="54" y="218" font-family="Georgia" font-size="50" fill="{ink}">fifteen WhatsApp groups.</text>
<line x1="54" y1="260" x2="1146" y2="260" stroke="{rule}"/>
<text x="54" y="315" font-family="Arial" font-size="15" fill="{muted}">HOUSING</text>
<text x="255" y="315" font-family="Arial" font-size="15" fill="{muted}">RESALE</text>
<text x="440" y="315" font-family="Arial" font-size="15" fill="{muted}">ACADEMICS</text>
<text x="675" y="315" font-family="Arial" font-size="15" fill="{muted}">FOOD</text>
<text x="840" y="315" font-family="Arial" font-size="15" fill="{muted}">HEALTHCARE</text>
<rect x="54" y="365" width="210" height="52" fill="none" stroke="{red}" stroke-width="3" transform="rotate(-2 54 365)"/>
<text x="73" y="399" font-family="Arial" font-size="20" fill="{red}" font-weight="700">BUILT + OPERATED</text>
<text x="825" y="398" font-family="Arial" font-size="14" fill="{blue}">The interface is the easy part.</text>
<text x="825" y="425" font-family="Arial" font-size="14" fill="{blue}">Governance is the product.</text>
'''
    elif kind == "kairo-receipt":
        body = f'''
<text x="54" y="58" font-family="Arial" font-size="13" fill="{red}" letter-spacing="2">ACTION REVIEW / KP-01976 / PRE-LAUNCH</text>
<line x1="54" y1="80" x2="1146" y2="80" stroke="{rule}"/>
<text x="54" y="137" font-family="Georgia" font-size="36" fill="{ink}">The model can make a claim.</text>
<text x="54" y="182" font-family="Georgia" font-size="36" fill="{ink}">The receipt has to prove it.</text>
<line x1="620" y1="110" x2="620" y2="454" stroke="{rule}"/>
<text x="660" y="130" font-family="Arial" font-size="13" fill="{muted}">OPERATION</text>
<text x="885" y="130" font-family="Arial" font-size="15" fill="{ink}">LOCAL APPLICATION ACTION</text>
<text x="660" y="183" font-family="Arial" font-size="13" fill="{muted}">NETWORK</text>
<text x="885" y="183" font-family="Arial" font-size="15" fill="{ink}">DECLARED TEST: ZERO EGRESS</text>
<text x="660" y="236" font-family="Arial" font-size="13" fill="{muted}">CONFIRMATION</text>
<text x="885" y="236" font-family="Arial" font-size="15" fill="{ink}">REQUIRED BEFORE WRITE</text>
<text x="660" y="289" font-family="Arial" font-size="13" fill="{muted}">EVIDENCE</text>
<text x="885" y="289" font-family="Arial" font-size="15" fill="{ink}">SIGNED + HASH-CHAINED</text>
<text x="660" y="342" font-family="Arial" font-size="13" fill="{muted}">VALIDATION</text>
<text x="885" y="342" font-family="Arial" font-size="15" fill="{red}">THIRD-PARTY PENDING</text>
<text x="54" y="360" font-family="Arial" font-size="15" fill="{blue}">Separately runnable ≠ independently validated.</text>
<text x="54" y="400" font-family="Arial" font-size="14" fill="{muted}">Visual explanation—not a claim that this exact action occurred.</text>
'''
    else:
        # Two-by-two method grid avoids long-word collisions.
        body = f'''
<text x="54" y="58" font-family="Arial" font-size="13" fill="{red}" letter-spacing="2">SYSTEMS NOTEBOOK / RECURRING METHOD</text>
<text x="54" y="130" font-family="Georgia" font-size="40" fill="{ink}">01 claim</text>
<text x="320" y="130" font-family="Georgia" font-size="40" fill="{ink}">02 test</text>
<path d="M230 118 H290" stroke="{red}" stroke-width="3"/>
<text x="54" y="205" font-family="Georgia" font-size="40" fill="{ink}">03 counterexample</text>
<path d="M430 193 H500" stroke="{red}" stroke-width="3"/>
<text x="540" y="205" font-family="Georgia" font-size="40" fill="{ink}">04 boundary</text>
<line x1="54" y1="250" x2="1146" y2="250" stroke="{rule}"/>
<text x="54" y="310" font-family="Arial" font-size="15" fill="{muted}">PROJECT X-RAY INDIA</text>
<text x="54" y="352" font-family="Georgia" font-size="28" fill="{ink}">Sources before conclusions.</text>
<text x="650" y="310" font-family="Arial" font-size="15" fill="{muted}">PROVING GROUNDS</text>
<text x="650" y="352" font-family="Georgia" font-size="28" fill="{ink}">The patch does not grade itself.</text>
<line x1="54" y1="400" x2="1146" y2="400" stroke="{rule}"/>
<text x="54" y="455" font-family="Arial" font-size="17" fill="{blue}">A passing test is evidence about an oracle and a surface—not permission to stop thinking.</text>
'''

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img">'
        f'<rect width="100%" height="100%" fill="{paper}"/>'
        f"{body}</svg>"
    )


for kind in ["masthead", "rgit", "kairo-receipt", "notebook"]:
    for dark in [False, True]:
        name = f'{kind}-{"dark" if dark else "light"}.svg'
        (A / name).write_text(make(kind, dark), encoding="utf-8")
