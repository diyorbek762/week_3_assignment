
#bath_price = 15
#trim_price = 25
#full_price = 40
    
#while True
total=0
current_total=0
print('*'*40)
print(' === Pet Grooming Service Calculator ===')
print('*'*40)
print('\nEnter service package: bath, trim, or full')
print('Type "done" when finished selecting services\n')
print('*'*40)

while True:
   service_order = input('Enter service package(bath/trim/full): ')
   if service_order=='done':
      print(f'Total Price: ${total:.2f}')
      break
   elif service_order=='bath':
      price=15
   elif service_order=='trim':
      price=25
   elif service_order=='full':
      price=40
   else:
      print('Please enter only the available service!')
      continue
   total +=price
   current_total+=price
   print(f'Price: ${price:.02f}')
   print(f'Current Total: ${total:.2f}\n')

print('==Service Summary==')
print(f"Total Price: ${total:.2f}")
if total >= 75.00:
   total_after_discount = total - 12.00
   print(f'Price After Discounts: {total_after_discount:.2f}')









