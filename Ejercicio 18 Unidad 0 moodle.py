##Algorithm conversion
##Inputs: currency_exchange_rate: real
##Output: real
##Constants:
##Variables: euros: real
##           dolares: real
##Start
##    currency_exchange_rate <-- 1.08
##    euros = 100
##    dolares = euros * currency_exchange_rate
##    return dolares
##End

euros = input('Enter the euros:')
euros = float(euros)

currency_exchange_rate = 1.08
dolares = euros * currency_exchange_rate
print('Euros in dolares is', dolares)
