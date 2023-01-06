# guide to web scraping

# get the page title
import requests
import bs4
from PIL import Image

result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
soup = bs4.BeautifulSoup(result.text, 'lxml')

salk_image = soup.select('img')[0]
salk_table_content = soup.select('.toclevel-1')


# print(soup)
# print(salk_image['src'])
# print(salk_table_content)

image_link = requests.get(
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Jonas_Salk_candid.jpg/220px-Jonas_Salk_candid.jpg')
# print(image_link.content)

# f = open('jonas_salk.jpg', 'wb')
# f.write(image_link.content)
# f.close()

# with open("jonas_salk.jpg", "wb") as img:
#     img.write(image_link.content)

img = Image.open(requests.get(salk_image['src'], stream=True).raw)
img.save('jonas_salk.jpg')
