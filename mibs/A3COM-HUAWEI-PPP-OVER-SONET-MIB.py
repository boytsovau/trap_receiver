#
# PySNMP MIB module A3COM-HUAWEI-PPP-OVER-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-PPP-OVER-SONET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Gauge32, iso, MibIdentifier, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, ObjectIdentity, Integer32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Gauge32", "iso", "MibIdentifier", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "ObjectIdentity", "Integer32", "NotificationType", "IpAddress")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
h3cPos = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19))
h3cPos.setRevisions(('2010-05-19 17:00', '2007-07-19 17:00',))
if mibBuilder.loadTexts: h3cPos.setLastUpdated('201005191700Z')
if mibBuilder.loadTexts: h3cPos.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
h3cPosMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1))
h3cPosParamTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1), )
if mibBuilder.loadTexts: h3cPosParamTable.setStatus('current')
h3cPosParamTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosParamTableEntry.setStatus('current')
h3cPosCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc32", 1), ("crc16", 2))).clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosCRC.setStatus('current')
h3cPosMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 9192))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosMTU.setStatus('current')
h3cPosScramble = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosScramble.setStatus('current')
h3cPosClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("system", 1), ("line", 2))).clone('line')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosClockSource.setStatus('current')
h3cPosSdhFlagJ0 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosSdhFlagJ0.setStatus('current')
h3cPosSdhFlagJ1 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosSdhFlagJ1.setStatus('current')
h3cPosSonetFlagJ0 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosSonetFlagJ0.setStatus('current')
h3cPosSonetFlagJ1 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosSonetFlagJ1.setStatus('current')
h3cPosFlagC2 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosFlagC2.setStatus('current')
h3cPosFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosFrameType.setStatus('current')
h3cPosBindVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosBindVlanId.setStatus('current')
h3cPosEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ppp", 1), ("hdlc", 2))).clone('ppp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosEncapsulation.setStatus('current')
h3cPoskeepaliveTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPoskeepaliveTimeout.setStatus('current')
h3cPosBERthresholdSF = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosBERthresholdSF.setStatus('current')
h3cPosBERthresholdSD = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosBERthresholdSD.setStatus('current')
h3cPosB1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPosB1Error.setStatus('current')
h3cPosB2Error = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPosB2Error.setStatus('current')
h3cPosB3Error = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPosB3Error.setStatus('current')
h3cPosM1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPosM1Error.setStatus('current')
h3cPosG1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cPosG1Error.setStatus('current')
h3cPosFlagJ0Type = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosFlagJ0Type.setStatus('current')
h3cPosFlagJ1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosFlagJ1Type.setStatus('current')
h3cPosB1TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosB1TCAThreshold.setStatus('current')
h3cPosB2TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosB2TCAThreshold.setStatus('current')
h3cPosB3TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosB3TCAThreshold.setStatus('current')
h3cPosB1TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosB1TCAEnable.setStatus('current')
h3cPosB2TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosB2TCAEnable.setStatus('current')
h3cPosB3TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 1, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cPosB3TCAEnable.setStatus('current')
h3cPosMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2))
h3cPosMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0))
h3cPosLOSAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosLOSAlarm.setStatus('current')
h3cPosLOFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosLOFAlarm.setStatus('current')
h3cPosOOFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosOOFAlarm.setStatus('current')
h3cPosLAISAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosLAISAlarm.setStatus('current')
h3cPosLRDIAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosLRDIAlarm.setStatus('current')
h3cPosPRDIAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 6)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosPRDIAlarm.setStatus('current')
h3cPosPAISAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 7)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosPAISAlarm.setStatus('current')
h3cPosLOPAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 8)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosLOPAlarm.setStatus('current')
h3cPosSTIMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 9)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosSTIMAlarm.setStatus('current')
h3cPosPTIMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 10)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosPTIMAlarm.setStatus('current')
h3cPosPSLMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 11)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosPSLMAlarm.setStatus('current')
h3cPosLSDAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosLSDAlarm.setStatus('current')
h3cPosLSFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 13)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosLSFAlarm.setStatus('current')
h3cPosNormalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 14)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cPosNormalAlarm.setStatus('current')
h3cPosB1TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 15)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: h3cPosB1TCAlarm.setStatus('current')
h3cPosB2TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 16)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: h3cPosB2TCAlarm.setStatus('current')
h3cPosB3TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 19, 2, 0, 17)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: h3cPosB3TCAlarm.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-PPP-OVER-SONET-MIB", h3cPosB2Error=h3cPosB2Error, h3cPosPAISAlarm=h3cPosPAISAlarm, h3cPosSonetFlagJ0=h3cPosSonetFlagJ0, h3cPosB3TCAThreshold=h3cPosB3TCAThreshold, h3cPosLRDIAlarm=h3cPosLRDIAlarm, h3cPosMTU=h3cPosMTU, PYSNMP_MODULE_ID=h3cPos, h3cPosParamTable=h3cPosParamTable, h3cPosBERthresholdSD=h3cPosBERthresholdSD, h3cPosLAISAlarm=h3cPosLAISAlarm, h3cPosB1TCAThreshold=h3cPosB1TCAThreshold, h3cPosMIBNotificationsPrefix=h3cPosMIBNotificationsPrefix, h3cPoskeepaliveTimeout=h3cPoskeepaliveTimeout, h3cPosFlagJ0Type=h3cPosFlagJ0Type, h3cPosB3TCAlarm=h3cPosB3TCAlarm, h3cPosFlagC2=h3cPosFlagC2, h3cPosLOSAlarm=h3cPosLOSAlarm, h3cPosM1Error=h3cPosM1Error, h3cPosG1Error=h3cPosG1Error, h3cPosFlagJ1Type=h3cPosFlagJ1Type, h3cPosLOPAlarm=h3cPosLOPAlarm, h3cPosB1TCAEnable=h3cPosB1TCAEnable, h3cPosSdhFlagJ1=h3cPosSdhFlagJ1, h3cPosB2TCAlarm=h3cPosB2TCAlarm, h3cPos=h3cPos, h3cPosLOFAlarm=h3cPosLOFAlarm, h3cPosPSLMAlarm=h3cPosPSLMAlarm, h3cPosFrameType=h3cPosFrameType, h3cPosMIBNotifications=h3cPosMIBNotifications, h3cPosSdhFlagJ0=h3cPosSdhFlagJ0, h3cPosB3Error=h3cPosB3Error, h3cPosNormalAlarm=h3cPosNormalAlarm, h3cPosB3TCAEnable=h3cPosB3TCAEnable, h3cPosB1Error=h3cPosB1Error, h3cPosLSFAlarm=h3cPosLSFAlarm, h3cPosScramble=h3cPosScramble, h3cPosPRDIAlarm=h3cPosPRDIAlarm, h3cPosOOFAlarm=h3cPosOOFAlarm, h3cPosSonetFlagJ1=h3cPosSonetFlagJ1, h3cPosLSDAlarm=h3cPosLSDAlarm, h3cPosB1TCAlarm=h3cPosB1TCAlarm, h3cPosMIBObjects=h3cPosMIBObjects, h3cPosB2TCAEnable=h3cPosB2TCAEnable, h3cPosClockSource=h3cPosClockSource, h3cPosSTIMAlarm=h3cPosSTIMAlarm, h3cPosParamTableEntry=h3cPosParamTableEntry, h3cPosBERthresholdSF=h3cPosBERthresholdSF, h3cPosB2TCAThreshold=h3cPosB2TCAThreshold, h3cPosPTIMAlarm=h3cPosPTIMAlarm, h3cPosBindVlanId=h3cPosBindVlanId, h3cPosEncapsulation=h3cPosEncapsulation, h3cPosCRC=h3cPosCRC)
