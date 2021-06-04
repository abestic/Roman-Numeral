def convert(number):
  roman_numeral = ""
  arabic_remainder = number

  while arabic_remainder >=  1000:
    roman_numeral += "M"
    arabic_remainder -= 1000
  
  if arabic_remainder >= 900:
    roman_numeral += "CM"
    arabic_remainder -= 900
  
  if arabic_remainder >= 500:
    roman_numeral += "D"
    arabic_remainder -= 500
  
  if arabic_remainder >= 400:
    roman_numeral += "CD"
    arabic_remainder -= 400

  while arabic_remainder >= 100:
    roman_numeral += "C"
    arabic_remainder -= 100
  
  if arabic_remainder >= 90:
    roman_numeral += "XC"
    arabic_remainder -= 90
  
  if arabic_remainder >= 50:
    roman_numeral += "L"
    arabic_remainder -= 50

  if arabic_remainder >= 40:
    roman_numeral += "XL"
    arabic_remainder -= 40
  
  while arabic_remainder >= 10:
    roman_numeral += "X"
    arabic_remainder -= 10

  if arabic_remainder == 9:
    roman_numeral += "IX"
    arabic_remainder -= 9

  if arabic_remainder >= 5:
    roman_numeral += "V"
    arabic_remainder -= 5

  if arabic_remainder == 4:
    roman_numeral += "IV"
    arabic_remainder -= 4

  while arabic_remainder > 0:
    roman_numeral += "I"
    arabic_remainder -= 1

  return roman_numeral


try:
  number = int(input("\nEnter a whole number between 1 and 3999: "))
  if number < 1 or number > 3999:
    raise Exception
except ValueError:
  print("Error: Not a whole number between 1 and 3999!!!\n")
except Exception:
  print("Error: Not a whole number between 1 and 3999!!!\n")
else:
  print("Roman Numeral: ", convert(number), "\n")

