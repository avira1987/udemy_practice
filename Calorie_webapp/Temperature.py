from selectorlib import Extractor
import requests

class Temperature:
    """ a scraoer that uses an yml file to read the xpath of a value it needs to
        extract from the timeanddate.com/weather/ url"""

    header = {
        'pragma' : 'no-cache', 
        'cache-control' : 'no-cache',
        'dnt' : '1',
        'upgrade-insecure-requests' : '1',
        'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept_language':'en-GB,en-US;q=0.9,en;q=0.8', 
        }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'
    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Builds the url string adding country and city"""
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """ Extracts a value as instructed by the yml file and return a distionary"""
        url = self._build_url()
        print(self.yml_path)
        extractor = Extractor.from_yaml_file(self.yml_path)
        print(url, extractor)
        r = requests.get(url, headers=self.header)
        print(r)
        full_content = r.text
        row_content = extractor.extract(full_content)
        return row_content

    def get(self):
        """Cleans the output of _scrape"""
        scraped_content = self._scrape()
        print(scraped_content)
        with open('f1.txt', 'w') as file: file.write(scraped_content['temp'].strip() + ' '+ self.city)
        return float(scraped_content['temp'].replace("°C", "").strip())       


if __name__ == '__main__':
    temperature = Temperature(country='IRAN',city='Gorgan')
    print(temperature.get())