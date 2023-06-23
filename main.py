from bs4 import BeautifulSoup
import requests
import wget
import json

def main(): 
    offset = 0
    url = 'https://librivox.org/api/feed/audiobooks/?format=json&fields={title,language,url_zip_file}&limit=5000&&offset=0'
    page = requests.get(url, 'json')

    books = json.loads(page.text)
    
    for book in books['books']:
        if(book['language'] == 'Portuguese'):
            print(book['title'])
            url = book['url_zip_file']
            wget.download(url)

        
if __name__== '__main__':
    main()