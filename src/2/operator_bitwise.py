d = input("Masukan nilai a: ")
i = input("Masukan nilai b: ")

# Operasi AND
a = d & i
print "d & i = %s" % a

# Operasi OR
a = d | i
print "d | i = %s" % a

# Operasi XOR
a = d ^ i
print "d ^ i = %s" % a

# Operasi Not
a = ~d
print "~d = %s" % a

# Operasi shift left (tukar posisi biner)
a = d << i
print "d << i = %s" % a

# Operasi shift right (tukar posisi biner)
a = d >> i
print "d >> i = %s" % a