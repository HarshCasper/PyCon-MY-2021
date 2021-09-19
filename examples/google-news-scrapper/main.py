import requests
from xml.dom.minidom import parseString

def get_google_news_result(term):
    """Function to pass a term and get the top 5 Google News results"""

    count = 5
    results = []

    obj = parseString(requests.get('https://news.google.com/news/feeds?q={}&output=rss'.format(term)).text)
    items = obj.getElementsByTagName('item')
    links = list()

    for item in items[:count]:
        link = ""
        for node in item.childNodes:
            if node.nodeName == 'link':
                link = node.firstChild.data
        links.append(link)

    return links

if __name__ == "__main__":
    print(get_google_news_result('bitcoin'))
