if code == RAW_VALUE:
  try:
   anu = value[0]
   itu = value[1]
  except IndexError:
   anu = "0"
   itu = "0"