from address import Address
from mailing import Mailing


to_addr = Address("62701", "Воронеж", "Ватутина", "42", "5")
from_addr = Address("62960", "Москва", "Ленина", "456", "123")
    
mailing = Mailing(to_address=to_addr, from_address=from_addr, cost=5.99, track="TRACK0046")
    
print(mailing)