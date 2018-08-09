# -*- coding: utf-8 -*-
import re


def convert(input):
    tallAA = u'\u102B'
    AA = u'\u102C'
    vi = u'\u102D'
    # lone gyi tin
    ii = u'\u102E'
    u = u'\u102F'
    uu = u'\u1030'
    ve = u'\u1031'
    ai = u'\u1032'
    ans = u'\u1036'
    db = u'\u1037'
    visarga = u'\u1038'

    asat = u'\u103A'

    ya = u'\u103B'
    ra = u'\u103C'
    wa = u'\u103D'
    ha = u'\u103E'
    zero = u'\u1040'
    i=0
    byee=[u'\u1000',u'\u1001',u'\u1002',u'\u1003',u'\u1005',u'\u1006',u'\u1007',u'\u1008',u'\u100b',u'\u100c',u'\u100f',u'\u1010',u'\u1011',u'\u1012',u'\u1013',u'\u1014',u'\u1015',u'\u1016',u'\u1017',u'\u1018',u'\u1019',u'\u101c']
    byeesint=[u'\u1060',u'\u1061',u'\u1062',u'\u1063',u'\u1065',u'\u1066',u'\u1068',u'\u1069',u'\u106b',u'\u106d',u'\u1070',u'\u1071',u'\u1073',u'\u1075',u'\u1076',u'\u1077',u'\u1078',u'\u1079',u'\u107a',u'\u107b',u'\u107c',u'\u1085']

 #---------------------------------------------------------------------------------------
    output = input
    output = output.replace(u'\u100b\u1039\u100c', u'\u1092')
    output = output.replace(u'\u1039\u1000', u'\u1060')
    output = output.replace(u'\u1039\u1001', u'\u1061')
    output = output.replace(u'\u1039\u1002', u'\u1062')
    output = output.replace(u'\u1039\u1003', u'\u1063')
    output = output.replace(u'\u1039\u1005', u'\u1065')
    output = output.replace(u'\u1039\u1006', u'\u1066')
    output = output.replace(u'\u1039\u1006', u'\u1067')
    output = output.replace(u'\u1039\u1007', u'\u1068')
    output = output.replace(u'\u1039\u1008', u'\u1069')
    output = output.replace(u'\u1039\u100B', u'\u106C')
    output = output.replace(u'\u1039\u100C', u'\u106D')
    output = output.replace(u'\u1039\u100F', u'\u1070')
    output = output.replace(u'\u1039\u1010', u'\u1071')
    output = output.replace(u'\u1039\u1011', u'\u1073')
    output = output.replace(u'\u1039\u1011', u'\u1074')
    output = output.replace(u'\u1039\u1012', u'\u1075')
    output = output.replace(u'\u1039\u1013', u'\u1076')
    output = output.replace(u'\u1039\u1014', u'\u1077')
    output = output.replace(u'\u1039\u1015', u'\u1078')
    output = output.replace(u'\u1039\u1016', u'\u1079')
    output = output.replace(u'\u1039\u1017', u'\u107A')
    output = output.replace(u'\u1039\u1019', u'\u107C')
    output = output.replace(u'\u1039\u101C', u'\u1085')
    output = output.replace(u'\u1039\u1018', u'\u107B')

    #-------------------------------------------------------------------------------------------------------------------------------
    output = output.replace(u'\u100F\u103A\u100D', u'\u1091')
    output = output.replace(u'\u100d\u1039\u100e', u'\u106f')
    output = output.replace(u'\u103A', u'\u1039')#a-that
    output = output.replace(u'\u103B', u'\u103A')#ya-pint
    output = output.replace(u'\u103C', u'\u103B')#ya-yit
    output = output.replace(u'\u103D', u'\u103C')#wa-swae
    output = output.replace(u'\u103E', u'\u103D')#ha-htoe
    output = output.replace(u'\u103F', u'\u1086')#ta-gyi

    output = output.replace(u'\u1040', u'\u101D') #wa
    #output = output.replace(u'\u1039\u1004\u103A', u'\u1064')
    output = output.replace(u'\u1009\u1039', u'\u1025\u1039')#nyalay-that
    output = output.replace(u'\u103C\u103D', u'\u103D\u103C')
    output = output.replace(u'\u103D\u103C', u'\u108A')#waswae-hatoe
    #output = output.replace(u'[\u102F\u1030]\u1037', u'[\u102F\u1030]\u1095')
    #output = output.replace(u'[\u102F\u1030][\u102D\u102E]\u1037', u'[\u102F\u1030][\u102D\u102E]\u1095')
    output = output.replace(u'\u102D\u1036', u'\u108E')  # NgaGyi...
    output = output.replace(u'\u100A\u103D', u'\u100A\u1087')  #nya-htoe
    output = output.replace(u'\u102f\u1036', u'\u1036\u102f') #ttt-tachaung
#--------------------------------------------------------------------------------------------------------------------------
    output = output.replace(u'\u1004\u1039\u1062', u'\u1002\u1064') #Ka....
    output = output.replace(u'\u1004\u1039\u1060', u'\u1000\u1064') #Kha...
    output = output.replace(u'\u1004\u1039\u1061', u'\u1001\u1064') #Ga....
    output = output.replace(u'\u1004\u1039\u1063', u'\u1003\u1064') #NgaGyi...
    output = output.replace(u'\u1064\u102D', u'\u108B')  # NgaGyi...
    output = output.replace(u'\u1064\u102E', u'\u108C')  # NgaGyi...
    output = output.replace(u'\u1064\u1036', u'\u108D')  # NgaGyi...
    output = output.replace(u'\u102D\u1036', u'\u108E')  # NgaGyi...

#-----------------------nange-------------------------------------------------------------------------------------------------
    output = output.replace(u'\u1014\u103D', u'\u108F\u103D')#nange-hatoe
    output = output.replace(u'\u1014\u103C', u'\u108F\u103C')  # nange-waswae
    output = output.replace(u'\u1014\u102F', u'\u108F\u102F')  # nange-tachaung
    output = output.replace(u'\u1014\u1075', u'\u108F\u1075')  # nange-dadwae
    output = output.replace(u'\u1014\u1076', u'\u108F\u1076')  # nange-daout
    output = output.replace(u'\u1014\u1077', u'\u108F\u1077')  # nange-nange
    output = output.replace(u'\u1014\u102D\u102F', u'\u108F\u102D\u102F')  # nange-tachaung lonetin

#----------------------ya-----------------------------------------------------------------------------------------------
    #output = output.replace(u'\u101B\u103D', u'\u1090\u103D')  # ya-hatoe
    output = output.replace(u'\u101B\u103C', u'\u1090\u103C')  # ya-waswae
    output = output.replace(u'\u101B\u102F', u'\u1090\u102F')  # ya-tachaung
    output = output.replace(u'\u101B\u102D\u102F', u'\u1090\u102D\u102F')  # ya-tachaung lonetin
    output = output.replace(u'\u101B\u108A', u'\u1090\u108A')  # ya-tachaung lonetini
#-----------------------tachaung-nachaung-------------------------------------------------------------------------------
    output = re.sub(u'\u103B\u102F', u'\u103B\u1033', output)#yit-tachaung
    output = re.sub(u'\u103B\u1030', u'\u103B\u1034', output) #yit-nachaung
    output = re.sub(u'\u103B\u102D\u102F', u'\u103B\u102D\u1033', output) #yit-lonetin-tachaung
    output = re.sub(u'\u103B\u1036\u102F', u'\u103B\u1036\u1033', output)  # yit-ttt-tachaung
    output = re.sub(u'\u103A\u102F', u'\u103A\u1033', output)  #pint-tachaung
    output = re.sub(u'\u103A\u1030', u'\u103A\u1034', output)  #pint-nachaung
    output = re.sub(u'\u103A\u103C', u'\u107D\u103C', output)  #pint-waswe
    output = output.replace(u'\u103D\u103A', u'\u103A\u103D')  #pint-htoe
    output = re.sub(u'\u103A\u102D\u102F', u'\u103A\u102D\u1033', output) #pint-lontin-tachaung
#-------------------------ta-wai-htoe-----------------------------------------------------------------------------------
    output = re.sub(u'([\u1000-\u1021])([\u103A])(\u1031)', u"\\3\\1\\2", output)#tawai-yapint-byee
    output = re.sub(u'([\u1000-\u1021])(\u103B)', u"\\2\\1", output)#yayit-byee
    output = re.sub(u'([\u1000-\u1021])(\u1031)', u"\\2\\1", output)#thawai-byee
    output = re.sub(u'([\u103B])(\u1031)', u"\\2\\1", output)#tawai-yayit
    output = re.sub(u'([\u1000-\u1021])([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)#tawai-byee-swae-htoe
    output = re.sub(u'(\u108F)([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)#tawai-nagnge-swae-htoe
    output = re.sub(u'(\u1090)([\u103C\u103D])(\u1031)', u"\\3\\1\\2", output)  # tawai-ya-swae-htoe
    output = re.sub(u'(\u108F)(\u108A)(\u1031)', u"\\3\\1\\2", output)  # tawai-nagnge-swae-htoe
    output = re.sub(u'(\u1090)(\u108A)(\u1031)', u"\\3\\1\\2", output)  # tawai-nagnge-swae-htoe
    output = re.sub(u'([\u1000-\u1021])([\u108A])(\u1031)', u"\\3\\1\\2", output)#tawai-byee-swae-htoe
    output = re.sub(u'([\u1000-\u1021])(\u103A)(\u103D)(\u1031)', u"\\4\\1\\2\\3", output)  # tawai-yapint-byee
    output = re.sub(u'\u1014([\u1070-\u107c])', u'\u108f\\1', output)
    # while(True):
    #     output = re.sub(([\u1070-\u107c])', u'\u108f\\1', output)
#-------------------------------out myit-------------------------------------------------------------------------------
    output = re.sub(u'\u1030\u1037', u'\u1030\u1094', output)  # out-myit nachaung
    output = re.sub(u'\u103C\u1037', u'\u103C\u1095', output)  # out-myit waswae
    output = re.sub(u'\u108A\u1037', u'\u108A\u1095', output)  # out-myit waswaehtoe
    output = re.sub(u'\u102D\u102F\u1037', u'\u102D\u102F\u1094', output)  # out-myit lonetin tachaung
    output = re.sub(u'\u103C\u1032\u1037', u'\u103C\u1032\u1094', output)  # out-myit nouthtoe waswae
    output = re.sub(u'\u103C\u1036\u1037', u'\u103C\u1036\u1095', output)  # out-myit taetin waswae
    output = re.sub(u'\u1036\u1088\u1037', u'\u1036\u1088\u1095', output)  # out-myit hahtoe nachaung
    output = re.sub(u'(\u103D)(\u1036)(\u102F)\u1037', u'\\1\\2\\3\u1094', output)  # out-myit hahtoe nachaung
    output = re.sub(u'\u1014\u1037', u'\u1014\u1094', output)  # autmyint-nange
    #------------------------twae----------------------------------------------------------------------------------
    output = output.replace(u'\u102B\u1039', u'\u105A')#yaecha-shaehtoe
    #output = output.replace(u'\u103D\u102F', u'\u1088')#hatoe-tachaung
    output = output.replace(u'\u103D\u1030', u'\u1089')#hatoe-nachaung
    output = re.sub(u'([\u1060-\u1063])((?:[\u102D\u102E])?)\u102F', u'\\1\\2\u1033', output)#sint lonetin chaungnin
    output = re.sub(u'([\u1065-\u1069])((?:[\u102D\u102E])?)\u102F', u'\\1\\2\u1033', output)  # sint lonetin chaungnin
    output = re.sub(u'([\u1070-\u107C])((?:[\u102D\u102E])?)\u102F', u'\\1\\2\u1033', output)  # sint lonetin chaungnin
    output = re.sub(u'([\u1085\u1093])((?:[\u102D\u102E])?)\u102F', u'\\1\\2\u1033', output)  # sint lonetin chaungnin
    output = re.sub(u'([\u1060-\u1063])((?:[\u102D\u102E])?)\u1030', u'\\1\\2\u1034', output)  # sint lonetin chaungnin
    output = re.sub(u'([\u1065-\u1069])((?:[\u102D\u102E])?)\u1030', u'\\1\\2\u1034', output)  # sint lonetin chaungnin
    output = re.sub(u'([\u1070-\u107C])((?:[\u102D\u102E])?)\u1030', u'\\1\\2\u1034', output)  # sint lonetin chaungnin
    output = re.sub(u'([\u1085\u1093])((?:[\u102D\u102E])?)\u1030', u'\\1\\2\u1034', output)  # sint lonetin chaungnin
    output = output.replace(u'(\u103A)(\u103D)((?:\u102D)?)(', u'\u107D\u103D')#pint-htoe
    #output = output.replace(u'\u103C\u103D', u'\u108A')


    #-------------------yitgyilonegyitin-----------------------------------------------------------------------------------------------
    output = re.sub(u'\u103b(\u1000)([\u1036\u102D\u102E])', u'\u1080\\1\\2', output)
    output = re.sub(u'\u103b(\u1006)([\u1036\u102D\u102E])', u'\u1080\\1\\2', output)
    output = re.sub(u'\u103b(\u1010)([\u1036\u102D\u102E])', u'\u1080\\1\\2', output)
    # -------------------yitgyi-------------------------------------------------------------------------------------------

    output = re.sub(u'\u103b\u1000', u'\u107E\u1000', output)
    output = re.sub(u'\u103b\u1006', u'\u107E\u1006', output)
    output = re.sub(u'\u103b\u1010', u'\u107E\u1010', output)
    # --------------yitgyi-lonetin-waswae-------------------------------------------------------------
    output = re.sub(u'\u107E\u1000\u103C\u102D', u'\u1084\u1000\u103C\u102D', output)
    output = re.sub(u'\u107E\u1006\u103C\u102D', u'\u1084\u1006\u103C\u102D', output)
    output = re.sub(u'\u107E\u1010\u103C\u102D', u'\u1084\u1010\u103C\u102D', output)
    output = re.sub(u'\u107E\u1000\u103C\u102E', u'\u1084\u1000\u103C\u102E', output)
    output = re.sub(u'\u107E\u1006\u103C\u102E', u'\u1084\u1006\u103C\u102E', output)
    output = re.sub(u'\u107E\u1010\u103C\u102E', u'\u1084\u1010\u103C\u102E', output)

    #-------------------------yayutgi-waswae-------------------------------------------------------------------------------------------------------------------
    output = re.sub(u'\u107E\u1000\u103C', u'\u1082\u1000\u103C', output)
    output = re.sub(u'\u107E\u1006\u103C', u'\u1082\u1006\u103C', output)
    output = re.sub(u'\u107E\u1010\u103C', u'\u1082\u1010\u103C', output)
    output = re.sub(u'\u107E\u1010([\u1070-\u107c])', u'\u1082\u1010([\u1070-\u107c])', output)
#---------------------------------yitlay-lonetin-waswae------------------------------------------ -----------------------------------------

    output = re.sub(u'\u103B(\u1001)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
    output = re.sub(u'\u103B(\u1002)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
    output = re.sub(u'\u103B(\u1004)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
    output = re.sub(u'\u103B(\u1012)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
    output = re.sub(u'\u103B(\u1015)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
    output = re.sub(u'\u103B(\u1016)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
    output = re.sub(u'\u103B(\u1017)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
    output = re.sub(u'\u103B(\u1019)(\u103C)([\u102D\u102e])', u'\u1083\\1\\2', output)
#---------------yitlay-lonetin-ttt-----------------------------------------------------------------------------------------------------------------------

    output = re.sub(u'\u103B(\u1001)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
    output = re.sub(u'\u103B(\u1002)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
    output = re.sub(u'\u103B(\u1004)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
    output = re.sub(u'\u103B(\u1012)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
    output = re.sub(u'\u103B(\u1015)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
    output = re.sub(u'\u103B(\u1016)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
    output = re.sub(u'\u103B(\u1017)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
    output = re.sub(u'\u103B(\u1019)([\u1036\u102d\u102e])', u'\u107F\\1\\2', output)
#--------------------------yitlay-waswae-----------------------------------------------------------------------------------------
    output = re.sub(u'\u103B\u1001\u103C', u'\u1081\u1001\u103C', output)
    output = re.sub(u'\u103B\u1002\u103C', u'\u1081\u1002\u103C', output)
    output = re.sub(u'\u103B\u1004\u103C', u'\u1081\u1004\u103C', output)
    output = re.sub(u'\u103B\u1012\u103C', u'\u1081\u1012\u103C', output)
    output = re.sub(u'\u103B\u1015\u103C', u'\u1081\u1015\u103C', output)
    output = re.sub(u'\u103B\u1016\u103C', u'\u1081\u1016\u103C', output)
    output = re.sub(u'\u103B\u1017\u103C', u'\u1081\u1017\u103C', output)
    output = re.sub(u'\u103B\u1019\u103C', u'\u1081\u1019\u103C', output)
    output = re.sub(u'\u107f([\u1001\u1002\u1004\u1012\u1015\u1016\u1017\u1019])', u'\u103b\\1', output)
    output = re.sub(u'\u1019\u107B\u102c', u'\u1019\u1093\u102c', output)  # ma-ba
    output = re.sub(u'\u1005\u1066\u102c', u'\u1005\u1067\u102c', output)  # sa-sal
    output = re.sub(u'\u1014\u1071\u102c', u'\u108f\u1072\u102c', output)  # na-ta
    # output = re.sub(u'\u1019\u107B\u102c', u'\u1019\u1093\u102c', output)  # ma-ba
    output = re.sub(u'\u100a(\u108a)', u'\u106b\\1', output)  # nya-swae-htoe
    output = re.sub(u'(\u1036)(\u102f)', u'\\2\\1', output)
    output = re.sub(u'\u1025([\u1065\u1068])', u'\u106a\\1', output)
    output = re.sub(u'(\u108f)(\u1075)\u103b', u'\u1081\\1\\2', output)

    return output
