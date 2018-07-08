import unittest
import zg2uni

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        zawgyi = u'''လူတိုင္းသည္ တူညီ လြတ္လပ္ေသာ ဂုဏ္သိကၡာျဖင့္ လည္းေကာင္း၊ တူညီလြတ္လပ္ေသာ အခြင့္အေရးမ်ားျဖင့္ လည္းေကာင္း၊ ေမြးဖြားလာသူမ်ား ျဖစ္သည္။'''
        unicode = u'''လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။'''
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article One")



    def test_article_two(self):
        zawgyi = u'''ကခဂငစဆဇည ဋဌဍ ဏတထဒဓနပဖဗဘမ ယရလ၀သဟ ဠအ'''
        unicode = u'''ကခဂငစဆဇည ဋဌဍ ဏတထဒဓနပဖဗဘမ ယရလ၀သဟ ဠအ'''
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article Two")

    def test_article_three(self):
        zawgyi = u'''သီဟိုဠ္မွ ဉာဏ္ႀကီးရွင္သည္ အာယုဝၯနေဆးၫႊန္းစာကို ဇလြန္ေဈးေဘးဗာဒံပင္ထက္ အဓိ႒ာန္လ်က္ ဂဃနဏဖတ္ခဲ့သည္။'''
        unicode = u'''သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက် အဓိဋ္ဌာန်လျက် ဂဃနဏဖတ်ခဲ့သည်။'''
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article three")


if __name__ == "__main__":
    unittest.main()
