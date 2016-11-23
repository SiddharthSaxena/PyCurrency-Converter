try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    import BeautifulSoup


# Add feature to print codes of different currency conversion available at Google Finance.
class PyCurrency:
    @staticmethod
    def convert(amount, _from, _to):
        url = 'https://www.google.com/finance/converter?a={}&from={}&to={}'.format(amount, _from, _to)
        response = urllib2.urlopen(url)
        html = response.read()
        parser = BeautifulSoup(html, 'lxml')
        parsed = parser.body.find('span', attrs={'class': 'bld'}).text
        return parsed


def convert(amount, _from, _to):
    return PyCurrency.convert(amount, _from, _to)
