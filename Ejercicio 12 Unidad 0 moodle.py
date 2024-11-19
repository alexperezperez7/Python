##Algorithm calculate_total_cost_product
##Inputs: base_price: real
##Output: real
##Constants: VAT (IVA) = 0.21
##Variables: total_cost: real
##Start
##	taxes ← base_price * VAT
##	total_cost ← base_price + taxes
##	return total_cost
##End

base_price = 50
VAT = 0.21

taxes = base_price * VAT
total_cost = base_price + taxes
print('The total cost is', total_cost)
