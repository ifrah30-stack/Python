# 11. GET Request
import requests
response = requests.get('https://api.github.com/users')

# 12. POST Request
data = {'name': 'John'}
res = requests.post('https://api.example.com/create', json=data)

# 13. Handle JSON response
result = res.json()

# 14. API authentication
res = requests.get(url, headers={'Authorization': 'Bearer <token>'})

# 15. Retry on failure
from requests.adapters import HTTPAdapter
s = requests.Session()
s.mount('https://', HTTPAdapter(max_retries=3))

# 16. Timeout handling
requests.get(url, timeout=5)

# 17. File upload
files = {'file': open('report.pdf', 'rb')}
requests.post(url, files=files)

# 18. Custom headers
requests.get(url, headers={'User-Agent': 'MNCApp'})

# 19. Download file
with open('image.png', 'wb') as f:
    f.write(requests.get(img_url).content)

# 20. API pagination
while url:
    data = requests.get(url).json()
    url = data.get('next')
