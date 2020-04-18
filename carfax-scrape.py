import requests, bs4 

# Refactored code
def get_model_and_car(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    models = soup.select('#listing_0 > div.listing-header > span')
    price = soup.select('#listing_0 > div.srp-list-item-description > a > div.great-value.value-badge-srp > div > span')

    return 'The price for a ' + models[0].text + " is " + price[0].text[7:] + "."

# def get_price(url):
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     elems = soup.select('#listing_0 > div.srp-list-item-description > a > div.great-value.value-badge-srp > div > span')
#     return elems[0].text[7:]

# def get_model(url):
#     res = requests.get(url)
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     elems = soup.select('#listing_0 > div.listing-header > span')
#     return elems[0].text

# car_price = get_price('https://www.carfax.com/Used-Cars-in-Brooklyn-NY_c10456')
# car_model = get_model('https://www.carfax.com/Used-Cars-in-Brooklyn-NY_c10456')


print(get_model_and_car('https://www.carfax.com/Used-Cars-in-Brooklyn-NY_c10456'))