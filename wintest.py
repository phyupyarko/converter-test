import unittest
import win2uni


class TestWIN2UNI(unittest.TestCase):
    def test_myanmar_consonants(self):
        win = u'''uc*CipqZ#X!Pwx'"yzAbr,vo[Vt'''
        unicode = u'''ကခဂဃငစဆဇဋဌဍဏတထဒဓပဖဗဘမယလသဟဠအ'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting Consonants")

    def test_article_one(self):
        win = u'''tydk'f 1vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? 
        arG;zGm;vmolrsm; jzpfonf/ xdkolwdkhü ydkif;jcm; a0zefwwfaom ÚmPfeSihf usihf0wf odwwfaom pdwfwdkh&Sdjuí xdkolwdkhonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        unicode = u'''အပိုဒ် ၁လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ 
        မွေးဖွားလာသူများ ဖြစ်သည်။ ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article One")

    def test_article_three(self):
        win = u'''tydk'f 3
        vlwdkif;ü touf&Sif&ef vGwfvyfrIcGihfeSihf vkHjckHpdwfcscGihf &Sdonf/'''
        unicode = u'''အပိုဒ် ၃
        လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Three")

    def test_article_Two(self):
        win = u'''OD;'''
        unicode = u'''ဦး'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Two")

    def test_article_Four(self):
        win = u'''tydk'f 4
        rnfoludkrsS aus;usGeftjzpf? odkhwnf;r[kwf taptyg;tjzpf? edkifxufpD;eif; apcdkif;jcif; rjyk&? vludk aus;usGefozG,f t"r® apcdkif;jcif;? ta&mif;t0,f jykjcif;eSihf xdkoabm oufa&mufaom vkyfief;[lorsSudk ydwfyif wm;jrpf &rnf/
'''
        unicode = u'''အပိုဒ် ၄
        မည်သူကိုမျှ ကျေးကျွန်အဖြစ်၊ သို့တည်းမဟုတ် အစေအပါးအဖြစ်၊ နိုင်ထက်စီးနင်း စေခိုင်းခြင်း မပြုရ၊ လူကို ကျေးကျွန်သဖွယ် အဓမ္မ စေခိုင်းခြင်း၊ အရောင်းအဝယ် ပြုခြင်းနှင့် ထိုသဘော သက်ရောက်သော လုပ်ငန်းဟူသမျှကို ပိတ်ပင် တားမြစ် ရမည်။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Four")

    def test_article_Five(self):
        win = u'''tydk'f 5
        rnfoludkrsS nSÚf;yef; eSdyfpufjcif;? odkhwnf;r[kwf &ufpufjurf;jukwfpGm vlrqefpGm *kPfi,fapaom qufqHrI rjyk&? odkhwnf;r[kwf tjypf'Pf ay;jcif;rjyk&/
'''
        unicode = u'''အပိုဒ် ၅
        မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊ သို့တည်းမဟုတ် ရက်စက်ကြမ်းကြုတ်စွာ လူမဆန်စွာ ဂုဏ်ငယ်စေသော ဆက်ဆံမှု မပြုရ၊ သို့တည်းမဟုတ် အပြစ်ဒဏ် ပေးခြင်းမပြုရ။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Five")

    def test_article_Six(self):
        win = u'''tydk'f 6
        vlwdkif;wGif Oya't&mü vlyk*¾dkvfwpfOD; '''
        unicode = u'''အပိုဒ် ၆
        လူတိုင်းတွင် ဥပဒေအရာ၌ လူပုဂ္ဂိုလ်တစ်ဦး '''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Six")

    def test_article_Seaven(self):
        win = u'''tydk'f 7
        vltm;vkH;wdkhonf Oya't&mü wlnDjuonhftjyif? Oya'\ tumtuG,fudk jcm;em;jcif; rcH&apbJ wlnDpGm cHpm;ydkifcGihf&Sdonf/ 
        þajunm pmwrf;yg oabmw&m;rsm;udk zDqefí cGJjcm;jcif;rS vnf;aumif;? xdkodkhcGJjcm;jcif;udk vIHhaqmfjcif;rS vnf;aumif;? uif;vGwf ap&ef tumtuG,fudk wlnDpGm cHpm;ydkifcGihf &Sdonf/
'''
        unicode = u'''အပိုဒ် ၇
        လူအားလုံးတို့သည် ဥပဒေအရာ၌ တူညီကြသည့်အပြင်၊ ဥပဒေ၏ အကာအကွယ်ကို ခြားနားခြင်း မခံရစေဘဲ တူညီစွာ ခံစားပိုင်ခွင့်ရှိသည်။ 
        ဤကြေညာ စာတမ်းပါ သဘောတရားများကို ဖီဆန်၍ ခွဲခြားခြင်းမှ လည်းကောင်း၊ ထိုသို့ခွဲခြားခြင်းကို လှုံ့ဆော်ခြင်းမှ လည်းကောင်း၊ ကင်းလွတ် စေရန် အကာအကွယ်ကို တူညီစွာ ခံစားပိုင်ခွင့် ရှိသည်။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Seaven")

    def test_article_Eight(self):
        win = u'''tydk'f 8
        zGJhpnf;ykH tajccHOya'u aomfvnf;aumif; tjcm; Oya'u aomfvnf;aumif; vlwdkif;twGuf 
        ay;xm;onhf tajccH tcGihfta&; rsm;onf csdk;azmuf zsufqD;jcif;cHcJh&vsSif xdkodkh csdk;azmufzsufqD; aom jykvkyfrIajumihf 
        jzpfay:vmaom epfemcsuf twGuf xdkolonf edkifiHqdkif&m tmPmydkifw&m;&kH;wGif xda&mufpGm oufomcGihf &Sdedkifap&rnf/
'''
        unicode = u'''အပိုဒ် ၈
        ဖွဲ့စည်းပုံ အခြေခံဥပဒေက သော်လည်းကောင်း အခြား ဥပဒေက သော်လည်းကောင်း လူတိုင်းအတွက် 
        ပေးထားသည့် အခြေခံ အခွင့်အရေး များသည် ချိုးဖောက် ဖျက်ဆီးခြင်းခံခဲ့ရလျှင် ထိုသို့ ချိုးဖောက်ဖျက်ဆီး သော ပြုလုပ်မှုကြောင့် 
        ဖြစ်ပေါ်လာသော နစ်နာချက် အတွက် ထိုသူသည် နိုင်ငံဆိုင်ရာ အာဏာပိုင်တရားရုံးတွင် ထိရောက်စွာ သက်သာခွင့် ရှိနိုင်စေရမည်။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Eight")

    def test_article_Nine(self):
        win = u'''tydk'f 9
        rnfolrsS Oya't& r[kwfaom zrf;qD;jcif;udk jzpfap? cskyfaeSmifjcif;udk jzpfap? jynfeSifjcif;udkjzpfap rcHap&/
'''
        unicode = u'''အပိုဒ် ၉
        မည်သူမျှ ဥပဒေအရ မဟုတ်သော ဖမ်းဆီးခြင်းကို ဖြစ်စေ၊ ချုပ်နှောင်ခြင်းကို ဖြစ်စေ၊ ပြည်နှင်ခြင်းကိုဖြစ်စေ မခံစေရ။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Nine")

    def test_article_Ten(self):
        win = u'''tydk'f 10
        tcGihfta&;rsm;eSihf wm0ef 0wÅ&m;rsm;udk tqkH;tjzwfcH&mwGif vnf;aumif;? jypfrIajumihf w&m;pGJqdk pD&if qkH;jzwfcH&mwGif 
        vnf;aumif;? vlwdkif;onf vGwfvyfí bufrvdkufaom w&m;&kH;awmf\ vltrsm; a&SharSmufwGif rsSwpGm jum;emppfaq;jcif;udk wlnDpGm cHpm; ydkifcGihf&Sdonf/
'''
        unicode = u'''အပိုဒ် ၁ဝ
        အခွင့်အရေးများနှင့် တာဝန် ဝတ္တရားများကို အဆုံးအဖြတ်ခံရာတွင် လည်းကောင်း၊ ပြစ်မှုကြောင့် တရားစွဲဆို စီရင် ဆုံးဖြတ်ခံရာတွင် 
        လည်းကောင်း၊ လူတိုင်းသည် လွတ်လပ်၍ ဘက်မလိုက်သော တရားရုံးတော်၏ လူအများ ရှေ့မှောက်တွင် မျှတစွာ ကြားနာစစ်ဆေးခြင်းကို တူညီစွာ ခံစား ပိုင်ခွင့်ရှိသည်။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Ten")

    def test_article_Eleven(self):
        win = u'''tydk'f 11
        vltrsm; a&SharSmufü Oya'twdkif; ppfaq;í jypfrIusl;vGefonf[k xif&Sm; pD&ifjcif;cH&onhf tcsdeftxd jypfrIeSihf 
        w&m;pGJqdkjcif; cH&olwdkif;onf tjypfrJhol[lí ,lq jcif;cHxdkufonhf tcGihfta&;&Sdonf/ xdktrIudk jum;emppfaq;&m0,f 
        pGyfpGJcH&onhf jypfrItwGuf ckcHacsyedkif&ef vdktyfaom tcGihfta&;rsm;udk xdkoltm; ay;jyD; jzpfap&rnf/
        vlwpfOD;wpfa,muftm; edkifiHOya't&jzpfap? tjynfjynfqdkif&m Oya't& jzpfap? jypfrIrajrmufaom vkyf&yf 
        odkhr[kwf ysufuGufrIt& qGJqdkjypfay;jcif; rjyk&/ 
        xdkhtjyif jypfrIusl;vGefpÚftcgu xdkufoihfapedkifaom tjypf'PfxufydkrdkjuD;av;aom tjypf'Pfudk xdkufoihfjcif;r&Sdap&/
'''
        unicode = u'''အပိုဒ် ၁၁
        လူအများ ရှေ့မှောက်၌ ဥပဒေအတိုင်း စစ်ဆေး၍ ပြစ်မှုကျူးလွန်သည်ဟု ထင်ရှား စီရင်ခြင်းခံရသည့် အချိန်အထိ ပြစ်မှုနှင့် 
        တရားစွဲဆိုခြင်း ခံရသူတိုင်းသည် အပြစ်မဲ့သူဟူ၍ ယူဆ ခြင်းခံထိုက်သည့် အခွင့်အရေးရှိသည်။ ထိုအမှုကို ကြားနာစစ်ဆေးရာဝယ် 
        စွပ်စွဲခံရသည့် ပြစ်မှုအတွက် ခုခံချေပနိုင်ရန် လိုအပ်သော အခွင့်အရေးများကို ထိုသူအား ပေးပြီး ဖြစ်စေရမည်။
        လူတစ်ဦးတစ်ယောက်အား နိုင်ငံဥပဒေအရဖြစ်စေ၊ အပြည်ပြည်ဆိုင်ရာ ဥပဒေအရ ဖြစ်စေ၊ ပြစ်မှုမမြောက်သော လုပ်ရပ် 
        သို့မဟုတ် ပျက်ကွက်မှုအရ ဆွဲဆိုပြစ်ပေးခြင်း မပြုရ။ 
        ထို့အပြင် ပြစ်မှုကျူးလွန်စဉ်အခါက ထိုက်သင့်စေနိုင်သော အပြစ်ဒဏ်ထက်ပိုမိုကြီးလေးသော အပြစ်ဒဏ်ကို ထိုက်သင့်ခြင်းမရှိစေရ။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Eleven")

    def test_article_Twelve(self):
        win = u'''tydk'f 12
        rnfolrsS rdrdoabmtwdkif; at;csrf;vGwfvyfpGm aexdkifjcif;udk aomfvnf;aumif;? rdrd\ rdom;pkudk aomfvnf;aumif;? 
        rdrd\ aetdrf todkuft0ef;udk aomfvnf;aumif;? pmay;pm,ludk aomfvnf;aumif;? Oya't& r[kwfaom 0ifa&muf pGufzufjcif; rcHap&/ 
        xdkhjyif rdrd\*kPfodu©m udkvnf; txufyg twdkif; ykwfcwfjcif; rcHap&/ vlwdkif;wGif xdkodkh 0ifa&mufpGufzufjcif;rS aomfvnf;aumif; 
        ykwfcwfjcif;rS aomfvnf;aumif; Oya't& umuG,f ydkifcGihf&Sdonf/
'''
        unicode = u'''အပိုဒ် ၁၂
        မည်သူမျှ မိမိသဘောအတိုင်း အေးချမ်းလွတ်လပ်စွာ နေထိုင်ခြင်းကို သော်လည်းကောင်း၊ မိမိ၏ မိသားစုကို သော်လည်းကောင်း၊ 
        မိမိ၏ နေအိမ် အသိုက်အဝန်းကို သော်လည်းကောင်း၊ စာပေးစာယူကို သော်လည်းကောင်း၊ ဥပဒေအရ မဟုတ်သော ဝင်ရောက် စွက်ဖက်ခြင်း မခံစေရ။ 
        ထို့ပြင် မိမိ၏ဂုဏ်သိက္ခာ ကိုလည်း အထက်ပါ အတိုင်း ပုတ်ခတ်ခြင်း မခံစေရ။ လူတိုင်းတွင် ထိုသို့ ဝင်ရောက်စွက်ဖက်ခြင်းမှ သော်လည်းကောင်း 
        ပုတ်ခတ်ခြင်းမှ သော်လည်းကောင်း ဥပဒေအရ ကာကွယ် ပိုင်ခွင့်ရှိသည်။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Twelve")

    def test_article_Thirteen(self):
        win = u'''tydk'f 13
        vlwdkif;wGif rdrd\edkifiH e,fedrdwf twGif;ü vGwfvyfpGm oGm;vm a&GShajymif; edkifcGihf? aexdkifcGihf&Sdonf/
        vlwdkif;wGif rdrdaexdkif&m wdkif;jynfrS vnf;aumif;? tjcm;wdkif;jynfrSvnf;aumif; xGufcGm oGm;ydkifcGihf&Sdonhftjyif?rdrd\ wdkif;jynfodkh jyefvm ydkifcGihfvnf;&Sdonf/
'''
        unicode = u'''အပိုဒ် ၁၃
        လူတိုင်းတွင် မိမိ၏နိုင်ငံ နယ်နိမိတ် အတွင်း၌ လွတ်လပ်စွာ သွားလာ ရွှေ့ပြောင်း နိုင်ခွင့်၊ နေထိုင်ခွင့်ရှိသည်။
        လူတိုင်းတွင် မိမိနေထိုင်ရာ တိုင်းပြည်မှ လည်းကောင်း၊ အခြားတိုင်းပြည်မှလည်းကောင်း ထွက်ခွာ သွားပိုင်ခွင့်ရှိသည့်အပြင်၊မိမိ၏ တိုင်းပြည်သို့ ပြန်လာ ပိုင်ခွင့်လည်းရှိသည်။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Thirteen")

    def test_article_Fourteen(self):
        win = u'''tydk'f 14
        vlwdkif;onf nSÚf;yef; eSdyfpuf cHae&jcif;rS vGwfuif;&ef tjcm;wdkif;jynf rsm;ü at;csrf;pGm cdkvIHaeedkifcGihf&Sdonf/
        edkifiHa&;eSihf rywfoufonhf jypfrIrsm;rS aomfvnf;aumif;? ukvor*¾\ &nf&GufcsufeSihf oabmw&m; rIrsm;udk 
        zDqefaom trIrsm;rS aomfvn;faumif;? trSef ay:ayguf vmaom jypfrIajumihf w&m;pGJqdkjcif; cH&onhf trItcif;rsm;wGif txufyg tcGihfta&;udk tokH;rjykedkifap&/
'''
        unicode = u'''အပိုဒ် ၁၄
        လူတိုင်းသည် ညှဉ်းပန်း နှိပ်စက် ခံနေရခြင်းမှ လွတ်ကင်းရန် အခြားတိုင်းပြည် များ၌ အေးချမ်းစွာ ခိုလှုံနေနိုင်ခွင့်ရှိသည်။
        နိုင်ငံရေးနှင့် မပတ်သက်သည့် ပြစ်မှုများမှ သော်လည်းကောင်း၊ ကုလသမဂ္ဂ၏ ရည်ရွက်ချက်နှင့် သဘောတရား မှုများကို 
        ဖီဆန်သော အမှုများမှ သော်လညး်ကောင်း၊ အမှန် ပေါ်ပေါက် လာသော ပြစ်မှုကြောင့် တရားစွဲဆိုခြင်း ခံရသည့် အမှုအခင်းများတွင် အထက်ပါ အခွင့်အရေးကို အသုံးမပြုနိုင်စေရ။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Fourteen")

    def test_article_Fifteen(self):
        win = u'''tydk'f 15
        vlwdkif;onf? edkifiH wpfedkifiH\ edkifiHom;tjzpf cH,lcGihf&Sdonf/
        Oya't& r[kwfvsSif rnfolrsS rdrd\ edkifiHom;tjzpfudk pGehfvGSwfjcif; rcHap&? edkifiHom;tjzpf ajymif;vJedkifaomtcGihfta&;udk vnf; jiif;y,fjcif; rcHap&/
'''
        unicode = u'''အပိုဒ် ၁၅
        လူတိုင်းသည်၊ နိုင်ငံ တစ်နိုင်ငံ၏ နိုင်ငံသားအဖြစ် ခံယူခွင့်ရှိသည်။
        ဥပဒေအရ မဟုတ်လျှင် မည်သူမျှ မိမိ၏ နိုင်ငံသားအဖြစ်ကို စွန့်လွှတ်ခြင်း မခံစေရ၊ နိုင်ငံသားအဖြစ် ပြောင်းလဲနိုင်သောအခွင့်အရေးကို လည်း ငြင်းပယ်ခြင်း မခံစေရ။
'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting article Fifteen")

    def test_article_sixteen(self):
        win = u'''tydk'f 16
        t&G,fa&muf jyD;aom a,musmf; eSihf rdef;rwdkhwGif vlrsdk;udk aomfvnf;aumif;? edkifiHom; tjzpfudk aomfvnf;aumif; udk;uG,fonhf bmomudk aomfvnf;aumif;? 
        tajumif;jykí cskyfcs,f uehfowfjcif; r&SdbJ? 
        xdrf;jrm;edkifcGihf eSihf rdom;pkxlaxmifedkifcGihf&Sdonf/ tqdkyg a,musmf;eSihf rdef;r wdkhonf vifr,m;tjzpf aygif;oif;aepÚf tcsdef twGif;ü aomfvnf;aumif;? 
        tdrfaxmifudk zsufodrf;í uGm&Sif;juonhf tcgüvnf;aumif;? vufxyf aygif;oif; tdrfaxmifjykjcif;eSihf pyfvsÚf;aom wlnDonhf tcGihfta&;rsm;udk &&Sdxdkufonf/
        owdkhom; eSihf owdkhorD; eSpfOD;eSpfbuf\ vGwfvyfaom oabmqe´&SdrSomvsSif xdrf;jrm;jcif;udk jyk&rnf/
        rdom;pk wpfckonf vlhtzGJhtpnf;\ obm0usaom tajccHtzGJhwpf&yfjzpfonf? xdkrdom;pkonf vlh tzGJhtpnf;eSihf tpdk;&wdkh\ umuG,fapmihfa&Smufjcif;udk cH,lcGihf&Sdonf/'''
        unicode = u'''အပိုဒ် ၁၆
        အရွယ်ရောက် ပြီးသော ယောကျာ်း နှင့် မိန်းမတို့တွင် လူမျိုးကို သော်လည်းကောင်း၊ နိုင်ငံသား အဖြစ်ကို သော်လည်းကောင်း ကိုးကွယ်သည့် ဘာသာကို သော်လည်းကောင်း၊ 
        အကြောင်းပြု၍ ချုပ်ချယ် ကန့်သတ်ခြင်း မရှိဘဲ၊ 
        ထိမ်းမြားနိုင်ခွင့် နှင့် မိသားစုထူထောင်နိုင်ခွင့်ရှိသည်။ အဆိုပါ ယောကျာ်းနှင့် မိန်းမ တို့သည် လင်မယားအဖြစ် ပေါင်းသင်းနေစဉ် အချိန် အတွင်း၌ သော်လည်းကောင်း၊ 
        အိမ်ထောင်ကို ဖျက်သိမ်း၍ ကွာရှင်းကြသည့် အခါ၌လည်းကောင်း၊ လက်ထပ် ပေါင်းသင်း အိမ်ထောင်ပြုခြင်းနှင့် စပ်လျဉ်းသော တူညီသည့် အခွင့်အရေးများကို ရရှိထိုက်သည်။
        သတို့သား နှင့် သတို့သမီး နှစ်ဦးနှစ်ဘက်၏ လွတ်လပ်သော သဘောဆန္ဒရှိမှသာလျှင် ထိမ်းမြားခြင်းကို ပြုရမည်။
        မိသားစု တစ်ခုသည် လူ့အဖွဲ့အစည်း၏ သဘာဝကျသော အခြေခံအဖွဲ့တစ်ရပ်ဖြစ်သည်၊ ထိုမိသားစုသည် လူ့ အဖွဲ့အစည်းနှင့် အစိုးရတို့၏ ကာကွယ်စောင့်ရှောက်ခြင်းကို ခံယူခွင့်ရှိသည်။'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed to Convert Article Sixteen")

    def test_myanmar_pangram(self):
        win = u'''oD[dkVfrS ÓPfBuD;½§ifonf tm,k0¹eaq;ñTef;pmudk ZvGefaps;ab;Am'Hyifxuf'''
        unicode = u'''သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက်'''
        result = win2uni.convert(win)
        self.assertEqual(unicode, result, "Failed converting Article Pangram")


if __name__ == "__main__":
    unittest.main()
