##Algorithm calculate_cost_of_a_bus_per_person
##Inputs: number_people: integer
##Output: real
##Constants: MAXIMUM_COST = 4000
##       LOW_COST = 65
##       MEDIUM_COST = 70
##       EXPENSIVE_COST = 95
##       MANY_PEOPLE = 100
##       MEDIUM_PEOPLE = 50
##       FEW_PEOPLE = 30
##Variables:
##Start
##	if number_people < FEW_PEOPLE do:
##		return MINIMUM_COST
##	if number_people < MEDIUM_PEOPLE do:
##		return number_people * EXPENSIVE_COST
##	if number_people < MANY_PEOPLE do:
##		return number_people * MEDIUM_COST
##	return number_people * LOW_COST
##End


MAXIMUM_COST = 4000
LOW_COST = 65
MEDIUM_COST = 70
EXPENSIVE_COST = 95
MANY_PEOPLE = 100
MEDIUM_PEOPLE = 50
FEW_PEOPLE = 30

number_people = input('Enter the number of people:')
number_people = int(number_people)

if number_people <= FEW_PEOPLE:
    print('The price is:', MAXIMUM_COST)
if number_people > FEW_PEOPLE and number_people < MEDIUM_PEOPLE:
    print('The price is:', number_people*EXPENSIVE_COST)
if number_people >= MEDIUM_PEOPLE and number_people < MANY_PEOPLE:
    print('The price is:', number_people*MEDIUM_COST)
if number_people >= MANY_PEOPLE:
    print('The price is:', number_people*LOW_COST)
          
