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
    listgyi=[u'\u1000', u'\u1003', u'\u1006', u'\u100F', u'\u1010', u'\u1011', u'\u1018', u'\u101A', u'\u101C', u'\u101E', u'\u101F', u'\u1021']
 #---------------------------------------------------------------------------------------
    output = input
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
    output = output.replace(u'\u1039\u1010', u'\u1072')
    output = output.replace(u'\u1039\u1011', u'\u1073')
    output = output.replace(u'\u1039\u1011', u'\u1074')
    output = output.replace(u'\u1039\u1012', u'\u1075')
    output = output.replace(u'\u1039\u1013', u'\u1076')
    output = output.replace(u'\u1039\u1014', u'\u1077')
    output = output.replace(u'\u1039\u1015', u'\u1078')
    output = output.replace(u'\u1039\u1016', u'\u1079')
    output = output.replace(u'\u1039\u1017', u'\u107A')
    output = output.replace(u'\u1039\u1018', u'\u107B')
    output = output.replace(u'\u1039\u1019', u'\u107C')
    output = output.replace(u'\u1039\u101C', u'\u1085')
    output = output.replace(u'\u1039\u1018', u'\u1092')
#-------------------------------------------------------------------------------------------------------------------------------
    output = output.replace(u'\u100F\u103A\u100D', u'\u1091')
    output = output.replace(u'\u103A', u'\u1039')#a-that
    output = output.replace(u'\u103B', u'\u103A')#ya-pint
    output = output.replace(u'\u103C', u'\u103B')#ya-yit
    output = output.replace(u'\u103D', u'\u103C')#wa-swae
    output = output.replace(u'\u103E', u'\u103D')#ha-htoe
    output = output.replace(u'\u103F', u'\u1086')#ta-gyi
    #output = output.replace(u'\u1039\u1004\u103A', u'\u1064')
    output = output.replace(u'\u1009\u1039', u'\u106A\u1039')#nyalay-that
    output = output.replace(u'\u103C\u103D', u'\u103D\u103C')
    output = output.replace(u'\u103D\u103C', u'\u108A')#waswae-hatoe
    #output = output.replace(u'[\u102F\u1030]\u1037', u'[\u102F\u1030]\u1095')
    #output = output.replace(u'[\u102F\u1030][\u102D\u102E]\u1037', u'[\u102F\u1030][\u102D\u102E]\u1095')
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

#----------------------ya-------------------------------------------------------------------------------------------------------
    output = output.replace(u'\u101B\u103D', u'\u1090\u103D')  # ya-hatoe
    output = output.replace(u'\u101B\u103C', u'\u1090\u103C')  # ya-waswae
    output = output.replace(u'\u101B\u102F', u'\u1090\u102F')  # ya-tachaung
    output = output.replace(u'\u101B\u103D', u'\u1090\u103D')  # ya-hatoe
    output = output.replace(u'\u101B\u102D\u102F', u'\u1090\u102D\u102F')  # ya-tachaung lonetin
    output = output.replace(u'\u101B\u108A', u'\u1090\u108A')  # ya-tachaung lonetin
#------------------------------------------------------------------------------------------------------------------------------
    output = re.sub(u'\u103B\u102F', u'\u103B\u1033', output)#yayit-tachaung
    output = re.sub(u'\u103B\u1030', u'\u103B\u1034', output)  # yayit-nachaung
    output = re.sub(u'\u103B\u102D\u102F', u'\u103B\u102D\u1033', output)  # yayit-lonetin-tachaung
    output = re.sub(u'\u103A\u102F', u'\u103A\u1033', output)  # yapint-tachaung
    output = re.sub(u'\u103A\u1030', u'\u103A\u1034', output)  # yapint-nachaung
    output = re.sub(u'\u103A\u103C', u'\u107D\u103C', output)  # pint-waswe
    output = output.replace(u'\u103D\u103A', u'\u103A\u103D')  # pint-htoe
    output = re.sub(u'\u103A\u102D\u102F', u'\u103A\u102D\u1033', output) #yapint-lontin-tachaung

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

#-------------------------------out myit-------------------------------------------------------------------------------
    output = re.sub(u'\u1030\u1037', u'\u1030\u1094', output)  #out-myit nachaung
    output = re.sub(u'\u103C\u1037', u'\u103C\u1094', output)  # out-myit waswae
    output = re.sub(u'\u108A\u1037', u'\u108A\u1095', output)  # out-myit waswae
    output = re.sub(u'\u102D\u102F\u1037', u'\u102D\u102F\u1094', output)  #out-myit lonetin tachaung
    output = re.sub(u'\u103C\u1032\u1037', u'\u103C\u1032\u1094', output)  # out-myit nouthtoe waswae
    output = re.sub(u'\u103C\u1036\u1037', u'\u103C\u1036\u1095', output)  # out-myit taetin waswae
    output = re.sub(u'\u1036\u1088\u1037', u'\u1036\u1088\u1095', output)  # out-myit hahtoe nachaung
    output = output.replace(u'\u1014\u1037', u'\u1014\u1094')  # autmyint-nange

#----------------------------------------------------------------------------------------------------------
    output = output.replace(u'\u102B\u1039', u'\u105A')#yaecha-shaehtoe
    output = output.replace(u'\u103D\u102F', u'\u1088')#hatoe-tachaung
    output = output.replace(u'\u103D\u1030', u'\u1089')#hatoe-nachaung
    output = output.replace(u'\u1062\u102D\u102F', u'\u1062\u102D\u1033')
    output = output.replace(u'\u1062\u102F', u'\u1062\u1033')
    #output = output.replace(u'\u103C\u103D', u'\u108A')
#-------------------yitgyi-------------------------------------------------------------------------------------------

    output = re.sub(u'\u103B\u1000', u'\u107E\u1000', output)
    output = re.sub(u'\u103B\u1006', u'\u107E\u1006', output)
    output = re.sub(u'\u103B\u1010', u'\u107E\u1010', output)
#--------------yitgyi-lonetin-waswae-------------------------------------------------------------
    output = re.sub(u'\u107E\u1000\u103C\u102D', u'\u1084\u1000\u103C\u102D', output)
    output = re.sub(u'\u107E\u1006\u103C\u102D', u'\u1084\u1006\u103C\u102D', output)
    output = re.sub(u'\u107E\u1010\u103C\u102D', u'\u1084\u1010\u103C\u102D', output)
    output = re.sub(u'\u107E\u1000\u103C\u102E', u'\u1084\u1000\u103C\u102E', output)
    output = re.sub(u'\u107E\u1006\u103C\u102E', u'\u1084\u1006\u103C\u102E', output)
    output = re.sub(u'\u107E\u1010\u103C\u102E', u'\u1084\u1010\u103C\u102E', output)

    #-------------------yitgyilonegyitin-----------------------------------------------------------------------------------------------
    output = re.sub(u'\u107E\u1000\u102D', u'\u1080\u1000\u102D', output)
    output = re.sub(u'\u107E\u1006\u102D', u'\u1080\u1006\u102D', output)
    output = re.sub(u'\u107E\u1010\u102D', u'\u1080\u1010\u102D', output)
    output = re.sub(u'\u107E\u1000\u102E', u'\u1080\u1000\u102E', output)
    output = re.sub(u'\u107E\u1006\u102E', u'\u1080\u1006\u102E', output)
    output = re.sub(u'\u107E\u1010\u102E', u'\u1080\u1010\u102E', output)

#-------------------------yayutgi-waswae-------------------------------------------------------------------------------------------------------------------
    output = re.sub(u'\u107E\u1000\u103C', u'\u1082\u1000\u103C', output)
    output = re.sub(u'\u107E\u1006\u103C', u'\u1082\u1006\u103C', output)
    output = re.sub(u'\u107E\u1010\u103C', u'\u1082\u1010\u103C', output)
#---------------------------------yitlay-lonetin-waswae------------------------------------------ -----------------------------------------
    output = re.sub(u'\u103B\u1001\u103C\u102D', u'\u1083\u1001\u103C\u102D', output)
    output = re.sub(u'\u103B\u1002\u103C\u102D', u'\u1083\u1002\u103C\u102D', output)
    output = re.sub(u'\u103B\u1004\u103C\u102D', u'\u1083\u1004\u103C\u102D', output)
    output = re.sub(u'\u103B\u1012\u103C\u102D', u'\u1083\u1012\u103C\u102D', output)
    output = re.sub(u'\u103B\u1015\u103C\u102D', u'\u1083\u1015\u103C\u102D', output)
    output = re.sub(u'\u103B\u1016\u103C\u102D', u'\u1083\u1016\u103C\u102D', output)
    output = re.sub(u'\u103B\u1017\u103C\u102D', u'\u1083\u1017\u103C\u102D', output)
    output = re.sub(u'\u103B\u1019\u103C\u102E', u'\u1083\u1019\u103C\u102D', output)
    output = re.sub(u'\u103B\u1001\u103C\u102E', u'\u1083\u1001\u103C\u102E', output)
    output = re.sub(u'\u103B\u1002\u103C\u102E', u'\u1083\u1002\u103C\u102E', output)
    output = re.sub(u'\u103B\u1004\u103C\u102E', u'\u1083\u1004\u103C\u102E', output)
    output = re.sub(u'\u103B\u1012\u103C\u102E', u'\u1083\u1012\u103C\u102E', output)
    output = re.sub(u'\u103B\u1015\u103C\u102E', u'\u1083\u1015\u103C\u102E', output)
    output = re.sub(u'\u103B\u1016\u103C\u102E', u'\u1083\u1016\u103C\u102E', output)
    output = re.sub(u'\u103B\u1017\u103C\u102E', u'\u1083\u1017\u103C\u102E', output)
    output = re.sub(u'\u103B\u1019\u103C\u102E', u'\u1083\u1019\u103C\u102E', output)
#---------------yitlay-lonetin-----------------------------------------------------------------------------------------------------------------------
    output = re.sub(u'\u103B\u1001\u102D', u'\u107F\u1001\u102D', output)
    output = re.sub(u'\u103B\u1002\u102D', u'\u107F\u1002\u102D', output)
    output = re.sub(u'\u103B\u1004\u102D', u'\u107F\u1004\u102D', output)
    output = re.sub(u'\u103B\u1012\u102D', u'\u107F\u1012\u102D', output)
    output = re.sub(u'\u103B\u1015\u102D', u'\u107F\u1015\u102D', output)
    output = re.sub(u'\u103B\u1016\u102D', u'\u107F\u1016\u102D', output)
    output = re.sub(u'\u103B\u1017\u102D', u'\u107F\u1017\u102D', output)
    output = re.sub(u'\u103B\u1019\u102E', u'\u107F\u1019\u102D', output)
    output = re.sub(u'\u103B\u1001\u102E', u'\u107F\u1001\u102E', output)
    output = re.sub(u'\u103B\u1002\u102E', u'\u107F\u1002\u102E', output)
    output = re.sub(u'\u103B\u1004\u102E', u'\u107F\u1004\u102E', output)
    output = re.sub(u'\u103B\u1012\u102E', u'\u107F\u1012\u102E', output)
    output = re.sub(u'\u103B\u1015\u102E', u'\u107F\u1015\u102E', output)
    output = re.sub(u'\u103B\u1016\u102E', u'\u107F\u1016\u102E', output)
    output = re.sub(u'\u103B\u1017\u102E', u'\u107F\u1017\u102E', output)
    output = re.sub(u'\u103B\u1019\u102E', u'\u107F\u1019\u102E', output)
#--------------------------yitlay-waswae-----------------------------------------------------------------------------------------
    output = re.sub(u'\u103B\u1001\u103C', u'\u1081\u1001\u103C', output)
    output = re.sub(u'\u103B\u1002\u103C', u'\u1081\u1002\u103C', output)
    output = re.sub(u'\u103B\u1004\u103C', u'\u1081\u1004\u103C', output)
    output = re.sub(u'\u103B\u1012\u103C', u'\u1081\u1012\u103C', output)
    output = re.sub(u'\u103B\u1015\u103C', u'\u1081\u1015\u103C', output)
    output = re.sub(u'\u103B\u1016\u103C', u'\u1081\u1016\u103C', output)
    output = re.sub(u'\u103B\u1017\u103C', u'\u1081\u1017\u103C', output)
    output = re.sub(u'\u103B\u1019\u103C', u'\u1081\u1019\u103C', output)


    return output