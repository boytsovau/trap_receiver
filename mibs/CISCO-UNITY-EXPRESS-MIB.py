#
# PySNMP MIB module CISCO-UNITY-EXPRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNITY-EXPRESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:01:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, IpAddress, iso, Bits, Counter64, MibIdentifier, ObjectIdentity, NotificationType, Integer32, Counter32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "IpAddress", "iso", "Bits", "Counter64", "MibIdentifier", "ObjectIdentity", "NotificationType", "Integer32", "Counter32", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime", "TruthValue")
ciscoUnityExpressMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 420))
ciscoUnityExpressMIB.setRevisions(('2007-01-08 00:00', '2005-09-02 00:00',))
if mibBuilder.loadTexts: ciscoUnityExpressMIB.setLastUpdated('200509020000Z')
if mibBuilder.loadTexts: ciscoUnityExpressMIB.setOrganization('Cisco Systems, Inc.')
ciscoUnityExpressMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 0))
ciscoUnityExpressMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1))
ciscoUnityExpressMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 2))
cueSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1))
cueSystemControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 1))
cueShutdownRequest = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueShutdownRequest.setStatus('current')
cueSystemScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2))
cueAVTNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueAVTNumber.setStatus('current')
cueVoicemailNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueVoicemailNumber.setStatus('current')
cueAANumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueAANumber.setStatus('current')
cueHardwareModuleType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("aim", 1), ("nm", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueHardwareModuleType.setStatus('deprecated')
cueCallControlAgentType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ccm", 1), ("ccme", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueCallControlAgentType.setStatus('current')
cueSIPInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3))
cueSIPGatewayName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueSIPGatewayName.setStatus('current')
cueSIPGatewayIPType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueSIPGatewayIPType.setStatus('current')
cueSIPGatewayIP = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueSIPGatewayIP.setStatus('current')
cueSIPPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 4), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueSIPPort.setStatus('current')
cueJTAPIInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4))
cueJTAPIServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1), )
if mibBuilder.loadTexts: cueJTAPIServerTable.setStatus('current')
cueJTAPIServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIndex"))
if mibBuilder.loadTexts: cueJTAPIServerEntry.setStatus('current')
cueJTAPIServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cueJTAPIServerIndex.setStatus('current')
cueJTAPIServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueJTAPIServerName.setStatus('current')
cueJTAPIServerIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueJTAPIServerIPType.setStatus('current')
cueJTAPIServerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueJTAPIServerIP.setStatus('current')
cueJTAPISubsystemState = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("initializing", 2), ("inService", 3), ("outOfService", 4), ("shuttingDown", 5), ("shutDown", 6), ("partialService", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueJTAPISubsystemState.setStatus('current')
cueJTAPIUsername = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueJTAPIUsername.setStatus('current')
cueJTAPISoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueJTAPISoftwareVersion.setStatus('current')
cueJTAPIPortsRegistered = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueJTAPIPortsRegistered.setStatus('current')
cueSystemDefaults = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5))
cueDefaultMailboxSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueDefaultMailboxSize.setStatus('current')
cueDefaultGreetingSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueDefaultGreetingSize.setStatus('current')
cueDefaultMessageSizeMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueDefaultMessageSizeMax.setStatus('current')
cueDefaultMessageExpiryTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('days').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueDefaultMessageExpiryTime.setStatus('current')
cueUsage = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2))
cueUsageScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1))
cueLicensedPortsMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueLicensedPortsMax.setStatus('current')
cueActiveCalls = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueActiveCalls.setStatus('current')
cuePersonalMailboxes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePersonalMailboxes.setStatus('current')
cueGeneralDeliveryMailboxes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueGeneralDeliveryMailboxes.setStatus('current')
cueOrphanedMailboxes = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueOrphanedMailboxes.setStatus('current')
cueCapacityOfVoicemail = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueCapacityOfVoicemail.setStatus('current')
cueAllocatedCapacity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueAllocatedCapacity.setStatus('current')
cueTotalTimeUsed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueTotalTimeUsed.setStatus('current')
cuePercentTimeUsed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePercentTimeUsed.setStatus('current')
cueMessageTimeUsed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMessageTimeUsed.setStatus('current')
cueMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMessageCount.setStatus('current')
cueAverageMessageLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueAverageMessageLength.setStatus('current')
cueGreetingTimeUsed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueGreetingTimeUsed.setStatus('current')
cueGreetingCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 14), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueGreetingCount.setStatus('current')
cueAverageGreetingLength = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 15), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueAverageGreetingLength.setStatus('current')
cueMessagesLeft = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMessagesLeft.setStatus('current')
cueMessagesRetrieved = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMessagesRetrieved.setStatus('current')
cueMessagesDeleted = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMessagesDeleted.setStatus('current')
cueLicensedMailboxesMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueLicensedMailboxesMax.setStatus('current')
cueMailboxesAbove90PercentFull = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMailboxesAbove90PercentFull.setStatus('current')
cueMboxTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2), )
if mibBuilder.loadTexts: cueMboxTable.setStatus('current')
cueMboxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-UNITY-EXPRESS-MIB", "cueMboxIndex"))
if mibBuilder.loadTexts: cueMboxEntry.setStatus('current')
cueMboxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cueMboxIndex.setStatus('current')
cueMboxOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxOwner.setStatus('current')
cueMboxPrimaryExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxPrimaryExtension.setStatus('current')
cueMboxType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("personal", 1), ("generalDelivery", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxType.setStatus('current')
cueMboxDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxDescription.setStatus('current')
cueMboxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxSize.setStatus('current')
cueMboxTimeUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxTimeUsed.setStatus('current')
cueMboxPercentTimeUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxPercentTimeUsed.setStatus('current')
cueMboxNumberOfMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 9), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxNumberOfMessages.setStatus('current')
cueMboxNumberOfNewMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 10), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxNumberOfNewMessages.setStatus('current')
cueMboxNumberOfSavedMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 11), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxNumberOfSavedMessages.setStatus('current')
cueMboxMessageSizeMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxMessageSizeMax.setStatus('current')
cueMboxMessageExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('days').setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxMessageExpiryTime.setStatus('current')
cueMboxPlayTutorial = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxPlayTutorial.setStatus('current')
cueMboxGreetingType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("alternate", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxGreetingType.setStatus('current')
cueMboxEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxEnabled.setStatus('current')
cueMboxBusy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxBusy.setStatus('current')
cueMboxMWIState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueMboxMWIState.setStatus('current')
cueSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3))
cueLoginInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1))
cueLoginAttempts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueLoginAttempts.setStatus('current')
cueLoginUsernameFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueLoginUsernameFailures.setStatus('current')
cueLoginPasswordFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueLoginPasswordFailures.setStatus('current')
cuePINInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2))
cuePINAttempts = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePINAttempts.setStatus('current')
cuePINResets = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePINResets.setStatus('current')
cuePINUidFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePINUidFailures.setStatus('current')
cuePINPasswordFailures = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePINPasswordFailures.setStatus('current')
cueNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4))
cueNotifConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 1))
cueNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cueNotifEnable.setStatus('current')
cueNotifInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2))
cueNotifSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("error", 1), ("warning", 2), ("informational", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cueNotifSeverity.setStatus('current')
cueNotifDate = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 2), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cueNotifDate.setStatus('current')
cueNotifDescription = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 3), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cueNotifDescription.setStatus('current')
cueNotifDetail = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 4), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cueNotifDetail.setStatus('current')
cueNotifSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3))
cueLoginUsernameThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueLoginUsernameThresh.setStatus('current')
cueLoginPasswordThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueLoginPasswordThresh.setStatus('current')
cuePINUidThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePINUidThresh.setStatus('current')
cuePINPasswordThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePINPasswordThresh.setStatus('current')
cuePINResetThresh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cuePINResetThresh.setStatus('current')
cueBackupRestore = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5))
cueBRHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1), )
if mibBuilder.loadTexts: cueBRHistoryTable.setStatus('current')
cueBRHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryIndex"))
if mibBuilder.loadTexts: cueBRHistoryEntry.setStatus('current')
cueBRHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cueBRHistoryIndex.setStatus('current')
cueBRHistoryOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("restore", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueBRHistoryOperation.setStatus('current')
cueBRHistoryDate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueBRHistoryDate.setStatus('current')
cueBRHistoryResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("success", 1), ("failure", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cueBRHistoryResult.setStatus('current')
ciscoUnityExpressApplAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 1)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
if mibBuilder.loadTexts: ciscoUnityExpressApplAlert.setStatus('current')
ciscoUnityExpressStorageAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 2)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
if mibBuilder.loadTexts: ciscoUnityExpressStorageAlert.setStatus('current')
ciscoUnityExpressSecurityAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 3)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
if mibBuilder.loadTexts: ciscoUnityExpressSecurityAlert.setStatus('current')
ciscoUnityExpressCallMgrAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 4)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
if mibBuilder.loadTexts: ciscoUnityExpressCallMgrAlert.setStatus('current')
ciscoUnityExpressRescExhausted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 5)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
if mibBuilder.loadTexts: ciscoUnityExpressRescExhausted.setStatus('current')
ciscoUnityExpressBackupAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 6)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
if mibBuilder.loadTexts: ciscoUnityExpressBackupAlert.setStatus('current')
ciscoUnityExpressNTPAlert = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 7)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
if mibBuilder.loadTexts: ciscoUnityExpressNTPAlert.setStatus('current')
ciscoUnityExpressMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 1))
ciscoUnityExpressMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2))
ciscoUnityExpressMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 1, 1)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueSystemGroup"), ("CISCO-UNITY-EXPRESS-MIB", "cueUsageGroup"), ("CISCO-UNITY-EXPRESS-MIB", "cueSecurityGroup"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifGroup"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressMIBNotificationsGroup"), ("CISCO-UNITY-EXPRESS-MIB", "cueBackupRestoreGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityExpressMIBCompliance = ciscoUnityExpressMIBCompliance.setStatus('current')
ciscoUnityExpressMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 1, 2)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueSystemGroupRev1"), ("CISCO-UNITY-EXPRESS-MIB", "cueUsageGroup"), ("CISCO-UNITY-EXPRESS-MIB", "cueSecurityGroup"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifGroup"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressMIBNotificationsGroup"), ("CISCO-UNITY-EXPRESS-MIB", "cueBackupRestoreGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityExpressMIBComplianceRev1 = ciscoUnityExpressMIBComplianceRev1.setStatus('current')
cueSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 1)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueShutdownRequest"), ("CISCO-UNITY-EXPRESS-MIB", "cueAVTNumber"), ("CISCO-UNITY-EXPRESS-MIB", "cueVoicemailNumber"), ("CISCO-UNITY-EXPRESS-MIB", "cueAANumber"), ("CISCO-UNITY-EXPRESS-MIB", "cueHardwareModuleType"), ("CISCO-UNITY-EXPRESS-MIB", "cueCallControlAgentType"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayName"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIPType"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIP"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPPort"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerName"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIPType"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIP"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISubsystemState"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIUsername"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISoftwareVersion"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIPortsRegistered"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMailboxSize"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultGreetingSize"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageSizeMax"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cueSystemGroup = cueSystemGroup.setStatus('deprecated')
cueUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 2)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueLicensedPortsMax"), ("CISCO-UNITY-EXPRESS-MIB", "cueActiveCalls"), ("CISCO-UNITY-EXPRESS-MIB", "cuePersonalMailboxes"), ("CISCO-UNITY-EXPRESS-MIB", "cueGeneralDeliveryMailboxes"), ("CISCO-UNITY-EXPRESS-MIB", "cueOrphanedMailboxes"), ("CISCO-UNITY-EXPRESS-MIB", "cueCapacityOfVoicemail"), ("CISCO-UNITY-EXPRESS-MIB", "cueAllocatedCapacity"), ("CISCO-UNITY-EXPRESS-MIB", "cueTotalTimeUsed"), ("CISCO-UNITY-EXPRESS-MIB", "cuePercentTimeUsed"), ("CISCO-UNITY-EXPRESS-MIB", "cueMessageTimeUsed"), ("CISCO-UNITY-EXPRESS-MIB", "cueMessageCount"), ("CISCO-UNITY-EXPRESS-MIB", "cueAverageMessageLength"), ("CISCO-UNITY-EXPRESS-MIB", "cueGreetingTimeUsed"), ("CISCO-UNITY-EXPRESS-MIB", "cueGreetingCount"), ("CISCO-UNITY-EXPRESS-MIB", "cueAverageGreetingLength"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxOwner"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxPrimaryExtension"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxType"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxSize"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxTimeUsed"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxPercentTimeUsed"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxNumberOfMessages"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxNumberOfNewMessages"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxNumberOfSavedMessages"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxMessageSizeMax"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxMessageExpiryTime"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxPlayTutorial"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxGreetingType"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxEnabled"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxBusy"), ("CISCO-UNITY-EXPRESS-MIB", "cueMboxMWIState"), ("CISCO-UNITY-EXPRESS-MIB", "cueMessagesLeft"), ("CISCO-UNITY-EXPRESS-MIB", "cueMessagesRetrieved"), ("CISCO-UNITY-EXPRESS-MIB", "cueMessagesDeleted"), ("CISCO-UNITY-EXPRESS-MIB", "cueLicensedMailboxesMax"), ("CISCO-UNITY-EXPRESS-MIB", "cueMailboxesAbove90PercentFull"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cueUsageGroup = cueUsageGroup.setStatus('current')
cueSecurityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 3)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueLoginAttempts"), ("CISCO-UNITY-EXPRESS-MIB", "cueLoginUsernameFailures"), ("CISCO-UNITY-EXPRESS-MIB", "cueLoginPasswordFailures"), ("CISCO-UNITY-EXPRESS-MIB", "cuePINAttempts"), ("CISCO-UNITY-EXPRESS-MIB", "cuePINResets"), ("CISCO-UNITY-EXPRESS-MIB", "cuePINUidFailures"), ("CISCO-UNITY-EXPRESS-MIB", "cuePINPasswordFailures"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cueSecurityGroup = cueSecurityGroup.setStatus('current')
cueNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 4)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueNotifEnable"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"), ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"), ("CISCO-UNITY-EXPRESS-MIB", "cueLoginUsernameThresh"), ("CISCO-UNITY-EXPRESS-MIB", "cueLoginPasswordThresh"), ("CISCO-UNITY-EXPRESS-MIB", "cuePINUidThresh"), ("CISCO-UNITY-EXPRESS-MIB", "cuePINPasswordThresh"), ("CISCO-UNITY-EXPRESS-MIB", "cuePINResetThresh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cueNotifGroup = cueNotifGroup.setStatus('current')
ciscoUnityExpressMIBNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 5)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressApplAlert"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressStorageAlert"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressSecurityAlert"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressCallMgrAlert"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressRescExhausted"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressBackupAlert"), ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressNTPAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUnityExpressMIBNotificationsGroup = ciscoUnityExpressMIBNotificationsGroup.setStatus('current')
cueBackupRestoreGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 6)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryOperation"), ("CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryDate"), ("CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cueBackupRestoreGroup = cueBackupRestoreGroup.setStatus('current')
cueSystemGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 7)).setObjects(("CISCO-UNITY-EXPRESS-MIB", "cueShutdownRequest"), ("CISCO-UNITY-EXPRESS-MIB", "cueAVTNumber"), ("CISCO-UNITY-EXPRESS-MIB", "cueVoicemailNumber"), ("CISCO-UNITY-EXPRESS-MIB", "cueAANumber"), ("CISCO-UNITY-EXPRESS-MIB", "cueCallControlAgentType"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayName"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIPType"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIP"), ("CISCO-UNITY-EXPRESS-MIB", "cueSIPPort"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerName"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIPType"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIP"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISubsystemState"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIUsername"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISoftwareVersion"), ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIPortsRegistered"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMailboxSize"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultGreetingSize"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageSizeMax"), ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cueSystemGroupRev1 = cueSystemGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNITY-EXPRESS-MIB", cueMboxType=cueMboxType, cueMboxMessageExpiryTime=cueMboxMessageExpiryTime, cuePercentTimeUsed=cuePercentTimeUsed, cueNotifGroup=cueNotifGroup, cueLicensedMailboxesMax=cueLicensedMailboxesMax, cueDefaultGreetingSize=cueDefaultGreetingSize, cueAVTNumber=cueAVTNumber, cueLoginPasswordThresh=cueLoginPasswordThresh, cueAverageGreetingLength=cueAverageGreetingLength, cueMboxEnabled=cueMboxEnabled, cueHardwareModuleType=cueHardwareModuleType, cueTotalTimeUsed=cueTotalTimeUsed, cueBackupRestoreGroup=cueBackupRestoreGroup, cueAANumber=cueAANumber, cueUsage=cueUsage, ciscoUnityExpressCallMgrAlert=ciscoUnityExpressCallMgrAlert, ciscoUnityExpressMIBCompliance=ciscoUnityExpressMIBCompliance, cueNotifSeverity=cueNotifSeverity, cueUsageGroup=cueUsageGroup, cueNotifDetail=cueNotifDetail, cueDefaultMailboxSize=cueDefaultMailboxSize, cueNotifSecurity=cueNotifSecurity, cueJTAPISoftwareVersion=cueJTAPISoftwareVersion, ciscoUnityExpressMIBNotifs=ciscoUnityExpressMIBNotifs, cueLoginAttempts=cueLoginAttempts, cuePINResets=cuePINResets, cueBRHistoryTable=cueBRHistoryTable, cueMboxNumberOfNewMessages=cueMboxNumberOfNewMessages, ciscoUnityExpressMIBNotificationsGroup=ciscoUnityExpressMIBNotificationsGroup, cueSIPGatewayIP=cueSIPGatewayIP, cueCapacityOfVoicemail=cueCapacityOfVoicemail, cueUsageScalars=cueUsageScalars, cueVoicemailNumber=cueVoicemailNumber, ciscoUnityExpressMIBCompliances=ciscoUnityExpressMIBCompliances, cueSystemDefaults=cueSystemDefaults, ciscoUnityExpressApplAlert=ciscoUnityExpressApplAlert, cueJTAPIServerName=cueJTAPIServerName, cueBackupRestore=cueBackupRestore, cueDefaultMessageExpiryTime=cueDefaultMessageExpiryTime, cueJTAPIServerIPType=cueJTAPIServerIPType, ciscoUnityExpressSecurityAlert=ciscoUnityExpressSecurityAlert, cueBRHistoryEntry=cueBRHistoryEntry, cueGreetingTimeUsed=cueGreetingTimeUsed, ciscoUnityExpressMIBComplianceRev1=ciscoUnityExpressMIBComplianceRev1, cueNotifDescription=cueNotifDescription, cueBRHistoryOperation=cueBRHistoryOperation, cueNotifConfig=cueNotifConfig, cuePersonalMailboxes=cuePersonalMailboxes, cuePINResetThresh=cuePINResetThresh, cueJTAPIInfo=cueJTAPIInfo, cueJTAPIUsername=cueJTAPIUsername, ciscoUnityExpressStorageAlert=ciscoUnityExpressStorageAlert, cueSystemGroupRev1=cueSystemGroupRev1, cueJTAPISubsystemState=cueJTAPISubsystemState, cueMboxEntry=cueMboxEntry, cueNotifDate=cueNotifDate, cueMboxMessageSizeMax=cueMboxMessageSizeMax, cueMboxIndex=cueMboxIndex, cuePINInfo=cuePINInfo, cueNotifEnable=cueNotifEnable, cueMboxSize=cueMboxSize, ciscoUnityExpressBackupAlert=ciscoUnityExpressBackupAlert, cueGreetingCount=cueGreetingCount, cueSystemGroup=cueSystemGroup, cueMboxNumberOfSavedMessages=cueMboxNumberOfSavedMessages, cueSIPPort=cueSIPPort, cueNotif=cueNotif, PYSNMP_MODULE_ID=ciscoUnityExpressMIB, cueMboxTable=cueMboxTable, ciscoUnityExpressMIB=ciscoUnityExpressMIB, cueNotifInfo=cueNotifInfo, cueJTAPIServerEntry=cueJTAPIServerEntry, cueAverageMessageLength=cueAverageMessageLength, ciscoUnityExpressMIBObjects=ciscoUnityExpressMIBObjects, cueMboxPercentTimeUsed=cueMboxPercentTimeUsed, cueMessagesDeleted=cueMessagesDeleted, cuePINAttempts=cuePINAttempts, cuePINUidThresh=cuePINUidThresh, cueSystemControl=cueSystemControl, cueJTAPIServerIP=cueJTAPIServerIP, cueLoginUsernameFailures=cueLoginUsernameFailures, cueMboxPrimaryExtension=cueMboxPrimaryExtension, cueSecurity=cueSecurity, cueBRHistoryDate=cueBRHistoryDate, cueLoginPasswordFailures=cueLoginPasswordFailures, ciscoUnityExpressRescExhausted=ciscoUnityExpressRescExhausted, cueShutdownRequest=cueShutdownRequest, ciscoUnityExpressMIBConform=ciscoUnityExpressMIBConform, cueMboxOwner=cueMboxOwner, cueMboxBusy=cueMboxBusy, cueJTAPIServerIndex=cueJTAPIServerIndex, cueMboxMWIState=cueMboxMWIState, cueLoginInfo=cueLoginInfo, cueMboxPlayTutorial=cueMboxPlayTutorial, cueSIPGatewayIPType=cueSIPGatewayIPType, cueJTAPIPortsRegistered=cueJTAPIPortsRegistered, cueAllocatedCapacity=cueAllocatedCapacity, cueBRHistoryIndex=cueBRHistoryIndex, cueSystem=cueSystem, cueLoginUsernameThresh=cueLoginUsernameThresh, cueMboxNumberOfMessages=cueMboxNumberOfMessages, ciscoUnityExpressMIBGroups=ciscoUnityExpressMIBGroups, cueDefaultMessageSizeMax=cueDefaultMessageSizeMax, cueSIPInfo=cueSIPInfo, cueSecurityGroup=cueSecurityGroup, cueLicensedPortsMax=cueLicensedPortsMax, cueMboxGreetingType=cueMboxGreetingType, cueMessagesLeft=cueMessagesLeft, cueBRHistoryResult=cueBRHistoryResult, ciscoUnityExpressNTPAlert=ciscoUnityExpressNTPAlert, cuePINPasswordThresh=cuePINPasswordThresh, cueSIPGatewayName=cueSIPGatewayName, cueJTAPIServerTable=cueJTAPIServerTable, cueMailboxesAbove90PercentFull=cueMailboxesAbove90PercentFull, cueCallControlAgentType=cueCallControlAgentType, cuePINUidFailures=cuePINUidFailures, cueMessageTimeUsed=cueMessageTimeUsed, cuePINPasswordFailures=cuePINPasswordFailures, cueActiveCalls=cueActiveCalls, cueGeneralDeliveryMailboxes=cueGeneralDeliveryMailboxes, cueMessagesRetrieved=cueMessagesRetrieved, cueMboxDescription=cueMboxDescription, cueMboxTimeUsed=cueMboxTimeUsed, cueOrphanedMailboxes=cueOrphanedMailboxes, cueMessageCount=cueMessageCount, cueSystemScalars=cueSystemScalars)
