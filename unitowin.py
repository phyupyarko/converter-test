# -*- coding: utf-8 -*-
import re
def convert(input):
    output = input
    output = re.sub(u'\u1039\u1010\u103d', u'\u00c9', output)#twa
    output = re.sub(u'\u100b\u1039\u100b', u'\u00a5', output)#ta-ta-sint
    output = re.sub(u'\u100d\u1039\u100d', u'\u00d7', output)  # yin-yin-sint
    output = re.sub(u'\u100b\u1039\u100c', u'\u007c', output)  # ta-htasint
    output = re.sub(u'\u100f\u1039\u100d', u'\u0040', output)  # na-yin sint
    ############yit

    output = re.sub(u'([\u1000-\u1021])((?:[\u103b-\u103e])?)(\u1031)', u'\\3\\1\\2', output)  # pysh-byee-tawai
    output = re.sub(u'([\u1000\u1003\u1006\u100f\u1011\u1018\u101a\u101e\u101f\u1021\u1010])\u103c([\u102d\u102e\u1036])', u'\u0042\\1\\2', output)  # yitgyi-ttt-ltsk
    output = re.sub(u'([\u1000\u1003\u1006\u100f\u1011\u1018\u101a\u101e\u101f\u1021\u1010])\u103c\u103d', u'\u003c\\1', output)  # yitgyi-swae
    output = re.sub(u'([\u1000\u1003\u1006\u100f\u1011\u1018\u101a\u101e\u101f\u1021\u1010])\u103c', u'\u004d\\1',output)  # yitgyi

    output = re.sub(u'([\u1001\u1002\u1004\u1005\u1007\u1012\u1013\u1015\u1016\u1017\u1019])\u103c([\u102d\u102e\u1036])',u'\u004e\\1\\2', output)  # yitlay-ttt-ltsk
    output = re.sub(u'([\u1001\u1002\u1004\u1005\u1007\u1012\u1013\u1015\u1016\u1017\u1019])\u103c\u103d', u'\u003e\\1',output)  # yitlay-swae
    output = re.sub(u'([\u1000-\u1021])(\u103c)', u'\\2\\1', output)  # yit-byee
    output = re.sub(u'\u100d\u1039\u100e', u'\u00b9', output)
    output = re.sub(u'\u103e\u102f', u'\u0049', output)#hote-tachaung
    output = re.sub(u'\u103e\u1030', u'\u00aa', output)  # hote-nachaung


    output = re.sub(u'\u1009\u102c', u'\u00d3', output)  # nyalay-yaecha
    output = output.replace(u'\u104f', u'\u005c')

    output = output.replace(u'\u1039\u1000', u'\u00fa')#ka sint
    output = output.replace(u'\u1039\u1001', u'\u00a9')  # kha sint
    output = output.replace(u'\u1039\u1002', u'\u00be')  # ga sint
    output = output.replace(u'\u1039\u1003', u'\u00a2')  # ga-gyi sint
    output = output.replace(u'\u1039\u1005', u'\u00f6')  # sa sint
    output = output.replace(u'\u1039\u1006', u'\u00e4')  # sal sint
    output = output.replace(u'\u1039\u1007', u'\u00c6')  # za sint
    output = output.replace(u'\u1039\u1008', u'\u00d1')  # zamyin sint
    output = output.replace(u'\u1039\u100b', u'\u00b3')  # tatalin sint
    output = output.replace(u'\u1039\u100c', u'\u00b2')  # htawonbae sint
    output = output.replace(u'\u1039\u100f', u'\u00d6')  # na-gyi sint
    output = output.replace(u'\u1039\u1010', u'\u00c5')  # ta sint
    output = output.replace(u'\u1039\u1011', u'\u00a6')  # hta sint
    output = output.replace(u'\u1039\u1012', u'\u00b4')  # da sint
    output = output.replace(u'\u1039\u1013', u'\u00a8')  # daout sint
    output = output.replace(u'\u1039\u1014', u'\u00e9')  # na sint
    output = output.replace(u'\u1039\u1015', u'\u00dc')  # pa sint
    output = output.replace(u'\u1039\u1016', u'\u00e6')  # pha sint
    output = output.replace(u'\u1039\u1017', u'\u00c1')  # va sint
    output = output.replace(u'\u1039\u1018', u'\u00c7')  # ba sint
    output = output.replace(u'\u1039\u1019', u'\u00ae')  # ma sint
    output = output.replace(u'\u103e\u103b', u'\u103b\u103e')  # pint-htoe
    output = output.replace(u'\u103d\u103b', u'\u103b\u103d')  # pint-swae
    output = output.replace(u'\u103e\u103d', u'\u103d\u103e')  # swae-htoe


    output = re.sub(u'\u103e\u102f', u'\u0049', output)  # hahtoe-tachaung
    output = re.sub(u'\u102b\u103a', u'\u003a', output)  # yaecha-shaehtoe
    output = re.sub(u'\u103b\u103e', u'\u0051', output)  # pint-htoe
    output = re.sub(u'\u103d\u103b', u'\u0052', output)  # pint-swae
    output = re.sub(u'\u103d\u103e', u'\u0054', output)  # swae-htoe
    output = re.sub(u'\u1000\u103b\u1015\u103a', u'\u0024', output)  # kyat

    ####byee
    output = re.sub(u'\u1000', u'\u0075', output)#ka
    output = re.sub(u'\u1001', u'\u0063', output)  # kha
    output = re.sub(u'\u1002', u'\u002A', output)  # ga
    output = re.sub(u'\u1003', u'\u0043', output)  # ga-gyi
    output = re.sub(u'\u1004', u'\u0069', output)  # nga
    output = re.sub(u'\u1005', u'\u0070', output)  # sa-lone
    output = re.sub(u'\u1006', u'\u0071', output)  # sa-lane
    output = re.sub(u'\u1007', u'\u005A', output)  # za
    output = re.sub(u'\u1009', u'\u00da', output)  # nyalay
    output = re.sub(u'\u100A', u'\u006E', output)  # nya
    #output = re.sub(u'\u100A', u'\u00f1', output)  # nya
    output = re.sub(u'\u100B', u'\u0023', output)  # talin
    output = re.sub(u'\u100c', u'\u0058', output)  # hta-won-bae
    output = re.sub(u'\u100d', u'\u0021', output)  # da-yin-kout
    output = re.sub(u'\u100e', u'\u00a1', output)  # da-yin-mote
    output = re.sub(u'\u100f', u'\u0050', output)  # na-gyi
    output = re.sub(u'\u1010', u'\u0077', output)  # ta
    output = re.sub(u'\u1011', u'\u0078', output)  # hta
    output = re.sub(u'\u1012', u'\u0027', output)  # da
    output = re.sub(u'\u1013', u'\u0022', output)  # da-out-cha
    #output = re.sub(u'\u1014', u'\u0045', output)  # na
    output = re.sub(u'\u1014', u'\u0065', output)  # na
    output = re.sub(u'\u1015', u'\u0079', output)  # pa
    output = re.sub(u'\u1016', u'\u007A', output)  # pha
    output = re.sub(u'\u1017', u'\u0041', output)  # va
    output = re.sub(u'\u1018', u'\u0062', output)  # ba
    output = re.sub(u'\u1019', u'\u0072', output)  # ma
    output = re.sub(u'\u101A', u'\u002c', output)  # ya-palat
    output = re.sub(u'\u101B', u'\u0026', output)  # ya
    #output = re.sub(u'\u101B', u'\u00bd', output)  # ya
    output = re.sub(u'\u101c', u'\u0076', output)  # la
    output = re.sub(u'\u101d', u'\u0030', output)  # wa
    output = re.sub(u'\u101e', u'\u006f', output)  # tha
    output = re.sub(u'\u101f', u'\u005b', output)  # ha
    output = re.sub(u'\u1020', u'\u0056', output)  # la-gyi
    output = re.sub(u'\u1021', u'\u0074', output)  # art

    ############number
    output = re.sub(u'\u1040', u'\u0030', output)  # 0
    output = re.sub(u'\u1041', u'\u0031', output)  # 1
    output = re.sub(u'\u1042', u'\u0032', output)  # 2
    output = re.sub(u'\u1043', u'\u0033', output)  # 3
    output = re.sub(u'\u1044', u'\u0034', output)  # 4
    output = re.sub(u'\u1045', u'\u0035', output)  # 5
    output = re.sub(u'\u1046', u'\u0036', output)  # 6
    output = re.sub(u'\u1047', u'\u0037', output)  # 7
    output = re.sub(u'\u1048', u'\u0038', output)  # 8
    output = re.sub(u'\u1049', u'\u0039', output)  # 9
    output = re.sub(u'\u104A', u'\u003f', output)  # pote-lay
    output = re.sub(u'\u104B', u'\u002f', output)  # pote-gyi
    #############
    output = re.sub(u'\u102b', u'\u0067', output)  #mout-cha
    output = re.sub(u'\u102c', u'\u006d', output)  #yae-cha
    output = re.sub(u'\u102d', u'\u0064', output)  #lone-tin
    output = re.sub(u'\u102e', u'\u0044', output)  #san-kat
    #output = re.sub(u'\u102f', u'\u004B', output)  #ta-chaung
    output = re.sub(u'\u102f', u'\u006B', output)  #ta-chaung
    #output = re.sub(u'\u1030', u'\u004c', output)  #na-chaung
    output = re.sub(u'\u1030', u'\u006c', output)  #na-chaung
    output = re.sub(u'\u1031', u'\u0061', output)  #tawai
    output = re.sub(u'\u1032', u'\u004a', output)  #naut-pyit
    output = re.sub(u'\u1036', u'\u0048', output)   #ttt
    #output = re.sub(u'\u1037', u'\u0055', output)  #out-myit
    #output = re.sub(u'\u1037', u'\u0059', output)  #out-myit
    output = re.sub(u'\u1037', u'\u0068', output)  #out-myit
    output = re.sub(u'\u1038', u'\u003b', output)  #witsapout
    output = re.sub(u'\u103A', u'\u0066', output)  #athat
    output = re.sub(u'\u103b', u'\u0073', output)  #pint
    output = re.sub(u'\u103c', u'\u006a', output)  # yit
    output = re.sub(u'\u103d', u'\u0047', output)  # swae
    output = re.sub(u'\u103e', u'\u0053', output)  # htoe

    output = re.sub(u'\u104e', u'\u00a4', output)  # lae-gaung
    output = re.sub(u'\u104d', u'\u00ed', output)  # ywae
    output = re.sub(u'\u104c', u'\u00fc', output)  # nite
    output = re.sub(u'\u1023', u'\u00a3', output)  # eie
    output = re.sub(u'\u1024', u'\u00fe', output)  # eii
    output = re.sub(u'\u1026', u'\u004f\u0044', output)  # uuu
    output = re.sub(u'\u1025', u'\u004f', output)  # uu
    output = re.sub(u'\u1027', u'\u007b', output)  # ae
    output = re.sub(u'\u0073\u0054', u'\u0057', output)  # pint-swae-့htoe
    output = re.sub(u'\u0069\u0066\u00a9', u'\u0063\u0046', output)  # nga-tat-kha
    output = re.sub(u'\u0069\u0066\u00fa', u'\u0075\u0046', output)  # nga-tat-ka
    output = re.sub(u'\u0069\u0066\u00be', u'\u002a\u0046', output)  # nga-tat-ga
    output = re.sub(u'\u0069\u0066\u00a2', u'\u0043\u0046', output)  # nga-tat-gagyi
    output = re.sub(u'\u0046\u0064', u'\u00d8', output)  #lontin-ngatat
    output = re.sub(u'\u0046\u0044', u'\u00d0', output)  #sankat-ngatat

    return output

