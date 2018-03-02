import urllib.request
from bs4 import BeautifulSoup


BASE_URL = 'http://gen.lib.rus.ec/'
BASE_DOWNLAOD_LINK = 'http://libgen.io/ads.php'

def browse(term):
    url = BASE_URL + 'search.php/?req=' + (term.replace(' ', '+'))
    result = urllib.request.urlopen(url)
    assert result
    
    return result

def get_dict_of_books(result):
    results = []

    soup = BeautifulSoup(result, 'html.parser')
    soup = soup.find_all('table', attrs={'align': 'center'})[0]
    search_results = soup.find_all('tr') [1:]

    for r in search_results:
        columns = r.find_all('td')
        
        ## Get book's author
        author = columns[1].get_text()
        
        ## Get books' title
        title = columns[2]
        title = title.find('a')
        if title.find('font'): title.find('font').extract()
        title = title.get_text()
        
        ## Book's md5
        md5 = columns[2].find('a', attrs={'title': True})['href']
        results.append({
            'title': title, 
            'author': author,
            'md5': md5.replace('book/index.php?md5=', '' )
        })
    return results

def fetch(md5):
    assert md5
    url = BASE_DOWNLAOD_LINK + '?md5=' + md5
    result = urllib.request.urlopen(url)
    soup = BeautifulSoup(result, 'html.parser')
    
    return soup.table.find_all('td')[2].a['href']

def search(term):
    return get_dict_of_books(browse(term))

