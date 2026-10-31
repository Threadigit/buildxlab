"""Responsive and functional smoke checks for the static BuildxLab site."""
import os,json,time
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
  assert page.locator('.index').bounding_box()['y']>0,'menu must scroll into place first'
  assert page.locator('.navigation').evaluate("e=>getComputedStyle(e).borderTopWidth==='0px'&&getComputedStyle(e).borderBottomWidth==='0px'"),'menu must not have permanent divider lines'
  assert page.locator('.nav-label').evaluate_all("els=>els.every(e=>getComputedStyle(e,'::after').opacity==='0')"),'indicators must stay hidden before a section is reached'
  assert page.get_by_role('link',name='Talk to us',exact=True).bounding_box()['height']>=44
  page.get_by_role('link',name='Builders',exact=True).click()
  page.wait_for_function("location.hash==='#builders'")
  assert page.locator('#builders-title').is_visible()
  nav=page.locator('.navigation').bounding_box()
  heading=page.locator('#builders-title').bounding_box()
  assert abs(nav['y'])<2,f'menu is not stable at {width}: {nav}'
  assert abs(nav['x'])<2 and abs(nav['width']-width)<2,f'menu background must span the viewport at {width}'
  assert heading['y']>=nav['y']+nav['height'],f'menu covers heading at {width}'
  page.get_by_role('link',name='Organisations',exact=True).click()
  page.wait_for_function("location.hash==='#organisations'")
  assert page.get_by_role('link',name='Discuss your organisation').get_attribute('href').startswith('mailto:x@buybuild.xyz')
  for image in page.locator('img').all():assert image.evaluate('e=>e.complete&&e.naturalWidth>0'),image.get_attribute('src')
  assert '80%' in page.locator('.ambition').inner_text()
  assert 'target we are working towards' in page.locator('.ambition').text_content()
  assert page.get_by_role('heading',name='Companies currently in incubation.').count()==1
  assert all(a.get_attribute('href').startswith('mailto:x@buybuild.xyz') for a in page.locator('.track>a').all())
  # Manual scrolling must update the current section in both directions, without changing history.
  original_hash=page.evaluate('location.hash')
  for section_id in ['technology','builders','companies','organisations','companies','builders','technology']:
   page.evaluate("id=>window.scrollTo(0,document.getElementById(id).getBoundingClientRect().top+scrollY-document.querySelector('.navigation').offsetHeight-16)",section_id)
   page.wait_for_function("id=>document.querySelector('.index a[aria-current=\"location\"]')?.getAttribute('href')==='#'+id",arg=section_id,timeout=3000)
   assert page.locator('.index a[aria-current="location"]').count()==1
   assert page.locator('.index a[aria-current] .nav-label').evaluate("e=>getComputedStyle(e,'::after').opacity==='1'"),'current section must have a fine text indicator'
   assert page.locator('.index a[aria-current]').evaluate("e=>getComputedStyle(e).backgroundColor==='rgba(0, 0, 0, 0)'"),'active section must not use a black block'
   assert page.locator('.index a:not([aria-current]) .nav-label').evaluate_all("els=>els.every(e=>getComputedStyle(e,'::after').opacity==='0')")
   if section_id=='companies':
    assert page.evaluate("[1,innerWidth-1].every(x=>document.elementFromPoint(x,20)?.closest('.navigation'))"),'menu background detaches over dark section'
  assert page.evaluate('location.hash')==original_hash
  page.evaluate('window.scrollTo(0,document.documentElement.scrollHeight)')
  page.wait_for_function("document.querySelector('.index a[aria-current=\"location\"]')?.getAttribute('href')==='#organisations'",timeout=3000)
  assert abs(page.locator('.navigation').bounding_box()['y'])<2,'menu must stay pinned through the footer'
  page.get_by_role('link',name='Back to BuildxLab home',exact=True).click()
  page.wait_for_function("!document.querySelector('.index a[aria-current]')",timeout=3000)
  page.mouse.move(0,0)
  page.screenshot(path=f'/tmp/buildxlab-{width}.png',full_page=True)
  assert not errors,errors
  assert not failed,failed
  assert page.evaluate("performance.getEntriesByType('resource').every(r=>new URL(r.name).origin===location.origin)"),'third-party startup request'
  print(f'PASS {width}x{height}: full-width sticky menu, scroll highlighting, content, links and first-party loading')
  page.close()
 # A direct section link must be highlighted after loading, too.
 page=browser.new_page(ignore_https_errors=bool(os.environ.get('CODEX_PROXY_CERT')),reduced_motion='reduce')
 page.goto(base.rstrip('/')+'/#companies',wait_until='networkidle')
 page.wait_for_function("document.querySelector('.index a[aria-current=\"location\"]')?.getAttribute('href')==='#companies'",timeout=3000)
 page.close()
 print('PASS direct section link highlighting')
 # Core copy and navigation continue to work without JavaScript.
 page=browser.new_page(java_script_enabled=False,ignore_https_errors=bool(os.environ.get('CODEX_PROXY_CERT')))
 page.goto(base,wait_until='networkidle');assert page.locator('h1').is_visible();assert page.locator('.track>a').count()==2
 page.get_by_role('link',name='Builders',exact=True).click()
 # Poll from Python: page-level animation-frame polling is disabled with JavaScript off.
 for _ in range(40):
  if abs(page.locator('.navigation').bounding_box()['y'])<2:break
  time.sleep(.05)
 assert abs(page.locator('.navigation').bounding_box()['y'])<2
 print('PASS no-JavaScript rendering')
 browser.close()
