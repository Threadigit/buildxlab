# Deployment status

Verified 2026-10-31. Project and site are already created; reuse them.

- Repository: https://github.com/Threadigit/buildxlab (owner-created public repository).
- Local source: /workspace/buildxlab, main branch.
- GitHub authorization restored after reconnecting the app. main is pushed.
  main is connected to the existing Vercel project. A Git push triggered
  production deployment dpl_2mKBiE3U7zSFDs74C8Q6LMSESr87 (READY),
  commit 48754b9fc894f06b13011662e1ee1dfcc8dbebe2.
- Vercel team: toluadetuyis-projects, team_1HRMSafo3kjx8ErMiKg6Rlww.
- Vercel project: buildxlab, prj_MOHzyRvsCKO3SLSa2HzstiYvBYke.
- Public production: https://buildxlab.vercel.app.
- Verified editorial redesign deployment (including organisational transition):
  dpl_3uMXTVXKYDKNBhrDdMQhWEfD5oBB, READY, built automatically from GitHub
  main commit 2b0dc8df2d0502b13169540cc845a6fa55529084;
  production HTTP 200, icon/avatar/social preview HTTP 200,
  live organisational contact path and sticky menu checked on mobile, and
  responsive checks passed at 320, 390, 768, 1024, 1440 and 1920px.
  Initial assets total about 88KB compressed; no runtime JavaScript or external requests.
- Automatic Git deployments are enabled for Threadigit/buildxlab main.
  The owner connected the existing project in Vercel Git settings; do not create
  another project. Initial deployments uploaded files before Git was connected.
- Framework Other/static, Node 22.x, build npm run build, output dist,
  install npm install --ignore-scripts. Production protection disabled.

## Domains

All four domains are attached and ownership verified in Vercel:
- buildxlab.co: primary.
- www.buildxlab.co, buildxlab.xyz, www.buildxlab.xyz: 308 to buildxlab.co.

DNS remains on Namecheap (dns1/dns2.registrar-servers.com), currently forwarding
or parking. TinyFish browser automation is now connected; Namecheap sign-in
is still required before it can edit the authoritative DNS zone. The owner
approved opening secure sign-in, and the setup link was provided. Await their
saved profile before running the DNS automation. Do not ask for credentials in chat.
Vercel's current rank-1 recommendations for BOTH domains:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 216.198.79.1 |
| A | @ | 64.29.17.1 |
| CNAME | www | a3e46b32b405bf40.vercel-dns-017.com. |

Replace conflicting website forwarding/parking records only. Preserve all MX,
TXT and email records. Re-fetch Vercel domain config before future DNS changes.
After the owner saves records, verify domain config, public HTTPS, and redirects.
Do not claim the custom domains serve this site until these checks pass.

## Resume

1. Read this file and AGENTS.md, inspect local status and current Vercel state.
2. GitHub push works. Never force push.
3. Push approved changes to main, then verify Vercel creates a production
   deployment for that exact commit and reaches READY. No manual upload needed.
4. Check DNS after owner's update; preserve email records.
5. Run npm run build and npm test as relevant. The managed environment requires
   a network permission grant to launch Chromium. Its HTTPS inspection proxy CA
   is validated with curl; browser checks permit that proxy certificate.
