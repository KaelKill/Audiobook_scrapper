from bs4 import BeautifulSoup
import requests
import wget

def main(): 
    url = 'https://librivox.org/api/feed/audiobooks'
    page = BeautifulSoup(requests.get(url).content)

    books = page.xml.books
    
    for book in books.contents:
        # print(book.url_zip_file)
        url = book.contents[8].contents[0]
        print(url)
        wget.download(url)
        
if __name__== '__main__':
    main()