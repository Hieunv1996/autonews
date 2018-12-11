import pypyodbc
from time import sleep
from datetime import datetime
from news_summarization import NewsSummarization
from rss_parser import RssParser

# Nếu thêm site, sửa file rss_parser.py nhé ^^
RSS_FEEDS = ['https://vnexpress.net/rss/tin-moi-nhat.rss',
             'https://dantri.com.vn/rss/tin-moi-nhat.rss',
             'https://tuoitre.vn/rss/tin-moi-nhat.rss']

SLEEP_TIME = 5 * 60

CRAWLED_FILE = 'stored/crawled.json'

SQL_CON = "Driver={SQL Server};Server=DESKTOP-LM8I71M;Database=AutoNews;uid=sa;pwd=123456"


def insert_news(news):
    try:
        connection = pypyodbc.connect(SQL_CON)
        cursor = connection.cursor()
        sql_command = (
            "INSERT INTO News(Url, Title, Description, Body, CreateDate, ShortBody, Site) VALUES (?,?,?,?,?,?,?)")
        values = [news.get_url(), news.get_title(), news.get_description(), news.get_body(),
                  news.get_create_date(), news.get_short_body(), news.get_site()]
        # Processing Query
        cursor.execute(sql_command, values)
        # Commiting any pending transaction to the database.
        connection.commit()
        # closing connection
        connection.close()
        return True
    except:
        return False


def main(log=True):
    sumary_bot = NewsSummarization('w2v/vi.vec')
    while True:
        list_news = RssParser(rss_urls=RSS_FEEDS, crawled_file=CRAWLED_FILE, log=log).get_data()
        cnt = 0
        if list_news:
            for news in list_news:
                news.set_short_body(sumary_bot.summarization(news.get_body()))
                if insert_news(news):
                    cnt += 1
        if log:
            print(str(datetime.now()) + ": Successful crawl " + str(cnt) + " news!")
            print('SLEEP IN ' + str(SLEEP_TIME) + ' Seconds.')
        sleep(SLEEP_TIME)


if __name__ == '__main__':
    main(True)
