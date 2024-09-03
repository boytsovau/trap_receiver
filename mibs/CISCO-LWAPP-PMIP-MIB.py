#
# PySNMP MIB module CISCO-LWAPP-PMIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-PMIP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cldcClientMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, ObjectIdentity, iso, NotificationType, Counter32, Gauge32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ModuleIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "iso", "NotificationType", "Counter32", "Gauge32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ModuleIdentity", "TimeTicks", "Unsigned32")
RowStatus, TimeStamp, DisplayString, TruthValue, TextualConvention, MacAddress, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "DisplayString", "TruthValue", "TextualConvention", "MacAddress", "TimeInterval")
ciscoLwappPmipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 888))
ciscoLwappPmipMIB.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: ciscoLwappPmipMIB.setLastUpdated('201112220000Z')
if mibBuilder.loadTexts: ciscoLwappPmipMIB.setOrganization('Cisco Systems Inc.')
ciscoLwappPmipMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0))
ciscoLwappPmipGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1))
ciscoLwappPmipConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2))
ciscoLwappPmipStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3))
cLPmipDomainName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipDomainName.setStatus('current')
cLPmipMAGInterface = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipMAGInterface.setStatus('current')
cLPmipMaxBindings = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipMaxBindings.setStatus('current')
cLPmipBindingLifeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 4), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingLifeTime.setStatus('current')
cLPmipBindingRefreshTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 5), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingRefreshTime.setStatus('current')
cLPmipBindingInitRetxTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 6), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingInitRetxTime.setStatus('current')
cLPmipBindingMaxRetxTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 7), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBindingMaxRetxTime.setStatus('current')
cLPmipReplayProtectionTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 8), TimeStamp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipReplayProtectionTimestamp.setStatus('current')
cLPmipBriMinDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 9), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBriMinDelayTime.setStatus('current')
cLPmipBriMaxDelayTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBriMaxDelayTime.setStatus('current')
cLPmipBriRetries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipBriRetries.setStatus('current')
cLPmipMagApnName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 12), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipMagApnName.setStatus('current')
cLPmipLmaTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1), )
if mibBuilder.loadTexts: cLPmipLmaTable.setStatus('current')
cLPmipLmaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipLmaName"))
if mibBuilder.loadTexts: cLPmipLmaEntry.setStatus('current')
cLPmipLmaName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaName.setStatus('current')
cLPmipLmaIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaIPAddrType.setStatus('current')
cLPmipLmaIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaIPAddr.setStatus('current')
cLPmipLmaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipLmaRowStatus.setStatus('current')
cLPmipLmaStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1), )
if mibBuilder.loadTexts: cLPmipLmaStatsTable.setStatus('current')
cLPmipLmaStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipLmaName"))
if mibBuilder.loadTexts: cLPmipLmaStatsEntry.setStatus('current')
cLPmipLmaTotalBindings = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaTotalBindings.setStatus('current')
cLPmipLmaPbuSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbuSent.setStatus('current')
cLPmipLmaPbaReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbaReceived.setStatus('current')
cLPmipLmaPbriSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbriSent.setStatus('current')
cLPmipLmaPbriReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbriReceived.setStatus('current')
cLPmipLmaPbraSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbraSent.setStatus('current')
cLPmipLmaPbraReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 7), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbraReceived.setStatus('current')
cLPmipLmaNoOfHandoff = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 8), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaNoOfHandoff.setStatus('current')
cLPmipLmaPbuDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 9), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipLmaPbuDropped.setStatus('current')
cLPmipProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2), )
if mibBuilder.loadTexts: cLPmipProfileTable.setStatus('current')
cLPmipProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileName"))
if mibBuilder.loadTexts: cLPmipProfileEntry.setStatus('current')
cLPmipProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipProfileName.setStatus('current')
cLPmipProfileNaiTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3), )
if mibBuilder.loadTexts: cLPmipProfileNaiTable.setStatus('current')
cLPmipProfileNaiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1), ).setIndexNames((0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileName"), (0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileNai"))
if mibBuilder.loadTexts: cLPmipProfileNaiEntry.setStatus('current')
cLPmipProfileNai = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileNai.setStatus('current')
cLPmipProfileApn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileApn.setStatus('current')
cLPmipProfileLmaName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileLmaName.setStatus('current')
cLPmipProfileNaiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLPmipProfileNaiRowStatus.setStatus('current')
cLPmipWlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4), )
if mibBuilder.loadTexts: cLPmipWlanTable.setStatus('current')
cLPmipWlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLPmipWlanEntry.setStatus('current')
cLPmipWlanProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 1), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipWlanProfileName.setStatus('current')
cLPmipWlanMobilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("pmipv6", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipWlanMobilityType.setStatus('current')
cLPmipWlanDefaultRealm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLPmipWlanDefaultRealm.setStatus('current')
cLPmipClientInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2), )
if mibBuilder.loadTexts: cLPmipClientInfoTable.setStatus('current')
cLPmipClientInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
if mibBuilder.loadTexts: cLPmipClientInfoEntry.setStatus('current')
cLPmipClientNai = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientNai.setStatus('current')
cLPmipClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientState.setStatus('current')
cLPmipClientInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientInterface.setStatus('current')
cLPmipClientHomeAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientHomeAddressType.setStatus('current')
cLPmipClientHomeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientHomeAddress.setStatus('current')
cLPmipClientAtt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("reserved", 0), ("logicalNetworkInterface", 1), ("pointToPointInterface", 2), ("ethernet", 3), ("wirelessLan", 4), ("wimax", 5), ("threeGPPGERAN", 6), ("threeGPPUTRAN", 7), ("threeGPPETRAN", 8), ("threeGPP2eHRPD", 9), ("threeGPP2HRPD", 10), ("threeGPP21xRTT", 11), ("threeGPP2UMB", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientAtt.setStatus('current')
cLPmipClientLocalLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientLocalLinkId.setStatus('current')
cLPmipClientLmaName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientLmaName.setStatus('current')
cLPmipClientLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientLifeTime.setStatus('current')
cLPmipClientDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientDomainName.setStatus('current')
cLPmipClientUpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientUpKey.setStatus('current')
cLPmipClientDownKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLPmipClientDownKey.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-PMIP-MIB", cLPmipLmaPbuSent=cLPmipLmaPbuSent, cLPmipBindingLifeTime=cLPmipBindingLifeTime, cLPmipLmaStatsTable=cLPmipLmaStatsTable, cLPmipWlanMobilityType=cLPmipWlanMobilityType, cLPmipReplayProtectionTimestamp=cLPmipReplayProtectionTimestamp, cLPmipLmaTotalBindings=cLPmipLmaTotalBindings, ciscoLwappPmipGlobal=ciscoLwappPmipGlobal, cLPmipLmaName=cLPmipLmaName, cLPmipProfileNaiRowStatus=cLPmipProfileNaiRowStatus, cLPmipClientDownKey=cLPmipClientDownKey, cLPmipBriMaxDelayTime=cLPmipBriMaxDelayTime, cLPmipLmaPbriReceived=cLPmipLmaPbriReceived, cLPmipClientInfoEntry=cLPmipClientInfoEntry, cLPmipLmaStatsEntry=cLPmipLmaStatsEntry, cLPmipProfileApn=cLPmipProfileApn, cLPmipBindingMaxRetxTime=cLPmipBindingMaxRetxTime, cLPmipClientDomainName=cLPmipClientDomainName, cLPmipLmaRowStatus=cLPmipLmaRowStatus, cLPmipLmaPbuDropped=cLPmipLmaPbuDropped, cLPmipClientAtt=cLPmipClientAtt, cLPmipBindingRefreshTime=cLPmipBindingRefreshTime, cLPmipLmaNoOfHandoff=cLPmipLmaNoOfHandoff, cLPmipDomainName=cLPmipDomainName, cLPmipLmaPbaReceived=cLPmipLmaPbaReceived, cLPmipBindingInitRetxTime=cLPmipBindingInitRetxTime, cLPmipWlanDefaultRealm=cLPmipWlanDefaultRealm, cLPmipWlanProfileName=cLPmipWlanProfileName, cLPmipClientUpKey=cLPmipClientUpKey, cLPmipClientState=cLPmipClientState, cLPmipLmaIPAddrType=cLPmipLmaIPAddrType, cLPmipProfileName=cLPmipProfileName, cLPmipLmaPbraSent=cLPmipLmaPbraSent, cLPmipBriMinDelayTime=cLPmipBriMinDelayTime, cLPmipClientLifeTime=cLPmipClientLifeTime, cLPmipClientLocalLinkId=cLPmipClientLocalLinkId, ciscoLwappPmipMIBObjects=ciscoLwappPmipMIBObjects, cLPmipWlanTable=cLPmipWlanTable, cLPmipProfileEntry=cLPmipProfileEntry, cLPmipClientHomeAddress=cLPmipClientHomeAddress, ciscoLwappPmipConfig=ciscoLwappPmipConfig, PYSNMP_MODULE_ID=ciscoLwappPmipMIB, cLPmipClientLmaName=cLPmipClientLmaName, cLPmipLmaIPAddr=cLPmipLmaIPAddr, cLPmipClientInfoTable=cLPmipClientInfoTable, cLPmipProfileNaiEntry=cLPmipProfileNaiEntry, cLPmipWlanEntry=cLPmipWlanEntry, cLPmipMaxBindings=cLPmipMaxBindings, cLPmipBriRetries=cLPmipBriRetries, cLPmipLmaEntry=cLPmipLmaEntry, cLPmipLmaPbriSent=cLPmipLmaPbriSent, cLPmipProfileNaiTable=cLPmipProfileNaiTable, cLPmipMagApnName=cLPmipMagApnName, cLPmipProfileNai=cLPmipProfileNai, cLPmipProfileLmaName=cLPmipProfileLmaName, cLPmipClientInterface=cLPmipClientInterface, cLPmipLmaTable=cLPmipLmaTable, cLPmipClientNai=cLPmipClientNai, ciscoLwappPmipMIB=ciscoLwappPmipMIB, cLPmipMAGInterface=cLPmipMAGInterface, cLPmipProfileTable=cLPmipProfileTable, ciscoLwappPmipStatistics=ciscoLwappPmipStatistics, cLPmipLmaPbraReceived=cLPmipLmaPbraReceived, cLPmipClientHomeAddressType=cLPmipClientHomeAddressType)
