#
# PySNMP MIB module HUAWEI-PIM-BSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-PIM-BSR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:35:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InetAddressPrefixLength, InetAddressType, InetZoneIndex, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddressType", "InetZoneIndex", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Bits, Integer32, Unsigned32, Counter64, iso, ObjectIdentity, MibIdentifier, Counter32, mib_2, NotificationType, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Integer32", "Unsigned32", "Counter64", "iso", "ObjectIdentity", "MibIdentifier", "Counter32", "mib-2", "NotificationType", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
hwMcast = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149))
hwPimBsrMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2))
hwPimBsrMib.setRevisions(('2007-04-16 00:00',))
if mibBuilder.loadTexts: hwPimBsrMib.setLastUpdated('200704160000Z')
if mibBuilder.loadTexts: hwPimBsrMib.setOrganization('Huawei Technologies co.,Ltd.')
hwPimBsrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1))
hwPimBsrConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2))
hwPimBsrCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 1))
hwPimBsrGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 2))
hwPimBsrElectedBsrRpSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2), )
if mibBuilder.loadTexts: hwPimBsrElectedBsrRpSetTable.setStatus('current')
hwPimBsrElectedBsrRpSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1), ).setIndexNames((0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingAddrType"), (0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingGrpAddr"), (0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingGrpPrefixLen"), (0, "HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrGrpMappingRPAddr"))
if mibBuilder.loadTexts: hwPimBsrElectedBsrRpSetEntry.setStatus('current')
hwPimBsrElectedBsrGrpMappingAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hwPimBsrElectedBsrGrpMappingAddrType.setStatus('current')
hwPimBsrElectedBsrGrpMappingGrpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 3), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: hwPimBsrElectedBsrGrpMappingGrpAddr.setStatus('current')
hwPimBsrElectedBsrGrpMappingGrpPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 4), InetAddressPrefixLength().subtype(subtypeSpec=ValueRangeConstraint(4, 128)))
if mibBuilder.loadTexts: hwPimBsrElectedBsrGrpMappingGrpPrefixLen.setStatus('current')
hwPimBsrElectedBsrGrpMappingRPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 5), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )))
if mibBuilder.loadTexts: hwPimBsrElectedBsrGrpMappingRPAddr.setStatus('current')
hwPimBsrElectedBsrRpSetPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPimBsrElectedBsrRpSetPriority.setStatus('current')
hwPimBsrElectedBsrRpSetHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPimBsrElectedBsrRpSetHoldtime.setStatus('current')
hwPimBsrElectedBsrRpSetExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPimBsrElectedBsrRpSetExpiryTime.setStatus('current')
hwPimBsrElectedBsrRpSetGrpBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPimBsrElectedBsrRpSetGrpBidir.setStatus('current')
hwPimBsrCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 1, 1)).setObjects(("HUAWEI-PIM-BSR-MIB", "hwPimBsrObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPimBsrCompliance = hwPimBsrCompliance.setStatus('current')
hwPimBsrObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 2, 2, 2, 1)).setObjects(("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetPriority"), ("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetHoldtime"), ("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetExpiryTime"), ("HUAWEI-PIM-BSR-MIB", "hwPimBsrElectedBsrRpSetGrpBidir"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPimBsrObjectGroup = hwPimBsrObjectGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-PIM-BSR-MIB", hwPimBsrElectedBsrGrpMappingAddrType=hwPimBsrElectedBsrGrpMappingAddrType, hwPimBsrElectedBsrGrpMappingRPAddr=hwPimBsrElectedBsrGrpMappingRPAddr, PYSNMP_MODULE_ID=hwPimBsrMib, hwPimBsrElectedBsrRpSetGrpBidir=hwPimBsrElectedBsrRpSetGrpBidir, hwPimBsrCompliances=hwPimBsrCompliances, hwPimBsrCompliance=hwPimBsrCompliance, hwMcast=hwMcast, hwPimBsrGroups=hwPimBsrGroups, hwPimBsrElectedBsrRpSetExpiryTime=hwPimBsrElectedBsrRpSetExpiryTime, hwPimBsrElectedBsrRpSetHoldtime=hwPimBsrElectedBsrRpSetHoldtime, hwPimBsrConformance=hwPimBsrConformance, hwPimBsrObjectGroup=hwPimBsrObjectGroup, hwPimBsrElectedBsrRpSetEntry=hwPimBsrElectedBsrRpSetEntry, hwPimBsrElectedBsrRpSetPriority=hwPimBsrElectedBsrRpSetPriority, hwPimBsrElectedBsrRpSetTable=hwPimBsrElectedBsrRpSetTable, hwPimBsrElectedBsrGrpMappingGrpAddr=hwPimBsrElectedBsrGrpMappingGrpAddr, hwPimBsrMib=hwPimBsrMib, hwPimBsrElectedBsrGrpMappingGrpPrefixLen=hwPimBsrElectedBsrGrpMappingGrpPrefixLen, hwPimBsrObjects=hwPimBsrObjects)
