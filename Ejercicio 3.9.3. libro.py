#Algorithm max_product
#Inputs: n1: int
#        n2: int
#        n3: int
#        n4: int
#Output: integer
#Constants:
#Variables: result: int
#           aux: int
#Start
#   result <-- n1 * n2
#   aux <-- n1 * n3
#   if aux > result do:
#       result <-- aux
#   aux <-- n1 * n4
#   if aux > result do:
#       result <-- aux
#   aux <-- n2 * n3
#   if aux > result do:
#        result <-- aux
#   aux <-- n2 * n4
#   if aux > result do:
#        result <-- aux
#   aux <-- n3 * n4
#   if aux > result do:
#        result <-- aux
#   return result
#End

def max_product(n1, n2, n3, n4):
    result1 = n1 * n2
    result2 = n1 * n3
    result3 = n1 * n4
    result4 = n2 * n3
    result5 = n2 * n4
    result6 = n3 * n4
    return max(result1, result2, result3, result4, result5, result6)
 

