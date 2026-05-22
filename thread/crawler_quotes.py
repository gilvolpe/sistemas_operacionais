import threading
import requests
from bs4 import BeautifulSoup

class CrawlerQuotes(threading.Thread):
    def __init__(self,url_base,pages):
        super().__init__()
        self.url_base = url_base
        self.page_begin = pages[0]
        self.page_end   = pages[1]

        self.html = []
        self.authors = []
        self.quotes  = []
        self.tags = []

    def run(self):
        print(f'Thread scrapping pages from {self.page_begin} to {self.page_end}')
        for idx in range(self.page_begin,self.page_end+1):
            url = self.url_base + str(idx) + '/'
            r = requests.get(url)
            html = r.text
            self.html.append(html)
            soup = BeautifulSoup(html,'lxml')
            for div in soup.find_all('div',class_='quote'):
                span = div.find('span',class_='text')
                self.quotes.append(span.text)
                small = div.find('small', class_='author')
                self.authors.append(small.text)
                
                tags = div.find('div', class_='tags')
                tmp_tag = []
                for t in tags.find_all('a',class_='tag'):
                    tmp_tag.append(t.text)
                    self.tags.append(t.text)

                print(f'\nQuote:{span.text}\n\rBy:{small.text}\n\rTags:{tmp_tag}\n')


if __name__ == '__main__':
    indices_crawler = []
    for i in range(0,10):
        indices_crawler.append((i*10+1,i*10+10))
    print(indices_crawler)

    threads = []
    for pages in indices_crawler:
        crawler = CrawlerQuotes('https://quotes.toscrape.com/page/',pages)
        #crawler.run()
        crawler.start()
        threads.append(crawler)

    for t in threads:
        t.join()
