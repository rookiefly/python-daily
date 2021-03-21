from phone import Phone
import sys
p  = Phone()
while True:
    phone_num = input('please enter your phone number: ')
    if phone_num == 'exit':
        sys.exit(1)
    print(p.find(phone_num))