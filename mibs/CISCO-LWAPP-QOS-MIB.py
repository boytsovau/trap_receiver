#
# PySNMP MIB module CISCO-LWAPP-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
cLApDot11IfEntry, cLApDot11IfType, cLApSysMacAddress, cLApDot11IfSlotId, cLApName = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApDot11IfEntry", "cLApDot11IfType", "cLApSysMacAddress", "cLApDot11IfSlotId", "cLApName")
cldcClientMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress")
cLWlanIndex, cLWlanConfigEntry = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex", "cLWlanConfigEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Unsigned32, NotificationType, iso, ObjectIdentity, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Unsigned32", "NotificationType", "iso", "ObjectIdentity", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "Counter64", "MibIdentifier")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoLwappQosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 524))
ciscoLwappQosMIB.setRevisions(('2010-07-21 00:00', '2007-01-07 00:00', '2006-04-13 00:00',))
if mibBuilder.loadTexts: ciscoLwappQosMIB.setLastUpdated('201007210000Z')
if mibBuilder.loadTexts: ciscoLwappQosMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappQosMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 0))
ciscoLwappQosMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1))
ciscoLwappQosMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 2))
cLQd11aCACConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1))
cLQd11bCACConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2))
cLQd11GprConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3))
cLQd11CACStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4))
cLQEntConfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 5))
cLQd11VoiceStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6))
cLQVoiceWlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7))
cLQVoiceClient = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8))
cLQd11SipCacConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9))
cLQConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 10))
cLQd11aVoiceAdmCtrlSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aVoiceAdmCtrlSupport.setStatus('current')
cLQd11aVoiceMaxAdmBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aVoiceMaxAdmBandwidth.setStatus('current')
cLQd11aVoiceMaxRoamBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aVoiceMaxRoamBandwidth.setStatus('current')
cLQd11aVideoAdmCtrlSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aVideoAdmCtrlSupport.setStatus('current')
cLQd11aVideoMaxAdmBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aVideoMaxAdmBandwidth.setStatus('current')
cLQd11aVideoMaxRoamBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aVideoMaxRoamBandwidth.setStatus('current')
cLQd11bVoiceAdmCtrlSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bVoiceAdmCtrlSupport.setStatus('current')
cLQd11bVoiceMaxAdmBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bVoiceMaxAdmBandwidth.setStatus('current')
cLQd11bVoiceMaxRoamBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bVoiceMaxRoamBandwidth.setStatus('current')
cLQd11bVideoAdmCtrlSupport = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 4), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bVideoAdmCtrlSupport.setStatus('current')
cLQd11bVideoMaxAdmBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bVideoMaxAdmBandwidth.setStatus('current')
cLQd11bVideoMaxRoamBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bVideoMaxRoamBandwidth.setStatus('current')
cLQd11aGprProbeInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(10)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aGprProbeInterval.setStatus('current')
cLQd11aVoiceCtrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loadBased", 1), ("static", 2))).clone('loadBased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aVoiceCtrl.setStatus('current')
cLQd11aExpeditedBw = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aExpeditedBw.setStatus('current')
cLQd11aEdcaProfile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("wmmDefault", 1), ("svpVoice", 2), ("optimizedVoice", 3), ("optimizedVideoVoice", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aEdcaProfile.setStatus('current')
cLQd11aMacOptimization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aMacOptimization.setStatus('current')
cLQd11aMaxCallLimit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11aMaxCallLimit.setStatus('current')
cLQd11bGprProbeInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(10)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bGprProbeInterval.setStatus('current')
cLQd11bVoiceCtrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loadBased", 1), ("static", 2))).clone('loadBased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bVoiceCtrl.setStatus('current')
cLQd11bExpeditedBw = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bExpeditedBw.setStatus('current')
cLQd11bEdcaProfile = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("wmmDefault", 1), ("svpVoice", 2), ("optimizedVoice", 3), ("optimizedVideoVoice", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bEdcaProfile.setStatus('current')
cLQd11bMacOptimization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bMacOptimization.setStatus('current')
cLQd11bMaxCallLimit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 2, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11bMaxCallLimit.setStatus('current')
cLQd11GprTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1), )
if mibBuilder.loadTexts: cLQd11GprTable.setStatus('current')
cLQd11GprEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1, 1), )
cLWlanConfigEntry.registerAugmentions(("CISCO-LWAPP-QOS-MIB", "cLQd11GprEntry"))
cLQd11GprEntry.setIndexNames(*cLWlanConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cLQd11GprEntry.setStatus('current')
cLQd11GprSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 3, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11GprSupport.setStatus('current')
cLQd11CACStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1), )
if mibBuilder.loadTexts: cLQd11CACStatsTable.setStatus('current')
cLQd11CACStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1), )
cLApDot11IfEntry.registerAugmentions(("CISCO-LWAPP-QOS-MIB", "cLQd11CACStatsEntry"))
cLQd11CACStatsEntry.setIndexNames(*cLApDot11IfEntry.getIndexNames())
if mibBuilder.loadTexts: cLQd11CACStatsEntry.setStatus('current')
cLQd11CacVoiceBwInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacVoiceBwInUse.setStatus('current')
cLQd11CacVideoBwInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacVideoBwInUse.setStatus('current')
cLQd11CacVoiceCallsInProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacVoiceCallsInProgress.setStatus('current')
cLQd11CacRoamVoiceCallsInProg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacRoamVoiceCallsInProg.setStatus('current')
cLQd11CacTotalVoiceCallsAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacTotalVoiceCallsAP.setStatus('current')
cLQd11CacTotalRoamCallsAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacTotalRoamCallsAP.setStatus('current')
cLQd11CacVoiceCallsRejectedAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacVoiceCallsRejectedAP.setStatus('current')
cLQd11CacRoamCallsRejectedAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacRoamCallsRejectedAP.setStatus('current')
cLQd11CacRejCallsInsufBw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacRejCallsInsufBw.setStatus('current')
cLQd11CacRejCallsBadParams = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacRejCallsBadParams.setStatus('current')
cLQd11CacRejCallsPhyRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacRejCallsPhyRate.setStatus('current')
cLQd11CacRejCallsQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacRejCallsQosPolicy.setStatus('current')
cLQd11SipCacNonRoamCallsInProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacNonRoamCallsInProgress.setStatus('current')
cLQd11SipCacRoamCallsInProg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacRoamCallsInProg.setStatus('current')
cLQd11SipCacTotalNonRoamCallsAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacTotalNonRoamCallsAP.setStatus('current')
cLQd11SipCacTotalRoamCallsAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacTotalRoamCallsAP.setStatus('current')
cLQd11SipCacNonRoamCallsRejectedInSuffBw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacNonRoamCallsRejectedInSuffBw.setStatus('current')
cLQd11SipCacRoamCallsRejectedInSuffBw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacRoamCallsRejectedInSuffBw.setStatus('current')
cLQd11SipCacNonRoamCallsRejectedMaxLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacNonRoamCallsRejectedMaxLimit.setStatus('current')
cLQd11SipCacRoamCallsRejectedMaxLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacRoamCallsRejectedMaxLimit.setStatus('current')
cLQd11SipCacRejCallsQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 4, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11SipCacRejCallsQosPolicy.setStatus('current')
cLQd11VoiceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1), )
if mibBuilder.loadTexts: cLQd11VoiceStatsTable.setStatus('current')
cLQd11VoiceStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"), (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"))
if mibBuilder.loadTexts: cLQd11VoiceStatsEntry.setStatus('current')
cLQd11VoiceCallCounts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1, 1), Counter32()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11VoiceCallCounts.setStatus('current')
cLQd11CacVoiceCallTimePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 6, 1, 1, 2), TimeIntervalSec()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQd11CacVoiceCallTimePeriod.setStatus('current')
cLQVoiceWlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1), )
if mibBuilder.loadTexts: cLQVoiceWlanConfigTable.setStatus('current')
cLQVoiceWlanConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLQVoiceWlanConfigEntry.setStatus('current')
cLQVoiceWlanConfigDetectVoipCallFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 7, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQVoiceWlanConfigDetectVoipCallFailure.setStatus('current')
cLQVoiceClientTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1), )
if mibBuilder.loadTexts: cLQVoiceClientTable.setStatus('current')
cLQVoiceClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
if mibBuilder.loadTexts: cLQVoiceClientEntry.setStatus('current')
cLQVoiceClientCallingNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQVoiceClientCallingNumber.setStatus('current')
cLQVoiceClientLastCalledNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQVoiceClientLastCalledNumber.setStatus('current')
cLQVoiceClientLastCallFailureReasonCode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 413, 414, 415, 420, 480, 481, 482, 483, 484, 485, 486, 500, 501, 502, 503, 504, 505, 600, 603, 604, 606))).clone(namedValues=NamedValues(("unknown", 1), ("normalFailure", 2), ("roamFailure", 3), ("maxLimitExceeded", 4), ("badRequest", 400), ("unathorized", 401), ("paymentRequired", 402), ("forbidden", 403), ("notFound", 404), ("methodNotallowed", 405), ("notAcceptable", 406), ("proxyAuthenticationRequired", 407), ("requestTimeout", 408), ("conflict", 409), ("gone", 410), ("lengthRequired", 411), ("requestEntityTooLarge", 413), ("requestURITooLarge", 414), ("unsupportedMdediaType", 415), ("badExtension", 420), ("temporarilyNotAvailable", 480), ("callLegDoesNotExist", 481), ("loopDetected", 482), ("tooManyHops", 483), ("addressIncomplete", 484), ("ambiguous", 485), ("busy", 486), ("internalServerError", 500), ("notImplemented", 501), ("badGateway", 502), ("serviceUnavailable", 503), ("serverTimeout", 504), ("versionNotSupported", 505), ("busyEverywhere", 600), ("decline", 603), ("doesNotExistAnywhere", 604), ("sessionNotAcceptable", 606)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLQVoiceClientLastCallFailureReasonCode.setStatus('current')
cLQd11SipCacConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1), )
if mibBuilder.loadTexts: cLQd11SipCacConfigTable.setStatus('current')
cLQd11SipCacConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"))
if mibBuilder.loadTexts: cLQd11SipCacConfigEntry.setStatus('current')
cLQd11SipCacConfigCodecType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("userDefined", 1), ("g711", 2), ("g729", 3))).clone('g711')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11SipCacConfigCodecType.setStatus('current')
cLQd11SipCacConfigBw = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 2), Unsigned32()).setUnits('kbps').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11SipCacConfigBw.setStatus('current')
cLQd11SipCacConfigVoiceSampleSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 9, 1, 1, 3), Unsigned32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLQd11SipCacConfigVoiceSampleSize.setStatus('current')
ciscoLwappVoipCallFailureNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 524, 1, 10, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoLwappVoipCallFailureNotifEnabled.setStatus('current')
ciscoLwappVoipCallFailureNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 524, 0, 1)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCallFailureReasonCode"), ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientCallingNumber"), ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCalledNumber"), ("CISCO-LWAPP-AP-MIB", "cLApName"), ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"))
if mibBuilder.loadTexts: ciscoLwappVoipCallFailureNotif.setStatus('current')
ciscoLwappQosMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1))
ciscoLwappQosMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2))
ciscoLwappQosMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 1)).setObjects(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosMIBCompliance = ciscoLwappQosMIBCompliance.setStatus('deprecated')
ciscoLwappQosMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 2)).setObjects(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup1"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosMIBComplianceRev1 = ciscoLwappQosMIBComplianceRev1.setStatus('deprecated')
ciscoLwappQosMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 1, 3)).setObjects(("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11WlanConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11CacStatsGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup1"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup1"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11aConfigGroupSup2"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11bConfigGroupSup2"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipCacStatsGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11SipConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceStatsGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceConfigGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosDot11VoiceNotifGroup"), ("CISCO-LWAPP-QOS-MIB", "ciscoLwappQosConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosMIBComplianceRev2 = ciscoLwappQosMIBComplianceRev2.setStatus('current')
ciscoLwappQosDot11aConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 1)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceAdmCtrlSupport"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceMaxAdmBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceMaxRoamBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoAdmCtrlSupport"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoMaxAdmBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aVideoMaxRoamBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aGprProbeInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11aConfigGroup = ciscoLwappQosDot11aConfigGroup.setStatus('current')
ciscoLwappQosDot11bConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 2)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceAdmCtrlSupport"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceMaxAdmBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceMaxRoamBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoAdmCtrlSupport"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoMaxAdmBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bVideoMaxRoamBandwidth"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bGprProbeInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11bConfigGroup = ciscoLwappQosDot11bConfigGroup.setStatus('current')
ciscoLwappQosDot11WlanConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 3)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11GprSupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11WlanConfigGroup = ciscoLwappQosDot11WlanConfigGroup.setStatus('current')
ciscoLwappQosDot11CacStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 4)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceBwInUse"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVideoBwInUse"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallsInProgress"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRoamVoiceCallsInProg"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacTotalVoiceCallsAP"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacTotalRoamCallsAP"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallsRejectedAP"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRoamCallsRejectedAP"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsInsufBw"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsBadParams"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsPhyRate"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacRejCallsQosPolicy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11CacStatsGroup = ciscoLwappQosDot11CacStatsGroup.setStatus('current')
ciscoLwappQosDot11aConfigGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 5)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11aVoiceCtrl"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aExpeditedBw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11aConfigGroupSup1 = ciscoLwappQosDot11aConfigGroupSup1.setStatus('current')
ciscoLwappQosDot11bConfigGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 6)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11bVoiceCtrl"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bExpeditedBw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11bConfigGroupSup1 = ciscoLwappQosDot11bConfigGroupSup1.setStatus('current')
ciscoLwappQosDot11aConfigGroupSup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 7)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11aEdcaProfile"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aMacOptimization"), ("CISCO-LWAPP-QOS-MIB", "cLQd11aMaxCallLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11aConfigGroupSup2 = ciscoLwappQosDot11aConfigGroupSup2.setStatus('current')
ciscoLwappQosDot11bConfigGroupSup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 8)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11bEdcaProfile"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bMacOptimization"), ("CISCO-LWAPP-QOS-MIB", "cLQd11bMaxCallLimit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11bConfigGroupSup2 = ciscoLwappQosDot11bConfigGroupSup2.setStatus('current')
ciscoLwappQosDot11SipCacStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 9)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsInProgress"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsInProg"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacTotalNonRoamCallsAP"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacTotalRoamCallsAP"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsRejectedInSuffBw"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsRejectedInSuffBw"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacNonRoamCallsRejectedMaxLimit"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRoamCallsRejectedMaxLimit"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacRejCallsQosPolicy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11SipCacStatsGroup = ciscoLwappQosDot11SipCacStatsGroup.setStatus('current')
ciscoLwappQosDot11SipConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 10)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigCodecType"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigBw"), ("CISCO-LWAPP-QOS-MIB", "cLQd11SipCacConfigVoiceSampleSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11SipConfigGroup = ciscoLwappQosDot11SipConfigGroup.setStatus('current')
ciscoLwappQosDot11VoiceStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 11)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQd11VoiceCallCounts"), ("CISCO-LWAPP-QOS-MIB", "cLQd11CacVoiceCallTimePeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11VoiceStatsGroup = ciscoLwappQosDot11VoiceStatsGroup.setStatus('current')
ciscoLwappQosDot11VoiceConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 12)).setObjects(("CISCO-LWAPP-QOS-MIB", "cLQVoiceWlanConfigDetectVoipCallFailure"), ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientCallingNumber"), ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCalledNumber"), ("CISCO-LWAPP-QOS-MIB", "cLQVoiceClientLastCallFailureReasonCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11VoiceConfigGroup = ciscoLwappQosDot11VoiceConfigGroup.setStatus('current')
ciscoLwappQosDot11VoiceNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 13)).setObjects(("CISCO-LWAPP-QOS-MIB", "ciscoLwappVoipCallFailureNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosDot11VoiceNotifGroup = ciscoLwappQosDot11VoiceNotifGroup.setStatus('current')
ciscoLwappQosConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 524, 2, 2, 14)).setObjects(("CISCO-LWAPP-QOS-MIB", "ciscoLwappVoipCallFailureNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappQosConfigGroup = ciscoLwappQosConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-QOS-MIB", cLQd11bVoiceMaxAdmBandwidth=cLQd11bVoiceMaxAdmBandwidth, cLQVoiceWlanConfig=cLQVoiceWlanConfig, ciscoLwappQosMIBCompliance=ciscoLwappQosMIBCompliance, cLQVoiceWlanConfigDetectVoipCallFailure=cLQVoiceWlanConfigDetectVoipCallFailure, ciscoLwappQosDot11WlanConfigGroup=ciscoLwappQosDot11WlanConfigGroup, cLQd11aVoiceAdmCtrlSupport=cLQd11aVoiceAdmCtrlSupport, cLQd11SipCacRoamCallsRejectedMaxLimit=cLQd11SipCacRoamCallsRejectedMaxLimit, cLQd11CACStats=cLQd11CACStats, cLQVoiceWlanConfigTable=cLQVoiceWlanConfigTable, cLQd11aVoiceMaxRoamBandwidth=cLQd11aVoiceMaxRoamBandwidth, cLQd11bVoiceCtrl=cLQd11bVoiceCtrl, cLQd11bVoiceAdmCtrlSupport=cLQd11bVoiceAdmCtrlSupport, cLQd11CacRoamCallsRejectedAP=cLQd11CacRoamCallsRejectedAP, cLQd11SipCacTotalNonRoamCallsAP=cLQd11SipCacTotalNonRoamCallsAP, ciscoLwappQosDot11SipConfigGroup=ciscoLwappQosDot11SipConfigGroup, cLQd11bCACConfig=cLQd11bCACConfig, cLQd11aMaxCallLimit=cLQd11aMaxCallLimit, ciscoLwappQosMIBObjects=ciscoLwappQosMIBObjects, cLQd11CacVoiceCallTimePeriod=cLQd11CacVoiceCallTimePeriod, ciscoLwappQosMIBNotifs=ciscoLwappQosMIBNotifs, cLQd11VoiceCallCounts=cLQd11VoiceCallCounts, cLQd11bEdcaProfile=cLQd11bEdcaProfile, cLQd11aGprProbeInterval=cLQd11aGprProbeInterval, cLQd11GprEntry=cLQd11GprEntry, cLQd11bVideoAdmCtrlSupport=cLQd11bVideoAdmCtrlSupport, ciscoLwappQosDot11bConfigGroup=ciscoLwappQosDot11bConfigGroup, cLQVoiceWlanConfigEntry=cLQVoiceWlanConfigEntry, cLQd11aExpeditedBw=cLQd11aExpeditedBw, cLQd11CacRoamVoiceCallsInProg=cLQd11CacRoamVoiceCallsInProg, ciscoLwappQosDot11SipCacStatsGroup=ciscoLwappQosDot11SipCacStatsGroup, cLQd11SipCacRoamCallsRejectedInSuffBw=cLQd11SipCacRoamCallsRejectedInSuffBw, cLQd11SipCacConfigTable=cLQd11SipCacConfigTable, ciscoLwappQosMIBCompliances=ciscoLwappQosMIBCompliances, ciscoLwappQosMIBComplianceRev2=ciscoLwappQosMIBComplianceRev2, cLQd11bVideoMaxRoamBandwidth=cLQd11bVideoMaxRoamBandwidth, cLQd11CacVoiceCallsInProgress=cLQd11CacVoiceCallsInProgress, ciscoLwappQosConfigGroup=ciscoLwappQosConfigGroup, cLQd11CacRejCallsPhyRate=cLQd11CacRejCallsPhyRate, ciscoLwappQosMIB=ciscoLwappQosMIB, cLQd11VoiceStats=cLQd11VoiceStats, cLQd11CacTotalRoamCallsAP=cLQd11CacTotalRoamCallsAP, cLQd11SipCacConfig=cLQd11SipCacConfig, cLQd11bMacOptimization=cLQd11bMacOptimization, ciscoLwappQosDot11bConfigGroupSup2=ciscoLwappQosDot11bConfigGroupSup2, cLQVoiceClient=cLQVoiceClient, cLQd11SipCacRejCallsQosPolicy=cLQd11SipCacRejCallsQosPolicy, ciscoLwappQosDot11aConfigGroupSup2=ciscoLwappQosDot11aConfigGroupSup2, cLQd11bExpeditedBw=cLQd11bExpeditedBw, cLQd11SipCacConfigCodecType=cLQd11SipCacConfigCodecType, cLQd11bVideoMaxAdmBandwidth=cLQd11bVideoMaxAdmBandwidth, cLQVoiceClientTable=cLQVoiceClientTable, cLQd11SipCacConfigEntry=cLQd11SipCacConfigEntry, cLQd11aCACConfig=cLQd11aCACConfig, cLQd11SipCacRoamCallsInProg=cLQd11SipCacRoamCallsInProg, ciscoLwappVoipCallFailureNotif=ciscoLwappVoipCallFailureNotif, cLQConfigObjects=cLQConfigObjects, cLQd11aVoiceMaxAdmBandwidth=cLQd11aVoiceMaxAdmBandwidth, cLQd11GprTable=cLQd11GprTable, cLQd11CacVoiceCallsRejectedAP=cLQd11CacVoiceCallsRejectedAP, cLQd11SipCacConfigBw=cLQd11SipCacConfigBw, cLQd11CACStatsEntry=cLQd11CACStatsEntry, cLQd11bGprProbeInterval=cLQd11bGprProbeInterval, cLQd11SipCacNonRoamCallsRejectedInSuffBw=cLQd11SipCacNonRoamCallsRejectedInSuffBw, ciscoLwappQosDot11VoiceNotifGroup=ciscoLwappQosDot11VoiceNotifGroup, cLQd11bMaxCallLimit=cLQd11bMaxCallLimit, ciscoLwappQosDot11CacStatsGroup=ciscoLwappQosDot11CacStatsGroup, cLQd11aVideoMaxAdmBandwidth=cLQd11aVideoMaxAdmBandwidth, cLQd11SipCacNonRoamCallsRejectedMaxLimit=cLQd11SipCacNonRoamCallsRejectedMaxLimit, cLQVoiceClientLastCalledNumber=cLQVoiceClientLastCalledNumber, cLQd11GprSupport=cLQd11GprSupport, cLQd11SipCacNonRoamCallsInProgress=cLQd11SipCacNonRoamCallsInProgress, cLQVoiceClientCallingNumber=cLQVoiceClientCallingNumber, cLQd11aEdcaProfile=cLQd11aEdcaProfile, cLQd11aVoiceCtrl=cLQd11aVoiceCtrl, ciscoLwappVoipCallFailureNotifEnabled=ciscoLwappVoipCallFailureNotifEnabled, PYSNMP_MODULE_ID=ciscoLwappQosMIB, cLQd11CacRejCallsBadParams=cLQd11CacRejCallsBadParams, ciscoLwappQosDot11aConfigGroupSup1=ciscoLwappQosDot11aConfigGroupSup1, ciscoLwappQosDot11bConfigGroupSup1=ciscoLwappQosDot11bConfigGroupSup1, cLQd11VoiceStatsEntry=cLQd11VoiceStatsEntry, ciscoLwappQosMIBConform=ciscoLwappQosMIBConform, cLQd11CACStatsTable=cLQd11CACStatsTable, cLQd11CacRejCallsInsufBw=cLQd11CacRejCallsInsufBw, cLQVoiceClientEntry=cLQVoiceClientEntry, cLQd11bVoiceMaxRoamBandwidth=cLQd11bVoiceMaxRoamBandwidth, cLQd11aVideoMaxRoamBandwidth=cLQd11aVideoMaxRoamBandwidth, cLQd11GprConfig=cLQd11GprConfig, ciscoLwappQosMIBComplianceRev1=ciscoLwappQosMIBComplianceRev1, cLQd11CacVoiceBwInUse=cLQd11CacVoiceBwInUse, cLQd11CacVideoBwInUse=cLQd11CacVideoBwInUse, cLQd11aVideoAdmCtrlSupport=cLQd11aVideoAdmCtrlSupport, ciscoLwappQosDot11aConfigGroup=ciscoLwappQosDot11aConfigGroup, cLQVoiceClientLastCallFailureReasonCode=cLQVoiceClientLastCallFailureReasonCode, ciscoLwappQosDot11VoiceStatsGroup=ciscoLwappQosDot11VoiceStatsGroup, cLQd11CacRejCallsQosPolicy=cLQd11CacRejCallsQosPolicy, cLQEntConfConfig=cLQEntConfConfig, ciscoLwappQosDot11VoiceConfigGroup=ciscoLwappQosDot11VoiceConfigGroup, cLQd11SipCacConfigVoiceSampleSize=cLQd11SipCacConfigVoiceSampleSize, cLQd11CacTotalVoiceCallsAP=cLQd11CacTotalVoiceCallsAP, cLQd11SipCacTotalRoamCallsAP=cLQd11SipCacTotalRoamCallsAP, ciscoLwappQosMIBGroups=ciscoLwappQosMIBGroups, cLQd11aMacOptimization=cLQd11aMacOptimization, cLQd11VoiceStatsTable=cLQd11VoiceStatsTable)
