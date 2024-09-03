#
# PySNMP MIB module CISCO-802-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-802-TAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Bits, MibIdentifier, NotificationType, ModuleIdentity, iso, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "NotificationType", "ModuleIdentity", "iso", "Gauge32", "Counter32")
DisplayString, RowStatus, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "MacAddress")
cisco802TapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 395))
cisco802TapMIB.setRevisions(('2004-03-11 00:00',))
if mibBuilder.loadTexts: cisco802TapMIB.setLastUpdated('200403110000Z')
if mibBuilder.loadTexts: cisco802TapMIB.setOrganization('Cisco Systems, Inc.')
cisco802TapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 395, 0))
cisco802TapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 395, 1))
cisco802TapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 395, 2))
c802tapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1))
c802tapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("dstMacAddr", 2), ("srcMacAddr", 3), ("ethernetPid", 4), ("dstLlcSap", 5), ("srcLlcSap", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: c802tapStreamCapabilities.setStatus('current')
c802tapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2), )
if mibBuilder.loadTexts: c802tapStreamTable.setStatus('current')
c802tapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: c802tapStreamEntry.setStatus('current')
c802tapStreamFields = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 1), Bits().clone(namedValues=NamedValues(("interface", 0), ("dstMacAddress", 1), ("srcMacAddress", 2), ("ethernetPid", 3), ("dstLlcSap", 4), ("srcLlcSap", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamFields.setStatus('current')
c802tapStreamInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamInterface.setStatus('current')
c802tapStreamDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamDestinationAddress.setStatus('current')
c802tapStreamSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamSourceAddress.setStatus('current')
c802tapStreamEthernetPid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamEthernetPid.setStatus('current')
c802tapStreamDestinationLlcSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamDestinationLlcSap.setStatus('current')
c802tapStreamSourceLlcSap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamSourceLlcSap.setStatus('current')
c802tapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 395, 1, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: c802tapStreamStatus.setStatus('current')
cisco802TapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 1))
cisco802TapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 2))
cisco802TapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 1, 1)).setObjects(("CISCO-802-TAP-MIB", "cisco802TapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisco802TapMIBCompliance = cisco802TapMIBCompliance.setStatus('current')
cisco802TapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 395, 2, 2, 1)).setObjects(("CISCO-802-TAP-MIB", "c802tapStreamCapabilities"), ("CISCO-802-TAP-MIB", "c802tapStreamFields"), ("CISCO-802-TAP-MIB", "c802tapStreamInterface"), ("CISCO-802-TAP-MIB", "c802tapStreamDestinationAddress"), ("CISCO-802-TAP-MIB", "c802tapStreamSourceAddress"), ("CISCO-802-TAP-MIB", "c802tapStreamEthernetPid"), ("CISCO-802-TAP-MIB", "c802tapStreamSourceLlcSap"), ("CISCO-802-TAP-MIB", "c802tapStreamDestinationLlcSap"), ("CISCO-802-TAP-MIB", "c802tapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cisco802TapStreamGroup = cisco802TapStreamGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-802-TAP-MIB", cisco802TapMIBCompliances=cisco802TapMIBCompliances, c802tapStreamEncodePacket=c802tapStreamEncodePacket, cisco802TapMIBCompliance=cisco802TapMIBCompliance, cisco802TapMIB=cisco802TapMIB, cisco802TapMIBGroups=cisco802TapMIBGroups, c802tapStreamCapabilities=c802tapStreamCapabilities, c802tapStreamStatus=c802tapStreamStatus, c802tapStreamSourceAddress=c802tapStreamSourceAddress, cisco802TapMIBObjects=cisco802TapMIBObjects, c802tapStreamEntry=c802tapStreamEntry, c802tapStreamInterface=c802tapStreamInterface, PYSNMP_MODULE_ID=cisco802TapMIB, cisco802TapMIBNotifs=cisco802TapMIBNotifs, c802tapStreamSourceLlcSap=c802tapStreamSourceLlcSap, c802tapStreamDestinationAddress=c802tapStreamDestinationAddress, cisco802TapStreamGroup=cisco802TapStreamGroup, c802tapStreamTable=c802tapStreamTable, c802tapStreamFields=c802tapStreamFields, c802tapStreamEthernetPid=c802tapStreamEthernetPid, cisco802TapMIBConform=cisco802TapMIBConform, c802tapStreamDestinationLlcSap=c802tapStreamDestinationLlcSap)
