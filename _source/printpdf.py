import asyncio, sys
from playwright.async_api import async_playwright

FOOTER = """
<div style="width:100%; font-family: Arial, sans-serif; font-size:7.5pt; color:#5b6672;
            padding: 0 20mm; display:flex; justify-content:space-between;">
  <span>Eike Düvel, curriculum vitae, November 2026</span>
  <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>"""

async def main(src, out):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page()
        await pg.goto("file://" + src)
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(800)
        await pg.pdf(path=out, format="A4", print_background=True,
                     prefer_css_page_size=True, display_header_footer=True,
                     header_template="<span></span>", footer_template=FOOTER)
        await b.close()

asyncio.run(main(sys.argv[1], sys.argv[2]))
