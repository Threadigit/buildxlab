# Deployment status

Verified 2026-10-31. The website, Git deployments and custom domains are working.
Reuse the existing project and repository.

- Repository: https://github.com/Threadigit/buildxlab, production branch main.
- Vercel team: toluadetuyis-projects, team_1HRMSafo3kjx8ErMiKg6Rlww.
- Vercel project: buildxlab, prj_MOHzyRvsCKO3SLSa2HzstiYvBYke.
- Primary production URL: https://buildxlab.co.
- Vercel alias: https://buildxlab.vercel.app.
- Automatic Git deployment verified; no manual uploads are needed.
- Verified content deployment: dpl_FNiyeeXfD93RfiKaEPJJJZKo1zqQ, READY,
  source dd1d7b92797d49fb54971a5c34cc407547547531.
- Framework Other/static, Node 22.x, build npm run build, output dist,
  install npm install --ignore-scripts. Production is public.

## Website

The current design uses a compact persistent header, Source Serif display type,
Inter body text, full-width training rows and a dark incubation section. Browser icon, touch avatar and social preview are updated.
Four areas of work: technology, builder training, incubation, and helping
organisations transition to technology and AI-native ways of working.

The ambition is technology doing 80% of the work, with a company of no more than
two people equipped with the right technology stack. Keep this aspirational.
AI research, prototyping, product development and business workflows are part of
the builder-training introduction; there is no separate AI beginner section.
Mention potential funding without naming a funding partner.

Responsive and navigation checks passed at 320, 390, 768, 1024, 1440 and 1920px,
including sticky menu position and unobscured anchor headings. No-JavaScript
rendering passed. Public HTTPS and current content were checked on buildxlab.co.

## Domains and DNS — complete

Namecheap DNS was configured through TinyFish's signed-in browser. Both domains
were saved and reloaded to confirm the records. Nameservers remain
Namecheap dns1/dns2.registrar-servers.com.

Both buildxlab.co and buildxlab.xyz have these records (Automatic TTL):

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 216.198.79.1 |
| A | @ | 64.29.17.1 |
| CNAME | www | a3e46b32b405bf40.vercel-dns-017.com. |

Vercel reports all four domain configurations valid, with no conflicts.
Ownership is verified. Public HTTPS checks confirmed:

| Address | Result |
| --- | --- |
| https://buildxlab.co/ | 200, correct website |
| https://www.buildxlab.co/ | 308 to https://buildxlab.co/, then 200 |
| https://buildxlab.xyz/ | 308 to https://buildxlab.co/, then 200 |
| https://www.buildxlab.xyz/ | 308 to https://buildxlab.co/, then 200 |

The five existing eforward MX records and Namecheap nameservers were compared
before and after and are unchanged on both domains. The existing TXT/SPF records
and mail settings were preserved. Do not change email records or nameservers.

## Resume

1. Read AGENTS.md, README.md and this file; inspect local and remote status.
2. Keep the existing GitHub/Vercel link. Never force push or create duplicates.
3. Build and check relevant behavior, push approved changes to main, then verify
   Vercel deploys that exact commit to production and reaches READY.
4. DNS is configured. Re-fetch Vercel recommendations before any future DNS work,
   and preserve existing mail records. Browser sign-in may require user refresh;
   never ask for credentials in chat.
5. Tests use Python Playwright and Chromium. The managed environment needs a
   network permission grant to launch Chromium. The HTTPS inspection proxy CA is
   validated with curl; browser checks permit that proxy certificate.
