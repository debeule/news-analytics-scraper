from flask import Flask, request, jsonify
from crochet import setup, run_in_reactor, wait_for
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


setup()

app = Flask(__name__)

@app.route('/api/ArticleListScraper', methods=['POST'])
def start_spider():
    try:
        organization_id = int(request.json.get('organizationId'))

        # Run the spider asynchronously using Crochet
        run_spider(organization_id)
        
        return "bonn", 200
    
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@wait_for(timeout=60.0)
def run_spider(organization_id):
    settings = get_project_settings()
    settings.update({
        'organization_id': organization_id,
    })

    process = CrawlerRunner(settings)
    d = process.crawl("ArticleListScraper", organization_id=organization_id)

    d.addBoth(lambda _: "done")

    return d


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



# def run_spider():
#     data = request.get_json()

#     if 'organizationId' not in data:
#         return jsonify(message='Missing organizationId in the request data'), 400
    
#     try:
#         result = sync_run_spider(data)
        
#     except Exception as e:
#         return jsonify(message=str(e)), 500

#     return jsonify(result), 200
    


# @run_in_reactor
# def sync_run_spider(data):
#     crawler = CrawlerRunner(get_project_settings())
#     d = crawler.crawl("ArticleListScraper", organization_id = data['organizationId'])
#     d.addBoth(lambda _: reactor.stop())
    
#     # wait for callback = block until the crawling is finished
#     reactor.run()
#     return d
