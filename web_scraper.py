import requests
from bs4 import BeautifulSoup as bs 

username = input('Input Github username: ')
url = 'https://github.com/' + username
res = requests.get(url)
content = bs(res.content, 'html.parser')
image = content.find('img', {'alt': 'Avatar'})['src']
profile = content.find('div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'})
result = {}
result['Avatar'] = image
result['Bio'] = profile.text

print(image, '\n', profile.text)
print(result)

# Print out multiple data points and store in dictionary before committing code
