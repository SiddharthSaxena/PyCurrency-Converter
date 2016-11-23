#!/usr/bin/env python3
import PyCurrency

To = input('Convert To: ')
amount = input('Amount: ')
From = input('Convert from: ')

print(PyCurrency.get(amount, From, To))
