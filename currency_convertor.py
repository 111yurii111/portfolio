from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

#input
amount = input("How much: ")
curency1 = input("Of what curency: ")
curency2 = input("To what curency: ")


url = f"https://www.google.com/search?q=%22{amount}+{curency1}+in+{curency2}%22&biw=885&bih=825&sxsrf=APq-WBtZCaQmVORos3cBfe8m93J0UNaK8g%3A1644151304929&ei=CML_YZCRONiDi-gP8fODoA8&ved=0ahUKEwiQtfLzjOv1AhXYwQIHHfH5APQQ4dUDCA4&uact=5&oq=%22{amount}+{curency1}+in+{curency2}22&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEA0QHjIICAAQDRAFEB4yCAgAEAgQDRAeOgcIABBHELADOgQIIxAnOgUIABCRAjoECC4QQzoFCC4QgAQ6BQgAEIAEOgkIIxAnEEYQggI6BggAEAcQHjoICAAQBxAKEB46BAgAEEM6BAgAEAo6CggAEJECEEYQggI6CggAEIAEEEYQggI6CAgAEAgQBxAeOggIABAIEAoQHjoKCAAQCBANEAoQHkoECEEYAEoECEYYAFDliwFYgd8CYNvuAmgJcAF4AIABkAGIAdIbkgEEMi4yOZgBAKABAcgBBMABAQ&sclient=gws-wiz"
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
find = soup.find("span", {"class":"DFlfde SwHCTb"}).text#finds the information

print(amount, "in", curency1, "is", find, "in", curency2)
