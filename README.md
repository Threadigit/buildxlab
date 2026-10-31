# BuildxLab

A fast, dependency-free one-page website for BuildxLab, a technology and
venture-building company.

The page introduces software/hardware development, Product Builder and Market
Builder training, incubation of Novacrust and Pagoramp, organisational transition to technology and AI-native workflows, and potential funding.
The 80% technology-powered work figure is clearly an
ambition, not an achieved metric. The target company has no more than two people,
equipped with the right technology stack. Owned AI tools and computing are long-term plans.

## Local development

- `npm run dev`: static preview on port 8080.
- `npm run build`: copy the public site into dist/ using Node 22+; no dependencies.
- `npm test`: responsive checks with Python Playwright and Chromium installed.
  Set BUILDXLAB_TEST_URL to test a deployment instead of the local preview.

Fonts and graphics are served locally. See DESIGN.md for the approved brand reference. Font licenses are in public/assets/fonts/.
The website renders and navigates without JavaScript. The section menu stays
visible while scrolling; anchor offsets keep headings clear on phones and desktops.
The browser icon and social preview use the full BuildxLab name. Contact and training links
use x@buybuild.xyz, the temporary address requested by the owner.

## Hosting

Vercel settings are declared in vercel.json: Other/static framework, `npm run
build`, dist/ output, canonical-domain redirects, clean URLs and font caching.
GitHub main is connected to Vercel and deploys automatically on every push.
Production is public; source is published in Threadigit/buildxlab.
Domain attachment and DNS status are recorded in DEPLOYMENT.md.

Primary domain: buildxlab.co. www.buildxlab.co, buildxlab.xyz and www.buildxlab.xyz
redirect to the primary. DNS, HTTPS and all redirects are verified working.
Do not change existing MX/email records when configuring website DNS.
