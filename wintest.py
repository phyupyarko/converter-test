import unittest
import win2uni


class TestWIN2UNI(unittest.TestCase):
    def test_myanmar_consonants(self):
        win = u'''uc*CipqZ#X!Pwx'"yzAbr,vo[Vt'''
        unicode = u'''ကခဂဃငစဆဇဋဌဍဏတထဒဓပဖဗဘမယလသဟဠအ'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting Consonants")

    def test_article_one(self):
        win = u'''aps;'''
        unicode = u'''ဈေး'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article One")

    def test_myanmar_pangram(self):
        win = u'''oD[dkVfrS ÓPfBuD;½§ifonf tm,k0¹eaq;ñTef;pmudk ZvGefaps;ab;Am'Hyifxuf'''
        unicode = u'''သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက်'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting Article Pangram")



if __name__ == "__main__":
    unittest.main()
