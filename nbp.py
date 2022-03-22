'''
Module to gets actual currency rates from nbp.pl
'''

import requests


def nbp_rates():
    '''gets actual currency rates from nbp.pl
    returns a dict with currencies and their values'''
    url = 'http://api.nbp.pl/api/exchangerates/tables/A/'

    response = requests.get(url)
    #print(response)
    rates = response.json()

    currencies = {}
    for i in rates[0]['rates']:
        currencies[i['code']] = i['mid']

    date = rates[0]['effectiveDate']
    currencies['date'] = date

    return currencies


if __name__ == '__main__':
    print(nbp_rates())
