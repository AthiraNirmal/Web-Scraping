# Web-Scraping
Web Scarping is the automatic method of extraction data and content from a website. It is really helpful for data harvesting. These can be used for price comparison, sentiment analysis ,news monitoring etc. Web scraping tools are software that first recognizes unique html tags and then extract and transform the content.

Here, the scarping code is written completely in Python using Scrapy and the scraped data is stored into MongoDb Database.

Install Scrapy : pip install Scrapy
Install pyMongo: pip install pymongo

Run: scrapy crawl -s MONGODB_URI="mongodb+srv://<YOUR_CONNECTION_STRING>" -s MONGODB_DATABASE="scrapy" quotes

  ** *Obtain the Connection String from MongoDb Atlas, Go to "connect" in your preferred Cluster and choose "Connect your Application".
Select Driver(Python) and Version***

If you wish not to store data into Database: To Run, first go into the srapy project folder (cd stack) and then: scrapy crawl stack -o output.csv
  This will save the data into a csv file
  
  PS: In this case make the necessary changes to pipelines.py by replacing Class MongoDBPipeline with: 
  
class StackPipeline:
  def process_item(self, item, spider):
      return item
      
  Remove ITEM_PIPELINES = {"stack.pipelines.MongoDBPipeline": 500} from settings.py
