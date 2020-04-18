import requests, bs4 

def get_price(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#listing_0 > div.srp-list-item-description > a > div.great-value.value-badge-srp > div > span')
    return elems[0].text[7:]

def get_model(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#listing_0 > div.listing-header > span')
    return elems[0].text

car_price = get_price('https://www.carfax.com/Used-Cars-in-Brooklyn-NY_c10456')
car_model = get_model('https://www.carfax.com/Used-Cars-in-Brooklyn-NY_c10456')

print('The price for a ' + car_model + " is " + car_price + ".")