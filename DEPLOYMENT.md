# Deployment status

Verified 2026-10-31. Project and site are already created; reuse them.

- Repository: https://github.com/Threadigit/buildxlab (owner-created public repository).
- Local source: /workspace/buildxlab, main branch.
- GitHub authorization restored after reconnecting the app. main is pushed.
  Verified remote commit 8b4dbaf8ffdafed329e5dd9182867c787b9fd573.
  Future push-triggered deployment linking is still awaiting the project Git connection.
- Vercel team: toluadetuyis-projects, team_1HRMSafo3kjx8ErMiKg6Rlww.
- Vercel project: buildxlab, prj_MOHzyRvsCKO3SLSa2HzstiYvBYke.
- Public production: https://buildxlab.vercel.app.
- Latest verified deployment (including AI-native building):
  dpl_CGubxHCzoq5ugJNthbGopRKt7jNo, READY, built directly from GitHub
  main commit 8b4dbaf8ffdafed329e5dd9182867c787b9fd573;
  production HTTP 200, live AI contact link checked on mobile, and
  responsive checks passed at 320, 390, 768, 1024, 1440 and 1920px.
  Initial assets total about 88KB compressed; no runtime JavaScript or external requests.
- Initial deployments uploaded files. The latest production build uses Git source.
  Automatic deployment on push still needs the existing project's Git connection.
  The create_git_project tool cannot reconnect an existing unlinked project;
  prefer the existing project's Git settings rather than creating duplicates.
- Framework Other/static, Node 22.x, build npm run build, output dist,
  install npm install --ignore-scripts. Production protection disabled.

## Domains

All four domains are attached and ownership verified in Vercel:
- buildxlab.co: primary.
- www.buildxlab.co, buildxlab.xyz, www.buildxlab.xyz: 308 to buildxlab.co.

DNS remains on Namecheap (dns1/dns2.registrar-servers.com), currently forwarding
or parking. No connected tool can edit the authoritative Namecheap zone.
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
3. Link existing Vercel project to Threadigit/buildxlab main and verify a Git push
   triggers a deployment. A file-upload deployment alone is not Git integration.
4. Check DNS after owner's update; preserve email records.
5. Run npm run build and npm test as relevant. The managed environment requires
   a network permission grant to launch Chromium. Its HTTPS inspection proxy CA
   is validated with curl; browser checks permit that proxy certificate.
