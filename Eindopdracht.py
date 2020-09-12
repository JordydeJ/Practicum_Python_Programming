# Valuta wisselen
# Jordy de Jong
# 12-09-2020

"""
prijs US dollar
prijs GB pound
prijs Japense Yen

Optie 1 wisselen vanuit USD
Optie 2 wisselen vanuit GBP
Optie 3 wisselen vanuit JPY

Invoer bedrag

Berekenen valuta naar euro

Berekenen van transactiekosten 1,5%
Min. 2 euro
Max. 15 euro

Tonen bedrag in euro's
Tonen bedrag transactiekosten
Tonen ontvangen bedrag in euro's

"""


transactie = 0
bedrag = 0

koers_usd = 0
koers_gbp = 0
koers_jpy = 0
USD_NAAR_EURO = 0.84
GBP_NAAR_EURO = 1.08
JPY_NAAR_EURO = 0.008
TRANSACTIE_PERCENTAGE = 0.015

valuta_lijst = ["Amerikaanse Dollar", "Engelse Pond", "Japanse Yen"]


def koers_usd_func():
    import requests

    global koers_usd

    van_valuta = "USD"
    naar_valuta = "EUR"

    api_key = "Q9CY81B4JZVHKTP1"

    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    main_url = base_url + "&from_currency=" + van_valuta + "&to_currency=" + naar_valuta + "&apikey=" + api_key

    req_ob = requests.get(main_url)

    result = req_ob.json()

    koers_usd = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])


def koers_gbp_func():
    import requests

    global koers_gbp

    van_valuta = "GBP"
    naar_valuta = "EUR"

    api_key = "Q9CY81B4JZVHKTP1"

    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    main_url = base_url + "&from_currency=" + van_valuta + "&to_currency=" + naar_valuta + "&apikey=" + api_key

    req_ob = requests.get(main_url)

    result = req_ob.json()

    koers_gbp = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])


def koers_jpy_func():
    import requests

    global koers_jpy

    van_valuta = "JPY"
    naar_valuta = "EUR"

    api_key = "Q9CY81B4JZVHKTP1"

    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    main_url = base_url + "&from_currency=" + van_valuta + "&to_currency=" + naar_valuta + "&apikey=" + api_key

    req_ob = requests.get(main_url)

    result = req_ob.json()

    koers_jpy = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])


def format_valuta_func(valuta):
    if valuta == "Amerikaanse Dollar":
        koers_usd_func()
        return f"{valuta.title()} - {koers_usd} USD"
    elif valuta == "Engelse Pond":
        koers_gbp_func()
        return f"{valuta.title()} - {koers_gbp} GBP"
    elif valuta == "Japanse Yen":
        koers_jpy_func()
        return f"{valuta.title()} - {koers_jpy} JPY"


def valuta_keuze_func(keuze):
    print("Hallo, u kunt bij ons de onderstaande valuta wisselen naar euro's")
    for valuta in keuze:
        print(format_valuta_func(valuta))


def omwisseling_func():

    global transactie
    global bedrag
    global koers_usd
    global koers_gbp
    global koers_jpy

    gekozen_valuta = int(input(f"\n0. voor {valuta_lijst[0]}\n1. voor {valuta_lijst[1]}\n2. voor {valuta_lijst[2]}\nKies uw valuta nummer: "))
    if gekozen_valuta != 0 and gekozen_valuta != 1 and gekozen_valuta != 2:
        print(f"Invoer onbekend, het programma zal worden herstart\n")
        return
    else:
        om_te_wisselen_bedrag = float(input(f"\nHoeveel {valuta_lijst[gekozen_valuta]} wilt u omwisselen in euro's? "))
        if gekozen_valuta == 0:
            bedrag = float(om_te_wisselen_bedrag * koers_usd)
            print("\nNa omwisselen bedraagt het %.2f euro" % bedrag)
            transactie += 1
        elif gekozen_valuta == 1:
            bedrag = float(om_te_wisselen_bedrag * koers_gbp)
            print("\nNa omwisselen bedraagt het %.2f euro" % bedrag)
            transactie += 1
        elif gekozen_valuta == 2:
            bedrag = float(om_te_wisselen_bedrag * koers_jpy)
            print("\nNa omwisselen bedraagt het %.2f euro" % bedrag)
            transactie += 1


def transactiekosten_func():

    global TRANSACTIE_PERCENTAGE
    global bedrag

    transactiekosten = bedrag * TRANSACTIE_PERCENTAGE

    if transactiekosten < 2:
        bedrag = bedrag - 2
        print(f"Uw transactiekosten bedragen: 2 euro")
    elif transactiekosten > 15:
        bedrag = bedrag - 15
        print(f"Uw transactiekosten bedragen: 15 euro")
    else:
        bedrag = bedrag - transactiekosten
        print(f"uw transactiekosten bedragen: {transactiekosten}")


def uitgifte_func():
    global bedrag

    print(f"U ontvangt: {bedrag}")


while transactie < 1:
    valuta_keuze_func(valuta_lijst)
    omwisseling_func()
    transactiekosten_func()
    uitgifte_func()
    if transactie == 1:
        print(f"Bedankt voor uw transactie, wij wensen u een prettige dag")
