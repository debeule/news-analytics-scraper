### scrapy test spider command
docker exec websitetest-scraper-1 scrapy crawl articles_list_scraper -a organization_id=1
docker exec websitetest-scraper-1 curl -X POST -H "Content-Type: application/json" -d '{"organizationId": "1"}' http://localhost:5000/api/articles_list_scraper


docker exec websitetest-scraper-1 scrapy crawl article_scraper -a article_url=

### to install project dependencies & activate virtual environment:
    python3 -m venv venv

    pip install -r requirements.txt

    source "source_dir"/venv/Scripts/activate
