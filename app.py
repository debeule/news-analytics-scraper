from flask import Flask, request, jsonify
from crochet import setup, run_in_reactor, wait_for
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from twisted.internet import reactor
from scrapy.signalmanager import dispatcher
from scrapy import signals

from scrapyscript import Job, Processor
from scrapy.utils.project import get_project_settings

app = Flask(__name__)

@app.route('/api/article_scraper', methods=['POST'])
def start_article_scraper_spider():
    try:
        organization_id = int(request.json.get('organization_id'))
        url = request.json.get('url')

        job = Job('article_scraper', organization_id = organization_id, url = url)
        processor = Processor(settings=get_project_settings())
       
        result = processor.run(job)

        if result is None or not result:  raise ValueError('scraping article failed')

        return jsonify({'response': result}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500 
    

@app.route('/api/articles_list_scraper', methods=['POST'])
def start_articles_list_scraper_spider():
    try:
        organization_id = int(request.json.get('organization_id'))

        job = Job('articles_list_scraper', organization_id = organization_id)
        processor = Processor(settings=get_project_settings())

        result = processor.run(job)

        if result is None or not result:  raise ValueError('scraping article failed')
        
        return jsonify({'response': result}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)