#
# PySNMP MIB module CISCO-COMPRESSION-SERVICE-ADAPTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COMPRESSION-SERVICE-ADAPTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cardIndex, = mibBuilder.importSymbols("OLD-CISCO-CHASSIS-MIB", "cardIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, MibIdentifier, Gauge32, Counter32, iso, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Gauge32", "Counter32", "iso", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "Integer32", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoCompressionServiceAdapterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 57))
if mibBuilder.loadTexts: ciscoCompressionServiceAdapterMIB.setLastUpdated('9608150000Z')
if mibBuilder.loadTexts: ciscoCompressionServiceAdapterMIB.setOrganization('Cisco Systems, Inc.')
ciscoCSAMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 57, 1))
csaStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1))
csaStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1), )
if mibBuilder.loadTexts: csaStatsTable.setStatus('current')
csaStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1), ).setIndexNames((0, "OLD-CISCO-CHASSIS-MIB", "cardIndex"))
if mibBuilder.loadTexts: csaStatsEntry.setStatus('current')
csaInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaInOctets.setStatus('current')
csaOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaOutOctets.setStatus('current')
csaInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaInPackets.setStatus('current')
csaOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaOutPackets.setStatus('current')
csaInPacketsDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaInPacketsDrop.setStatus('current')
csaOutPacketsDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaOutPacketsDrop.setStatus('current')
csaNumberOfRestarts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaNumberOfRestarts.setStatus('current')
csaCompressionRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaCompressionRatio.setStatus('current')
csaDecompressionRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csaDecompressionRatio.setStatus('current')
csaEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 57, 1, 1, 1, 1, 10), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaEnable.setStatus('current')
ciscoCSAMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 57, 3))
csaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 1))
csaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 2))
csaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 1, 1)).setObjects(("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaMIBCompliance = csaMIBCompliance.setStatus('current')
csaMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 57, 3, 2, 1)).setObjects(("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaInOctets"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaOutOctets"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaInPackets"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaOutPackets"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaInPacketsDrop"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaOutPacketsDrop"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaNumberOfRestarts"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaCompressionRatio"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaDecompressionRatio"), ("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", "csaEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaMIBGroup = csaMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-COMPRESSION-SERVICE-ADAPTER-MIB", ciscoCompressionServiceAdapterMIB=ciscoCompressionServiceAdapterMIB, csaOutPacketsDrop=csaOutPacketsDrop, csaStatsTable=csaStatsTable, csaInPacketsDrop=csaInPacketsDrop, csaNumberOfRestarts=csaNumberOfRestarts, csaMIBGroups=csaMIBGroups, csaStatsEntry=csaStatsEntry, csaInOctets=csaInOctets, csaEnable=csaEnable, csaMIBCompliance=csaMIBCompliance, ciscoCSAMIBConformance=ciscoCSAMIBConformance, csaDecompressionRatio=csaDecompressionRatio, csaMIBCompliances=csaMIBCompliances, ciscoCSAMIBObjects=ciscoCSAMIBObjects, csaCompressionRatio=csaCompressionRatio, csaOutOctets=csaOutOctets, csaOutPackets=csaOutPackets, csaStats=csaStats, csaMIBGroup=csaMIBGroup, PYSNMP_MODULE_ID=ciscoCompressionServiceAdapterMIB, csaInPackets=csaInPackets)
