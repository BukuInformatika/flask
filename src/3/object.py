p = Product("Ultora Milek")
p.set_price(5500)

print "%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price)
# print p.__vendor_message

p.get_vendor_message()

p1 = Product("Indomilek")
p1.set_price(5000)

print "%s dengan ukuran %s %s harganya Rp. %d" % (p.name, p.size, p.unit, p.price)