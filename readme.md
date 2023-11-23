command:
scrapy crawl ArticleListScraper -a scrape_url=  -a operation=
scrapy crawl ArticleListScraper -a scrape_url=http://scrapingtester.matthias.debeule.nxtmediatech.eu/ -a operation=create
scrapy crawl ArticleListScraper -a scrape_url=https://www.tutorialspoint.com/selenium/selenium_environment_setup.htm -a operation=create

scrapy crawl ArticleListScraper -a scrape_url=https://www.hln.be/net-binnen -a operation=create
scrapy crawl ArticleListScraper -a provider=hln



### to install project dependencies & activate virtual environment:
python -m venv venv

source "source_dir"/venv/Scripts/activate

pip install -r requirements.txt