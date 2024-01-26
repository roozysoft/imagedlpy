import requests

url = 'URL'  # Replace with the desired image URL

response = requests.get(url)

if response.status_code == 200:
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    print("Image downloaded successfully")
else:
    print("Failed to download image")
