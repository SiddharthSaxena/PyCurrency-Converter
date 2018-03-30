# PyCurrency-Converter

[![Build Status](https://travis-ci.org/SiddharthSaxena/PyCurrency-Converter.svg?branch=master)](https://travis-ci.org/SiddharthSaxena/PyCurrency-Converter)&nbsp;&nbsp;[![PyPI Version](https://img.shields.io/badge/pypi-v1.0-orange.svg?maxAge=3600&&style=flat)](https://pypi.python.org/pypi/PyCurrency-Converter)&nbsp;&nbsp;[![Github Release](https://img.shields.io/badge/version-v1.0-red.svg?maxAge=3600&&style=flat)](https://github.com/SiddharthSaxena/PyCurrency-Converter/releases/tag/v1.0)&nbsp;&nbsp;[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?maxAge=3600&&style=flat)](https://github.com/SiddharthSaxena/PyCurrency-Converter/blob/master/LICENSE)

A python [library](https://pypi.python.org/pypi/PyCurrency-Converter) to convert currency using [Google Finance](https://finance.google.com/finance).

---

* [Installation](#installation)
* [Dependencies](#dependencies)
* [Usage](#usage)

---

### Installation

For Python 2 users:

```python
sudo pip install PyCurrency_Converter
```

For Python3 users:

```python
sudo pip3 install PyCurrency_Converter
```

Alternatively you can install git clone this repository and install it via `setup.py`.

```python
git clone https://github.com/SiddharthSaxena/PyCurrency-Converter.git
python setup.py install
```

---

### Dependencies

* BeautifulSoup

```python
sudo pip install bs4
```

* urllib

```python
sudo pip install urllib
```

---

### Usage

#### Import

``` python
>>> import PyCurrency_Converter
```

#### Get currency codes

```python
>>> import PyCurrency_Converter
>>> PyCurrency_Converter.codes()
United Arab Emirates Dirham (AED)
Afghan Afghani (AFN)
Albanian Lek (ALL)
Armenian Dram (AMD)
Netherlands Antillean Guilder (ANG)
Angolan Kwanza (AOA)
Argentine Peso (ARS)
Australian Dollar (A$)
Aruban Florin (AWG)
Azerbaijani Manat (AZN)
Bosnia-Herzegovina Convertible Mark (BAM)
Barbadian Dollar (BBD)
Bangladeshi Taka (BDT)
Bulgarian Lev (BGN)
Bahraini Dinar (BHD)
Burundian Franc (BIF)
Bermudan Dollar (BMD)
Brunei Dollar (BND)
Bolivian Boliviano (BOB)
Brazilian Real (R$)
Bahamian Dollar (BSD)
Bitcoin (฿)
Bhutanese Ngultrum (BTN)
Botswanan Pula (BWP)
BYN (BYN)
Belarusian Ruble (BYR)
Belize Dollar (BZD)
Canadian Dollar (CA$)
Congolese Franc (CDF)
Swiss Franc (CHF)
Chilean Unit of Account (UF) (CLF)
Chilean Peso (CLP)
CNH (CNH)
Chinese Yuan (CNĽ)
Colombian Peso (COP)
Costa Rican Colón (CRC)
Cuban Peso (CUP)
Cape Verdean Escudo (CVE)
Czech Republic Koruna (CZK)
German Mark (DEM)
Djiboutian Franc (DJF)
Danish Krone (DKK)
Dominican Peso (DOP)
Algerian Dinar (DZD)
Egyptian Pound (EGP)
Eritrean Nakfa (ERN)
Ethiopian Birr (ETB)
Euro (€)
Finnish Markka (FIM)
Fijian Dollar (FJD)
Falkland Islands Pound (FKP)
French Franc (FRF)
British Pound (Ł)
Georgian Lari (GEL)
Ghanaian Cedi (GHS)
Gibraltar Pound (GIP)
Gambian Dalasi (GMD)
Guinean Franc (GNF)
Guatemalan Quetzal (GTQ)
Guyanaese Dollar (GYD)
Hong Kong Dollar (HK$)
Honduran Lempira (HNL)
Croatian Kuna (HRK)
Haitian Gourde (HTG)
Hungarian Forint (HUF)
Indonesian Rupiah (IDR)
Irish Pound (IEP)
Israeli New Sheqel (₪)
Indian Rupee (₹)
Iraqi Dinar (IQD)
Iranian Rial (IRR)
Icelandic Króna (ISK)
Italian Lira (ITL)
Jamaican Dollar (JMD)
Jordanian Dinar (JOD)
Japanese Yen (Ľ)
Kenyan Shilling (KES)
Kyrgystani Som (KGS)
Cambodian Riel (KHR)
Comorian Franc (KMF)
North Korean Won (KPW)
South Korean Won (₩)
Kuwaiti Dinar (KWD)
Cayman Islands Dollar (KYD)
Kazakhstani Tenge (KZT)
Laotian Kip (LAK)
Lebanese Pound (LBP)
Sri Lankan Rupee (LKR)
Liberian Dollar (LRD)
Lesotho Loti (LSL)
Lithuanian Litas (LTL)
Latvian Lats (LVL)
Libyan Dinar (LYD)
Moroccan Dirham (MAD)
Moldovan Leu (MDL)
Malagasy Ariary (MGA)
Macedonian Denar (MKD)
Myanmar Kyat (MMK)
Mongolian Tugrik (MNT)
Macanese Pataca (MOP)
Mauritanian Ouguiya (MRO)
Mauritian Rupee (MUR) .......
```

#### Get exchange rate

```python
>>> import PyCurrency_Converter
>>> PyCurrency_Converter.convert(1, 'USD', 'INR')
68.8122 INR
```

##### General Format

```python
>>> import PyCurrency_Converter
>>> PyCurrency_Converter.convert(amount, from, to)
```
