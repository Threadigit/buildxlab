"""Responsive and functional smoke checks for the static BuildxLab site."""
import os,json
from pathlib import Path
from playwright.sync_api import sync_playwright
base=os.environ.get('BUILDXLAB_TEST_URL','http://127.0.0.1:8080')
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(320,740),(390,844),(768,1024),(1024,768),(1440,900),(1920,1080)]:
  # The managed proxy CA is validated separately by curl; Chromium uses its own trust store.
  page=browser.new_page(ignore_https_errors=bool(os.environ.get('CODEX_PROXY_CERT')),viewport={'width':width,'height':height},reduced_motion='reduce')
  errors=[];failed=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.on('response',lambda r:failed.append((r.status,r.url)) if r.status>=400 else None)
  page.goto(base,wait_until='networkidle')
  page.evaluate('document.fonts.ready')
  assert page.locator('h1').count()==1
  assert page.locator('main').count()==1
  assert page.locator('h1').is_visible()
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),f'overflow {width}'
  for link in page.locator('a[href^="#"]').all():
   target=link.get_attribute('href')
   if len(target)>1:assert page.locator(target).count()==1,target
  page.get_by_role('link',name='Builders',exact=True).click()
  page.wait_for_function("location.hash==='#builders'")
  assert page.locator('#builders-title').is_visible()
  nav=page.locator('.index').bounding_box()
  heading=page.locator('#builders-title').bounding_box()
  assert abs(nav['y'])<2,f'menu is not stable at {width}: {nav}'
  assert heading['y']>=nav['y']+nav['height'],f'menu covers heading at {width}'
  page.get_by_role('link',name='Organisations',exact=True).click()
  page.wait_for_function("location.hash==='#organisations'")
  assert page.get_by_role('link',name='Discuss your organisation').get_attribute('href').startswith('mailto:x@buybuild.xyz')
  for image in page.locator('img').all():assert image.evaluate('e=>e.complete&&e.naturalWidth>0'),image.get_attribute('src')
  assert '70%' in page.locator('.ambition').inner_text()
  assert 'target we are working towards' in page.locator('.ambition').text_content()
  assert page.get_by_role('heading',name='Companies we are working with.').count()==1
  assert all(a.get_attribute('href').startswith('mailto:x@buybuild.xyz') for a in page.locator('.track>a').all())
  page.evaluate('window.scrollTo(0,0)')
  page.screenshot(path=f'/tmp/buildxlab-{width}.png',full_page=True)
  assert not errors,errors
  assert not failed,failed
  assert page.evaluate("performance.getEntriesByType('resource').every(r=>new URL(r.name).origin===location.origin)"),'third-party startup request'
  print(f'PASS {width}x{height}: no overflow/errors, links, images, 70% target, first-party loading')
  page.close()
 # Core copy and navigation continue to work without JavaScript.
 page=browser.new_page(java_script_enabled=False,ignore_https_errors=bool(os.environ.get('CODEX_PROXY_CERT')))
 page.goto(base,wait_until='networkidle');assert page.locator('h1').is_visible();assert page.locator('.track>a').count()==2
 print('PASS no-JavaScript rendering')
 browser.close()
