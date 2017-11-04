import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen(input("Enter URL: "))
soup = BeautifulSoup(html, "html.parser")

spans = soup('span')

numbers = list()

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))