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


## Follow-up: copy and visual consistency

Baseline: a2665bb. Reviewed the live page and full-page phone, tablet and desktop
screenshots, then refined the established design.

- Replaced broad service slogans with software/hardware, product/market training,
  and working alongside founders. Descriptions now name the work rather than
  repeating “our approach”.
- Shortened the introduction and ambition without changing the two-person goal,
  80% target or the distinction between current work and future infrastructure.
- Removed the repeated purpose note and footer slogan.
- Made email-based training links explicit enquiries, with distinct accessible
  names that include the visible label. Corporate contact now names technology
  adoption. Search and social descriptions reflect the same concrete services.
- Aligned the ambition paragraph to the main text column. Increased navigation,
  action links and company domains to 13px; improved header/footer small text.
- Stacked the corporate section below 1200px to avoid a narrow four-line heading.
  The owner's corporate wording and company caption remain unchanged.

Checked 20 widths from 320 to 2560px, including 1100, 1200 and 1201px around the
new layout threshold. No horizontal overflow or clipped headings; all links
retain 44px targets. Desktop ambition text aligns with the introduction.
Reviewed final screenshots at 390, 1024 and 1440px and the pinned desktop menu.
The existing six-size functional suite covers native anchors, section tracking,
footer navigation, direct links and operation without JavaScript.
