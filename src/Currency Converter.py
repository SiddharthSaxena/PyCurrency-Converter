#!/usr/bin/env python3
import pycurrency

To = input('Convert To: ')
amount = input('Amount: ')
From = input('Convert from: ')

print(pycurrency.get(amount, From, To))
