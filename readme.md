### scrapy test article_list_scraper example
docker exec scraper scrapy crawl articles_list_scraper -a organization_id=1
docker exec scraper curl -X POST -H "Content-Type: application/json" -d '{"organizationId": "1"}' http://localhost:5000/api/articles_list_scraper

### scrapy test articles_list_scraper example
docker exec scraper scrapy crawl articles_list_scraper -a organization_id=1

### scrapy test article_scraper example
docker exec scraper scrapy crawl article_scraper -a url=https://www.tijd.be/markten-live/live-chat/herlees-de-marktenchat-over-nvidia-umicore-en-lotus-bakeries/10547603.html -a organization_id=1

### to install project dependencies & activate virtual environment:
    python3 -m venv venv

    pip install -r requirements.txt

    source "source_dir"/venv/Scripts/activate
