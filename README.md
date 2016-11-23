# PyCurrency-Converter

[![Build Status](https://travis-ci.org/SiddharthSaxena/PyCurrency-Converter.svg?branch=master)](https://travis-ci.org/SiddharthSaxena/PyCurrency-Converter)&nbsp;&nbsp;[![Github Release](https://img.shields.io/badge/version-v1.0-red.svg?maxAge=3600&&style=flat)](https;//github.com/SiddharthSaxena/PyCurrency-Converter/releases/tag/v1.0)&nbsp;&nbsp;[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?maxAge=3600&&style=flat)](https://github.com/SiddharthSaxena/PyCurrency-Converter/blob/master/LICENSE)

A python [library]() to convert currency using [Google Finance](https://www.google.com/finance).

---

###Installation

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
python setup.py install or python3 setup.py install
```

---

###Dependencies

* BeautifulSoup

```python
sudo pip install bs4
```

* urllib

```python
sudo pip install urllib
```

---

###Usage

####Import

``` python
import PyCurrency_Converter
```

####Get exchange rate

```python
PyCurrency_Converter.convert(1, 'USD', 'INR')
68.69
```

#####General Format

```python
PyCurrency_Converter.convert(amount, from, to)
```
