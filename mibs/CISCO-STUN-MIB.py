#
# PySNMP MIB module CISCO-STUN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-STUN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, TimeTicks, Counter64, Counter32, Bits, iso, Integer32, NotificationType, Unsigned32, IpAddress, ModuleIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Counter64", "Counter32", "Bits", "iso", "Integer32", "NotificationType", "Unsigned32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoStunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 30))
ciscoStunMIB.setRevisions(('1995-08-21 00:00', '1995-03-17 00:00',))
if mibBuilder.loadTexts: ciscoStunMIB.setLastUpdated('9508210000Z')
if mibBuilder.loadTexts: ciscoStunMIB.setOrganization('Cisco Systems, Inc.')
stunObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1))
stunGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 1))
stunGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2))
stunPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3))
stunRoutes = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4))
stunIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunIPAddr.setStatus('current')
stunGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1), )
if mibBuilder.loadTexts: stunGroupTable.setStatus('current')
stunGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-STUN-MIB", "stunGroupIndex"))
if mibBuilder.loadTexts: stunGroupEntry.setStatus('current')
stunGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: stunGroupIndex.setStatus('current')
stunProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("basic", 1), ("sdlc", 2), ("sdlctg", 3), ("custom", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunProtocolType.setStatus('current')
stunPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1), )
if mibBuilder.loadTexts: stunPortTable.setStatus('current')
stunPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: stunPortEntry.setStatus('current')
stunPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortGroupIndex.setStatus('current')
stunPortDefaultPeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ip", 2), ("direct", 3), ("frameRelay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortDefaultPeerType.setStatus('current')
stunPortDefaultPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortDefaultPeerIP.setStatus('current')
stunPortDefaultPeerSerialInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunPortDefaultPeerSerialInterface.setStatus('current')
stunRouteTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1), )
if mibBuilder.loadTexts: stunRouteTable.setStatus('current')
stunRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-STUN-MIB", "stunGroupIndex"), (0, "CISCO-STUN-MIB", "stunRouteStationAddress"))
if mibBuilder.loadTexts: stunRouteEntry.setStatus('current')
stunRouteStationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: stunRouteStationAddress.setStatus('current')
stunRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ip", 2), ("direct", 3), ("frameRelay", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteType.setStatus('current')
stunRouteRemoteIP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteRemoteIP.setStatus('current')
stunRouteSerialInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteSerialInterface.setStatus('current')
stunRoutePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("low", 1), ("normal", 2), ("medium", 3), ("high", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRoutePriority.setStatus('current')
stunRoutePeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dead", 1), ("closed", 2), ("opening", 3), ("openWait", 4), ("connected", 5), ("direct", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRoutePeerState.setStatus('current')
stunRouteLocalAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteLocalAck.setStatus('current')
stunRouteRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteRxPackets.setStatus('current')
stunRouteTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteTxPackets.setStatus('current')
stunRouteRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteRxBytes.setStatus('current')
stunRouteTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stunRouteTxBytes.setStatus('current')
stunNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 2))
stunNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 2, 0))
stunPeerStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 30, 2, 0, 1)).setObjects(("CISCO-STUN-MIB", "stunRoutePeerState"))
if mibBuilder.loadTexts: stunPeerStateChangeNotification.setStatus('current')
stunMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 3))
stunMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 1))
stunMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2))
stunMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 1, 1)).setObjects(("CISCO-STUN-MIB", "stunGlobalGroup"), ("CISCO-STUN-MIB", "stunGroupGroup"), ("CISCO-STUN-MIB", "stunPortGroup"), ("CISCO-STUN-MIB", "stunRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunMibCompliance = stunMibCompliance.setStatus('current')
stunGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 1)).setObjects(("CISCO-STUN-MIB", "stunIPAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunGlobalGroup = stunGlobalGroup.setStatus('current')
stunGroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 2)).setObjects(("CISCO-STUN-MIB", "stunProtocolType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunGroupGroup = stunGroupGroup.setStatus('current')
stunPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 3)).setObjects(("CISCO-STUN-MIB", "stunPortGroupIndex"), ("CISCO-STUN-MIB", "stunPortDefaultPeerType"), ("CISCO-STUN-MIB", "stunPortDefaultPeerIP"), ("CISCO-STUN-MIB", "stunPortDefaultPeerSerialInterface"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunPortGroup = stunPortGroup.setStatus('current')
stunRouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 4)).setObjects(("CISCO-STUN-MIB", "stunRouteType"), ("CISCO-STUN-MIB", "stunRouteRemoteIP"), ("CISCO-STUN-MIB", "stunRouteSerialInterface"), ("CISCO-STUN-MIB", "stunRoutePriority"), ("CISCO-STUN-MIB", "stunRoutePeerState"), ("CISCO-STUN-MIB", "stunRouteLocalAck"), ("CISCO-STUN-MIB", "stunRouteRxPackets"), ("CISCO-STUN-MIB", "stunRouteTxPackets"), ("CISCO-STUN-MIB", "stunRouteRxBytes"), ("CISCO-STUN-MIB", "stunRouteTxBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    stunRouteGroup = stunRouteGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-STUN-MIB", stunRouteRxBytes=stunRouteRxBytes, PYSNMP_MODULE_ID=ciscoStunMIB, stunRouteRemoteIP=stunRouteRemoteIP, stunGroupEntry=stunGroupEntry, stunPortTable=stunPortTable, stunRouteType=stunRouteType, stunRouteRxPackets=stunRouteRxPackets, stunRouteSerialInterface=stunRouteSerialInterface, stunPortEntry=stunPortEntry, stunProtocolType=stunProtocolType, stunPortGroup=stunPortGroup, stunPorts=stunPorts, stunRouteLocalAck=stunRouteLocalAck, stunNotifications=stunNotifications, stunRoutePriority=stunRoutePriority, stunMibGroups=stunMibGroups, stunGroupIndex=stunGroupIndex, stunMibConformance=stunMibConformance, stunGroups=stunGroups, stunRoutePeerState=stunRoutePeerState, stunRouteTxPackets=stunRouteTxPackets, stunRouteGroup=stunRouteGroup, stunObjects=stunObjects, stunGlobal=stunGlobal, stunPortDefaultPeerType=stunPortDefaultPeerType, stunIPAddr=stunIPAddr, stunRouteEntry=stunRouteEntry, stunPortDefaultPeerIP=stunPortDefaultPeerIP, stunGroupGroup=stunGroupGroup, ciscoStunMIB=ciscoStunMIB, stunPortDefaultPeerSerialInterface=stunPortDefaultPeerSerialInterface, stunGroupTable=stunGroupTable, stunRouteStationAddress=stunRouteStationAddress, stunRouteTxBytes=stunRouteTxBytes, stunPeerStateChangeNotification=stunPeerStateChangeNotification, stunGlobalGroup=stunGlobalGroup, stunMibCompliances=stunMibCompliances, stunRouteTable=stunRouteTable, stunRoutes=stunRoutes, stunPortGroupIndex=stunPortGroupIndex, stunNotificationPrefix=stunNotificationPrefix, stunMibCompliance=stunMibCompliance)
