from requests import get
from bs4 import BeautifulSoup
import time



f = open("educ_urls", "a")


for x in range(797):

	trycnt = 1

	while trycnt > 0:
		try:

			url = "https://godfgkldfg.com/d=%s" % (x)
			resp = get(url)

			html_sp = BeautifulSoup(resp.text, 'html.parser')

			for y in range(len(html_sp.find_all('div', class_='smlbooks book'))):
		
				f.write("https://books-library.online/%s\n" % (html_sp.find_all('div', class_='smlbooks book')[y].a['href']))
			trycnt = 0

		except:
			if trycnt <= 0: print("Failed to retrieve")	
			else: trycnt -= 1
			time.sleep(0.05)

f.close()
