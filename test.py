import unittest
from roman import convert

class RomanNumeralConverterTest(unittest.TestCase):

  def test_convert_one(self):
    self.assertEqual(convert(1), "I")

  def test_convert_two(self):
    self.assertEqual(convert(2), "II")

  def test_convert_three(self):
    self.assertEqual(convert(3), "III")

  def test_convert_four(self):
    self.assertEqual(convert(4), "IV")

  def test_convert_five(self):
    self.assertEqual(convert(5), "V")

  def test_convert_six(self):
    self.assertEqual(convert(6), "VI")

  def test_convert_seven(self):
    self.assertEqual(convert(7), "VII")

  def test_convert_eight(self):
    self.assertEqual(convert(8), "VIII")

  def test_convert_nine(self):
    self.assertEqual(convert(9), "IX")

  def test_convert_ten(self):
    self.assertEqual(convert(10), "X")

  def test_convert_eleven(self):
    self.assertEqual(convert(11), "XI")

  def test_convert_fourteen(self):
    self.assertEqual(convert(14), "XIV")

  def test_convert_fifteen(self):
    self.assertEqual(convert(15), "XV")

  def test_convert_sixteen(self):
    self.assertEqual(convert(16), "XVI")

  def test_convert_sixteen(self):
    self.assertEqual(convert(19), "XIX")

  def test_convert_twenty(self):
    self.assertEqual(convert(20), "XX")

  def test_convert_twenty_four(self):
    self.assertEqual(convert(24), "XXIV")

  def test_convert_thirty(self):
    self.assertEqual(convert(30), "XXX")

  def test_convert_thirty_nine(self):
    self.assertEqual(convert(39), "XXXIX")

  def test_convert_forty(self):
    self.assertEqual(convert(40), "XL")

  def test_convert_forty_six(self):
    self.assertEqual(convert(46), "XLVI")

  def test_convert_fifty(self):
    self.assertEqual(convert(50), "L")
  
  def test_convert_fifty_eight(self):
    self.assertEqual(convert(58), "LVIII")

  def test_convert_sixty(self):
    self.assertEqual(convert(60), "LX")

  def test_convert_seventy(self):
    self.assertEqual(convert(70), "LXX")

  def test_convert_eighty(self):
    self.assertEqual(convert(80), "LXXX")

  def test_convert_ninety(self):
    self.assertEqual(convert(90), "XC")

  def test_convert_one_hundred(self):
    self.assertEqual(convert(100), "C")

  def test_convert_one_hundred_fifty(self):
    self.assertEqual(convert(150), "CL")

  def test_convert_two_hundred(self):
    self.assertEqual(convert(200), "CC")

  def test_convert_three_hundred(self):
    self.assertEqual(convert(300), "CCC")

  def test_convert_four_hundred(self):
    self.assertEqual(convert(400), "CD")

  def test_convert_four_hundred_ninety_nine(self):
    self.assertEqual(convert(499), "CDXCIX")

  def test_convert_five_hundred(self):
    self.assertEqual(convert(500), "D")

  def test_convert_five_hundred_forty_nine(self):
    self.assertEqual(convert(549), "DXLIX")

  def test_convert_six_hundred_twenty_two(self):
    self.assertEqual(convert(622), "DCXXII")

  def test_convert_seven_hundred_eighty_eight(self):
    self.assertEqual(convert(788), "DCCLXXXVIII")

  def test_convert_eight_hundred_five(self):
    self.assertEqual(convert(805), "DCCCV")

  def test_convert_nine_hundred_sixty_three(self):  #failing test
    self.assertEqual(convert(963), "CMLXIII")

  def test_convert_one_thousand(self):
    self.assertEqual(convert(1000), "M")

  def test_convert_two_thousand(self):
    self.assertEqual(convert(2000), "MM")

  def test_convert_three_thousand(self):
    self.assertEqual(convert(3000), "MMM")

  def test_convert_three_thousand_nine_hundred_ninety_nine(self):
    self.assertEqual(convert(3999), "MMMCMXCIX")

if __name__ == '__main__':
  unittest.main()