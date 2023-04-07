import urllib.request as r
import urllib.parse as p
import bs4  # requires BeautifulSoup
import os
import zipfile
import gzip
import io

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 'Accept-Encoding': 'gzip,deflate,sdch',
 'Accept-Language': 'en-US,en;q=0.8',
 'Cache-Control': 'max_age=0',
 'Connection': 'keep-alive',
 'Content-Type': 'application/x-www-form-urlencoded',
 'Host': 'www.census.gov',
 'Referer': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36'}

data = p.urlencode({"layergroup": "ZIP Code Tabulation Areas"}).encode("utf-8")
url = 'http://www.census.gov/cgi-bin/geo/shapefiles2010/layers.cgi'

req = r.Request(url, headers=HEADERS)
req.add_header("Content-Length", len(data))
resp = r.urlopen(req, data)  # POST request

bi = io.BytesIO(resp.read())
gf = gzip.GzipFile(fileobj=bi, mode="rb")
page_bytes = gf.read()
page_text = bi.read().decode("ascii", "replace")

### This used to return gzipped bytes
# gf = gzip.GzipFile(fileobj=bi, mode="rb")
# page_bytes = gf.read()
# page_text = page_bytes.decode("ascii", "replace")

# So there's an error in the page's Javascript that not even BeautifulSoup can handle
# We need to only look at the page <body>
body_start = page_text.index("<body")
body_end = page_text.index("</body>")+len("</body>")
body_text = page_text[body_start:body_end]

soup = bs4.BeautifulSoup(body_text)

form = soup.find("form",{"name":"zcta510_2010"})
opts = form.findAll("option")

# The first option is a dummy value
# The second will download the mammoth ALL US ZIPS files
# Let's skip them both for now
skip_values = ('error', 'ZCTA5/2010/tl_2010_us_zcta510.zip')

url_state_zip = "http://www2.census.gov/geo/tiger/TIGER2010/"
HEADERS = {
    "Host": "www2.census.gov",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "Referer": "http://www.census.gov/cgi-bin/geo/shapefiles2010/file-download"}

# Download each request as a zip file, then unzip it to a folder in the same directory
for opt in opts:
    name = opt.text.strip()
    value = opt["value"]
    if not value in skip_values:
        url_state = url_state_zip + value
        req = r.Request(url_state, headers=HEADERS)
        resp = r.urlopen(req)  # GET request

        zip_name = name + ".zip"

        f_out = open(zip_name, "wb")
        f_out.write(resp.read())
        f_out.close()

        os.mkdir(name)
        zf = zipfile.ZipFile(zip_name)
        zf.extractall(name)
