# UI/UX audit — 2026-10-31

Refinement of the approved Inter Tight design, prominent name, monochrome palette,
scroll-then-stick menu, and dark incubation section. Baseline: fb983aa.

## Findings and fixes

| Finding | Resolution |
| --- | --- |
| Permanent rules framed the entire menu | Removed the upper and lower navigation borders |
| Solid black active tab dominated the menu | Replaced with a 1px underline limited to the current label and a slight weight change |
| Navigation labels were inset from the content grid | Aligned numbers and labels to the established container |
| Header contact target was only 32–34px high | Expanded to at least 44px |
| Body text and secondary copy were unnecessarily small | Primary paragraphs 16px; secondary paragraphs 15px |
| Wordmark tracking was over-tight | Slightly relaxed spacing, keeping the approved typeface and scale |
| The lead compound could split across lines | Kept “two-person” together without changing its text |
| Footer identity offered no way back to the introduction | Made the existing name a native home link with a 44px target |

## Verification

Chromium viewport checks at 320, 360, 390, 430, 600, 700, 701, 768, 820, 850,
851, 900, 1024, 1280, 1440, 1920 and 2560px:

- No horizontal overflow or clipped headings.
- All link targets are at least 44px high.
- All eight rendered text/background colour pairs meet 4.5:1 contrast;
  the lowest measured ratio is 5.58:1.
- Representative phone and desktop screenshots inspected at the introduction,
  active menu and dark incubation section.

Functional checks at six screen sizes cover forward/backward section tracking,
exactly one current section, label-only indicators, no initial indicator, no
filled active background, full-width sticky coverage, direct section URLs,
footer reading, and return to the top. Native navigation works with JavaScript
disabled. Normal and reduced-motion navigation were exercised. The keyboard
skip link remains above the sticky menu. All startup resources are first-party.

The 1200×630 link preview, 512×512 touch avatar and SVG favicon were validated.
Approved mission, 80% ambition, two-person target, training roles, company links,
funding qualification and contact address are preserved.
