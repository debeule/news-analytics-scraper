from flask import Flask, request, jsonify
from crochet import setup, run_in_reactor, wait_for
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


setup()

app = Flask(__name__)


@app.route('/api/articles_list_scraper', methods=['POST'])
def start_articles_list_scraper_spider():
    try:
        organization_id = int(request.json.get('organizationId'))

        run_spider(organization_id)
        
        return "bonn", 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500    


@app.route('/api/article_scraper', methods=['POST'])
def start_article_scraper_spider():
    try:
        article_url = int(request.json.get('article_url'))

        run_spider(article_url)
        
        return "bonn", 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@wait_for(timeout=60.0)
def run_spider(input):
    
    process = CrawlerRunner(get_project_settings())

    if type(input) == int:
        d = process.crawl("articles_list_scraper", organization_id = input)

    if type(input) == str:
        d = process.crawl("article_scraper", article_url = input)


    d.addBoth(lambda _: "done")

    return d


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)