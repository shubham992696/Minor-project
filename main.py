import mechanize
from bs4 import BeautifulSoup

url = "https://www.findandtrace.com/trace-mobile-number-location"

brow = mechanize.Browser()
brow.set_handle_robots(False)

brow.open(url)
brow.select_form(name="trace")
brow['mobilenumber'] = str(input("Enter the mobile Number : "))

result = brow.submit()

soup = BeautifulSoup(result.read(), 'html.parser')
table_extr = soup.find_all('table', class_='shop_table')

data_ext = table_extr[0].find('tfoot')
count = 0
for tr in data_ext :
    count+=1
    if count in (1,4,6,8,10):
        continue
    th = tr.find('th')
    td = tr.find('td')
    print(th.text,td.text)

data_ext = table_extr[1].find('tfoot')

c = 0
for tr in data_ext :
     c+=1
     if c in (2,8,10,12,14,16,18.20,22,24,26):
         th = tr.find('th')
         td = tr.find('td')
         print(th.text,td.text)
  
