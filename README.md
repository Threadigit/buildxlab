# BuildxLab

A fast, dependency-free one-page website for BuildxLab, a technology and
venture-building company.

The page introduces software/hardware development, Product Builder and Market
Builder training, incubation of Novacrust and Pagoramp, and potential access to
Buildx Capital backing. The 70% technology-powered work figure is clearly an
ambition, not an achieved metric. Owned AI tools and computing are long-term plans.

## Local development

- `npm run dev`: static preview on port 8080.
- `npm run build`: copy the public site into dist/ using Node 22+; no dependencies.
- `npm test`: responsive checks with Python Playwright and Chromium installed.
  Set BUILDXLAB_TEST_URL to test a deployment instead of the local preview.

All fonts and graphics are first-party. Font licenses are in public/assets/fonts/.
The website renders and navigates without JavaScript. Contact and training links
use x@buybuild.xyz, the temporary address requested by the owner.

## Hosting

Vercel settings are declared in vercel.json: Other/static framework, `npm run
build`, dist/ output, canonical-domain redirects, clean URLs and font caching.
GitHub main is the production branch. Production should be public; source is
published in the owner-provided Threadigit/buildxlab repository. Domain attachment and DNS status are recorded in DEPLOYMENT.md.

Primary domain: buildxlab.co. www.buildxlab.co and buildxlab.xyz should redirect
to the primary once their DNS and Vercel domain attachments are configured.
Do not change existing MX/email records when configuring website DNS.
