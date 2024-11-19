incomes = input('Please enter your incomes: ')
incomes = float(incomes)

THRESHOLD_VERY_LOW = 12450
THRESHOLD_LOW = 20200
THRESHOLD_MEDIUM = 35000
THRESHOLD_HIGH = 60000
THRESHOLD_VERY_HIGH = 300000

PERCENT_MINIMUM = 0.19
PERCENT_LOW = 0.24
PERCENT_MEDIUM = 0.3
PERCENT_HIGH = 0.37
PERCENT_VERY_HIGH = 0.45
PERCENT_MAXIMUM = 0.47

if incomes <= THRESHOLD_VERY_LOW:
    taxes = incomes * PERCENT_MINIMUM
else:
    taxes = THRESHOLD_VERY_LOW * PERCENT_MINIMUM
    if incomes <= THRESHOLD_LOW:
        taxes += (incomes - THRESHOLD_VERY_LOW) * PERCENT_LOW
    else:
        taxes += (THRESHOLD_LOW - THRESHOLD_VERY_LOW) * PERCENT_LOW
        if incomes <= THRESHOLD_MEDIUM:
            taxes += (incomes - THRESHOLD_LOW) * PERCENT_MEDIUM
        else:
            taxes += (THRESHOLD_MEDIUM - THRESHOLD_LOW) * PERCENT_MEDIUM
            if incomes <= THRESHOLD_HIGH:
                taxes += (incomes - THRESHOLD_MEDIUM) * PERCENT_HIGH
            else:
                taxes += (THRESHOLD_HIGH - THRESHOLD_MEDIUM) * PERCENT_HIGH
                if incomes <= THRESHOLD_VERY_HIGH:
                    taxes += (incomes - THRESHOLD_HIGH) * PERCENT_VERY_HIGH
                else:
                    taxes += (THRESHOLD_VERY_HIGH - THRESHOLD_HIGH) * PERCENT_VERY_HIGH
                    taxes += (incomes - THRESHOLD_VERY_HIGH) * PERCENT_MAXIMUM
net_incomes = incomes - taxes
print('Your total amount of taxes is: ', taxes)
print('Your net incomes are: ', net_incomes)
