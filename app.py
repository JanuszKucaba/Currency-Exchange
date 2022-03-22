'''
Simple currency exchange application
'''
from flask import Flask, render_template, request
from nbp import nbp_rates


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    '''Main site'''
    if request.method == 'POST':
        try:
            value = float(request.form['value1'])
        except ValueError or KeyError:
            value = 0

        currency1 = request.form['currency_from']
        currency2 = request.form['currency_to']
        currencies_rates = nbp_rates()

        currencies = ['PLN', 'USD', 'EUR', 'GBP', 'CHF']

        if currency1 == currency2:
            res = value
        elif currency1 == 'PLN':
            res = round((value / currencies_rates[str(currency2)]), 2)
        elif currency2 == 'PLN':
            res = round((value * currencies_rates[str(currency1)]), 2)
        else:
            res = -1

        return render_template('index.html',
                                currencies_rates=currencies_rates,
                                currencies=currencies,
                                res=res,
                                value=value,
                                currency1=currency1,
                                currency2=currency2
                            )

    currencies_rates = nbp_rates()
    currencies = ['PLN', 'USD', 'EUR', 'GBP', 'CHF']
    res, value = '', ''
    return render_template('index.html',
                            currencies_rates=currencies_rates,
                            currencies=currencies,
                            res=res,
                            value=value
                        )


if __name__ == '__main__':
    app.run()
