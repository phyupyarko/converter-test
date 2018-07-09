# -*- coding: utf-8 -*-
import re



def replace(input):
    output = input
    output = output.replace(u'\u106A', u'\u1009')
    #  nyalay

    output = output.replace(u'\u1033', u'\u102F')
    #  1chaungngin

    output = output.replace(u'\u1034', u'\u1030')
    #  2chaungngin

    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')
    #  hahtoe

    output = output.replace(u'\u103C', u'\u103D')
    #  waswe

    output = output.replace(u'\u103B', u'\u103C')
    output = output.replace(u'\u107E', u'\u103C')
    output = output.replace(u'\u107F', u'\u103C')
    output = output.replace(u'\u1080', u'\u103C')
    output = output.replace(u'\u1081', u'\u103C')
    output = output.replace(u'\u1082', u'\u103C')
    output = output.replace(u'\u1083', u'\u103C')
    output = output.replace(u'\u1084', u'\u103C')

    # yayint

    output = output.replace(u'\u103A', u'\u103B')
    output = output.replace(u'\u107D', u'\u103B')
    #  yapint
    output = output.replace(u'\u106B', u'\u100A')
    #  nya

    output = output.replace(u'\u1090', u'\u101B')
    #  yakaut

    #  htawonbae

    #  dayinkaut

    #  tatlin

    output = output.replace(u'\u108F', u'\u1014')
    #  nange

    output = output.replace(u'\u1039', u'\u103A')
    # athet

    output = output.replace(u'\u1094', u'\u1037')
    output = output.replace(u'\u1095', u'\u1037')
    # out-kamyit
    output = output.replace(u'\u1086', u'\u103F')
    #  thagyi

    return output

def decompose(input):
    output = input

    output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1', output)

    output = re.sub(u'\u1064', u'\u1004\u103A\u1039', output)
    # up-ngathet
    output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038', output)
    #  la-gaung
    output = re.sub(u'\u105A', u'\u102B' + u'\u103A', output)
    #  yaychar-htoe
    output = re.sub(u'\u108A', u'\u103D' + u'\u103E', output)
    #  wa ha-htoe
    output = re.sub(u'\u1088', u'\u103E' + u'\u102F', output)
    #  hahtoe1chaung
    output = re.sub(u'\u1089', u'\u103E' + u'\u1030', output)
    #  hahtoe2chaung
    output = re.sub(u'\u103E\u103B', u'\u103B' + u'\u103E', output)
    # yapit-hahtoe
    output = re.sub(u'\u108E', u'\u102D' + u'\u1036', output)
    #  lgt-ttt
    output = re.sub(u'\u108B', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102D', output)
    # ngathet-lgt
    output = re.sub(u'\u108B', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102E', output)
    #  ngathet-lgtsk
    output = re.sub(u'\u108B', u'\u1004' + u'\u103A' + u'\u1039' + u'\u1036', output)
    #  ngathet-ttt
    output = re.sub(u'\u1025(?=[\u103a\u102c])', u'\u1009', output)


    ######  pat-sint

    output = re.sub(u'\u1060', u'\u1039\u1000', output)
    # ka
    output = re.sub(u'\u1061', u'\u1039\u1001', output)
    # kha
    output = re.sub(u'\u1062', u'\u1039\u1002', output)
    # ga-nge
    output = re.sub(u'\u1063', u'\u1039\u1003', output)
    # ga-gyi
    output = re.sub(u'\u1065', u'\u1039\u1005', output)
    # sa-lone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output)
    # sa-lane
    output = re.sub(u'\u1068', u'\u1039\u1007', output)
    # za
    output = re.sub(u'\u1069', u'\u1039\u1008', output)
    # za-zwe
    output = re.sub(u'\u106C', u'\u1039\u100B', output)
    # tatalin
    output = re.sub(u'\u1070', u'\u1039\u100F', output)
    # na-gyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output)
    # ta
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output)
    # hta
    output = re.sub(u'\u1075', u'\u1039\u1012', output)
    # da-dwe
    output = re.sub(u'\u1076', u'\u1039\u1013', output)
    # da-out
    output = re.sub(u'\u1077', u'\u1039\u1014', output)
    # na
    output = re.sub(u'\u1078', u'\u1039\u1015', output)
    # pa
    output = re.sub(u'\u1079', u'\u1039\u1016', output)
    # pha
    output = re.sub(u'\u107A', u'\u1039\u1017', output)
    # ba-htet
    output = re.sub(u'[\u107B\u1093]', u'\u1039\u1018', output)
    # ba
    output = re.sub(u'\u107C', u'\u1039\u1019', output)
    # ma
    output = re.sub(u'\u1085', u'\u1039\u101C', output)
    # la
    output = re.sub(u'\u106D', u'\u1039\u100C', output)
    # htawonbae

    ############

    output = re.sub(u'\u1091', u'\u100F\u1039\u100D', output)
    # gan-da
    output = re.sub(u'\u1092', u'\u100B\u1039\u100C', output)
    # htawon
    output = re.sub(u'\u1097', u'\u100B\u1039\u100B', output)
    # tatalin
    output = re.sub(u'\u106F', u'\u100D\u1039\u100E', output)
    # dayin-hmote
    output = re.sub(u'\u106E', u'\u100D\u1039\u100D', output)
    # dayin-kaut
    return output





def visual2logical(input):
    output = input
    output = re.sub(
        u'((?:\u1031)?)((?:\u103c)?)([\u1000-\u1021])((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1037)?)((?:\u102c)?)',
        '\\3\\2\\4\\5\\6\\1\\7\\8', output)

    return output


def convert(input):
    output = input

    output = replace(output)
    output = decompose(output)
    output = visual2logical(output)

    return output



