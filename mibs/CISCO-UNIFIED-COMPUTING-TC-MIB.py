#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoAlarmSeverity, TimeIntervalSec, CiscoNetworkAddress, Unsigned64, CiscoInetAddressMask = mibBuilder.importSymbols("CISCO-TC", "CiscoAlarmSeverity", "TimeIntervalSec", "CiscoNetworkAddress", "Unsigned64", "CiscoInetAddressMask")
CucsManagedObjectId, CucsManagedObjectDn, ciscoUnifiedComputingMIB = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "CucsManagedObjectId", "CucsManagedObjectDn", "ciscoUnifiedComputingMIB")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter64, NotificationType, TimeTicks, ModuleIdentity, iso, Integer32, Gauge32, Unsigned32, Counter32, Bits, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "NotificationType", "TimeTicks", "ModuleIdentity", "iso", "Integer32", "Gauge32", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, MacAddress, RowPointer, TruthValue, TimeStamp, TextualConvention, TimeInterval, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "MacAddress", "RowPointer", "TruthValue", "TimeStamp", "TextualConvention", "TimeInterval", "DisplayString")
cucsTextualConventionsObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 4))
if mibBuilder.loadTexts: cucsTextualConventionsObjects.setLastUpdated('201306240000Z')
if mibBuilder.loadTexts: cucsTextualConventionsObjects.setOrganization('Cisco Systems Inc.')
class CucsAaaAccess(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("readOnly", 0), ("admin", 1), ("operations", 2), ("fault", 3), ("aaa", 4), ("podConfig", 5), ("podPolicy", 6), ("podSecurity", 7), ("podQos", 8), ("extLanConfig", 9), ("extLanPolicy", 10), ("extLanSecurity", 11), ("extLanQos", 12), ("extSanConfig", 13), ("extSanPolicy", 14), ("extSanSecurity", 15), ("extSanQos", 16), ("pnEquipment", 17), ("pnPolicy", 18), ("pnSecurity", 19), ("pnMaintenance", 20), ("lsConfig", 21), ("lsStorage", 22), ("lsNetwork", 23), ("lsSecurity", 24), ("lsServer", 25), ("lsQos", 26), ("lsConfigPolicy", 27), ("lsStoragePolicy", 28), ("lsNetworkPolicy", 29), ("lsSecurityPolicy", 30), ("lsServerPolicy", 31), ("lsQosPolicy", 32), ("lsExtAccess", 33), ("powerMgmt", 34), ("lsServerOper", 36), ("lsCompute", 37), ("orgManagement", 38))

class CucsAaaAccountStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("active", 0), ("inactive", 1))

class CucsAaaAuthRealmFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 200))
    namedValues = NamedValues(("nop", 0), ("updateRealm", 200))

class CucsAaaAuthRealmFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 200, 201, 202, 324, 325))
    namedValues = NamedValues(("nop", 0), ("updateRealmBegin", 200), ("updateRealmSetRealmLocal", 201), ("updateRealmSetRealmPeer", 202), ("updateRealmFail", 324), ("updateRealmSuccess", 325))

class CucsAaaCimcSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("all", 0), ("kvm", 1), ("vmedia", 2), ("sol", 3))

class CucsAaaClear(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CucsAaaConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("notApplied", 1))

class CucsAaaDomainAuthRealm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("local", 0), ("radius", 1), ("tacacs", 2), ("ldap", 3), ("none", 4))

class CucsAaaEpAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("readonly", 1), ("admin", 2))

class CucsAaaEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197))
    namedValues = NamedValues(("nop", 0), ("updateEp", 197))

class CucsAaaEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197, 198, 199, 322, 323))
    namedValues = NamedValues(("nop", 0), ("updateEpBegin", 197), ("updateEpSetEpLocal", 198), ("updateEpSetEpPeer", 199), ("updateEpFail", 322), ("updateEpSuccess", 323))

class CucsAaaEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197))
    namedValues = NamedValues(("nop", 0), ("updateEp", 197))

class CucsAaaExtMgmtAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("kvm", 1))

class CucsAaaLdapEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197))
    namedValues = NamedValues(("nop", 0), ("updateEp", 197))

class CucsAaaLdapEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197, 198, 199, 322, 323))
    namedValues = NamedValues(("nop", 0), ("updateEpBegin", 197), ("updateEpSetEpLocal", 198), ("updateEpSetEpPeer", 199), ("updateEpFail", 322), ("updateEpSuccess", 323))

class CucsAaaLdapGroupRuleAuthorization(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class CucsAaaLdapGroupRuleTraversal(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nonRecursive", 0), ("recursive", 1))

class CucsAaaLdapVendor(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("openLdap", 0), ("msAd", 1))

class CucsAaaNoRolePolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("noLogin", 0), ("assignDefaultRole", 1))

class CucsAaaPwdPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("enable", 0), ("disable", 1))

class CucsAaaRadiusEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197))
    namedValues = NamedValues(("nop", 0), ("updateEp", 197))

class CucsAaaRadiusEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197, 198, 199, 322, 323))
    namedValues = NamedValues(("nop", 0), ("updateEpBegin", 197), ("updateEpSetEpLocal", 198), ("updateEpSetEpPeer", 199), ("updateEpFail", 322), ("updateEpSuccess", 323))

class CucsAaaRadiusService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("all", 0), ("defaultValue", 1), ("accounting", 2))

class CucsAaaRealm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("local", 0), ("radius", 1), ("tacacs", 2), ("ldap", 3), ("none", 4))

class CucsAaaRealmFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 200))
    namedValues = NamedValues(("nop", 0), ("updateRealm", 200))

class CucsAaaRealmFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 200, 201, 202, 324, 325))
    namedValues = NamedValues(("nop", 0), ("updateRealmBegin", 200), ("updateRealmSetRealmLocal", 201), ("updateRealmSetRealmPeer", 202), ("updateRealmFail", 324), ("updateRealmSuccess", 325))

class CucsAaaRealmFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 200))
    namedValues = NamedValues(("nop", 0), ("updateRealm", 200))

class CucsAaaSession(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("local", 0), ("remote", 1), ("ipmi", 2))

class CucsAaaSessionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("active", 0), ("inactive", 1))

class CucsAaaSshStr(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("key", 1))

class CucsAaaTacacsPlusEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197))
    namedValues = NamedValues(("nop", 0), ("updateEp", 197))

class CucsAaaTacacsPlusEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 197, 198, 199, 322, 323))
    namedValues = NamedValues(("nop", 0), ("updateEpBegin", 197), ("updateEpSetEpLocal", 198), ("updateEpSetEpPeer", 199), ("updateEpFail", 322), ("updateEpSuccess", 323))

class CucsAaaUserEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 203))
    namedValues = NamedValues(("nop", 0), ("updateUserEp", 203))

class CucsAaaUserEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 203, 204, 205, 326, 327))
    namedValues = NamedValues(("nop", 0), ("updateUserEpBegin", 203), ("updateUserEpSetUserLocal", 204), ("updateUserEpSetUserPeer", 205), ("updateUserEpFail", 326), ("updateUserEpSuccess", 327))

class CucsAaaUserEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 203))
    namedValues = NamedValues(("nop", 0), ("updateUserEp", 203))

class CucsAaaUserInterface(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("shell", 1), ("web", 2), ("ep", 3), ("kvm", 4), ("vmedia", 5), ("sol", 6))

class CucsAdaptorAdapterStatsTrafficDir(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tx", 1), ("rx", 2))

class CucsAdaptorAdminPowerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("resetPower", 1))

class CucsAdaptorCIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsAdaptorCapDefFwVersionOpr(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("gt", 1), ("lt", 2), ("range", 3))

class CucsAdaptorCapDefType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("virtualizedEthIf", 1), ("virtualizedFcIf", 2), ("virtualizedScsiIf", 3), ("nonVirtualizedEthIf", 4), ("nonVirtualizedFcIf", 5), ("fcoe", 6), ("protectedEthIf", 7), ("protectedFcIf", 8), ("protectedFcoe", 9), ("pathEncapVirtual", 10), ("pathEncapConsolidated", 11), ("uplinkAggregation", 12), ("virtualizedEthSriov", 13), ("virtualizedFcSriov", 14))

class CucsAdaptorCapSpecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("virtualizedEthIf", 1), ("virtualizedFcIf", 2), ("virtualizedScsiIf", 3), ("nonVirtualizedEthIf", 4), ("nonVirtualizedFcIf", 5), ("fcoe", 6), ("protectedEthIf", 7), ("protectedFcIf", 8), ("protectedFcoe", 9), ("pathEncapVirtual", 10), ("pathEncapConsolidated", 11), ("uplinkAggregation", 12), ("virtualizedEthSriov", 13), ("virtualizedFcSriov", 14))

class CucsAdaptorDefaultAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CucsAdaptorEthInterruptProfileCoalescingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("min", 0), ("idle", 1))

class CucsAdaptorEthOffloadProfileLargeReceive(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorEthOffloadProfileTcpRxChecksum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorEthOffloadProfileTcpSegment(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorEthOffloadProfileTcpTxChecksum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorEthPortBySizeLargeStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("greaterThanOrEqualTo9216Delta", 0), ("greaterThanOrEqualTo9216DeltaAvg", 1), ("greaterThanOrEqualTo9216DeltaMax", 2), ("greaterThanOrEqualTo9216DeltaMin", 3), ("lessThan2048Delta", 4), ("lessThan2048DeltaAvg", 5), ("lessThan2048DeltaMax", 6), ("lessThan2048DeltaMin", 7), ("lessThan4096Delta", 8), ("lessThan4096DeltaAvg", 9), ("lessThan4096DeltaMax", 10), ("lessThan4096DeltaMin", 11), ("lessThan8192Delta", 12), ("lessThan8192DeltaAvg", 13), ("lessThan8192DeltaMax", 14), ("lessThan8192DeltaMin", 15), ("lessThan9216Delta", 16), ("lessThan9216DeltaAvg", 17), ("lessThan9216DeltaMax", 18), ("lessThan9216DeltaMin", 19), ("lessThanOrEqualTo1518Delta", 20), ("lessThanOrEqualTo1518DeltaAvg", 21), ("lessThanOrEqualTo1518DeltaMax", 22), ("lessThanOrEqualTo1518DeltaMin", 23), ("noBreakdownGreaterThan1518Delta", 24), ("noBreakdownGreaterThan1518DeltaAvg", 25), ("noBreakdownGreaterThan1518DeltaMax", 26), ("noBreakdownGreaterThan1518DeltaMin", 27))

class CucsAdaptorEthPortBySizeLargeStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("greaterThanOrEqualTo9216Delta", 0), ("greaterThanOrEqualTo9216DeltaAvg", 1), ("greaterThanOrEqualTo9216DeltaMax", 2), ("greaterThanOrEqualTo9216DeltaMin", 3), ("lessThan2048Delta", 4), ("lessThan2048DeltaAvg", 5), ("lessThan2048DeltaMax", 6), ("lessThan2048DeltaMin", 7), ("lessThan4096Delta", 8), ("lessThan4096DeltaAvg", 9), ("lessThan4096DeltaMax", 10), ("lessThan4096DeltaMin", 11), ("lessThan8192Delta", 12), ("lessThan8192DeltaAvg", 13), ("lessThan8192DeltaMax", 14), ("lessThan8192DeltaMin", 15), ("lessThan9216Delta", 16), ("lessThan9216DeltaAvg", 17), ("lessThan9216DeltaMax", 18), ("lessThan9216DeltaMin", 19), ("lessThanOrEqualTo1518Delta", 20), ("lessThanOrEqualTo1518DeltaAvg", 21), ("lessThanOrEqualTo1518DeltaMax", 22), ("lessThanOrEqualTo1518DeltaMin", 23), ("noBreakdownGreaterThan1518Delta", 24), ("noBreakdownGreaterThan1518DeltaAvg", 25), ("noBreakdownGreaterThan1518DeltaMax", 26), ("noBreakdownGreaterThan1518DeltaMin", 27))

class CucsAdaptorEthPortBySizeSmallStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("equals64Delta", 0), ("equals64DeltaAvg", 1), ("equals64DeltaMax", 2), ("equals64DeltaMin", 3), ("lessThan1024Delta", 4), ("lessThan1024DeltaAvg", 5), ("lessThan1024DeltaMax", 6), ("lessThan1024DeltaMin", 7), ("lessThan128Delta", 8), ("lessThan128DeltaAvg", 9), ("lessThan128DeltaMax", 10), ("lessThan128DeltaMin", 11), ("lessThan256Delta", 12), ("lessThan256DeltaAvg", 13), ("lessThan256DeltaMax", 14), ("lessThan256DeltaMin", 15), ("lessThan512Delta", 16), ("lessThan512DeltaAvg", 17), ("lessThan512DeltaMax", 18), ("lessThan512DeltaMin", 19), ("lessThan64Delta", 20), ("lessThan64DeltaAvg", 21), ("lessThan64DeltaMax", 22), ("lessThan64DeltaMin", 23))

class CucsAdaptorEthPortBySizeSmallStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("equals64Delta", 0), ("equals64DeltaAvg", 1), ("equals64DeltaMax", 2), ("equals64DeltaMin", 3), ("lessThan1024Delta", 4), ("lessThan1024DeltaAvg", 5), ("lessThan1024DeltaMax", 6), ("lessThan1024DeltaMin", 7), ("lessThan128Delta", 8), ("lessThan128DeltaAvg", 9), ("lessThan128DeltaMax", 10), ("lessThan128DeltaMin", 11), ("lessThan256Delta", 12), ("lessThan256DeltaAvg", 13), ("lessThan256DeltaMax", 14), ("lessThan256DeltaMin", 15), ("lessThan512Delta", 16), ("lessThan512DeltaAvg", 17), ("lessThan512DeltaMax", 18), ("lessThan512DeltaMin", 19), ("lessThan64Delta", 20), ("lessThan64DeltaAvg", 21), ("lessThan64DeltaMax", 22), ("lessThan64DeltaMin", 23))

class CucsAdaptorEthPortErrStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("badCrcPacketsDelta", 0), ("badCrcPacketsDeltaAvg", 1), ("badCrcPacketsDeltaMax", 2), ("badCrcPacketsDeltaMin", 3), ("badLengthPacketsDelta", 4), ("badLengthPacketsDeltaAvg", 5), ("badLengthPacketsDeltaMax", 6), ("badLengthPacketsDeltaMin", 7), ("macDiscardedPacketsDelta", 8), ("macDiscardedPacketsDeltaAvg", 9), ("macDiscardedPacketsDeltaMax", 10), ("macDiscardedPacketsDeltaMin", 11))

class CucsAdaptorEthPortErrStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("badCrcPacketsDelta", 0), ("badCrcPacketsDeltaAvg", 1), ("badCrcPacketsDeltaMax", 2), ("badCrcPacketsDeltaMin", 3), ("badLengthPacketsDelta", 4), ("badLengthPacketsDeltaAvg", 5), ("badLengthPacketsDeltaMax", 6), ("badLengthPacketsDeltaMin", 7), ("macDiscardedPacketsDelta", 8), ("macDiscardedPacketsDeltaAvg", 9), ("macDiscardedPacketsDeltaMax", 10), ("macDiscardedPacketsDeltaMin", 11))

class CucsAdaptorEthPortMcastStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("broadcastPacketsDelta", 0), ("broadcastPacketsDeltaAvg", 1), ("broadcastPacketsDeltaMax", 2), ("broadcastPacketsDeltaMin", 3), ("multicastPacketsDelta", 4), ("multicastPacketsDeltaAvg", 5), ("multicastPacketsDeltaMax", 6), ("multicastPacketsDeltaMin", 7), ("unicastPacketsDelta", 8), ("unicastPacketsDeltaAvg", 9), ("unicastPacketsDeltaMax", 10), ("unicastPacketsDeltaMin", 11))

class CucsAdaptorEthPortMcastStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("broadcastPacketsDelta", 0), ("broadcastPacketsDeltaAvg", 1), ("broadcastPacketsDeltaMax", 2), ("broadcastPacketsDeltaMin", 3), ("multicastPacketsDelta", 4), ("multicastPacketsDeltaAvg", 5), ("multicastPacketsDeltaMax", 6), ("multicastPacketsDeltaMin", 7), ("unicastPacketsDelta", 8), ("unicastPacketsDeltaAvg", 9), ("unicastPacketsDeltaMax", 10), ("unicastPacketsDeltaMin", 11))

class CucsAdaptorEthPortOutsizedStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("oversizedBadCrcPacketsDelta", 0), ("oversizedBadCrcPacketsDeltaAvg", 1), ("oversizedBadCrcPacketsDeltaMax", 2), ("oversizedBadCrcPacketsDeltaMin", 3), ("oversizedGoodCrcPacketsDelta", 4), ("oversizedGoodCrcPacketsDeltaAvg", 5), ("oversizedGoodCrcPacketsDeltaMax", 6), ("oversizedGoodCrcPacketsDeltaMin", 7), ("oversizedPacketsDelta", 8), ("oversizedPacketsDeltaAvg", 9), ("oversizedPacketsDeltaMax", 10), ("oversizedPacketsDeltaMin", 11), ("undersizedBadCrcPacketsDelta", 12), ("undersizedBadCrcPacketsDeltaAvg", 13), ("undersizedBadCrcPacketsDeltaMax", 14), ("undersizedBadCrcPacketsDeltaMin", 15), ("undersizedGoodCrcPacketsDelta", 16), ("undersizedGoodCrcPacketsDeltaAvg", 17), ("undersizedGoodCrcPacketsDeltaMax", 18), ("undersizedGoodCrcPacketsDeltaMin", 19))

class CucsAdaptorEthPortOutsizedStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("oversizedBadCrcPacketsDelta", 0), ("oversizedBadCrcPacketsDeltaAvg", 1), ("oversizedBadCrcPacketsDeltaMax", 2), ("oversizedBadCrcPacketsDeltaMin", 3), ("oversizedGoodCrcPacketsDelta", 4), ("oversizedGoodCrcPacketsDeltaAvg", 5), ("oversizedGoodCrcPacketsDeltaMax", 6), ("oversizedGoodCrcPacketsDeltaMin", 7), ("oversizedPacketsDelta", 8), ("oversizedPacketsDeltaAvg", 9), ("oversizedPacketsDeltaMax", 10), ("oversizedPacketsDeltaMin", 11), ("undersizedBadCrcPacketsDelta", 12), ("undersizedBadCrcPacketsDeltaAvg", 13), ("undersizedBadCrcPacketsDeltaMax", 14), ("undersizedBadCrcPacketsDeltaMin", 15), ("undersizedGoodCrcPacketsDelta", 16), ("undersizedGoodCrcPacketsDeltaAvg", 17), ("undersizedGoodCrcPacketsDeltaMax", 18), ("undersizedGoodCrcPacketsDeltaMin", 19))

class CucsAdaptorEthPortStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("goodPacketsDelta", 0), ("goodPacketsDeltaAvg", 1), ("goodPacketsDeltaMax", 2), ("goodPacketsDeltaMin", 3), ("pausePacketsDelta", 4), ("pausePacketsDeltaAvg", 5), ("pausePacketsDeltaMax", 6), ("pausePacketsDeltaMin", 7), ("perPriorityPausePacketsDelta", 8), ("perPriorityPausePacketsDeltaAvg", 9), ("perPriorityPausePacketsDeltaMax", 10), ("perPriorityPausePacketsDeltaMin", 11), ("pppPacketsDelta", 12), ("pppPacketsDeltaAvg", 13), ("pppPacketsDeltaMax", 14), ("pppPacketsDeltaMin", 15), ("totalPacketsDelta", 16), ("totalPacketsDeltaAvg", 17), ("totalPacketsDeltaMax", 18), ("totalPacketsDeltaMin", 19), ("vlanPacketsDelta", 20), ("vlanPacketsDeltaAvg", 21), ("vlanPacketsDeltaMax", 22), ("vlanPacketsDeltaMin", 23))

class CucsAdaptorEthPortStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("goodPacketsDelta", 0), ("goodPacketsDeltaAvg", 1), ("goodPacketsDeltaMax", 2), ("goodPacketsDeltaMin", 3), ("pausePacketsDelta", 4), ("pausePacketsDeltaAvg", 5), ("pausePacketsDeltaMax", 6), ("pausePacketsDeltaMin", 7), ("perPriorityPausePacketsDelta", 8), ("perPriorityPausePacketsDeltaAvg", 9), ("perPriorityPausePacketsDeltaMax", 10), ("perPriorityPausePacketsDeltaMin", 11), ("pppPacketsDelta", 12), ("pppPacketsDeltaAvg", 13), ("pppPacketsDeltaMax", 14), ("pppPacketsDeltaMin", 15), ("totalPacketsDelta", 16), ("totalPacketsDeltaAvg", 17), ("totalPacketsDeltaMax", 18), ("totalPacketsDeltaMin", 19), ("vlanPacketsDelta", 20), ("vlanPacketsDeltaAvg", 21), ("vlanPacketsDeltaMax", 22), ("vlanPacketsDeltaMin", 23))

class CucsAdaptorEtherIfStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxBytesDelta", 0), ("rxBytesDeltaAvg", 1), ("rxBytesDeltaMax", 2), ("rxBytesDeltaMin", 3), ("rxDroppedDelta", 4), ("rxDroppedDeltaAvg", 5), ("rxDroppedDeltaMax", 6), ("rxDroppedDeltaMin", 7), ("rxErrorsDelta", 8), ("rxErrorsDeltaAvg", 9), ("rxErrorsDeltaMax", 10), ("rxErrorsDeltaMin", 11), ("rxPacketsDelta", 12), ("rxPacketsDeltaAvg", 13), ("rxPacketsDeltaMax", 14), ("rxPacketsDeltaMin", 15), ("txBytesDelta", 16), ("txBytesDeltaAvg", 17), ("txBytesDeltaMax", 18), ("txBytesDeltaMin", 19), ("txDroppedDelta", 20), ("txDroppedDeltaAvg", 21), ("txDroppedDeltaMax", 22), ("txDroppedDeltaMin", 23), ("txErrorsDelta", 24), ("txErrorsDeltaAvg", 25), ("txErrorsDeltaMax", 26), ("txErrorsDeltaMin", 27), ("txPacketsDelta", 28), ("txPacketsDeltaAvg", 29), ("txPacketsDeltaMax", 30), ("txPacketsDeltaMin", 31))

class CucsAdaptorEtherIfStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxBytesDelta", 0), ("rxBytesDeltaAvg", 1), ("rxBytesDeltaMax", 2), ("rxBytesDeltaMin", 3), ("rxDroppedDelta", 4), ("rxDroppedDeltaAvg", 5), ("rxDroppedDeltaMax", 6), ("rxDroppedDeltaMin", 7), ("rxErrorsDelta", 8), ("rxErrorsDeltaAvg", 9), ("rxErrorsDeltaMax", 10), ("rxErrorsDeltaMin", 11), ("rxPacketsDelta", 12), ("rxPacketsDeltaAvg", 13), ("rxPacketsDeltaMax", 14), ("rxPacketsDeltaMin", 15), ("txBytesDelta", 16), ("txBytesDeltaAvg", 17), ("txBytesDeltaMax", 18), ("txBytesDeltaMin", 19), ("txDroppedDelta", 20), ("txDroppedDeltaAvg", 21), ("txDroppedDeltaMax", 22), ("txDroppedDeltaMin", 23), ("txErrorsDelta", 24), ("txErrorsDeltaAvg", 25), ("txErrorsDeltaMax", 26), ("txErrorsDeltaMin", 27), ("txPacketsDelta", 28), ("txPacketsDeltaAvg", 29), ("txPacketsDeltaMax", 30), ("txPacketsDeltaMin", 31))

class CucsAdaptorExtEthIfFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 499))
    namedValues = NamedValues(("nop", 0), ("pathReset", 499))

class CucsAdaptorExtEthIfFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 499, 500, 501, 502, 503))
    namedValues = NamedValues(("nop", 0), ("pathResetBegin", 499), ("pathResetDisable", 500), ("pathResetEnable", 501), ("pathResetFail", 502), ("pathResetSuccess", 503))

class CucsAdaptorExtEthIfFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 499))
    namedValues = NamedValues(("nop", 0), ("pathReset", 499))

class CucsAdaptorExtEthIfPcPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1024, 4096)

class CucsAdaptorExtEthIfPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsAdaptorExtEthIfPcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsAdaptorExtEthIfPcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsAdaptorExtIfAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 44))
    namedValues = NamedValues(("enabled", 0), ("resetConnectivity", 44))

class CucsAdaptorExtIfEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsAdaptorExtIfEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsAdaptorExtIfPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsAdaptorExtIfPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsAdaptorExtIpV6RssHashProfileIpHash(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorExtIpV6RssHashProfileTcpHash(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorExternalEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsAdaptorExternalPcLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsAdaptorFcErrorRecoveryProfileFcpErrorRecovery(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorFcIfEventStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("invalidCRCCountDelta", 0), ("invalidCRCCountDeltaAvg", 1), ("invalidCRCCountDeltaMax", 2), ("invalidCRCCountDeltaMin", 3), ("linkFailureCountDelta", 4), ("linkFailureCountDeltaAvg", 5), ("linkFailureCountDeltaMax", 6), ("linkFailureCountDeltaMin", 7), ("lipCountDelta", 8), ("lipCountDeltaAvg", 9), ("lipCountDeltaMax", 10), ("lipCountDeltaMin", 11), ("lossOfSignalCountDelta", 12), ("lossOfSignalCountDeltaAvg", 13), ("lossOfSignalCountDeltaMax", 14), ("lossOfSignalCountDeltaMin", 15), ("lossOfSyncCountDelta", 16), ("lossOfSyncCountDeltaAvg", 17), ("lossOfSyncCountDeltaMax", 18), ("lossOfSyncCountDeltaMin", 19), ("nOSCountDelta", 20), ("nOSCountDeltaAvg", 21), ("nOSCountDeltaMax", 22), ("nOSCountDeltaMin", 23), ("secondsSinceLastResetDelta", 24), ("secondsSinceLastResetDeltaAvg", 25), ("secondsSinceLastResetDeltaMax", 26), ("secondsSinceLastResetDeltaMin", 27), ("seqProtocolErrCountDelta", 28), ("seqProtocolErrCountDeltaAvg", 29), ("seqProtocolErrCountDeltaMax", 30), ("seqProtocolErrCountDeltaMin", 31))

class CucsAdaptorFcIfEventStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("invalidCRCCountDelta", 0), ("invalidCRCCountDeltaAvg", 1), ("invalidCRCCountDeltaMax", 2), ("invalidCRCCountDeltaMin", 3), ("linkFailureCountDelta", 4), ("linkFailureCountDeltaAvg", 5), ("linkFailureCountDeltaMax", 6), ("linkFailureCountDeltaMin", 7), ("lipCountDelta", 8), ("lipCountDeltaAvg", 9), ("lipCountDeltaMax", 10), ("lipCountDeltaMin", 11), ("lossOfSignalCountDelta", 12), ("lossOfSignalCountDeltaAvg", 13), ("lossOfSignalCountDeltaMax", 14), ("lossOfSignalCountDeltaMin", 15), ("lossOfSyncCountDelta", 16), ("lossOfSyncCountDeltaAvg", 17), ("lossOfSyncCountDeltaMax", 18), ("lossOfSyncCountDeltaMin", 19), ("nOSCountDelta", 20), ("nOSCountDeltaAvg", 21), ("nOSCountDeltaMax", 22), ("nOSCountDeltaMin", 23), ("secondsSinceLastResetDelta", 24), ("secondsSinceLastResetDeltaAvg", 25), ("secondsSinceLastResetDeltaMax", 26), ("secondsSinceLastResetDeltaMin", 27), ("seqProtocolErrCountDelta", 28), ("seqProtocolErrCountDeltaAvg", 29), ("seqProtocolErrCountDeltaMax", 30), ("seqProtocolErrCountDeltaMin", 31))

class CucsAdaptorFcIfFC4StatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("controlRequestsDelta", 0), ("controlRequestsDeltaAvg", 1), ("controlRequestsDeltaMax", 2), ("controlRequestsDeltaMin", 3), ("inputMegabytesDelta", 4), ("inputMegabytesDeltaAvg", 5), ("inputMegabytesDeltaMax", 6), ("inputMegabytesDeltaMin", 7), ("inputRequestsDelta", 8), ("inputRequestsDeltaAvg", 9), ("inputRequestsDeltaMax", 10), ("inputRequestsDeltaMin", 11), ("outputMegabytesDelta", 12), ("outputMegabytesDeltaAvg", 13), ("outputMegabytesDeltaMax", 14), ("outputMegabytesDeltaMin", 15), ("outputRequestsDelta", 16), ("outputRequestsDeltaAvg", 17), ("outputRequestsDeltaMax", 18), ("outputRequestsDeltaMin", 19))

class CucsAdaptorFcIfFC4StatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("controlRequestsDelta", 0), ("controlRequestsDeltaAvg", 1), ("controlRequestsDeltaMax", 2), ("controlRequestsDeltaMin", 3), ("inputMegabytesDelta", 4), ("inputMegabytesDeltaAvg", 5), ("inputMegabytesDeltaMax", 6), ("inputMegabytesDeltaMin", 7), ("inputRequestsDelta", 8), ("inputRequestsDeltaAvg", 9), ("inputRequestsDeltaMax", 10), ("inputRequestsDeltaMin", 11), ("outputMegabytesDelta", 12), ("outputMegabytesDeltaAvg", 13), ("outputMegabytesDeltaMax", 14), ("outputMegabytesDeltaMin", 15), ("outputRequestsDelta", 16), ("outputRequestsDeltaAvg", 17), ("outputRequestsDeltaMax", 18), ("outputRequestsDeltaMin", 19))

class CucsAdaptorFcIfFrameStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dumpedFramesDelta", 0), ("dumpedFramesDeltaAvg", 1), ("dumpedFramesDeltaMax", 2), ("dumpedFramesDeltaMin", 3), ("errorFramesDelta", 4), ("errorFramesDeltaAvg", 5), ("errorFramesDeltaMax", 6), ("errorFramesDeltaMin", 7), ("rxFramesDelta", 8), ("rxFramesDeltaAvg", 9), ("rxFramesDeltaMax", 10), ("rxFramesDeltaMin", 11), ("txFramesDelta", 12), ("txFramesDeltaAvg", 13), ("txFramesDeltaMax", 14), ("txFramesDeltaMin", 15))

class CucsAdaptorFcIfFrameStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dumpedFramesDelta", 0), ("dumpedFramesDeltaAvg", 1), ("dumpedFramesDeltaMax", 2), ("dumpedFramesDeltaMin", 3), ("errorFramesDelta", 4), ("errorFramesDeltaAvg", 5), ("errorFramesDeltaMax", 6), ("errorFramesDeltaMin", 7), ("rxFramesDelta", 8), ("rxFramesDeltaAvg", 9), ("rxFramesDeltaMax", 10), ("rxFramesDeltaMin", 11), ("txFramesDelta", 12), ("txFramesDeltaAvg", 13), ("txFramesDeltaMax", 14), ("txFramesDeltaMin", 15))

class CucsAdaptorFcPortStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxBadFramesDelta", 0), ("rxBadFramesDeltaAvg", 1), ("rxBadFramesDeltaMax", 2), ("rxBadFramesDeltaMin", 3), ("rxFramesDelta", 4), ("rxFramesDeltaAvg", 5), ("rxFramesDeltaMax", 6), ("rxFramesDeltaMin", 7), ("txBadFramesDelta", 8), ("txBadFramesDeltaAvg", 9), ("txBadFramesDeltaMax", 10), ("txBadFramesDeltaMin", 11), ("txFramesDelta", 12), ("txFramesDeltaAvg", 13), ("txFramesDeltaMax", 14), ("txFramesDeltaMin", 15))

class CucsAdaptorFcPortStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxBadFramesDelta", 0), ("rxBadFramesDeltaAvg", 1), ("rxBadFramesDeltaMax", 2), ("rxBadFramesDeltaMin", 3), ("rxFramesDelta", 4), ("rxFramesDeltaAvg", 5), ("rxFramesDeltaMax", 6), ("rxFramesDeltaMin", 7), ("txBadFramesDelta", 8), ("txBadFramesDeltaAvg", 9), ("txBadFramesDeltaMax", 10), ("txBadFramesDeltaMin", 11), ("txFramesDelta", 12), ("txFramesDeltaAvg", 13), ("txFramesDeltaMax", 14), ("txFramesDeltaMin", 15))

class CucsAdaptorHostEthIfFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 505))
    namedValues = NamedValues(("nop", 0), ("circuitReset", 505))

class CucsAdaptorHostEthIfFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 505, 506, 507, 508, 509, 515, 516))
    namedValues = NamedValues(("nop", 0), ("circuitResetBegin", 505), ("circuitResetDisableA", 506), ("circuitResetEnableA", 507), ("circuitResetDisableB", 508), ("circuitResetEnableB", 509), ("circuitResetFail", 515), ("circuitResetSuccess", 516))

class CucsAdaptorHostEthIfFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 505))
    namedValues = NamedValues(("nop", 0), ("circuitReset", 505))

class CucsAdaptorHostFcIfAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 44, 45, 46))
    namedValues = NamedValues(("enabled", 0), ("resetConnectivityActive", 44), ("resetConnectivityPassive", 45), ("resetConnectivity", 46))

class CucsAdaptorHostFcIfPersBind(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4))
    namedValues = NamedValues(("disabled", 0), ("enabled", 4))

class CucsAdaptorHostFcIfFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 142, 510))
    namedValues = NamedValues(("nop", 0), ("resetFcPersBinding", 142), ("circuitReset", 510))

class CucsAdaptorHostFcIfFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 142, 328, 329, 510, 511, 512, 513, 514, 517, 518, 813, 814))
    namedValues = NamedValues(("nop", 0), ("resetFcPersBindingBegin", 142), ("resetFcPersBindingFail", 328), ("resetFcPersBindingSuccess", 329), ("circuitResetBegin", 510), ("circuitResetDisableA", 511), ("circuitResetEnableA", 512), ("circuitResetDisableB", 513), ("circuitResetEnableB", 514), ("circuitResetFail", 517), ("circuitResetSuccess", 518), ("resetFcPersBindingExecuteLocal", 813), ("resetFcPersBindingExecutePeer", 814))

class CucsAdaptorHostFcIfFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 142, 510))
    namedValues = NamedValues(("nop", 0), ("resetFcPersBinding", 142), ("circuitReset", 510))

class CucsAdaptorHostIfAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 44, 45, 46))
    namedValues = NamedValues(("enabled", 0), ("resetConnectivityActive", 44), ("resetConnectivityPassive", 45), ("resetConnectivity", 46))

class CucsAdaptorHostIfBootDev(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorHostMgmtCapPreboot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("pnuOS", 1), ("efi", 2))

class CucsAdaptorHostMgmtCapPresence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unspecified", 0), ("host", 1), ("cimc", 2))

class CucsAdaptorHostVisibility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("no", 0), ("yes", 1), ("osDependent", 2))

class CucsAdaptorIScsiCapBootOrderType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 6, 16, 128))
    namedValues = NamedValues(("systemBootOrder", 0), ("fddOrder", 1), ("hddOrder", 2), ("cdOrder", 3), ("networkDeviceOrder", 6), ("internalEfiShell", 16), ("bevOrder", 128))

class CucsAdaptorInterruptMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("msiX", 1), ("msi", 2), ("intx", 3))

class CucsAdaptorIpV4RssHashProfileIpHash(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorIpV4RssHashProfileTcpHash(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorIpV6RssHashProfileIpHash(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorIpV6RssHashProfileTcpHash(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorIscsiProtConnectionTimeOut(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 255)

class CucsAdaptorIscsiProtDhcpTimeOut(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(60, 300)

class CucsAdaptorIscsiProtLunBusyRetryCount(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 60)

class CucsAdaptorLanCapDefaultVlan(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("nativeVlan", 1), ("defaultVlan", 2))

class CucsAdaptorLinkState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("adminDown", 1), ("down", 2), ("error", 3), ("up", 4), ("unallocated", 5), ("unavailable", 6))

class CucsAdaptorLldpCapSupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("full", 2))

class CucsAdaptorMenloBaseErrorStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("uncorrectableErrorsDelta", 4), ("uncorrectableErrorsDeltaAvg", 5), ("uncorrectableErrorsDeltaMax", 6), ("uncorrectableErrorsDeltaMin", 7))

class CucsAdaptorMenloBaseErrorStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("uncorrectableErrorsDelta", 4), ("uncorrectableErrorsDeltaAvg", 5), ("uncorrectableErrorsDeltaMax", 6), ("uncorrectableErrorsDeltaMin", 7))

class CucsAdaptorMenloDcePortStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxPauseCFCDelta", 0), ("rxPauseCFCDeltaAvg", 1), ("rxPauseCFCDeltaMax", 2), ("rxPauseCFCDeltaMin", 3), ("rxPausePFCDelta", 4), ("rxPausePFCDeltaAvg", 5), ("rxPausePFCDeltaMax", 6), ("rxPausePFCDeltaMin", 7), ("txPauseCFCDelta", 8), ("txPauseCFCDeltaAvg", 9), ("txPauseCFCDeltaMax", 10), ("txPauseCFCDeltaMin", 11), ("txPausePFCDelta", 12), ("txPausePFCDeltaAvg", 13), ("txPausePFCDeltaMax", 14), ("txPausePFCDeltaMin", 15))

class CucsAdaptorMenloDcePortStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxPauseCFCDelta", 0), ("rxPauseCFCDeltaAvg", 1), ("rxPauseCFCDeltaMax", 2), ("rxPauseCFCDeltaMin", 3), ("rxPausePFCDelta", 4), ("rxPausePFCDeltaAvg", 5), ("rxPausePFCDeltaMax", 6), ("rxPausePFCDeltaMin", 7), ("txPauseCFCDelta", 8), ("txPauseCFCDeltaAvg", 9), ("txPauseCFCDeltaMax", 10), ("txPauseCFCDeltaMin", 11), ("txPausePFCDelta", 12), ("txPausePFCDeltaAvg", 13), ("txPausePFCDeltaMax", 14), ("txPausePFCDeltaMin", 15))

class CucsAdaptorMenloEthErrorStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("dropAclDelta", 4), ("dropAclDeltaAvg", 5), ("dropAclDeltaMax", 6), ("dropAclDeltaMin", 7), ("popErrorsDelta", 8), ("popErrorsDeltaAvg", 9), ("popErrorsDeltaMax", 10), ("popErrorsDeltaMin", 11), ("pushErrorsDelta", 12), ("pushErrorsDeltaAvg", 13), ("pushErrorsDeltaMax", 14), ("pushErrorsDeltaMin", 15), ("uncorrectableErrorsDelta", 16), ("uncorrectableErrorsDeltaAvg", 17), ("uncorrectableErrorsDeltaMax", 18), ("uncorrectableErrorsDeltaMin", 19))

class CucsAdaptorMenloEthErrorStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("dropAclDelta", 4), ("dropAclDeltaAvg", 5), ("dropAclDeltaMax", 6), ("dropAclDeltaMin", 7), ("popErrorsDelta", 8), ("popErrorsDeltaAvg", 9), ("popErrorsDeltaMax", 10), ("popErrorsDeltaMin", 11), ("pushErrorsDelta", 12), ("pushErrorsDeltaAvg", 13), ("pushErrorsDeltaMax", 14), ("pushErrorsDeltaMin", 15), ("uncorrectableErrorsDelta", 16), ("uncorrectableErrorsDeltaAvg", 17), ("uncorrectableErrorsDeltaMax", 18), ("uncorrectableErrorsDeltaMin", 19))

class CucsAdaptorMenloEthStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropOverrunDelta", 0), ("dropOverrunDeltaAvg", 1), ("dropOverrunDeltaMax", 2), ("dropOverrunDeltaMin", 3), ("dropRuntDelta", 4), ("dropRuntDeltaAvg", 5), ("dropRuntDeltaMax", 6), ("dropRuntDeltaMin", 7), ("truncateOverrunDelta", 8), ("truncateOverrunDeltaAvg", 9), ("truncateOverrunDeltaMax", 10), ("truncateOverrunDeltaMin", 11))

class CucsAdaptorMenloEthStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropOverrunDelta", 0), ("dropOverrunDeltaAvg", 1), ("dropOverrunDeltaMax", 2), ("dropOverrunDeltaMin", 3), ("dropRuntDelta", 4), ("dropRuntDeltaAvg", 5), ("dropRuntDeltaMax", 6), ("dropRuntDeltaMin", 7), ("truncateOverrunDelta", 8), ("truncateOverrunDeltaAvg", 9), ("truncateOverrunDeltaMax", 10), ("truncateOverrunDeltaMin", 11))

class CucsAdaptorMenloFcErrorStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("popErrorsDelta", 4), ("popErrorsDeltaAvg", 5), ("popErrorsDeltaMax", 6), ("popErrorsDeltaMin", 7), ("pushErrorsDelta", 8), ("pushErrorsDeltaAvg", 9), ("pushErrorsDeltaMax", 10), ("pushErrorsDeltaMin", 11), ("uncorrectableErrorsDelta", 12), ("uncorrectableErrorsDeltaAvg", 13), ("uncorrectableErrorsDeltaMax", 14), ("uncorrectableErrorsDeltaMin", 15))

class CucsAdaptorMenloFcErrorStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("popErrorsDelta", 4), ("popErrorsDeltaAvg", 5), ("popErrorsDeltaMax", 6), ("popErrorsDeltaMin", 7), ("pushErrorsDelta", 8), ("pushErrorsDeltaAvg", 9), ("pushErrorsDeltaMax", 10), ("pushErrorsDeltaMin", 11), ("uncorrectableErrorsDelta", 12), ("uncorrectableErrorsDeltaAvg", 13), ("uncorrectableErrorsDeltaMax", 14), ("uncorrectableErrorsDeltaMin", 15))

class CucsAdaptorMenloFcStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropAclDelta", 0), ("dropAclDeltaAvg", 1), ("dropAclDeltaMax", 2), ("dropAclDeltaMin", 3), ("dropOverrunDelta", 4), ("dropOverrunDeltaAvg", 5), ("dropOverrunDeltaMax", 6), ("dropOverrunDeltaMin", 7), ("dropRuntDelta", 8), ("dropRuntDeltaAvg", 9), ("dropRuntDeltaMax", 10), ("dropRuntDeltaMin", 11), ("truncateOverrunDelta", 12), ("truncateOverrunDeltaAvg", 13), ("truncateOverrunDeltaMax", 14), ("truncateOverrunDeltaMin", 15))

class CucsAdaptorMenloFcStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropAclDelta", 0), ("dropAclDeltaAvg", 1), ("dropAclDeltaMax", 2), ("dropAclDeltaMin", 3), ("dropOverrunDelta", 4), ("dropOverrunDeltaAvg", 5), ("dropOverrunDeltaMax", 6), ("dropOverrunDeltaMin", 7), ("dropRuntDelta", 8), ("dropRuntDeltaAvg", 9), ("dropRuntDeltaMax", 10), ("dropRuntDeltaMin", 11), ("truncateOverrunDelta", 12), ("truncateOverrunDeltaAvg", 13), ("truncateOverrunDeltaMax", 14), ("truncateOverrunDeltaMin", 15))

class CucsAdaptorMenloHostPortStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxPauseCFCDelta", 0), ("rxPauseCFCDeltaAvg", 1), ("rxPauseCFCDeltaMax", 2), ("rxPauseCFCDeltaMin", 3), ("rxPausePFCDelta", 4), ("rxPausePFCDeltaAvg", 5), ("rxPausePFCDeltaMax", 6), ("rxPausePFCDeltaMin", 7), ("txPauseCFCDelta", 8), ("txPauseCFCDeltaAvg", 9), ("txPauseCFCDeltaMax", 10), ("txPauseCFCDeltaMin", 11), ("txPausePFCDelta", 12), ("txPausePFCDeltaAvg", 13), ("txPausePFCDeltaMax", 14), ("txPausePFCDeltaMin", 15))

class CucsAdaptorMenloHostPortStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rxPauseCFCDelta", 0), ("rxPauseCFCDeltaAvg", 1), ("rxPauseCFCDeltaMax", 2), ("rxPauseCFCDeltaMin", 3), ("rxPausePFCDelta", 4), ("rxPausePFCDeltaAvg", 5), ("rxPausePFCDeltaMax", 6), ("rxPausePFCDeltaMin", 7), ("txPauseCFCDelta", 8), ("txPauseCFCDeltaAvg", 9), ("txPauseCFCDeltaMax", 10), ("txPauseCFCDeltaMin", 11), ("txPausePFCDelta", 12), ("txPausePFCDeltaAvg", 13), ("txPausePFCDeltaMax", 14), ("txPausePFCDeltaMin", 15))

class CucsAdaptorMenloMcpuErrorStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("popErrorsDelta", 4), ("popErrorsDeltaAvg", 5), ("popErrorsDeltaMax", 6), ("popErrorsDeltaMin", 7), ("pushErrorsDelta", 8), ("pushErrorsDeltaAvg", 9), ("pushErrorsDeltaMax", 10), ("pushErrorsDeltaMin", 11), ("uncorrectableErrorsDelta", 12), ("uncorrectableErrorsDeltaAvg", 13), ("uncorrectableErrorsDeltaMax", 14), ("uncorrectableErrorsDeltaMin", 15))

class CucsAdaptorMenloMcpuErrorStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("popErrorsDelta", 4), ("popErrorsDeltaAvg", 5), ("popErrorsDeltaMax", 6), ("popErrorsDeltaMin", 7), ("pushErrorsDelta", 8), ("pushErrorsDeltaAvg", 9), ("pushErrorsDeltaMax", 10), ("pushErrorsDeltaMin", 11), ("uncorrectableErrorsDelta", 12), ("uncorrectableErrorsDeltaAvg", 13), ("uncorrectableErrorsDeltaMax", 14), ("uncorrectableErrorsDeltaMin", 15))

class CucsAdaptorMenloMcpuStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropAclDelta", 0), ("dropAclDeltaAvg", 1), ("dropAclDeltaMax", 2), ("dropAclDeltaMin", 3), ("dropOverrunDelta", 4), ("dropOverrunDeltaAvg", 5), ("dropOverrunDeltaMax", 6), ("dropOverrunDeltaMin", 7), ("dropRuntDelta", 8), ("dropRuntDeltaAvg", 9), ("dropRuntDeltaMax", 10), ("dropRuntDeltaMin", 11), ("truncateOverrunDelta", 12), ("truncateOverrunDeltaAvg", 13), ("truncateOverrunDeltaMax", 14), ("truncateOverrunDeltaMin", 15))

class CucsAdaptorMenloMcpuStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropAclDelta", 0), ("dropAclDeltaAvg", 1), ("dropAclDeltaMax", 2), ("dropAclDeltaMin", 3), ("dropOverrunDelta", 4), ("dropOverrunDeltaAvg", 5), ("dropOverrunDeltaMax", 6), ("dropOverrunDeltaMin", 7), ("dropRuntDelta", 8), ("dropRuntDeltaAvg", 9), ("dropRuntDeltaMax", 10), ("dropRuntDeltaMin", 11), ("truncateOverrunDelta", 12), ("truncateOverrunDeltaAvg", 13), ("truncateOverrunDeltaMax", 14), ("truncateOverrunDeltaMin", 15))

class CucsAdaptorMenloNetEgStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropCmdDelta", 0), ("dropCmdDeltaAvg", 1), ("dropCmdDeltaMax", 2), ("dropCmdDeltaMin", 3), ("dropLifCfgInvalidDelta", 4), ("dropLifCfgInvalidDeltaAvg", 5), ("dropLifCfgInvalidDeltaMax", 6), ("dropLifCfgInvalidDeltaMin", 7), ("dropLifMapNoHitDelta", 8), ("dropLifMapNoHitDeltaAvg", 9), ("dropLifMapNoHitDeltaMax", 10), ("dropLifMapNoHitDeltaMin", 11), ("dropSrcBindDelta", 12), ("dropSrcBindDeltaAvg", 13), ("dropSrcBindDeltaMax", 14), ("dropSrcBindDeltaMin", 15), ("learnReqDropDelta", 16), ("learnReqDropDeltaAvg", 17), ("learnReqDropDeltaMax", 18), ("learnReqDropDeltaMin", 19))

class CucsAdaptorMenloNetEgStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropCmdDelta", 0), ("dropCmdDeltaAvg", 1), ("dropCmdDeltaMax", 2), ("dropCmdDeltaMin", 3), ("dropLifCfgInvalidDelta", 4), ("dropLifCfgInvalidDeltaAvg", 5), ("dropLifCfgInvalidDeltaMax", 6), ("dropLifCfgInvalidDeltaMin", 7), ("dropLifMapNoHitDelta", 8), ("dropLifMapNoHitDeltaAvg", 9), ("dropLifMapNoHitDeltaMax", 10), ("dropLifMapNoHitDeltaMin", 11), ("dropSrcBindDelta", 12), ("dropSrcBindDeltaAvg", 13), ("dropSrcBindDeltaMax", 14), ("dropSrcBindDeltaMin", 15), ("learnReqDropDelta", 16), ("learnReqDropDeltaAvg", 17), ("learnReqDropDeltaMax", 18), ("learnReqDropDeltaMin", 19))

class CucsAdaptorMenloNetInStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropFcLifInvalidDelta", 0), ("dropFcLifInvalidDeltaAvg", 1), ("dropFcLifInvalidDeltaMax", 2), ("dropFcLifInvalidDeltaMin", 3), ("dropFcMulticastDelta", 4), ("dropFcMulticastDeltaAvg", 5), ("dropFcMulticastDeltaMax", 6), ("dropFcMulticastDeltaMin", 7), ("dropNullPifDelta", 8), ("dropNullPifDeltaAvg", 9), ("dropNullPifDeltaMax", 10), ("dropNullPifDeltaMin", 11), ("fwdLookupNoHitDelta", 12), ("fwdLookupNoHitDeltaAvg", 13), ("fwdLookupNoHitDeltaMax", 14), ("fwdLookupNoHitDeltaMin", 15))

class CucsAdaptorMenloNetInStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropFcLifInvalidDelta", 0), ("dropFcLifInvalidDeltaAvg", 1), ("dropFcLifInvalidDeltaMax", 2), ("dropFcLifInvalidDeltaMin", 3), ("dropFcMulticastDelta", 4), ("dropFcMulticastDeltaAvg", 5), ("dropFcMulticastDeltaMax", 6), ("dropFcMulticastDeltaMin", 7), ("dropNullPifDelta", 8), ("dropNullPifDeltaAvg", 9), ("dropNullPifDeltaMax", 10), ("dropNullPifDeltaMin", 11), ("fwdLookupNoHitDelta", 12), ("fwdLookupNoHitDeltaAvg", 13), ("fwdLookupNoHitDeltaMax", 14), ("fwdLookupNoHitDeltaMin", 15))

class CucsAdaptorMenloQErrorStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("popErrorsDelta", 4), ("popErrorsDeltaAvg", 5), ("popErrorsDeltaMax", 6), ("popErrorsDeltaMin", 7), ("pushErrorsDelta", 8), ("pushErrorsDeltaAvg", 9), ("pushErrorsDeltaMax", 10), ("pushErrorsDeltaMin", 11), ("uncorrectableErrorsDelta", 12), ("uncorrectableErrorsDeltaAvg", 13), ("uncorrectableErrorsDeltaMax", 14), ("uncorrectableErrorsDeltaMin", 15))

class CucsAdaptorMenloQErrorStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("correctableErrorsDelta", 0), ("correctableErrorsDeltaAvg", 1), ("correctableErrorsDeltaMax", 2), ("correctableErrorsDeltaMin", 3), ("popErrorsDelta", 4), ("popErrorsDeltaAvg", 5), ("popErrorsDeltaMax", 6), ("popErrorsDeltaMin", 7), ("pushErrorsDelta", 8), ("pushErrorsDeltaAvg", 9), ("pushErrorsDeltaMax", 10), ("pushErrorsDeltaMin", 11), ("uncorrectableErrorsDelta", 12), ("uncorrectableErrorsDeltaAvg", 13), ("uncorrectableErrorsDeltaMax", 14), ("uncorrectableErrorsDeltaMin", 15))

class CucsAdaptorMenloQStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropOverrunN0Delta", 0), ("dropOverrunN0DeltaAvg", 1), ("dropOverrunN0DeltaMax", 2), ("dropOverrunN0DeltaMin", 3), ("dropOverrunN1Delta", 4), ("dropOverrunN1DeltaAvg", 5), ("dropOverrunN1DeltaMax", 6), ("dropOverrunN1DeltaMin", 7), ("truncateOverrunN0Delta", 8), ("truncateOverrunN0DeltaAvg", 9), ("truncateOverrunN0DeltaMax", 10), ("truncateOverrunN0DeltaMin", 11), ("truncateOverrunN1Delta", 12), ("truncateOverrunN1DeltaAvg", 13), ("truncateOverrunN1DeltaMax", 14), ("truncateOverrunN1DeltaMin", 15))

class CucsAdaptorMenloQStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dropOverrunN0Delta", 0), ("dropOverrunN0DeltaAvg", 1), ("dropOverrunN0DeltaMax", 2), ("dropOverrunN0DeltaMin", 3), ("dropOverrunN1Delta", 4), ("dropOverrunN1DeltaAvg", 5), ("dropOverrunN1DeltaMax", 6), ("dropOverrunN1DeltaMin", 7), ("truncateOverrunN0Delta", 8), ("truncateOverrunN0DeltaAvg", 9), ("truncateOverrunN0DeltaMax", 10), ("truncateOverrunN0DeltaMin", 11), ("truncateOverrunN1Delta", 12), ("truncateOverrunN1DeltaAvg", 13), ("truncateOverrunN1DeltaMax", 14), ("truncateOverrunN1DeltaMin", 15))

class CucsAdaptorMenloQueueStatsComponent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("cpu", 1), ("eth", 2), ("fc", 3), ("n", 4))

class CucsAdaptorMenloStatsIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("n0", 1), ("n1", 2), ("n0A", 3), ("n0B", 4), ("n1A", 5), ("n1B", 6))

class CucsAdaptorMgmtCapMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("full", 1), ("partial", 2))

class CucsAdaptorMgmtCapOperPowerRequirement(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("standby", 1), ("full", 2))

class CucsAdaptorMgmtCapRebootActionOnDestructive(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("host", 1), ("adaptor", 2))

class CucsAdaptorNwMgmtCapApi(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("menlo", 1), ("palo", 2))

class CucsAdaptorNwMgmtCapMgmtTransport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("l2", 0), ("l3", 1))

class CucsAdaptorOffloadMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("virtual", 0), ("physical", 1), ("none", 2))

class CucsAdaptorPIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsAdaptorProtocolProfileConnectionTimeOut(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 255)

class CucsAdaptorProtocolProfileLunBusyRetryCount(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 60)

class CucsAdaptorPurpose(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unused", 0), ("general", 1), ("management", 2), ("utility", 3))

class CucsAdaptorReachability(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("a", 0), ("b", 1), ("unmanaged", 7))

class CucsAdaptorRssProfileReceiveSideScaling(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsAdaptorSanCapHostNvram(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("full", 2))

class CucsAdaptorUnitId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsAdaptorUnitExtnId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 5000)

class CucsAdaptorVnicStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bytesRxDelta", 0), ("bytesRxDeltaAvg", 1), ("bytesRxDeltaMax", 2), ("bytesRxDeltaMin", 3), ("bytesTxDelta", 4), ("bytesTxDeltaAvg", 5), ("bytesTxDeltaMax", 6), ("bytesTxDeltaMin", 7), ("droppedRxDelta", 8), ("droppedRxDeltaAvg", 9), ("droppedRxDeltaMax", 10), ("droppedRxDeltaMin", 11), ("droppedTxDelta", 12), ("droppedTxDeltaAvg", 13), ("droppedTxDeltaMax", 14), ("droppedTxDeltaMin", 15), ("errorsRxDelta", 16), ("errorsRxDeltaAvg", 17), ("errorsRxDeltaMax", 18), ("errorsRxDeltaMin", 19), ("errorsTxDelta", 20), ("errorsTxDeltaAvg", 21), ("errorsTxDeltaMax", 22), ("errorsTxDeltaMin", 23), ("packetsRxDelta", 24), ("packetsRxDeltaAvg", 25), ("packetsRxDeltaMax", 26), ("packetsRxDeltaMin", 27), ("packetsTxDelta", 28), ("packetsTxDeltaAvg", 29), ("packetsTxDeltaMax", 30), ("packetsTxDeltaMin", 31))

class CucsAdaptorVnicStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bytesRxDelta", 0), ("bytesRxDeltaAvg", 1), ("bytesRxDeltaMax", 2), ("bytesRxDeltaMin", 3), ("bytesTxDelta", 4), ("bytesTxDeltaAvg", 5), ("bytesTxDeltaMax", 6), ("bytesTxDeltaMin", 7), ("droppedRxDelta", 8), ("droppedRxDeltaAvg", 9), ("droppedRxDeltaMax", 10), ("droppedRxDeltaMin", 11), ("droppedTxDelta", 12), ("droppedTxDeltaAvg", 13), ("droppedTxDeltaMax", 14), ("droppedTxDeltaMin", 15), ("errorsRxDelta", 16), ("errorsRxDeltaAvg", 17), ("errorsRxDeltaMax", 18), ("errorsRxDeltaMin", 19), ("errorsTxDelta", 20), ("errorsTxDeltaAvg", 21), ("errorsTxDeltaMax", 22), ("errorsTxDeltaMin", 23), ("packetsRxDelta", 24), ("packetsRxDeltaAvg", 25), ("packetsRxDeltaMax", 26), ("packetsRxDeltaMin", 27), ("packetsTxDelta", 28), ("packetsTxDeltaAvg", 29), ("packetsTxDeltaMax", 30), ("packetsTxDeltaMin", 31))

class CucsAddressMACMask(TextualConvention, Counter64):
    status = 'current'

class CucsAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("operational", 1), ("floating", 2))

class CucsAddressUIDSuffxMask(TextualConvention, Counter64):
    status = 'current'

class CucsAddressWWNMask(TextualConvention, Counter64):
    status = 'current'

class CucsBiosBootDevGrpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 6, 16, 128))
    namedValues = NamedValues(("systemBootOrder", 0), ("fddOrder", 1), ("hddOrder", 2), ("cdOrder", 3), ("networkDeviceOrder", 6), ("internalEfiShell", 16), ("bevOrder", 128))

class CucsBiosBootDevOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("n1", 1), ("n2", 2), ("n3", 3), ("n4", 4))

class CucsBiosDefaultAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CucsBiosSupportedAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CucsBiosVfACPI10SupportVpACPI10Support(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 122, 123, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 122), ("enabled", 123), ("platformDefault", -2))

class CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 68, 69, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 68), ("enabled", 69), ("platformDefault", -2))

class CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 66, 67, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 66), ("enabled", 67), ("platformDefault", -2))

class CucsBiosVfBootOptionRetryVpBootOptionRetry(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 96, 97, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 96), ("enabled", 97), ("platformDefault", -2))

class CucsBiosVfCPUPerformanceVpCPUPerformance(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 175, 176, 177, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("enterprise", 175), ("highThroughput", 176), ("hpc", 177), ("platformDefault", -2))

class CucsBiosVfConsoleRedirectionVpBaudRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 131, 132, 133, 134, 135, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("n9600", 131), ("n19200", 132), ("n38400", 133), ("n57600", 134), ("n115200", 135), ("platformDefault", -2))

class CucsBiosVfConsoleRedirectionVpConsoleRedirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 77, 78, 130, 260, 261, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 77), ("serialPortA", 78), ("serialPortB", 130), ("enabled", 260), ("com0", 261), ("platformDefault", -2))

class CucsBiosVfConsoleRedirectionVpFlowControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 79, 80, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("none", 79), ("rtsCts", 80), ("platformDefault", -2))

class CucsBiosVfConsoleRedirectionVpLegacyOSRedirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 90, 91, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 90), ("enabled", 91), ("platformDefault", -2))

class CucsBiosVfConsoleRedirectionVpTerminalType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 86, 87, 88, 89, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("pcAnsi", 86), ("vt100", 87), ("vt100Plus", 88), ("vtUtf8", 89), ("platformDefault", -2))

class CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 170, 178, 179, 180, 181, 182, 183, 184, 185, 190, 191, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("all", 170), ("n1", 178), ("n2", 179), ("n3", 180), ("n4", 181), ("n5", 182), ("n6", 183), ("n7", 184), ("n8", 185), ("n9", 190), ("n10", 191), ("platformDefault", -2))

class CucsBiosVfDirectCacheAccessVpDirectCacheAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 28, 29, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 28), ("enabled", 29), ("platformDefault", -2))

class CucsBiosVfDramRefreshRateVpDramRefreshRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 262, 263, 264, 265))
    namedValues = NamedValues(("platformRecommended", 0), ("n1x", 262), ("n2x", 263), ("n3x", 264), ("n4x", 265))

class CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3, 4, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 3), ("enabled", 4), ("platformDefault", -2))

class CucsBiosVfExecuteDisableBitVpExecuteDisableBit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10, 11, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 10), ("enabled", 11), ("platformDefault", -2))

class CucsBiosVfFrontPanelLockoutVpFrontPanelLockout(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 60, 61, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 60), ("enabled", 61), ("platformDefault", -2))

class CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 154, 155, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 154), ("enabled", 155), ("platformDefault", -2))

class CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 156, 157, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("itIrRaid", 156), ("intelEsrtii", 157), ("platformDefault", -2))

class CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 5, 6, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 5), ("enabled", 6), ("platformDefault", -2))

class CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 1), ("enabled", 2), ("platformDefault", -2))

class CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 20, 21, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 20), ("enabled", 21), ("platformDefault", -2))

class CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 18, 19, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 18), ("enabled", 19), ("platformDefault", -2))

class CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 16, 17, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 16), ("enabled", 17), ("platformDefault", -2))

class CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 22, 23, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 22), ("enabled", 23), ("platformDefault", -2))

class CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 14, 15, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 14), ("enabled", 15), ("platformDefault", -2))

class CucsBiosVpIntelVirtualizationTechnology(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 12, 13, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 12), ("enabled", 13), ("platformDefault", -2))

class CucsBiosVfLvDIMMSupportVpLvDDRMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 138, 139, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("powerSavingMode", 138), ("performanceMode", 139), ("platformDefault", -2))

class CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 192, 193, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("autoMax", 192), ("n8", 193), ("platformDefault", -2))

class CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 54, 55, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 54), ("enabled", 55), ("platformDefault", -2))

class CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 56, 57, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 56), ("enabled", 57), ("platformDefault", -2))

class CucsBiosVfMirroringModeVpMirroringMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 142, 143, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("interSocket", 142), ("intraSocket", 143), ("platformDefault", -2))

class CucsBiosVfNUMAOptimizedVpNUMAOptimized(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 32, 33, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 32), ("enabled", 33), ("platformDefault", -2))

class CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 114, 115, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 114), ("enabled", 115), ("platformDefault", -2))

class CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 116, 162, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("powerOff", 116), ("reset", 162), ("platformDefault", -2))

class CucsBiosVfOSBootWatchdogTimerTimeOutVpOSBootWatchdogTimerPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 171, 172, 173, 174, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("n5Minutes", 171), ("n10Minutes", 172), ("n15Minutes", 173), ("n20Minutes", 174), ("platformDefault", -2))

class CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 254, 255, 256, 257, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("n5Minutes", 254), ("n10Minutes", 255), ("n15Minutes", 256), ("n20Minutes", 257), ("platformDefault", -2))

class CucsBiosVfOnboardSATAControllerVpOnboardSATAController(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 38, 39, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 38), ("enabled", 39), ("platformDefault", -2))

class CucsBiosVfOnboardSATAControllerVpSATAMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 40, 41, 42, 186, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("enhanced", 40), ("compatibility", 41), ("ahci", 42), ("swRaid", 186), ("platformDefault", -2))

class CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 252, 253, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 252), ("enabled", 253), ("platformDefault", -2))

class CucsBiosVfOptionROMEnableVpState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 208, 209, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 208), ("enabled", 209), ("platformDefault", -2))

class CucsBiosVfOptionROMLoadVpLoad(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 163, 164, 187, 188, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("enable", 163), ("disable", 164), ("enabled", 187), ("disabled", 188), ("platformDefault", -2))

class CucsBiosVfPCISlotOptionROMEnableVpSlot1State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 210, 211, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 210), ("enabled", 211), ("platformDefault", -2))

class CucsBiosVfPCISlotOptionROMEnableVpSlot2State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 212, 213, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 212), ("enabled", 213), ("platformDefault", -2))

class CucsBiosVfPCISlotOptionROMEnableVpSlot3State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 214, 215, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 214), ("enabled", 215), ("platformDefault", -2))

class CucsBiosVfPCISlotOptionROMEnableVpSlot4State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 216, 217, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 216), ("enabled", 217), ("platformDefault", -2))

class CucsBiosVfPCISlotOptionROMEnableVpSlot5State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 218, 219, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 218), ("enabled", 219), ("platformDefault", -2))

class CucsBiosVfPCISlotOptionROMEnableVpSlot6State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 266, 267))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 266), ("enabled", 267))

class CucsBiosVfPCISlotOptionROMEnableVpSlot7State(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 268, 269))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 268), ("enabled", 269))

class CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 220, 221, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 220), ("enabled", 221), ("platformDefault", -2))

class CucsBiosVfPOSTErrorPauseVpPOSTErrorPause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 102, 103, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 102), ("enabled", 103), ("platformDefault", -2))

class CucsBiosVfPackageCStateLimitVpPackageCStateLimit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 222, 223, 224, 225, 226, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("noLimit", 222), ("c0", 223), ("c1", 224), ("c3", 225), ("c6", 226), ("platformDefault", -2))

class CucsBiosVfProcessorC1EVpProcessorC1E(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 202, 203, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 202), ("enabled", 203), ("platformDefault", -2))

class CucsBiosVfProcessorC3ReportVpProcessorC3Report(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 108, 109, 136, 137, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 108), ("enabled", 109), ("acpiC2", 136), ("acpiC3", 137), ("platformDefault", -2))

class CucsBiosVfProcessorC6ReportVpProcessorC6Report(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 110, 111, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 110), ("enabled", 111), ("platformDefault", -2))

class CucsBiosVfProcessorC7ReportVpProcessorC7Report(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 206, 207, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 206), ("enabled", 207), ("platformDefault", -2))

class CucsBiosVfProcessorCStateVpProcessorCState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 200, 201, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 200), ("enabled", 201), ("platformDefault", -2))

class CucsBiosVfQuietBootVpQuietBoot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 100, 101, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 100), ("enabled", 101), ("platformDefault", -2))

class CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 70, 71, 72, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("stayOff", 70), ("lastState", 71), ("reset", 72), ("platformDefault", -2))

class CucsBiosVpSelectMemoryRASConfiguration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 30, 31, 124, 125, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("maximumPerformance", 30), ("mirroring", 31), ("lockstep", 124), ("sparing", 125), ("platformDefault", -2))

class CucsBiosVfSerialPortAEnableVpSerialPortAEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 44, 45, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 44), ("enabled", 45), ("platformDefault", -2))

class CucsBiosVfSparingModeVpSparingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 126, 127, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("dimmSparing", 126), ("rankSparing", 127), ("platformDefault", -2))

class CucsBiosVfSriovConfigVpSriov(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 258, 259, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 258), ("enabled", 259), ("platformDefault", -2))

class CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 198, 199, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("strict", 198), ("loose", 199), ("platformDefault", -2))

class CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 160, 161, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 160), ("enabled", 161), ("platformDefault", -2))

class CucsBiosVfUSBBootConfigVpLegacyUSBSupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 249, 250, 251, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 249), ("enabled", 250), ("auto", 251), ("platformDefault", -2))

class CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 106, 107, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 106), ("enabled", 107), ("platformDefault", -2))

class CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 196, 197, 204, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("disabled", 196), ("enable", 197), ("enabled", 204), ("platformDefault", -2))

class CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 194, 195, -2))
    namedValues = NamedValues(("platformRecommended", 0), ("highPerformance", 194), ("lowerIdlePower", 195), ("platformDefault", -2))

class CucsBmcSELCntEqptClassId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 142, 247, 605))
    namedValues = NamedValues(("unspecified", 0), ("processorUnit", 142), ("memoryUnit", 247), ("computeBoard", 605))

class CucsBmcSELCntEqptInstIdPropId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 360, 698))
    namedValues = NamedValues(("unspecified", 0), ("processorUnitId", 360), ("memoryUnitId", 698))

class CucsBmcSELCntStatsClassId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 882, 884, 886, 888, 935, 940))
    namedValues = NamedValues(("unspecified", 0), ("computePCIeFatalProtocolStats", 882), ("computePCIeFatalReceiveStats", 884), ("computePCIeFatalCompletionStats", 886), ("computePCIeFatalStats", 888), ("processorErrorStats", 935), ("memoryErrorStats", 940))

class CucsCallhomeAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class CucsCallhomeAlertGroup(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 100))
    namedValues = NamedValues(("diagnostic", 0), ("environmental", 1), ("unknown", 100))

class CucsCallhomeAlertGroups(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("system", 0), ("environmental", 1), ("linecard", 2), ("supervisor", 3), ("inventory", 4), ("test", 5), ("ciscoTac", 6), ("syslogPort", 7), ("license", 8), ("lifeCycle", 9), ("diagnostic", 10))

class CucsCallhomeAlertLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 100))
    namedValues = NamedValues(("debug", 0), ("normal", 1), ("notify", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6), ("fatal", 7), ("unknown", 100))

class CucsCallhomeAlertMessageSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 100))
    namedValues = NamedValues(("nosubtype", 0), ("test", 1), ("full", 2), ("delta", 3), ("minor", 4), ("major", 5), ("goldnormal", 6), ("goldminor", 7), ("goldmajor", 8), ("unknown", 100))

class CucsCallhomeAlertMessageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 100))
    namedValues = NamedValues(("inventory", 0), ("syslog", 1), ("test", 2), ("diag", 3), ("env", 4), ("conf", 5), ("unknown", 100))

class CucsCallhomeAlertThrottlingAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class CucsCallhomeEpConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("notApplied", 1))

class CucsCallhomeEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 274))
    namedValues = NamedValues(("nop", 0), ("configCallhome", 274))

class CucsCallhomeEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 274, 275, 276, 330, 331))
    namedValues = NamedValues(("nop", 0), ("configCallhomeBegin", 274), ("configCallhomeSetLocal", 275), ("configCallhomeSetPeer", 276), ("configCallhomeFail", 330), ("configCallhomeSuccess", 331))

class CucsCallhomeEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 274))
    namedValues = NamedValues(("nop", 0), ("configCallhome", 274))

class CucsCallhomeFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("xml", 1), ("fullTxt", 2), ("shortTxt", 4))

class CucsCallhomeLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("debug", 0), ("normal", 1), ("notification", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6), ("fatal", 7), ("disaster", 8))

class CucsCallhomePolicyAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCallhomeUrgency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

class CucsCapabilityAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("restart", 0), ("idle", 1))

class CucsCapabilityCatalogueFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 609, 904))
    namedValues = NamedValues(("nop", 0), ("deployCatalogue", 609), ("activateCatalog", 904))

class CucsCapabilityCatalogueFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 904, 905, 906, 907, 908, 909, 936, 937))
    namedValues = NamedValues(("nop", 0), ("deployCatalogueBegin", 609), ("deployCatalogueSyncBladeAGLocal", 610), ("deployCatalogueSyncBladeAGRemote", 611), ("deployCatalogueSyncNicAGLocal", 612), ("deployCatalogueSyncNicAGRemote", 613), ("deployCatalogueSyncPortAGLocal", 614), ("deployCatalogueSyncPortAGRemote", 615), ("deployCatalogueSyncHostagentAGLocal", 616), ("deployCatalogueSyncHostagentAGRemote", 617), ("deployCatalogueFinalize", 618), ("deployCatalogueFail", 619), ("deployCatalogueSuccess", 620), ("activateCatalogBegin", 904), ("activateCatalogUnpackLocal", 905), ("activateCatalogCopyRemote", 906), ("activateCatalogApplyCatalog", 907), ("activateCatalogRescanImages", 908), ("activateCatalogEvaluateStatus", 909), ("activateCatalogFail", 936), ("activateCatalogSuccess", 937))

class CucsCapabilityCatalogueFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 839, 893))
    namedValues = NamedValues(("nop", 0), ("deployCatalogue", 839), ("activateCatalog", 893))

class CucsCapabilityFeatureStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("supported", 0), ("unsupported", 1))

class CucsCapabilityMgmtExtensionFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 910))
    namedValues = NamedValues(("nop", 0), ("activateMgmtExt", 910))

class CucsCapabilityMgmtExtensionFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 910, 911, 912, 913, 914, 915, 938, 939))
    namedValues = NamedValues(("nop", 0), ("activateMgmtExtBegin", 910), ("activateMgmtExtUnpackLocal", 911), ("activateMgmtExtCopyRemote", 912), ("activateMgmtExtApplyCatalog", 913), ("activateMgmtExtRescanImages", 914), ("activateMgmtExtEvaluateStatus", 915), ("activateMgmtExtFail", 938), ("activateMgmtExtSuccess", 939))

class CucsCapabilityMgmtExtensionFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 899))
    namedValues = NamedValues(("nop", 0), ("activateMgmtExt", 899))

class CucsCapabilityOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("init", 0), ("downloading", 1), ("downloaded", 2), ("applied", 3), ("failed", 4))

class CucsCapabilityPlatform(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ucs6100", 0), ("ucs6200", 1))

class CucsCapabilityUpdaterFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 582))
    namedValues = NamedValues(("nop", 0), ("updater", 582))

class CucsCapabilityUpdaterFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 582, 583, 584, 585, 586, 587, 588, 589, 590, 903))
    namedValues = NamedValues(("nop", 0), ("updaterBegin", 582), ("updaterLocal", 583), ("updaterUnpackLocal", 584), ("updaterDeleteLocal", 585), ("updaterCopyRemote", 586), ("updaterApply", 587), ("updaterRescanImages", 588), ("updaterFail", 589), ("updaterSuccess", 590), ("updaterEvaluateStatus", 903))

class CucsCapabilityUpdaterFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 582))
    namedValues = NamedValues(("nop", 0), ("updater", 582))

class CucsChangeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("modified", 0), ("created", 1), ("deleted", 2), ("intentDeletion", 3))

class CucsCommAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("fullssl", 0), ("noencssl", 1), ("plain", 2))

class CucsCommCipherSuiteMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("highStrength", 1), ("mediumStrength", 2), ("lowStrength", 3), ("custom", 4))

class CucsCommClientAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommDnsProviderAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommFilePathProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("workspace", 1), ("volatile", 2), ("ftp", 3), ("tftp", 4), ("scp", 5), ("sftp", 6))

class CucsCommHttpRedirectState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommNtpProviderAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tcp", 1), ("udp", 2), ("all", 3))

class CucsCommShellProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tcp", 1), ("udp", 2), ("all", 3))

class CucsCommSmashCLPProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tcp", 1), ("udp", 2), ("all", 3))

class CucsCommSnmpConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("notApplied", 1))

class CucsCommSnmpProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tcp", 1), ("udp", 2), ("all", 3))

class CucsCommSnmpAuth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha", 2))

class CucsCommSnmpNotificationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("traps", 1), ("informs", 2))

class CucsCommSnmpV3Privilege(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auth", 1), ("noauth", 2), ("priv", 3))

class CucsCommSnmpVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("v1", 1), ("v2c", 2), ("v3", 3))

class CucsCommSvcEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 190, 193))
    namedValues = NamedValues(("nop", 0), ("updateSvcEp", 190), ("restartWebSvc", 193))

class CucsCommSvcEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 190, 191, 192, 193, 332, 333, 334, 335, 532, 592, 593, 877, 878, 1046, 1047, 1165, 1166))
    namedValues = NamedValues(("nop", 0), ("updateSvcEpBegin", 190), ("updateSvcEpSetEpLocal", 191), ("updateSvcEpSetEpPeer", 192), ("restartWebSvcBegin", 193), ("restartWebSvcFail", 332), ("restartWebSvcSuccess", 333), ("updateSvcEpFail", 334), ("updateSvcEpSuccess", 335), ("updateSvcEpPropogateEpSettings", 532), ("updateSvcEpPropogateEpTimeZoneSettingsLocal", 592), ("updateSvcEpPropogateEpTimeZoneSettingsPeer", 593), ("updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsLocal", 877), ("updateSvcEpPropogateEpTimeZoneSettingsToAdaptorsPeer", 878), ("updateSvcEpPropogateEpTimeZoneSettingsToFexIomLocal", 1046), ("updateSvcEpPropogateEpTimeZoneSettingsToFexIomPeer", 1047), ("restartWebSvcLocal", 1165), ("restartWebSvcPeer", 1166))

class CucsCommSvcEpFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeCommSvcEpUpdateSvcEpEpChange", 21), ("samDmeCommSvcEpUpdateSvcEpPropogateSettings", 22))

class CucsCommSvcEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 190, 193))
    namedValues = NamedValues(("nop", 0), ("updateSvcEp", 190), ("restartWebSvc", 193))

class CucsCommSyslogProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tcp", 1), ("udp", 2), ("all", 3))

class CucsCommSyslogAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommSyslogClientEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("primary", 1), ("secondary", 2), ("tertiary", 3))

class CucsCommSyslogFileSize(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(4096, 4194304)

class CucsCommSyslogForwardingFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("local0", 0), ("local1", 1), ("local2", 2), ("local3", 3), ("local4", 4), ("local5", 5), ("local6", 6), ("local7", 7))

class CucsCommSyslogRestrictedSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("emergencies", 0), ("alerts", 1), ("critical", 2))

class CucsCommSyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergencies", 0), ("alerts", 1), ("critical", 2), ("errors", 3), ("warnings", 4), ("notifications", 5), ("information", 6), ("debugging", 7))

class CucsCommSyslogSourceAudits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommSyslogSourceEvents(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommSyslogSourceFaults(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsCommTimeZoneConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("success", 0), ("failure", 1))

class CucsCommWebProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("tcp", 1), ("udp", 2), ("all", 3))

class CucsCommXmlClConnPolicyClientType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("javaUi", 0), ("flexUi", 1), ("extrenalApiClient", 2))

class CucsComputeAdminLinkAggregation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("portChannel", 1), ("global", 2))

class CucsComputeAdminPowerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 12, 13, 14, 15, 16, 30, 31, 32, 33))
    namedValues = NamedValues(("cycleImmediate", 2), ("cycleWait", 3), ("hardResetImmediate", 4), ("hardResetWait", 5), ("cmosResetImmediate", 12), ("bmcResetImmediate", 13), ("bmcResetWait", 14), ("diagnosticInterrupt", 15), ("kvmReset", 16), ("policy", 30), ("adminUp", 31), ("adminDown", 32), ("ipmiReset", 33))

class CucsComputeAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2))

class CucsComputeAdminTrigger(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undiscovered", 0), ("rediscover", 1), ("resetToFactory", 2), ("discovered", 3), ("remove", 4), ("migrate", 5), ("decommission", 6), ("upgradeFirmware", 7))

class CucsComputeAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("minor", 1), ("severe", 2))

class CucsComputeAssociation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("establishing", 1), ("associated", 2), ("removing", 3), ("failed", 4), ("throttled", 5))

class CucsComputeAvailability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unavailable", 0), ("available", 1))

class CucsComputeBladeSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsComputeBladeFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 23, 144, 604, 665, 727, 767, 769, 771, 773, 775, 777, 781, 785, 789, 792, 806, 815, 879, 891, 898, 932, 934, 1036, 1055, 1152, 1157, 1254, 1256, 1478))
    namedValues = NamedValues(("nop", 0), ("discover", 23), ("diag", 144), ("updateBoardController", 604), ("associate", 665), ("disassociate", 727), ("powerCap", 767), ("decommission", 769), ("softShutdown", 771), ("hardShutdown", 773), ("turnup", 775), ("powercycle", 777), ("hardreset", 781), ("softreset", 785), ("swConnUpd", 789), ("biosRecovery", 792), ("cmosReset", 806), ("resetBmc", 815), ("updateExtUsers", 879), ("updateAdaptor", 891), ("activateAdaptor", 898), ("configSoL", 932), ("unconfigSoL", 934), ("diagnosticInterrupt", 1036), ("resetKvm", 1055), ("updateBIOS", 1152), ("activateBIOS", 1157), ("resetIpmi", 1254), ("fwUpgrade", 1256), ("cimcSessionDelete", 1478))

class CucsComputeBladeFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 23, 24, 25, 26, 27, 28, 29, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 144, 145, 146, 147, 148, 149, 152, 153, 155, 156, 158, 159, 160, 161, 162, 165, 166, 167, 168, 171, 172, 173, 174, 176, 177, 178, 180, 181, 182, 183, 458, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 504, 519, 520, 521, 526, 527, 528, 529, 530, 531, 533, 534, 535, 545, 567, 591, 599, 604, 605, 606, 607, 608, 621, 622, 629, 647, 648, 649, 650, 651, 652, 653, 654, 657, 658, 659, 660, 663, 664, 665, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 806, 807, 808, 809, 810, 811, 812, 815, 816, 879, 880, 891, 892, 893, 894, 895), SingleValueConstraint(896, 897, 898, 899, 900, 901, 902, 932, 933, 934, 935, 940, 941, 942, 943, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 1019, 1020, 1021, 1022, 1032, 1033, 1036, 1037, 1038, 1039, 1040, 1055, 1056, 1057, 1058, 1069, 1070, 1071, 1072, 1078, 1079, 1080, 1089, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1178, 1179, 1180, 1181, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1361, 1363, 1385, 1386, 1387, 1388, 1471, 1472, 1473, 1478, 1479, 1480, 1481))
    namedValues = NamedValues(("nop", 0), ("discoverBegin", 23), ("discoverBmcPresence", 24), ("discoverBmcInventory", 25), ("discoverConfigFeLocal", 26), ("discoverConfigFePeer", 27), ("discoverConfigUserAccess", 28), ("discoverBladePowerOn", 29), ("discoverSwConfigPnuOSLocal", 33), ("discoverSwConfigPnuOSPeer", 34), ("discoverBladeBootPnuos", 35), ("discoverBladeReadSmbios", 36), ("discoverHagConnect", 37), ("discoverPnuOSIdent", 38), ("discoverPnuOSPolicy", 39), ("discoverPnuOSInventory", 40), ("discoverPnuOSSelfTest", 41), ("discoverSwUnconfigPnuOSLocal", 43), ("discoverSwUnconfigPnuOSPeer", 44), ("discoverHagDisconnect", 45), ("discoverBmcShutdownDiscovered", 46), ("discoverHandlePooling", 47), ("discoverSuccess", 48), ("discoverFail", 49), ("diagBegin", 144), ("diagBmcPresence", 145), ("diagBmcInventory", 146), ("diagConfigFeLocal", 147), ("diagConfigFePeer", 148), ("diagBladePowerOn", 149), ("diagDeriveConfig", 152), ("diagConfigUserAccess", 153), ("diagSwConfigLocal", 155), ("diagSwConfigPeer", 156), ("diagSetupVMediaLocal", 158), ("diagSetupVMediaPeer", 159), ("diagBladeBoot", 160), ("diagBladeReadSmbios", 161), ("diagHostConnect", 162), ("diagHostIdent", 165), ("diagHostPolicy", 166), ("diagSetDiagUser", 167), ("diagHostInventory", 168), ("diagGenerateReport", 171), ("diagRemoveConfig", 172), ("diagRemoveVMediaLocal", 173), ("diagRemoveVMediaPeer", 174), ("diagSwUnconfigLocal", 176), ("diagSwUnconfigPeer", 177), ("diagUnconfigUserAccess", 178), ("diagHostDisconnect", 180), ("diagBmcShutdownDiagCompleted", 181), ("diagSuccess", 182), ("diagFail", 183), ("discoverPnuOSScrub", 458), ("diagHostServerDiag", 479), ("diagHostServerDiagStatus", 480), ("diagDisableServerConnSwB", 481), ("diagStartFabricATrafficTest", 482), ("diagFabricATrafficTestStatus", 483), ("diagEnableServerConnSwB", 484), ("diagDisableServerConnSwA", 485), ("diagStartFabricBTrafficTest", 486), ("diagFabricBTrafficTestStatus", 487), ("diagEnableServerConnSwA", 488), ("discoverBladeBootWait", 504), ("diagBladeBootWait", 519), ("diagBiosPostCompletion", 520), ("discoverBiosPostCompletion", 521), ("diagRestoreConfigFeLocal", 526), ("diagRestoreConfigFePeer", 527), ("discoverSetupVmediaLocal", 528), ("discoverSetupVmediaPeer", 529), ("discoverTeardownVmediaLocal", 530), ("discoverTeardownVmediaPeer", 531), ("diagGenerateLogWait", 533), ("diagStopVMediaLocal", 534), ("diagStopVMediaPeer", 535), ("discoverSanitize", 545), ("discoverPreSanitize", 567), ("diagDebugWait", 591), ("diagEvaluateStatus", 599), ("updateBoardControllerBegin", 604), ("updateBoardControllerBladePowerOff", 605), ("updateBoardControllerUpdateRequest", 606), ("updateBoardControllerPollUpdateStatus", 607), ("updateBoardControllerBladePowerOn", 608), ("updateBoardControllerFail", 621), ("updateBoardControllerSuccess", 622), ("updateBoardControllerPrepareForUpdate", 629), ("diagNicPresenceLocal", 647), ("diagNicPresencePeer", 648), ("diagNicInventoryLocal", 649), ("diagNicInventoryPeer", 650), ("diagNicConfigLocal", 651), ("diagNicConfigPeer", 652), ("diagNicUnconfigLocal", 653), ("diagNicUnconfigPeer", 654), ("discoverNicPresenceLocal", 657), ("discoverNicPresencePeer", 658), ("discoverNicConfigPnuOSLocal", 659), ("discoverNicConfigPnuOSPeer", 660), ("discoverNicUnconfigPnuOSLocal", 663), ("discoverNicUnconfigPnuOSPeer", 664), ("associateBegin", 665), ("associateUpdateIBMCFw", 668), ("associateWaitForIBMCFwUpdate", 669), ("associateActivateIBMCFw", 670), ("associateResetIBMC", 671), ("associatePreSanitize", 672), ("associateSanitize", 673), ("associateConfigUserAccess", 674), ("associateBladePowerOff", 675), ("associateUpdateBoardCtrlRequest", 676), ("associatePollBoardCtrlUpdateStatus", 677), ("associatePowerOn", 678), ("associateBmcPreconfigPnuOSLocal", 679), ("associateBmcPreconfigPnuOSPeer", 680), ("associateBmcConfigPnuOS", 681), ("associateSwConfigPnuOSLocal", 682), ("associateSwConfigPnuOSPeer", 683), ("associateUpdateAdaptorNwFwLocal", 684), ("associateUpdateAdaptorNwFwPeer", 685), ("associateWaitForAdaptorNwFwUpdateLocal", 686), ("associateWaitForAdaptorNwFwUpdatePeer", 687), ("associateActivateAdaptorNwFwLocal", 688), ("associateActivateAdaptorNwFwPeer", 689), ("associateNicConfigPnuOSLocal", 690), ("associateNicConfigPnuOSPeer", 691), ("associateBootPnuos", 692), ("associateBootWait", 693), ("associateBiosPostCompletion", 694), ("associateHagPnuOSConnect", 695), ("associatePnuOSIdent", 696), ("associatePnuOSPolicy", 697), ("associatePnuOSValidate", 698), ("associatePnuOSSelfTest", 699), ("associateBiosImgUpdate", 700), ("associateStorageCtlrImgUpdate", 701), ("associateHbaImgUpdate", 702), ("associateNicImgUpdate", 703), ("associatePnuOSInventory", 704), ("associatePnuOSConfig", 705), ("associatePnuOSLocalDiskConfig", 706), ("associatePnuOSUnloadDrivers", 707), ("associateBmcUnconfigPnuOS", 708), ("associateNicUnconfigPnuOSLocal", 709), ("associateNicUnconfigPnuOSPeer", 710), ("associateSwUnconfigPnuOSLocal", 711), ("associateSwUnconfigPnuOSPeer", 712), ("associateSwConfigHostOSLocal", 713), ("associateSwConfigHostOSPeer", 714), ("associateNicConfigHostOSLocal", 715), ("associateNicConfigHostOSPeer", 716), ("associateHagPnuOSDisconnect", 717), ("associateConfigSoL", 718), ("associatePrepareForBoot", 719), ("associateConfigUuid", 720), ("associateBootHost", 721), ("associateHagHostOSConnect", 722), ("associateHostOSIdent", 723), ("associateHostOSPolicy", 724), ("associateHostOSValidate", 725), ("associateHostOSConfig", 726), ("disassociateBegin", 727), ("disassociateConfigUserAccess", 730), ("disassociatePowerOn", 731), ("disassociatePreSanitize", 732), ("disassociateSanitize", 733), ("disassociateNicUnconfigHostOSLocal", 734), ("disassociateNicUnconfigHostOSPeer", 735), ("disassociateSwUnconfigHostOSLocal", 736), ("disassociateSwUnconfigHostOSPeer", 737), ("disassociateBmcPreconfigPnuOSLocal", 738), ("disassociateBmcPreconfigPnuOSPeer", 739), ("disassociateBmcConfigPnuOS", 740), ("disassociateSwConfigPnuOSLocal", 741), ("disassociateSwConfigPnuOSPeer", 742), ("disassociateNicConfigPnuOSLocal", 743), ("disassociateNicConfigPnuOSPeer", 744), ("disassociateConfigBios", 745), ("disassociateBootPnuos", 746), ("disassociateBootWait", 747), ("disassociateBiosPostCompletion", 748), ("disassociateHagPnuOSConnect", 749), ("disassociatePnuOSIdent", 750), ("disassociatePnuOSPolicy", 751), ("disassociatePnuOSValidate", 752), ("disassociatePnuOSUnconfig", 753), ("disassociatePnuOSScrub", 754), ("disassociatePnuOSSelfTest", 755), ("disassociateBmcUnconfigPnuOS", 756), ("disassociateNicUnconfigPnuOSLocal", 757), ("disassociateNicUnconfigPnuOSPeer", 758), ("disassociateHagPnuOSDisconnect", 759), ("disassociateUnconfigUuid", 760), ("disassociateShutdown", 761), ("disassociateUnconfigBios", 762), ("disassociateSwUnconfigPnuOSLocal", 763), ("disassociateSwUnconfigPnuOSPeer", 764), ("disassociateUnconfigSoL", 765), ("disassociateHandlePooling", 766), ("powerCapBegin", 767), ("powerCapConfig", 768), ("decommissionBegin", 769), ("decommissionExecute", 770), ("softShutdownBegin", 771), ("softShutdownExecute", 772), ("hardShutdownBegin", 773), ("hardShutdownExecute", 774), ("turnupBegin", 775), ("turnupExecute", 776), ("powercycleBegin", 777), ("powercyclePreSanitize", 778), ("powercycleSanitize", 779), ("powercycleExecute", 780), ("hardresetBegin", 781), ("hardresetPreSanitize", 782), ("hardresetSanitize", 783), ("hardresetExecute", 784), ("softresetBegin", 785), ("softresetPreSanitize", 786), ("softresetSanitize", 787), ("softresetExecute", 788), ("swConnUpdBegin", 789), ("swConnUpdA", 790), ("swConnUpdB", 791), ("biosRecoveryBegin", 792), ("biosRecoveryShutdown", 793), ("biosRecoveryPreSanitize", 794), ("biosRecoverySanitize", 795), ("biosRecoverySetupVmediaLocal", 796), ("biosRecoverySetupVmediaPeer", 797), ("biosRecoveryStart", 798), ("biosRecoveryWait", 799), ("biosRecoveryCleanup", 800), ("biosRecoveryReset", 801), ("biosRecoveryTeardownVmediaLocal", 802), ("biosRecoveryTeardownVmediaPeer", 803), ("cmosResetBegin", 806), ("cmosResetPreSanitize", 807), ("cmosResetSanitize", 808), ("cmosResetExecute", 809), ("cmosResetReconfigBios", 810), ("cmosResetReconfigUuid", 811), ("cmosResetBladePowerOn", 812), ("resetBmcBegin", 815), ("resetBmcExecute", 816), ("updateExtUsersBegin", 879), ("updateExtUsersDeploy", 880), ("updateAdaptorBegin", 891), ("updateAdaptorPowerOn", 892), ("updateAdaptorUpdateRequestLocal", 893), ("updateAdaptorUpdateRequestPeer", 894), ("updateAdaptorPollUpdateStatusLocal", 895)) + NamedValues(("updateAdaptorPollUpdateStatusPeer", 896), ("updateAdaptorPowerOff", 897), ("activateAdaptorBegin", 898), ("activateAdaptorPowerOn", 899), ("activateAdaptorActivateLocal", 900), ("activateAdaptorActivatePeer", 901), ("activateAdaptorReset", 902), ("configSoLBegin", 932), ("configSoLExecute", 933), ("unconfigSoLBegin", 934), ("unconfigSoLExecute", 935), ("activateAdaptorFail", 940), ("activateAdaptorSuccess", 941), ("associateFail", 942), ("associateSuccess", 943), ("biosRecoveryFail", 946), ("biosRecoverySuccess", 947), ("cmosResetFail", 948), ("cmosResetSuccess", 949), ("configSoLFail", 950), ("configSoLSuccess", 951), ("decommissionFail", 952), ("decommissionSuccess", 953), ("disassociateFail", 954), ("disassociateSuccess", 955), ("hardShutdownFail", 956), ("hardShutdownSuccess", 957), ("hardresetFail", 958), ("hardresetSuccess", 959), ("powerCapFail", 960), ("powerCapSuccess", 961), ("powercycleFail", 962), ("powercycleSuccess", 963), ("resetBmcFail", 964), ("resetBmcSuccess", 965), ("softShutdownFail", 966), ("softShutdownSuccess", 967), ("softresetFail", 968), ("softresetSuccess", 969), ("swConnUpdFail", 970), ("swConnUpdSuccess", 971), ("turnupFail", 972), ("turnupSuccess", 973), ("unconfigSoLFail", 974), ("unconfigSoLSuccess", 975), ("updateAdaptorFail", 976), ("updateAdaptorSuccess", 977), ("updateExtUsersFail", 978), ("updateExtUsersSuccess", 979), ("decommissionStopVMediaLocal", 1019), ("decommissionStopVMediaPeer", 1020), ("biosRecoveryStopVMediaLocal", 1021), ("biosRecoveryStopVMediaPeer", 1022), ("diagCleanupServerConnSwA", 1032), ("diagCleanupServerConnSwB", 1033), ("diagnosticInterruptBegin", 1036), ("diagnosticInterruptExecute", 1037), ("diagnosticInterruptFail", 1038), ("diagnosticInterruptSuccess", 1039), ("associateLocalDiskFwUpdate", 1040), ("resetKvmBegin", 1055), ("resetKvmExecute", 1056), ("resetKvmFail", 1057), ("resetKvmSuccess", 1058), ("associateSwConfigPortNivLocal", 1069), ("associateSwConfigPortNivPeer", 1070), ("disassociateSwConfigPortNivLocal", 1071), ("disassociateSwConfigPortNivPeer", 1072), ("discoverBmcPreConfigPnuOSLocal", 1078), ("discoverBmcPreConfigPnuOSPeer", 1079), ("discoverBmcConfigPnuOS", 1080), ("diagBmcConfigPnuOS", 1089), ("diagSolRedirectEnable", 1096), ("diagSerialDebugConnect", 1097), ("diagSerialDebugDisconnect", 1098), ("diagSolRedirectDisable", 1099), ("discoverSolRedirectEnable", 1100), ("discoverSerialDebugConnect", 1101), ("discoverSerialDebugDisconnect", 1102), ("discoverSolRedirectDisable", 1103), ("associateSolRedirectEnable", 1104), ("associateSerialDebugPnuOSConnect", 1105), ("associateSerialDebugPnuOSDisconnect", 1106), ("associateSolRedirectDisable", 1107), ("disassociateSolRedirectEnable", 1108), ("disassociateSerialDebugPnuOSConnect", 1109), ("disassociateSerialDebugPnuOSDisconnect", 1110), ("disassociateSolRedirectDisable", 1111), ("decommissionCleanupCIMC", 1112), ("updateBIOSBegin", 1152), ("updateBIOSClear", 1153), ("updateBIOSPollClearStatus", 1154), ("updateBIOSUpdateRequest", 1155), ("updateBIOSPollUpdateStatus", 1156), ("activateBIOSBegin", 1157), ("activateBIOSPowerOff", 1158), ("activateBIOSClear", 1159), ("activateBIOSPollClearStatus", 1160), ("activateBIOSActivate", 1161), ("activateBIOSPollActivateStatus", 1162), ("activateBIOSUpdateTokens", 1163), ("activateBIOSPowerOn", 1164), ("diagHostCatalog", 1167), ("discoverPnuOSCatalog", 1168), ("associateClearBiosUpdate", 1169), ("associatePollClearBiosUpdateStatus", 1170), ("associateUpdateBiosRequest", 1171), ("associatePollBiosUpdateStatus", 1172), ("associateActivateBios", 1173), ("associatePollBiosActivateStatus", 1174), ("associatePnuOSCatalog", 1175), ("disassociatePnuOSCatalog", 1176), ("activateBIOSFail", 1178), ("activateBIOSSuccess", 1179), ("updateBIOSFail", 1180), ("updateBIOSSuccess", 1181), ("discoverCheckPowerAvailability", 1246), ("associateMarkAdapterForReboot", 1247), ("associateDeassertResetBypass", 1248), ("associateVerifyFcZoneConfig", 1249), ("disassociateDeassertResetBypass", 1250), ("disassociateVerifyFcZoneConfig", 1251), ("decommissionCleanupPortConfigLocal", 1252), ("decommissionCleanupPortConfigPeer", 1253), ("resetIpmiBegin", 1254), ("resetIpmiExecute", 1255), ("fwUpgradeBegin", 1256), ("fwUpgradeUpdateIBMCFw", 1257), ("fwUpgradeWaitForIBMCFwUpdate", 1258), ("fwUpgradeActivateIBMCFw", 1259), ("fwUpgradeResetIBMC", 1260), ("fwUpgradePreSanitize", 1261), ("fwUpgradeSanitize", 1262), ("fwUpgradeBladePowerOff", 1263), ("fwUpgradeUpdateBoardCtrlRequest", 1264), ("fwUpgradePollBoardCtrlUpdateStatus", 1265), ("fwUpgradeClearBiosUpdate", 1266), ("fwUpgradePollClearBiosUpdateStatus", 1267), ("fwUpgradeUpdateBiosRequest", 1268), ("fwUpgradePollBiosUpdateStatus", 1269), ("fwUpgradeActivateBios", 1270), ("fwUpgradePollBiosActivateStatus", 1271), ("fwUpgradePowerOn", 1272), ("fwUpgradeBmcPreconfigPnuOSLocal", 1273), ("fwUpgradeBmcPreconfigPnuOSPeer", 1274), ("fwUpgradeSwConfigPortNivLocal", 1275), ("fwUpgradeSwConfigPortNivPeer", 1276), ("fwUpgradeSwConfigPnuOSLocal", 1277), ("fwUpgradeSwConfigPnuOSPeer", 1278), ("fwUpgradeUpdateAdaptorNwFwLocal", 1279), ("fwUpgradeUpdateAdaptorNwFwPeer", 1280), ("fwUpgradeWaitForAdaptorNwFwUpdateLocal", 1281), ("fwUpgradeWaitForAdaptorNwFwUpdatePeer", 1282), ("fwUpgradeActivateAdaptorNwFwLocal", 1283), ("fwUpgradeActivateAdaptorNwFwPeer", 1284), ("fwUpgradeNicConfigPnuOSLocal", 1285), ("fwUpgradeNicConfigPnuOSPeer", 1286), ("fwUpgradeBmcConfigPnuOS", 1287), ("fwUpgradeSolRedirectEnable", 1288), ("fwUpgradeSerialDebugPnuOSConnect", 1289), ("fwUpgradeBootPnuos", 1290), ("fwUpgradeBootWait", 1291), ("fwUpgradeBiosPostCompletion", 1292), ("fwUpgradeHagPnuOSConnect", 1293), ("fwUpgradePnuOSIdent", 1294), ("fwUpgradePnuOSPolicy", 1295), ("fwUpgradePnuOSCatalog", 1296), ("fwUpgradePnuOSValidate", 1297), ("fwUpgradePnuOSSelfTest", 1298), ("fwUpgradeStorageCtlrImgUpdate", 1299), ("fwUpgradeHbaImgUpdate", 1300), ("fwUpgradeNicImgUpdate", 1301), ("fwUpgradeLocalDiskFwUpdate", 1302), ("fwUpgradePnuOSConfig", 1303), ("fwUpgradePnuOSInventory", 1304), ("fwUpgradeBiosImgUpdate", 1305), ("fwUpgradePnuOSUnloadDrivers", 1306), ("fwUpgradeBmcUnconfigPnuOS", 1307), ("fwUpgradeNicUnconfigPnuOSLocal", 1308), ("fwUpgradeNicUnconfigPnuOSPeer", 1309), ("fwUpgradeSwUnconfigPnuOSLocal", 1310), ("fwUpgradeSwUnconfigPnuOSPeer", 1311), ("fwUpgradeHagPnuOSDisconnect", 1312), ("fwUpgradeSerialDebugPnuOSDisconnect", 1313), ("fwUpgradeSolRedirectDisable", 1314), ("fwUpgradeShutdown", 1315), ("activateAdaptorDeassertResetBypass", 1361), ("fwUpgradeDeassertResetBypass", 1363), ("fwUpgradeFail", 1385), ("fwUpgradeSuccess", 1386), ("resetIpmiFail", 1387), ("resetIpmiSuccess", 1388), ("associateConfigFlexFlash", 1471), ("associateSyncPowerState", 1472), ("disassociateUnconfigFlexFlash", 1473), ("cimcSessionDeleteBegin", 1478), ("cimcSessionDeleteExecute", 1479), ("cimcSessionDeleteFail", 1480), ("cimcSessionDeleteSuccess", 1481))

class CucsComputeBladeFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeComputeBladeDiscoverCheckPoint", 0), ("samDmeComputeBladeDiagEfiDiag", 18), ("samDmeComputeBladeDiagDetailDiag", 20), ("samDmeComputeBladeDiagCancelDiag", 23))

class CucsComputeBladeFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 23, 144, 834))
    namedValues = NamedValues(("nop", 0), ("discover", 23), ("diag", 144), ("updateBoardController", 834))

class CucsComputeBoardPower(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 100))
    namedValues = NamedValues(("unknown", 0), ("on", 1), ("test", 2), ("off", 3), ("online", 4), ("offline", 5), ("offduty", 6), ("degraded", 7), ("powerSave", 8), ("error", 9), ("ok", 10), ("failed", 11), ("notSupported", 100))

class CucsComputeChassisConnPolicyChassisId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 255)

class CucsComputeChassisDiscAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("immediate", 0), ("userAcknowledged", 1), ("n1Link", 2), ("n2Link", 3), ("n4Link", 4), ("n8Link", 5), ("platformMax", 6))

class CucsComputeChassisQualMaxId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsComputeChassisQualMinId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsComputeCheckPoint(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("removing", 1), ("shallowCheckpoint", 2), ("deepCheckpoint", 3), ("discovered", 4))

class CucsComputeConnectivityRebalancing(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("immediate", 0), ("userAcknowledged", 1))

class CucsComputeDiscovery(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 8, 16, 32, 64, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137))
    namedValues = NamedValues(("undiscovered", 0), ("inProgress", 1), ("malformedFruInfo", 2), ("fruNotReady", 3), ("insufficientlyEquipped", 4), ("invalidAdaptorIocard", 5), ("failed", 8), ("complete", 16), ("retry", 32), ("throttled", 64), ("illegalFru", 128), ("fruIdentityIndeterminate", 129), ("fruStateIndeterminate", 130), ("diagnosticsInProgress", 131), ("efidiagnosticsInProgress", 132), ("diagnosticsFailed", 133), ("diagnosticsComplete", 134), ("waitingForUserAck", 135), ("userAcknowledged", 136), ("waitingForMgmtAck", 137))

class CucsComputeIOHubEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("temperature", 0), ("temperatureAvg", 1), ("temperatureMax", 2), ("temperatureMin", 3))

class CucsComputeIOHubEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("temperature", 0), ("temperatureAvg", 1), ("temperatureMax", 2), ("temperatureMin", 3))

class CucsComputeIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("computeThermal", 0), ("computeInoperable", 1), ("computeVoltage", 2), ("computePerf", 3), ("computePower", 4), ("removed", 5), ("config", 6), ("computePostFailure", 7), ("cpuThermal", 8), ("cpuInoperable", 9), ("cpuVoltage", 10), ("cpuPerf", 11), ("cpuPower", 12), ("memoryThermal", 13), ("memoryInoperable", 14), ("memoryVoltage", 15), ("memoryPerf", 16), ("memoryPower", 17), ("adaptorThermal", 18), ("adaptorInoperable", 19), ("adaptorVoltage", 20), ("adaptorPerf", 21), ("adaptorPower", 22), ("nicThermal", 23), ("nicInoperable", 24), ("nicVoltage", 25), ("nicPerf", 26), ("nicPower", 27), ("hbaThermal", 28), ("hbaInoperable", 29), ("hbaVoltage", 30), ("hbaPerf", 31), ("hbaPower", 32), ("mismatch", 33), ("powerInoperable", 34), ("networkMisconfig", 35))

class CucsComputeLinkAggregation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("portChannel", 1))

class CucsComputeLinkAggregationCap(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("portChannel", 0))

class CucsComputeMbPowerStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("consumedPower", 0), ("consumedPowerAvg", 1), ("consumedPowerMax", 2), ("consumedPowerMin", 3), ("inputCurrent", 4), ("inputCurrentAvg", 5), ("inputCurrentMax", 6), ("inputCurrentMin", 7), ("inputVoltage", 8), ("inputVoltageAvg", 9), ("inputVoltageMax", 10), ("inputVoltageMin", 11))

class CucsComputeMbPowerStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("consumedPower", 0), ("consumedPowerAvg", 1), ("consumedPowerMax", 2), ("consumedPowerMin", 3), ("inputCurrent", 4), ("inputCurrentAvg", 5), ("inputCurrentMax", 6), ("inputCurrentMin", 7), ("inputVoltage", 8), ("inputVoltageAvg", 9), ("inputVoltageMax", 10), ("inputVoltageMin", 11))

class CucsComputeMbTempStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("fmTempSenIo", 0), ("fmTempSenIoAvg", 1), ("fmTempSenIoMax", 2), ("fmTempSenIoMin", 3), ("fmTempSenRear", 4), ("fmTempSenRearAvg", 5), ("fmTempSenRearL", 6), ("fmTempSenRearLAvg", 7), ("fmTempSenRearLMax", 8), ("fmTempSenRearLMin", 9), ("fmTempSenRearMax", 10), ("fmTempSenRearMin", 11), ("fmTempSenRearR", 12), ("fmTempSenRearRAvg", 13), ("fmTempSenRearRMax", 14), ("fmTempSenRearRMin", 15))

class CucsComputeMbTempStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("fmTempSenIo", 0), ("fmTempSenIoAvg", 1), ("fmTempSenIoMax", 2), ("fmTempSenIoMin", 3), ("fmTempSenRear", 4), ("fmTempSenRearAvg", 5), ("fmTempSenRearL", 6), ("fmTempSenRearLAvg", 7), ("fmTempSenRearLMax", 8), ("fmTempSenRearLMin", 9), ("fmTempSenRearMax", 10), ("fmTempSenRearMin", 11), ("fmTempSenRearR", 12), ("fmTempSenRearRAvg", 13), ("fmTempSenRearRMax", 14), ("fmTempSenRearRMin", 15))

class CucsComputeMemoryUnitConstraintType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unknown", 0), ("kit", 1))

class CucsComputeOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("policy", 1), ("management", 2))

class CucsComputePCIeFatalCompletionStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("abortErrors", 0), ("timeoutErrors", 1), ("unexpectedErrors", 2))

class CucsComputePCIeFatalProtocolStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("dllpErrors", 0), ("flowControlErrors", 1))

class CucsComputePCIeFatalReceiveStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bufferOverflowErrors", 0), ("errFatalErrors", 1), ("errNonFatalErrors", 2), ("unsupportedRequestErrors", 3))

class CucsComputePCIeFatalStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("acsViolationErrors", 0), ("malformedTLPErrors", 1), ("poisonedTLPErrors", 2), ("surpriseLinkDownErrors", 3))

class CucsComputePciCapOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ascending", 0), ("descending", 1), ("ascendingDual", 2), ("ascendingSeq", 3))

class CucsComputePhysicalLowVoltageMemory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("yes", 1), ("regularVoltage", 2))

class CucsComputePhysicalFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 665, 727, 767, 769, 771, 773, 775, 777, 781, 785, 789, 792, 806, 815, 879, 891, 898, 932, 934, 1036, 1055, 1152, 1157, 1254, 1256, 1478))
    namedValues = NamedValues(("nop", 0), ("associate", 665), ("disassociate", 727), ("powerCap", 767), ("decommission", 769), ("softShutdown", 771), ("hardShutdown", 773), ("turnup", 775), ("powercycle", 777), ("hardreset", 781), ("softreset", 785), ("swConnUpd", 789), ("biosRecovery", 792), ("cmosReset", 806), ("resetBmc", 815), ("updateExtUsers", 879), ("updateAdaptor", 891), ("activateAdaptor", 898), ("configSoL", 932), ("unconfigSoL", 934), ("diagnosticInterrupt", 1036), ("resetKvm", 1055), ("updateBIOS", 1152), ("activateBIOS", 1157), ("resetIpmi", 1254), ("fwUpgrade", 1256), ("cimcSessionDelete", 1478))

class CucsComputePhysicalFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 665, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 806, 807, 808, 809, 810, 811, 812, 815, 816, 879, 880, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 932, 933, 934, 935, 940, 941, 942, 943, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 1019, 1020, 1021, 1022, 1036, 1037, 1038, 1039, 1040, 1055, 1056, 1057, 1058, 1069, 1070, 1071, 1072, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1178, 1179, 1180, 1181, 1247, 1248, 1249), SingleValueConstraint(1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1361, 1363, 1385, 1386, 1387, 1388, 1471, 1472, 1473, 1478, 1479, 1480, 1481))
    namedValues = NamedValues(("nop", 0), ("associateBegin", 665), ("associateUpdateIBMCFw", 668), ("associateWaitForIBMCFwUpdate", 669), ("associateActivateIBMCFw", 670), ("associateResetIBMC", 671), ("associatePreSanitize", 672), ("associateSanitize", 673), ("associateConfigUserAccess", 674), ("associateBladePowerOff", 675), ("associateUpdateBoardCtrlRequest", 676), ("associatePollBoardCtrlUpdateStatus", 677), ("associatePowerOn", 678), ("associateBmcPreconfigPnuOSLocal", 679), ("associateBmcPreconfigPnuOSPeer", 680), ("associateBmcConfigPnuOS", 681), ("associateSwConfigPnuOSLocal", 682), ("associateSwConfigPnuOSPeer", 683), ("associateUpdateAdaptorNwFwLocal", 684), ("associateUpdateAdaptorNwFwPeer", 685), ("associateWaitForAdaptorNwFwUpdateLocal", 686), ("associateWaitForAdaptorNwFwUpdatePeer", 687), ("associateActivateAdaptorNwFwLocal", 688), ("associateActivateAdaptorNwFwPeer", 689), ("associateNicConfigPnuOSLocal", 690), ("associateNicConfigPnuOSPeer", 691), ("associateBootPnuos", 692), ("associateBootWait", 693), ("associateBiosPostCompletion", 694), ("associateHagPnuOSConnect", 695), ("associatePnuOSIdent", 696), ("associatePnuOSPolicy", 697), ("associatePnuOSValidate", 698), ("associatePnuOSSelfTest", 699), ("associateBiosImgUpdate", 700), ("associateStorageCtlrImgUpdate", 701), ("associateHbaImgUpdate", 702), ("associateNicImgUpdate", 703), ("associatePnuOSInventory", 704), ("associatePnuOSConfig", 705), ("associatePnuOSLocalDiskConfig", 706), ("associatePnuOSUnloadDrivers", 707), ("associateBmcUnconfigPnuOS", 708), ("associateNicUnconfigPnuOSLocal", 709), ("associateNicUnconfigPnuOSPeer", 710), ("associateSwUnconfigPnuOSLocal", 711), ("associateSwUnconfigPnuOSPeer", 712), ("associateSwConfigHostOSLocal", 713), ("associateSwConfigHostOSPeer", 714), ("associateNicConfigHostOSLocal", 715), ("associateNicConfigHostOSPeer", 716), ("associateHagPnuOSDisconnect", 717), ("associateConfigSoL", 718), ("associatePrepareForBoot", 719), ("associateConfigUuid", 720), ("associateBootHost", 721), ("associateHagHostOSConnect", 722), ("associateHostOSIdent", 723), ("associateHostOSPolicy", 724), ("associateHostOSValidate", 725), ("associateHostOSConfig", 726), ("disassociateBegin", 727), ("disassociateConfigUserAccess", 730), ("disassociatePowerOn", 731), ("disassociatePreSanitize", 732), ("disassociateSanitize", 733), ("disassociateNicUnconfigHostOSLocal", 734), ("disassociateNicUnconfigHostOSPeer", 735), ("disassociateSwUnconfigHostOSLocal", 736), ("disassociateSwUnconfigHostOSPeer", 737), ("disassociateBmcPreconfigPnuOSLocal", 738), ("disassociateBmcPreconfigPnuOSPeer", 739), ("disassociateBmcConfigPnuOS", 740), ("disassociateSwConfigPnuOSLocal", 741), ("disassociateSwConfigPnuOSPeer", 742), ("disassociateNicConfigPnuOSLocal", 743), ("disassociateNicConfigPnuOSPeer", 744), ("disassociateConfigBios", 745), ("disassociateBootPnuos", 746), ("disassociateBootWait", 747), ("disassociateBiosPostCompletion", 748), ("disassociateHagPnuOSConnect", 749), ("disassociatePnuOSIdent", 750), ("disassociatePnuOSPolicy", 751), ("disassociatePnuOSValidate", 752), ("disassociatePnuOSUnconfig", 753), ("disassociatePnuOSScrub", 754), ("disassociatePnuOSSelfTest", 755), ("disassociateBmcUnconfigPnuOS", 756), ("disassociateNicUnconfigPnuOSLocal", 757), ("disassociateNicUnconfigPnuOSPeer", 758), ("disassociateHagPnuOSDisconnect", 759), ("disassociateUnconfigUuid", 760), ("disassociateShutdown", 761), ("disassociateUnconfigBios", 762), ("disassociateSwUnconfigPnuOSLocal", 763), ("disassociateSwUnconfigPnuOSPeer", 764), ("disassociateUnconfigSoL", 765), ("disassociateHandlePooling", 766), ("powerCapBegin", 767), ("powerCapConfig", 768), ("decommissionBegin", 769), ("decommissionExecute", 770), ("softShutdownBegin", 771), ("softShutdownExecute", 772), ("hardShutdownBegin", 773), ("hardShutdownExecute", 774), ("turnupBegin", 775), ("turnupExecute", 776), ("powercycleBegin", 777), ("powercyclePreSanitize", 778), ("powercycleSanitize", 779), ("powercycleExecute", 780), ("hardresetBegin", 781), ("hardresetPreSanitize", 782), ("hardresetSanitize", 783), ("hardresetExecute", 784), ("softresetBegin", 785), ("softresetPreSanitize", 786), ("softresetSanitize", 787), ("softresetExecute", 788), ("swConnUpdBegin", 789), ("swConnUpdA", 790), ("swConnUpdB", 791), ("biosRecoveryBegin", 792), ("biosRecoveryShutdown", 793), ("biosRecoveryPreSanitize", 794), ("biosRecoverySanitize", 795), ("biosRecoverySetupVmediaLocal", 796), ("biosRecoverySetupVmediaPeer", 797), ("biosRecoveryStart", 798), ("biosRecoveryWait", 799), ("biosRecoveryCleanup", 800), ("biosRecoveryReset", 801), ("biosRecoveryTeardownVmediaLocal", 802), ("biosRecoveryTeardownVmediaPeer", 803), ("cmosResetBegin", 806), ("cmosResetPreSanitize", 807), ("cmosResetSanitize", 808), ("cmosResetExecute", 809), ("cmosResetReconfigBios", 810), ("cmosResetReconfigUuid", 811), ("cmosResetBladePowerOn", 812), ("resetBmcBegin", 815), ("resetBmcExecute", 816), ("updateExtUsersBegin", 879), ("updateExtUsersDeploy", 880), ("updateAdaptorBegin", 891), ("updateAdaptorPowerOn", 892), ("updateAdaptorUpdateRequestLocal", 893), ("updateAdaptorUpdateRequestPeer", 894), ("updateAdaptorPollUpdateStatusLocal", 895), ("updateAdaptorPollUpdateStatusPeer", 896), ("updateAdaptorPowerOff", 897), ("activateAdaptorBegin", 898), ("activateAdaptorPowerOn", 899), ("activateAdaptorActivateLocal", 900), ("activateAdaptorActivatePeer", 901), ("activateAdaptorReset", 902), ("configSoLBegin", 932), ("configSoLExecute", 933), ("unconfigSoLBegin", 934), ("unconfigSoLExecute", 935), ("activateAdaptorFail", 940), ("activateAdaptorSuccess", 941), ("associateFail", 942), ("associateSuccess", 943), ("biosRecoveryFail", 946), ("biosRecoverySuccess", 947), ("cmosResetFail", 948), ("cmosResetSuccess", 949), ("configSoLFail", 950), ("configSoLSuccess", 951), ("decommissionFail", 952), ("decommissionSuccess", 953), ("disassociateFail", 954), ("disassociateSuccess", 955), ("hardShutdownFail", 956), ("hardShutdownSuccess", 957), ("hardresetFail", 958), ("hardresetSuccess", 959), ("powerCapFail", 960), ("powerCapSuccess", 961), ("powercycleFail", 962), ("powercycleSuccess", 963), ("resetBmcFail", 964), ("resetBmcSuccess", 965), ("softShutdownFail", 966), ("softShutdownSuccess", 967), ("softresetFail", 968), ("softresetSuccess", 969), ("swConnUpdFail", 970), ("swConnUpdSuccess", 971), ("turnupFail", 972), ("turnupSuccess", 973), ("unconfigSoLFail", 974), ("unconfigSoLSuccess", 975), ("updateAdaptorFail", 976), ("updateAdaptorSuccess", 977), ("updateExtUsersFail", 978), ("updateExtUsersSuccess", 979), ("decommissionStopVMediaLocal", 1019), ("decommissionStopVMediaPeer", 1020), ("biosRecoveryStopVMediaLocal", 1021), ("biosRecoveryStopVMediaPeer", 1022), ("diagnosticInterruptBegin", 1036), ("diagnosticInterruptExecute", 1037), ("diagnosticInterruptFail", 1038), ("diagnosticInterruptSuccess", 1039), ("associateLocalDiskFwUpdate", 1040), ("resetKvmBegin", 1055), ("resetKvmExecute", 1056), ("resetKvmFail", 1057), ("resetKvmSuccess", 1058), ("associateSwConfigPortNivLocal", 1069), ("associateSwConfigPortNivPeer", 1070), ("disassociateSwConfigPortNivLocal", 1071), ("disassociateSwConfigPortNivPeer", 1072), ("associateSolRedirectEnable", 1104), ("associateSerialDebugPnuOSConnect", 1105), ("associateSerialDebugPnuOSDisconnect", 1106), ("associateSolRedirectDisable", 1107), ("disassociateSolRedirectEnable", 1108), ("disassociateSerialDebugPnuOSConnect", 1109), ("disassociateSerialDebugPnuOSDisconnect", 1110), ("disassociateSolRedirectDisable", 1111), ("decommissionCleanupCIMC", 1112), ("updateBIOSBegin", 1152), ("updateBIOSClear", 1153), ("updateBIOSPollClearStatus", 1154), ("updateBIOSUpdateRequest", 1155), ("updateBIOSPollUpdateStatus", 1156), ("activateBIOSBegin", 1157), ("activateBIOSPowerOff", 1158), ("activateBIOSClear", 1159), ("activateBIOSPollClearStatus", 1160), ("activateBIOSActivate", 1161), ("activateBIOSPollActivateStatus", 1162), ("activateBIOSUpdateTokens", 1163), ("activateBIOSPowerOn", 1164), ("associateClearBiosUpdate", 1169), ("associatePollClearBiosUpdateStatus", 1170), ("associateUpdateBiosRequest", 1171), ("associatePollBiosUpdateStatus", 1172), ("associateActivateBios", 1173), ("associatePollBiosActivateStatus", 1174), ("associatePnuOSCatalog", 1175), ("disassociatePnuOSCatalog", 1176), ("activateBIOSFail", 1178), ("activateBIOSSuccess", 1179), ("updateBIOSFail", 1180), ("updateBIOSSuccess", 1181), ("associateMarkAdapterForReboot", 1247), ("associateDeassertResetBypass", 1248), ("associateVerifyFcZoneConfig", 1249)) + NamedValues(("disassociateDeassertResetBypass", 1250), ("disassociateVerifyFcZoneConfig", 1251), ("decommissionCleanupPortConfigLocal", 1252), ("decommissionCleanupPortConfigPeer", 1253), ("resetIpmiBegin", 1254), ("resetIpmiExecute", 1255), ("fwUpgradeBegin", 1256), ("fwUpgradeUpdateIBMCFw", 1257), ("fwUpgradeWaitForIBMCFwUpdate", 1258), ("fwUpgradeActivateIBMCFw", 1259), ("fwUpgradeResetIBMC", 1260), ("fwUpgradePreSanitize", 1261), ("fwUpgradeSanitize", 1262), ("fwUpgradeBladePowerOff", 1263), ("fwUpgradeUpdateBoardCtrlRequest", 1264), ("fwUpgradePollBoardCtrlUpdateStatus", 1265), ("fwUpgradeClearBiosUpdate", 1266), ("fwUpgradePollClearBiosUpdateStatus", 1267), ("fwUpgradeUpdateBiosRequest", 1268), ("fwUpgradePollBiosUpdateStatus", 1269), ("fwUpgradeActivateBios", 1270), ("fwUpgradePollBiosActivateStatus", 1271), ("fwUpgradePowerOn", 1272), ("fwUpgradeBmcPreconfigPnuOSLocal", 1273), ("fwUpgradeBmcPreconfigPnuOSPeer", 1274), ("fwUpgradeSwConfigPortNivLocal", 1275), ("fwUpgradeSwConfigPortNivPeer", 1276), ("fwUpgradeSwConfigPnuOSLocal", 1277), ("fwUpgradeSwConfigPnuOSPeer", 1278), ("fwUpgradeUpdateAdaptorNwFwLocal", 1279), ("fwUpgradeUpdateAdaptorNwFwPeer", 1280), ("fwUpgradeWaitForAdaptorNwFwUpdateLocal", 1281), ("fwUpgradeWaitForAdaptorNwFwUpdatePeer", 1282), ("fwUpgradeActivateAdaptorNwFwLocal", 1283), ("fwUpgradeActivateAdaptorNwFwPeer", 1284), ("fwUpgradeNicConfigPnuOSLocal", 1285), ("fwUpgradeNicConfigPnuOSPeer", 1286), ("fwUpgradeBmcConfigPnuOS", 1287), ("fwUpgradeSolRedirectEnable", 1288), ("fwUpgradeSerialDebugPnuOSConnect", 1289), ("fwUpgradeBootPnuos", 1290), ("fwUpgradeBootWait", 1291), ("fwUpgradeBiosPostCompletion", 1292), ("fwUpgradeHagPnuOSConnect", 1293), ("fwUpgradePnuOSIdent", 1294), ("fwUpgradePnuOSPolicy", 1295), ("fwUpgradePnuOSCatalog", 1296), ("fwUpgradePnuOSValidate", 1297), ("fwUpgradePnuOSSelfTest", 1298), ("fwUpgradeStorageCtlrImgUpdate", 1299), ("fwUpgradeHbaImgUpdate", 1300), ("fwUpgradeNicImgUpdate", 1301), ("fwUpgradeLocalDiskFwUpdate", 1302), ("fwUpgradePnuOSConfig", 1303), ("fwUpgradePnuOSInventory", 1304), ("fwUpgradeBiosImgUpdate", 1305), ("fwUpgradePnuOSUnloadDrivers", 1306), ("fwUpgradeBmcUnconfigPnuOS", 1307), ("fwUpgradeNicUnconfigPnuOSLocal", 1308), ("fwUpgradeNicUnconfigPnuOSPeer", 1309), ("fwUpgradeSwUnconfigPnuOSLocal", 1310), ("fwUpgradeSwUnconfigPnuOSPeer", 1311), ("fwUpgradeHagPnuOSDisconnect", 1312), ("fwUpgradeSerialDebugPnuOSDisconnect", 1313), ("fwUpgradeSolRedirectDisable", 1314), ("fwUpgradeShutdown", 1315), ("activateAdaptorDeassertResetBypass", 1361), ("fwUpgradeDeassertResetBypass", 1363), ("fwUpgradeFail", 1385), ("fwUpgradeSuccess", 1386), ("resetIpmiFail", 1387), ("resetIpmiSuccess", 1388), ("associateConfigFlexFlash", 1471), ("associateSyncPowerState", 1472), ("disassociateUnconfigFlexFlash", 1473), ("cimcSessionDeleteBegin", 1478), ("cimcSessionDeleteExecute", 1479), ("cimcSessionDeleteFail", 1480), ("cimcSessionDeleteSuccess", 1481))

class CucsComputePhysicalFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeComputePhysicalFwUpgradeConfigPnuos", 0), ("samDmeComputePhysicalFwUpgradeConfigAdaptorNwFw", 1), ("samDmeComputePhysicalFwUpgradeConfigMgmtFw", 2), ("samDmeComputePhysicalFwUpgradeConfigBoardCtrlFw", 3), ("samDmeComputePhysicalFwUpgradeConfigBmcBiosUpdate", 4), ("samDmeComputePhysicalAssociateFlexflashConfig", 9), ("samDmeComputePhysicalAssociatePowerForceConfig", 10), ("samDmeComputePhysicalDisassociateMaskPnuos", 11), ("samDmeComputePhysicalAssociatePnuosConfig", 26), ("samDmeComputePhysicalAssociateSwitchConfig", 27), ("samDmeComputePhysicalAssociateHostConfig", 28), ("samDmeComputePhysicalAssociateHostReboot", 29), ("samDmeComputePhysicalAssociateIfConfig", 30), ("samDmeComputePhysicalAssociateNicConfig", 31), ("samDmeComputePhysicalAssociateAdaptorNwFwConfig", 32), ("samDmeComputePhysicalAssociateMgmtFwConfig", 33), ("samDmeComputePhysicalAssociateBootConfig", 34), ("samDmeComputePhysicalAssociateBiosUpdate", 35), ("samDmeComputePhysicalAssociateSolConfig", 36), ("samDmeComputePhysicalAssociateEpAuthConfig", 37), ("samDmeComputePhysicalAssociateDiskConfig", 38), ("samDmeComputePhysicalDisassociateSwitchUnconfig", 39), ("samDmeComputePhysicalActivateAdaptorActivate", 40), ("samDmeComputePhysicalActivateAdaptorReset", 41), ("samDmeComputePhysicalCmosResetAlways", 42), ("samDmeComputePhysicalCmosResetSetUuidBiosBoot", 43), ("samDmeComputePhysicalCmosResetPowerOn", 44), ("samDmeComputePhysicalAssociateBoardCtrlFwConfig", 45), ("samDmeComputePhysicalAssociateBmcBiosUpdate", 58), ("samDmeComputePhysicalAssociateLsRename", 62))

class CucsComputePhysicalFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 634, 680, 711, 713, 715, 717, 719, 723, 727, 731, 734, 748, 752, 754, 756, 761, 765, 767, 1036, 1055, 1152, 1157, 1254, 1256, 1478))
    namedValues = NamedValues(("nop", 0), ("associate", 634), ("disassociate", 680), ("decommission", 711), ("softShutdown", 713), ("hardShutdown", 715), ("turnup", 717), ("powercycle", 719), ("hardreset", 723), ("softreset", 727), ("swConnUpd", 731), ("biosRecovery", 734), ("cmosReset", 748), ("resetBmc", 752), ("updateExtUsers", 754), ("updateAdaptor", 756), ("activateAdaptor", 761), ("configSoL", 765), ("unconfigSoL", 767), ("diagnosticInterrupt", 1036), ("resetKvm", 1055), ("updateBIOS", 1152), ("activateBIOS", 1157), ("resetIpmi", 1254), ("fwUpgrade", 1256), ("cimcSessionDelete", 1478))

class CucsComputePooledRackUnitId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsComputePooledSlotSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsComputePsuClusterState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("slot1Master", 1), ("slot2Master", 2), ("notClustered", 3))

class CucsComputePsuControlRedundancy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("nonRedundant", 1), ("nPlus1", 2), ("grid", 3))

class CucsComputePsuRedundancy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("nonRedundant", 1), ("nPlus1", 2), ("grid", 3))

class CucsComputePsuRedundancyOperQualifier(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("redundancyLost", 0), ("redundancyDegraded", 1), ("nonRedundantSufficientResources", 2), ("nonRedundantInsufficientResources", 3))

class CucsComputePsuRedundancyOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("failed", 2), ("degraded", 3))

class CucsComputeRackQualMaxId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsComputeRackQualMinId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsComputeRackUnitId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsComputeRackUnitFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 665, 727, 767, 769, 771, 773, 775, 777, 781, 785, 789, 792, 806, 815, 819, 879, 891, 898, 932, 934, 1036, 1055, 1064, 1152, 1157, 1254, 1256, 1316, 1478))
    namedValues = NamedValues(("nop", 0), ("associate", 665), ("disassociate", 727), ("powerCap", 767), ("decommission", 769), ("softShutdown", 771), ("hardShutdown", 773), ("turnup", 775), ("powercycle", 777), ("hardreset", 781), ("softreset", 785), ("swConnUpd", 789), ("biosRecovery", 792), ("cmosReset", 806), ("resetBmc", 815), ("discover", 819), ("updateExtUsers", 879), ("updateAdaptor", 891), ("activateAdaptor", 898), ("configSoL", 932), ("unconfigSoL", 934), ("diagnosticInterrupt", 1036), ("resetKvm", 1055), ("offline", 1064), ("updateBIOS", 1152), ("activateBIOS", 1157), ("resetIpmi", 1254), ("fwUpgrade", 1256), ("adapterReset", 1316), ("cimcSessionDelete", 1478))

class CucsComputeRackUnitFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 665, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 806, 807, 808, 809, 810, 811, 812, 815, 816, 819, 820, 821, 822, 823, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 879, 880, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 932, 933, 934, 935, 940, 941, 942, 943, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1027, 1028, 1029, 1030, 1031, 1036, 1037, 1038, 1039, 1040, 1050, 1055), SingleValueConstraint(1056, 1057, 1058, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1092, 1093, 1094, 1095, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1243, 1244, 1245, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1361, 1363, 1385, 1386, 1387, 1388, 1389, 1390, 1471, 1472, 1473, 1478, 1479, 1480, 1481))
    namedValues = NamedValues(("nop", 0), ("associateBegin", 665), ("associateUpdateIBMCFw", 668), ("associateWaitForIBMCFwUpdate", 669), ("associateActivateIBMCFw", 670), ("associateResetIBMC", 671), ("associatePreSanitize", 672), ("associateSanitize", 673), ("associateConfigUserAccess", 674), ("associateBladePowerOff", 675), ("associateUpdateBoardCtrlRequest", 676), ("associatePollBoardCtrlUpdateStatus", 677), ("associatePowerOn", 678), ("associateBmcPreconfigPnuOSLocal", 679), ("associateBmcPreconfigPnuOSPeer", 680), ("associateBmcConfigPnuOS", 681), ("associateSwConfigPnuOSLocal", 682), ("associateSwConfigPnuOSPeer", 683), ("associateUpdateAdaptorNwFwLocal", 684), ("associateUpdateAdaptorNwFwPeer", 685), ("associateWaitForAdaptorNwFwUpdateLocal", 686), ("associateWaitForAdaptorNwFwUpdatePeer", 687), ("associateActivateAdaptorNwFwLocal", 688), ("associateActivateAdaptorNwFwPeer", 689), ("associateNicConfigPnuOSLocal", 690), ("associateNicConfigPnuOSPeer", 691), ("associateBootPnuos", 692), ("associateBootWait", 693), ("associateBiosPostCompletion", 694), ("associateHagPnuOSConnect", 695), ("associatePnuOSIdent", 696), ("associatePnuOSPolicy", 697), ("associatePnuOSValidate", 698), ("associatePnuOSSelfTest", 699), ("associateBiosImgUpdate", 700), ("associateStorageCtlrImgUpdate", 701), ("associateHbaImgUpdate", 702), ("associateNicImgUpdate", 703), ("associatePnuOSInventory", 704), ("associatePnuOSConfig", 705), ("associatePnuOSLocalDiskConfig", 706), ("associatePnuOSUnloadDrivers", 707), ("associateBmcUnconfigPnuOS", 708), ("associateNicUnconfigPnuOSLocal", 709), ("associateNicUnconfigPnuOSPeer", 710), ("associateSwUnconfigPnuOSLocal", 711), ("associateSwUnconfigPnuOSPeer", 712), ("associateSwConfigHostOSLocal", 713), ("associateSwConfigHostOSPeer", 714), ("associateNicConfigHostOSLocal", 715), ("associateNicConfigHostOSPeer", 716), ("associateHagPnuOSDisconnect", 717), ("associateConfigSoL", 718), ("associatePrepareForBoot", 719), ("associateConfigUuid", 720), ("associateBootHost", 721), ("associateHagHostOSConnect", 722), ("associateHostOSIdent", 723), ("associateHostOSPolicy", 724), ("associateHostOSValidate", 725), ("associateHostOSConfig", 726), ("disassociateBegin", 727), ("disassociateConfigUserAccess", 730), ("disassociatePowerOn", 731), ("disassociatePreSanitize", 732), ("disassociateSanitize", 733), ("disassociateNicUnconfigHostOSLocal", 734), ("disassociateNicUnconfigHostOSPeer", 735), ("disassociateSwUnconfigHostOSLocal", 736), ("disassociateSwUnconfigHostOSPeer", 737), ("disassociateBmcPreconfigPnuOSLocal", 738), ("disassociateBmcPreconfigPnuOSPeer", 739), ("disassociateBmcConfigPnuOS", 740), ("disassociateSwConfigPnuOSLocal", 741), ("disassociateSwConfigPnuOSPeer", 742), ("disassociateNicConfigPnuOSLocal", 743), ("disassociateNicConfigPnuOSPeer", 744), ("disassociateConfigBios", 745), ("disassociateBootPnuos", 746), ("disassociateBootWait", 747), ("disassociateBiosPostCompletion", 748), ("disassociateHagPnuOSConnect", 749), ("disassociatePnuOSIdent", 750), ("disassociatePnuOSPolicy", 751), ("disassociatePnuOSValidate", 752), ("disassociatePnuOSUnconfig", 753), ("disassociatePnuOSScrub", 754), ("disassociatePnuOSSelfTest", 755), ("disassociateBmcUnconfigPnuOS", 756), ("disassociateNicUnconfigPnuOSLocal", 757), ("disassociateNicUnconfigPnuOSPeer", 758), ("disassociateHagPnuOSDisconnect", 759), ("disassociateUnconfigUuid", 760), ("disassociateShutdown", 761), ("disassociateUnconfigBios", 762), ("disassociateSwUnconfigPnuOSLocal", 763), ("disassociateSwUnconfigPnuOSPeer", 764), ("disassociateUnconfigSoL", 765), ("disassociateHandlePooling", 766), ("powerCapBegin", 767), ("powerCapConfig", 768), ("decommissionBegin", 769), ("decommissionExecute", 770), ("softShutdownBegin", 771), ("softShutdownExecute", 772), ("hardShutdownBegin", 773), ("hardShutdownExecute", 774), ("turnupBegin", 775), ("turnupExecute", 776), ("powercycleBegin", 777), ("powercyclePreSanitize", 778), ("powercycleSanitize", 779), ("powercycleExecute", 780), ("hardresetBegin", 781), ("hardresetPreSanitize", 782), ("hardresetSanitize", 783), ("hardresetExecute", 784), ("softresetBegin", 785), ("softresetPreSanitize", 786), ("softresetSanitize", 787), ("softresetExecute", 788), ("swConnUpdBegin", 789), ("swConnUpdA", 790), ("swConnUpdB", 791), ("biosRecoveryBegin", 792), ("biosRecoveryShutdown", 793), ("biosRecoveryPreSanitize", 794), ("biosRecoverySanitize", 795), ("biosRecoverySetupVmediaLocal", 796), ("biosRecoverySetupVmediaPeer", 797), ("biosRecoveryStart", 798), ("biosRecoveryWait", 799), ("biosRecoveryCleanup", 800), ("biosRecoveryReset", 801), ("biosRecoveryTeardownVmediaLocal", 802), ("biosRecoveryTeardownVmediaPeer", 803), ("cmosResetBegin", 806), ("cmosResetPreSanitize", 807), ("cmosResetSanitize", 808), ("cmosResetExecute", 809), ("cmosResetReconfigBios", 810), ("cmosResetReconfigUuid", 811), ("cmosResetBladePowerOn", 812), ("resetBmcBegin", 815), ("resetBmcExecute", 816), ("discoverBegin", 819), ("discoverBmcConfigureConnLocal", 820), ("discoverSwConfigureConnLocal", 821), ("discoverBmcConfigureConnPeer", 822), ("discoverSwConfigureConnPeer", 823), ("discoverBmcPresence", 826), ("discoverBmcInventory", 827), ("discoverPreSanitize", 828), ("discoverSanitize", 829), ("discoverConfigUserAccess", 830), ("discoverSwConfigPnuOSLocal", 831), ("discoverSwConfigPnuOSPeer", 832), ("discoverBmcPreconfigPnuOSLocal", 833), ("discoverBmcPreconfigPnuOSPeer", 834), ("discoverBmcConfigPnuOS", 835), ("discoverBootPnuos", 836), ("discoverBootWait", 837), ("discoverBiosPostCompletion", 838), ("discoverReadSmbios", 839), ("discoverHagConnect", 841), ("discoverPnuOSIdent", 842), ("discoverPnuOSPolicy", 843), ("discoverPnuOSInventory", 844), ("discoverPnuOSScrub", 845), ("discoverPnuOSConnectivity", 846), ("discoverPnuOSConnStatus", 847), ("discoverSwPnuOSConnectivityLocal", 848), ("discoverSwPnuOSConnectivityPeer", 849), ("discoverPnuOSSelfTest", 850), ("discoverBmcUnconfigPnuOS", 851), ("discoverHagDisconnect", 852), ("discoverBmcShutdownDiscovered", 853), ("discoverHandlePooling", 854), ("discoverSuccess", 855), ("discoverFail", 856), ("updateExtUsersBegin", 879), ("updateExtUsersDeploy", 880), ("updateAdaptorBegin", 891), ("updateAdaptorPowerOn", 892), ("updateAdaptorUpdateRequestLocal", 893), ("updateAdaptorUpdateRequestPeer", 894), ("updateAdaptorPollUpdateStatusLocal", 895), ("updateAdaptorPollUpdateStatusPeer", 896), ("updateAdaptorPowerOff", 897), ("activateAdaptorBegin", 898), ("activateAdaptorPowerOn", 899), ("activateAdaptorActivateLocal", 900), ("activateAdaptorActivatePeer", 901), ("activateAdaptorReset", 902), ("configSoLBegin", 932), ("configSoLExecute", 933), ("unconfigSoLBegin", 934), ("unconfigSoLExecute", 935), ("activateAdaptorFail", 940), ("activateAdaptorSuccess", 941), ("associateFail", 942), ("associateSuccess", 943), ("biosRecoveryFail", 946), ("biosRecoverySuccess", 947), ("cmosResetFail", 948), ("cmosResetSuccess", 949), ("configSoLFail", 950), ("configSoLSuccess", 951), ("decommissionFail", 952), ("decommissionSuccess", 953), ("disassociateFail", 954), ("disassociateSuccess", 955), ("hardShutdownFail", 956), ("hardShutdownSuccess", 957), ("hardresetFail", 958), ("hardresetSuccess", 959), ("powerCapFail", 960), ("powerCapSuccess", 961), ("powercycleFail", 962), ("powercycleSuccess", 963), ("resetBmcFail", 964), ("resetBmcSuccess", 965), ("softShutdownFail", 966), ("softShutdownSuccess", 967), ("softresetFail", 968), ("softresetSuccess", 969), ("swConnUpdFail", 970), ("swConnUpdSuccess", 971), ("turnupFail", 972), ("turnupSuccess", 973), ("unconfigSoLFail", 974), ("unconfigSoLSuccess", 975), ("updateAdaptorFail", 976), ("updateAdaptorSuccess", 977), ("updateExtUsersFail", 978), ("updateExtUsersSuccess", 979), ("decommissionStopVMediaLocal", 1019), ("decommissionStopVMediaPeer", 1020), ("biosRecoveryStopVMediaLocal", 1021), ("biosRecoveryStopVMediaPeer", 1022), ("discoverConfigDiscoveryMode", 1023), ("discoverSwUnconfigPortNivLocal", 1024), ("discoverSwUnconfigPortNivPeer", 1025), ("discoverSwConfigPortNivLocal", 1027), ("discoverSwConfigPortNivPeer", 1028), ("discoverNicInventoryLocal", 1029), ("discoverNicInventoryPeer", 1030), ("discoverConfigNivMode", 1031), ("diagnosticInterruptBegin", 1036), ("diagnosticInterruptExecute", 1037), ("diagnosticInterruptFail", 1038), ("diagnosticInterruptSuccess", 1039), ("associateLocalDiskFwUpdate", 1040), ("discoverWaitForConnReady", 1050), ("resetKvmBegin", 1055)) + NamedValues(("resetKvmExecute", 1056), ("resetKvmFail", 1057), ("resetKvmSuccess", 1058), ("offlineBegin", 1064), ("offlineCleanupLocal", 1065), ("offlineCleanupPeer", 1066), ("offlineSwUnconfigureLocal", 1067), ("offlineSwUnconfigurePeer", 1068), ("associateSwConfigPortNivLocal", 1069), ("associateSwConfigPortNivPeer", 1070), ("disassociateSwConfigPortNivLocal", 1071), ("disassociateSwConfigPortNivPeer", 1072), ("offlineFail", 1073), ("offlineSuccess", 1074), ("discoverSolRedirectEnable", 1092), ("discoverSerialDebugConnect", 1093), ("discoverSerialDebugDisconnect", 1094), ("discoverSolRedirectDisable", 1095), ("associateSolRedirectEnable", 1104), ("associateSerialDebugPnuOSConnect", 1105), ("associateSerialDebugPnuOSDisconnect", 1106), ("associateSolRedirectDisable", 1107), ("disassociateSolRedirectEnable", 1108), ("disassociateSerialDebugPnuOSConnect", 1109), ("disassociateSerialDebugPnuOSDisconnect", 1110), ("disassociateSolRedirectDisable", 1111), ("decommissionCleanupCIMC", 1112), ("updateBIOSBegin", 1152), ("updateBIOSClear", 1153), ("updateBIOSPollClearStatus", 1154), ("updateBIOSUpdateRequest", 1155), ("updateBIOSPollUpdateStatus", 1156), ("activateBIOSBegin", 1157), ("activateBIOSPowerOff", 1158), ("activateBIOSClear", 1159), ("activateBIOSPollClearStatus", 1160), ("activateBIOSActivate", 1161), ("activateBIOSPollActivateStatus", 1162), ("activateBIOSUpdateTokens", 1163), ("activateBIOSPowerOn", 1164), ("associateClearBiosUpdate", 1169), ("associatePollClearBiosUpdateStatus", 1170), ("associateUpdateBiosRequest", 1171), ("associatePollBiosUpdateStatus", 1172), ("associateActivateBios", 1173), ("associatePollBiosActivateStatus", 1174), ("associatePnuOSCatalog", 1175), ("disassociatePnuOSCatalog", 1176), ("discoverPnuOSCatalog", 1177), ("activateBIOSFail", 1178), ("activateBIOSSuccess", 1179), ("updateBIOSFail", 1180), ("updateBIOSSuccess", 1181), ("discoverBladePowerOff", 1243), ("discoverNicConfigPnuOSLocal", 1244), ("discoverNicConfigPnuOSPeer", 1245), ("associateMarkAdapterForReboot", 1247), ("associateDeassertResetBypass", 1248), ("associateVerifyFcZoneConfig", 1249), ("disassociateDeassertResetBypass", 1250), ("disassociateVerifyFcZoneConfig", 1251), ("decommissionCleanupPortConfigLocal", 1252), ("decommissionCleanupPortConfigPeer", 1253), ("resetIpmiBegin", 1254), ("resetIpmiExecute", 1255), ("fwUpgradeBegin", 1256), ("fwUpgradeUpdateIBMCFw", 1257), ("fwUpgradeWaitForIBMCFwUpdate", 1258), ("fwUpgradeActivateIBMCFw", 1259), ("fwUpgradeResetIBMC", 1260), ("fwUpgradePreSanitize", 1261), ("fwUpgradeSanitize", 1262), ("fwUpgradeBladePowerOff", 1263), ("fwUpgradeUpdateBoardCtrlRequest", 1264), ("fwUpgradePollBoardCtrlUpdateStatus", 1265), ("fwUpgradeClearBiosUpdate", 1266), ("fwUpgradePollClearBiosUpdateStatus", 1267), ("fwUpgradeUpdateBiosRequest", 1268), ("fwUpgradePollBiosUpdateStatus", 1269), ("fwUpgradeActivateBios", 1270), ("fwUpgradePollBiosActivateStatus", 1271), ("fwUpgradePowerOn", 1272), ("fwUpgradeBmcPreconfigPnuOSLocal", 1273), ("fwUpgradeBmcPreconfigPnuOSPeer", 1274), ("fwUpgradeSwConfigPortNivLocal", 1275), ("fwUpgradeSwConfigPortNivPeer", 1276), ("fwUpgradeSwConfigPnuOSLocal", 1277), ("fwUpgradeSwConfigPnuOSPeer", 1278), ("fwUpgradeUpdateAdaptorNwFwLocal", 1279), ("fwUpgradeUpdateAdaptorNwFwPeer", 1280), ("fwUpgradeWaitForAdaptorNwFwUpdateLocal", 1281), ("fwUpgradeWaitForAdaptorNwFwUpdatePeer", 1282), ("fwUpgradeActivateAdaptorNwFwLocal", 1283), ("fwUpgradeActivateAdaptorNwFwPeer", 1284), ("fwUpgradeNicConfigPnuOSLocal", 1285), ("fwUpgradeNicConfigPnuOSPeer", 1286), ("fwUpgradeBmcConfigPnuOS", 1287), ("fwUpgradeSolRedirectEnable", 1288), ("fwUpgradeSerialDebugPnuOSConnect", 1289), ("fwUpgradeBootPnuos", 1290), ("fwUpgradeBootWait", 1291), ("fwUpgradeBiosPostCompletion", 1292), ("fwUpgradeHagPnuOSConnect", 1293), ("fwUpgradePnuOSIdent", 1294), ("fwUpgradePnuOSPolicy", 1295), ("fwUpgradePnuOSCatalog", 1296), ("fwUpgradePnuOSValidate", 1297), ("fwUpgradePnuOSSelfTest", 1298), ("fwUpgradeStorageCtlrImgUpdate", 1299), ("fwUpgradeHbaImgUpdate", 1300), ("fwUpgradeNicImgUpdate", 1301), ("fwUpgradeLocalDiskFwUpdate", 1302), ("fwUpgradePnuOSConfig", 1303), ("fwUpgradePnuOSInventory", 1304), ("fwUpgradeBiosImgUpdate", 1305), ("fwUpgradePnuOSUnloadDrivers", 1306), ("fwUpgradeBmcUnconfigPnuOS", 1307), ("fwUpgradeNicUnconfigPnuOSLocal", 1308), ("fwUpgradeNicUnconfigPnuOSPeer", 1309), ("fwUpgradeSwUnconfigPnuOSLocal", 1310), ("fwUpgradeSwUnconfigPnuOSPeer", 1311), ("fwUpgradeHagPnuOSDisconnect", 1312), ("fwUpgradeSerialDebugPnuOSDisconnect", 1313), ("fwUpgradeSolRedirectDisable", 1314), ("fwUpgradeShutdown", 1315), ("adapterResetBegin", 1316), ("adapterResetPreSanitize", 1317), ("adapterResetSanitize", 1318), ("adapterResetDeassertResetBypass", 1319), ("adapterResetPowerCycle", 1320), ("activateAdaptorDeassertResetBypass", 1361), ("fwUpgradeDeassertResetBypass", 1363), ("fwUpgradeFail", 1385), ("fwUpgradeSuccess", 1386), ("resetIpmiFail", 1387), ("resetIpmiSuccess", 1388), ("adapterResetFail", 1389), ("adapterResetSuccess", 1390), ("associateConfigFlexFlash", 1471), ("associateSyncPowerState", 1472), ("disassociateUnconfigFlexFlash", 1473), ("cimcSessionDeleteBegin", 1478), ("cimcSessionDeleteExecute", 1479), ("cimcSessionDeleteFail", 1480), ("cimcSessionDeleteSuccess", 1481))

class CucsComputeRackUnitFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeComputeRackUnitAdapterResetAlways", 5), ("samDmeComputeRackUnitAdapterResetPowerOn", 6), ("samDmeComputeRackUnitDiscoverCheckPoint", 24))

class CucsComputeRackUnitFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 599, 1064, 1316))
    namedValues = NamedValues(("nop", 0), ("discover", 599), ("offline", 1064), ("adapterReset", 1316))

class CucsComputeRackUnitMbTempStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("frontTemp", 4), ("frontTempAvg", 5), ("frontTempMax", 6), ("frontTempMin", 7), ("ioh1Temp", 8), ("ioh1TempAvg", 9), ("ioh1TempMax", 10), ("ioh1TempMin", 11), ("ioh2Temp", 12), ("ioh2TempAvg", 13), ("ioh2TempMax", 14), ("ioh2TempMin", 15), ("rearTemp", 16), ("rearTempAvg", 17), ("rearTempMax", 18), ("rearTempMin", 19))

class CucsComputeRackUnitMbTempStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("frontTemp", 4), ("frontTempAvg", 5), ("frontTempMax", 6), ("frontTempMin", 7), ("ioh1Temp", 8), ("ioh1TempAvg", 9), ("ioh1TempMax", 10), ("ioh1TempMin", 11), ("ioh2Temp", 12), ("ioh2TempAvg", 13), ("ioh2TempMax", 14), ("ioh2TempMin", 15), ("rearTemp", 16), ("rearTempAvg", 17), ("rearTempMax", 18), ("rearTempMin", 19))

class CucsComputeScrubAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CucsComputeServerDiscPolicyFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1231))
    namedValues = NamedValues(("nop", 0), ("resolveScrubPolicy", 1231))

class CucsComputeServerDiscPolicyFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1231, 1232, 1391, 1392))
    namedValues = NamedValues(("nop", 0), ("resolveScrubPolicyBegin", 1231), ("resolveScrubPolicyResolve", 1232), ("resolveScrubPolicyFail", 1391), ("resolveScrubPolicySuccess", 1392))

class CucsComputeServerDiscPolicyFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1231))
    namedValues = NamedValues(("nop", 0), ("resolveScrubPolicy", 1231))

class CucsComputeServerMgmtDiscAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("autoAcknowledged", 0), ("userAcknowledged", 1))

class CucsComputeSlotQualMaxId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsComputeSlotQualMinId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsConditionAckAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deleteOnClear", 1), ("initialSeverity", 2))

class CucsConditionActionIndicator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("creation", 0), ("modification", 1), ("deletion", 2), ("stateTransition", 3), ("special", 4), ("failure", 5))

class CucsConditionAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsConditionCallHomeCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))
    namedValues = NamedValues(("unspecified", 0), ("equipmentInoperable", 1), ("thermalProblem", 2), ("connectivityProblem", 3), ("licenseGraceperiodExpired", 4), ("mgmtifDown", 5), ("linkDown", 6), ("electionFailure", 7), ("managementServicesFailure", 8), ("managementServicesUnresponsive", 9), ("versionIncompatible", 10), ("identityUnestablishable", 11), ("equipmentInaccessible", 12), ("configurationFailure", 13), ("associationFailed", 14), ("powerProblem", 15), ("equipmentProblem", 16), ("voltageProblem", 17), ("fruProblem", 18), ("equipmentDisabled", 19), ("limitReached", 20), ("equipmentOffline", 21), ("inventoryFailed", 22), ("portFailed", 23), ("vifIdsMismatch", 24), ("arpTargetsConfigError", 25), ("equipmentDegraded", 26))

class CucsConditionCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261), SingleValueConstraint(262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 283, 284, 285, 286, 287, 288, 289, 290, 291, 293, 294, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 345, 353, 355, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 430, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543), SingleValueConstraint(544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, -1))
    namedValues = NamedValues(("unknown", 0), ("transition", 1), ("beginFailed", 2), ("fsmFailed", 3), ("checkLicenseFailed", 4), ("identifyFailed", 5), ("configureSwMgmtEndPointFailed", 6), ("configureVifNsFailed", 7), ("configureEndPointFailed", 8), ("discoverChassisFailed", 9), ("enableChassisFailed", 10), ("decomissionFailed", 11), ("unIdentifyLocalFailed", 12), ("cleanupEntriesFailed", 13), ("waitFailed", 14), ("disableEndPointFailed", 15), ("unIdentifyPeerFailed", 16), ("executeFailed", 17), ("deployFailed", 18), ("bmcConfigureConnLocalFailed", 20), ("swConfigureConnLocalFailed", 21), ("bmcConfigureConnPeerFailed", 22), ("swConfigureConnPeerFailed", 23), ("bmcPresenceFailed", 24), ("bmcInventoryFailed", 25), ("preSanitizeFailed", 26), ("sanitizeFailed", 27), ("configUserAccessFailed", 28), ("swConfigPnuoslocalFailed", 29), ("swConfigPnuospeerFailed", 30), ("configDiscoveryModeFailed", 31), ("swUnconfigPortNivLocalFailed", 32), ("swUnconfigPortNivPeerFailed", 33), ("bootPnuosFailed", 35), ("bootWaitFailed", 36), ("biosPostCompletionFailed", 37), ("readSmbiosFailed", 38), ("hagConnectFailed", 39), ("pnuosidentFailed", 40), ("pnuospolicyFailed", 41), ("pnuosinventoryFailed", 42), ("pnuosscrubFailed", 43), ("pnuosconnectivityFailed", 44), ("pnuosconnStatusFailed", 45), ("swPnuosconnectivityLocalFailed", 46), ("swPnuosconnectivityPeerFailed", 47), ("pnuosselfTestFailed", 48), ("hagDisconnectFailed", 51), ("bmcShutdownDiscoveredFailed", 52), ("handlePoolingFailed", 53), ("successFailed", 54), ("failFailed", 55), ("configFeLocalFailed", 56), ("swConfigPortNivLocalFailed", 57), ("swConfigPortNivPeerFailed", 58), ("nicPresenceLocalFailed", 59), ("nicPresencePeerFailed", 60), ("nicInventoryLocalFailed", 61), ("nicInventoryPeerFailed", 62), ("deriveConfigFailed", 63), ("configSolFailed", 64), ("swConfigLocalFailed", 65), ("swConfigPeerFailed", 66), ("nicConfigLocalFailed", 67), ("nicConfigPeerFailed", 68), ("stopvmediaLocalFailed", 69), ("stopvmediaPeerFailed", 70), ("setupvmediaLocalFailed", 71), ("setupvmediaPeerFailed", 72), ("bladeBootFailed", 73), ("bladeBootWaitFailed", 74), ("bladeReadSmbiosFailed", 75), ("hostConnectFailed", 76), ("startMemoryTestStatusFailed", 77), ("pollMemoryTestStatusFailed", 78), ("hostIdentFailed", 79), ("hostPolicyFailed", 80), ("setDiagUserFailed", 81), ("hostInventoryFailed", 82), ("hostServerDiagFailed", 83), ("hostServerDiagStatusFailed", 84), ("disableServerConnSwBfailed", 85), ("startFabricatrafficTestFailed", 86), ("fabricatrafficTestStatusFailed", 87), ("enableServerConnSwBfailed", 88), ("disableServerConnSwAfailed", 89), ("startFabricbtrafficTestFailed", 90), ("fabricbtrafficTestStatusFailed", 91), ("enableServerConnSwAfailed", 92), ("generateReportFailed", 93), ("generateLogWaitFailed", 94), ("debugWaitFailed", 95), ("removevmediaLocalFailed", 96), ("removevmediaPeerFailed", 97), ("nicUnconfigLocalFailed", 98), ("nicUnconfigPeerFailed", 99), ("swUnconfigLocalFailed", 100), ("swUnconfigPeerFailed", 101), ("removeConfigFailed", 102), ("restoreConfigFeLocalFailed", 103), ("restoreConfigFePeerFailed", 104), ("unconfigUserAccessFailed", 105), ("unconfigSolFailed", 106), ("hostDisconnectFailed", 107), ("bmcShutdownDiagCompletedFailed", 108), ("evaluateStatusFailed", 109), ("primaryFailed", 110), ("secondaryFailed", 111), ("executeLocalFailed", 112), ("executePeerFailed", 113), ("nicConfigPnuoslocalFailed", 114), ("nicConfigPnuospeerFailed", 115), ("setupVmediaLocalFailed", 116), ("setupVmediaPeerFailed", 117), ("bladeBootPnuosFailed", 118), ("nicUnconfigPnuoslocalFailed", 119), ("nicUnconfigPnuospeerFailed", 120), ("swUnconfigPnuoslocalFailed", 121), ("swUnconfigPnuospeerFailed", 122), ("teardownVmediaLocalFailed", 123), ("teardownVmediaPeerFailed", 124), ("updateibmcfwFailed", 125), ("waitForibmcfwUpdateFailed", 126), ("activateibmcfwFailed", 127), ("resetibmcFailed", 128), ("powerOnFailed", 129), ("updateAdaptorNwFwLocalFailed", 130), ("updateAdaptorNwFwPeerFailed", 131), ("waitForAdaptorNwFwUpdateLocalFailed", 132), ("waitForAdaptorNwFwUpdatePeerFailed", 133), ("activateAdaptorNwFwLocalFailed", 134), ("activateAdaptorNwFwPeerFailed", 135), ("hagPnuosconnectFailed", 136), ("pnuosvalidateFailed", 137), ("biosImgUpdateFailed", 138), ("storageCtlrImgUpdateFailed", 139), ("hbaImgUpdateFailed", 140), ("nicImgUpdateFailed", 141), ("pnuosconfigFailed", 142), ("pnuoslocalDiskConfigFailed", 143), ("swConfigHostoslocalFailed", 144), ("swConfigHostospeerFailed", 145), ("nicConfigHostoslocalFailed", 146), ("nicConfigHostospeerFailed", 147), ("hagPnuosdisconnectFailed", 148), ("pnuosunloadDriversFailed", 149), ("prepareForBootFailed", 150), ("configUuidFailed", 151), ("bootHostFailed", 152), ("waitForConnReadyFailed", 153), ("hostosidentFailed", 154), ("hostospolicyFailed", 155), ("hostosvalidateFailed", 156), ("hostosconfigFailed", 157), ("nicUnconfigHostoslocalFailed", 158), ("nicUnconfigHostospeerFailed", 159), ("swUnconfigHostoslocalFailed", 160), ("swUnconfigHostospeerFailed", 161), ("pnuosunconfigFailed", 162), ("unconfigUuidFailed", 163), ("shutdownFailed", 164), ("unconfigSoLfailed", 165), ("configFailed", 166), ("swUnconfigureLocalFailed", 167), ("swUnconfigurePeerFailed", 168), ("startFailed", 169), ("cleanupFailed", 170), ("resetFailed", 171), ("unconfigBiosFailed", 172), ("applyTemplateFailed", 173), ("applyIdentifiersFailed", 174), ("applyPoliciesFailed", 175), ("resolveBootConfigFailed", 176), ("evaluateAssociationFailed", 177), ("analyzeImpactFailed", 178), ("waitForMaintPermissionFailed", 179), ("waitForMaintWindowFailed", 180), ("reconfigUuidFailed", 181), ("updateEthMonFailed", 182), ("updateFcMonFailed", 183), ("serverMoved", 186), ("serverIdentificationProblem", 187), ("primaryVlanMissingIsolated", 188), ("namedPolicyUnresolved", 189), ("localFailed", 190), ("peerFailed", 191), ("configurationFailed", 192), ("equipmentInoperable", 193), ("thermalProblem", 194), ("voltageProblem", 195), ("capacityExceeded", 196), ("equipmentDegraded", 197), ("identityUnestablishable", 198), ("setEpLocalFailed", 199), ("setEpPeerFailed", 200), ("propogateEpSettingsFailed", 201), ("propogateEpTimeZoneSettingsLocalFailed", 202), ("propogateEpTimeZoneSettingsPeerFailed", 203), ("restartFailed", 204), ("setRealmLocalFailed", 205), ("setRealmPeerFailed", 206), ("setUserPeerFailed", 208), ("setKeyRingLocalFailed", 209), ("setKeyRingPeerFailed", 210), ("unidentifiableFru", 211), ("equipmentMissing", 212), ("connectivityProblem", 213), ("linkDown", 214), ("linkMisconnected", 215), ("disableFailed", 216), ("enableFailed", 217), ("disableAfailed", 218), ("enableAfailed", 219), ("propogateEpTimeZoneSettingsToAdaptorsLocalFailed", 220), ("propogateEpTimeZoneSettingsToAdaptorsPeerFailed", 221), ("vifDown", 222), ("updateConnectivityFailed", 223), ("createLocalFailed", 224), ("createRemoteFailed", 225), ("unpackLocalFailed", 226), ("deleteLocalFailed", 227), ("copyRemoteFailed", 228), ("remoteFailed", 229), ("updateLocalFailed", 230), ("verifyLocalFailed", 231), ("resetLocalFailed", 232), ("updateRemoteFailed", 233), ("verifyRemoteFailed", 234), ("resetRemoteFailed", 235), ("updateRequestFailed", 236), ("pollUpdateStatusFailed", 237), ("activateFailed", 238), ("updateRequestLocalFailed", 239), ("updateRequestPeerFailed", 240), ("pollUpdateStatusLocalFailed", 241), ("pollUpdateStatusPeerFailed", 242), ("powerOffFailed", 243), ("copyPrimaryFailed", 244), ("imageDeleted", 245), ("imageUnusable", 246), ("imageCannotBoot", 247), ("psuInsufficient", 248), ("rescanImagesFailed", 249), ("applyCatalogFailed", 250), ("syncBladeaglocalFailed", 251), ("syncBladeagremoteFailed", 252), ("syncNicaglocalFailed", 253), ("syncNicagremoteFailed", 254), ("syncPortaglocalFailed", 255), ("syncPortagremoteFailed", 256), ("syncHostagentaglocalFailed", 257), ("syncHostagentagremoteFailed", 258), ("finalizeFailed", 259), ("validateLocalFailed", 260), ("validateRemoteFailed", 261)) + NamedValues(("deleteRemoteFailed", 262), ("licenseGraceperiodEntered", 263), ("licenseGraceperiod10days", 264), ("oldChassisComponentFirmware", 265), ("licenseGraceperiod60days", 266), ("psuFailure", 267), ("psuRedundancyFail", 268), ("licenseGraceperiodExpired", 269), ("powerConsumptionHitLimit", 270), ("noAckFromBios", 271), ("portFailed", 272), ("interfaceFailed", 273), ("operationalStateDown", 274), ("cmcVifDown", 275), ("setLocalFailed", 276), ("setPeerFailed", 277), ("switchFailed", 278), ("limitReached", 279), ("emptyPool", 280), ("decommissioned", 283), ("uploadFailed", 284), ("downloadLocalFailed", 285), ("tftpServerError", 286), ("electionFailure", 287), ("managementServicesFailure", 288), ("managementServicesUnresponsive", 289), ("haNotReady", 290), ("versionIncompatible", 291), ("logCapacity", 293), ("fileTransferFailed", 294), ("insufficientResources", 296), ("insufficientlyEquipped", 297), ("powerProblem", 298), ("discoveryFailed", 299), ("associationFailed", 300), ("unsupportedTransceiver", 301), ("equipmentProblem", 302), ("discoveryInProgress", 303), ("configurationInProgress", 304), ("unconfigurationInProgress", 305), ("poweredOff", 306), ("inMaintenance", 307), ("underTest", 308), ("serverUnassociated", 309), ("serverAssociating", 310), ("unassociated", 311), ("serverDeassociating", 312), ("serverUnassigned", 313), ("serverAssigned", 314), ("configurationNotApplied", 315), ("configurationApplying", 316), ("propogateEpTimeZoneSettingsToFexIomLocalFailed", 317), ("serverFailed", 318), ("configurationFailure", 319), ("maintenanceFailed", 320), ("equipmentRemoved", 321), ("serverInaccessible", 322), ("getVersionFailed", 324), ("removeLocalFailed", 325), ("setEpAfailed", 326), ("setEpBfailed", 327), ("satelliteConnectionAbsent", 328), ("satelliteConnectionInit", 329), ("satelliteMisConnected", 330), ("unexpectedNumberOfLinks", 331), ("equipmentOffline", 332), ("performanceProblem", 333), ("firmwareUpgradeProblem", 334), ("unsupportedConnectivityConfiguration", 335), ("equipmentUnacknowledged", 336), ("autoFirmwareUpgrade", 337), ("equipmentDisconnected", 338), ("fruProblem", 339), ("thresholdCrossed", 340), ("deviceSEEPROMIOError", 345), ("assignmentFailed", 353), ("deviceSeepromError", 355), ("newLink", 360), ("bmcPreconfigPnuoslocalFailed", 361), ("bmcPreconfigPnuospeerFailed", 362), ("bmcConfigPnuosFailed", 363), ("solRedirectEnableFailed", 364), ("serialDebugConnectFailed", 365), ("bmcUnconfigPnuosFailed", 366), ("serialDebugDisconnectFailed", 367), ("solRedirectDisableFailed", 368), ("configNivModeFailed", 369), ("cleanupLocalFailed", 370), ("cleanupPeerFailed", 371), ("configFePeerFailed", 372), ("bladePowerOnFailed", 373), ("cleanupServerConnSwAfailed", 374), ("cleanupServerConnSwBfailed", 375), ("bmcPreConfigPnuoslocalFailed", 376), ("bmcPreConfigPnuospeerFailed", 377), ("bladePowerOffFailed", 378), ("updateBoardCtrlRequestFailed", 379), ("pollBoardCtrlUpdateStatusFailed", 380), ("serialDebugPnuosconnectFailed", 381), ("localDiskFwUpdateFailed", 382), ("serialDebugPnuosdisconnectFailed", 383), ("configSoLfailed", 384), ("hagHostosconnectFailed", 385), ("configBiosFailed", 386), ("cleanupcimcFailed", 387), ("aFailed", 388), ("bFailed", 389), ("reconfigBiosFailed", 390), ("applyConfigFailed", 391), ("mgmtifDown", 392), ("validateConfigurationFailed", 393), ("applyPhysicalFailed", 394), ("waitOnPhysFailed", 395), ("emptyPinGroup", 396), ("membershipDown", 397), ("vsanMisconfigured", 398), ("incompatibleSpeed", 399), ("configError", 400), ("vlanMisconfigured", 401), ("interfaceMisconfigured", 402), ("missingPrimaryVlan", 403), ("pinningMismatch", 404), ("pinningMisconfig", 405), ("equipmentDisabled", 406), ("propogateEpTimeZoneSettingsToFexIomPeerFailed", 407), ("setUserLocalFailed", 408), ("linkMissing", 409), ("disableBfailed", 410), ("enableBfailed", 411), ("copySubFailed", 412), ("deleteSubFailed", 413), ("deletePrimaryFailed", 414), ("groupCapInsufficient", 415), ("oldFirmware", 416), ("powerCapFail", 417), ("noCapFail", 418), ("portInventorySwAfailed", 419), ("portInventorySwBfailed", 420), ("configSwAfailed", 421), ("configSwBfailed", 422), ("verifyPhysConfigFailed", 423), ("activateLocalFailed", 424), ("activatePeerFailed", 425), ("prepareForUpdateFailed", 426), ("activationFailed", 427), ("applyFailed", 428), ("licenseGraceperiod30days", 430), ("licenseGraceperiod90days", 432), ("licenseGraceperiod119days", 433), ("licenseFileUninstallable", 434), ("licenseFileNotDeleted", 435), ("backupLocalFailed", 436), ("reportResultsFailed", 437), ("deviceSharedStorageError", 438), ("haSshKeysMismatched", 439), ("ucsmProcessFailure", 440), ("equipmentInaccessible", 441), ("nonExistentScheduler", 442), ("executeAfailed", 443), ("executeBfailed", 444), ("powerDown", 445), ("leadershipChange", 446), ("deviceSharedStorageIOError", 447), ("serverAssociated", 448), ("configurationApplied", 449), ("inventoryFailed", 454), ("configureFailed", 455), ("clearFailed", 456), ("pollClearStatusFailed", 457), ("pollActivateStatusFailed", 458), ("updateTokensFailed", 459), ("hostCatalogFailed", 460), ("pnuoscatalogFailed", 461), ("clearBiosUpdateFailed", 462), ("pollClearBiosUpdateStatusFailed", 463), ("updateBiosRequestFailed", 464), ("pollBiosUpdateStatusFailed", 465), ("activateBiosFailed", 466), ("pollBiosActivateStatusFailed", 467), ("fexUnsupported", 468), ("invalidKeyringCertificate", 469), ("invalidTrustpointCertChain", 470), ("disassociationFailed", 471), ("vifIdsMismatch", 472), ("profileConfigIncorrect", 473), ("updateVlanGroupsFailed", 474), ("updateZonesFailed", 475), ("vlanCompNotSupport", 476), ("anotherConnectionAlreadyEnabled", 477), ("connectionUnused", 478), ("unsupportedConnectivity", 479), ("reportFailed", 480), ("providerGroupAlreadyExists", 481), ("noVlanOptimization", 482), ("roleConfigError", 483), ("localeConfigError", 484), ("userRoleConfigError", 485), ("userLocaleConfigError", 486), ("keyringConfigError", 487), ("snmpConfigError", 488), ("timezoneFileNotExists", 489), ("userConfigError", 490), ("snmpUserConfigError", 491), ("commSvcConfigError", 492), ("inaccessibleVlanReferenced", 493), ("referencedVlanUnresolvable", 494), ("invalidVlanInTheAllowedVlanList", 495), ("vlanConflictPermit", 496), ("vlanPermitUnresolved", 497), ("groupPermitUnresolved", 498), ("removeFailed", 499), ("arpTargetsConfigError", 500), ("newVnicVconSchemeApplied", 501), ("suspendModeEntered", 502), ("verifyGuidFailed", 503), ("unregisterFailed", 504), ("cleanOldDataFailed", 505), ("requestFailed", 506), ("verifyFailed", 507), ("resolveFailed", 508), ("releaseFailed", 509), ("resolveManyFailed", 510), ("releaseManyFailed", 511), ("resolveAllFailed", 512), ("releaseAllFailed", 513), ("registerClientFailed", 514), ("verifyRegistrationFailed", 515), ("mountLocalFailed", 516), ("mountPeerFailed", 517), ("unmountLocalFailed", 518), ("unmountPeerFailed", 519), ("checkPowerAvailabilityFailed", 520), ("markAdapterForRebootFailed", 521), ("deassertResetBypassFailed", 522), ("verifyFcZoneConfigFailed", 523), ("cleanupPortConfigLocalFailed", 524), ("cleanupPortConfigPeerFailed", 525), ("powerCycleFailed", 526), ("resolveIdentifiersFailed", 527), ("applyDefaultIdentifiersFailed", 528), ("resolveDefaultIdentifiersFailed", 529), ("resolvePoliciesFailed", 530), ("resolveDistributableNamesFailed", 531), ("resolveDistributableFailed", 532), ("resolveImagesFailed", 533), ("resolveScheduleFailed", 534), ("provisionStorageFailed", 535), ("waitForStorageProvisionFailed", 536), ("commitStorageFailed", 537), ("waitForCommitStorageFailed", 538), ("waitForAssocCompletionFailed", 539), ("enablePortFailed", 540), ("loadCatalogFailed", 541), ("pingFailed", 542), ("suppressStatusChange", 543)) + NamedValues(("fcoeUplinkUnsupportedFiSettings", 544), ("fcoeUplinkPortChannelUnsupportedFiSettings", 545), ("invalidTarget", 546), ("fcZoningEnabled", 547), ("configurationError", 548), ("fcStorageportNpvMode", 549), ("fcoeStorageportNpvMode", 550), ("fcPortchannelMembersInconsistentSpeed", 551), ("vlanMcastPolicyMisconfigured", 552), ("clientLostConnectivity", 553), ("callhomeConfigError", 554), ("copyExtToLocalFailed", 555), ("copyExtToPeerFailed", 556), ("copyToLocalFailed", 557), ("copyToPeerFailed", 558), ("waitForDeployFailed", 559), ("activateucsmFailed", 560), ("pollActivateOfucsmFailed", 561), ("updateiomFailed", 562), ("pollUpdateOfiomFailed", 563), ("activateiomFailed", 564), ("pollActivateOfiomFailed", 565), ("activateRemotefiFailed", 566), ("pollActivateOfRemotefiFailed", 567), ("waitForUserAckFailed", 568), ("activateLocalfiFailed", 569), ("pollActivateOfLocalfiFailed", 570), ("activateCatalogFailed", 571), ("referencedVsanUnresolvable", 572), ("operationFailed", 573), ("localeOrgConfigError", 574), ("resolveNetworkPoliciesFailed", 575), ("resolveNetworkTemplatesFailed", 576), ("validatePolicyOwnershipFailed", 577), ("configFlexFlashFailed", 578), ("syncPowerStateFailed", 579), ("unconfigFlexFlashFailed", 580), ("syncFailed", 581), ("reportFullInventoryFailed", 582), ("healthLedAmberBlinking", 583), ("healthLedAmber", 584), ("extraPrimaryVlans", 585), ("licenseInsufficient", 586), ("checkInventoryStatusFailed", 587), ("any", -1))

class CucsConditionCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 156, 157, 169, 170, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 200, 203, 206, 207, 209, 276, 277, 278, 279, 282, 283, 291, 293, 294, 304, 305, 306, 310, 311, 312, 313, 314, 315, 317, 318, 319, 320, 321, 322, 324, 326, 327, 329, 330, 331, 332, 334, 337, 367, 368, 369, 371, 373, 374, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 387, 389, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 424, 425, 428, 429, 430, 434, 435, 436, 440, 451, 452, 453, 454, 455, 456, 458, 459, 460, 461, 462, 463, 464, 465, 466, 470, 471, 476, 478, 479, 480, 481, 484, 502, 517, 528, 531, 532, 533, 535, 536, 537, 538, 539, 540, 543, 549, 620, 621, 622, 625, 626, 635, 637, 640, 642, 643, 670, 671, 672, 673, 674, 675, 676, 677, 678, 688, 689, 702, 703, 708, 713, 717, 727, 728, 729, 730, 731, 733, 734, 735, 736, 740, 741, 742, 743, 744, 747, 757, 764, 765, 766, 772, 775, 776, 777, 778, 791, 792, 793, 794, 795, 796, 797, 798, 801, 807, 821, 826, 829, 831, 832, 833, 834, 835, 836, 837, 838, 840, 841, 842, 843, 844, 846, 855, 856, 857, 858, 859, 861, 862, 863, 864, 865, 866, 867, 868, 869, 872, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 887, 890, 900, 901, 902), SingleValueConstraint(903, 909, 910, 915, 916, 917, 918, 919, 920, 921, 928, 932, 933, 934, 935, 936, 937, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 957, 958, 959, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 988, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1017, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1040, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1097, 1098, 1099, 1101, 1102, 1103, 1104, 1105, 1106, 1114, 1202, 1204, 1205, 1206, 1207, 1208, 1209, 1216, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1232, 1233, 1237, 16405, 16406, 16407, 16408, 16518, 16519, 16520, 16533, 16534, 16535, 16539, 16550, 16576, 16577, 16579, 16580, 16581, 16582, 16600, 16601, 16604, 16605, 16606, 16634, 16635, 16636, 16637, 16641, 16650, 16651, 16653, 16654, 16655, 16656, 16657, 16670, 16673, 16674, 16679, 16680, 16681, 16682, 16683, 16684, 16742, 16745, 16749, 16750, 16803, 16815, 16823, 16852, 16857, 16858, 16879, 16880, 16881, 16898, 16904, 16906, 16930, 16931, 16942, 16943, 16944, 16945, 16973, 16974, 16975, 16976, 16977, 16978, 16979, 16980, 16981, 16982, 16983, 16984, 16986, 16987, 16988, 16994, 16995, 17000, 17001, 17002, 17008, 17012, 17013, 17014, 17043, 17044, 17045, 17046, 17050, 17051, 17052, 17053, 17083, 17084, 17089, 17116, 17133, 17134, 17163, 17169, 17170, 17187, 17188, 17190, 17192, 17195, 17196, 17207, 17214, 17223), SingleValueConstraint(17232, 17239, 17254, 17259, 17262, 17271, 17281, 17282, 17312, 17313, 17325, 17326, 17327, 17328, 17339, 17340, 17348, 17349, 17350, 17358, 17359, 17360, 17361, 17367, 17377, 17378, 17379, 17381, 17382, 17383, 17384, 17395, 17399, 17400, 17402, 17403, 17404, 17405, 17406, 17407, 17408, 17409, 17410, 17411, 17412, 17413, 17414, 17415, 17416, 17418, 17419, 17420, 17425, 17426, 17427, 17428, 17439, 17445, 17446, 17447, 17448, 17449, 17450, 17451, 17452, 17453, 17454, 17455, 17456, 17457, 17458, 17459, 17460, 17461, 17462, 17476, 17477, 17478, 17483, 17484, 17485, 17491, 17492, 17493, 17494, 17499, 17599, 17601, 17602, 33142, 33144, 33145, 33146, 33167, 33168, 33169, 33170, 33177, 33178, 33179, 33180, 33187, 33188, 33189, 33190, 33197, 33198, 33199, 33200, 33211, 33212, 33213, 33214, 33221, 33222, 33223, 33224, 33231, 33232, 33233, 33234, 33241, 33242, 33243, 33244, 33251, 33252, 33253, 33254, 33261, 33262, 33263, 33264, 33271, 33272, 33273, 33274, 33281, 33282, 33283, 33284, 33291, 33292, 33293, 33294, 33301, 33302, 33303, 33304, 33483, 33485, 33486, 33487, 33491, 33493, 33494, 33495, 33499, 33501, 33502, 33503, 33720, 33721, 33722, 33723, 33730, 33731, 33732, 33733, 33740, 33741, 33742, 33743, 33750, 33751, 33752, 33753, 33760, 33761, 33762, 33763, 33770, 33771, 33772, 33773, 33810, 33811, 33812, 33813, 33820, 33821, 33822, 33823, 33830, 33831, 33832, 33833, 33840, 33841, 33842, 33843, 33850, 33851, 33852, 33853, 33860, 33861, 33862, 33863, 33875, 33876, 33877, 33878, 33885, 33886, 33887, 33888, 33895, 33896, 33897, 33898, 33905, 33906, 33907, 33908, 33915, 33916, 33917, 33918, 33925, 33926, 33927, 33928, 33940, 33941, 33942, 33943, 33950, 33951, 33952, 33953, 33960, 33961, 33962, 33963, 33970, 33971, 33972, 33973, 33980, 33981, 33982, 33983, 33995, 33996), SingleValueConstraint(33997, 33998, 34005, 34006, 34007, 34008, 34015, 34016, 34017, 34018, 34030, 34031, 34032, 34033, 34040, 34041, 34042, 34043, 34050, 34051, 34052, 34053, 34064, 34065, 34066, 34067, 34074, 34075, 34076, 34077, 34084, 34085, 34086, 34087, 34094, 34095, 34096, 34097, 34108, 34109, 34110, 34111, 34118, 34119, 34120, 34121, 34128, 34129, 34130, 34131, 34138, 34139, 34140, 34141, 34148, 34149, 34150, 34151, 34158, 34159, 34160, 34161, 34168, 34169, 34170, 34171, 34178, 34179, 34180, 34181, 34192, 34193, 34194, 34195, 34202, 34203, 34204, 34205, 34212, 34213, 34214, 34215, 34222, 34223, 34224, 34225, 34232, 34233, 34234, 34235, 34246, 34247, 34248, 34249, 34256, 34257, 34258, 34259, 34271, 34272, 34273, 34274, 34281, 34282, 34283, 34284, 34291, 34292, 34293, 34294, 34301, 34302, 34303, 34304, 34316, 34317, 34318, 34319, 34326, 34327, 34328, 34329, 34336, 34337, 34338, 34339, 34346, 34347, 34348, 34349, 34361, 34362, 34363, 34364, 34371, 34372, 34373, 34374, 34381, 34382, 34383, 34384, 34396, 34397, 34398, 34399, 34406, 34407, 34408, 34409, 34416, 34417, 34418, 34419, 34426, 34427, 34428, 34429, 34436, 34437, 34438, 34439, 34451, 34452, 34453, 34454, 34461, 34462, 34463, 34464, 34471, 34472, 34473, 34474, 34481, 34482, 34483, 34484, 34496, 34497, 34498, 34499, 34506, 34507, 34508, 34509, 34516, 34517, 34518, 34519, 34526, 34527, 34528, 34529, 34542, 34543, 34544, 34545, 34552, 34553, 34554, 34555, 34562, 34563, 34564, 34565, 34572, 34573, 34574, 34575, 34588, 34589, 34590, 34591, 34598, 34599, 34600, 34601, 34608, 34609, 34610, 34611, 34618, 34619, 34620, 34621, 34633, 34634, 34635, 34636, 34643, 34644, 34645, 34646, 34653, 34654, 34655, 34656, 34663, 34664, 34665, 34666, 34673, 34674, 34675, 34676, 34688, 34689, 34690, 34691, 34698, 34699, 34700, 34701, 34708), SingleValueConstraint(34709, 34710, 34711, 34718, 34719, 34720, 34721, 34733, 34734, 34735, 34736, 34743, 34744, 34745, 34746, 34753, 34754, 34755, 34756, 34763, 34764, 34765, 34766, 34778, 34779, 34780, 34781, 34788, 34789, 34790, 34791, 34798, 34799, 34800, 34801, 34808, 34809, 34810, 34811, 34822, 34823, 34824, 34825, 34832, 34833, 34834, 34835, 34842, 34843, 34844, 34845, 34852, 34853, 34854, 34855, 34862, 34863, 34864, 34865, 34872, 34873, 34874, 34875, 34882, 34883, 34884, 34885, 34892, 34893, 34894, 34895, 34906, 34907, 34908, 34909, 34916, 34917, 34918, 34919, 34926, 34927, 34928, 34929, 34936, 34937, 34938, 34939, 34950, 34951, 34952, 34953, 34960, 34961, 34962, 34963, 34970, 34971, 34972, 34973, 34980, 34981, 34982, 34983, 34990, 34991, 34992, 34993, 35000, 35001, 35002, 35003, 35010, 35011, 35012, 35013, 35020, 35021, 35022, 35023, 35166, 35168, 35169, 35170, 35174, 35176, 35177, 35178, 35198, 35200, 35201, 35202, 35206, 35208, 35209, 35210, 35214, 35216, 35217, 35218, 35222, 35224, 35225, 35226, 35234, 35236, 35237, 35238, 35242, 35244, 35245, 35246, 35250, 35252, 35253, 35254, 35275, 35276, 35277, 35278, 35285, 35286, 35287, 35288, 35295, 35296, 35297, 35298, 35305, 35306, 35307, 35308, 35315, 35316, 35317, 35318, 35329, 35330, 35331, 35332, 35339, 35340, 35341, 35342, 35349, 35350, 35351, 35352, 35359, 35360, 35361, 35362, 35369, 35370, 35371, 35372, 35379, 35380, 35381, 35382, 35962, 35964, 35965, 35966, 35974, 35976, 35977, 35978, 36234, 36236, 36237, 36238, 36242, 36244, 36245, 36246, 36266, 36268, 36269, 36270, 36274, 36276, 36277, 36278, 36282, 36284, 36285, 36286, 36294, 36296, 36297, 36298, 36302, 36304, 36305, 36306, 36310, 36312, 36313, 36314, 36323, 36325, 36326, 36327, 36335, 36337, 36338, 36339, 37154, 37156, 37157, 37158, 37162, 37164, 37165, 37166), SingleValueConstraint(37170, 37172, 37173, 37174, 37269, 37271, 37272, 37273, 37313, 37314, 37315, 37316, 37323, 37324, 37325, 37326, 37333, 37334, 37335, 37336, 37343, 37344, 37345, 37346, 37353, 37354, 37355, 37356, 37363, 37364, 37365, 37366, 37383, 37384, 37385, 37386, 37393, 37394, 37395, 37396, 37403, 37404, 37405, 37406, 37413, 37414, 37415, 37416, 37423, 37424, 37425, 37426, 37443, 37444, 37445, 37446, 37453, 37454, 37455, 37456, 37463, 37464, 37465, 37466, 37473, 37474, 37475, 37476, 37485, 37486, 37487, 37488, 37495, 37496, 37497, 37498, 37505, 37506, 37507, 37508, 37532, 37533, 37534, 37535, 37543, 37544, 37545, 37546, 37553, 37554, 37555, 37556, 37564, 37566, 37567, 37568, 37572, 37574, 37575, 37576, 37580, 37582, 37583, 37584, 37600, 37602, 37603, 37604, 37610, 37612, 37613, 37614, 37771, 37773, 37774, 37775, 37779, 37781, 37782, 37783, 38022, 38032, 38044, 38054, 38064, 38086, 38096, 38106, 38128, 38138, 38148, 38158, 38311, 38313, 38314, 38315, 38349, 38351, 38352, 38353, 38357, 38359, 38360, 38361, 38408, 38409, 38410, 38411, 38438, 38440, 38441, 38442, 38451, 38453, 38454, 38455, 38779, 38788, 38797, 38806, 38815, 38829, 38838, 38847, 38856, 38909, 39032, 39034, 39035, 39036, 39040, 39042, 39043, 39044, 39240, 39242, 39243, 39244, 39421, 39423, 39424, 39425, 39429, 39431, 39432, 39433, 39437, 39439, 39440, 39441, 39445, 39447, 39448, 39449, 39453, 39455, 39456, 39457, 39464, 39466, 39467, 39468, 39472, 39474, 39475, 39476, 39480, 39482, 39483, 39484, 39488, 39490, 39491, 39492, 39498, 39500, 39501, 39502, 39506, 39508, 39509, 39510, 39514, 39516, 39517, 39518, 39525, 39527, 39528, 39529, 39533, 39535, 39536, 39537, 39541, 39543, 39544, 39545, 39549, 39551, 39552, 39553, 39557, 39559, 39560, 39561, 39565, 39567, 39568, 39569, 39575, 39577, 39578, 39579, 40092), SingleValueConstraint(40094, 40095, 40096, 40100, 40102, 40103, 40104, 40108, 40110, 40111, 40112, 40116, 40118, 40119, 40120, 40124, 40126, 40127, 40128, 40441, 40443, 40444, 40445, 40449, 40451, 40452, 40453, 40457, 40459, 40460, 40461, 40547, 40549, 40550, 40551, 40555, 40557, 40558, 40559, 40563, 40565, 40566, 40567, 40574, 40576, 40577, 40578, 40582, 40583, 40584, 40585, 40586, 40587, 40591, 40593, 40594, 40595, 40967, 40969, 40970, 40971, 40975, 40978, 40979, 40980, 40984, 40986, 40987, 40988, 41016, 41018, 41019, 41020, 41024, 41026, 41027, 41028, 41032, 41034, 41035, 41036, 41049, 41050, 41051, 41052, 41059, 41060, 41061, 41062, 41069, 41070, 41071, 41072, 41079, 41080, 41081, 41082, 41089, 41090, 41091, 41092, 41099, 41100, 41101, 41102, 41109, 41110, 41111, 41112, 41119, 41120, 41121, 41122, 41199, 41201, 41202, 41203, 41207, 41209, 41210, 41211, 41215, 41217, 41218, 41219, 41289, 41290, 41291, 41292, 41299, 41300, 41301, 41302, 41309, 41310, 41311, 41312, 41319, 41320, 41321, 41322, 41329, 41330, 41331, 41332, 41339, 41340, 41341, 41342, 41349, 41350, 41351, 41352, 41359, 41360, 41361, 41362, 41443, 41444, 41445, 41446, 41453, 41454, 41455, 41456, 41463, 41464, 41465, 41466, 41473, 41474, 41475, 41476, 41483, 41484, 41485, 41486, 41493, 41494, 41495, 41496, 41503, 41504, 41505, 41506, 41513, 41514, 41515, 41516, 77845, 77846, 77847, 77848, 77958, 77959, 77960, 77973, 77974, 77975, 77979, 77990, 78016, 78017, 78019, 78020, 78021, 78022, 78040, 78041, 78044, 78045, 78046, 78074, 78075, 78076, 78077, 78081, 78090, 78091, 78093, 78094, 78095, 78096, 78097, 78110, 78113, 78114, 78119, 78120, 78121, 78122, 78123, 78124, 78182, 78185, 78189, 78190, 78243, 78255, 78263, 78292, 78297, 78298, 78319, 78320, 78321, 78338, 78344, 78346, 78370, 78371, 78382, 78383, 78384, 78385), SingleValueConstraint(78413, 78414, 78415, 78416, 78417, 78418, 78419, 78420, 78421, 78422, 78423, 78424, 78426, 78427, 78428, 78434, 78435, 78440, 78441, 78442, 78448, 78452, 78453, 78454, 78483, 78484, 78485, 78486, 78490, 78491, 78492, 78493, 78523, 78524, 78529, 78556, 78573, 78574, 78603, 78609, 78610, 78627, 78628, 78630, 78632, 78635, 78636, 78647, 78654, 78663, 78672, 78679, 78694, 78699, 78702, 78711, 78721, 78722, 78752, 78753, 78765, 78766, 78767, 78768, 78779, 78780, 78788, 78789, 78790, 78798, 78799, 78800, 78801, 78807, 78817, 78818, 78819, 78821, 78822, 78823, 78824, 78835, 78839, 78840, 78842, 78843, 78844, 78845, 78846, 78847, 78848, 78849, 78850, 78851, 78852, 78853, 78854, 78855, 78856, 78858, 78859, 78860, 78865, 78866, 78867, 78868, 78879, 78885, 78886, 78887, 78888, 78889, 78890, 78891, 78892, 78893, 78894, 78895, 78896, 78897, 78898, 78899, 78900, 78901, 78902, 78916, 78917, 78918, 78923, 78924, 78925, 78931, 78932, 78933, 78934, 78939, 79039, 79041, 79042, 999445, 999446, 999447, 999448, 999558, 999559, 999560, 999573, 999574, 999575, 999579, 999590, 999616, 999617, 999619, 999620, 999621, 999622, 999640, 999641, 999644, 999645, 999646, 999674, 999675, 999676, 999677, 999681, 999690, 999691, 999693, 999694, 999695, 999696, 999697, 999710, 999713, 999714, 999719, 999720, 999721, 999722, 999723, 999724, 999782, 999785, 999789, 999790, 999843, 999855, 999863, 999892, 999897, 999898, 999919, 999920, 999921, 999938, 999944, 999946, 999970, 999971, 999982, 999983, 999984, 999985, 1000013, 1000014, 1000015, 1000016, 1000017, 1000018, 1000019, 1000020, 1000021, 1000022, 1000023, 1000024, 1000026, 1000027, 1000028, 1000034, 1000035, 1000040, 1000041, 1000042, 1000048, 1000052, 1000053, 1000054, 1000083, 1000084, 1000085, 1000086, 1000090, 1000091, 1000092, 1000093, 1000123, 1000124, 1000129, 1000156, 1000173, 1000174, 1000203, 1000209, 1000210, 1000227, 1000228, 1000230, 1000232, 1000235, 1000236, 1000247, 1000254, 1000263), SingleValueConstraint(1000272, 1000279, 1000294, 1000299, 1000302, 1000311, 1000321, 1000322, 1000352, 1000353, 1000365, 1000366, 1000367, 1000368, 1000379, 1000380, 1000388, 1000389, 1000390, 1000398, 1000399, 1000400, 1000401, 1000407, 1000417, 1000418, 1000419, 1000421, 1000422, 1000423, 1000424, 1000435, 1000439, 1000440, 1000442, 1000443, 1000444, 1000445, 1000446, 1000447, 1000448, 1000449, 1000450, 1000451, 1000452, 1000453, 1000454, 1000455, 1000456, 1000458, 1000459, 1000460, 1000465, 1000466, 1000467, 1000468, 1000479, 1000485, 1000486, 1000487, 1000488, 1000489, 1000490, 1000491, 1000492, 1000493, 1000494, 1000495, 1000496, 1000497, 1000498, 1000499, 1000500, 1000501, 1000502, 1000516, 1000517, 1000518, 1000523, 1000524, 1000525, 1000531, 1000532, 1000533, 1000534, 1000539, 1000639, 1000641, 1000642, 4194528, 4194529, 4194530, 4194531, 4194532, 4194533, 4194534, 4194535, 4194536, 4194537, 4194538, 4194539, 4194540, 4194541, 4194542, 4194543, 4194544, 4194545, 4194546, 4194547, 4194548, 4194549, 4194550, 4194551, 4194552, 4194553, 4194554, 4194555, 4194556, 4194557, 4194558, 4194559, 4194560, 4194561, 4194562, 4194563, 4194564, 4194565, 4194566, 4194567, 4194568, 4194569, 4194570, 4194571, 4194572, 4194573, 4194574, 4194575, 4194576, 4194577, 4194578, 4194579, 4194580, 4194581, 4194582, 4194583, 4194584, 4194585, 4194586, 4194587, 4194591, 4194592, 4194593, 4194594, 4194595, 4194596, 4194597, 4194598, 4194599, 4194600, 4194601, 4194602, 4194603, 4194604, 4194605, 4194607, 4194608, 4194609, 4194610, 4194611, 4194612, 4194613, 4194614, 4194615, 4194616, 4194617, 4194620, 4194621, 4194622, 4194623, 4194624, 4194626, 4194627, 4194628, 4194629, 4194630, 4194631, 4194632, 4194652, 4194654, 4194655, 4194656, 4194657, 4194658, 4194659, 4194660, 4194661, 4194662, 4194663, 4194664, 4194665, 4194671, 4194672, 4194673, 4194674, 4194675, 4194676, 4194683, 4194684, 4194685, 4194686, 4194687, 4194688, 4194689, 4194693, 4194694, 4194695, 4194697, 4194698, 4194699, 4194700, 4194701, 4194702, 4194703, 4194704, 4194705, 4194706, 4194714, 4194715, 4194717, 4194718, 4194719, 4194720, 4194721, 4194722, 4194723, 4194724, 4194725, 4194726, 4194727, 4194728, 4194729, 4194730, 4194734, 4194736, 4194737, 4194738, 4194739, 4194740, 4194741, 4194744, 4194745, 4194746, 4194747, 4194748, 4194749), SingleValueConstraint(4194750, 4194751, 4194752, 4194753, 4194754, 4194755, 4194763, 4194764, 4194765, 4194766, 4194767, 4194768, 4194769, 4194770, 4194771, 4194773, 4194774, 4194775, 4194776, 4194777, 4194778, 4194787, 4194788, 4194789, 4194790, 4194791, 4194792, 4194793, 4194794, 4194795, 4194796, 4194797, 4194798, 4194799, 4194800, 4194801, 4194802, 4194803, 4194804, 4194805, 4194806, 4194807, 4194812, 4194828, 4194830, 4194831, 4194832, 4194833, 4194834, 4194835, 4194836, 4194839, 4194840, 4194841, 4194842, 4194843, 4194844, 4194847, 4194848, 4194849, 4194855, 4194856, 4194859, 4194860, 4194861, 4194862, 4194863, 4194864, 4194865, 4194866, 4194867, 4194868, 4194869, 4194871, 4194876, 4194878, 4194879, 4194880, 4194881, 4194883, 4194884, 4194885, 4194886, 4194887, 4194888, 4194889, 4194890, 4194891, 4194892, 4194894, 4194895, 4194896, 4194897, 4194899, 4194900, 4194901, 4194902, 4194903, 4194904, 4194905, 4194906, 4194907, 4194908, 4194909, 4194910, 4194911, 4194918, 4194919, 4194920, 4194921, 4194922, 4194923, 4194924, 4194925, 4194926, 4194927, 4194928, 4194929, 4194930, 4194931, 4194932, 4194933, 4194934, 4194935, 4194936, 4194937, 4194938, 4194939, 4194940, 4194941, 4194942, 4194943, 4194944, 4194945, 4194946, 4194947, 4194948, 4194949, 4194950, 4194951, 4194952, 4194953, 4194954, 4194955, 4194956, 4194957, 4194958, 4194959, 4194960, 4194961, 4194962, 4194963, 4194964, 4194965, 4194966, 4194967, 4194968, 4194969, 4194970, 4194971, 4194972, 4194973, 4194974, 4194975, 4194976, 4194977, 4194978, 4194979, 4194980, 4194981, 4194982, 4194983, 4194984, 4194985, 4194986, 4194987, 4194988, 4194989, 4194990, 4194991, 4194992, 4194993, 4194994, 4194995, 4194996, 4194997, 4195000, 4195001, 4195002, 4195003, 4195004, 4195006, 4195007, 4195008, 4195009, 4195010, 4195011, 4195012, 4195013, 4195014, 4195015, 4195016, 4195017, 4195018, 4195019, 4195020, 4195021, 4195022, 4195023, 4195024, 4195025, 4195026, 4195027, 4195028, 4195029, 4195030, 4195031, 4195032, 4195033, 4195034, 4195036, 4195037, 4195038, 4195039, 4195040, 4195041, 4195042, 4195043, 4195044, 4195045, 4195046, 4195047, 4195048, 4195049, 4195050, 4195051, 4195052, 4195053, 4195054, 4195055, 4195056, 4195057, 4195058, 4195059, 4195060, 4195061, 4195064, 4195065, 4195066, 4195067, 4195068, 4195069, 4195071, 4195072, 4195073), SingleValueConstraint(4195074, 4195075, 4195076, 4195077, 4195078, 4195080, 4195081, 4195082, 4195083, 4195084, 4195085, 4195086, 4195087, 4195088, 4195207, 4195208, 4195209, 4195213, 4195214, 4195215, 4195216, 4195217, 4195218, 4195220, 4195221, 4195222, 4195223, 4195224, 4195225, 4195226, 4195227, 4195228, 4195229, 4195230, 4195231, 4195232, 4195233, 4195234, 4195235, 4195236, 4195237, 4195238, 4195239, 4195242, 4195243, 4195244, 4195245, 4195246, 4195247, 4195248, 4195249, 4195250, 4195251, 4195252, 4195253, 4195254, 4195255, 4195256, 4195257, 4195258, 4195259, 4195260, 4195261, 4195262, 4195263, 4195264, 4195265, 4195266, 4195267, 4195268, 4195269, 4195270, 4195271, 4195272, 4195273, 4195274, 4195275, 4195276, 4195277, 4195278, 4195279, 4195281, 4195282, 4195283, 4195284, 4195285, 4195286, 4195287, 4195288, 4195289, 4195290, 4195291, 4195292, 4195293, 4195294, 4195295, 4195296, 4195297, 4195298, 4195299, 4195300, 4195301, 4195302, 4195303, 4195304, 4195305, 4195306, 4195307, 4195308, 4195309, 4195310, 4195311, 4195312, 4195313, 4195314, 4195315, 4195316, 4195317, 4195318, 4195319, 4195320, 4195321, 4195331, 4195332, 4195333, 4195334, 4195335, 4195336, 4195337, 4195338, 4195339, 4195340, 4195341, 4195342, 4195343, 4195344, 4195345, 4195346, 4195347, 4195348, 4195349, 4195350, 4195351, 4195352, 4195353, 4195354, 4195355, 4195356, 4195357, 4195358, 4195359, 4195360, 4195361, 4195362, 4195363, 4195364, 4195365, 4195366, 4195367, 4195368, 4195369, 4195370, 4195371, 4195372, 4195373, 4195374, 4195375, 4195376, 4195377, 4195378, 4195379, 4195380, 4195381, 4195382, 4195387, 4195388, 4195389, 4195390, 4195391, 4195392, 4195393, 4195394, 4195395, 4195396, 4195397, 4195398, 4195399, 4195400, 4195401, 4195402, 4195403, 4195404, 4195405, 4195406, 4195407, 4195408, 4195409, 4195410, 4195411, 4195412, 4195413, 4195414, 4195415, 4195416, 4195417, 4195418, 4195419, 4195460, 4195461, 4195462, 4195463, 4195464, 4195465, 4195466, 4195467, 4195468, 4195469, 4195470, 4195471, 4195472, 4195473, 4195474, 4195475, 4195476, 4195477, 4195478, 4195479, 4195480, 4195481, 4195482, 4195483, 4195484, 4195485, 4195486, 4195487, 4195488, 4195489, 4195490, 4195491, 4195492, 4195493, 4195494, 4195495, 4195496, 4195497, 4195498, 4195499, 4195500, 4195501, 4195502, 4195503, 4195504, 4195505, 4195506, 4195507), SingleValueConstraint(4195508, 4195509, 4195510, 4195511, 4195512, 4195513, 4195514, 4195515, 4195516, 4195517, 4195518, 4195519, 4195520, 4195521, 4195522, 4195523, 4195524, 4195525, 4195526, 4195527, 4195528, 4195529, 4195530, 4195531, 4195532, 4195533, 4195534, 4195535, 4195536, 4195537, 4195538, 4195539, 4195540, 4195541, 4195542, 4195543, 4195544, 4195545, 4195546, 4195547, 4195548, 4195549, 4195550, 4195551, 4195552, 4195553, 4195554, 4195555, 4195556, 4195557, 4195558, 4195559, 4195560, 4195561, 4195562, 4195563, 4195564, 4195565, 4195566, 4195567, 4195568, 4195571, 4195572, 4195573, 4195574, 4195575, 4195576, 4195577, 4195578, 4195579, 4195580, 4195581, 4195582, 4195583, 4195584, 4195585, 4195586, 4195587, 4195588, 4195592, 4195593, 4195594, 4195595, 4195596, 4195597, 4195598, 4195599, 4195601, 4195602, 4195603, 4195604, 4195605, 4195606, 4195607, 4195615, 4195616, 4195617, 4195655, 4195656, 4195660, 4195661, 4195662, 4195663, 4195664, 4195665, 4195666, 4195667, 4195669, 4195670, 4195671, 4195672, 4195673, 4195674, 4195698, 4195699, 4195700, 4195701, 4195702, 4195703, 4195704, 4195705, 4195706, 4195707, 4195708, 4195709, 4195710, 4195711, 4195712, 4195713, 4195714, 4195715, 4195716, 4195718, 4195721, 4195730, 4195731, 4195732, 4195733, 4195734, 4195735, 4195736, 4195737, 4195738, 4195739, 4195740, 4195741, 4195742, 4195743, 4195744, 4195745, 4195746, 4195747, 4195748, 4195749, 4195750, 4195751, 4195752, 4195753, 4195754, 4195755, 4195756, 4195757, 4195758, 4195759, 4195760, 4195761, 4195762, 4195763, 4195764, 4195765, 4195766, 4195767, 4195768, 4195769, 4195770, 4195771, 4195772, 4195773, 4195774, 4195775, 4195776, 4195777, 4195778, 4195779, 4195786, 4195787, 4195788, 4195789, 4195790, 4195791, 4195792, 4195793, 4195794, 4195795, 4195796, 4195797, 4195798, 4195799, 4195800, 4195801, 4195802, 4195803, 4195804, 4195807, 4195808, 4195809, 4195810, 4195811, 4195812, 4195813, 4195814, 4195815, 4195818, 4195819, 4195820, 4195821, 4195822, 4195823, 4195824, 4195825, 4195826, 4195827, 4195828, 4195829, 4195830, 4195831, 4195832, 4195833, 4195834, 4195835, 4195836, 4195837, 4195838, 4195839, 4195840, 4195841, 4195842, 4195843, 4195844, 4195845, 4195846, 4195847, 4195848, 4195849, 4195850, 4195851, 4195852, 4195853, 4195854, 4195855, 4195856, 4195857, 4195858, 4195859, 4195860), SingleValueConstraint(4195861, 4195862, 4195863, 4195864, 4195865, 4195866, 4195867, 4195868, 4195869, 4195870, 4195871, 4195872, 4195873, 4195874, 4195875, 4195876, 4195877, 4195880, 4195881, 4195882, 4195883, 4195884, 4195885, 4195886, 4195887, 4195888, 4195889, 4195890, 4195891, 4195892, 4195893, 4195894, 4195895, 4195896, 4195897, 4195898, 4195899, 4195900, 4195901, 4195902, 4195903, 4195904, 4195905, 4195906, 4195907, 4195908, 4195909, 4195910, 4195911, 4195912, 4195913, 4195914, 4195915, 4195916, 4195917, 4195918, 4195919, 4195920, 4195921, 4195922, 4195923, 4195924, 4195925, 4195926, 4195927, 4195928, 4195929, 4195930, 4195931, 4195932, 4195933, 4195934, 4195935, 4195936, 4195937, 4195938, 4195939, 4195940, 4195941, 4195942, 4195943, 4195944, 4195945, 4195946, 4195947, 4195948, 4195949, 4195950, 4195951, 4195952, 4195953, 4195956, 4195957, 4195958, 4195959, 4195960, 4195961, 4195962, 4195963, 4195964, 4195965, 4195966, 4195967, 4195968, 4195969, 4195970, 4195971, 4195972, 4195973, 4195976, 4195977, 4195978, 4195979, 4195980, 4195981, 4195982, 4195983, 4195984, 4195985, 4195986, 4195987, 4195988, 4195989, 4195991, 4195992, 4195993, 4195994, 4195995, 4195996, 4195997, 4195998, 4195999, 4196000, 4196001, 4196002, 4196003, 4196004, 4196005, 4196006, 4196007, 4196008, 4196009, 4196010, 4196011, 4196012, 4196013, 4196014, 4196015, 4196016, 4196017, 4196018, 4196019, 4196020, 4196021, 4196022, 4196023, 4196024, 4196025, 4196026, 4196027, 4196028, 4196029, 4196030, 4196031, 4196032, 4196033, 4196034, 4196035, 4196036, 4196041, 4196042, 4196045, 4196047, 4196048, 4196049, 4196051, 4196052, 4196055, 4196056, 4196060, 4196061, 4196062, 4196063, 4196065, 4196066, 4196067, 4196068, 4196069, 4196070, 4196071, 4196072, 4196073, 4196074, 4196075, 4196076, 4196077, 4196078, 4196079, 4196080, 4196081, 4196082, 4196083, 4196084, 4196085, 4196086, 4196087, 4196088, 4196089, 4196090, 4196091, 4196092, 4196093, 4196094, 4196095, 4196096, 4196097, 4196098, 4196099, 4196100, 4196101, 4196102, 4196103, 4196104, 4196105, 4196106, 4196107, 4196108, 4196109, 4196110, 4196111, 4196112, 4196113, 4196114, 4196115, 4196116, 4196117, 4196118, 4196119, 4196120, 4196121, 4196122, 4196123, 4196124, 4196125, 4196126, 4196127, 4196128, 4196129, 4196130, 4196131, 4196132, 4196133, 4196134, 4196135, 4196136), SingleValueConstraint(4196137, 4196138, 4196139, 4196140, 4196141, 4196142, 4196143, 4196144, 4196145, 4196146, 4196147, 4196149, 4196150, 4196151, 4196152, 4196153, 4196154, 4196155, 4196156, 4196157, 4196158, 4196159, 4196160, 4196161, 4196162, 4196163, 4196164, 4196165, 4196168, 4196169, 4196170, 4196171, 4196172, 4196173, 4196174, 4196175, 4196176, 4196177, 4196178, 4196179, 4196180, 4196181, 4196182, 4196183, 4196184, 4196185, 4196186, 4196187, 4196188, 4196189, 4196190, 4196191, 4196192, 4196193, 4196194, 4196195, 4196196, 4196197, 4196198, 4196199, 4196200, 4196201, 4196202, 4196203, 4196204, 4196205, 4196206, 4196207, 4196208, 4196209, 4196210, 4196211, 4196214, 4196215, 4196216, 4196217, 4196218, 4196219, 4196220, 4196221, 4196222, 4196223, 4196224, 4196225, 4196226, 4196227, 4196228, 4196229, 4196230, 4196231, 4196232, 4196233, 4196234, 4196235, 4196236, 4196237, 4196241, 4196242, 4196243, 4196244, 4196245, 4196246, 4196247, 4196249, 4196250, 4196251, 4196252, 4196253, 4196254, 4196255, 4196256, 4196257, 4196258, 4196259, 4196260, 4196261, 4196262, 4196263, 4196264, 4196265, 4196266, 4196267, 4196268, 4196269, 4196270, 4196271, 4196272, 4196273, 4196274, 4196275, 4196276, 4196277, 4196278, 4196279, 4196280, 4196281, 4196282, 4196283, 4196284, 4196285, 4196286, 4196287, 4196288, 4196289, 4196290, 4196291, 4196292, 4196293, 4196294, 4196295, 4196296, 4196297, 4196298, 4196299, 4196300, 4196301, 4196302, 4196303, 4196304, 4196305, 4196306, 4196307, 4196308, 4196309, 4196310, 4196317, 4196318, 4196319, 4196320, 4196321, 4196322, 4196323, 4196324, 4196325, 4196326, 4196327, 4196328, 4196329, 4196330, 4196331, 4196332, 4196333, 4196334, 4196335, 4196336, 4196337, 4196338, 4196339, 4196340, 4196341, 4196342, 4196343, 4196344, 4196345, 4196346, 4196347, 4196348, 4196349, 4196350, 4196354, 4196355, 4196356, 4196357, 4196358, 4196359, 4196360, 4196361, 4196362, 4196363, 4196364, 4196365, 4196366, 4196367, 4196368, 4196369, 4196370, 4196371, 4196372, 4196373, 4196374, 4196375, 4196376, 4196377, 4196378, 4196379, 4196380, 4196381, 4196382, 4196383, 4196384, 4196385, 4196386, 4196387, 4196388, 4196389, 4196390, 4196391, 4196392, 4196393, 4196394, 4196395, 4196396, 4196397, 4196398, 4196399, 4196400, 4196401, 4196402, 4196403, 4196404, 4196405, 4196406, 4196407, 4196408, 4196409), SingleValueConstraint(4196410, 4196411, 4196412, 4196413, 4196414, 4196415, 4196416, 4196417, 4196418, 4196419, 4196420, 4196421, 4196422, 4196423, 4196424, 4196425, 4196426, 4196427, 4196428, 4196429, 4196430, 4196431, 4196432, 4196433, 4196434, 4196435, 4196436, 4196437, 4196438, 4196439, 4196440, 4196441, 4196442, 4196443, 4196444, 4196445, 4196446, 4196447, 4196448, 4196449, 4196450, 4196451, 4196452, 4196453, 4196454, 4196455, 4196456, 4196457, 4196458, 4196459, 4196460, 4196461, 4196462, 4196463, 4196464, 4196465, 4196466, 4196467, 4196468, 4196469, 4196470, 4196471, 4196472, 4196474, 4196475, 4196477, 4196478, 4196480, 4196481, 4196483, 4196484, 4196485, 4196486, 4196487, 4196488, 4196489, 4196490, 4196491, 4196492, 4196493, 4196494, 4196495, 4196496, 4196497, 4196498, 4196499, 4196500, 4196501, 4196502, 4196503, 4196504, 4196505, 4196506, 4196507, 4196508, 4196509, 4196510, 4196511, 4196512, 4196513, 4196514, 4196515, 4196516, 4196517, 4196518, 4196519, 4196520, 4196521, 4196522, 4196523, 4196524, 4196525, 4196526, 4196527, 4196528, 4196529, 4196530, 4196531, 4196532, 4196533, 4196534, 4196535, 4196536, 4196537, 4196538, 4196539, 4196540, 4196541, 4196542, 4196543, 4196544, 4196545, 4196546, 4196555, 4196556, 4196557, 4196558, 4196559, 4196560, 4196561, 4196562, 4196563, 4196564, 4196565, 4196566, 4196567, 4196568, 4196569, 4196570, 4196571, 4196572, 4196573, 4196574, 4196575, 4196576, 4196577, 4196578, 4196579, 4196580, 4196581, 4196582, 4196583, 4196584, 4196585, 4196586, 4196587, 4196588, 4196589, 4196590, 4196591, 4196592, 4196593, 4196594, 4196595, 4196596, 4196597, 4196598, 4196599, 4196600, 4196601, 4196602, 4196603, 4196604, 4196605, 4196606, 4196607, 4196608, 4196609, 4196610, 4196611, 4196612, 4196613, 4196614, 4196619, 4196620, 4196621, 4196622, 4196623, 4196624, 4196625, 4196626, 4196627, 4196628, 4196629, 4196630, 4196631, 4196632, 4196633, 4196634, 4196635, 4196636, 4196637, 4196638, 4196639, 4196640, 4196641, 4196642, 4196643, 4196644, 4196645, 4196646, 4196647, 4196648, 4196649, 4196650, 4196651, 4196652, 4196653, 4196654, 4196655, 4196656, 4196657, 4196658, 4196659, 4196660, 4196661, 4196662, 4196663, 4196664, 4196665, 4196666, 4196667, 4196668, 4196669, 4196670, 4196671, 4196672, 4196673, 4196674, 4196675, 4196676, 4196677, 4196678, 4196679, 4196680), SingleValueConstraint(4196681, 4196682, 4196683, 4196684, 4196685, 4196686, 4196687, 4196688, 4196689, 4196690, 4196691, 4196692, 4196693, 4196694, 4196695, 4196696, 4196697, 4196698, 4196699, 4196700, 4196701, 4196702, 4196703, 4196704, 4196705, 4196706, 4196707, 4196708, 4196709, 4196710, 4196711, 4196712, 4196713, 4196714, 4196715, 4196716, 4196717, 4196718, 4196719, 4196720, 4196721, 4196722, 4196723, 4196724, 4196725, 4196726, 4196727, 4196728, 4196729, 4196730, 4196731, 4196732, 4196733, 4196734, 4196735, 4196736, 4196737, 4196738, 4196739, 4196740, 4196741, 4196742, 4196743, 4196744, 4196745, 4196746, 4196747, 4196748, 4196749, 4196750, 4196751, 4196752, 4196753, 4196754, 4196755, 4196756, 4196757, 4196758, 4196759, 4196760, 4196761, 4196762, 4196763, 4196764, 4196765, 4196766, 4196767, 4196768, 4196769, 4196770, 4196771, 4196772, 4196773, 4196774, 4196775, 4196776, 4196777, 4196778, 4196779, 4196780, 4196781, 4196785, 4196787, 4196788, 4196789, 4196790, 4196791, 4196792, 4196793, 4196794, 4196795, 4196796, 4196797, 4196798, 4196799, 4196800, 4196801, 4196802, 4196803, 4196804, 4196805, 4196806, 4196807, 4196808, 4196809, 4196810, 4196811, 4196812, 4196813, 4196814, 4196815, 4196816, 4196817, 4196818, 4196819, 4196820, 4196821, 4196822, 4196823, 4196824, 4196825, 4196826, 4196827, 4196828, 4196829, 4196830, 4196831, 4196832, 4196833, 4196834, 4196835, 4196836, 4196837, 4196838, 4196839, 4196840, 4196841, 4196842, 4196843, 4196844, 4196845, 4196846, 4196847, 4196848, 4196849, 4196850, 4196851, 4196852, 4196853, 4196854, 4196855, 4196856, 4196857, 4196858, 4196859, 4196860, 4196861, 4196862, 4196863, 4196864, 4196865, 4196866, 4196867, 4196868, 4196869, 4196870, 4196871, 4196872, 4196873, 4196874, 4196875, 4196876, 4196877, 4196878, 4196879, 4196880, 4196881, 4196882, 4196883, 4196884, 4196885, 4196886, 4196887, 4196888, 4196889, 4196890, 4196891, 4196892, 4196893, 4196894, 4196895, 4196896, 4196897, 4196898, 4196899, 4196900, 4196901, 4196902, 4196903, 4196904, 4196905, 4196906, 4196907, 4196908, 4196909, 4196910, 4196911, 4196912, 4196913, 4196914, 4196915, 4196916, 4196917, 4196918, 4196919, 4196920, 4196921, 4196922, 4196923, 4196924, 4196925, 4196926, 4196927, 4196928, 4196929, 4196930, 4196931, 4196932, 4196933, 4196934, 4196935, 4196936, 4196937, 4196938, 4196939), SingleValueConstraint(4196940, 4196941, 4196942, 4196943, 4196944, 4196945, 4196946, 4196947, 4196948, 4196949, 4196950, 4196951, 4196952, 4196953, 4196954, 4196955, 4196956, 4196957, 4196958, 4196959, 4196960, 4196961, 4196962, 4196963, 4196964, 4196965, 4196966, 4196967, 4196968, 4196969, 4196970, 4196971, 4196972, 4196973, 4196974, 4196975, 4196976, 4196977, 4196978, 4196979, 4196980, 4196981, 4196982, 4196983, 4196984, 4196985, 4196986, 4196987, 4196988, 4196989, 4196990, 4196991, 4196992, 4196993, 4196994, 4196995, 4196996, 4196997, 4196998, 4196999, 4197000, 4197001, 4197002, 4197003, 4197004, 4197005, 4197006, 4197007, 4197008, 4197009, 4197010, 4197011, 4197012, 4197013, 4197014, 4197015, 4197016, 4197017, 4197018, 4197019, 4197020, 4197021, 4197022, 4197023, 4197024, 4197025, 4197026, 4197027, 4197028, 4197029, 4197030, 4197031, 4197032, 4197033, 4197034, 4197035, 4197036, 4197037, 4197038, 4197039, 4197040, 4197041, 4197042, 4197043, 4197044, 4197045, 4197046, 4197047, 4197048, 4197049, 4197050, 4197051, 4197052, 4197053, 4197054, 4197055, 4197056, 4197057, 4197058, 4197059, 4197060, 4197061, 4197062, 4197063, 4197064, 4197065, 4197066, 4197067, 4197068, 4197069, 4197070, 4197071, 4197072, 4197073, 4197074, 4197075, 4197076, 4197077, 4197078, 4197079, 4197080, 4197081, 4197082, 4197083, 4197084, 4197085, 4197086, 4197087, 4197088, 4197089, 4197090, 4197091, 4197092, 4197093, 4522530, 4522532, 4522544, 4522556, 4522561, 4522588, 4522603, 4525234, 4525239, 4525240, 4525241, 4525247, 4525248, 4525250, 4525251, 4525252, 4525253, 4525254, 4526517, 4526850, 4526851, 4526901, 4526902, 4527601, 4528207, 4528209, 4528211, 4528216, 4528218, 4528220, 4528223, 4528225, 4528227, 4528268, 4528270, 4528591, 4528596, 4528842, 4529444, 4529447, 4529495, 4529514, 4529517, 4529520, 4529522, 4529524, 4529533, 4529601, 4529604, 4529606, 4529615, 4529722, 4529725, 4529838, 4529847, 4529849, 4529971, 4529973, 4530046, 4530050, 4530080, 4530082, 4530083, 4530085, 4530092, 4530095, 4530097, 4530098, 4530100, 4530106, 4530109, 4530111, 4530112, 4530113, 4530114, 4530115, 4530117, 4530119, 4530121, 4530122, 4530123, 4530125, 4530127, 4530139, 4530143, 4530166, 4530204, 4530206, 4530389, 4530391, 4530407, 4530451, 4530727, 4531275))
    namedValues = NamedValues(("generic", 0), ("f0156", 156), ("f0157", 157), ("f0169", 169), ("f0170", 170), ("f0174", 174), ("f0175", 175), ("f0176", 176), ("f0177", 177), ("f0178", 178), ("f0179", 179), ("f0180", 180), ("f0181", 181), ("f0182", 182), ("f0183", 183), ("f0184", 184), ("f0185", 185), ("f0186", 186), ("f0187", 187), ("f0188", 188), ("f0189", 189), ("f0190", 190), ("f0191", 191), ("f0200", 200), ("f0203", 203), ("f0206", 206), ("f0207", 207), ("f0209", 209), ("f0276", 276), ("f0277", 277), ("f0278", 278), ("f0279", 279), ("f0282", 282), ("f0283", 283), ("f0291", 291), ("f0293", 293), ("f0294", 294), ("f0304", 304), ("f0305", 305), ("f0306", 306), ("f0310", 310), ("f0311", 311), ("f0312", 312), ("f0313", 313), ("f0314", 314), ("f0315", 315), ("f0317", 317), ("f0318", 318), ("f0319", 319), ("f0320", 320), ("f0321", 321), ("f0322", 322), ("f0324", 324), ("f0326", 326), ("f0327", 327), ("f0329", 329), ("f0330", 330), ("f0331", 331), ("f0332", 332), ("f0334", 334), ("f0337", 337), ("f0367", 367), ("f0368", 368), ("f0369", 369), ("f0371", 371), ("f0373", 373), ("f0374", 374), ("f0376", 376), ("f0377", 377), ("f0378", 378), ("f0379", 379), ("f0380", 380), ("f0381", 381), ("f0382", 382), ("f0383", 383), ("f0384", 384), ("f0385", 385), ("f0387", 387), ("f0389", 389), ("f0391", 391), ("f0392", 392), ("f0393", 393), ("f0394", 394), ("f0395", 395), ("f0396", 396), ("f0397", 397), ("f0398", 398), ("f0399", 399), ("f0400", 400), ("f0401", 401), ("f0402", 402), ("f0403", 403), ("f0404", 404), ("f0405", 405), ("f0406", 406), ("f0407", 407), ("f0408", 408), ("f0409", 409), ("f0410", 410), ("f0411", 411), ("f0424", 424), ("f0425", 425), ("f0428", 428), ("f0429", 429), ("f0430", 430), ("f0434", 434), ("f0435", 435), ("f0436", 436), ("f0440", 440), ("f0451", 451), ("f0452", 452), ("f0453", 453), ("f0454", 454), ("f0455", 455), ("f0456", 456), ("f0458", 458), ("f0459", 459), ("f0460", 460), ("f0461", 461), ("f0462", 462), ("f0463", 463), ("f0464", 464), ("f0465", 465), ("f0466", 466), ("f0470", 470), ("f0471", 471), ("f0476", 476), ("f0478", 478), ("f0479", 479), ("f0480", 480), ("f0481", 481), ("f0484", 484), ("f0502", 502), ("f0517", 517), ("f0528", 528), ("f0531", 531), ("f0532", 532), ("f0533", 533), ("f0535", 535), ("f0536", 536), ("f0537", 537), ("f0538", 538), ("f0539", 539), ("f0540", 540), ("f0543", 543), ("f0549", 549), ("f0620", 620), ("f0621", 621), ("f0622", 622), ("f0625", 625), ("f0626", 626), ("f0635", 635), ("f0637", 637), ("f0640", 640), ("f0642", 642), ("f0643", 643), ("f0670", 670), ("f0671", 671), ("f0672", 672), ("f0673", 673), ("f0674", 674), ("f0675", 675), ("f0676", 676), ("f0677", 677), ("f0678", 678), ("f0688", 688), ("f0689", 689), ("f0702", 702), ("f0703", 703), ("f0708", 708), ("f0713", 713), ("f0717", 717), ("f0727", 727), ("f0728", 728), ("f0729", 729), ("f0730", 730), ("f0731", 731), ("f0733", 733), ("f0734", 734), ("f0735", 735), ("f0736", 736), ("f0740", 740), ("f0741", 741), ("f0742", 742), ("f0743", 743), ("f0744", 744), ("f0747", 747), ("f0757", 757), ("f0764", 764), ("f0765", 765), ("f0766", 766), ("f0772", 772), ("f0775", 775), ("f0776", 776), ("f0777", 777), ("f0778", 778), ("f0791", 791), ("f0792", 792), ("f0793", 793), ("f0794", 794), ("f0795", 795), ("f0796", 796), ("f0797", 797), ("f0798", 798), ("f0801", 801), ("f0807", 807), ("f0821", 821), ("f0826", 826), ("f0829", 829), ("f0831", 831), ("f0832", 832), ("f0833", 833), ("f0834", 834), ("f0835", 835), ("f0836", 836), ("f0837", 837), ("f0838", 838), ("f0840", 840), ("f0841", 841), ("f0842", 842), ("f0843", 843), ("f0844", 844), ("f0846", 846), ("f0855", 855), ("f0856", 856), ("f0857", 857), ("f0858", 858), ("f0859", 859), ("f0861", 861), ("f0862", 862), ("f0863", 863), ("f0864", 864), ("f0865", 865), ("f0866", 866), ("f0867", 867), ("f0868", 868), ("f0869", 869), ("f0872", 872), ("f0874", 874), ("f0875", 875), ("f0876", 876), ("f0877", 877), ("f0878", 878), ("f0879", 879), ("f0880", 880), ("f0881", 881), ("f0882", 882), ("f0883", 883), ("f0884", 884), ("f0885", 885), ("f0887", 887), ("f0890", 890), ("f0900", 900), ("f0901", 901), ("f0902", 902)) + NamedValues(("f0903", 903), ("f0909", 909), ("f0910", 910), ("f0915", 915), ("f0916", 916), ("f0917", 917), ("f0918", 918), ("f0919", 919), ("f0920", 920), ("f0921", 921), ("f0928", 928), ("f0932", 932), ("f0933", 933), ("f0934", 934), ("f0935", 935), ("f0936", 936), ("f0937", 937), ("f0943", 943), ("f0944", 944), ("f0945", 945), ("f0946", 946), ("f0947", 947), ("f0948", 948), ("f0949", 949), ("f0950", 950), ("f0951", 951), ("f0952", 952), ("f0953", 953), ("f0954", 954), ("f0957", 957), ("f0958", 958), ("f0959", 959), ("f0967", 967), ("f0968", 968), ("f0969", 969), ("f0970", 970), ("f0971", 971), ("f0972", 972), ("f0973", 973), ("f0974", 974), ("f0975", 975), ("f0976", 976), ("f0977", 977), ("f0978", 978), ("f0979", 979), ("f0980", 980), ("f0981", 981), ("f0982", 982), ("f0988", 988), ("f0996", 996), ("f0997", 997), ("f0998", 998), ("f0999", 999), ("f1000", 1000), ("f1001", 1001), ("f1002", 1002), ("f1003", 1003), ("f1004", 1004), ("f1005", 1005), ("f1006", 1006), ("f1007", 1007), ("f1008", 1008), ("f1009", 1009), ("f1010", 1010), ("f1017", 1017), ("f1026", 1026), ("f1027", 1027), ("f1028", 1028), ("f1029", 1029), ("f1030", 1030), ("f1031", 1031), ("f1032", 1032), ("f1033", 1033), ("f1034", 1034), ("f1035", 1035), ("f1036", 1036), ("f1037", 1037), ("f1040", 1040), ("f1046", 1046), ("f1047", 1047), ("f1048", 1048), ("f1049", 1049), ("f1050", 1050), ("f1051", 1051), ("f1052", 1052), ("f1053", 1053), ("f1054", 1054), ("f1055", 1055), ("f1056", 1056), ("f1057", 1057), ("f1058", 1058), ("f1080", 1080), ("f1081", 1081), ("f1082", 1082), ("f1083", 1083), ("f1084", 1084), ("f1085", 1085), ("f1086", 1086), ("f1087", 1087), ("f1088", 1088), ("f1089", 1089), ("f1090", 1090), ("f1091", 1091), ("f1092", 1092), ("f1093", 1093), ("f1094", 1094), ("f1095", 1095), ("f1097", 1097), ("f1098", 1098), ("f1099", 1099), ("f1101", 1101), ("f1102", 1102), ("f1103", 1103), ("f1104", 1104), ("f1105", 1105), ("f1106", 1106), ("f1114", 1114), ("f1202", 1202), ("f1204", 1204), ("f1205", 1205), ("f1206", 1206), ("f1207", 1207), ("f1208", 1208), ("f1209", 1209), ("f1216", 1216), ("f1219", 1219), ("f1220", 1220), ("f1221", 1221), ("f1222", 1222), ("f1223", 1223), ("f1224", 1224), ("f1225", 1225), ("f1226", 1226), ("f1227", 1227), ("f1228", 1228), ("f1229", 1229), ("f1232", 1232), ("f1233", 1233), ("f1237", 1237), ("f16405", 16405), ("f16406", 16406), ("f16407", 16407), ("f16408", 16408), ("f16518", 16518), ("f16519", 16519), ("f16520", 16520), ("f16533", 16533), ("f16534", 16534), ("f16535", 16535), ("f16539", 16539), ("f16550", 16550), ("f16576", 16576), ("f16577", 16577), ("f16579", 16579), ("f16580", 16580), ("f16581", 16581), ("f16582", 16582), ("f16600", 16600), ("f16601", 16601), ("f16604", 16604), ("f16605", 16605), ("f16606", 16606), ("f16634", 16634), ("f16635", 16635), ("f16636", 16636), ("f16637", 16637), ("f16641", 16641), ("f16650", 16650), ("f16651", 16651), ("f16653", 16653), ("f16654", 16654), ("f16655", 16655), ("f16656", 16656), ("f16657", 16657), ("f16670", 16670), ("f16673", 16673), ("f16674", 16674), ("f16679", 16679), ("f16680", 16680), ("f16681", 16681), ("f16682", 16682), ("f16683", 16683), ("f16684", 16684), ("f16742", 16742), ("f16745", 16745), ("f16749", 16749), ("f16750", 16750), ("f16803", 16803), ("f16815", 16815), ("f16823", 16823), ("f16852", 16852), ("f16857", 16857), ("f16858", 16858), ("f16879", 16879), ("f16880", 16880), ("f16881", 16881), ("f16898", 16898), ("f16904", 16904), ("f16906", 16906), ("f16930", 16930), ("f16931", 16931), ("f16942", 16942), ("f16943", 16943), ("f16944", 16944), ("f16945", 16945), ("f16973", 16973), ("f16974", 16974), ("f16975", 16975), ("f16976", 16976), ("f16977", 16977), ("f16978", 16978), ("f16979", 16979), ("f16980", 16980), ("f16981", 16981), ("f16982", 16982), ("f16983", 16983), ("f16984", 16984), ("f16986", 16986), ("f16987", 16987), ("f16988", 16988), ("f16994", 16994), ("f16995", 16995), ("f17000", 17000), ("f17001", 17001), ("f17002", 17002), ("f17008", 17008), ("f17012", 17012), ("f17013", 17013), ("f17014", 17014), ("f17043", 17043), ("f17044", 17044), ("f17045", 17045), ("f17046", 17046), ("f17050", 17050), ("f17051", 17051), ("f17052", 17052), ("f17053", 17053), ("f17083", 17083), ("f17084", 17084), ("f17089", 17089), ("f17116", 17116), ("f17133", 17133), ("f17134", 17134), ("f17163", 17163), ("f17169", 17169), ("f17170", 17170), ("f17187", 17187), ("f17188", 17188), ("f17190", 17190), ("f17192", 17192), ("f17195", 17195), ("f17196", 17196), ("f17207", 17207), ("f17214", 17214), ("f17223", 17223)) + NamedValues(("f17232", 17232), ("f17239", 17239), ("f17254", 17254), ("f17259", 17259), ("f17262", 17262), ("f17271", 17271), ("f17281", 17281), ("f17282", 17282), ("f17312", 17312), ("f17313", 17313), ("f17325", 17325), ("f17326", 17326), ("f17327", 17327), ("f17328", 17328), ("f17339", 17339), ("f17340", 17340), ("f17348", 17348), ("f17349", 17349), ("f17350", 17350), ("f17358", 17358), ("f17359", 17359), ("f17360", 17360), ("f17361", 17361), ("f17367", 17367), ("f17377", 17377), ("f17378", 17378), ("f17379", 17379), ("f17381", 17381), ("f17382", 17382), ("f17383", 17383), ("f17384", 17384), ("f17395", 17395), ("f17399", 17399), ("f17400", 17400), ("f17402", 17402), ("f17403", 17403), ("f17404", 17404), ("f17405", 17405), ("f17406", 17406), ("f17407", 17407), ("f17408", 17408), ("f17409", 17409), ("f17410", 17410), ("f17411", 17411), ("f17412", 17412), ("f17413", 17413), ("f17414", 17414), ("f17415", 17415), ("f17416", 17416), ("f17418", 17418), ("f17419", 17419), ("f17420", 17420), ("f17425", 17425), ("f17426", 17426), ("f17427", 17427), ("f17428", 17428), ("f17439", 17439), ("f17445", 17445), ("f17446", 17446), ("f17447", 17447), ("f17448", 17448), ("f17449", 17449), ("f17450", 17450), ("f17451", 17451), ("f17452", 17452), ("f17453", 17453), ("f17454", 17454), ("f17455", 17455), ("f17456", 17456), ("f17457", 17457), ("f17458", 17458), ("f17459", 17459), ("f17460", 17460), ("f17461", 17461), ("f17462", 17462), ("f17476", 17476), ("f17477", 17477), ("f17478", 17478), ("f17483", 17483), ("f17484", 17484), ("f17485", 17485), ("f17491", 17491), ("f17492", 17492), ("f17493", 17493), ("f17494", 17494), ("f17499", 17499), ("f17599", 17599), ("f17601", 17601), ("f17602", 17602), ("f33142", 33142), ("f33144", 33144), ("f33145", 33145), ("f33146", 33146), ("f33167", 33167), ("f33168", 33168), ("f33169", 33169), ("f33170", 33170), ("f33177", 33177), ("f33178", 33178), ("f33179", 33179), ("f33180", 33180), ("f33187", 33187), ("f33188", 33188), ("f33189", 33189), ("f33190", 33190), ("f33197", 33197), ("f33198", 33198), ("f33199", 33199), ("f33200", 33200), ("f33211", 33211), ("f33212", 33212), ("f33213", 33213), ("f33214", 33214), ("f33221", 33221), ("f33222", 33222), ("f33223", 33223), ("f33224", 33224), ("f33231", 33231), ("f33232", 33232), ("f33233", 33233), ("f33234", 33234), ("f33241", 33241), ("f33242", 33242), ("f33243", 33243), ("f33244", 33244), ("f33251", 33251), ("f33252", 33252), ("f33253", 33253), ("f33254", 33254), ("f33261", 33261), ("f33262", 33262), ("f33263", 33263), ("f33264", 33264), ("f33271", 33271), ("f33272", 33272), ("f33273", 33273), ("f33274", 33274), ("f33281", 33281), ("f33282", 33282), ("f33283", 33283), ("f33284", 33284), ("f33291", 33291), ("f33292", 33292), ("f33293", 33293), ("f33294", 33294), ("f33301", 33301), ("f33302", 33302), ("f33303", 33303), ("f33304", 33304), ("f33483", 33483), ("f33485", 33485), ("f33486", 33486), ("f33487", 33487), ("f33491", 33491), ("f33493", 33493), ("f33494", 33494), ("f33495", 33495), ("f33499", 33499), ("f33501", 33501), ("f33502", 33502), ("f33503", 33503), ("f33720", 33720), ("f33721", 33721), ("f33722", 33722), ("f33723", 33723), ("f33730", 33730), ("f33731", 33731), ("f33732", 33732), ("f33733", 33733), ("f33740", 33740), ("f33741", 33741), ("f33742", 33742), ("f33743", 33743), ("f33750", 33750), ("f33751", 33751), ("f33752", 33752), ("f33753", 33753), ("f33760", 33760), ("f33761", 33761), ("f33762", 33762), ("f33763", 33763), ("f33770", 33770), ("f33771", 33771), ("f33772", 33772), ("f33773", 33773), ("f33810", 33810), ("f33811", 33811), ("f33812", 33812), ("f33813", 33813), ("f33820", 33820), ("f33821", 33821), ("f33822", 33822), ("f33823", 33823), ("f33830", 33830), ("f33831", 33831), ("f33832", 33832), ("f33833", 33833), ("f33840", 33840), ("f33841", 33841), ("f33842", 33842), ("f33843", 33843), ("f33850", 33850), ("f33851", 33851), ("f33852", 33852), ("f33853", 33853), ("f33860", 33860), ("f33861", 33861), ("f33862", 33862), ("f33863", 33863), ("f33875", 33875), ("f33876", 33876), ("f33877", 33877), ("f33878", 33878), ("f33885", 33885), ("f33886", 33886), ("f33887", 33887), ("f33888", 33888), ("f33895", 33895), ("f33896", 33896), ("f33897", 33897), ("f33898", 33898), ("f33905", 33905), ("f33906", 33906), ("f33907", 33907), ("f33908", 33908), ("f33915", 33915), ("f33916", 33916), ("f33917", 33917), ("f33918", 33918), ("f33925", 33925), ("f33926", 33926), ("f33927", 33927), ("f33928", 33928), ("f33940", 33940), ("f33941", 33941), ("f33942", 33942), ("f33943", 33943), ("f33950", 33950), ("f33951", 33951), ("f33952", 33952), ("f33953", 33953), ("f33960", 33960), ("f33961", 33961), ("f33962", 33962), ("f33963", 33963), ("f33970", 33970), ("f33971", 33971), ("f33972", 33972), ("f33973", 33973), ("f33980", 33980), ("f33981", 33981), ("f33982", 33982), ("f33983", 33983), ("f33995", 33995), ("f33996", 33996)) + NamedValues(("f33997", 33997), ("f33998", 33998), ("f34005", 34005), ("f34006", 34006), ("f34007", 34007), ("f34008", 34008), ("f34015", 34015), ("f34016", 34016), ("f34017", 34017), ("f34018", 34018), ("f34030", 34030), ("f34031", 34031), ("f34032", 34032), ("f34033", 34033), ("f34040", 34040), ("f34041", 34041), ("f34042", 34042), ("f34043", 34043), ("f34050", 34050), ("f34051", 34051), ("f34052", 34052), ("f34053", 34053), ("f34064", 34064), ("f34065", 34065), ("f34066", 34066), ("f34067", 34067), ("f34074", 34074), ("f34075", 34075), ("f34076", 34076), ("f34077", 34077), ("f34084", 34084), ("f34085", 34085), ("f34086", 34086), ("f34087", 34087), ("f34094", 34094), ("f34095", 34095), ("f34096", 34096), ("f34097", 34097), ("f34108", 34108), ("f34109", 34109), ("f34110", 34110), ("f34111", 34111), ("f34118", 34118), ("f34119", 34119), ("f34120", 34120), ("f34121", 34121), ("f34128", 34128), ("f34129", 34129), ("f34130", 34130), ("f34131", 34131), ("f34138", 34138), ("f34139", 34139), ("f34140", 34140), ("f34141", 34141), ("f34148", 34148), ("f34149", 34149), ("f34150", 34150), ("f34151", 34151), ("f34158", 34158), ("f34159", 34159), ("f34160", 34160), ("f34161", 34161), ("f34168", 34168), ("f34169", 34169), ("f34170", 34170), ("f34171", 34171), ("f34178", 34178), ("f34179", 34179), ("f34180", 34180), ("f34181", 34181), ("f34192", 34192), ("f34193", 34193), ("f34194", 34194), ("f34195", 34195), ("f34202", 34202), ("f34203", 34203), ("f34204", 34204), ("f34205", 34205), ("f34212", 34212), ("f34213", 34213), ("f34214", 34214), ("f34215", 34215), ("f34222", 34222), ("f34223", 34223), ("f34224", 34224), ("f34225", 34225), ("f34232", 34232), ("f34233", 34233), ("f34234", 34234), ("f34235", 34235), ("f34246", 34246), ("f34247", 34247), ("f34248", 34248), ("f34249", 34249), ("f34256", 34256), ("f34257", 34257), ("f34258", 34258), ("f34259", 34259), ("f34271", 34271), ("f34272", 34272), ("f34273", 34273), ("f34274", 34274), ("f34281", 34281), ("f34282", 34282), ("f34283", 34283), ("f34284", 34284), ("f34291", 34291), ("f34292", 34292), ("f34293", 34293), ("f34294", 34294), ("f34301", 34301), ("f34302", 34302), ("f34303", 34303), ("f34304", 34304), ("f34316", 34316), ("f34317", 34317), ("f34318", 34318), ("f34319", 34319), ("f34326", 34326), ("f34327", 34327), ("f34328", 34328), ("f34329", 34329), ("f34336", 34336), ("f34337", 34337), ("f34338", 34338), ("f34339", 34339), ("f34346", 34346), ("f34347", 34347), ("f34348", 34348), ("f34349", 34349), ("f34361", 34361), ("f34362", 34362), ("f34363", 34363), ("f34364", 34364), ("f34371", 34371), ("f34372", 34372), ("f34373", 34373), ("f34374", 34374), ("f34381", 34381), ("f34382", 34382), ("f34383", 34383), ("f34384", 34384), ("f34396", 34396), ("f34397", 34397), ("f34398", 34398), ("f34399", 34399), ("f34406", 34406), ("f34407", 34407), ("f34408", 34408), ("f34409", 34409), ("f34416", 34416), ("f34417", 34417), ("f34418", 34418), ("f34419", 34419), ("f34426", 34426), ("f34427", 34427), ("f34428", 34428), ("f34429", 34429), ("f34436", 34436), ("f34437", 34437), ("f34438", 34438), ("f34439", 34439), ("f34451", 34451), ("f34452", 34452), ("f34453", 34453), ("f34454", 34454), ("f34461", 34461), ("f34462", 34462), ("f34463", 34463), ("f34464", 34464), ("f34471", 34471), ("f34472", 34472), ("f34473", 34473), ("f34474", 34474), ("f34481", 34481), ("f34482", 34482), ("f34483", 34483), ("f34484", 34484), ("f34496", 34496), ("f34497", 34497), ("f34498", 34498), ("f34499", 34499), ("f34506", 34506), ("f34507", 34507), ("f34508", 34508), ("f34509", 34509), ("f34516", 34516), ("f34517", 34517), ("f34518", 34518), ("f34519", 34519), ("f34526", 34526), ("f34527", 34527), ("f34528", 34528), ("f34529", 34529), ("f34542", 34542), ("f34543", 34543), ("f34544", 34544), ("f34545", 34545), ("f34552", 34552), ("f34553", 34553), ("f34554", 34554), ("f34555", 34555), ("f34562", 34562), ("f34563", 34563), ("f34564", 34564), ("f34565", 34565), ("f34572", 34572), ("f34573", 34573), ("f34574", 34574), ("f34575", 34575), ("f34588", 34588), ("f34589", 34589), ("f34590", 34590), ("f34591", 34591), ("f34598", 34598), ("f34599", 34599), ("f34600", 34600), ("f34601", 34601), ("f34608", 34608), ("f34609", 34609), ("f34610", 34610), ("f34611", 34611), ("f34618", 34618), ("f34619", 34619), ("f34620", 34620), ("f34621", 34621), ("f34633", 34633), ("f34634", 34634), ("f34635", 34635), ("f34636", 34636), ("f34643", 34643), ("f34644", 34644), ("f34645", 34645), ("f34646", 34646), ("f34653", 34653), ("f34654", 34654), ("f34655", 34655), ("f34656", 34656), ("f34663", 34663), ("f34664", 34664), ("f34665", 34665), ("f34666", 34666), ("f34673", 34673), ("f34674", 34674), ("f34675", 34675), ("f34676", 34676), ("f34688", 34688), ("f34689", 34689), ("f34690", 34690), ("f34691", 34691), ("f34698", 34698), ("f34699", 34699), ("f34700", 34700), ("f34701", 34701), ("f34708", 34708)) + NamedValues(("f34709", 34709), ("f34710", 34710), ("f34711", 34711), ("f34718", 34718), ("f34719", 34719), ("f34720", 34720), ("f34721", 34721), ("f34733", 34733), ("f34734", 34734), ("f34735", 34735), ("f34736", 34736), ("f34743", 34743), ("f34744", 34744), ("f34745", 34745), ("f34746", 34746), ("f34753", 34753), ("f34754", 34754), ("f34755", 34755), ("f34756", 34756), ("f34763", 34763), ("f34764", 34764), ("f34765", 34765), ("f34766", 34766), ("f34778", 34778), ("f34779", 34779), ("f34780", 34780), ("f34781", 34781), ("f34788", 34788), ("f34789", 34789), ("f34790", 34790), ("f34791", 34791), ("f34798", 34798), ("f34799", 34799), ("f34800", 34800), ("f34801", 34801), ("f34808", 34808), ("f34809", 34809), ("f34810", 34810), ("f34811", 34811), ("f34822", 34822), ("f34823", 34823), ("f34824", 34824), ("f34825", 34825), ("f34832", 34832), ("f34833", 34833), ("f34834", 34834), ("f34835", 34835), ("f34842", 34842), ("f34843", 34843), ("f34844", 34844), ("f34845", 34845), ("f34852", 34852), ("f34853", 34853), ("f34854", 34854), ("f34855", 34855), ("f34862", 34862), ("f34863", 34863), ("f34864", 34864), ("f34865", 34865), ("f34872", 34872), ("f34873", 34873), ("f34874", 34874), ("f34875", 34875), ("f34882", 34882), ("f34883", 34883), ("f34884", 34884), ("f34885", 34885), ("f34892", 34892), ("f34893", 34893), ("f34894", 34894), ("f34895", 34895), ("f34906", 34906), ("f34907", 34907), ("f34908", 34908), ("f34909", 34909), ("f34916", 34916), ("f34917", 34917), ("f34918", 34918), ("f34919", 34919), ("f34926", 34926), ("f34927", 34927), ("f34928", 34928), ("f34929", 34929), ("f34936", 34936), ("f34937", 34937), ("f34938", 34938), ("f34939", 34939), ("f34950", 34950), ("f34951", 34951), ("f34952", 34952), ("f34953", 34953), ("f34960", 34960), ("f34961", 34961), ("f34962", 34962), ("f34963", 34963), ("f34970", 34970), ("f34971", 34971), ("f34972", 34972), ("f34973", 34973), ("f34980", 34980), ("f34981", 34981), ("f34982", 34982), ("f34983", 34983), ("f34990", 34990), ("f34991", 34991), ("f34992", 34992), ("f34993", 34993), ("f35000", 35000), ("f35001", 35001), ("f35002", 35002), ("f35003", 35003), ("f35010", 35010), ("f35011", 35011), ("f35012", 35012), ("f35013", 35013), ("f35020", 35020), ("f35021", 35021), ("f35022", 35022), ("f35023", 35023), ("f35166", 35166), ("f35168", 35168), ("f35169", 35169), ("f35170", 35170), ("f35174", 35174), ("f35176", 35176), ("f35177", 35177), ("f35178", 35178), ("f35198", 35198), ("f35200", 35200), ("f35201", 35201), ("f35202", 35202), ("f35206", 35206), ("f35208", 35208), ("f35209", 35209), ("f35210", 35210), ("f35214", 35214), ("f35216", 35216), ("f35217", 35217), ("f35218", 35218), ("f35222", 35222), ("f35224", 35224), ("f35225", 35225), ("f35226", 35226), ("f35234", 35234), ("f35236", 35236), ("f35237", 35237), ("f35238", 35238), ("f35242", 35242), ("f35244", 35244), ("f35245", 35245), ("f35246", 35246), ("f35250", 35250), ("f35252", 35252), ("f35253", 35253), ("f35254", 35254), ("f35275", 35275), ("f35276", 35276), ("f35277", 35277), ("f35278", 35278), ("f35285", 35285), ("f35286", 35286), ("f35287", 35287), ("f35288", 35288), ("f35295", 35295), ("f35296", 35296), ("f35297", 35297), ("f35298", 35298), ("f35305", 35305), ("f35306", 35306), ("f35307", 35307), ("f35308", 35308), ("f35315", 35315), ("f35316", 35316), ("f35317", 35317), ("f35318", 35318), ("f35329", 35329), ("f35330", 35330), ("f35331", 35331), ("f35332", 35332), ("f35339", 35339), ("f35340", 35340), ("f35341", 35341), ("f35342", 35342), ("f35349", 35349), ("f35350", 35350), ("f35351", 35351), ("f35352", 35352), ("f35359", 35359), ("f35360", 35360), ("f35361", 35361), ("f35362", 35362), ("f35369", 35369), ("f35370", 35370), ("f35371", 35371), ("f35372", 35372), ("f35379", 35379), ("f35380", 35380), ("f35381", 35381), ("f35382", 35382), ("f35962", 35962), ("f35964", 35964), ("f35965", 35965), ("f35966", 35966), ("f35974", 35974), ("f35976", 35976), ("f35977", 35977), ("f35978", 35978), ("f36234", 36234), ("f36236", 36236), ("f36237", 36237), ("f36238", 36238), ("f36242", 36242), ("f36244", 36244), ("f36245", 36245), ("f36246", 36246), ("f36266", 36266), ("f36268", 36268), ("f36269", 36269), ("f36270", 36270), ("f36274", 36274), ("f36276", 36276), ("f36277", 36277), ("f36278", 36278), ("f36282", 36282), ("f36284", 36284), ("f36285", 36285), ("f36286", 36286), ("f36294", 36294), ("f36296", 36296), ("f36297", 36297), ("f36298", 36298), ("f36302", 36302), ("f36304", 36304), ("f36305", 36305), ("f36306", 36306), ("f36310", 36310), ("f36312", 36312), ("f36313", 36313), ("f36314", 36314), ("f36323", 36323), ("f36325", 36325), ("f36326", 36326), ("f36327", 36327), ("f36335", 36335), ("f36337", 36337), ("f36338", 36338), ("f36339", 36339), ("f37154", 37154), ("f37156", 37156), ("f37157", 37157), ("f37158", 37158), ("f37162", 37162), ("f37164", 37164), ("f37165", 37165), ("f37166", 37166)) + NamedValues(("f37170", 37170), ("f37172", 37172), ("f37173", 37173), ("f37174", 37174), ("f37269", 37269), ("f37271", 37271), ("f37272", 37272), ("f37273", 37273), ("f37313", 37313), ("f37314", 37314), ("f37315", 37315), ("f37316", 37316), ("f37323", 37323), ("f37324", 37324), ("f37325", 37325), ("f37326", 37326), ("f37333", 37333), ("f37334", 37334), ("f37335", 37335), ("f37336", 37336), ("f37343", 37343), ("f37344", 37344), ("f37345", 37345), ("f37346", 37346), ("f37353", 37353), ("f37354", 37354), ("f37355", 37355), ("f37356", 37356), ("f37363", 37363), ("f37364", 37364), ("f37365", 37365), ("f37366", 37366), ("f37383", 37383), ("f37384", 37384), ("f37385", 37385), ("f37386", 37386), ("f37393", 37393), ("f37394", 37394), ("f37395", 37395), ("f37396", 37396), ("f37403", 37403), ("f37404", 37404), ("f37405", 37405), ("f37406", 37406), ("f37413", 37413), ("f37414", 37414), ("f37415", 37415), ("f37416", 37416), ("f37423", 37423), ("f37424", 37424), ("f37425", 37425), ("f37426", 37426), ("f37443", 37443), ("f37444", 37444), ("f37445", 37445), ("f37446", 37446), ("f37453", 37453), ("f37454", 37454), ("f37455", 37455), ("f37456", 37456), ("f37463", 37463), ("f37464", 37464), ("f37465", 37465), ("f37466", 37466), ("f37473", 37473), ("f37474", 37474), ("f37475", 37475), ("f37476", 37476), ("f37485", 37485), ("f37486", 37486), ("f37487", 37487), ("f37488", 37488), ("f37495", 37495), ("f37496", 37496), ("f37497", 37497), ("f37498", 37498), ("f37505", 37505), ("f37506", 37506), ("f37507", 37507), ("f37508", 37508), ("f37532", 37532), ("f37533", 37533), ("f37534", 37534), ("f37535", 37535), ("f37543", 37543), ("f37544", 37544), ("f37545", 37545), ("f37546", 37546), ("f37553", 37553), ("f37554", 37554), ("f37555", 37555), ("f37556", 37556), ("f37564", 37564), ("f37566", 37566), ("f37567", 37567), ("f37568", 37568), ("f37572", 37572), ("f37574", 37574), ("f37575", 37575), ("f37576", 37576), ("f37580", 37580), ("f37582", 37582), ("f37583", 37583), ("f37584", 37584), ("f37600", 37600), ("f37602", 37602), ("f37603", 37603), ("f37604", 37604), ("f37610", 37610), ("f37612", 37612), ("f37613", 37613), ("f37614", 37614), ("f37771", 37771), ("f37773", 37773), ("f37774", 37774), ("f37775", 37775), ("f37779", 37779), ("f37781", 37781), ("f37782", 37782), ("f37783", 37783), ("f38022", 38022), ("f38032", 38032), ("f38044", 38044), ("f38054", 38054), ("f38064", 38064), ("f38086", 38086), ("f38096", 38096), ("f38106", 38106), ("f38128", 38128), ("f38138", 38138), ("f38148", 38148), ("f38158", 38158), ("f38311", 38311), ("f38313", 38313), ("f38314", 38314), ("f38315", 38315), ("f38349", 38349), ("f38351", 38351), ("f38352", 38352), ("f38353", 38353), ("f38357", 38357), ("f38359", 38359), ("f38360", 38360), ("f38361", 38361), ("f38408", 38408), ("f38409", 38409), ("f38410", 38410), ("f38411", 38411), ("f38438", 38438), ("f38440", 38440), ("f38441", 38441), ("f38442", 38442), ("f38451", 38451), ("f38453", 38453), ("f38454", 38454), ("f38455", 38455), ("f38779", 38779), ("f38788", 38788), ("f38797", 38797), ("f38806", 38806), ("f38815", 38815), ("f38829", 38829), ("f38838", 38838), ("f38847", 38847), ("f38856", 38856), ("f38909", 38909), ("f39032", 39032), ("f39034", 39034), ("f39035", 39035), ("f39036", 39036), ("f39040", 39040), ("f39042", 39042), ("f39043", 39043), ("f39044", 39044), ("f39240", 39240), ("f39242", 39242), ("f39243", 39243), ("f39244", 39244), ("f39421", 39421), ("f39423", 39423), ("f39424", 39424), ("f39425", 39425), ("f39429", 39429), ("f39431", 39431), ("f39432", 39432), ("f39433", 39433), ("f39437", 39437), ("f39439", 39439), ("f39440", 39440), ("f39441", 39441), ("f39445", 39445), ("f39447", 39447), ("f39448", 39448), ("f39449", 39449), ("f39453", 39453), ("f39455", 39455), ("f39456", 39456), ("f39457", 39457), ("f39464", 39464), ("f39466", 39466), ("f39467", 39467), ("f39468", 39468), ("f39472", 39472), ("f39474", 39474), ("f39475", 39475), ("f39476", 39476), ("f39480", 39480), ("f39482", 39482), ("f39483", 39483), ("f39484", 39484), ("f39488", 39488), ("f39490", 39490), ("f39491", 39491), ("f39492", 39492), ("f39498", 39498), ("f39500", 39500), ("f39501", 39501), ("f39502", 39502), ("f39506", 39506), ("f39508", 39508), ("f39509", 39509), ("f39510", 39510), ("f39514", 39514), ("f39516", 39516), ("f39517", 39517), ("f39518", 39518), ("f39525", 39525), ("f39527", 39527), ("f39528", 39528), ("f39529", 39529), ("f39533", 39533), ("f39535", 39535), ("f39536", 39536), ("f39537", 39537), ("f39541", 39541), ("f39543", 39543), ("f39544", 39544), ("f39545", 39545), ("f39549", 39549), ("f39551", 39551), ("f39552", 39552), ("f39553", 39553), ("f39557", 39557), ("f39559", 39559), ("f39560", 39560), ("f39561", 39561), ("f39565", 39565), ("f39567", 39567), ("f39568", 39568), ("f39569", 39569), ("f39575", 39575), ("f39577", 39577), ("f39578", 39578), ("f39579", 39579), ("f40092", 40092)) + NamedValues(("f40094", 40094), ("f40095", 40095), ("f40096", 40096), ("f40100", 40100), ("f40102", 40102), ("f40103", 40103), ("f40104", 40104), ("f40108", 40108), ("f40110", 40110), ("f40111", 40111), ("f40112", 40112), ("f40116", 40116), ("f40118", 40118), ("f40119", 40119), ("f40120", 40120), ("f40124", 40124), ("f40126", 40126), ("f40127", 40127), ("f40128", 40128), ("f40441", 40441), ("f40443", 40443), ("f40444", 40444), ("f40445", 40445), ("f40449", 40449), ("f40451", 40451), ("f40452", 40452), ("f40453", 40453), ("f40457", 40457), ("f40459", 40459), ("f40460", 40460), ("f40461", 40461), ("f40547", 40547), ("f40549", 40549), ("f40550", 40550), ("f40551", 40551), ("f40555", 40555), ("f40557", 40557), ("f40558", 40558), ("f40559", 40559), ("f40563", 40563), ("f40565", 40565), ("f40566", 40566), ("f40567", 40567), ("f40574", 40574), ("f40576", 40576), ("f40577", 40577), ("f40578", 40578), ("f40582", 40582), ("f40583", 40583), ("f40584", 40584), ("f40585", 40585), ("f40586", 40586), ("f40587", 40587), ("f40591", 40591), ("f40593", 40593), ("f40594", 40594), ("f40595", 40595), ("f40967", 40967), ("f40969", 40969), ("f40970", 40970), ("f40971", 40971), ("f40975", 40975), ("f40978", 40978), ("f40979", 40979), ("f40980", 40980), ("f40984", 40984), ("f40986", 40986), ("f40987", 40987), ("f40988", 40988), ("f41016", 41016), ("f41018", 41018), ("f41019", 41019), ("f41020", 41020), ("f41024", 41024), ("f41026", 41026), ("f41027", 41027), ("f41028", 41028), ("f41032", 41032), ("f41034", 41034), ("f41035", 41035), ("f41036", 41036), ("f41049", 41049), ("f41050", 41050), ("f41051", 41051), ("f41052", 41052), ("f41059", 41059), ("f41060", 41060), ("f41061", 41061), ("f41062", 41062), ("f41069", 41069), ("f41070", 41070), ("f41071", 41071), ("f41072", 41072), ("f41079", 41079), ("f41080", 41080), ("f41081", 41081), ("f41082", 41082), ("f41089", 41089), ("f41090", 41090), ("f41091", 41091), ("f41092", 41092), ("f41099", 41099), ("f41100", 41100), ("f41101", 41101), ("f41102", 41102), ("f41109", 41109), ("f41110", 41110), ("f41111", 41111), ("f41112", 41112), ("f41119", 41119), ("f41120", 41120), ("f41121", 41121), ("f41122", 41122), ("f41199", 41199), ("f41201", 41201), ("f41202", 41202), ("f41203", 41203), ("f41207", 41207), ("f41209", 41209), ("f41210", 41210), ("f41211", 41211), ("f41215", 41215), ("f41217", 41217), ("f41218", 41218), ("f41219", 41219), ("f41289", 41289), ("f41290", 41290), ("f41291", 41291), ("f41292", 41292), ("f41299", 41299), ("f41300", 41300), ("f41301", 41301), ("f41302", 41302), ("f41309", 41309), ("f41310", 41310), ("f41311", 41311), ("f41312", 41312), ("f41319", 41319), ("f41320", 41320), ("f41321", 41321), ("f41322", 41322), ("f41329", 41329), ("f41330", 41330), ("f41331", 41331), ("f41332", 41332), ("f41339", 41339), ("f41340", 41340), ("f41341", 41341), ("f41342", 41342), ("f41349", 41349), ("f41350", 41350), ("f41351", 41351), ("f41352", 41352), ("f41359", 41359), ("f41360", 41360), ("f41361", 41361), ("f41362", 41362), ("f41443", 41443), ("f41444", 41444), ("f41445", 41445), ("f41446", 41446), ("f41453", 41453), ("f41454", 41454), ("f41455", 41455), ("f41456", 41456), ("f41463", 41463), ("f41464", 41464), ("f41465", 41465), ("f41466", 41466), ("f41473", 41473), ("f41474", 41474), ("f41475", 41475), ("f41476", 41476), ("f41483", 41483), ("f41484", 41484), ("f41485", 41485), ("f41486", 41486), ("f41493", 41493), ("f41494", 41494), ("f41495", 41495), ("f41496", 41496), ("f41503", 41503), ("f41504", 41504), ("f41505", 41505), ("f41506", 41506), ("f41513", 41513), ("f41514", 41514), ("f41515", 41515), ("f41516", 41516), ("f77845", 77845), ("f77846", 77846), ("f77847", 77847), ("f77848", 77848), ("f77958", 77958), ("f77959", 77959), ("f77960", 77960), ("f77973", 77973), ("f77974", 77974), ("f77975", 77975), ("f77979", 77979), ("f77990", 77990), ("f78016", 78016), ("f78017", 78017), ("f78019", 78019), ("f78020", 78020), ("f78021", 78021), ("f78022", 78022), ("f78040", 78040), ("f78041", 78041), ("f78044", 78044), ("f78045", 78045), ("f78046", 78046), ("f78074", 78074), ("f78075", 78075), ("f78076", 78076), ("f78077", 78077), ("f78081", 78081), ("f78090", 78090), ("f78091", 78091), ("f78093", 78093), ("f78094", 78094), ("f78095", 78095), ("f78096", 78096), ("f78097", 78097), ("f78110", 78110), ("f78113", 78113), ("f78114", 78114), ("f78119", 78119), ("f78120", 78120), ("f78121", 78121), ("f78122", 78122), ("f78123", 78123), ("f78124", 78124), ("f78182", 78182), ("f78185", 78185), ("f78189", 78189), ("f78190", 78190), ("f78243", 78243), ("f78255", 78255), ("f78263", 78263), ("f78292", 78292), ("f78297", 78297), ("f78298", 78298), ("f78319", 78319), ("f78320", 78320), ("f78321", 78321), ("f78338", 78338), ("f78344", 78344), ("f78346", 78346), ("f78370", 78370), ("f78371", 78371), ("f78382", 78382), ("f78383", 78383), ("f78384", 78384), ("f78385", 78385)) + NamedValues(("f78413", 78413), ("f78414", 78414), ("f78415", 78415), ("f78416", 78416), ("f78417", 78417), ("f78418", 78418), ("f78419", 78419), ("f78420", 78420), ("f78421", 78421), ("f78422", 78422), ("f78423", 78423), ("f78424", 78424), ("f78426", 78426), ("f78427", 78427), ("f78428", 78428), ("f78434", 78434), ("f78435", 78435), ("f78440", 78440), ("f78441", 78441), ("f78442", 78442), ("f78448", 78448), ("f78452", 78452), ("f78453", 78453), ("f78454", 78454), ("f78483", 78483), ("f78484", 78484), ("f78485", 78485), ("f78486", 78486), ("f78490", 78490), ("f78491", 78491), ("f78492", 78492), ("f78493", 78493), ("f78523", 78523), ("f78524", 78524), ("f78529", 78529), ("f78556", 78556), ("f78573", 78573), ("f78574", 78574), ("f78603", 78603), ("f78609", 78609), ("f78610", 78610), ("f78627", 78627), ("f78628", 78628), ("f78630", 78630), ("f78632", 78632), ("f78635", 78635), ("f78636", 78636), ("f78647", 78647), ("f78654", 78654), ("f78663", 78663), ("f78672", 78672), ("f78679", 78679), ("f78694", 78694), ("f78699", 78699), ("f78702", 78702), ("f78711", 78711), ("f78721", 78721), ("f78722", 78722), ("f78752", 78752), ("f78753", 78753), ("f78765", 78765), ("f78766", 78766), ("f78767", 78767), ("f78768", 78768), ("f78779", 78779), ("f78780", 78780), ("f78788", 78788), ("f78789", 78789), ("f78790", 78790), ("f78798", 78798), ("f78799", 78799), ("f78800", 78800), ("f78801", 78801), ("f78807", 78807), ("f78817", 78817), ("f78818", 78818), ("f78819", 78819), ("f78821", 78821), ("f78822", 78822), ("f78823", 78823), ("f78824", 78824), ("f78835", 78835), ("f78839", 78839), ("f78840", 78840), ("f78842", 78842), ("f78843", 78843), ("f78844", 78844), ("f78845", 78845), ("f78846", 78846), ("f78847", 78847), ("f78848", 78848), ("f78849", 78849), ("f78850", 78850), ("f78851", 78851), ("f78852", 78852), ("f78853", 78853), ("f78854", 78854), ("f78855", 78855), ("f78856", 78856), ("f78858", 78858), ("f78859", 78859), ("f78860", 78860), ("f78865", 78865), ("f78866", 78866), ("f78867", 78867), ("f78868", 78868), ("f78879", 78879), ("f78885", 78885), ("f78886", 78886), ("f78887", 78887), ("f78888", 78888), ("f78889", 78889), ("f78890", 78890), ("f78891", 78891), ("f78892", 78892), ("f78893", 78893), ("f78894", 78894), ("f78895", 78895), ("f78896", 78896), ("f78897", 78897), ("f78898", 78898), ("f78899", 78899), ("f78900", 78900), ("f78901", 78901), ("f78902", 78902), ("f78916", 78916), ("f78917", 78917), ("f78918", 78918), ("f78923", 78923), ("f78924", 78924), ("f78925", 78925), ("f78931", 78931), ("f78932", 78932), ("f78933", 78933), ("f78934", 78934), ("f78939", 78939), ("f79039", 79039), ("f79041", 79041), ("f79042", 79042), ("f999445", 999445), ("f999446", 999446), ("f999447", 999447), ("f999448", 999448), ("f999558", 999558), ("f999559", 999559), ("f999560", 999560), ("f999573", 999573), ("f999574", 999574), ("f999575", 999575), ("f999579", 999579), ("f999590", 999590), ("f999616", 999616), ("f999617", 999617), ("f999619", 999619), ("f999620", 999620), ("f999621", 999621), ("f999622", 999622), ("f999640", 999640), ("f999641", 999641), ("f999644", 999644), ("f999645", 999645), ("f999646", 999646), ("f999674", 999674), ("f999675", 999675), ("f999676", 999676), ("f999677", 999677), ("f999681", 999681), ("f999690", 999690), ("f999691", 999691), ("f999693", 999693), ("f999694", 999694), ("f999695", 999695), ("f999696", 999696), ("f999697", 999697), ("f999710", 999710), ("f999713", 999713), ("f999714", 999714), ("f999719", 999719), ("f999720", 999720), ("f999721", 999721), ("f999722", 999722), ("f999723", 999723), ("f999724", 999724), ("f999782", 999782), ("f999785", 999785), ("f999789", 999789), ("f999790", 999790), ("f999843", 999843), ("f999855", 999855), ("f999863", 999863), ("f999892", 999892), ("f999897", 999897), ("f999898", 999898), ("f999919", 999919), ("f999920", 999920), ("f999921", 999921), ("f999938", 999938), ("f999944", 999944), ("f999946", 999946), ("f999970", 999970), ("f999971", 999971), ("f999982", 999982), ("f999983", 999983), ("f999984", 999984), ("f999985", 999985), ("f1000013", 1000013), ("f1000014", 1000014), ("f1000015", 1000015), ("f1000016", 1000016), ("f1000017", 1000017), ("f1000018", 1000018), ("f1000019", 1000019), ("f1000020", 1000020), ("f1000021", 1000021), ("f1000022", 1000022), ("f1000023", 1000023), ("f1000024", 1000024), ("f1000026", 1000026), ("f1000027", 1000027), ("f1000028", 1000028), ("f1000034", 1000034), ("f1000035", 1000035), ("f1000040", 1000040), ("f1000041", 1000041), ("f1000042", 1000042), ("f1000048", 1000048), ("f1000052", 1000052), ("f1000053", 1000053), ("f1000054", 1000054), ("f1000083", 1000083), ("f1000084", 1000084), ("f1000085", 1000085), ("f1000086", 1000086), ("f1000090", 1000090), ("f1000091", 1000091), ("f1000092", 1000092), ("f1000093", 1000093), ("f1000123", 1000123), ("f1000124", 1000124), ("f1000129", 1000129), ("f1000156", 1000156), ("f1000173", 1000173), ("f1000174", 1000174), ("f1000203", 1000203), ("f1000209", 1000209), ("f1000210", 1000210), ("f1000227", 1000227), ("f1000228", 1000228), ("f1000230", 1000230), ("f1000232", 1000232), ("f1000235", 1000235), ("f1000236", 1000236), ("f1000247", 1000247), ("f1000254", 1000254), ("f1000263", 1000263)) + NamedValues(("f1000272", 1000272), ("f1000279", 1000279), ("f1000294", 1000294), ("f1000299", 1000299), ("f1000302", 1000302), ("f1000311", 1000311), ("f1000321", 1000321), ("f1000322", 1000322), ("f1000352", 1000352), ("f1000353", 1000353), ("f1000365", 1000365), ("f1000366", 1000366), ("f1000367", 1000367), ("f1000368", 1000368), ("f1000379", 1000379), ("f1000380", 1000380), ("f1000388", 1000388), ("f1000389", 1000389), ("f1000390", 1000390), ("f1000398", 1000398), ("f1000399", 1000399), ("f1000400", 1000400), ("f1000401", 1000401), ("f1000407", 1000407), ("f1000417", 1000417), ("f1000418", 1000418), ("f1000419", 1000419), ("f1000421", 1000421), ("f1000422", 1000422), ("f1000423", 1000423), ("f1000424", 1000424), ("f1000435", 1000435), ("f1000439", 1000439), ("f1000440", 1000440), ("f1000442", 1000442), ("f1000443", 1000443), ("f1000444", 1000444), ("f1000445", 1000445), ("f1000446", 1000446), ("f1000447", 1000447), ("f1000448", 1000448), ("f1000449", 1000449), ("f1000450", 1000450), ("f1000451", 1000451), ("f1000452", 1000452), ("f1000453", 1000453), ("f1000454", 1000454), ("f1000455", 1000455), ("f1000456", 1000456), ("f1000458", 1000458), ("f1000459", 1000459), ("f1000460", 1000460), ("f1000465", 1000465), ("f1000466", 1000466), ("f1000467", 1000467), ("f1000468", 1000468), ("f1000479", 1000479), ("f1000485", 1000485), ("f1000486", 1000486), ("f1000487", 1000487), ("f1000488", 1000488), ("f1000489", 1000489), ("f1000490", 1000490), ("f1000491", 1000491), ("f1000492", 1000492), ("f1000493", 1000493), ("f1000494", 1000494), ("f1000495", 1000495), ("f1000496", 1000496), ("f1000497", 1000497), ("f1000498", 1000498), ("f1000499", 1000499), ("f1000500", 1000500), ("f1000501", 1000501), ("f1000502", 1000502), ("f1000516", 1000516), ("f1000517", 1000517), ("f1000518", 1000518), ("f1000523", 1000523), ("f1000524", 1000524), ("f1000525", 1000525), ("f1000531", 1000531), ("f1000532", 1000532), ("f1000533", 1000533), ("f1000534", 1000534), ("f1000539", 1000539), ("f1000639", 1000639), ("f1000641", 1000641), ("f1000642", 1000642), ("e4194528", 4194528), ("e4194529", 4194529), ("e4194530", 4194530), ("e4194531", 4194531), ("e4194532", 4194532), ("e4194533", 4194533), ("e4194534", 4194534), ("e4194535", 4194535), ("e4194536", 4194536), ("e4194537", 4194537), ("e4194538", 4194538), ("e4194539", 4194539), ("e4194540", 4194540), ("e4194541", 4194541), ("e4194542", 4194542), ("e4194543", 4194543), ("e4194544", 4194544), ("e4194545", 4194545), ("e4194546", 4194546), ("e4194547", 4194547), ("e4194548", 4194548), ("e4194549", 4194549), ("e4194550", 4194550), ("e4194551", 4194551), ("e4194552", 4194552), ("e4194553", 4194553), ("e4194554", 4194554), ("e4194555", 4194555), ("e4194556", 4194556), ("e4194557", 4194557), ("e4194558", 4194558), ("e4194559", 4194559), ("e4194560", 4194560), ("e4194561", 4194561), ("e4194562", 4194562), ("e4194563", 4194563), ("e4194564", 4194564), ("e4194565", 4194565), ("e4194566", 4194566), ("e4194567", 4194567), ("e4194568", 4194568), ("e4194569", 4194569), ("e4194570", 4194570), ("e4194571", 4194571), ("e4194572", 4194572), ("e4194573", 4194573), ("e4194574", 4194574), ("e4194575", 4194575), ("e4194576", 4194576), ("e4194577", 4194577), ("e4194578", 4194578), ("e4194579", 4194579), ("e4194580", 4194580), ("e4194581", 4194581), ("e4194582", 4194582), ("e4194583", 4194583), ("e4194584", 4194584), ("e4194585", 4194585), ("e4194586", 4194586), ("e4194587", 4194587), ("e4194591", 4194591), ("e4194592", 4194592), ("e4194593", 4194593), ("e4194594", 4194594), ("e4194595", 4194595), ("e4194596", 4194596), ("e4194597", 4194597), ("e4194598", 4194598), ("e4194599", 4194599), ("e4194600", 4194600), ("e4194601", 4194601), ("e4194602", 4194602), ("e4194603", 4194603), ("e4194604", 4194604), ("e4194605", 4194605), ("e4194607", 4194607), ("e4194608", 4194608), ("e4194609", 4194609), ("e4194610", 4194610), ("e4194611", 4194611), ("e4194612", 4194612), ("e4194613", 4194613), ("e4194614", 4194614), ("e4194615", 4194615), ("e4194616", 4194616), ("e4194617", 4194617), ("e4194620", 4194620), ("e4194621", 4194621), ("e4194622", 4194622), ("e4194623", 4194623), ("e4194624", 4194624), ("e4194626", 4194626), ("e4194627", 4194627), ("e4194628", 4194628), ("e4194629", 4194629), ("e4194630", 4194630), ("e4194631", 4194631), ("e4194632", 4194632), ("e4194652", 4194652), ("e4194654", 4194654), ("e4194655", 4194655), ("e4194656", 4194656), ("e4194657", 4194657), ("e4194658", 4194658), ("e4194659", 4194659), ("e4194660", 4194660), ("e4194661", 4194661), ("e4194662", 4194662), ("e4194663", 4194663), ("e4194664", 4194664), ("e4194665", 4194665), ("e4194671", 4194671), ("e4194672", 4194672), ("e4194673", 4194673), ("e4194674", 4194674), ("e4194675", 4194675), ("e4194676", 4194676), ("e4194683", 4194683), ("e4194684", 4194684), ("e4194685", 4194685), ("e4194686", 4194686), ("e4194687", 4194687), ("e4194688", 4194688), ("e4194689", 4194689), ("e4194693", 4194693), ("e4194694", 4194694), ("e4194695", 4194695), ("e4194697", 4194697), ("e4194698", 4194698), ("e4194699", 4194699), ("e4194700", 4194700), ("e4194701", 4194701), ("e4194702", 4194702), ("e4194703", 4194703), ("e4194704", 4194704), ("e4194705", 4194705), ("e4194706", 4194706), ("e4194714", 4194714), ("e4194715", 4194715), ("e4194717", 4194717), ("e4194718", 4194718), ("e4194719", 4194719), ("e4194720", 4194720), ("e4194721", 4194721), ("e4194722", 4194722), ("e4194723", 4194723), ("e4194724", 4194724), ("e4194725", 4194725), ("e4194726", 4194726), ("e4194727", 4194727), ("e4194728", 4194728), ("e4194729", 4194729), ("e4194730", 4194730), ("e4194734", 4194734), ("e4194736", 4194736), ("e4194737", 4194737), ("e4194738", 4194738), ("e4194739", 4194739), ("e4194740", 4194740), ("e4194741", 4194741), ("e4194744", 4194744), ("e4194745", 4194745), ("e4194746", 4194746), ("e4194747", 4194747), ("e4194748", 4194748), ("e4194749", 4194749)) + NamedValues(("e4194750", 4194750), ("e4194751", 4194751), ("e4194752", 4194752), ("e4194753", 4194753), ("e4194754", 4194754), ("e4194755", 4194755), ("e4194763", 4194763), ("e4194764", 4194764), ("e4194765", 4194765), ("e4194766", 4194766), ("e4194767", 4194767), ("e4194768", 4194768), ("e4194769", 4194769), ("e4194770", 4194770), ("e4194771", 4194771), ("e4194773", 4194773), ("e4194774", 4194774), ("e4194775", 4194775), ("e4194776", 4194776), ("e4194777", 4194777), ("e4194778", 4194778), ("e4194787", 4194787), ("e4194788", 4194788), ("e4194789", 4194789), ("e4194790", 4194790), ("e4194791", 4194791), ("e4194792", 4194792), ("e4194793", 4194793), ("e4194794", 4194794), ("e4194795", 4194795), ("e4194796", 4194796), ("e4194797", 4194797), ("e4194798", 4194798), ("e4194799", 4194799), ("e4194800", 4194800), ("e4194801", 4194801), ("e4194802", 4194802), ("e4194803", 4194803), ("e4194804", 4194804), ("e4194805", 4194805), ("e4194806", 4194806), ("e4194807", 4194807), ("e4194812", 4194812), ("e4194828", 4194828), ("e4194830", 4194830), ("e4194831", 4194831), ("e4194832", 4194832), ("e4194833", 4194833), ("e4194834", 4194834), ("e4194835", 4194835), ("e4194836", 4194836), ("e4194839", 4194839), ("e4194840", 4194840), ("e4194841", 4194841), ("e4194842", 4194842), ("e4194843", 4194843), ("e4194844", 4194844), ("e4194847", 4194847), ("e4194848", 4194848), ("e4194849", 4194849), ("e4194855", 4194855), ("e4194856", 4194856), ("e4194859", 4194859), ("e4194860", 4194860), ("e4194861", 4194861), ("e4194862", 4194862), ("e4194863", 4194863), ("e4194864", 4194864), ("e4194865", 4194865), ("e4194866", 4194866), ("e4194867", 4194867), ("e4194868", 4194868), ("e4194869", 4194869), ("e4194871", 4194871), ("e4194876", 4194876), ("e4194878", 4194878), ("e4194879", 4194879), ("e4194880", 4194880), ("e4194881", 4194881), ("e4194883", 4194883), ("e4194884", 4194884), ("e4194885", 4194885), ("e4194886", 4194886), ("e4194887", 4194887), ("e4194888", 4194888), ("e4194889", 4194889), ("e4194890", 4194890), ("e4194891", 4194891), ("e4194892", 4194892), ("e4194894", 4194894), ("e4194895", 4194895), ("e4194896", 4194896), ("e4194897", 4194897), ("e4194899", 4194899), ("e4194900", 4194900), ("e4194901", 4194901), ("e4194902", 4194902), ("e4194903", 4194903), ("e4194904", 4194904), ("e4194905", 4194905), ("e4194906", 4194906), ("e4194907", 4194907), ("e4194908", 4194908), ("e4194909", 4194909), ("e4194910", 4194910), ("e4194911", 4194911), ("e4194918", 4194918), ("e4194919", 4194919), ("e4194920", 4194920), ("e4194921", 4194921), ("e4194922", 4194922), ("e4194923", 4194923), ("e4194924", 4194924), ("e4194925", 4194925), ("e4194926", 4194926), ("e4194927", 4194927), ("e4194928", 4194928), ("e4194929", 4194929), ("e4194930", 4194930), ("e4194931", 4194931), ("e4194932", 4194932), ("e4194933", 4194933), ("e4194934", 4194934), ("e4194935", 4194935), ("e4194936", 4194936), ("e4194937", 4194937), ("e4194938", 4194938), ("e4194939", 4194939), ("e4194940", 4194940), ("e4194941", 4194941), ("e4194942", 4194942), ("e4194943", 4194943), ("e4194944", 4194944), ("e4194945", 4194945), ("e4194946", 4194946), ("e4194947", 4194947), ("e4194948", 4194948), ("e4194949", 4194949), ("e4194950", 4194950), ("e4194951", 4194951), ("e4194952", 4194952), ("e4194953", 4194953), ("e4194954", 4194954), ("e4194955", 4194955), ("e4194956", 4194956), ("e4194957", 4194957), ("e4194958", 4194958), ("e4194959", 4194959), ("e4194960", 4194960), ("e4194961", 4194961), ("e4194962", 4194962), ("e4194963", 4194963), ("e4194964", 4194964), ("e4194965", 4194965), ("e4194966", 4194966), ("e4194967", 4194967), ("e4194968", 4194968), ("e4194969", 4194969), ("e4194970", 4194970), ("e4194971", 4194971), ("e4194972", 4194972), ("e4194973", 4194973), ("e4194974", 4194974), ("e4194975", 4194975), ("e4194976", 4194976), ("e4194977", 4194977), ("e4194978", 4194978), ("e4194979", 4194979), ("e4194980", 4194980), ("e4194981", 4194981), ("e4194982", 4194982), ("e4194983", 4194983), ("e4194984", 4194984), ("e4194985", 4194985), ("e4194986", 4194986), ("e4194987", 4194987), ("e4194988", 4194988), ("e4194989", 4194989), ("e4194990", 4194990), ("e4194991", 4194991), ("e4194992", 4194992), ("e4194993", 4194993), ("e4194994", 4194994), ("e4194995", 4194995), ("e4194996", 4194996), ("e4194997", 4194997), ("e4195000", 4195000), ("e4195001", 4195001), ("e4195002", 4195002), ("e4195003", 4195003), ("e4195004", 4195004), ("e4195006", 4195006), ("e4195007", 4195007), ("e4195008", 4195008), ("e4195009", 4195009), ("e4195010", 4195010), ("e4195011", 4195011), ("e4195012", 4195012), ("e4195013", 4195013), ("e4195014", 4195014), ("e4195015", 4195015), ("e4195016", 4195016), ("e4195017", 4195017), ("e4195018", 4195018), ("e4195019", 4195019), ("e4195020", 4195020), ("e4195021", 4195021), ("e4195022", 4195022), ("e4195023", 4195023), ("e4195024", 4195024), ("e4195025", 4195025), ("e4195026", 4195026), ("e4195027", 4195027), ("e4195028", 4195028), ("e4195029", 4195029), ("e4195030", 4195030), ("e4195031", 4195031), ("e4195032", 4195032), ("e4195033", 4195033), ("e4195034", 4195034), ("e4195036", 4195036), ("e4195037", 4195037), ("e4195038", 4195038), ("e4195039", 4195039), ("e4195040", 4195040), ("e4195041", 4195041), ("e4195042", 4195042), ("e4195043", 4195043), ("e4195044", 4195044), ("e4195045", 4195045), ("e4195046", 4195046), ("e4195047", 4195047), ("e4195048", 4195048), ("e4195049", 4195049), ("e4195050", 4195050), ("e4195051", 4195051), ("e4195052", 4195052), ("e4195053", 4195053), ("e4195054", 4195054), ("e4195055", 4195055), ("e4195056", 4195056), ("e4195057", 4195057), ("e4195058", 4195058), ("e4195059", 4195059), ("e4195060", 4195060), ("e4195061", 4195061), ("e4195064", 4195064), ("e4195065", 4195065), ("e4195066", 4195066), ("e4195067", 4195067), ("e4195068", 4195068), ("e4195069", 4195069), ("e4195071", 4195071), ("e4195072", 4195072), ("e4195073", 4195073)) + NamedValues(("e4195074", 4195074), ("e4195075", 4195075), ("e4195076", 4195076), ("e4195077", 4195077), ("e4195078", 4195078), ("e4195080", 4195080), ("e4195081", 4195081), ("e4195082", 4195082), ("e4195083", 4195083), ("e4195084", 4195084), ("e4195085", 4195085), ("e4195086", 4195086), ("e4195087", 4195087), ("e4195088", 4195088), ("e4195207", 4195207), ("e4195208", 4195208), ("e4195209", 4195209), ("e4195213", 4195213), ("e4195214", 4195214), ("e4195215", 4195215), ("e4195216", 4195216), ("e4195217", 4195217), ("e4195218", 4195218), ("e4195220", 4195220), ("e4195221", 4195221), ("e4195222", 4195222), ("e4195223", 4195223), ("e4195224", 4195224), ("e4195225", 4195225), ("e4195226", 4195226), ("e4195227", 4195227), ("e4195228", 4195228), ("e4195229", 4195229), ("e4195230", 4195230), ("e4195231", 4195231), ("e4195232", 4195232), ("e4195233", 4195233), ("e4195234", 4195234), ("e4195235", 4195235), ("e4195236", 4195236), ("e4195237", 4195237), ("e4195238", 4195238), ("e4195239", 4195239), ("e4195242", 4195242), ("e4195243", 4195243), ("e4195244", 4195244), ("e4195245", 4195245), ("e4195246", 4195246), ("e4195247", 4195247), ("e4195248", 4195248), ("e4195249", 4195249), ("e4195250", 4195250), ("e4195251", 4195251), ("e4195252", 4195252), ("e4195253", 4195253), ("e4195254", 4195254), ("e4195255", 4195255), ("e4195256", 4195256), ("e4195257", 4195257), ("e4195258", 4195258), ("e4195259", 4195259), ("e4195260", 4195260), ("e4195261", 4195261), ("e4195262", 4195262), ("e4195263", 4195263), ("e4195264", 4195264), ("e4195265", 4195265), ("e4195266", 4195266), ("e4195267", 4195267), ("e4195268", 4195268), ("e4195269", 4195269), ("e4195270", 4195270), ("e4195271", 4195271), ("e4195272", 4195272), ("e4195273", 4195273), ("e4195274", 4195274), ("e4195275", 4195275), ("e4195276", 4195276), ("e4195277", 4195277), ("e4195278", 4195278), ("e4195279", 4195279), ("e4195281", 4195281), ("e4195282", 4195282), ("e4195283", 4195283), ("e4195284", 4195284), ("e4195285", 4195285), ("e4195286", 4195286), ("e4195287", 4195287), ("e4195288", 4195288), ("e4195289", 4195289), ("e4195290", 4195290), ("e4195291", 4195291), ("e4195292", 4195292), ("e4195293", 4195293), ("e4195294", 4195294), ("e4195295", 4195295), ("e4195296", 4195296), ("e4195297", 4195297), ("e4195298", 4195298), ("e4195299", 4195299), ("e4195300", 4195300), ("e4195301", 4195301), ("e4195302", 4195302), ("e4195303", 4195303), ("e4195304", 4195304), ("e4195305", 4195305), ("e4195306", 4195306), ("e4195307", 4195307), ("e4195308", 4195308), ("e4195309", 4195309), ("e4195310", 4195310), ("e4195311", 4195311), ("e4195312", 4195312), ("e4195313", 4195313), ("e4195314", 4195314), ("e4195315", 4195315), ("e4195316", 4195316), ("e4195317", 4195317), ("e4195318", 4195318), ("e4195319", 4195319), ("e4195320", 4195320), ("e4195321", 4195321), ("e4195331", 4195331), ("e4195332", 4195332), ("e4195333", 4195333), ("e4195334", 4195334), ("e4195335", 4195335), ("e4195336", 4195336), ("e4195337", 4195337), ("e4195338", 4195338), ("e4195339", 4195339), ("e4195340", 4195340), ("e4195341", 4195341), ("e4195342", 4195342), ("e4195343", 4195343), ("e4195344", 4195344), ("e4195345", 4195345), ("e4195346", 4195346), ("e4195347", 4195347), ("e4195348", 4195348), ("e4195349", 4195349), ("e4195350", 4195350), ("e4195351", 4195351), ("e4195352", 4195352), ("e4195353", 4195353), ("e4195354", 4195354), ("e4195355", 4195355), ("e4195356", 4195356), ("e4195357", 4195357), ("e4195358", 4195358), ("e4195359", 4195359), ("e4195360", 4195360), ("e4195361", 4195361), ("e4195362", 4195362), ("e4195363", 4195363), ("e4195364", 4195364), ("e4195365", 4195365), ("e4195366", 4195366), ("e4195367", 4195367), ("e4195368", 4195368), ("e4195369", 4195369), ("e4195370", 4195370), ("e4195371", 4195371), ("e4195372", 4195372), ("e4195373", 4195373), ("e4195374", 4195374), ("e4195375", 4195375), ("e4195376", 4195376), ("e4195377", 4195377), ("e4195378", 4195378), ("e4195379", 4195379), ("e4195380", 4195380), ("e4195381", 4195381), ("e4195382", 4195382), ("e4195387", 4195387), ("e4195388", 4195388), ("e4195389", 4195389), ("e4195390", 4195390), ("e4195391", 4195391), ("e4195392", 4195392), ("e4195393", 4195393), ("e4195394", 4195394), ("e4195395", 4195395), ("e4195396", 4195396), ("e4195397", 4195397), ("e4195398", 4195398), ("e4195399", 4195399), ("e4195400", 4195400), ("e4195401", 4195401), ("e4195402", 4195402), ("e4195403", 4195403), ("e4195404", 4195404), ("e4195405", 4195405), ("e4195406", 4195406), ("e4195407", 4195407), ("e4195408", 4195408), ("e4195409", 4195409), ("e4195410", 4195410), ("e4195411", 4195411), ("e4195412", 4195412), ("e4195413", 4195413), ("e4195414", 4195414), ("e4195415", 4195415), ("e4195416", 4195416), ("e4195417", 4195417), ("e4195418", 4195418), ("e4195419", 4195419), ("e4195460", 4195460), ("e4195461", 4195461), ("e4195462", 4195462), ("e4195463", 4195463), ("e4195464", 4195464), ("e4195465", 4195465), ("e4195466", 4195466), ("e4195467", 4195467), ("e4195468", 4195468), ("e4195469", 4195469), ("e4195470", 4195470), ("e4195471", 4195471), ("e4195472", 4195472), ("e4195473", 4195473), ("e4195474", 4195474), ("e4195475", 4195475), ("e4195476", 4195476), ("e4195477", 4195477), ("e4195478", 4195478), ("e4195479", 4195479), ("e4195480", 4195480), ("e4195481", 4195481), ("e4195482", 4195482), ("e4195483", 4195483), ("e4195484", 4195484), ("e4195485", 4195485), ("e4195486", 4195486), ("e4195487", 4195487), ("e4195488", 4195488), ("e4195489", 4195489), ("e4195490", 4195490), ("e4195491", 4195491), ("e4195492", 4195492), ("e4195493", 4195493), ("e4195494", 4195494), ("e4195495", 4195495), ("e4195496", 4195496), ("e4195497", 4195497), ("e4195498", 4195498), ("e4195499", 4195499), ("e4195500", 4195500), ("e4195501", 4195501), ("e4195502", 4195502), ("e4195503", 4195503), ("e4195504", 4195504), ("e4195505", 4195505), ("e4195506", 4195506), ("e4195507", 4195507)) + NamedValues(("e4195508", 4195508), ("e4195509", 4195509), ("e4195510", 4195510), ("e4195511", 4195511), ("e4195512", 4195512), ("e4195513", 4195513), ("e4195514", 4195514), ("e4195515", 4195515), ("e4195516", 4195516), ("e4195517", 4195517), ("e4195518", 4195518), ("e4195519", 4195519), ("e4195520", 4195520), ("e4195521", 4195521), ("e4195522", 4195522), ("e4195523", 4195523), ("e4195524", 4195524), ("e4195525", 4195525), ("e4195526", 4195526), ("e4195527", 4195527), ("e4195528", 4195528), ("e4195529", 4195529), ("e4195530", 4195530), ("e4195531", 4195531), ("e4195532", 4195532), ("e4195533", 4195533), ("e4195534", 4195534), ("e4195535", 4195535), ("e4195536", 4195536), ("e4195537", 4195537), ("e4195538", 4195538), ("e4195539", 4195539), ("e4195540", 4195540), ("e4195541", 4195541), ("e4195542", 4195542), ("e4195543", 4195543), ("e4195544", 4195544), ("e4195545", 4195545), ("e4195546", 4195546), ("e4195547", 4195547), ("e4195548", 4195548), ("e4195549", 4195549), ("e4195550", 4195550), ("e4195551", 4195551), ("e4195552", 4195552), ("e4195553", 4195553), ("e4195554", 4195554), ("e4195555", 4195555), ("e4195556", 4195556), ("e4195557", 4195557), ("e4195558", 4195558), ("e4195559", 4195559), ("e4195560", 4195560), ("e4195561", 4195561), ("e4195562", 4195562), ("e4195563", 4195563), ("e4195564", 4195564), ("e4195565", 4195565), ("e4195566", 4195566), ("e4195567", 4195567), ("e4195568", 4195568), ("e4195571", 4195571), ("e4195572", 4195572), ("e4195573", 4195573), ("e4195574", 4195574), ("e4195575", 4195575), ("e4195576", 4195576), ("e4195577", 4195577), ("e4195578", 4195578), ("e4195579", 4195579), ("e4195580", 4195580), ("e4195581", 4195581), ("e4195582", 4195582), ("e4195583", 4195583), ("e4195584", 4195584), ("e4195585", 4195585), ("e4195586", 4195586), ("e4195587", 4195587), ("e4195588", 4195588), ("e4195592", 4195592), ("e4195593", 4195593), ("e4195594", 4195594), ("e4195595", 4195595), ("e4195596", 4195596), ("e4195597", 4195597), ("e4195598", 4195598), ("e4195599", 4195599), ("e4195601", 4195601), ("e4195602", 4195602), ("e4195603", 4195603), ("e4195604", 4195604), ("e4195605", 4195605), ("e4195606", 4195606), ("e4195607", 4195607), ("e4195615", 4195615), ("e4195616", 4195616), ("e4195617", 4195617), ("e4195655", 4195655), ("e4195656", 4195656), ("e4195660", 4195660), ("e4195661", 4195661), ("e4195662", 4195662), ("e4195663", 4195663), ("e4195664", 4195664), ("e4195665", 4195665), ("e4195666", 4195666), ("e4195667", 4195667), ("e4195669", 4195669), ("e4195670", 4195670), ("e4195671", 4195671), ("e4195672", 4195672), ("e4195673", 4195673), ("e4195674", 4195674), ("e4195698", 4195698), ("e4195699", 4195699), ("e4195700", 4195700), ("e4195701", 4195701), ("e4195702", 4195702), ("e4195703", 4195703), ("e4195704", 4195704), ("e4195705", 4195705), ("e4195706", 4195706), ("e4195707", 4195707), ("e4195708", 4195708), ("e4195709", 4195709), ("e4195710", 4195710), ("e4195711", 4195711), ("e4195712", 4195712), ("e4195713", 4195713), ("e4195714", 4195714), ("e4195715", 4195715), ("e4195716", 4195716), ("e4195718", 4195718), ("e4195721", 4195721), ("e4195730", 4195730), ("e4195731", 4195731), ("e4195732", 4195732), ("e4195733", 4195733), ("e4195734", 4195734), ("e4195735", 4195735), ("e4195736", 4195736), ("e4195737", 4195737), ("e4195738", 4195738), ("e4195739", 4195739), ("e4195740", 4195740), ("e4195741", 4195741), ("e4195742", 4195742), ("e4195743", 4195743), ("e4195744", 4195744), ("e4195745", 4195745), ("e4195746", 4195746), ("e4195747", 4195747), ("e4195748", 4195748), ("e4195749", 4195749), ("e4195750", 4195750), ("e4195751", 4195751), ("e4195752", 4195752), ("e4195753", 4195753), ("e4195754", 4195754), ("e4195755", 4195755), ("e4195756", 4195756), ("e4195757", 4195757), ("e4195758", 4195758), ("e4195759", 4195759), ("e4195760", 4195760), ("e4195761", 4195761), ("e4195762", 4195762), ("e4195763", 4195763), ("e4195764", 4195764), ("e4195765", 4195765), ("e4195766", 4195766), ("e4195767", 4195767), ("e4195768", 4195768), ("e4195769", 4195769), ("e4195770", 4195770), ("e4195771", 4195771), ("e4195772", 4195772), ("e4195773", 4195773), ("e4195774", 4195774), ("e4195775", 4195775), ("e4195776", 4195776), ("e4195777", 4195777), ("e4195778", 4195778), ("e4195779", 4195779), ("e4195786", 4195786), ("e4195787", 4195787), ("e4195788", 4195788), ("e4195789", 4195789), ("e4195790", 4195790), ("e4195791", 4195791), ("e4195792", 4195792), ("e4195793", 4195793), ("e4195794", 4195794), ("e4195795", 4195795), ("e4195796", 4195796), ("e4195797", 4195797), ("e4195798", 4195798), ("e4195799", 4195799), ("e4195800", 4195800), ("e4195801", 4195801), ("e4195802", 4195802), ("e4195803", 4195803), ("e4195804", 4195804), ("e4195807", 4195807), ("e4195808", 4195808), ("e4195809", 4195809), ("e4195810", 4195810), ("e4195811", 4195811), ("e4195812", 4195812), ("e4195813", 4195813), ("e4195814", 4195814), ("e4195815", 4195815), ("e4195818", 4195818), ("e4195819", 4195819), ("e4195820", 4195820), ("e4195821", 4195821), ("e4195822", 4195822), ("e4195823", 4195823), ("e4195824", 4195824), ("e4195825", 4195825), ("e4195826", 4195826), ("e4195827", 4195827), ("e4195828", 4195828), ("e4195829", 4195829), ("e4195830", 4195830), ("e4195831", 4195831), ("e4195832", 4195832), ("e4195833", 4195833), ("e4195834", 4195834), ("e4195835", 4195835), ("e4195836", 4195836), ("e4195837", 4195837), ("e4195838", 4195838), ("e4195839", 4195839), ("e4195840", 4195840), ("e4195841", 4195841), ("e4195842", 4195842), ("e4195843", 4195843), ("e4195844", 4195844), ("e4195845", 4195845), ("e4195846", 4195846), ("e4195847", 4195847), ("e4195848", 4195848), ("e4195849", 4195849), ("e4195850", 4195850), ("e4195851", 4195851), ("e4195852", 4195852), ("e4195853", 4195853), ("e4195854", 4195854), ("e4195855", 4195855), ("e4195856", 4195856), ("e4195857", 4195857), ("e4195858", 4195858), ("e4195859", 4195859), ("e4195860", 4195860)) + NamedValues(("e4195861", 4195861), ("e4195862", 4195862), ("e4195863", 4195863), ("e4195864", 4195864), ("e4195865", 4195865), ("e4195866", 4195866), ("e4195867", 4195867), ("e4195868", 4195868), ("e4195869", 4195869), ("e4195870", 4195870), ("e4195871", 4195871), ("e4195872", 4195872), ("e4195873", 4195873), ("e4195874", 4195874), ("e4195875", 4195875), ("e4195876", 4195876), ("e4195877", 4195877), ("e4195880", 4195880), ("e4195881", 4195881), ("e4195882", 4195882), ("e4195883", 4195883), ("e4195884", 4195884), ("e4195885", 4195885), ("e4195886", 4195886), ("e4195887", 4195887), ("e4195888", 4195888), ("e4195889", 4195889), ("e4195890", 4195890), ("e4195891", 4195891), ("e4195892", 4195892), ("e4195893", 4195893), ("e4195894", 4195894), ("e4195895", 4195895), ("e4195896", 4195896), ("e4195897", 4195897), ("e4195898", 4195898), ("e4195899", 4195899), ("e4195900", 4195900), ("e4195901", 4195901), ("e4195902", 4195902), ("e4195903", 4195903), ("e4195904", 4195904), ("e4195905", 4195905), ("e4195906", 4195906), ("e4195907", 4195907), ("e4195908", 4195908), ("e4195909", 4195909), ("e4195910", 4195910), ("e4195911", 4195911), ("e4195912", 4195912), ("e4195913", 4195913), ("e4195914", 4195914), ("e4195915", 4195915), ("e4195916", 4195916), ("e4195917", 4195917), ("e4195918", 4195918), ("e4195919", 4195919), ("e4195920", 4195920), ("e4195921", 4195921), ("e4195922", 4195922), ("e4195923", 4195923), ("e4195924", 4195924), ("e4195925", 4195925), ("e4195926", 4195926), ("e4195927", 4195927), ("e4195928", 4195928), ("e4195929", 4195929), ("e4195930", 4195930), ("e4195931", 4195931), ("e4195932", 4195932), ("e4195933", 4195933), ("e4195934", 4195934), ("e4195935", 4195935), ("e4195936", 4195936), ("e4195937", 4195937), ("e4195938", 4195938), ("e4195939", 4195939), ("e4195940", 4195940), ("e4195941", 4195941), ("e4195942", 4195942), ("e4195943", 4195943), ("e4195944", 4195944), ("e4195945", 4195945), ("e4195946", 4195946), ("e4195947", 4195947), ("e4195948", 4195948), ("e4195949", 4195949), ("e4195950", 4195950), ("e4195951", 4195951), ("e4195952", 4195952), ("e4195953", 4195953), ("e4195956", 4195956), ("e4195957", 4195957), ("e4195958", 4195958), ("e4195959", 4195959), ("e4195960", 4195960), ("e4195961", 4195961), ("e4195962", 4195962), ("e4195963", 4195963), ("e4195964", 4195964), ("e4195965", 4195965), ("e4195966", 4195966), ("e4195967", 4195967), ("e4195968", 4195968), ("e4195969", 4195969), ("e4195970", 4195970), ("e4195971", 4195971), ("e4195972", 4195972), ("e4195973", 4195973), ("e4195976", 4195976), ("e4195977", 4195977), ("e4195978", 4195978), ("e4195979", 4195979), ("e4195980", 4195980), ("e4195981", 4195981), ("e4195982", 4195982), ("e4195983", 4195983), ("e4195984", 4195984), ("e4195985", 4195985), ("e4195986", 4195986), ("e4195987", 4195987), ("e4195988", 4195988), ("e4195989", 4195989), ("e4195991", 4195991), ("e4195992", 4195992), ("e4195993", 4195993), ("e4195994", 4195994), ("e4195995", 4195995), ("e4195996", 4195996), ("e4195997", 4195997), ("e4195998", 4195998), ("e4195999", 4195999), ("e4196000", 4196000), ("e4196001", 4196001), ("e4196002", 4196002), ("e4196003", 4196003), ("e4196004", 4196004), ("e4196005", 4196005), ("e4196006", 4196006), ("e4196007", 4196007), ("e4196008", 4196008), ("e4196009", 4196009), ("e4196010", 4196010), ("e4196011", 4196011), ("e4196012", 4196012), ("e4196013", 4196013), ("e4196014", 4196014), ("e4196015", 4196015), ("e4196016", 4196016), ("e4196017", 4196017), ("e4196018", 4196018), ("e4196019", 4196019), ("e4196020", 4196020), ("e4196021", 4196021), ("e4196022", 4196022), ("e4196023", 4196023), ("e4196024", 4196024), ("e4196025", 4196025), ("e4196026", 4196026), ("e4196027", 4196027), ("e4196028", 4196028), ("e4196029", 4196029), ("e4196030", 4196030), ("e4196031", 4196031), ("e4196032", 4196032), ("e4196033", 4196033), ("e4196034", 4196034), ("e4196035", 4196035), ("e4196036", 4196036), ("e4196041", 4196041), ("e4196042", 4196042), ("e4196045", 4196045), ("e4196047", 4196047), ("e4196048", 4196048), ("e4196049", 4196049), ("e4196051", 4196051), ("e4196052", 4196052), ("e4196055", 4196055), ("e4196056", 4196056), ("e4196060", 4196060), ("e4196061", 4196061), ("e4196062", 4196062), ("e4196063", 4196063), ("e4196065", 4196065), ("e4196066", 4196066), ("e4196067", 4196067), ("e4196068", 4196068), ("e4196069", 4196069), ("e4196070", 4196070), ("e4196071", 4196071), ("e4196072", 4196072), ("e4196073", 4196073), ("e4196074", 4196074), ("e4196075", 4196075), ("e4196076", 4196076), ("e4196077", 4196077), ("e4196078", 4196078), ("e4196079", 4196079), ("e4196080", 4196080), ("e4196081", 4196081), ("e4196082", 4196082), ("e4196083", 4196083), ("e4196084", 4196084), ("e4196085", 4196085), ("e4196086", 4196086), ("e4196087", 4196087), ("e4196088", 4196088), ("e4196089", 4196089), ("e4196090", 4196090), ("e4196091", 4196091), ("e4196092", 4196092), ("e4196093", 4196093), ("e4196094", 4196094), ("e4196095", 4196095), ("e4196096", 4196096), ("e4196097", 4196097), ("e4196098", 4196098), ("e4196099", 4196099), ("e4196100", 4196100), ("e4196101", 4196101), ("e4196102", 4196102), ("e4196103", 4196103), ("e4196104", 4196104), ("e4196105", 4196105), ("e4196106", 4196106), ("e4196107", 4196107), ("e4196108", 4196108), ("e4196109", 4196109), ("e4196110", 4196110), ("e4196111", 4196111), ("e4196112", 4196112), ("e4196113", 4196113), ("e4196114", 4196114), ("e4196115", 4196115), ("e4196116", 4196116), ("e4196117", 4196117), ("e4196118", 4196118), ("e4196119", 4196119), ("e4196120", 4196120), ("e4196121", 4196121), ("e4196122", 4196122), ("e4196123", 4196123), ("e4196124", 4196124), ("e4196125", 4196125), ("e4196126", 4196126), ("e4196127", 4196127), ("e4196128", 4196128), ("e4196129", 4196129), ("e4196130", 4196130), ("e4196131", 4196131), ("e4196132", 4196132), ("e4196133", 4196133), ("e4196134", 4196134), ("e4196135", 4196135), ("e4196136", 4196136)) + NamedValues(("e4196137", 4196137), ("e4196138", 4196138), ("e4196139", 4196139), ("e4196140", 4196140), ("e4196141", 4196141), ("e4196142", 4196142), ("e4196143", 4196143), ("e4196144", 4196144), ("e4196145", 4196145), ("e4196146", 4196146), ("e4196147", 4196147), ("e4196149", 4196149), ("e4196150", 4196150), ("e4196151", 4196151), ("e4196152", 4196152), ("e4196153", 4196153), ("e4196154", 4196154), ("e4196155", 4196155), ("e4196156", 4196156), ("e4196157", 4196157), ("e4196158", 4196158), ("e4196159", 4196159), ("e4196160", 4196160), ("e4196161", 4196161), ("e4196162", 4196162), ("e4196163", 4196163), ("e4196164", 4196164), ("e4196165", 4196165), ("e4196168", 4196168), ("e4196169", 4196169), ("e4196170", 4196170), ("e4196171", 4196171), ("e4196172", 4196172), ("e4196173", 4196173), ("e4196174", 4196174), ("e4196175", 4196175), ("e4196176", 4196176), ("e4196177", 4196177), ("e4196178", 4196178), ("e4196179", 4196179), ("e4196180", 4196180), ("e4196181", 4196181), ("e4196182", 4196182), ("e4196183", 4196183), ("e4196184", 4196184), ("e4196185", 4196185), ("e4196186", 4196186), ("e4196187", 4196187), ("e4196188", 4196188), ("e4196189", 4196189), ("e4196190", 4196190), ("e4196191", 4196191), ("e4196192", 4196192), ("e4196193", 4196193), ("e4196194", 4196194), ("e4196195", 4196195), ("e4196196", 4196196), ("e4196197", 4196197), ("e4196198", 4196198), ("e4196199", 4196199), ("e4196200", 4196200), ("e4196201", 4196201), ("e4196202", 4196202), ("e4196203", 4196203), ("e4196204", 4196204), ("e4196205", 4196205), ("e4196206", 4196206), ("e4196207", 4196207), ("e4196208", 4196208), ("e4196209", 4196209), ("e4196210", 4196210), ("e4196211", 4196211), ("e4196214", 4196214), ("e4196215", 4196215), ("e4196216", 4196216), ("e4196217", 4196217), ("e4196218", 4196218), ("e4196219", 4196219), ("e4196220", 4196220), ("e4196221", 4196221), ("e4196222", 4196222), ("e4196223", 4196223), ("e4196224", 4196224), ("e4196225", 4196225), ("e4196226", 4196226), ("e4196227", 4196227), ("e4196228", 4196228), ("e4196229", 4196229), ("e4196230", 4196230), ("e4196231", 4196231), ("e4196232", 4196232), ("e4196233", 4196233), ("e4196234", 4196234), ("e4196235", 4196235), ("e4196236", 4196236), ("e4196237", 4196237), ("e4196241", 4196241), ("e4196242", 4196242), ("e4196243", 4196243), ("e4196244", 4196244), ("e4196245", 4196245), ("e4196246", 4196246), ("e4196247", 4196247), ("e4196249", 4196249), ("e4196250", 4196250), ("e4196251", 4196251), ("e4196252", 4196252), ("e4196253", 4196253), ("e4196254", 4196254), ("e4196255", 4196255), ("e4196256", 4196256), ("e4196257", 4196257), ("e4196258", 4196258), ("e4196259", 4196259), ("e4196260", 4196260), ("e4196261", 4196261), ("e4196262", 4196262), ("e4196263", 4196263), ("e4196264", 4196264), ("e4196265", 4196265), ("e4196266", 4196266), ("e4196267", 4196267), ("e4196268", 4196268), ("e4196269", 4196269), ("e4196270", 4196270), ("e4196271", 4196271), ("e4196272", 4196272), ("e4196273", 4196273), ("e4196274", 4196274), ("e4196275", 4196275), ("e4196276", 4196276), ("e4196277", 4196277), ("e4196278", 4196278), ("e4196279", 4196279), ("e4196280", 4196280), ("e4196281", 4196281), ("e4196282", 4196282), ("e4196283", 4196283), ("e4196284", 4196284), ("e4196285", 4196285), ("e4196286", 4196286), ("e4196287", 4196287), ("e4196288", 4196288), ("e4196289", 4196289), ("e4196290", 4196290), ("e4196291", 4196291), ("e4196292", 4196292), ("e4196293", 4196293), ("e4196294", 4196294), ("e4196295", 4196295), ("e4196296", 4196296), ("e4196297", 4196297), ("e4196298", 4196298), ("e4196299", 4196299), ("e4196300", 4196300), ("e4196301", 4196301), ("e4196302", 4196302), ("e4196303", 4196303), ("e4196304", 4196304), ("e4196305", 4196305), ("e4196306", 4196306), ("e4196307", 4196307), ("e4196308", 4196308), ("e4196309", 4196309), ("e4196310", 4196310), ("e4196317", 4196317), ("e4196318", 4196318), ("e4196319", 4196319), ("e4196320", 4196320), ("e4196321", 4196321), ("e4196322", 4196322), ("e4196323", 4196323), ("e4196324", 4196324), ("e4196325", 4196325), ("e4196326", 4196326), ("e4196327", 4196327), ("e4196328", 4196328), ("e4196329", 4196329), ("e4196330", 4196330), ("e4196331", 4196331), ("e4196332", 4196332), ("e4196333", 4196333), ("e4196334", 4196334), ("e4196335", 4196335), ("e4196336", 4196336), ("e4196337", 4196337), ("e4196338", 4196338), ("e4196339", 4196339), ("e4196340", 4196340), ("e4196341", 4196341), ("e4196342", 4196342), ("e4196343", 4196343), ("e4196344", 4196344), ("e4196345", 4196345), ("e4196346", 4196346), ("e4196347", 4196347), ("e4196348", 4196348), ("e4196349", 4196349), ("e4196350", 4196350), ("e4196354", 4196354), ("e4196355", 4196355), ("e4196356", 4196356), ("e4196357", 4196357), ("e4196358", 4196358), ("e4196359", 4196359), ("e4196360", 4196360), ("e4196361", 4196361), ("e4196362", 4196362), ("e4196363", 4196363), ("e4196364", 4196364), ("e4196365", 4196365), ("e4196366", 4196366), ("e4196367", 4196367), ("e4196368", 4196368), ("e4196369", 4196369), ("e4196370", 4196370), ("e4196371", 4196371), ("e4196372", 4196372), ("e4196373", 4196373), ("e4196374", 4196374), ("e4196375", 4196375), ("e4196376", 4196376), ("e4196377", 4196377), ("e4196378", 4196378), ("e4196379", 4196379), ("e4196380", 4196380), ("e4196381", 4196381), ("e4196382", 4196382), ("e4196383", 4196383), ("e4196384", 4196384), ("e4196385", 4196385), ("e4196386", 4196386), ("e4196387", 4196387), ("e4196388", 4196388), ("e4196389", 4196389), ("e4196390", 4196390), ("e4196391", 4196391), ("e4196392", 4196392), ("e4196393", 4196393), ("e4196394", 4196394), ("e4196395", 4196395), ("e4196396", 4196396), ("e4196397", 4196397), ("e4196398", 4196398), ("e4196399", 4196399), ("e4196400", 4196400), ("e4196401", 4196401), ("e4196402", 4196402), ("e4196403", 4196403), ("e4196404", 4196404), ("e4196405", 4196405), ("e4196406", 4196406), ("e4196407", 4196407), ("e4196408", 4196408), ("e4196409", 4196409)) + NamedValues(("e4196410", 4196410), ("e4196411", 4196411), ("e4196412", 4196412), ("e4196413", 4196413), ("e4196414", 4196414), ("e4196415", 4196415), ("e4196416", 4196416), ("e4196417", 4196417), ("e4196418", 4196418), ("e4196419", 4196419), ("e4196420", 4196420), ("e4196421", 4196421), ("e4196422", 4196422), ("e4196423", 4196423), ("e4196424", 4196424), ("e4196425", 4196425), ("e4196426", 4196426), ("e4196427", 4196427), ("e4196428", 4196428), ("e4196429", 4196429), ("e4196430", 4196430), ("e4196431", 4196431), ("e4196432", 4196432), ("e4196433", 4196433), ("e4196434", 4196434), ("e4196435", 4196435), ("e4196436", 4196436), ("e4196437", 4196437), ("e4196438", 4196438), ("e4196439", 4196439), ("e4196440", 4196440), ("e4196441", 4196441), ("e4196442", 4196442), ("e4196443", 4196443), ("e4196444", 4196444), ("e4196445", 4196445), ("e4196446", 4196446), ("e4196447", 4196447), ("e4196448", 4196448), ("e4196449", 4196449), ("e4196450", 4196450), ("e4196451", 4196451), ("e4196452", 4196452), ("e4196453", 4196453), ("e4196454", 4196454), ("e4196455", 4196455), ("e4196456", 4196456), ("e4196457", 4196457), ("e4196458", 4196458), ("e4196459", 4196459), ("e4196460", 4196460), ("e4196461", 4196461), ("e4196462", 4196462), ("e4196463", 4196463), ("e4196464", 4196464), ("e4196465", 4196465), ("e4196466", 4196466), ("e4196467", 4196467), ("e4196468", 4196468), ("e4196469", 4196469), ("e4196470", 4196470), ("e4196471", 4196471), ("e4196472", 4196472), ("e4196474", 4196474), ("e4196475", 4196475), ("e4196477", 4196477), ("e4196478", 4196478), ("e4196480", 4196480), ("e4196481", 4196481), ("e4196483", 4196483), ("e4196484", 4196484), ("e4196485", 4196485), ("e4196486", 4196486), ("e4196487", 4196487), ("e4196488", 4196488), ("e4196489", 4196489), ("e4196490", 4196490), ("e4196491", 4196491), ("e4196492", 4196492), ("e4196493", 4196493), ("e4196494", 4196494), ("e4196495", 4196495), ("e4196496", 4196496), ("e4196497", 4196497), ("e4196498", 4196498), ("e4196499", 4196499), ("e4196500", 4196500), ("e4196501", 4196501), ("e4196502", 4196502), ("e4196503", 4196503), ("e4196504", 4196504), ("e4196505", 4196505), ("e4196506", 4196506), ("e4196507", 4196507), ("e4196508", 4196508), ("e4196509", 4196509), ("e4196510", 4196510), ("e4196511", 4196511), ("e4196512", 4196512), ("e4196513", 4196513), ("e4196514", 4196514), ("e4196515", 4196515), ("e4196516", 4196516), ("e4196517", 4196517), ("e4196518", 4196518), ("e4196519", 4196519), ("e4196520", 4196520), ("e4196521", 4196521), ("e4196522", 4196522), ("e4196523", 4196523), ("e4196524", 4196524), ("e4196525", 4196525), ("e4196526", 4196526), ("e4196527", 4196527), ("e4196528", 4196528), ("e4196529", 4196529), ("e4196530", 4196530), ("e4196531", 4196531), ("e4196532", 4196532), ("e4196533", 4196533), ("e4196534", 4196534), ("e4196535", 4196535), ("e4196536", 4196536), ("e4196537", 4196537), ("e4196538", 4196538), ("e4196539", 4196539), ("e4196540", 4196540), ("e4196541", 4196541), ("e4196542", 4196542), ("e4196543", 4196543), ("e4196544", 4196544), ("e4196545", 4196545), ("e4196546", 4196546), ("e4196555", 4196555), ("e4196556", 4196556), ("e4196557", 4196557), ("e4196558", 4196558), ("e4196559", 4196559), ("e4196560", 4196560), ("e4196561", 4196561), ("e4196562", 4196562), ("e4196563", 4196563), ("e4196564", 4196564), ("e4196565", 4196565), ("e4196566", 4196566), ("e4196567", 4196567), ("e4196568", 4196568), ("e4196569", 4196569), ("e4196570", 4196570), ("e4196571", 4196571), ("e4196572", 4196572), ("e4196573", 4196573), ("e4196574", 4196574), ("e4196575", 4196575), ("e4196576", 4196576), ("e4196577", 4196577), ("e4196578", 4196578), ("e4196579", 4196579), ("e4196580", 4196580), ("e4196581", 4196581), ("e4196582", 4196582), ("e4196583", 4196583), ("e4196584", 4196584), ("e4196585", 4196585), ("e4196586", 4196586), ("e4196587", 4196587), ("e4196588", 4196588), ("e4196589", 4196589), ("e4196590", 4196590), ("e4196591", 4196591), ("e4196592", 4196592), ("e4196593", 4196593), ("e4196594", 4196594), ("e4196595", 4196595), ("e4196596", 4196596), ("e4196597", 4196597), ("e4196598", 4196598), ("e4196599", 4196599), ("e4196600", 4196600), ("e4196601", 4196601), ("e4196602", 4196602), ("e4196603", 4196603), ("e4196604", 4196604), ("e4196605", 4196605), ("e4196606", 4196606), ("e4196607", 4196607), ("e4196608", 4196608), ("e4196609", 4196609), ("e4196610", 4196610), ("e4196611", 4196611), ("e4196612", 4196612), ("e4196613", 4196613), ("e4196614", 4196614), ("e4196619", 4196619), ("e4196620", 4196620), ("e4196621", 4196621), ("e4196622", 4196622), ("e4196623", 4196623), ("e4196624", 4196624), ("e4196625", 4196625), ("e4196626", 4196626), ("e4196627", 4196627), ("e4196628", 4196628), ("e4196629", 4196629), ("e4196630", 4196630), ("e4196631", 4196631), ("e4196632", 4196632), ("e4196633", 4196633), ("e4196634", 4196634), ("e4196635", 4196635), ("e4196636", 4196636), ("e4196637", 4196637), ("e4196638", 4196638), ("e4196639", 4196639), ("e4196640", 4196640), ("e4196641", 4196641), ("e4196642", 4196642), ("e4196643", 4196643), ("e4196644", 4196644), ("e4196645", 4196645), ("e4196646", 4196646), ("e4196647", 4196647), ("e4196648", 4196648), ("e4196649", 4196649), ("e4196650", 4196650), ("e4196651", 4196651), ("e4196652", 4196652), ("e4196653", 4196653), ("e4196654", 4196654), ("e4196655", 4196655), ("e4196656", 4196656), ("e4196657", 4196657), ("e4196658", 4196658), ("e4196659", 4196659), ("e4196660", 4196660), ("e4196661", 4196661), ("e4196662", 4196662), ("e4196663", 4196663), ("e4196664", 4196664), ("e4196665", 4196665), ("e4196666", 4196666), ("e4196667", 4196667), ("e4196668", 4196668), ("e4196669", 4196669), ("e4196670", 4196670), ("e4196671", 4196671), ("e4196672", 4196672), ("e4196673", 4196673), ("e4196674", 4196674), ("e4196675", 4196675), ("e4196676", 4196676), ("e4196677", 4196677), ("e4196678", 4196678), ("e4196679", 4196679), ("e4196680", 4196680)) + NamedValues(("e4196681", 4196681), ("e4196682", 4196682), ("e4196683", 4196683), ("e4196684", 4196684), ("e4196685", 4196685), ("e4196686", 4196686), ("e4196687", 4196687), ("e4196688", 4196688), ("e4196689", 4196689), ("e4196690", 4196690), ("e4196691", 4196691), ("e4196692", 4196692), ("e4196693", 4196693), ("e4196694", 4196694), ("e4196695", 4196695), ("e4196696", 4196696), ("e4196697", 4196697), ("e4196698", 4196698), ("e4196699", 4196699), ("e4196700", 4196700), ("e4196701", 4196701), ("e4196702", 4196702), ("e4196703", 4196703), ("e4196704", 4196704), ("e4196705", 4196705), ("e4196706", 4196706), ("e4196707", 4196707), ("e4196708", 4196708), ("e4196709", 4196709), ("e4196710", 4196710), ("e4196711", 4196711), ("e4196712", 4196712), ("e4196713", 4196713), ("e4196714", 4196714), ("e4196715", 4196715), ("e4196716", 4196716), ("e4196717", 4196717), ("e4196718", 4196718), ("e4196719", 4196719), ("e4196720", 4196720), ("e4196721", 4196721), ("e4196722", 4196722), ("e4196723", 4196723), ("e4196724", 4196724), ("e4196725", 4196725), ("e4196726", 4196726), ("e4196727", 4196727), ("e4196728", 4196728), ("e4196729", 4196729), ("e4196730", 4196730), ("e4196731", 4196731), ("e4196732", 4196732), ("e4196733", 4196733), ("e4196734", 4196734), ("e4196735", 4196735), ("e4196736", 4196736), ("e4196737", 4196737), ("e4196738", 4196738), ("e4196739", 4196739), ("e4196740", 4196740), ("e4196741", 4196741), ("e4196742", 4196742), ("e4196743", 4196743), ("e4196744", 4196744), ("e4196745", 4196745), ("e4196746", 4196746), ("e4196747", 4196747), ("e4196748", 4196748), ("e4196749", 4196749), ("e4196750", 4196750), ("e4196751", 4196751), ("e4196752", 4196752), ("e4196753", 4196753), ("e4196754", 4196754), ("e4196755", 4196755), ("e4196756", 4196756), ("e4196757", 4196757), ("e4196758", 4196758), ("e4196759", 4196759), ("e4196760", 4196760), ("e4196761", 4196761), ("e4196762", 4196762), ("e4196763", 4196763), ("e4196764", 4196764), ("e4196765", 4196765), ("e4196766", 4196766), ("e4196767", 4196767), ("e4196768", 4196768), ("e4196769", 4196769), ("e4196770", 4196770), ("e4196771", 4196771), ("e4196772", 4196772), ("e4196773", 4196773), ("e4196774", 4196774), ("e4196775", 4196775), ("e4196776", 4196776), ("e4196777", 4196777), ("e4196778", 4196778), ("e4196779", 4196779), ("e4196780", 4196780), ("e4196781", 4196781), ("e4196785", 4196785), ("e4196787", 4196787), ("e4196788", 4196788), ("e4196789", 4196789), ("e4196790", 4196790), ("e4196791", 4196791), ("e4196792", 4196792), ("e4196793", 4196793), ("e4196794", 4196794), ("e4196795", 4196795), ("e4196796", 4196796), ("e4196797", 4196797), ("e4196798", 4196798), ("e4196799", 4196799), ("e4196800", 4196800), ("e4196801", 4196801), ("e4196802", 4196802), ("e4196803", 4196803), ("e4196804", 4196804), ("e4196805", 4196805), ("e4196806", 4196806), ("e4196807", 4196807), ("e4196808", 4196808), ("e4196809", 4196809), ("e4196810", 4196810), ("e4196811", 4196811), ("e4196812", 4196812), ("e4196813", 4196813), ("e4196814", 4196814), ("e4196815", 4196815), ("e4196816", 4196816), ("e4196817", 4196817), ("e4196818", 4196818), ("e4196819", 4196819), ("e4196820", 4196820), ("e4196821", 4196821), ("e4196822", 4196822), ("e4196823", 4196823), ("e4196824", 4196824), ("e4196825", 4196825), ("e4196826", 4196826), ("e4196827", 4196827), ("e4196828", 4196828), ("e4196829", 4196829), ("e4196830", 4196830), ("e4196831", 4196831), ("e4196832", 4196832), ("e4196833", 4196833), ("e4196834", 4196834), ("e4196835", 4196835), ("e4196836", 4196836), ("e4196837", 4196837), ("e4196838", 4196838), ("e4196839", 4196839), ("e4196840", 4196840), ("e4196841", 4196841), ("e4196842", 4196842), ("e4196843", 4196843), ("e4196844", 4196844), ("e4196845", 4196845), ("e4196846", 4196846), ("e4196847", 4196847), ("e4196848", 4196848), ("e4196849", 4196849), ("e4196850", 4196850), ("e4196851", 4196851), ("e4196852", 4196852), ("e4196853", 4196853), ("e4196854", 4196854), ("e4196855", 4196855), ("e4196856", 4196856), ("e4196857", 4196857), ("e4196858", 4196858), ("e4196859", 4196859), ("e4196860", 4196860), ("e4196861", 4196861), ("e4196862", 4196862), ("e4196863", 4196863), ("e4196864", 4196864), ("e4196865", 4196865), ("e4196866", 4196866), ("e4196867", 4196867), ("e4196868", 4196868), ("e4196869", 4196869), ("e4196870", 4196870), ("e4196871", 4196871), ("e4196872", 4196872), ("e4196873", 4196873), ("e4196874", 4196874), ("e4196875", 4196875), ("e4196876", 4196876), ("e4196877", 4196877), ("e4196878", 4196878), ("e4196879", 4196879), ("e4196880", 4196880), ("e4196881", 4196881), ("e4196882", 4196882), ("e4196883", 4196883), ("e4196884", 4196884), ("e4196885", 4196885), ("e4196886", 4196886), ("e4196887", 4196887), ("e4196888", 4196888), ("e4196889", 4196889), ("e4196890", 4196890), ("e4196891", 4196891), ("e4196892", 4196892), ("e4196893", 4196893), ("e4196894", 4196894), ("e4196895", 4196895), ("e4196896", 4196896), ("e4196897", 4196897), ("e4196898", 4196898), ("e4196899", 4196899), ("e4196900", 4196900), ("e4196901", 4196901), ("e4196902", 4196902), ("e4196903", 4196903), ("e4196904", 4196904), ("e4196905", 4196905), ("e4196906", 4196906), ("e4196907", 4196907), ("e4196908", 4196908), ("e4196909", 4196909), ("e4196910", 4196910), ("e4196911", 4196911), ("e4196912", 4196912), ("e4196913", 4196913), ("e4196914", 4196914), ("e4196915", 4196915), ("e4196916", 4196916), ("e4196917", 4196917), ("e4196918", 4196918), ("e4196919", 4196919), ("e4196920", 4196920), ("e4196921", 4196921), ("e4196922", 4196922), ("e4196923", 4196923), ("e4196924", 4196924), ("e4196925", 4196925), ("e4196926", 4196926), ("e4196927", 4196927), ("e4196928", 4196928), ("e4196929", 4196929), ("e4196930", 4196930), ("e4196931", 4196931), ("e4196932", 4196932), ("e4196933", 4196933), ("e4196934", 4196934), ("e4196935", 4196935), ("e4196936", 4196936), ("e4196937", 4196937), ("e4196938", 4196938), ("e4196939", 4196939)) + NamedValues(("e4196940", 4196940), ("e4196941", 4196941), ("e4196942", 4196942), ("e4196943", 4196943), ("e4196944", 4196944), ("e4196945", 4196945), ("e4196946", 4196946), ("e4196947", 4196947), ("e4196948", 4196948), ("e4196949", 4196949), ("e4196950", 4196950), ("e4196951", 4196951), ("e4196952", 4196952), ("e4196953", 4196953), ("e4196954", 4196954), ("e4196955", 4196955), ("e4196956", 4196956), ("e4196957", 4196957), ("e4196958", 4196958), ("e4196959", 4196959), ("e4196960", 4196960), ("e4196961", 4196961), ("e4196962", 4196962), ("e4196963", 4196963), ("e4196964", 4196964), ("e4196965", 4196965), ("e4196966", 4196966), ("e4196967", 4196967), ("e4196968", 4196968), ("e4196969", 4196969), ("e4196970", 4196970), ("e4196971", 4196971), ("e4196972", 4196972), ("e4196973", 4196973), ("e4196974", 4196974), ("e4196975", 4196975), ("e4196976", 4196976), ("e4196977", 4196977), ("e4196978", 4196978), ("e4196979", 4196979), ("e4196980", 4196980), ("e4196981", 4196981), ("e4196982", 4196982), ("e4196983", 4196983), ("e4196984", 4196984), ("e4196985", 4196985), ("e4196986", 4196986), ("e4196987", 4196987), ("e4196988", 4196988), ("e4196989", 4196989), ("e4196990", 4196990), ("e4196991", 4196991), ("e4196992", 4196992), ("e4196993", 4196993), ("e4196994", 4196994), ("e4196995", 4196995), ("e4196996", 4196996), ("e4196997", 4196997), ("e4196998", 4196998), ("e4196999", 4196999), ("e4197000", 4197000), ("e4197001", 4197001), ("e4197002", 4197002), ("e4197003", 4197003), ("e4197004", 4197004), ("e4197005", 4197005), ("e4197006", 4197006), ("e4197007", 4197007), ("e4197008", 4197008), ("e4197009", 4197009), ("e4197010", 4197010), ("e4197011", 4197011), ("e4197012", 4197012), ("e4197013", 4197013), ("e4197014", 4197014), ("e4197015", 4197015), ("e4197016", 4197016), ("e4197017", 4197017), ("e4197018", 4197018), ("e4197019", 4197019), ("e4197020", 4197020), ("e4197021", 4197021), ("e4197022", 4197022), ("e4197023", 4197023), ("e4197024", 4197024), ("e4197025", 4197025), ("e4197026", 4197026), ("e4197027", 4197027), ("e4197028", 4197028), ("e4197029", 4197029), ("e4197030", 4197030), ("e4197031", 4197031), ("e4197032", 4197032), ("e4197033", 4197033), ("e4197034", 4197034), ("e4197035", 4197035), ("e4197036", 4197036), ("e4197037", 4197037), ("e4197038", 4197038), ("e4197039", 4197039), ("e4197040", 4197040), ("e4197041", 4197041), ("e4197042", 4197042), ("e4197043", 4197043), ("e4197044", 4197044), ("e4197045", 4197045), ("e4197046", 4197046), ("e4197047", 4197047), ("e4197048", 4197048), ("e4197049", 4197049), ("e4197050", 4197050), ("e4197051", 4197051), ("e4197052", 4197052), ("e4197053", 4197053), ("e4197054", 4197054), ("e4197055", 4197055), ("e4197056", 4197056), ("e4197057", 4197057), ("e4197058", 4197058), ("e4197059", 4197059), ("e4197060", 4197060), ("e4197061", 4197061), ("e4197062", 4197062), ("e4197063", 4197063), ("e4197064", 4197064), ("e4197065", 4197065), ("e4197066", 4197066), ("e4197067", 4197067), ("e4197068", 4197068), ("e4197069", 4197069), ("e4197070", 4197070), ("e4197071", 4197071), ("e4197072", 4197072), ("e4197073", 4197073), ("e4197074", 4197074), ("e4197075", 4197075), ("e4197076", 4197076), ("e4197077", 4197077), ("e4197078", 4197078), ("e4197079", 4197079), ("e4197080", 4197080), ("e4197081", 4197081), ("e4197082", 4197082), ("e4197083", 4197083), ("e4197084", 4197084), ("e4197085", 4197085), ("e4197086", 4197086), ("e4197087", 4197087), ("e4197088", 4197088), ("e4197089", 4197089), ("e4197090", 4197090), ("e4197091", 4197091), ("e4197092", 4197092), ("e4197093", 4197093), ("f4522530", 4522530), ("f4522532", 4522532), ("f4522544", 4522544), ("f4522556", 4522556), ("f4522561", 4522561), ("f4522588", 4522588), ("f4522603", 4522603), ("f4525234", 4525234), ("f4525239", 4525239), ("f4525240", 4525240), ("f4525241", 4525241), ("f4525247", 4525247), ("f4525248", 4525248), ("f4525250", 4525250), ("f4525251", 4525251), ("f4525252", 4525252), ("f4525253", 4525253), ("f4525254", 4525254), ("f4526517", 4526517), ("f4526850", 4526850), ("f4526851", 4526851), ("f4526901", 4526901), ("f4526902", 4526902), ("f4527601", 4527601), ("f4528207", 4528207), ("f4528209", 4528209), ("f4528211", 4528211), ("f4528216", 4528216), ("f4528218", 4528218), ("f4528220", 4528220), ("f4528223", 4528223), ("f4528225", 4528225), ("f4528227", 4528227), ("f4528268", 4528268), ("f4528270", 4528270), ("f4528591", 4528591), ("f4528596", 4528596), ("f4528842", 4528842), ("f4529444", 4529444), ("f4529447", 4529447), ("f4529495", 4529495), ("f4529514", 4529514), ("f4529517", 4529517), ("f4529520", 4529520), ("f4529522", 4529522), ("f4529524", 4529524), ("f4529533", 4529533), ("f4529601", 4529601), ("f4529604", 4529604), ("f4529606", 4529606), ("f4529615", 4529615), ("f4529722", 4529722), ("f4529725", 4529725), ("f4529838", 4529838), ("f4529847", 4529847), ("f4529849", 4529849), ("f4529971", 4529971), ("f4529973", 4529973), ("f4530046", 4530046), ("f4530050", 4530050), ("f4530080", 4530080), ("f4530082", 4530082), ("f4530083", 4530083), ("f4530085", 4530085), ("f4530092", 4530092), ("f4530095", 4530095), ("f4530097", 4530097), ("f4530098", 4530098), ("f4530100", 4530100), ("f4530106", 4530106), ("f4530109", 4530109), ("f4530111", 4530111), ("f4530112", 4530112), ("f4530113", 4530113), ("f4530114", 4530114), ("f4530115", 4530115), ("f4530117", 4530117), ("f4530119", 4530119), ("f4530121", 4530121), ("f4530122", 4530122), ("f4530123", 4530123), ("f4530125", 4530125), ("f4530127", 4530127), ("f4530139", 4530139), ("f4530143", 4530143), ("f4530166", 4530166), ("f4530204", 4530204), ("f4530206", 4530206), ("f4530389", 4530389), ("f4530391", 4530391), ("f4530407", 4530407), ("f4530451", 4530451), ("f4530727", 4530727), ("f4531275", 4531275))

class CucsConditionLifecycle(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("flapping", 0), ("soakingClear", 1), ("soakingRaise", 2), ("suppressed", 3))

class CucsConditionRemoteInvRslt(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("failure", 0), ("unidentifiedFail", 1), ("internalError", 2), ("timeout", 3), ("endPointUnavailable", 4), ("endPointFailed", 5), ("endPointProtocolError", 6), ("swDefect", 7), ("fwDefect", 8), ("hwDefect", 9), ("resourceUnavailable", 10), ("resourceCapacityExceeded", 11), ("resourceDependency", 12), ("capabilityNotImplementedIgnore", 13), ("capabilityNotImplementedFailure", 14), ("capabilityNotSupported", 15), ("capabilityUnavailable", 16), ("serviceNotImplementedIgnore", 17), ("serviceNotImplementedFail", 18), ("serviceNotSupported", 19), ("serviceUnavailable", 20), ("serviceProtocolError", 21), ("fruIdentityIndeterminate", 22), ("fruInfoMalformed", 23), ("illegalFru", 24), ("fruStateIndeterminate", 25), ("fruNotReady", 26), ("extendTimeout", 27), ("taskReset", 28), ("fruNotSupported", 29), ("intermittentError", 30))

class CucsConditionRule(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 156, 157, 169, 170, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 200, 203, 206, 207, 209, 276, 277, 278, 279, 282, 283, 291, 293, 294, 304, 305, 306, 310, 311, 312, 313, 314, 315, 317, 318, 319, 320, 321, 322, 324, 326, 327, 329, 330, 331, 332, 334, 337, 367, 368, 369, 371, 373, 374, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 387, 389, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 424, 425, 428, 429, 430, 434, 435, 436, 440, 451, 452, 453, 454, 455, 456, 458, 459, 460, 461, 462, 463, 464, 465, 466, 470, 471, 476, 478, 479, 480, 481, 484, 502, 517, 528, 530, 560, 561, 577, 578, 579, 582, 583, 584, 587, 591, 592, 593, 594, 595, 596, 597, 598, 599, 621, 622, 625, 635, 646, 654, 656, 669, 670, 688, 689, 690, 693, 695, 696, 708, 710, 714, 727, 728, 729, 730, 731, 733, 734, 735, 736, 740, 741, 742, 743, 744, 747, 757, 764, 765, 766, 772, 775, 776, 777, 778, 791, 792, 793, 794, 795, 796, 797, 798, 801, 807, 826, 829, 837, 846, 855, 857, 859, 861, 862, 865, 866, 867, 872, 874, 875, 876, 877, 878, 879, 880, 885, 887, 890, 900, 901, 902, 903, 909, 910, 915, 916, 917, 918, 919, 920, 921, 928, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954), SingleValueConstraint(957, 958, 959, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 1010, 1017, 1037, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1097, 1101, 1102, 1103, 1104, 1105, 1106, 1202, 1204, 1206, 1207, 1209, 1216, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1232, 1233, 1237, 16405, 16406, 16407, 16408, 16518, 16519, 16520, 16533, 16534, 16535, 16539, 16550, 16576, 16577, 16579, 16580, 16581, 16582, 16600, 16601, 16604, 16605, 16606, 16634, 16635, 16636, 16637, 16641, 16650, 16651, 16653, 16654, 16655, 16656, 16657, 16670, 16673, 16674, 16679, 16680, 16681, 16682, 16683, 16684, 16742, 16745, 16749, 16750, 16803, 16815, 16823, 16852, 16857, 16858, 16879, 16880, 16881, 16898, 16904, 16906, 16920, 16921, 16922, 16924, 16925, 16926, 16927, 16928, 16929, 16930, 16931, 16932, 16934, 16935, 16938, 16939, 16940, 16941, 16942, 16943, 16944, 16945, 16950, 16964, 16965, 16973, 16974, 16975, 16976, 16977, 16978, 16979, 16980, 16981, 16982, 16983, 16984, 16986, 16987, 16988, 16991, 16992, 16993, 16994, 16995, 17000, 17001, 17002, 17007, 17008, 17012, 17013, 17014, 17017, 17018, 17043, 17044, 17045, 17046, 17050, 17051, 17052, 17053, 17060, 17061, 17083, 17084, 17089, 17116, 17133, 17134, 17163, 17169, 17170, 17187, 17190, 17192, 17195, 17196, 17207, 17214, 17223, 17239, 17254, 17259, 17262, 17271, 17281, 17282, 17325, 17326, 17339, 17340, 17348, 17349, 17350, 17367, 17381, 17382, 17383, 17384, 17399, 17400, 17402, 17403, 17404, 17405, 17406, 17407, 17408, 17409, 17410, 17411, 17412, 17413, 17414, 17415, 17416, 17418, 17419, 17420, 17425, 17426, 17427, 17428, 17445, 17476, 17477, 17478, 17483, 17485, 17599, 17601), SingleValueConstraint(17602, 33142, 33144, 33145, 33146, 33167, 33168, 33169, 33170, 33177, 33178, 33179, 33180, 33187, 33188, 33189, 33190, 33197, 33198, 33199, 33200, 33211, 33212, 33213, 33214, 33221, 33222, 33223, 33224, 33231, 33232, 33233, 33234, 33241, 33242, 33243, 33244, 33251, 33252, 33253, 33254, 33261, 33262, 33263, 33264, 33271, 33272, 33273, 33274, 33281, 33282, 33283, 33284, 33291, 33292, 33293, 33294, 33301, 33302, 33303, 33304, 33483, 33485, 33486, 33487, 33491, 33493, 33494, 33495, 33499, 33501, 33502, 33503, 33720, 33721, 33722, 33723, 33730, 33731, 33732, 33733, 33740, 33741, 33742, 33743, 33750, 33751, 33752, 33753, 33760, 33761, 33762, 33763, 33770, 33771, 33772, 33773, 33810, 33811, 33812, 33813, 33820, 33821, 33822, 33823, 33830, 33831, 33832, 33833, 33840, 33841, 33842, 33843, 33850, 33851, 33852, 33853, 33860, 33861, 33862, 33863, 33875, 33876, 33877, 33878, 33885, 33886, 33887, 33888, 33895, 33896, 33897, 33898, 33905, 33906, 33907, 33908, 33915, 33916, 33917, 33918, 33925, 33926, 33927, 33928, 33940, 33941, 33942, 33943, 33950, 33951, 33952, 33953, 33960, 33961, 33962, 33963, 33970, 33971, 33972, 33973, 33980, 33981, 33982, 33983, 33995, 33996, 33997, 33998, 34005, 34006, 34007, 34008, 34015, 34016, 34017, 34018, 34030, 34031, 34032, 34033, 34040, 34041, 34042, 34043, 34050, 34051, 34052, 34053, 34064, 34065, 34066, 34067, 34074, 34075, 34076, 34077, 34084, 34085, 34086, 34087, 34094, 34095, 34096, 34097, 34108, 34109, 34110, 34111, 34118, 34119, 34120, 34121, 34128, 34129, 34130, 34131, 34138, 34139, 34140, 34141, 34148, 34149, 34150, 34151, 34158, 34159, 34160, 34161, 34168, 34169, 34170, 34171, 34178, 34179, 34180, 34181, 34192, 34193, 34194, 34195, 34202, 34203, 34204, 34205, 34212, 34213, 34214, 34215, 34222, 34223, 34224, 34225, 34232, 34233), SingleValueConstraint(34234, 34235, 34246, 34247, 34248, 34249, 34256, 34257, 34258, 34259, 34271, 34272, 34273, 34274, 34281, 34282, 34283, 34284, 34291, 34292, 34293, 34294, 34301, 34302, 34303, 34304, 34316, 34317, 34318, 34319, 34326, 34327, 34328, 34329, 34336, 34337, 34338, 34339, 34346, 34347, 34348, 34349, 34361, 34362, 34363, 34364, 34371, 34372, 34373, 34374, 34381, 34382, 34383, 34384, 34396, 34397, 34398, 34399, 34406, 34407, 34408, 34409, 34416, 34417, 34418, 34419, 34426, 34427, 34428, 34429, 34436, 34437, 34438, 34439, 34451, 34452, 34453, 34454, 34461, 34462, 34463, 34464, 34471, 34472, 34473, 34474, 34481, 34482, 34483, 34484, 34496, 34497, 34498, 34499, 34506, 34507, 34508, 34509, 34516, 34517, 34518, 34519, 34526, 34527, 34528, 34529, 34542, 34543, 34544, 34545, 34552, 34553, 34554, 34555, 34562, 34563, 34564, 34565, 34572, 34573, 34574, 34575, 34588, 34589, 34590, 34591, 34598, 34599, 34600, 34601, 34608, 34609, 34610, 34611, 34618, 34619, 34620, 34621, 34633, 34634, 34635, 34636, 34643, 34644, 34645, 34646, 34653, 34654, 34655, 34656, 34663, 34664, 34665, 34666, 34673, 34674, 34675, 34676, 34688, 34689, 34690, 34691, 34698, 34699, 34700, 34701, 34708, 34709, 34710, 34711, 34718, 34719, 34720, 34721, 34733, 34734, 34735, 34736, 34743, 34744, 34745, 34746, 34753, 34754, 34755, 34756, 34763, 34764, 34765, 34766, 34778, 34779, 34780, 34781, 34788, 34789, 34790, 34791, 34798, 34799, 34800, 34801, 34808, 34809, 34810, 34811, 34822, 34823, 34824, 34825, 34832, 34833, 34834, 34835, 34842, 34843, 34844, 34845, 34852, 34853, 34854, 34855, 34862, 34863, 34864, 34865, 34872, 34873, 34874, 34875, 34882, 34883, 34884, 34885, 34892, 34893, 34894, 34895, 34906, 34907, 34908, 34909, 34916, 34917, 34918, 34919, 34926, 34927, 34928, 34929, 34936, 34937, 34938, 34939, 34950), SingleValueConstraint(34951, 34952, 34953, 34960, 34961, 34962, 34963, 34970, 34971, 34972, 34973, 34980, 34981, 34982, 34983, 34990, 34991, 34992, 34993, 35000, 35001, 35002, 35003, 35010, 35011, 35012, 35013, 35020, 35021, 35022, 35023, 35166, 35168, 35169, 35170, 35174, 35176, 35177, 35178, 35198, 35200, 35201, 35202, 35206, 35208, 35209, 35210, 35214, 35216, 35217, 35218, 35222, 35224, 35225, 35226, 35234, 35236, 35237, 35238, 35242, 35244, 35245, 35246, 35250, 35252, 35253, 35254, 35275, 35276, 35277, 35278, 35285, 35286, 35287, 35288, 35295, 35296, 35297, 35298, 35305, 35306, 35307, 35308, 35315, 35316, 35317, 35318, 35329, 35330, 35331, 35332, 35339, 35340, 35341, 35342, 35349, 35350, 35351, 35352, 35359, 35360, 35361, 35362, 35369, 35370, 35371, 35372, 35379, 35380, 35381, 35382, 35962, 35964, 35965, 35966, 35974, 35976, 35977, 35978, 36234, 36236, 36237, 36238, 36242, 36244, 36245, 36246, 36266, 36268, 36269, 36270, 36274, 36276, 36277, 36278, 36282, 36284, 36285, 36286, 36294, 36296, 36297, 36298, 36302, 36304, 36305, 36306, 36310, 36312, 36313, 36314, 36323, 36325, 36326, 36327, 36335, 36337, 36338, 36339, 37154, 37156, 37157, 37158, 37162, 37164, 37165, 37166, 37170, 37172, 37173, 37174, 37269, 37271, 37272, 37273, 37313, 37314, 37315, 37316, 37323, 37324, 37325, 37326, 37333, 37334, 37335, 37336, 37343, 37344, 37345, 37346, 37353, 37354, 37355, 37356, 37363, 37364, 37365, 37366, 37383, 37384, 37385, 37386, 37393, 37394, 37395, 37396, 37403, 37404, 37405, 37406, 37413, 37414, 37415, 37416, 37423, 37424, 37425, 37426, 37443, 37444, 37445, 37446, 37453, 37454, 37455, 37456, 37463, 37464, 37465, 37466, 37473, 37474, 37475, 37476, 37485, 37486, 37487, 37488, 37495, 37496, 37497, 37498, 37505, 37506, 37507, 37508, 37532, 37533, 37534, 37535, 37543, 37544, 37545, 37546), SingleValueConstraint(37553, 37554, 37555, 37556, 37564, 37566, 37567, 37568, 37572, 37574, 37575, 37576, 37580, 37582, 37583, 37584, 37600, 37602, 37603, 37604, 37610, 37612, 37613, 37614, 37771, 37773, 37774, 37775, 37779, 37781, 37782, 37783, 38022, 38032, 38044, 38054, 38064, 38086, 38096, 38106, 38128, 38138, 38148, 38158, 38311, 38313, 38314, 38315, 38349, 38351, 38352, 38353, 38357, 38359, 38360, 38361, 38470, 38471, 38472, 38473, 38557, 38559, 38560, 38561, 38624, 38626, 38627, 38628, 38678, 38680, 38681, 38682, 39082, 39084, 39085, 39086, 39090, 39092, 39093, 39094, 39107, 39109, 39110, 39111, 39115, 39117, 39118, 39119, 39123, 39125, 39126, 39127, 39131, 39133, 39134, 39135, 39139, 39141, 39142, 39143, 39166, 39168, 39169, 39170, 39174, 39176, 39177, 39178, 39182, 39184, 39185, 39186, 39190, 39192, 39193, 39194, 39200, 39202, 39203, 39204, 39208, 39210, 39211, 39212, 39216, 39218, 39219, 39220, 39227, 39229, 39230, 39231, 39235, 39237, 39238, 39239, 39243, 39245, 39246, 39247, 39251, 39253, 39254, 39255, 39259, 39261, 39262, 39263, 39267, 39269, 39270, 39271, 39583, 39649, 39658, 39667, 39676, 39685, 39702, 39711, 39720, 39729, 39794, 39796, 39797, 39798, 40092, 40094, 40095, 40096, 40100, 40102, 40103, 40104, 40108, 40110, 40111, 40112, 40116, 40118, 40119, 40120, 40124, 40126, 40127, 40128, 40441, 40443, 40444, 40445, 40449, 40451, 40452, 40453, 40457, 40459, 40460, 40461, 40583, 40585, 40586, 40587, 40591, 40593, 40594, 40595, 41016, 41018, 41019, 41020, 41024, 41026, 41027, 41028, 41032, 41034, 41035, 41036, 41049, 41050, 41051, 41052, 41059, 41060, 41061, 41062, 41069, 41070, 41071, 41072, 41079, 41080, 41081, 41082, 41089, 41090, 41091, 41092, 41099, 41100, 41101, 41102, 41109, 41110, 41111, 41112, 41119, 41120, 41121, 41122, 77845, 77846, 77847, 77848, 77958), SingleValueConstraint(77959, 77960, 77973, 77974, 77975, 77979, 77990, 78016, 78017, 78019, 78020, 78021, 78022, 78040, 78041, 78044, 78045, 78046, 78074, 78075, 78076, 78077, 78081, 78090, 78091, 78093, 78094, 78095, 78096, 78097, 78110, 78113, 78114, 78119, 78120, 78121, 78122, 78123, 78124, 78182, 78185, 78189, 78190, 78243, 78255, 78263, 78292, 78297, 78298, 78319, 78320, 78321, 78338, 78344, 78346, 78360, 78361, 78362, 78364, 78365, 78366, 78367, 78368, 78369, 78370, 78371, 78372, 78374, 78375, 78378, 78379, 78380, 78381, 78382, 78383, 78384, 78385, 78390, 78404, 78405, 78413, 78414, 78415, 78416, 78417, 78418, 78419, 78420, 78421, 78422, 78423, 78424, 78426, 78427, 78428, 78431, 78432, 78433, 78434, 78435, 78440, 78441, 78442, 78447, 78448, 78452, 78453, 78454, 78457, 78458, 78483, 78484, 78485, 78486, 78490, 78491, 78492, 78493, 78500, 78501, 78523, 78524, 78529, 78556, 78573, 78574, 78603, 78609, 78610, 78627, 78630, 78632, 78635, 78636, 78647, 78654, 78663, 78679, 78694, 78699, 78702, 78711, 78721, 78722, 78765, 78766, 78779, 78780, 78788, 78789, 78790, 78807, 78821, 78822, 78823, 78824, 78839, 78840, 78842, 78843, 78844, 78845, 78846, 78847, 78848, 78849, 78850, 78851, 78852, 78853, 78854, 78855, 78856, 78858, 78859, 78860, 78865, 78866, 78867, 78868, 78885, 78916, 78917, 78918, 78923, 78925, 79039, 79041, 79042, 999445, 999446, 999447, 999448, 999558, 999559, 999560, 999573, 999574, 999575, 999579, 999590, 999616, 999617, 999619, 999620, 999621, 999622, 999640, 999641, 999644, 999645, 999646, 999674, 999675, 999676, 999677, 999681, 999690, 999691, 999693, 999694, 999695, 999696, 999697, 999710, 999713, 999714, 999719, 999720, 999721, 999722, 999723, 999724, 999782, 999785, 999789, 999790, 999843, 999855, 999863, 999892, 999897, 999898, 999919, 999920, 999921, 999938, 999944, 999946, 999960, 999961, 999962, 999964, 999965, 999966), SingleValueConstraint(999967, 999968, 999969, 999970, 999971, 999972, 999974, 999975, 999978, 999979, 999980, 999981, 999982, 999983, 999984, 999985, 999990, 1000004, 1000005, 1000013, 1000014, 1000015, 1000016, 1000017, 1000018, 1000019, 1000020, 1000021, 1000022, 1000023, 1000024, 1000026, 1000027, 1000028, 1000031, 1000032, 1000033, 1000034, 1000035, 1000040, 1000041, 1000042, 1000047, 1000048, 1000052, 1000053, 1000054, 1000057, 1000058, 1000083, 1000084, 1000085, 1000086, 1000090, 1000091, 1000092, 1000093, 1000100, 1000101, 1000123, 1000124, 1000129, 1000156, 1000173, 1000174, 1000203, 1000209, 1000210, 1000227, 1000230, 1000232, 1000235, 1000236, 1000247, 1000254, 1000263, 1000279, 1000294, 1000299, 1000302, 1000311, 1000321, 1000322, 1000365, 1000366, 1000379, 1000380, 1000388, 1000389, 1000390, 1000407, 1000421, 1000422, 1000423, 1000424, 1000439, 1000440, 1000442, 1000443, 1000444, 1000445, 1000446, 1000447, 1000448, 1000449, 1000450, 1000451, 1000452, 1000453, 1000454, 1000455, 1000456, 1000458, 1000459, 1000460, 1000465, 1000466, 1000467, 1000468, 1000485, 1000516, 1000517, 1000518, 1000523, 1000525, 1000639, 1000641, 1000642, 4522530, 4522532, 4522544, 4522556, 4522561, 4522588, 4522603, 4525234, 4525239, 4525240, 4525241, 4525247, 4525248, 4525250, 4525251, 4525252, 4525253, 4525254, 4526517, 4526850, 4526851, 4526901, 4526902, 4527601, 4528591, 4528596, 4528609, 4528611, 4528613, 4528616, 4528618, 4528620, 4528623, 4528625, 4528627, 4528680, 4528682, 4528842, 4529444, 4529447, 4529601, 4529604, 4529606, 4529615, 4529838, 4529847, 4529849, 4529971, 4529973, 4530050, 4530085, 4530100, 4530109, 4530112, 4530114, 4530117, 4530119, 4530121, 4530139, 4530389, 4530391, 4530407, 4531275))
    namedValues = NamedValues(("generic", 0), ("fabricComputeSlotEpMisplacedInChassisSlot", 156), ("fabricComputeSlotEpServerIdentificationProblem", 157), ("vnicEtherConfigFailed", 169), ("vnicFcConfigFailed", 170), ("processorUnitInoperable", 174), ("processorUnitThermalNonCritical", 175), ("processorUnitThermalThresholdCritical", 176), ("processorUnitThermalThresholdNonRecoverable", 177), ("processorUnitVoltageThresholdNonCritical", 178), ("processorUnitVoltageThresholdCritical", 179), ("processorUnitVoltageThresholdNonRecoverable", 180), ("storageLocalDiskInoperable", 181), ("storageItemCapacityExceeded", 182), ("storageItemCapacityWarning", 183), ("memoryUnitDegraded", 184), ("memoryUnitInoperable", 185), ("memoryUnitThermalThresholdNonCritical", 186), ("memoryUnitThermalThresholdCritical", 187), ("memoryUnitThermalThresholdNonRecoverable", 188), ("memoryArrayVoltageThresholdNonCritical", 189), ("memoryArrayVoltageThresholdCritical", 190), ("memoryArrayVoltageThresholdNonRecoverable", 191), ("adaptorUnitUnidentifiableFru", 200), ("adaptorUnitMissing", 203), ("adaptorUnitAdaptorReachability", 206), ("adaptorHostIfLinkDown", 207), ("adaptorExtIfLinkDown", 209), ("portPioLinkDown", 276), ("portPioFailed", 277), ("portPioHardwareFailure", 278), ("portPioSfpNotPresent", 279), ("fabricExternalPcDown", 282), ("dcxVcDown", 283), ("networkElementInoperable", 291), ("mgmtEntityDegraded", 293), ("mgmtEntityDown", 294), ("dcxNsFailed", 304), ("computePhysicalInsufficientlyEquipped", 305), ("computePhysicalIdentityUnestablishable", 306), ("computeBoardPowerError", 310), ("computePhysicalPowerProblem", 311), ("computePhysicalThermalProblem", 312), ("computePhysicalBiosPostTimeout", 313), ("computePhysicalDiscoveryFailed", 314), ("computePhysicalAssociationFailed", 315), ("computePhysicalInoperable", 317), ("computePhysicalUnassignedMissing", 318), ("computePhysicalAssignedMissing", 319), ("computePhysicalUnidentified", 320), ("computePhysicalUnassignedInaccessible", 321), ("computePhysicalAssignedInaccessible", 322), ("lsServerFailed", 324), ("lsServerDiscoveryFailed", 326), ("lsServerConfigFailure", 327), ("lsServerMaintenanceFailed", 329), ("lsServerRemoved", 330), ("lsServerInaccessible", 331), ("lsServerAssociationFailed", 332), ("lsServerUnassociated", 334), ("lsServerServerUnfulfilled", 337), ("etherSwitchIntfioSatelliteConnectionAbsent", 367), ("etherSwitchIntfioSatelliteWiringProblem", 368), ("equipmentPsuPowerSupplyProblem", 369), ("equipmentFanDegraded", 371), ("equipmentFanInoperable", 373), ("equipmentPsuInoperable", 374), ("equipmentIocardRemoved", 376), ("equipmentFanModuleMissing", 377), ("equipmentPsuMissing", 378), ("equipmentIocardThermalProblem", 379), ("equipmentFanModuleThermalThresholdNonCritical", 380), ("equipmentPsuThermalThresholdNonCritical", 381), ("equipmentFanModuleThermalThresholdCritical", 382), ("equipmentPsuThermalThresholdCritical", 383), ("equipmentFanModuleThermalThresholdNonRecoverable", 384), ("equipmentPsuThermalThresholdNonRecoverable", 385), ("equipmentPsuVoltageThresholdNonCritical", 387), ("equipmentPsuVoltageThresholdCritical", 389), ("equipmentPsuVoltageThresholdNonRecoverable", 391), ("equipmentPsuPerfThresholdNonCritical", 392), ("equipmentPsuPerfThresholdCritical", 393), ("equipmentPsuPerfThresholdNonRecoverable", 394), ("equipmentFanPerfThresholdNonCritical", 395), ("equipmentFanPerfThresholdCritical", 396), ("equipmentFanPerfThresholdNonRecoverable", 397), ("equipmentIocardFirmwareUpgrade", 398), ("equipmentChassisUnsupportedConnectivity", 399), ("equipmentChassisUnacknowledged", 400), ("equipmentIocardUnsupportedConnectivity", 401), ("equipmentIocardUnacknowledged", 402), ("equipmentIocardPeerDisconnected", 403), ("equipmentChassisIdentity", 404), ("equipmentIocardIdentity", 405), ("equipmentFanModuleIdentity", 406), ("equipmentPsuIdentity", 407), ("equipmentChassisPowerProblem", 408), ("equipmentChassisThermalThresholdCritical", 409), ("equipmentChassisThermalThresholdNonCritical", 410), ("equipmentChassisThermalThresholdNonRecoverable", 411), ("computeBoardCmosVoltageThresholdCritical", 424), ("computeBoardCmosVoltageThresholdNonRecoverable", 425), ("mgmtEntityElectionFailure", 428), ("mgmtEntityHaNotReady", 429), ("mgmtEntityVersionIncompatible", 430), ("equipmentFanMissing", 434), ("equipmentIocardAutoUpgradingFirmware", 435), ("firmwarePackItemImageMissing", 436), ("etherSwitchIntfioSatelliteWiringNumbersUnexpected", 440), ("mgmtEntityManagementServicesFailure", 451), ("mgmtEntityManagementServicesUnresponsive", 452), ("mgmtEntityDevice1SharedStorageError", 453), ("mgmtEntityDevice2SharedStorageError", 454), ("mgmtEntityDevice3SharedStorageError", 455), ("equipmentChassisInoperable", 456), ("etherServerIntfioHardwareFailure", 458), ("dcxVcMgmtVifDown", 459), ("sysdebugMepLogMEpLogLog", 460), ("sysdebugMepLogMEpLogVeryLow", 461), ("sysdebugMepLogMEpLogFull", 462), ("computePoolEmpty", 463), ("uuidpoolPoolEmpty", 464), ("ippoolPoolEmpty", 465), ("macpoolPoolEmpty", 466), ("firmwareUpdatableImageUnusable", 470), ("firmwareBootUnitCantBoot", 471), ("fcpoolInitiatorsEmpty", 476), ("equipmentIocardInaccessible", 478), ("dcxVifLinkState", 479), ("equipmentFanModuleDegraded", 480), ("equipmentIocardPostFailure", 481), ("equipmentFanPerfThresholdLowerNonRecoverable", 484), ("memoryUnitIdentityUnestablishable", 502), ("computePhysicalPostFailure", 517), ("equipmentPsuOffline", 528), ("sysdebugMepLogTransferError", 530), ("storageRaidBatteryInoperable", 560), ("computeRtcBatteryInoperable", 561), ("memoryBufferUnitThermalThresholdNonCritical", 577), ("memoryBufferUnitThermalThresholdCritical", 578), ("memoryBufferUnitThermalThresholdNonRecoverable", 579), ("computeIohubThermalNonCritical", 582), ("computeIohubThermalThresholdCritical", 583), ("computeIohubThermalThresholdNonRecoverable", 584), ("equipmentChassisIdentityUnestablishable", 587), ("licenseInstanceGracePeriodWarning1", 591), ("licenseInstanceGracePeriodWarning2", 592), ("licenseInstanceGracePeriodWarning3", 593), ("licenseInstanceGracePeriodWarning4", 594), ("licenseInstanceGracePeriodWarning5", 595), ("licenseInstanceGracePeriodWarning6", 596), ("licenseInstanceGracePeriodWarning7", 597), ("licenseFileBadLicenseFile", 598), ("licenseFileFileNotDeleted", 599), ("fabricLanPinGroupEmpty", 621), ("fabricSanPinGroupEmpty", 622), ("adaptorExtEthIfMisConnect", 625), ("swVlanPortNsResourceStatus", 635), ("fabricVlanPrimaryVlanMissingIsolated", 646), ("mgmtIfMisConnect", 654), ("adaptorHostEthIfMisConnect", 656), ("equipmentFexPostFailure", 669), ("equipmentFexIdentity", 670), ("powerBudgetPowerBudgetCmcProblem", 688), ("lsComputeBindingAssignmentRequirementsNotMet", 689), ("powerBudgetPowerBudgetBmcProblem", 690), ("powerBudgetPowerBudgetDiscFail", 693), ("powerGroupPowerGroupInsufficientBudget", 695), ("powerGroupPowerGroupBudgetIncorrect", 696), ("adaptorHostEthIfMissing", 708), ("portPioInvalidSfp", 710), ("mgmtIfMissing", 714), ("fabricEthLanPcEpDown", 727), ("fabricFcSanPcEpDown", 728), ("equipmentIocardThermalThresholdNonCritical", 729), ("equipmentIocardThermalThresholdCritical", 730), ("equipmentIocardThermalThresholdNonRecoverable", 731), ("equipmentChassisSeepromInoperable", 733), ("fabricFcSanPcEpIncompatibleSpeed", 734), ("fabricFcSanPcIncompatibleSpeed", 735), ("extmgmtIfMgmtifdown", 736), ("powerChassisMemberPowerGroupCapInsufficient", 740), ("powerChassisMemberChassisFirmwareProblem", 741), ("powerChassisMemberChassisPsuInsufficient", 742), ("powerChassisMemberChassisPsuRedundanceFailure", 743), ("powerBudgetPowerCapReachedCommit", 744), ("sysdebugAutoCoreFileExportTargetAutoCoreTransferFailure", 747), ("fabricMonSpanConfigFail", 757), ("powerBudgetChassisPsuInsufficient", 764), ("powerBudgetTstateTransition", 765), ("powerPolicyPowerPolicyApplicationFail", 766), ("mgmtIfNew", 772), ("adaptorExtEthIfMissing", 775), ("storageLocalDiskSlotEpUnusable", 776), ("fabricEthEstcPcEpDown", 777), ("equipmentFexIdentityUnestablishable", 778), ("mgmtEntityDevice1SeepromError", 791), ("mgmtEntityDevice2SeepromError", 792), ("mgmtEntityDevice3SeepromError", 793), ("equipmentFanModuleInoperable", 794), ("lsmaintMaintPolicyUnresolvableScheduler", 795), ("fabricVsanErrorDisabled", 796), ("fabricVsanEpErrorDisabled", 797), ("powerBudgetFirmwareMismatch", 798), ("processorUnitIdentityUnestablishable", 801), ("firmwareBootUnitActivateStatusFailed", 807), ("fabricDceSwSrvPcEpDown", 826), ("fabricInternalPcDown", 829), ("fabricEpMgrEpTransModeFail", 837), ("mgmtPmonEntryUcsmProcessFailure", 846), ("processorUnitDisabled", 855), ("computeBoardThermalProblem", 857), ("equipmentPsuPowerSupplyShutdown", 859), ("iqnpoolPoolEmpty", 861), ("fabricVlanMisconfigured", 862), ("swEthLanEpMissingPrimaryVlan", 865), ("swEthLanPcMissingPrimaryVlan", 866), ("memoryUnitDisabled", 867), ("vmVifLinkState", 872), ("mgmtEntityHaSshKeysMismatched", 874), ("vnicEtherPinningMismatch", 875), ("vnicEtherPinningMisconfig", 876), ("storageLocalLunInoperable", 877), ("equipmentPsuPowerThreshold", 878), ("equipmentPsuInputError", 879), ("fabricPioEpErrorMisconfigured", 880), ("networkElementInventoryFailed", 885), ("computeBoardPowerFail", 887), ("equipmentSwitchCardPowerOff", 890), ("adaptorUnitExtnUnidentifiableFru", 900), ("adaptorUnitExtnMissing", 901), ("equipmentFexFexUnsupported", 902), ("vnicIscsiConfigFailed", 903), ("pkiKeyRingStatus", 909), ("pkiTpStatus", 910), ("computePhysicalDisassociationFailed", 915), ("computePhysicalNetworkMisconfigured", 916), ("vnicProfileProfileConfigIncorrect", 917), ("computeBoardMotherBoardVoltageThresholdUpperNonRecoverable", 918), ("computeBoardMotherBoardVoltageThresholdLowerNonRecoverable", 919), ("computeBoardMotherBoardVoltageUpperThresholdCritical", 920), ("computeBoardMotherBoardVoltageLowerThresholdCritical", 921), ("networkElementThermalThresholdCritical", 928), ("aaaProviderGroupProvidergroup", 943), ("aaaConfigServergroup", 944), ("aaaRoleRoleNotDeployed", 945), ("aaaLocaleLocaleNotDeployed", 946), ("aaaUserRoleUserRoleNotDeployed", 947), ("aaaUserLocaleUserLocaleNotDeployed", 948), ("pkiKeyRingKeyRingNotDeployed", 949), ("commSnmpSyscontactEmpty", 950), ("commDateTimeCommTimeZoneInvalid", 951), ("aaaUserLocalUserNotDeployed", 952), ("commSnmpUserSnmpUserNotDeployed", 953), ("commSvcEpCommSvcNotDeployed", 954)) + NamedValues(("mgmtConnectionDisabled", 957), ("mgmtConnectionUnused", 958), ("mgmtConnectionUnsupportedConnectivity", 959), ("capabilityCatalogueLoadErrors", 967), ("storageLocalDiskDegraded", 968), ("storageRaidBatteryDegraded", 969), ("storageRaidBatteryRelearnAborted", 970), ("storageRaidBatteryRelearnFailed", 971), ("storageAdefConfigurationError", 972), ("storageInitiatorConfigurationError", 973), ("storageVsanRefVsanUnresolvable", 974), ("storageControllerPatrolReadFailed", 975), ("storageControllerInoperable", 976), ("storageLocalDiskRebuildFailed", 977), ("storageLocalDiskCopybackFailed", 978), ("storageVirtualDriveInoperable", 979), ("storageVirtualDriveDegraded", 980), ("storageVirtualDriveReconstructionFailed", 981), ("storageVirtualDriveConsistencyCheckFailed", 982), ("extpolClientClientLostConnectivity", 1010), ("policyControlEpSuspendModeActive", 1017), ("extmgmtArpTargetsArpTargetsNotValid", 1037), ("fabricFcoeSanPcEpDown", 1046), ("fabricFcoeSanEpDown", 1047), ("fabricFcoeSanEpUnsupported", 1048), ("fabricFcoeSanPcDown", 1049), ("fabricFcoeSanPcUnsupported", 1050), ("fabricFcoeEstcEpDown", 1051), ("fabricPinTargetDown", 1052), ("fabricExternalEpFcZoningEnable", 1053), ("fabricEthLanEpOverlappingVlan", 1054), ("fabricEthLanPcOverlappingVlan", 1055), ("fabricFcEstcEpFcStoragePortInvalid", 1056), ("fabricFcoeEstcEpFcoeStoragePortInvalid", 1057), ("fabricFcSanPcFcPortchannelMembersInvalid", 1058), ("computeBoardPowerUsageProblem", 1097), ("vnicEtherIfVlanAccessFault", 1101), ("vnicEtherIfVlanUnresolvable", 1102), ("vnicEtherIfInvalidVlan", 1103), ("fabricVlanVlanConflictPermit", 1104), ("fabricVlanReqVlanPermitUnresolved", 1105), ("fabricVlanGroupReqVlanGroupPermitUnresolved", 1106), ("swVlanPortNsVlancompNotSupport", 1202), ("fabricVlanMisconfiguredMcastPolicy", 1204), ("fabricVsanMembershipDown", 1206), ("callhomeEpNoSnmpPolicyForCallhome", 1207), ("aaaOrgLocaleOrgNotPresent", 1209), ("vnicFcPinningMisconfig", 1216), ("equipmentHealthLedCriticalError", 1219), ("equipmentHealthLedMinorError", 1220), ("networkOperLevelExtraprimaryvlans", 1221), ("extpolClientGracePeriodWarning", 1222), ("extpolClientGracePeriodWarning2", 1223), ("extpolClientGracePeriodWarning3", 1224), ("extpolClientGracePeriodWarning4", 1225), ("extpolClientGracePeriodWarning5", 1226), ("extpolClientGracePeriodWarning6", 1227), ("extpolClientGracePeriodWarning7", 1228), ("extpolClientGracePeriodWarning1", 1229), ("storageInitiatorDuplicateFcZone", 1232), ("storageIniGroupSwitchModeDisabled", 1233), ("storageItemFilesystemIssues", 1237), ("fsmSamDmeEquipmentiocardFePresence", 16405), ("fsmSamDmeEquipmentiocardFeConn", 16406), ("fsmSamDmeEquipmentChassisRemoveChassis", 16407), ("fsmSetLocatorLed", 16408), ("fsmSamDmeMgmtControllerExtMgmtIfConfig", 16518), ("fsmSamDmeFabricComputeSlotEpIdentify", 16519), ("fsmSamDmeComputeBladeDiscover", 16520), ("fsmSamDmeEquipmentChassisPsuPolicyConfig", 16533), ("fsmSamDmeAdaptorHostFcIfResetFcPersBinding", 16534), ("fsmSamDmeComputeBladeDiag", 16535), ("fsmSwitchMode", 16539), ("fsmSamDmeVnicProfileSetDeploy", 16550), ("fsmUpdateSvcEp", 16576), ("fsmSamDmeCommSvcEpRestartWebSvc", 16577), ("fsmUpdateEp", 16579), ("fsmUpdateRealm", 16580), ("fsmUpdateUserEp", 16581), ("fsmSamDmePkiEpUpdateEp", 16582), ("fsmSingle", 16600), ("fsmSamDmeSysfileMutationGlobal", 16601), ("fsmSamDmeSysdebugManualCoreFileExportTargetExport", 16604), ("fsmSamDmeSysdebugAutoCoreFileExportTargetConfigure", 16605), ("fsmSamDmeSysdebugLogControlEpLogControlPersist", 16606), ("fsmSamDmeSwAccessDomainDeploy", 16634), ("fsmSamDmeSwEthLanBorderDeploy", 16635), ("fsmSamDmeSwFcSanBorderDeploy", 16636), ("fsmSamDmeSwUtilityDomainDeploy", 16637), ("fsmSamDmeSyntheticFsObjCreate", 16641), ("fsmSamDmeFirmwareDownloaderDownload", 16650), ("fsmSamDmeFirmwareImageDelete", 16651), ("fsmUpdateSwitch", 16653), ("fsmUpdateiom", 16654), ("fsmSamDmeMgmtControllerActivateiom", 16655), ("fsmUpdatebmc", 16656), ("fsmSamDmeMgmtControllerActivatebmc", 16657), ("fsmSamDmeCallhomeEpConfigCallhome", 16670), ("fsmSwMgmtOobIfConfig", 16673), ("fsmSwMgmtInbandIfConfig", 16674), ("fsmVirtualIfConfig", 16679), ("fsmSamDmeMgmtIfEnableVip", 16680), ("fsmSamDmeMgmtIfDisableVip", 16681), ("fsmSamDmeMgmtIfEnableha", 16682), ("fsmSamDmeMgmtBackupBackup", 16683), ("fsmSamDmeMgmtImporterImport", 16684), ("fsmSamDmeStatsCollectionPolicyUpdateEp", 16742), ("fsmSamDmeQosclassDefinitionConfigGlobalQos", 16745), ("fsmSamDmeEpqosDefinitionDeploy", 16749), ("fsmSamDmeEpqosDefinitionDelTaskRemove", 16750), ("fsmSamDmeEquipmentiocardResetCmc", 16803), ("fsmUpdateucsmanager", 16815), ("fsmSysConfig", 16823), ("fsmSamDmeAdaptorExtEthIfPathReset", 16852), ("fsmSamDmeAdaptorHostEthIfCircuitReset", 16857), ("fsmSamDmeAdaptorHostFcIfCircuitReset", 16858), ("fsmSamDmeExtvmmProviderConfig", 16879), ("fsmSamDmeExtvmmKeyStoreCertInstall", 16880), ("fsmSamDmeExtvmmSwitchDelTaskRemoveProvider", 16881), ("fsmSamDmeExtvmmMasterExtKeyConfig", 16898), ("fsmUpdater", 16904), ("fsmSamDmeFirmwareDistributableDelete", 16906), ("fsmDiscover", 16920), ("fsmAssociate", 16921), ("fsmDisassociate", 16922), ("fsmDecommission", 16924), ("fsmSoftShutdown", 16925), ("fsmHardShutdown", 16926), ("fsmTurnup", 16927), ("fsmPowercycle", 16928), ("fsmHardreset", 16929), ("fsmSoftreset", 16930), ("fsmSwConnUpd", 16931), ("fsmBiosRecovery", 16932), ("fsmCmosReset", 16934), ("fsmResetBmc", 16935), ("fsmUpdateExtUsers", 16938), ("fsmUpdateAdaptor", 16939), ("fsmActivateAdaptor", 16940), ("fsmConfigSol", 16941), ("fsmUnconfigSol", 16942), ("fsmSetFeLocatorLed", 16943), ("fsmSamDmeEquipmentChassisPowerCap", 16944), ("fsmSamDmeEquipmentiocardMuxOffline", 16945), ("fsmPowerCap", 16950), ("fsmUpdateBoardController", 16964), ("fsmDeployCatalogue", 16965), ("fsmSamDmeComputePhysicalAssociate", 16973), ("fsmSamDmeComputePhysicalDisassociate", 16974), ("fsmSamDmeComputePhysicalPowerCap", 16975), ("fsmSamDmeComputePhysicalDecommission", 16976), ("fsmSamDmeComputePhysicalSoftShutdown", 16977), ("fsmSamDmeComputePhysicalHardShutdown", 16978), ("fsmSamDmeComputePhysicalTurnup", 16979), ("fsmSamDmeComputePhysicalPowercycle", 16980), ("fsmSamDmeComputePhysicalHardreset", 16981), ("fsmSamDmeComputePhysicalSoftreset", 16982), ("fsmSamDmeComputePhysicalSwConnUpd", 16983), ("fsmSamDmeComputePhysicalBiosRecovery", 16984), ("fsmSamDmeComputePhysicalCmosReset", 16986), ("fsmSamDmeComputePhysicalResetBmc", 16987), ("fsmSamDmeEquipmentiocardResetIom", 16988), ("fsmInstall", 16991), ("fsmClear", 16992), ("fsmUpdateFlexlm", 16993), ("fsmSamDmeComputeRackUnitDiscover", 16994), ("fsmSamDmeLsServerConfigure", 16995), ("fsmSamDmeSwEthMonDeploy", 17000), ("fsmSamDmeSwFcMonDeploy", 17001), ("fsmSamDmeFabricSanCloudSwitchMode", 17002), ("fsmRemoveFex", 17007), ("fsmSamDmeComputePhysicalUpdateExtUsers", 17008), ("fsmSamDmeSysdebugTechSupportInitiate", 17012), ("fsmSamDmeSysdebugTechSupportDeleteTechSupFile", 17013), ("fsmSamDmeSysdebugTechSupportDownload", 17014), ("fsmActivateCatalog", 17017), ("fsmActivateMgmtExt", 17018), ("fsmSamDmeComputePhysicalUpdateAdaptor", 17043), ("fsmSamDmeComputePhysicalActivateAdaptor", 17044), ("fsmSamDmeCapabilityCatalogueActivateCatalog", 17045), ("fsmSamDmeCapabilityMgmtExtensionActivateMgmtExt", 17046), ("fsmSamDmeLicenseDownloaderDownload", 17050), ("fsmSamDmeLicenseFileInstall", 17051), ("fsmSamDmeLicenseFileClear", 17052), ("fsmSamDmeLicenseInstanceUpdateFlexlm", 17053), ("fsmConfigure", 17060), ("fsmMuxOffline", 17061), ("fsmSamDmeComputePhysicalConfigSol", 17083), ("fsmSamDmeComputePhysicalUnconfigSol", 17084), ("fsmSamDmePortpioInCompatSfpPresence", 17089), ("fsmSamDmeComputePhysicalDiagnosticInterrupt", 17116), ("fsmSamDmeSysdebugCoreDownload", 17133), ("fsmSamDmeEquipmentChassisDynamicReallocation", 17134), ("fsmSamDmeComputePhysicalResetKvm", 17163), ("fsmSamDmeMgmtControllerOnline", 17169), ("fsmSamDmeComputeRackUnitOffline", 17170), ("fsmSamDmeEquipmentLocatorLedSetFiLocatorLed", 17187), ("fsmConfPhysical", 17190), ("fsmClusterRole", 17192), ("fsmIlluminate", 17195), ("fsmSetFiLocatorLed", 17196), ("fsmDeployAlias", 17207), ("fsmSamDmeFabricEpMgrConfigure", 17214), ("fsmSamDmeVnicProfileSetDeployAlias", 17223), ("fsmSamDmeSwPhysConfPhysical", 17239), ("fsmSamDmeExtvmmEpClusterRole", 17254), ("fsmSamDmeVmLifeCyclePolicyConfig", 17259), ("fsmSamDmeEquipmentBeaconLedIlluminate", 17262), ("fsmSamDmeEtherServerIntfioConfigSpeed", 17271), ("fsmUpdatebios", 17281), ("fsmSamDmeComputePhysicalActivatebios", 17282), ("fsmSamDmeFirmwareSystemDeploy", 17325), ("fsmSamDmeFirmwareSystemApplyCatalogPack", 17326), ("fsmSamDmeMgmtExportPolicyReportConfigCopy", 17339), ("fsmSamDmeMgmtImporterReportConfigImport", 17340), ("fsmSamDmeNfsMountInstMount", 17348), ("fsmSamDmeNfsMountInstUnmount", 17349), ("fsmSamDmeNfsMountDefReportNfsMountSuspend", 17350), ("fsmSamDmeStorageSystemSync", 17367), ("fsmSamDmeSwFcSanBorderActivateZoneSet", 17381), ("fsmSamDmeExtpolEpRegisterFsm", 17382), ("fsmSamDmeExtpolRegistryCrossDomainConfig", 17383), ("fsmSamDmeExtpolRegistryCrossDomainDelete", 17384), ("fsmSamDmeExtpolEpRepairCert", 17399), ("fsmSamDmePolicyControlEpOperate", 17400), ("fsmSamDmePolicyPolicyScopeReleasePolicyFsm", 17402), ("fsmSamDmePolicyPolicyScopeReleaseOperationFsm", 17403), ("fsmSamDmePolicyPolicyScopeReleaseStorageFsm", 17404), ("fsmSamDmePolicyPolicyScopeResolveManyPolicyFsm", 17405), ("fsmSamDmePolicyPolicyScopeResolveManyOperationFsm", 17406), ("fsmSamDmePolicyPolicyScopeResolveManyStorageFsm", 17407), ("fsmSamDmePolicyPolicyScopeReleaseManyPolicyFsm", 17408), ("fsmSamDmePolicyPolicyScopeReleaseManyOperationFsm", 17409), ("fsmSamDmePolicyPolicyScopeReleaseManyStorageFsm", 17410), ("fsmSamDmePolicyPolicyScopeResolveAllPolicyFsm", 17411), ("fsmSamDmePolicyPolicyScopeResolveAllOperationFsm", 17412), ("fsmSamDmePolicyPolicyScopeResolveAllStorageFsm", 17413), ("fsmSamDmePolicyPolicyScopeReleaseAllPolicyFsm", 17414), ("fsmSamDmePolicyPolicyScopeReleaseAllOperationFsm", 17415), ("fsmSamDmePolicyPolicyScopeReleaseAllStorageFsm", 17416), ("fsmSamDmeIdentIdentRequestUpdateIdent", 17418), ("fsmSamDmeIdentMetaSystemSync", 17419), ("fsmSamDmeMgmtControllerRegistryConfig", 17420), ("fsmSamDmeObserveObservedResolvePolicyFsm", 17425), ("fsmSamDmeObserveObservedResolveResourceFsm", 17426), ("fsmSamDmeObserveObservedResolvevmfsm", 17427), ("fsmSamDmeObserveObservedResolveControllerFsm", 17428), ("fsmSamDmePortpioInCompatSfpReplaced", 17445), ("fsmSamDmeComputePhysicalResetIpmi", 17476), ("fsmSamDmeComputePhysicalFwUpgrade", 17477), ("fsmSamDmeComputeRackUnitAdapterReset", 17478), ("fsmSamDmeComputeServerDiscPolicyResolveScrubPolicy", 17483), ("fsmSamDmeExtpolProviderReportConfigImport", 17485), ("fsmSamDmeFabricVnetEpSyncEpPushVnetEpDeletion", 17599), ("fsmSamDmeGmetaHolderInventory", 17601)) + NamedValues(("fsmSamDmeComputePhysicalCimcSessionDelete", 17602), ("tcaProcessorRuntimeLoad", 33142), ("tcaProcessorRuntimeLoadMin", 33144), ("tcaProcessorRuntimeLoadMax", 33145), ("tcaProcessorRuntimeLoadAvg", 33146), ("tcaFcStatsBytesRxDelta", 33167), ("tcaFcStatsBytesRxDeltaMin", 33168), ("tcaFcStatsBytesRxDeltaMax", 33169), ("tcaFcStatsBytesRxDeltaAvg", 33170), ("tcaFcStatsPacketsRxDelta", 33177), ("tcaFcStatsPacketsRxDeltaMin", 33178), ("tcaFcStatsPacketsRxDeltaMax", 33179), ("tcaFcStatsPacketsRxDeltaAvg", 33180), ("tcaFcStatsBytesTxDelta", 33187), ("tcaFcStatsBytesTxDeltaMin", 33188), ("tcaFcStatsBytesTxDeltaMax", 33189), ("tcaFcStatsBytesTxDeltaAvg", 33190), ("tcaFcStatsPacketsTxDelta", 33197), ("tcaFcStatsPacketsTxDeltaMin", 33198), ("tcaFcStatsPacketsTxDeltaMax", 33199), ("tcaFcStatsPacketsTxDeltaAvg", 33200), ("tcaFcErrStatsCrcRxDelta", 33211), ("tcaFcErrStatsCrcRxDeltaMin", 33212), ("tcaFcErrStatsCrcRxDeltaMax", 33213), ("tcaFcErrStatsCrcRxDeltaAvg", 33214), ("tcaFcErrStatsDiscardRxDelta", 33221), ("tcaFcErrStatsDiscardRxDeltaMin", 33222), ("tcaFcErrStatsDiscardRxDeltaMax", 33223), ("tcaFcErrStatsDiscardRxDeltaAvg", 33224), ("tcaFcErrStatsTooLongRxDelta", 33231), ("tcaFcErrStatsTooLongRxDeltaMin", 33232), ("tcaFcErrStatsTooLongRxDeltaMax", 33233), ("tcaFcErrStatsTooLongRxDeltaAvg", 33234), ("tcaFcErrStatsTooShortRxDelta", 33241), ("tcaFcErrStatsTooShortRxDeltaMin", 33242), ("tcaFcErrStatsTooShortRxDeltaMax", 33243), ("tcaFcErrStatsTooShortRxDeltaAvg", 33244), ("tcaFcErrStatsRxDelta", 33251), ("tcaFcErrStatsRxDeltaMin", 33252), ("tcaFcErrStatsRxDeltaMax", 33253), ("tcaFcErrStatsRxDeltaAvg", 33254), ("tcaFcErrStatsDiscardTxDelta", 33261), ("tcaFcErrStatsDiscardTxDeltaMin", 33262), ("tcaFcErrStatsDiscardTxDeltaMax", 33263), ("tcaFcErrStatsDiscardTxDeltaAvg", 33264), ("tcaFcErrStatsTxDelta", 33271), ("tcaFcErrStatsTxDeltaMin", 33272), ("tcaFcErrStatsTxDeltaMax", 33273), ("tcaFcErrStatsTxDeltaAvg", 33274), ("tcaFcErrStatsLinkFailuresDelta", 33281), ("tcaFcErrStatsLinkFailuresDeltaMin", 33282), ("tcaFcErrStatsLinkFailuresDeltaMax", 33283), ("tcaFcErrStatsLinkFailuresDeltaAvg", 33284), ("tcaFcErrStatsSyncLossesDelta", 33291), ("tcaFcErrStatsSyncLossesDeltaMin", 33292), ("tcaFcErrStatsSyncLossesDeltaMax", 33293), ("tcaFcErrStatsSyncLossesDeltaAvg", 33294), ("tcaFcErrStatsSignalLossesDelta", 33301), ("tcaFcErrStatsSignalLossesDeltaMin", 33302), ("tcaFcErrStatsSignalLossesDeltaMax", 33303), ("tcaFcErrStatsSignalLossesDeltaAvg", 33304), ("tcaMemoryRuntimeTotal", 33483), ("tcaMemoryRuntimeTotalMin", 33485), ("tcaMemoryRuntimeTotalMax", 33486), ("tcaMemoryRuntimeTotalAvg", 33487), ("tcaMemoryRuntimeAvailable", 33491), ("tcaMemoryRuntimeAvailableMin", 33493), ("tcaMemoryRuntimeAvailableMax", 33494), ("tcaMemoryRuntimeAvailableAvg", 33495), ("tcaMemoryRuntimeCached", 33499), ("tcaMemoryRuntimeCachedMin", 33501), ("tcaMemoryRuntimeCachedMax", 33502), ("tcaMemoryRuntimeCachedAvg", 33503), ("tcaAdaptorEthPortStatsTotalPacketsDelta", 33720), ("tcaAdaptorEthPortStatsTotalPacketsDeltaMin", 33721), ("tcaAdaptorEthPortStatsTotalPacketsDeltaMax", 33722), ("tcaAdaptorEthPortStatsTotalPacketsDeltaAvg", 33723), ("tcaAdaptorEthPortStatsGoodPacketsDelta", 33730), ("tcaAdaptorEthPortStatsGoodPacketsDeltaMin", 33731), ("tcaAdaptorEthPortStatsGoodPacketsDeltaMax", 33732), ("tcaAdaptorEthPortStatsGoodPacketsDeltaAvg", 33733), ("tcaAdaptorEthPortStatsVlanPacketsDelta", 33740), ("tcaAdaptorEthPortStatsVlanPacketsDeltaMin", 33741), ("tcaAdaptorEthPortStatsVlanPacketsDeltaMax", 33742), ("tcaAdaptorEthPortStatsVlanPacketsDeltaAvg", 33743), ("tcaAdaptorEthPortStatsPausePacketsDelta", 33750), ("tcaAdaptorEthPortStatsPausePacketsDeltaMin", 33751), ("tcaAdaptorEthPortStatsPausePacketsDeltaMax", 33752), ("tcaAdaptorEthPortStatsPausePacketsDeltaAvg", 33753), ("tcaAdaptorEthPortStatsPerPriorityPausePacketsDelta", 33760), ("tcaAdaptorEthPortStatsPerPriorityPausePacketsDeltaMin", 33761), ("tcaAdaptorEthPortStatsPerPriorityPausePacketsDeltaMax", 33762), ("tcaAdaptorEthPortStatsPerPriorityPausePacketsDeltaAvg", 33763), ("tcaAdaptorEthPortStatsPppPacketsDelta", 33770), ("tcaAdaptorEthPortStatsPppPacketsDeltaMin", 33771), ("tcaAdaptorEthPortStatsPppPacketsDeltaMax", 33772), ("tcaAdaptorEthPortStatsPppPacketsDeltaAvg", 33773), ("tcaAdaptorEthPortBySizeSmallStatsLessThan64Delta", 33810), ("tcaAdaptorEthPortBySizeSmallStatsLessThan64DeltaMin", 33811), ("tcaAdaptorEthPortBySizeSmallStatsLessThan64DeltaMax", 33812), ("tcaAdaptorEthPortBySizeSmallStatsLessThan64DeltaAvg", 33813), ("tcaAdaptorEthPortBySizeSmallStatsEquals64Delta", 33820), ("tcaAdaptorEthPortBySizeSmallStatsEquals64DeltaMin", 33821), ("tcaAdaptorEthPortBySizeSmallStatsEquals64DeltaMax", 33822), ("tcaAdaptorEthPortBySizeSmallStatsEquals64DeltaAvg", 33823), ("tcaAdaptorEthPortBySizeSmallStatsLessThan128Delta", 33830), ("tcaAdaptorEthPortBySizeSmallStatsLessThan128DeltaMin", 33831), ("tcaAdaptorEthPortBySizeSmallStatsLessThan128DeltaMax", 33832), ("tcaAdaptorEthPortBySizeSmallStatsLessThan128DeltaAvg", 33833), ("tcaAdaptorEthPortBySizeSmallStatsLessThan256Delta", 33840), ("tcaAdaptorEthPortBySizeSmallStatsLessThan256DeltaMin", 33841), ("tcaAdaptorEthPortBySizeSmallStatsLessThan256DeltaMax", 33842), ("tcaAdaptorEthPortBySizeSmallStatsLessThan256DeltaAvg", 33843), ("tcaAdaptorEthPortBySizeSmallStatsLessThan512Delta", 33850), ("tcaAdaptorEthPortBySizeSmallStatsLessThan512DeltaMin", 33851), ("tcaAdaptorEthPortBySizeSmallStatsLessThan512DeltaMax", 33852), ("tcaAdaptorEthPortBySizeSmallStatsLessThan512DeltaAvg", 33853), ("tcaAdaptorEthPortBySizeSmallStatsLessThan1024Delta", 33860), ("tcaAdaptorEthPortBySizeSmallStatsLessThan1024DeltaMin", 33861), ("tcaAdaptorEthPortBySizeSmallStatsLessThan1024DeltaMax", 33862), ("tcaAdaptorEthPortBySizeSmallStatsLessThan1024DeltaAvg", 33863), ("tcaAdaptorEthPortBySizeLargeStatsLessThanOrEqualTo1518Delta", 33875), ("tcaAdaptorEthPortBySizeLargeStatsLessThanOrEqualTo1518DeltaMin", 33876), ("tcaAdaptorEthPortBySizeLargeStatsLessThanOrEqualTo1518DeltaMax", 33877), ("tcaAdaptorEthPortBySizeLargeStatsLessThanOrEqualTo1518DeltaAvg", 33878), ("tcaAdaptorEthPortBySizeLargeStatsLessThan2048Delta", 33885), ("tcaAdaptorEthPortBySizeLargeStatsLessThan2048DeltaMin", 33886), ("tcaAdaptorEthPortBySizeLargeStatsLessThan2048DeltaMax", 33887), ("tcaAdaptorEthPortBySizeLargeStatsLessThan2048DeltaAvg", 33888), ("tcaAdaptorEthPortBySizeLargeStatsLessThan4096Delta", 33895), ("tcaAdaptorEthPortBySizeLargeStatsLessThan4096DeltaMin", 33896), ("tcaAdaptorEthPortBySizeLargeStatsLessThan4096DeltaMax", 33897), ("tcaAdaptorEthPortBySizeLargeStatsLessThan4096DeltaAvg", 33898), ("tcaAdaptorEthPortBySizeLargeStatsLessThan8192Delta", 33905), ("tcaAdaptorEthPortBySizeLargeStatsLessThan8192DeltaMin", 33906), ("tcaAdaptorEthPortBySizeLargeStatsLessThan8192DeltaMax", 33907), ("tcaAdaptorEthPortBySizeLargeStatsLessThan8192DeltaAvg", 33908), ("tcaAdaptorEthPortBySizeLargeStatsLessThan9216Delta", 33915), ("tcaAdaptorEthPortBySizeLargeStatsLessThan9216DeltaMin", 33916), ("tcaAdaptorEthPortBySizeLargeStatsLessThan9216DeltaMax", 33917), ("tcaAdaptorEthPortBySizeLargeStatsLessThan9216DeltaAvg", 33918), ("tcaAdaptorEthPortBySizeLargeStatsGreaterThanOrEqualTo9216Delta", 33925), ("tcaAdaptorEthPrtBySizeLargeStatsGreaterThanOrEqualTo9216DeltaMin", 33926), ("tcaAdaptorEthPrtBySizeLargeStatsGreaterThanOrEqualTo9216DeltaMax", 33927), ("tcaAdaptorEthPrtBySizeLargeStatsGreaterThanOrEqualTo9216DeltaAvg", 33928), ("tcaAdaptorEthPortOutsizedStatsOversizedPacketsDelta", 33940), ("tcaAdaptorEthPortOutsizedStatsOversizedPacketsDeltaMin", 33941), ("tcaAdaptorEthPortOutsizedStatsOversizedPacketsDeltaMax", 33942), ("tcaAdaptorEthPortOutsizedStatsOversizedPacketsDeltaAvg", 33943), ("tcaAdaptorEthPortOutsizedStatsOversizedGoodCrcPacketsDelta", 33950), ("tcaAdaptorEthPortOutsizedStatsOversizedGoodCrcPacketsDeltaMin", 33951), ("tcaAdaptorEthPortOutsizedStatsOversizedGoodCrcPacketsDeltaMax", 33952), ("tcaAdaptorEthPortOutsizedStatsOversizedGoodCrcPacketsDeltaAvg", 33953), ("tcaAdaptorEthPortOutsizedStatsOversizedBadCrcPacketsDelta", 33960), ("tcaAdaptorEthPortOutsizedStatsOversizedBadCrcPacketsDeltaMin", 33961), ("tcaAdaptorEthPortOutsizedStatsOversizedBadCrcPacketsDeltaMax", 33962), ("tcaAdaptorEthPortOutsizedStatsOversizedBadCrcPacketsDeltaAvg", 33963), ("tcaAdaptorEthPortOutsizedStatsUndersizedGoodCrcPacketsDelta", 33970), ("tcaAdaptorEthPortOutsizedStatsUndersizedGoodCrcPacketsDeltaMin", 33971), ("tcaAdaptorEthPortOutsizedStatsUndersizedGoodCrcPacketsDeltaMax", 33972), ("tcaAdaptorEthPortOutsizedStatsUndersizedGoodCrcPacketsDeltaAvg", 33973), ("tcaAdaptorEthPortOutsizedStatsUndersizedBadCrcPacketsDelta", 33980), ("tcaAdaptorEthPortOutsizedStatsUndersizedBadCrcPacketsDeltaMin", 33981), ("tcaAdaptorEthPortOutsizedStatsUndersizedBadCrcPacketsDeltaMax", 33982), ("tcaAdaptorEthPortOutsizedStatsUndersizedBadCrcPacketsDeltaAvg", 33983), ("tcaAdaptorEthPortMcastStatsUnicastPacketsDelta", 33995), ("tcaAdaptorEthPortMcastStatsUnicastPacketsDeltaMin", 33996), ("tcaAdaptorEthPortMcastStatsUnicastPacketsDeltaMax", 33997), ("tcaAdaptorEthPortMcastStatsUnicastPacketsDeltaAvg", 33998), ("tcaAdaptorEthPortMcastStatsMulticastPacketsDelta", 34005), ("tcaAdaptorEthPortMcastStatsMulticastPacketsDeltaMin", 34006), ("tcaAdaptorEthPortMcastStatsMulticastPacketsDeltaMax", 34007), ("tcaAdaptorEthPortMcastStatsMulticastPacketsDeltaAvg", 34008), ("tcaAdaptorEthPortMcastStatsBroadcastPacketsDelta", 34015), ("tcaAdaptorEthPortMcastStatsBroadcastPacketsDeltaMin", 34016), ("tcaAdaptorEthPortMcastStatsBroadcastPacketsDeltaMax", 34017), ("tcaAdaptorEthPortMcastStatsBroadcastPacketsDeltaAvg", 34018), ("tcaAdaptorEthPortErrStatsMacDiscardedPacketsDelta", 34030), ("tcaAdaptorEthPortErrStatsMacDiscardedPacketsDeltaMin", 34031), ("tcaAdaptorEthPortErrStatsMacDiscardedPacketsDeltaMax", 34032), ("tcaAdaptorEthPortErrStatsMacDiscardedPacketsDeltaAvg", 34033), ("tcaAdaptorEthPortErrStatsBadCrcPacketsDelta", 34040), ("tcaAdaptorEthPortErrStatsBadCrcPacketsDeltaMin", 34041), ("tcaAdaptorEthPortErrStatsBadCrcPacketsDeltaMax", 34042), ("tcaAdaptorEthPortErrStatsBadCrcPacketsDeltaAvg", 34043), ("tcaAdaptorEthPortErrStatsBadLengthPacketsDelta", 34050), ("tcaAdaptorEthPortErrStatsBadLengthPacketsDeltaMin", 34051), ("tcaAdaptorEthPortErrStatsBadLengthPacketsDeltaMax", 34052), ("tcaAdaptorEthPortErrStatsBadLengthPacketsDeltaAvg", 34053), ("tcaAdaptorFcPortStatsRxFramesDelta", 34064), ("tcaAdaptorFcPortStatsRxFramesDeltaMin", 34065), ("tcaAdaptorFcPortStatsRxFramesDeltaMax", 34066), ("tcaAdaptorFcPortStatsRxFramesDeltaAvg", 34067), ("tcaAdaptorFcPortStatsTxFramesDelta", 34074), ("tcaAdaptorFcPortStatsTxFramesDeltaMin", 34075), ("tcaAdaptorFcPortStatsTxFramesDeltaMax", 34076), ("tcaAdaptorFcPortStatsTxFramesDeltaAvg", 34077), ("tcaAdaptorFcPortStatsRxBadFramesDelta", 34084), ("tcaAdaptorFcPortStatsRxBadFramesDeltaMin", 34085), ("tcaAdaptorFcPortStatsRxBadFramesDeltaMax", 34086), ("tcaAdaptorFcPortStatsRxBadFramesDeltaAvg", 34087), ("tcaAdaptorFcPortStatsTxBadFramesDelta", 34094), ("tcaAdaptorFcPortStatsTxBadFramesDeltaMin", 34095), ("tcaAdaptorFcPortStatsTxBadFramesDeltaMax", 34096), ("tcaAdaptorFcPortStatsTxBadFramesDeltaAvg", 34097), ("tcaAdaptorVnicStatsPacketsTxDelta", 34108), ("tcaAdaptorVnicStatsPacketsTxDeltaMin", 34109), ("tcaAdaptorVnicStatsPacketsTxDeltaMax", 34110), ("tcaAdaptorVnicStatsPacketsTxDeltaAvg", 34111), ("tcaAdaptorVnicStatsPacketsRxDelta", 34118), ("tcaAdaptorVnicStatsPacketsRxDeltaMin", 34119), ("tcaAdaptorVnicStatsPacketsRxDeltaMax", 34120), ("tcaAdaptorVnicStatsPacketsRxDeltaAvg", 34121), ("tcaAdaptorVnicStatsBytesTxDelta", 34128), ("tcaAdaptorVnicStatsBytesTxDeltaMin", 34129), ("tcaAdaptorVnicStatsBytesTxDeltaMax", 34130), ("tcaAdaptorVnicStatsBytesTxDeltaAvg", 34131), ("tcaAdaptorVnicStatsBytesRxDelta", 34138), ("tcaAdaptorVnicStatsBytesRxDeltaMin", 34139), ("tcaAdaptorVnicStatsBytesRxDeltaMax", 34140), ("tcaAdaptorVnicStatsBytesRxDeltaAvg", 34141), ("tcaAdaptorVnicStatsErrorsTxDelta", 34148), ("tcaAdaptorVnicStatsErrorsTxDeltaMin", 34149), ("tcaAdaptorVnicStatsErrorsTxDeltaMax", 34150), ("tcaAdaptorVnicStatsErrorsTxDeltaAvg", 34151), ("tcaAdaptorVnicStatsErrorsRxDelta", 34158), ("tcaAdaptorVnicStatsErrorsRxDeltaMin", 34159), ("tcaAdaptorVnicStatsErrorsRxDeltaMax", 34160), ("tcaAdaptorVnicStatsErrorsRxDeltaAvg", 34161), ("tcaAdaptorVnicStatsDroppedTxDelta", 34168), ("tcaAdaptorVnicStatsDroppedTxDeltaMin", 34169), ("tcaAdaptorVnicStatsDroppedTxDeltaMax", 34170), ("tcaAdaptorVnicStatsDroppedTxDeltaAvg", 34171), ("tcaAdaptorVnicStatsDroppedRxDelta", 34178), ("tcaAdaptorVnicStatsDroppedRxDeltaMin", 34179), ("tcaAdaptorVnicStatsDroppedRxDeltaMax", 34180), ("tcaAdaptorVnicStatsDroppedRxDeltaAvg", 34181), ("tcaAdaptorFcIffc4StatsInputRequestsDelta", 34192), ("tcaAdaptorFcIffc4StatsInputRequestsDeltaMin", 34193), ("tcaAdaptorFcIffc4StatsInputRequestsDeltaMax", 34194), ("tcaAdaptorFcIffc4StatsInputRequestsDeltaAvg", 34195), ("tcaAdaptorFcIffc4StatsOutputRequestsDelta", 34202), ("tcaAdaptorFcIffc4StatsOutputRequestsDeltaMin", 34203), ("tcaAdaptorFcIffc4StatsOutputRequestsDeltaMax", 34204), ("tcaAdaptorFcIffc4StatsOutputRequestsDeltaAvg", 34205), ("tcaAdaptorFcIffc4StatsControlRequestsDelta", 34212), ("tcaAdaptorFcIffc4StatsControlRequestsDeltaMin", 34213), ("tcaAdaptorFcIffc4StatsControlRequestsDeltaMax", 34214), ("tcaAdaptorFcIffc4StatsControlRequestsDeltaAvg", 34215), ("tcaAdaptorFcIffc4StatsInputMegabytesDelta", 34222), ("tcaAdaptorFcIffc4StatsInputMegabytesDeltaMin", 34223), ("tcaAdaptorFcIffc4StatsInputMegabytesDeltaMax", 34224), ("tcaAdaptorFcIffc4StatsInputMegabytesDeltaAvg", 34225), ("tcaAdaptorFcIffc4StatsOutputMegabytesDelta", 34232), ("tcaAdaptorFcIffc4StatsOutputMegabytesDeltaMin", 34233)) + NamedValues(("tcaAdaptorFcIffc4StatsOutputMegabytesDeltaMax", 34234), ("tcaAdaptorFcIffc4StatsOutputMegabytesDeltaAvg", 34235), ("tcaAdaptorMenloBaseErrorStatsCorrectableErrorsDelta", 34246), ("tcaAdaptorMenloBaseErrorStatsCorrectableErrorsDeltaMin", 34247), ("tcaAdaptorMenloBaseErrorStatsCorrectableErrorsDeltaMax", 34248), ("tcaAdaptorMenloBaseErrorStatsCorrectableErrorsDeltaAvg", 34249), ("tcaAdaptorMenloBaseErrorStatsUncorrectableErrorsDelta", 34256), ("tcaAdaptorMenloBaseErrorStatsUncorrectableErrorsDeltaMin", 34257), ("tcaAdaptorMenloBaseErrorStatsUncorrectableErrorsDeltaMax", 34258), ("tcaAdaptorMenloBaseErrorStatsUncorrectableErrorsDeltaAvg", 34259), ("tcaAdaptorMenloMcpuStatsDropAclDelta", 34271), ("tcaAdaptorMenloMcpuStatsDropAclDeltaMin", 34272), ("tcaAdaptorMenloMcpuStatsDropAclDeltaMax", 34273), ("tcaAdaptorMenloMcpuStatsDropAclDeltaAvg", 34274), ("tcaAdaptorMenloMcpuStatsDropOverrunDelta", 34281), ("tcaAdaptorMenloMcpuStatsDropOverrunDeltaMin", 34282), ("tcaAdaptorMenloMcpuStatsDropOverrunDeltaMax", 34283), ("tcaAdaptorMenloMcpuStatsDropOverrunDeltaAvg", 34284), ("tcaAdaptorMenloMcpuStatsDropRuntDelta", 34291), ("tcaAdaptorMenloMcpuStatsDropRuntDeltaMin", 34292), ("tcaAdaptorMenloMcpuStatsDropRuntDeltaMax", 34293), ("tcaAdaptorMenloMcpuStatsDropRuntDeltaAvg", 34294), ("tcaAdaptorMenloMcpuStatsTruncateOverrunDelta", 34301), ("tcaAdaptorMenloMcpuStatsTruncateOverrunDeltaMin", 34302), ("tcaAdaptorMenloMcpuStatsTruncateOverrunDeltaMax", 34303), ("tcaAdaptorMenloMcpuStatsTruncateOverrunDeltaAvg", 34304), ("tcaAdaptorMenloMcpuErrorStatsCorrectableErrorsDelta", 34316), ("tcaAdaptorMenloMcpuErrorStatsCorrectableErrorsDeltaMin", 34317), ("tcaAdaptorMenloMcpuErrorStatsCorrectableErrorsDeltaMax", 34318), ("tcaAdaptorMenloMcpuErrorStatsCorrectableErrorsDeltaAvg", 34319), ("tcaAdaptorMenloMcpuErrorStatsPopErrorsDelta", 34326), ("tcaAdaptorMenloMcpuErrorStatsPopErrorsDeltaMin", 34327), ("tcaAdaptorMenloMcpuErrorStatsPopErrorsDeltaMax", 34328), ("tcaAdaptorMenloMcpuErrorStatsPopErrorsDeltaAvg", 34329), ("tcaAdaptorMenloMcpuErrorStatsPushErrorsDelta", 34336), ("tcaAdaptorMenloMcpuErrorStatsPushErrorsDeltaMin", 34337), ("tcaAdaptorMenloMcpuErrorStatsPushErrorsDeltaMax", 34338), ("tcaAdaptorMenloMcpuErrorStatsPushErrorsDeltaAvg", 34339), ("tcaAdaptorMenloMcpuErrorStatsUncorrectableErrorsDelta", 34346), ("tcaAdaptorMenloMcpuErrorStatsUncorrectableErrorsDeltaMin", 34347), ("tcaAdaptorMenloMcpuErrorStatsUncorrectableErrorsDeltaMax", 34348), ("tcaAdaptorMenloMcpuErrorStatsUncorrectableErrorsDeltaAvg", 34349), ("tcaAdaptorMenloEthStatsDropOverrunDelta", 34361), ("tcaAdaptorMenloEthStatsDropOverrunDeltaMin", 34362), ("tcaAdaptorMenloEthStatsDropOverrunDeltaMax", 34363), ("tcaAdaptorMenloEthStatsDropOverrunDeltaAvg", 34364), ("tcaAdaptorMenloEthStatsDropRuntDelta", 34371), ("tcaAdaptorMenloEthStatsDropRuntDeltaMin", 34372), ("tcaAdaptorMenloEthStatsDropRuntDeltaMax", 34373), ("tcaAdaptorMenloEthStatsDropRuntDeltaAvg", 34374), ("tcaAdaptorMenloEthStatsTruncateOverrunDelta", 34381), ("tcaAdaptorMenloEthStatsTruncateOverrunDeltaMin", 34382), ("tcaAdaptorMenloEthStatsTruncateOverrunDeltaMax", 34383), ("tcaAdaptorMenloEthStatsTruncateOverrunDeltaAvg", 34384), ("tcaAdaptorMenloEthErrorStatsCorrectableErrorsDelta", 34396), ("tcaAdaptorMenloEthErrorStatsCorrectableErrorsDeltaMin", 34397), ("tcaAdaptorMenloEthErrorStatsCorrectableErrorsDeltaMax", 34398), ("tcaAdaptorMenloEthErrorStatsCorrectableErrorsDeltaAvg", 34399), ("tcaAdaptorMenloEthErrorStatsDropAclDelta", 34406), ("tcaAdaptorMenloEthErrorStatsDropAclDeltaMin", 34407), ("tcaAdaptorMenloEthErrorStatsDropAclDeltaMax", 34408), ("tcaAdaptorMenloEthErrorStatsDropAclDeltaAvg", 34409), ("tcaAdaptorMenloEthErrorStatsPopErrorsDelta", 34416), ("tcaAdaptorMenloEthErrorStatsPopErrorsDeltaMin", 34417), ("tcaAdaptorMenloEthErrorStatsPopErrorsDeltaMax", 34418), ("tcaAdaptorMenloEthErrorStatsPopErrorsDeltaAvg", 34419), ("tcaAdaptorMenloEthErrorStatsPushErrorsDelta", 34426), ("tcaAdaptorMenloEthErrorStatsPushErrorsDeltaMin", 34427), ("tcaAdaptorMenloEthErrorStatsPushErrorsDeltaMax", 34428), ("tcaAdaptorMenloEthErrorStatsPushErrorsDeltaAvg", 34429), ("tcaAdaptorMenloEthErrorStatsUncorrectableErrorsDelta", 34436), ("tcaAdaptorMenloEthErrorStatsUncorrectableErrorsDeltaMin", 34437), ("tcaAdaptorMenloEthErrorStatsUncorrectableErrorsDeltaMax", 34438), ("tcaAdaptorMenloEthErrorStatsUncorrectableErrorsDeltaAvg", 34439), ("tcaAdaptorMenloFcStatsDropAclDelta", 34451), ("tcaAdaptorMenloFcStatsDropAclDeltaMin", 34452), ("tcaAdaptorMenloFcStatsDropAclDeltaMax", 34453), ("tcaAdaptorMenloFcStatsDropAclDeltaAvg", 34454), ("tcaAdaptorMenloFcStatsDropOverrunDelta", 34461), ("tcaAdaptorMenloFcStatsDropOverrunDeltaMin", 34462), ("tcaAdaptorMenloFcStatsDropOverrunDeltaMax", 34463), ("tcaAdaptorMenloFcStatsDropOverrunDeltaAvg", 34464), ("tcaAdaptorMenloFcStatsDropRuntDelta", 34471), ("tcaAdaptorMenloFcStatsDropRuntDeltaMin", 34472), ("tcaAdaptorMenloFcStatsDropRuntDeltaMax", 34473), ("tcaAdaptorMenloFcStatsDropRuntDeltaAvg", 34474), ("tcaAdaptorMenloFcStatsTruncateOverrunDelta", 34481), ("tcaAdaptorMenloFcStatsTruncateOverrunDeltaMin", 34482), ("tcaAdaptorMenloFcStatsTruncateOverrunDeltaMax", 34483), ("tcaAdaptorMenloFcStatsTruncateOverrunDeltaAvg", 34484), ("tcaAdaptorMenloFcErrorStatsCorrectableErrorsDelta", 34496), ("tcaAdaptorMenloFcErrorStatsCorrectableErrorsDeltaMin", 34497), ("tcaAdaptorMenloFcErrorStatsCorrectableErrorsDeltaMax", 34498), ("tcaAdaptorMenloFcErrorStatsCorrectableErrorsDeltaAvg", 34499), ("tcaAdaptorMenloFcErrorStatsPopErrorsDelta", 34506), ("tcaAdaptorMenloFcErrorStatsPopErrorsDeltaMin", 34507), ("tcaAdaptorMenloFcErrorStatsPopErrorsDeltaMax", 34508), ("tcaAdaptorMenloFcErrorStatsPopErrorsDeltaAvg", 34509), ("tcaAdaptorMenloFcErrorStatsPushErrorsDelta", 34516), ("tcaAdaptorMenloFcErrorStatsPushErrorsDeltaMin", 34517), ("tcaAdaptorMenloFcErrorStatsPushErrorsDeltaMax", 34518), ("tcaAdaptorMenloFcErrorStatsPushErrorsDeltaAvg", 34519), ("tcaAdaptorMenloFcErrorStatsUncorrectableErrorsDelta", 34526), ("tcaAdaptorMenloFcErrorStatsUncorrectableErrorsDeltaMin", 34527), ("tcaAdaptorMenloFcErrorStatsUncorrectableErrorsDeltaMax", 34528), ("tcaAdaptorMenloFcErrorStatsUncorrectableErrorsDeltaAvg", 34529), ("tcaAdaptorMenloqstatsDropOverrunN0Delta", 34542), ("tcaAdaptorMenloqstatsDropOverrunN0DeltaMin", 34543), ("tcaAdaptorMenloqstatsDropOverrunN0DeltaMax", 34544), ("tcaAdaptorMenloqstatsDropOverrunN0DeltaAvg", 34545), ("tcaAdaptorMenloqstatsDropOverrunN1Delta", 34552), ("tcaAdaptorMenloqstatsDropOverrunN1DeltaMin", 34553), ("tcaAdaptorMenloqstatsDropOverrunN1DeltaMax", 34554), ("tcaAdaptorMenloqstatsDropOverrunN1DeltaAvg", 34555), ("tcaAdaptorMenloqstatsTruncateOverrunN0Delta", 34562), ("tcaAdaptorMenloqstatsTruncateOverrunN0DeltaMin", 34563), ("tcaAdaptorMenloqstatsTruncateOverrunN0DeltaMax", 34564), ("tcaAdaptorMenloqstatsTruncateOverrunN0DeltaAvg", 34565), ("tcaAdaptorMenloqstatsTruncateOverrunN1Delta", 34572), ("tcaAdaptorMenloqstatsTruncateOverrunN1DeltaMin", 34573), ("tcaAdaptorMenloqstatsTruncateOverrunN1DeltaMax", 34574), ("tcaAdaptorMenloqstatsTruncateOverrunN1DeltaAvg", 34575), ("tcaAdaptorMenloqerrorStatsCorrectableErrorsDelta", 34588), ("tcaAdaptorMenloqerrorStatsCorrectableErrorsDeltaMin", 34589), ("tcaAdaptorMenloqerrorStatsCorrectableErrorsDeltaMax", 34590), ("tcaAdaptorMenloqerrorStatsCorrectableErrorsDeltaAvg", 34591), ("tcaAdaptorMenloqerrorStatsPopErrorsDelta", 34598), ("tcaAdaptorMenloqerrorStatsPopErrorsDeltaMin", 34599), ("tcaAdaptorMenloqerrorStatsPopErrorsDeltaMax", 34600), ("tcaAdaptorMenloqerrorStatsPopErrorsDeltaAvg", 34601), ("tcaAdaptorMenloqerrorStatsPushErrorsDelta", 34608), ("tcaAdaptorMenloqerrorStatsPushErrorsDeltaMin", 34609), ("tcaAdaptorMenloqerrorStatsPushErrorsDeltaMax", 34610), ("tcaAdaptorMenloqerrorStatsPushErrorsDeltaAvg", 34611), ("tcaAdaptorMenloqerrorStatsUncorrectableErrorsDelta", 34618), ("tcaAdaptorMenloqerrorStatsUncorrectableErrorsDeltaMin", 34619), ("tcaAdaptorMenloqerrorStatsUncorrectableErrorsDeltaMax", 34620), ("tcaAdaptorMenloqerrorStatsUncorrectableErrorsDeltaAvg", 34621), ("tcaAdaptorMenloNetEgStatsLearnReqDropDelta", 34633), ("tcaAdaptorMenloNetEgStatsLearnReqDropDeltaMin", 34634), ("tcaAdaptorMenloNetEgStatsLearnReqDropDeltaMax", 34635), ("tcaAdaptorMenloNetEgStatsLearnReqDropDeltaAvg", 34636), ("tcaAdaptorMenloNetEgStatsDropCmdDelta", 34643), ("tcaAdaptorMenloNetEgStatsDropCmdDeltaMin", 34644), ("tcaAdaptorMenloNetEgStatsDropCmdDeltaMax", 34645), ("tcaAdaptorMenloNetEgStatsDropCmdDeltaAvg", 34646), ("tcaAdaptorMenloNetEgStatsDropLifCfgInvalidDelta", 34653), ("tcaAdaptorMenloNetEgStatsDropLifCfgInvalidDeltaMin", 34654), ("tcaAdaptorMenloNetEgStatsDropLifCfgInvalidDeltaMax", 34655), ("tcaAdaptorMenloNetEgStatsDropLifCfgInvalidDeltaAvg", 34656), ("tcaAdaptorMenloNetEgStatsDropLifMapNoHitDelta", 34663), ("tcaAdaptorMenloNetEgStatsDropLifMapNoHitDeltaMin", 34664), ("tcaAdaptorMenloNetEgStatsDropLifMapNoHitDeltaMax", 34665), ("tcaAdaptorMenloNetEgStatsDropLifMapNoHitDeltaAvg", 34666), ("tcaAdaptorMenloNetEgStatsDropSrcBindDelta", 34673), ("tcaAdaptorMenloNetEgStatsDropSrcBindDeltaMin", 34674), ("tcaAdaptorMenloNetEgStatsDropSrcBindDeltaMax", 34675), ("tcaAdaptorMenloNetEgStatsDropSrcBindDeltaAvg", 34676), ("tcaAdaptorMenloNetInStatsFwdLookupNoHitDelta", 34688), ("tcaAdaptorMenloNetInStatsFwdLookupNoHitDeltaMin", 34689), ("tcaAdaptorMenloNetInStatsFwdLookupNoHitDeltaMax", 34690), ("tcaAdaptorMenloNetInStatsFwdLookupNoHitDeltaAvg", 34691), ("tcaAdaptorMenloNetInStatsDropFcMulticastDelta", 34698), ("tcaAdaptorMenloNetInStatsDropFcMulticastDeltaMin", 34699), ("tcaAdaptorMenloNetInStatsDropFcMulticastDeltaMax", 34700), ("tcaAdaptorMenloNetInStatsDropFcMulticastDeltaAvg", 34701), ("tcaAdaptorMenloNetInStatsDropFcLifInvalidDelta", 34708), ("tcaAdaptorMenloNetInStatsDropFcLifInvalidDeltaMin", 34709), ("tcaAdaptorMenloNetInStatsDropFcLifInvalidDeltaMax", 34710), ("tcaAdaptorMenloNetInStatsDropFcLifInvalidDeltaAvg", 34711), ("tcaAdaptorMenloNetInStatsDropNullPifDelta", 34718), ("tcaAdaptorMenloNetInStatsDropNullPifDeltaMin", 34719), ("tcaAdaptorMenloNetInStatsDropNullPifDeltaMax", 34720), ("tcaAdaptorMenloNetInStatsDropNullPifDeltaAvg", 34721), ("tcaAdaptorMenloHostPortStatsRxPausecfcdelta", 34733), ("tcaAdaptorMenloHostPortStatsRxPausecfcdeltaMin", 34734), ("tcaAdaptorMenloHostPortStatsRxPausecfcdeltaMax", 34735), ("tcaAdaptorMenloHostPortStatsRxPausecfcdeltaAvg", 34736), ("tcaAdaptorMenloHostPortStatsRxPausepfcdelta", 34743), ("tcaAdaptorMenloHostPortStatsRxPausepfcdeltaMin", 34744), ("tcaAdaptorMenloHostPortStatsRxPausepfcdeltaMax", 34745), ("tcaAdaptorMenloHostPortStatsRxPausepfcdeltaAvg", 34746), ("tcaAdaptorMenloHostPortStatsTxPausecfcdelta", 34753), ("tcaAdaptorMenloHostPortStatsTxPausecfcdeltaMin", 34754), ("tcaAdaptorMenloHostPortStatsTxPausecfcdeltaMax", 34755), ("tcaAdaptorMenloHostPortStatsTxPausecfcdeltaAvg", 34756), ("tcaAdaptorMenloHostPortStatsTxPausepfcdelta", 34763), ("tcaAdaptorMenloHostPortStatsTxPausepfcdeltaMin", 34764), ("tcaAdaptorMenloHostPortStatsTxPausepfcdeltaMax", 34765), ("tcaAdaptorMenloHostPortStatsTxPausepfcdeltaAvg", 34766), ("tcaAdaptorMenloDcePortStatsRxPausecfcdelta", 34778), ("tcaAdaptorMenloDcePortStatsRxPausecfcdeltaMin", 34779), ("tcaAdaptorMenloDcePortStatsRxPausecfcdeltaMax", 34780), ("tcaAdaptorMenloDcePortStatsRxPausecfcdeltaAvg", 34781), ("tcaAdaptorMenloDcePortStatsRxPausepfcdelta", 34788), ("tcaAdaptorMenloDcePortStatsRxPausepfcdeltaMin", 34789), ("tcaAdaptorMenloDcePortStatsRxPausepfcdeltaMax", 34790), ("tcaAdaptorMenloDcePortStatsRxPausepfcdeltaAvg", 34791), ("tcaAdaptorMenloDcePortStatsTxPausecfcdelta", 34798), ("tcaAdaptorMenloDcePortStatsTxPausecfcdeltaMin", 34799), ("tcaAdaptorMenloDcePortStatsTxPausecfcdeltaMax", 34800), ("tcaAdaptorMenloDcePortStatsTxPausecfcdeltaAvg", 34801), ("tcaAdaptorMenloDcePortStatsTxPausepfcdelta", 34808), ("tcaAdaptorMenloDcePortStatsTxPausepfcdeltaMin", 34809), ("tcaAdaptorMenloDcePortStatsTxPausepfcdeltaMax", 34810), ("tcaAdaptorMenloDcePortStatsTxPausepfcdeltaAvg", 34811), ("tcaAdaptorEtherIfStatsTxBytesDelta", 34822), ("tcaAdaptorEtherIfStatsTxBytesDeltaMin", 34823), ("tcaAdaptorEtherIfStatsTxBytesDeltaMax", 34824), ("tcaAdaptorEtherIfStatsTxBytesDeltaAvg", 34825), ("tcaAdaptorEtherIfStatsTxPacketsDelta", 34832), ("tcaAdaptorEtherIfStatsTxPacketsDeltaMin", 34833), ("tcaAdaptorEtherIfStatsTxPacketsDeltaMax", 34834), ("tcaAdaptorEtherIfStatsTxPacketsDeltaAvg", 34835), ("tcaAdaptorEtherIfStatsTxErrorsDelta", 34842), ("tcaAdaptorEtherIfStatsTxErrorsDeltaMin", 34843), ("tcaAdaptorEtherIfStatsTxErrorsDeltaMax", 34844), ("tcaAdaptorEtherIfStatsTxErrorsDeltaAvg", 34845), ("tcaAdaptorEtherIfStatsTxDroppedDelta", 34852), ("tcaAdaptorEtherIfStatsTxDroppedDeltaMin", 34853), ("tcaAdaptorEtherIfStatsTxDroppedDeltaMax", 34854), ("tcaAdaptorEtherIfStatsTxDroppedDeltaAvg", 34855), ("tcaAdaptorEtherIfStatsRxBytesDelta", 34862), ("tcaAdaptorEtherIfStatsRxBytesDeltaMin", 34863), ("tcaAdaptorEtherIfStatsRxBytesDeltaMax", 34864), ("tcaAdaptorEtherIfStatsRxBytesDeltaAvg", 34865), ("tcaAdaptorEtherIfStatsRxPacketsDelta", 34872), ("tcaAdaptorEtherIfStatsRxPacketsDeltaMin", 34873), ("tcaAdaptorEtherIfStatsRxPacketsDeltaMax", 34874), ("tcaAdaptorEtherIfStatsRxPacketsDeltaAvg", 34875), ("tcaAdaptorEtherIfStatsRxErrorsDelta", 34882), ("tcaAdaptorEtherIfStatsRxErrorsDeltaMin", 34883), ("tcaAdaptorEtherIfStatsRxErrorsDeltaMax", 34884), ("tcaAdaptorEtherIfStatsRxErrorsDeltaAvg", 34885), ("tcaAdaptorEtherIfStatsRxDroppedDelta", 34892), ("tcaAdaptorEtherIfStatsRxDroppedDeltaMin", 34893), ("tcaAdaptorEtherIfStatsRxDroppedDeltaMax", 34894), ("tcaAdaptorEtherIfStatsRxDroppedDeltaAvg", 34895), ("tcaAdaptorFcIfFrameStatsTxFramesDelta", 34906), ("tcaAdaptorFcIfFrameStatsTxFramesDeltaMin", 34907), ("tcaAdaptorFcIfFrameStatsTxFramesDeltaMax", 34908), ("tcaAdaptorFcIfFrameStatsTxFramesDeltaAvg", 34909), ("tcaAdaptorFcIfFrameStatsRxFramesDelta", 34916), ("tcaAdaptorFcIfFrameStatsRxFramesDeltaMin", 34917), ("tcaAdaptorFcIfFrameStatsRxFramesDeltaMax", 34918), ("tcaAdaptorFcIfFrameStatsRxFramesDeltaAvg", 34919), ("tcaAdaptorFcIfFrameStatsErrorFramesDelta", 34926), ("tcaAdaptorFcIfFrameStatsErrorFramesDeltaMin", 34927), ("tcaAdaptorFcIfFrameStatsErrorFramesDeltaMax", 34928), ("tcaAdaptorFcIfFrameStatsErrorFramesDeltaAvg", 34929), ("tcaAdaptorFcIfFrameStatsDumpedFramesDelta", 34936), ("tcaAdaptorFcIfFrameStatsDumpedFramesDeltaMin", 34937), ("tcaAdaptorFcIfFrameStatsDumpedFramesDeltaMax", 34938), ("tcaAdaptorFcIfFrameStatsDumpedFramesDeltaAvg", 34939), ("tcaAdaptorFcIfEventStatsLipCountDelta", 34950)) + NamedValues(("tcaAdaptorFcIfEventStatsLipCountDeltaMin", 34951), ("tcaAdaptorFcIfEventStatsLipCountDeltaMax", 34952), ("tcaAdaptorFcIfEventStatsLipCountDeltaAvg", 34953), ("tcaAdaptorFcIfEventStatsInvalidcrccountDelta", 34960), ("tcaAdaptorFcIfEventStatsInvalidcrccountDeltaMin", 34961), ("tcaAdaptorFcIfEventStatsInvalidcrccountDeltaMax", 34962), ("tcaAdaptorFcIfEventStatsInvalidcrccountDeltaAvg", 34963), ("tcaAdaptorFcIfEventStatsNoscountDelta", 34970), ("tcaAdaptorFcIfEventStatsNoscountDeltaMin", 34971), ("tcaAdaptorFcIfEventStatsNoscountDeltaMax", 34972), ("tcaAdaptorFcIfEventStatsNoscountDeltaAvg", 34973), ("tcaAdaptorFcIfEventStatsLinkFailureCountDelta", 34980), ("tcaAdaptorFcIfEventStatsLinkFailureCountDeltaMin", 34981), ("tcaAdaptorFcIfEventStatsLinkFailureCountDeltaMax", 34982), ("tcaAdaptorFcIfEventStatsLinkFailureCountDeltaAvg", 34983), ("tcaAdaptorFcIfEventStatsLossOfSyncCountDelta", 34990), ("tcaAdaptorFcIfEventStatsLossOfSyncCountDeltaMin", 34991), ("tcaAdaptorFcIfEventStatsLossOfSyncCountDeltaMax", 34992), ("tcaAdaptorFcIfEventStatsLossOfSyncCountDeltaAvg", 34993), ("tcaAdaptorFcIfEventStatsLossOfSignalCountDelta", 35000), ("tcaAdaptorFcIfEventStatsLossOfSignalCountDeltaMin", 35001), ("tcaAdaptorFcIfEventStatsLossOfSignalCountDeltaMax", 35002), ("tcaAdaptorFcIfEventStatsLossOfSignalCountDeltaAvg", 35003), ("tcaAdaptorFcIfEventStatsSeqProtocolErrCountDelta", 35010), ("tcaAdaptorFcIfEventStatsSeqProtocolErrCountDeltaMin", 35011), ("tcaAdaptorFcIfEventStatsSeqProtocolErrCountDeltaMax", 35012), ("tcaAdaptorFcIfEventStatsSeqProtocolErrCountDeltaAvg", 35013), ("tcaAdaptorFcIfEventStatsSecondsSinceLastResetDelta", 35020), ("tcaAdaptorFcIfEventStatsSecondsSinceLastResetDeltaMin", 35021), ("tcaAdaptorFcIfEventStatsSecondsSinceLastResetDeltaMax", 35022), ("tcaAdaptorFcIfEventStatsSecondsSinceLastResetDeltaAvg", 35023), ("tcaSwEnvStatsMainBoardOutlet1", 35166), ("tcaSwEnvStatsMainBoardOutlet1Min", 35168), ("tcaSwEnvStatsMainBoardOutlet1Max", 35169), ("tcaSwEnvStatsMainBoardOutlet1Avg", 35170), ("tcaSwEnvStatsMainBoardOutlet2", 35174), ("tcaSwEnvStatsMainBoardOutlet2Min", 35176), ("tcaSwEnvStatsMainBoardOutlet2Max", 35177), ("tcaSwEnvStatsMainBoardOutlet2Avg", 35178), ("tcaSwEnvStatsFanCtrlrInlet1", 35198), ("tcaSwEnvStatsFanCtrlrInlet1Min", 35200), ("tcaSwEnvStatsFanCtrlrInlet1Max", 35201), ("tcaSwEnvStatsFanCtrlrInlet1Avg", 35202), ("tcaSwEnvStatsFanCtrlrInlet2", 35206), ("tcaSwEnvStatsFanCtrlrInlet2Min", 35208), ("tcaSwEnvStatsFanCtrlrInlet2Max", 35209), ("tcaSwEnvStatsFanCtrlrInlet2Avg", 35210), ("tcaSwEnvStatsFanCtrlrInlet3", 35214), ("tcaSwEnvStatsFanCtrlrInlet3Min", 35216), ("tcaSwEnvStatsFanCtrlrInlet3Max", 35217), ("tcaSwEnvStatsFanCtrlrInlet3Avg", 35218), ("tcaSwEnvStatsFanCtrlrInlet4", 35222), ("tcaSwEnvStatsFanCtrlrInlet4Min", 35224), ("tcaSwEnvStatsFanCtrlrInlet4Max", 35225), ("tcaSwEnvStatsFanCtrlrInlet4Avg", 35226), ("tcaSwSystemStatsMemAvailable", 35234), ("tcaSwSystemStatsMemAvailableMin", 35236), ("tcaSwSystemStatsMemAvailableMax", 35237), ("tcaSwSystemStatsMemAvailableAvg", 35238), ("tcaSwSystemStatsMemCached", 35242), ("tcaSwSystemStatsMemCachedMin", 35244), ("tcaSwSystemStatsMemCachedMax", 35245), ("tcaSwSystemStatsMemCachedAvg", 35246), ("tcaSwSystemStatsLoad", 35250), ("tcaSwSystemStatsLoadMin", 35252), ("tcaSwSystemStatsLoadMax", 35253), ("tcaSwSystemStatsLoadAvg", 35254), ("tcaEtherTxStatsTotalBytesDelta", 35275), ("tcaEtherTxStatsTotalBytesDeltaMin", 35276), ("tcaEtherTxStatsTotalBytesDeltaMax", 35277), ("tcaEtherTxStatsTotalBytesDeltaAvg", 35278), ("tcaEtherTxStatsTotalPacketsDelta", 35285), ("tcaEtherTxStatsTotalPacketsDeltaMin", 35286), ("tcaEtherTxStatsTotalPacketsDeltaMax", 35287), ("tcaEtherTxStatsTotalPacketsDeltaAvg", 35288), ("tcaEtherTxStatsMulticastPacketsDelta", 35295), ("tcaEtherTxStatsMulticastPacketsDeltaMin", 35296), ("tcaEtherTxStatsMulticastPacketsDeltaMax", 35297), ("tcaEtherTxStatsMulticastPacketsDeltaAvg", 35298), ("tcaEtherTxStatsBroadcastPacketsDelta", 35305), ("tcaEtherTxStatsBroadcastPacketsDeltaMin", 35306), ("tcaEtherTxStatsBroadcastPacketsDeltaMax", 35307), ("tcaEtherTxStatsBroadcastPacketsDeltaAvg", 35308), ("tcaEtherTxStatsJumboPacketsDelta", 35315), ("tcaEtherTxStatsJumboPacketsDeltaMin", 35316), ("tcaEtherTxStatsJumboPacketsDeltaMax", 35317), ("tcaEtherTxStatsJumboPacketsDeltaAvg", 35318), ("tcaEtherRxStatsTotalBytesDelta", 35329), ("tcaEtherRxStatsTotalBytesDeltaMin", 35330), ("tcaEtherRxStatsTotalBytesDeltaMax", 35331), ("tcaEtherRxStatsTotalBytesDeltaAvg", 35332), ("tcaEtherRxStatsTotalPacketsDelta", 35339), ("tcaEtherRxStatsTotalPacketsDeltaMin", 35340), ("tcaEtherRxStatsTotalPacketsDeltaMax", 35341), ("tcaEtherRxStatsTotalPacketsDeltaAvg", 35342), ("tcaEtherRxStatsUnicastPacketsDelta", 35349), ("tcaEtherRxStatsUnicastPacketsDeltaMin", 35350), ("tcaEtherRxStatsUnicastPacketsDeltaMax", 35351), ("tcaEtherRxStatsUnicastPacketsDeltaAvg", 35352), ("tcaEtherRxStatsMulticastPacketsDelta", 35359), ("tcaEtherRxStatsMulticastPacketsDeltaMin", 35360), ("tcaEtherRxStatsMulticastPacketsDeltaMax", 35361), ("tcaEtherRxStatsMulticastPacketsDeltaAvg", 35362), ("tcaEtherRxStatsBroadcastPacketsDelta", 35369), ("tcaEtherRxStatsBroadcastPacketsDeltaMin", 35370), ("tcaEtherRxStatsBroadcastPacketsDeltaMax", 35371), ("tcaEtherRxStatsBroadcastPacketsDeltaAvg", 35372), ("tcaEtherRxStatsJumboPacketsDelta", 35379), ("tcaEtherRxStatsJumboPacketsDeltaMin", 35380), ("tcaEtherRxStatsJumboPacketsDeltaMax", 35381), ("tcaEtherRxStatsJumboPacketsDeltaAvg", 35382), ("tcaComputeMbPowerStatsConsumedPower", 35962), ("tcaComputeMbPowerStatsConsumedPowerMin", 35964), ("tcaComputeMbPowerStatsConsumedPowerMax", 35965), ("tcaComputeMbPowerStatsConsumedPowerAvg", 35966), ("tcaComputeMbTempStatsFmTempSenIo", 35974), ("tcaComputeMbTempStatsFmTempSenIoMin", 35976), ("tcaComputeMbTempStatsFmTempSenIoMax", 35977), ("tcaComputeMbTempStatsFmTempSenIoAvg", 35978), ("tcaEquipmentChassisStatsInputPower", 36234), ("tcaEquipmentChassisStatsInputPowerMin", 36236), ("tcaEquipmentChassisStatsInputPowerMax", 36237), ("tcaEquipmentChassisStatsInputPowerAvg", 36238), ("tcaEquipmentChassisStatsOutputPower", 36242), ("tcaEquipmentChassisStatsOutputPowerMin", 36244), ("tcaEquipmentChassisStatsOutputPowerMax", 36245), ("tcaEquipmentChassisStatsOutputPowerAvg", 36246), ("tcaEquipmentPsuStatsAmbientTemp", 36266), ("tcaEquipmentPsuStatsAmbientTempMin", 36268), ("tcaEquipmentPsuStatsAmbientTempMax", 36269), ("tcaEquipmentPsuStatsAmbientTempAvg", 36270), ("tcaEquipmentPsuStatsOutputCurrent", 36274), ("tcaEquipmentPsuStatsOutputCurrentMin", 36276), ("tcaEquipmentPsuStatsOutputCurrentMax", 36277), ("tcaEquipmentPsuStatsOutputCurrentAvg", 36278), ("tcaEquipmentPsuStatsOutputPower", 36282), ("tcaEquipmentPsuStatsOutputPowerMin", 36284), ("tcaEquipmentPsuStatsOutputPowerMax", 36285), ("tcaEquipmentPsuStatsOutputPowerAvg", 36286), ("tcaEquipmentPsuInputStatsCurrent", 36294), ("tcaEquipmentPsuInputStatsCurrentMin", 36296), ("tcaEquipmentPsuInputStatsCurrentMax", 36297), ("tcaEquipmentPsuInputStatsCurrentAvg", 36298), ("tcaEquipmentPsuInputStatsVoltage", 36302), ("tcaEquipmentPsuInputStatsVoltageMin", 36304), ("tcaEquipmentPsuInputStatsVoltageMax", 36305), ("tcaEquipmentPsuInputStatsVoltageAvg", 36306), ("tcaEquipmentPsuInputStatsPower", 36310), ("tcaEquipmentPsuInputStatsPowerMin", 36312), ("tcaEquipmentPsuInputStatsPowerMax", 36313), ("tcaEquipmentPsuInputStatsPowerAvg", 36314), ("tcaEquipmentFanModuleStatsAmbientTemp", 36323), ("tcaEquipmentFanModuleStatsAmbientTempMin", 36325), ("tcaEquipmentFanModuleStatsAmbientTempMax", 36326), ("tcaEquipmentFanModuleStatsAmbientTempAvg", 36327), ("tcaEquipmentFanStatsSpeed", 36335), ("tcaEquipmentFanStatsSpeedMin", 36337), ("tcaEquipmentFanStatsSpeedMax", 36338), ("tcaEquipmentFanStatsSpeedAvg", 36339), ("tcaEquipmentPsuStatsOutput12v", 37154), ("tcaEquipmentPsuStatsOutput12vMin", 37156), ("tcaEquipmentPsuStatsOutput12vMax", 37157), ("tcaEquipmentPsuStatsOutput12vAvg", 37158), ("tcaEquipmentPsuStatsOutput3v3", 37162), ("tcaEquipmentPsuStatsOutput3v3Min", 37164), ("tcaEquipmentPsuStatsOutput3v3Max", 37165), ("tcaEquipmentPsuStatsOutput3v3Avg", 37166), ("tcaEquipmentPsuStatsInput210v", 37170), ("tcaEquipmentPsuStatsInput210vMin", 37172), ("tcaEquipmentPsuStatsInput210vMax", 37173), ("tcaEquipmentPsuStatsInput210vAvg", 37174), ("tcaEquipmentIocardStatsAmbientTemp", 37269), ("tcaEquipmentIocardStatsAmbientTempMin", 37271), ("tcaEquipmentIocardStatsAmbientTempMax", 37272), ("tcaEquipmentIocardStatsAmbientTempAvg", 37273), ("tcaEtherErrStatsAlignDelta", 37313), ("tcaEtherErrStatsAlignDeltaMin", 37314), ("tcaEtherErrStatsAlignDeltaMax", 37315), ("tcaEtherErrStatsAlignDeltaAvg", 37316), ("tcaEtherErrStatsFcsDelta", 37323), ("tcaEtherErrStatsFcsDeltaMin", 37324), ("tcaEtherErrStatsFcsDeltaMax", 37325), ("tcaEtherErrStatsFcsDeltaAvg", 37326), ("tcaEtherErrStatsXmitDelta", 37333), ("tcaEtherErrStatsXmitDeltaMin", 37334), ("tcaEtherErrStatsXmitDeltaMax", 37335), ("tcaEtherErrStatsXmitDeltaAvg", 37336), ("tcaEtherErrStatsRcvDelta", 37343), ("tcaEtherErrStatsRcvDeltaMin", 37344), ("tcaEtherErrStatsRcvDeltaMax", 37345), ("tcaEtherErrStatsRcvDeltaAvg", 37346), ("tcaEtherErrStatsUnderSizeDelta", 37353), ("tcaEtherErrStatsUnderSizeDeltaMin", 37354), ("tcaEtherErrStatsUnderSizeDeltaMax", 37355), ("tcaEtherErrStatsUnderSizeDeltaAvg", 37356), ("tcaEtherErrStatsOutDiscardDelta", 37363), ("tcaEtherErrStatsOutDiscardDeltaMin", 37364), ("tcaEtherErrStatsOutDiscardDeltaMax", 37365), ("tcaEtherErrStatsOutDiscardDeltaAvg", 37366), ("tcaEtherErrStatsIntMacTxDelta", 37383), ("tcaEtherErrStatsIntMacTxDeltaMin", 37384), ("tcaEtherErrStatsIntMacTxDeltaMax", 37385), ("tcaEtherErrStatsIntMacTxDeltaAvg", 37386), ("tcaEtherErrStatsIntMacRxDelta", 37393), ("tcaEtherErrStatsIntMacRxDeltaMin", 37394), ("tcaEtherErrStatsIntMacRxDeltaMax", 37395), ("tcaEtherErrStatsIntMacRxDeltaAvg", 37396), ("tcaEtherLossStatsSingleCollisionDelta", 37403), ("tcaEtherLossStatsSingleCollisionDeltaMin", 37404), ("tcaEtherLossStatsSingleCollisionDeltaMax", 37405), ("tcaEtherLossStatsSingleCollisionDeltaAvg", 37406), ("tcaEtherLossStatsMultiCollisionDelta", 37413), ("tcaEtherLossStatsMultiCollisionDeltaMin", 37414), ("tcaEtherLossStatsMultiCollisionDeltaMax", 37415), ("tcaEtherLossStatsMultiCollisionDeltaAvg", 37416), ("tcaEtherLossStatsLateCollisionDelta", 37423), ("tcaEtherLossStatsLateCollisionDeltaMin", 37424), ("tcaEtherLossStatsLateCollisionDeltaMax", 37425), ("tcaEtherLossStatsLateCollisionDeltaAvg", 37426), ("tcaEtherLossStatsCarrierSenseDelta", 37443), ("tcaEtherLossStatsCarrierSenseDeltaMin", 37444), ("tcaEtherLossStatsCarrierSenseDeltaMax", 37445), ("tcaEtherLossStatsCarrierSenseDeltaAvg", 37446), ("tcaEtherLossStatsGiantsDelta", 37453), ("tcaEtherLossStatsGiantsDeltaMin", 37454), ("tcaEtherLossStatsGiantsDeltaMax", 37455), ("tcaEtherLossStatsGiantsDeltaAvg", 37456), ("tcaEtherLossStatsSymbolDelta", 37463), ("tcaEtherLossStatsSymbolDeltaMin", 37464), ("tcaEtherLossStatsSymbolDeltaMax", 37465), ("tcaEtherLossStatsSymbolDeltaAvg", 37466), ("tcaEtherLossStatsSqetestDelta", 37473), ("tcaEtherLossStatsSqetestDeltaMin", 37474), ("tcaEtherLossStatsSqetestDeltaMax", 37475), ("tcaEtherLossStatsSqetestDeltaAvg", 37476), ("tcaEtherPauseStatsRecvPauseDelta", 37485), ("tcaEtherPauseStatsRecvPauseDeltaMin", 37486), ("tcaEtherPauseStatsRecvPauseDeltaMax", 37487), ("tcaEtherPauseStatsRecvPauseDeltaAvg", 37488), ("tcaEtherPauseStatsXmitPauseDelta", 37495), ("tcaEtherPauseStatsXmitPauseDeltaMin", 37496), ("tcaEtherPauseStatsXmitPauseDeltaMax", 37497), ("tcaEtherPauseStatsXmitPauseDeltaAvg", 37498), ("tcaEtherPauseStatsResetsDelta", 37505), ("tcaEtherPauseStatsResetsDeltaMin", 37506), ("tcaEtherPauseStatsResetsDeltaMax", 37507), ("tcaEtherPauseStatsResetsDeltaAvg", 37508), ("tcaEtherLossStatsExcessCollisionDelta", 37532), ("tcaEtherLossStatsExcessCollisionDeltaMin", 37533), ("tcaEtherLossStatsExcessCollisionDeltaMax", 37534), ("tcaEtherLossStatsExcessCollisionDeltaAvg", 37535), ("tcaEtherTxStatsUnicastPacketsDelta", 37543), ("tcaEtherTxStatsUnicastPacketsDeltaMin", 37544), ("tcaEtherTxStatsUnicastPacketsDeltaMax", 37545), ("tcaEtherTxStatsUnicastPacketsDeltaAvg", 37546)) + NamedValues(("tcaEtherErrStatsDeferredTxDelta", 37553), ("tcaEtherErrStatsDeferredTxDeltaMin", 37554), ("tcaEtherErrStatsDeferredTxDeltaMax", 37555), ("tcaEtherErrStatsDeferredTxDeltaAvg", 37556), ("tcaComputeMbPowerStatsInputVoltage", 37564), ("tcaComputeMbPowerStatsInputVoltageMin", 37566), ("tcaComputeMbPowerStatsInputVoltageMax", 37567), ("tcaComputeMbPowerStatsInputVoltageAvg", 37568), ("tcaComputeMbPowerStatsInputCurrent", 37572), ("tcaComputeMbPowerStatsInputCurrentMin", 37574), ("tcaComputeMbPowerStatsInputCurrentMax", 37575), ("tcaComputeMbPowerStatsInputCurrentAvg", 37576), ("tcaComputeMbTempStatsFmTempSenRear", 37580), ("tcaComputeMbTempStatsFmTempSenRearMin", 37582), ("tcaComputeMbTempStatsFmTempSenRearMax", 37583), ("tcaComputeMbTempStatsFmTempSenRearAvg", 37584), ("tcaMemoryUnitEnvStatsTemperature", 37600), ("tcaMemoryUnitEnvStatsTemperatureMin", 37602), ("tcaMemoryUnitEnvStatsTemperatureMax", 37603), ("tcaMemoryUnitEnvStatsTemperatureAvg", 37604), ("tcaProcessorEnvStatsTemperature", 37610), ("tcaProcessorEnvStatsTemperatureMin", 37612), ("tcaProcessorEnvStatsTemperatureMax", 37613), ("tcaProcessorEnvStatsTemperatureAvg", 37614), ("tcaSwEnvStatsPsuCtrlrInlet1", 37771), ("tcaSwEnvStatsPsuCtrlrInlet1Min", 37773), ("tcaSwEnvStatsPsuCtrlrInlet1Max", 37774), ("tcaSwEnvStatsPsuCtrlrInlet1Avg", 37775), ("tcaSwEnvStatsPsuCtrlrInlet2", 37779), ("tcaSwEnvStatsPsuCtrlrInlet2Min", 37781), ("tcaSwEnvStatsPsuCtrlrInlet2Max", 37782), ("tcaSwEnvStatsPsuCtrlrInlet2Avg", 37783), ("tcaComputePcieFatalProtocolStatsDllpErrors", 38022), ("tcaComputePcieFatalProtocolStatsFlowControlErrors", 38032), ("tcaComputePcieFatalReceiveStatsUnsupportedRequestErrors", 38044), ("tcaComputePcieFatalReceiveStatsErrFatalErrors", 38054), ("tcaComputePcieFatalReceiveStatsErrNonFatalErrors", 38064), ("tcaComputePcieFatalCompletionStatsUnexpectedErrors", 38086), ("tcaComputePcieFatalCompletionStatsTimeoutErrors", 38096), ("tcaComputePcieFatalCompletionStatsAbortErrors", 38106), ("tcaComputePcieFatalStatsSurpriseLinkDownErrors", 38128), ("tcaComputePcieFatalStatsPoisonedtlperrors", 38138), ("tcaComputePcieFatalStatsAcsViolationErrors", 38148), ("tcaComputePcieFatalStatsMalformedtlperrors", 38158), ("tcaEquipmentIocardStatsTemp", 38311), ("tcaEquipmentIocardStatsTempMin", 38313), ("tcaEquipmentIocardStatsTempMax", 38314), ("tcaEquipmentIocardStatsTempAvg", 38315), ("tcaProcessorEnvStatsInputCurrent", 38349), ("tcaProcessorEnvStatsInputCurrentMin", 38351), ("tcaProcessorEnvStatsInputCurrentMax", 38352), ("tcaProcessorEnvStatsInputCurrentAvg", 38353), ("tcaMemoryArrayEnvStatsInputCurrent", 38357), ("tcaMemoryArrayEnvStatsInputCurrentMin", 38359), ("tcaMemoryArrayEnvStatsInputCurrentMax", 38360), ("tcaMemoryArrayEnvStatsInputCurrentAvg", 38361), ("tcaAdaptorEthPortBySizeLargeStatsNoBreakdownGreaterThan1518Delta", 38470), ("tcaAdaptorEthPortBySizeLargeStatsNoBrkdnGreaterThan1518DeltaMin", 38471), ("tcaAdaptorEthPortBySizeLargeStatsNoBrkdnGreaterThan1518DeltaMax", 38472), ("tcaAdaptorEthPortBySizeLargeStatsNoBrkdnGreaterThan1518DeltaAvg", 38473), ("tcaPowerGroupStatsPower", 38557), ("tcaPowerGroupStatsPowerMin", 38559), ("tcaPowerGroupStatsPowerMax", 38560), ("tcaPowerGroupStatsPowerAvg", 38561), ("tcaMemoryBufferUnitEnvStatsTemperature", 38624), ("tcaMemoryBufferUnitEnvStatsTemperatureMin", 38626), ("tcaMemoryBufferUnitEnvStatsTemperatureMax", 38627), ("tcaMemoryBufferUnitEnvStatsTemperatureAvg", 38628), ("tcaComputeIohubEnvStatsTemperature", 38678), ("tcaComputeIohubEnvStatsTemperatureMin", 38680), ("tcaComputeIohubEnvStatsTemperatureMax", 38681), ("tcaComputeIohubEnvStatsTemperatureAvg", 38682), ("tcaComputeMbTempStatsFmTempSenRearl", 39082), ("tcaComputeMbTempStatsFmTempSenRearlmin", 39084), ("tcaComputeMbTempStatsFmTempSenRearlmax", 39085), ("tcaComputeMbTempStatsFmTempSenRearlavg", 39086), ("tcaComputeMbTempStatsFmTempSenRearr", 39090), ("tcaComputeMbTempStatsFmTempSenRearrmin", 39092), ("tcaComputeMbTempStatsFmTempSenRearrmax", 39093), ("tcaComputeMbTempStatsFmTempSenRearravg", 39094), ("tcaEquipmentFexEnvStatsOutlet1", 39107), ("tcaEquipmentFexEnvStatsOutlet1Min", 39109), ("tcaEquipmentFexEnvStatsOutlet1Max", 39110), ("tcaEquipmentFexEnvStatsOutlet1Avg", 39111), ("tcaEquipmentFexEnvStatsOutlet2", 39115), ("tcaEquipmentFexEnvStatsOutlet2Min", 39117), ("tcaEquipmentFexEnvStatsOutlet2Max", 39118), ("tcaEquipmentFexEnvStatsOutlet2Avg", 39119), ("tcaEquipmentFexEnvStatsInlet", 39123), ("tcaEquipmentFexEnvStatsInletMin", 39125), ("tcaEquipmentFexEnvStatsInletMax", 39126), ("tcaEquipmentFexEnvStatsInletAvg", 39127), ("tcaEquipmentFexEnvStatsInlet1", 39131), ("tcaEquipmentFexEnvStatsInlet1Min", 39133), ("tcaEquipmentFexEnvStatsInlet1Max", 39134), ("tcaEquipmentFexEnvStatsInlet1Avg", 39135), ("tcaEquipmentFexEnvStatsDie1", 39139), ("tcaEquipmentFexEnvStatsDie1Min", 39141), ("tcaEquipmentFexEnvStatsDie1Max", 39142), ("tcaEquipmentFexEnvStatsDie1Avg", 39143), ("tcaEquipmentFexPowerSummaryTotalPower", 39166), ("tcaEquipmentFexPowerSummaryTotalPowerMin", 39168), ("tcaEquipmentFexPowerSummaryTotalPowerMax", 39169), ("tcaEquipmentFexPowerSummaryTotalPowerAvg", 39170), ("tcaEquipmentFexPowerSummaryReservedPower", 39174), ("tcaEquipmentFexPowerSummaryReservedPowerMin", 39176), ("tcaEquipmentFexPowerSummaryReservedPowerMax", 39177), ("tcaEquipmentFexPowerSummaryReservedPowerAvg", 39178), ("tcaEquipmentFexPowerSummaryModulePower", 39182), ("tcaEquipmentFexPowerSummaryModulePowerMin", 39184), ("tcaEquipmentFexPowerSummaryModulePowerMax", 39185), ("tcaEquipmentFexPowerSummaryModulePowerAvg", 39186), ("tcaEquipmentFexPowerSummaryAvailablePower", 39190), ("tcaEquipmentFexPowerSummaryAvailablePowerMin", 39192), ("tcaEquipmentFexPowerSummaryAvailablePowerMax", 39193), ("tcaEquipmentFexPowerSummaryAvailablePowerAvg", 39194), ("tcaEquipmentFexPsuInputStatsCurrent", 39200), ("tcaEquipmentFexPsuInputStatsCurrentMin", 39202), ("tcaEquipmentFexPsuInputStatsCurrentMax", 39203), ("tcaEquipmentFexPsuInputStatsCurrentAvg", 39204), ("tcaEquipmentFexPsuInputStatsVoltage", 39208), ("tcaEquipmentFexPsuInputStatsVoltageMin", 39210), ("tcaEquipmentFexPsuInputStatsVoltageMax", 39211), ("tcaEquipmentFexPsuInputStatsVoltageAvg", 39212), ("tcaEquipmentFexPsuInputStatsPower", 39216), ("tcaEquipmentFexPsuInputStatsPowerMin", 39218), ("tcaEquipmentFexPsuInputStatsPowerMax", 39219), ("tcaEquipmentFexPsuInputStatsPowerAvg", 39220), ("tcaEquipmentRackUnitPsuStatsAmbientTemp", 39227), ("tcaEquipmentRackUnitPsuStatsAmbientTempMin", 39229), ("tcaEquipmentRackUnitPsuStatsAmbientTempMax", 39230), ("tcaEquipmentRackUnitPsuStatsAmbientTempAvg", 39231), ("tcaEquipmentRackUnitPsuStatsOutputCurrent", 39235), ("tcaEquipmentRackUnitPsuStatsOutputCurrentMin", 39237), ("tcaEquipmentRackUnitPsuStatsOutputCurrentMax", 39238), ("tcaEquipmentRackUnitPsuStatsOutputCurrentAvg", 39239), ("tcaEquipmentRackUnitPsuStatsOutputPower", 39243), ("tcaEquipmentRackUnitPsuStatsOutputPowerMin", 39245), ("tcaEquipmentRackUnitPsuStatsOutputPowerMax", 39246), ("tcaEquipmentRackUnitPsuStatsOutputPowerAvg", 39247), ("tcaEquipmentRackUnitPsuStatsInputPower", 39251), ("tcaEquipmentRackUnitPsuStatsInputPowerMin", 39253), ("tcaEquipmentRackUnitPsuStatsInputPowerMax", 39254), ("tcaEquipmentRackUnitPsuStatsInputPowerAvg", 39255), ("tcaEquipmentRackUnitPsuStatsOutputVoltage", 39259), ("tcaEquipmentRackUnitPsuStatsOutputVoltageMin", 39261), ("tcaEquipmentRackUnitPsuStatsOutputVoltageMax", 39262), ("tcaEquipmentRackUnitPsuStatsOutputVoltageAvg", 39263), ("tcaEquipmentRackUnitPsuStatsInputVoltage", 39267), ("tcaEquipmentRackUnitPsuStatsInputVoltageMin", 39269), ("tcaEquipmentRackUnitPsuStatsInputVoltageMax", 39270), ("tcaEquipmentRackUnitPsuStatsInputVoltageAvg", 39271), ("tcaComputePcieFatalReceiveStatsBufferOverflowErrors", 39583), ("tcaProcessorErrorStatsMirroringIntraSockErrors", 39649), ("tcaProcessorErrorStatsMirroringInterSockErrors", 39658), ("tcaProcessorErrorStatsSparingErrors", 39667), ("tcaProcessorErrorStatsSmiLinkCorrErrors", 39676), ("tcaProcessorErrorStatsSmiLinkUncorrErrors", 39685), ("tcaMemoryErrorStatsEccMultibitErrors", 39702), ("tcaMemoryErrorStatsEccSinglebitErrors", 39711), ("tcaMemoryErrorStatsAddressParityErrors", 39720), ("tcaMemoryErrorStatsMismatchErrors", 39729), ("tcaEquipmentRackUnitFanStatsSpeed", 39794), ("tcaEquipmentRackUnitFanStatsSpeedMin", 39796), ("tcaEquipmentRackUnitFanStatsSpeedMax", 39797), ("tcaEquipmentRackUnitFanStatsSpeedAvg", 39798), ("tcaComputeRackUnitMbTempStatsFrontTemp", 40092), ("tcaComputeRackUnitMbTempStatsFrontTempMin", 40094), ("tcaComputeRackUnitMbTempStatsFrontTempMax", 40095), ("tcaComputeRackUnitMbTempStatsFrontTempAvg", 40096), ("tcaComputeRackUnitMbTempStatsRearTemp", 40100), ("tcaComputeRackUnitMbTempStatsRearTempMin", 40102), ("tcaComputeRackUnitMbTempStatsRearTempMax", 40103), ("tcaComputeRackUnitMbTempStatsRearTempAvg", 40104), ("tcaComputeRackUnitMbTempStatsAmbientTemp", 40108), ("tcaComputeRackUnitMbTempStatsAmbientTempMin", 40110), ("tcaComputeRackUnitMbTempStatsAmbientTempMax", 40111), ("tcaComputeRackUnitMbTempStatsAmbientTempAvg", 40112), ("tcaComputeRackUnitMbTempStatsIoh1Temp", 40116), ("tcaComputeRackUnitMbTempStatsIoh1TempMin", 40118), ("tcaComputeRackUnitMbTempStatsIoh1TempMax", 40119), ("tcaComputeRackUnitMbTempStatsIoh1TempAvg", 40120), ("tcaComputeRackUnitMbTempStatsIoh2Temp", 40124), ("tcaComputeRackUnitMbTempStatsIoh2TempMin", 40126), ("tcaComputeRackUnitMbTempStatsIoh2TempMax", 40127), ("tcaComputeRackUnitMbTempStatsIoh2TempAvg", 40128), ("tcaEquipmentPsuOutputStatsCurrent", 40441), ("tcaEquipmentPsuOutputStatsCurrentMin", 40443), ("tcaEquipmentPsuOutputStatsCurrentMax", 40444), ("tcaEquipmentPsuOutputStatsCurrentAvg", 40445), ("tcaEquipmentPsuOutputStatsVoltage", 40449), ("tcaEquipmentPsuOutputStatsVoltageMin", 40451), ("tcaEquipmentPsuOutputStatsVoltageMax", 40452), ("tcaEquipmentPsuOutputStatsVoltageAvg", 40453), ("tcaEquipmentPsuOutputStatsPower", 40457), ("tcaEquipmentPsuOutputStatsPowerMin", 40459), ("tcaEquipmentPsuOutputStatsPowerMax", 40460), ("tcaEquipmentPsuOutputStatsPowerAvg", 40461), ("tcaEquipmentNetworkElementFanStatsSpeed", 40583), ("tcaEquipmentNetworkElementFanStatsSpeedMin", 40585), ("tcaEquipmentNetworkElementFanStatsSpeedMax", 40586), ("tcaEquipmentNetworkElementFanStatsSpeedAvg", 40587), ("tcaEquipmentNetworkElementFanStatsDrivePercentage", 40591), ("tcaEquipmentNetworkElementFanStatsDrivePercentageMin", 40593), ("tcaEquipmentNetworkElementFanStatsDrivePercentageMax", 40594), ("tcaEquipmentNetworkElementFanStatsDrivePercentageAvg", 40595), ("tcaSwCardEnvStatsSlotOutlet1", 41016), ("tcaSwCardEnvStatsSlotOutlet1Min", 41018), ("tcaSwCardEnvStatsSlotOutlet1Max", 41019), ("tcaSwCardEnvStatsSlotOutlet1Avg", 41020), ("tcaSwCardEnvStatsSlotOutlet2", 41024), ("tcaSwCardEnvStatsSlotOutlet2Min", 41026), ("tcaSwCardEnvStatsSlotOutlet2Max", 41027), ("tcaSwCardEnvStatsSlotOutlet2Avg", 41028), ("tcaSwCardEnvStatsSlotOutlet3", 41032), ("tcaSwCardEnvStatsSlotOutlet3Min", 41034), ("tcaSwCardEnvStatsSlotOutlet3Max", 41035), ("tcaSwCardEnvStatsSlotOutlet3Avg", 41036), ("tcaEtherFcoeInterfaceStatsPacketsTxDelta", 41049), ("tcaEtherFcoeInterfaceStatsPacketsTxDeltaMin", 41050), ("tcaEtherFcoeInterfaceStatsPacketsTxDeltaMax", 41051), ("tcaEtherFcoeInterfaceStatsPacketsTxDeltaAvg", 41052), ("tcaEtherFcoeInterfaceStatsPacketsRxDelta", 41059), ("tcaEtherFcoeInterfaceStatsPacketsRxDeltaMin", 41060), ("tcaEtherFcoeInterfaceStatsPacketsRxDeltaMax", 41061), ("tcaEtherFcoeInterfaceStatsPacketsRxDeltaAvg", 41062), ("tcaEtherFcoeInterfaceStatsBytesTxDelta", 41069), ("tcaEtherFcoeInterfaceStatsBytesTxDeltaMin", 41070), ("tcaEtherFcoeInterfaceStatsBytesTxDeltaMax", 41071), ("tcaEtherFcoeInterfaceStatsBytesTxDeltaAvg", 41072), ("tcaEtherFcoeInterfaceStatsBytesRxDelta", 41079), ("tcaEtherFcoeInterfaceStatsBytesRxDeltaMin", 41080), ("tcaEtherFcoeInterfaceStatsBytesRxDeltaMax", 41081), ("tcaEtherFcoeInterfaceStatsBytesRxDeltaAvg", 41082), ("tcaEtherFcoeInterfaceStatsErrorsTxDelta", 41089), ("tcaEtherFcoeInterfaceStatsErrorsTxDeltaMin", 41090), ("tcaEtherFcoeInterfaceStatsErrorsTxDeltaMax", 41091), ("tcaEtherFcoeInterfaceStatsErrorsTxDeltaAvg", 41092), ("tcaEtherFcoeInterfaceStatsErrorsRxDelta", 41099), ("tcaEtherFcoeInterfaceStatsErrorsRxDeltaMin", 41100), ("tcaEtherFcoeInterfaceStatsErrorsRxDeltaMax", 41101), ("tcaEtherFcoeInterfaceStatsErrorsRxDeltaAvg", 41102), ("tcaEtherFcoeInterfaceStatsDroppedTxDelta", 41109), ("tcaEtherFcoeInterfaceStatsDroppedTxDeltaMin", 41110), ("tcaEtherFcoeInterfaceStatsDroppedTxDeltaMax", 41111), ("tcaEtherFcoeInterfaceStatsDroppedTxDeltaAvg", 41112), ("tcaEtherFcoeInterfaceStatsDroppedRxDelta", 41119), ("tcaEtherFcoeInterfaceStatsDroppedRxDeltaMin", 41120), ("tcaEtherFcoeInterfaceStatsDroppedRxDeltaMax", 41121), ("tcaEtherFcoeInterfaceStatsDroppedRxDeltaAvg", 41122), ("fsmSamDmeEquipmentiocardFePresenceRemoteInv", 77845), ("fsmSamDmeEquipmentiocardFeConnRemoteInv", 77846), ("fsmSamDmeEquipmentChassisRemoveChassisRemoteInv", 77847), ("fsmSetLocatorLedRemoteInv", 77848), ("fsmSamDmeMgmtControllerExtMgmtIfConfigRemoteInv", 77958)) + NamedValues(("fsmSamDmeFabricComputeSlotEpIdentifyRemoteInv", 77959), ("fsmSamDmeComputeBladeDiscoverRemoteInv", 77960), ("fsmSamDmeEquipmentChassisPsuPolicyConfigRemoteInv", 77973), ("fsmSamDmeAdaptorHostFcIfResetFcPersBindingRemoteInv", 77974), ("fsmSamDmeComputeBladeDiagRemoteInv", 77975), ("fsmSwitchModeRemoteInv", 77979), ("fsmSamDmeVnicProfileSetDeployRemoteInv", 77990), ("fsmUpdateSvcEpRemoteInv", 78016), ("fsmSamDmeCommSvcEpRestartWebSvcRemoteInv", 78017), ("fsmUpdateEpRemoteInv", 78019), ("fsmUpdateRealmRemoteInv", 78020), ("fsmUpdateUserEpRemoteInv", 78021), ("fsmSamDmePkiEpUpdateEpRemoteInv", 78022), ("fsmSingleRemoteInv", 78040), ("fsmSamDmeSysfileMutationGlobalRemoteInv", 78041), ("fsmSamDmeSysdebugManualCoreFileExportTargetExportRemoteInv", 78044), ("fsmSamDmeSysdebugAutoCoreFileExportTargetConfigureRemoteInv", 78045), ("fsmSamDmeSysdebugLogControlEpLogControlPersistRemoteInv", 78046), ("fsmSamDmeSwAccessDomainDeployRemoteInv", 78074), ("fsmSamDmeSwEthLanBorderDeployRemoteInv", 78075), ("fsmSamDmeSwFcSanBorderDeployRemoteInv", 78076), ("fsmSamDmeSwUtilityDomainDeployRemoteInv", 78077), ("fsmSamDmeSyntheticFsObjCreateRemoteInv", 78081), ("fsmSamDmeFirmwareDownloaderDownloadRemoteInv", 78090), ("fsmSamDmeFirmwareImageDeleteRemoteInv", 78091), ("fsmUpdateSwitchRemoteInv", 78093), ("fsmUpdateiomRemoteInv", 78094), ("fsmSamDmeMgmtControllerActivateiomRemoteInv", 78095), ("fsmUpdatebmcRemoteInv", 78096), ("fsmSamDmeMgmtControllerActivatebmcRemoteInv", 78097), ("fsmSamDmeCallhomeEpConfigCallhomeRemoteInv", 78110), ("fsmSwMgmtOobIfConfigRemoteInv", 78113), ("fsmSwMgmtInbandIfConfigRemoteInv", 78114), ("fsmVirtualIfConfigRemoteInv", 78119), ("fsmSamDmeMgmtIfEnableVipRemoteInv", 78120), ("fsmSamDmeMgmtIfDisableVipRemoteInv", 78121), ("fsmSamDmeMgmtIfEnablehaRemoteInv", 78122), ("fsmSamDmeMgmtBackupBackupRemoteInv", 78123), ("fsmSamDmeMgmtImporterImportRemoteInv", 78124), ("fsmSamDmeStatsCollectionPolicyUpdateEpRemoteInv", 78182), ("fsmSamDmeQosclassDefinitionConfigGlobalQoSremoteInv", 78185), ("fsmSamDmeEpqosDefinitionDeployRemoteInv", 78189), ("fsmSamDmeEpqosDefinitionDelTaskRemoveRemoteInv", 78190), ("fsmSamDmeEquipmentiocardResetCmcRemoteInv", 78243), ("fsmUpdateucsmanagerRemoteInv", 78255), ("fsmSysConfigRemoteInv", 78263), ("fsmSamDmeAdaptorExtEthIfPathResetRemoteInv", 78292), ("fsmSamDmeAdaptorHostEthIfCircuitResetRemoteInv", 78297), ("fsmSamDmeAdaptorHostFcIfCircuitResetRemoteInv", 78298), ("fsmSamDmeExtvmmProviderConfigRemoteInv", 78319), ("fsmSamDmeExtvmmKeyStoreCertInstallRemoteInv", 78320), ("fsmSamDmeExtvmmSwitchDelTaskRemoveProviderRemoteInv", 78321), ("fsmSamDmeExtvmmMasterExtKeyConfigRemoteInv", 78338), ("fsmUpdaterRemoteInv", 78344), ("fsmSamDmeFirmwareDistributableDeleteRemoteInv", 78346), ("fsmDiscoverRemoteInv", 78360), ("fsmAssociateRemoteInv", 78361), ("fsmDisassociateRemoteInv", 78362), ("fsmDecommissionRemoteInv", 78364), ("fsmSoftShutdownRemoteInv", 78365), ("fsmHardShutdownRemoteInv", 78366), ("fsmTurnupRemoteInv", 78367), ("fsmPowercycleRemoteInv", 78368), ("fsmHardresetRemoteInv", 78369), ("fsmSoftresetRemoteInv", 78370), ("fsmSwConnUpdRemoteInv", 78371), ("fsmBiosRecoveryRemoteInv", 78372), ("fsmCmosResetRemoteInv", 78374), ("fsmResetBmcRemoteInv", 78375), ("fsmUpdateExtUsersRemoteInv", 78378), ("fsmUpdateAdaptorRemoteInv", 78379), ("fsmActivateAdaptorRemoteInv", 78380), ("fsmConfigSoLremoteInv", 78381), ("fsmUnconfigSoLremoteInv", 78382), ("fsmSetFeLocatorLedRemoteInv", 78383), ("fsmSamDmeEquipmentChassisPowerCapRemoteInv", 78384), ("fsmSamDmeEquipmentiocardMuxOfflineRemoteInv", 78385), ("fsmPowerCapRemoteInv", 78390), ("fsmUpdateBoardControllerRemoteInv", 78404), ("fsmDeployCatalogueRemoteInv", 78405), ("fsmSamDmeComputePhysicalAssociateRemoteInv", 78413), ("fsmSamDmeComputePhysicalDisassociateRemoteInv", 78414), ("fsmSamDmeComputePhysicalPowerCapRemoteInv", 78415), ("fsmSamDmeComputePhysicalDecommissionRemoteInv", 78416), ("fsmSamDmeComputePhysicalSoftShutdownRemoteInv", 78417), ("fsmSamDmeComputePhysicalHardShutdownRemoteInv", 78418), ("fsmSamDmeComputePhysicalTurnupRemoteInv", 78419), ("fsmSamDmeComputePhysicalPowercycleRemoteInv", 78420), ("fsmSamDmeComputePhysicalHardresetRemoteInv", 78421), ("fsmSamDmeComputePhysicalSoftresetRemoteInv", 78422), ("fsmSamDmeComputePhysicalSwConnUpdRemoteInv", 78423), ("fsmSamDmeComputePhysicalBiosRecoveryRemoteInv", 78424), ("fsmSamDmeComputePhysicalCmosResetRemoteInv", 78426), ("fsmSamDmeComputePhysicalResetBmcRemoteInv", 78427), ("fsmSamDmeEquipmentiocardResetIomRemoteInv", 78428), ("fsmInstallRemoteInv", 78431), ("fsmClearRemoteInv", 78432), ("fsmUpdateFlexlmRemoteInv", 78433), ("fsmSamDmeComputeRackUnitDiscoverRemoteInv", 78434), ("fsmSamDmeLsServerConfigureRemoteInv", 78435), ("fsmSamDmeSwEthMonDeployRemoteInv", 78440), ("fsmSamDmeSwFcMonDeployRemoteInv", 78441), ("fsmSamDmeFabricSanCloudSwitchModeRemoteInv", 78442), ("fsmRemoveFexRemoteInv", 78447), ("fsmSamDmeComputePhysicalUpdateExtUsersRemoteInv", 78448), ("fsmSamDmeSysdebugTechSupportInitiateRemoteInv", 78452), ("fsmSamDmeSysdebugTechSupportDeleteTechSupFileRemoteInv", 78453), ("fsmSamDmeSysdebugTechSupportDownloadRemoteInv", 78454), ("fsmActivateCatalogRemoteInv", 78457), ("fsmActivateMgmtExtRemoteInv", 78458), ("fsmSamDmeComputePhysicalUpdateAdaptorRemoteInv", 78483), ("fsmSamDmeComputePhysicalActivateAdaptorRemoteInv", 78484), ("fsmSamDmeCapabilityCatalogueActivateCatalogRemoteInv", 78485), ("fsmSamDmeCapabilityMgmtExtensionActivateMgmtExtRemoteInv", 78486), ("fsmSamDmeLicenseDownloaderDownloadRemoteInv", 78490), ("fsmSamDmeLicenseFileInstallRemoteInv", 78491), ("fsmSamDmeLicenseFileClearRemoteInv", 78492), ("fsmSamDmeLicenseInstanceUpdateFlexlmRemoteInv", 78493), ("fsmConfigureRemoteInv", 78500), ("fsmMuxOfflineRemoteInv", 78501), ("fsmSamDmeComputePhysicalConfigSoLremoteInv", 78523), ("fsmSamDmeComputePhysicalUnconfigSoLremoteInv", 78524), ("fsmSamDmePortpioInCompatSfpPresenceRemoteInv", 78529), ("fsmSamDmeComputePhysicalDiagnosticInterruptRemoteInv", 78556), ("fsmSamDmeSysdebugCoreDownloadRemoteInv", 78573), ("fsmSamDmeEquipmentChassisDynamicReallocationRemoteInv", 78574), ("fsmSamDmeComputePhysicalResetKvmRemoteInv", 78603), ("fsmSamDmeMgmtControllerOnlineRemoteInv", 78609), ("fsmSamDmeComputeRackUnitOfflineRemoteInv", 78610), ("fsmSamDmeEquipmentLocatorLedSetFiLocatorLedRemoteInv", 78627), ("fsmConfPhysicalRemoteInv", 78630), ("fsmClusterRoleRemoteInv", 78632), ("fsmIlluminateRemoteInv", 78635), ("fsmSetFiLocatorLedRemoteInv", 78636), ("fsmDeployAliasRemoteInv", 78647), ("fsmSamDmeFabricEpMgrConfigureRemoteInv", 78654), ("fsmSamDmeVnicProfileSetDeployAliasRemoteInv", 78663), ("fsmSamDmeSwPhysConfPhysicalRemoteInv", 78679), ("fsmSamDmeExtvmmEpClusterRoleRemoteInv", 78694), ("fsmSamDmeVmLifeCyclePolicyConfigRemoteInv", 78699), ("fsmSamDmeEquipmentBeaconLedIlluminateRemoteInv", 78702), ("fsmSamDmeEtherServerIntfioConfigSpeedRemoteInv", 78711), ("fsmUpdatebiosRemoteInv", 78721), ("fsmSamDmeComputePhysicalActivatebiosRemoteInv", 78722), ("fsmSamDmeFirmwareSystemDeployRemoteInv", 78765), ("fsmSamDmeFirmwareSystemApplyCatalogPackRemoteInv", 78766), ("fsmSamDmeMgmtExportPolicyReportConfigCopyRemoteInv", 78779), ("fsmSamDmeMgmtImporterReportConfigImportRemoteInv", 78780), ("fsmSamDmeNfsMountInstMountRemoteInv", 78788), ("fsmSamDmeNfsMountInstUnmountRemoteInv", 78789), ("fsmSamDmeNfsMountDefReportNfsMountSuspendRemoteInv", 78790), ("fsmSamDmeStorageSystemSyncRemoteInv", 78807), ("fsmSamDmeSwFcSanBorderActivateZoneSetRemoteInv", 78821), ("fsmSamDmeExtpolEpRegisterFsmRemoteInv", 78822), ("fsmSamDmeExtpolRegistryCrossDomainConfigRemoteInv", 78823), ("fsmSamDmeExtpolRegistryCrossDomainDeleteRemoteInv", 78824), ("fsmSamDmeExtpolEpRepairCertRemoteInv", 78839), ("fsmSamDmePolicyControlEpOperateRemoteInv", 78840), ("fsmSamDmePolicyPolicyScopeReleasePolicyFsmRemoteInv", 78842), ("fsmSamDmePolicyPolicyScopeReleaseOperationFsmRemoteInv", 78843), ("fsmSamDmePolicyPolicyScopeReleaseStorageFsmRemoteInv", 78844), ("fsmSamDmePolicyPolicyScopeResolveManyPolicyFsmRemoteInv", 78845), ("fsmSamDmePolicyPolicyScopeResolveManyOperationFsmRemoteInv", 78846), ("fsmSamDmePolicyPolicyScopeResolveManyStorageFsmRemoteInv", 78847), ("fsmSamDmePolicyPolicyScopeReleaseManyPolicyFsmRemoteInv", 78848), ("fsmSamDmePolicyPolicyScopeReleaseManyOperationFsmRemoteInv", 78849), ("fsmSamDmePolicyPolicyScopeReleaseManyStorageFsmRemoteInv", 78850), ("fsmSamDmePolicyPolicyScopeResolveAllPolicyFsmRemoteInv", 78851), ("fsmSamDmePolicyPolicyScopeResolveAllOperationFsmRemoteInv", 78852), ("fsmSamDmePolicyPolicyScopeResolveAllStorageFsmRemoteInv", 78853), ("fsmSamDmePolicyPolicyScopeReleaseAllPolicyFsmRemoteInv", 78854), ("fsmSamDmePolicyPolicyScopeReleaseAllOperationFsmRemoteInv", 78855), ("fsmSamDmePolicyPolicyScopeReleaseAllStorageFsmRemoteInv", 78856), ("fsmSamDmeIdentIdentRequestUpdateIdentRemoteInv", 78858), ("fsmSamDmeIdentMetaSystemSyncRemoteInv", 78859), ("fsmSamDmeMgmtControllerRegistryConfigRemoteInv", 78860), ("fsmSamDmeObserveObservedResolvePolicyFsmRemoteInv", 78865), ("fsmSamDmeObserveObservedResolveResourceFsmRemoteInv", 78866), ("fsmSamDmeObserveObservedResolvevmfsmRemoteInv", 78867), ("fsmSamDmeObserveObservedResolveControllerFsmRemoteInv", 78868), ("fsmSamDmePortpioInCompatSfpReplacedRemoteInv", 78885), ("fsmSamDmeComputePhysicalResetIpmiRemoteInv", 78916), ("fsmSamDmeComputePhysicalFwUpgradeRemoteInv", 78917), ("fsmSamDmeComputeRackUnitAdapterResetRemoteInv", 78918), ("fsmSamDmeComputeServerDiscPolicyResolveScrubPolicyRemoteInv", 78923), ("fsmSamDmeExtpolProviderReportConfigImportRemoteInv", 78925), ("fsmSamDmeFabricVnetEpSyncEpPushVnetEpDeletionRemoteInv", 79039), ("fsmSamDmeGmetaHolderInventoryRemoteInv", 79041), ("fsmSamDmeComputePhysicalCimcSessionDeleteRemoteInv", 79042), ("fsmSamDmeEquipmentiocardFePresenceFsmFail", 999445), ("fsmSamDmeEquipmentiocardFeConnFsmFail", 999446), ("fsmSamDmeEquipmentChassisRemoveChassisFsmFail", 999447), ("fsmSetLocatorLedFsmFail", 999448), ("fsmSamDmeMgmtControllerExtMgmtIfConfigFsmFail", 999558), ("fsmSamDmeFabricComputeSlotEpIdentifyFsmFail", 999559), ("fsmSamDmeComputeBladeDiscoverFsmFail", 999560), ("fsmSamDmeEquipmentChassisPsuPolicyConfigFsmFail", 999573), ("fsmSamDmeAdaptorHostFcIfResetFcPersBindingFsmFail", 999574), ("fsmSamDmeComputeBladeDiagFsmFail", 999575), ("fsmSwitchModeFsmFail", 999579), ("fsmSamDmeVnicProfileSetDeployFsmFail", 999590), ("fsmUpdateSvcEpFsmFail", 999616), ("fsmSamDmeCommSvcEpRestartWebSvcFsmFail", 999617), ("fsmUpdateEpFsmFail", 999619), ("fsmUpdateRealmFsmFail", 999620), ("fsmUpdateUserEpFsmFail", 999621), ("fsmSamDmePkiEpUpdateEpFsmFail", 999622), ("fsmSingleFsmFail", 999640), ("fsmSamDmeSysfileMutationGlobalFsmFail", 999641), ("fsmSamDmeSysdebugManualCoreFileExportTargetExportFsmFail", 999644), ("fsmSamDmeSysdebugAutoCoreFileExportTargetConfigureFsmFail", 999645), ("fsmSamDmeSysdebugLogControlEpLogControlPersistFsmFail", 999646), ("fsmSamDmeSwAccessDomainDeployFsmFail", 999674), ("fsmSamDmeSwEthLanBorderDeployFsmFail", 999675), ("fsmSamDmeSwFcSanBorderDeployFsmFail", 999676), ("fsmSamDmeSwUtilityDomainDeployFsmFail", 999677), ("fsmSamDmeSyntheticFsObjCreateFsmFail", 999681), ("fsmSamDmeFirmwareDownloaderDownloadFsmFail", 999690), ("fsmSamDmeFirmwareImageDeleteFsmFail", 999691), ("fsmUpdateSwitchFsmFail", 999693), ("fsmUpdateiomFsmFail", 999694), ("fsmSamDmeMgmtControllerActivateiomFsmFail", 999695), ("fsmUpdatebmcFsmFail", 999696), ("fsmSamDmeMgmtControllerActivatebmcFsmFail", 999697), ("fsmSamDmeCallhomeEpConfigCallhomeFsmFail", 999710), ("fsmSwMgmtOobIfConfigFsmFail", 999713), ("fsmSwMgmtInbandIfConfigFsmFail", 999714), ("fsmVirtualIfConfigFsmFail", 999719), ("fsmSamDmeMgmtIfEnableVipFsmFail", 999720), ("fsmSamDmeMgmtIfDisableVipFsmFail", 999721), ("fsmSamDmeMgmtIfEnablehaFsmFail", 999722), ("fsmSamDmeMgmtBackupBackupFsmFail", 999723), ("fsmSamDmeMgmtImporterImportFsmFail", 999724), ("fsmSamDmeStatsCollectionPolicyUpdateEpFsmFail", 999782), ("fsmSamDmeQosclassDefinitionConfigGlobalQoSfsmFail", 999785), ("fsmSamDmeEpqosDefinitionDeployFsmFail", 999789), ("fsmSamDmeEpqosDefinitionDelTaskRemoveFsmFail", 999790), ("fsmSamDmeEquipmentiocardResetCmcFsmFail", 999843), ("fsmUpdateucsmanagerFsmFail", 999855), ("fsmSysConfigFsmFail", 999863), ("fsmSamDmeAdaptorExtEthIfPathResetFsmFail", 999892), ("fsmSamDmeAdaptorHostEthIfCircuitResetFsmFail", 999897), ("fsmSamDmeAdaptorHostFcIfCircuitResetFsmFail", 999898), ("fsmSamDmeExtvmmProviderConfigFsmFail", 999919), ("fsmSamDmeExtvmmKeyStoreCertInstallFsmFail", 999920), ("fsmSamDmeExtvmmSwitchDelTaskRemoveProviderFsmFail", 999921), ("fsmSamDmeExtvmmMasterExtKeyConfigFsmFail", 999938), ("fsmUpdaterFsmFail", 999944), ("fsmSamDmeFirmwareDistributableDeleteFsmFail", 999946), ("fsmDiscoverFsmFail", 999960), ("fsmAssociateFsmFail", 999961), ("fsmDisassociateFsmFail", 999962), ("fsmDecommissionFsmFail", 999964), ("fsmSoftShutdownFsmFail", 999965), ("fsmHardShutdownFsmFail", 999966)) + NamedValues(("fsmTurnupFsmFail", 999967), ("fsmPowercycleFsmFail", 999968), ("fsmHardresetFsmFail", 999969), ("fsmSoftresetFsmFail", 999970), ("fsmSwConnUpdFsmFail", 999971), ("fsmBiosRecoveryFsmFail", 999972), ("fsmCmosResetFsmFail", 999974), ("fsmResetBmcFsmFail", 999975), ("fsmUpdateExtUsersFsmFail", 999978), ("fsmUpdateAdaptorFsmFail", 999979), ("fsmActivateAdaptorFsmFail", 999980), ("fsmConfigSoLfsmFail", 999981), ("fsmUnconfigSoLfsmFail", 999982), ("fsmSetFeLocatorLedFsmFail", 999983), ("fsmSamDmeEquipmentChassisPowerCapFsmFail", 999984), ("fsmSamDmeEquipmentiocardMuxOfflineFsmFail", 999985), ("fsmPowerCapFsmFail", 999990), ("fsmUpdateBoardControllerFsmFail", 1000004), ("fsmDeployCatalogueFsmFail", 1000005), ("fsmSamDmeComputePhysicalAssociateFsmFail", 1000013), ("fsmSamDmeComputePhysicalDisassociateFsmFail", 1000014), ("fsmSamDmeComputePhysicalPowerCapFsmFail", 1000015), ("fsmSamDmeComputePhysicalDecommissionFsmFail", 1000016), ("fsmSamDmeComputePhysicalSoftShutdownFsmFail", 1000017), ("fsmSamDmeComputePhysicalHardShutdownFsmFail", 1000018), ("fsmSamDmeComputePhysicalTurnupFsmFail", 1000019), ("fsmSamDmeComputePhysicalPowercycleFsmFail", 1000020), ("fsmSamDmeComputePhysicalHardresetFsmFail", 1000021), ("fsmSamDmeComputePhysicalSoftresetFsmFail", 1000022), ("fsmSamDmeComputePhysicalSwConnUpdFsmFail", 1000023), ("fsmSamDmeComputePhysicalBiosRecoveryFsmFail", 1000024), ("fsmSamDmeComputePhysicalCmosResetFsmFail", 1000026), ("fsmSamDmeComputePhysicalResetBmcFsmFail", 1000027), ("fsmSamDmeEquipmentiocardResetIomFsmFail", 1000028), ("fsmInstallFsmFail", 1000031), ("fsmClearFsmFail", 1000032), ("fsmUpdateFlexlmFsmFail", 1000033), ("fsmSamDmeComputeRackUnitDiscoverFsmFail", 1000034), ("fsmSamDmeLsServerConfigureFsmFail", 1000035), ("fsmSamDmeSwEthMonDeployFsmFail", 1000040), ("fsmSamDmeSwFcMonDeployFsmFail", 1000041), ("fsmSamDmeFabricSanCloudSwitchModeFsmFail", 1000042), ("fsmRemoveFexFsmFail", 1000047), ("fsmSamDmeComputePhysicalUpdateExtUsersFsmFail", 1000048), ("fsmSamDmeSysdebugTechSupportInitiateFsmFail", 1000052), ("fsmSamDmeSysdebugTechSupportDeleteTechSupFileFsmFail", 1000053), ("fsmSamDmeSysdebugTechSupportDownloadFsmFail", 1000054), ("fsmActivateCatalogFsmFail", 1000057), ("fsmActivateMgmtExtFsmFail", 1000058), ("fsmSamDmeComputePhysicalUpdateAdaptorFsmFail", 1000083), ("fsmSamDmeComputePhysicalActivateAdaptorFsmFail", 1000084), ("fsmSamDmeCapabilityCatalogueActivateCatalogFsmFail", 1000085), ("fsmSamDmeCapabilityMgmtExtensionActivateMgmtExtFsmFail", 1000086), ("fsmSamDmeLicenseDownloaderDownloadFsmFail", 1000090), ("fsmSamDmeLicenseFileInstallFsmFail", 1000091), ("fsmSamDmeLicenseFileClearFsmFail", 1000092), ("fsmSamDmeLicenseInstanceUpdateFlexlmFsmFail", 1000093), ("fsmConfigureFsmFail", 1000100), ("fsmMuxOfflineFsmFail", 1000101), ("fsmSamDmeComputePhysicalConfigSoLfsmFail", 1000123), ("fsmSamDmeComputePhysicalUnconfigSoLfsmFail", 1000124), ("fsmSamDmePortpioInCompatSfpPresenceFsmFail", 1000129), ("fsmSamDmeComputePhysicalDiagnosticInterruptFsmFail", 1000156), ("fsmSamDmeSysdebugCoreDownloadFsmFail", 1000173), ("fsmSamDmeEquipmentChassisDynamicReallocationFsmFail", 1000174), ("fsmSamDmeComputePhysicalResetKvmFsmFail", 1000203), ("fsmSamDmeMgmtControllerOnlineFsmFail", 1000209), ("fsmSamDmeComputeRackUnitOfflineFsmFail", 1000210), ("fsmSamDmeEquipmentLocatorLedSetFiLocatorLedFsmFail", 1000227), ("fsmConfPhysicalFsmFail", 1000230), ("fsmClusterRoleFsmFail", 1000232), ("fsmIlluminateFsmFail", 1000235), ("fsmSetFiLocatorLedFsmFail", 1000236), ("fsmDeployAliasFsmFail", 1000247), ("fsmSamDmeFabricEpMgrConfigureFsmFail", 1000254), ("fsmSamDmeVnicProfileSetDeployAliasFsmFail", 1000263), ("fsmSamDmeSwPhysConfPhysicalFsmFail", 1000279), ("fsmSamDmeExtvmmEpClusterRoleFsmFail", 1000294), ("fsmSamDmeVmLifeCyclePolicyConfigFsmFail", 1000299), ("fsmSamDmeEquipmentBeaconLedIlluminateFsmFail", 1000302), ("fsmSamDmeEtherServerIntfioConfigSpeedFsmFail", 1000311), ("fsmUpdatebiosFsmFail", 1000321), ("fsmSamDmeComputePhysicalActivatebiosFsmFail", 1000322), ("fsmSamDmeFirmwareSystemDeployFsmFail", 1000365), ("fsmSamDmeFirmwareSystemApplyCatalogPackFsmFail", 1000366), ("fsmSamDmeMgmtExportPolicyReportConfigCopyFsmFail", 1000379), ("fsmSamDmeMgmtImporterReportConfigImportFsmFail", 1000380), ("fsmSamDmeNfsMountInstMountFsmFail", 1000388), ("fsmSamDmeNfsMountInstUnmountFsmFail", 1000389), ("fsmSamDmeNfsMountDefReportNfsMountSuspendFsmFail", 1000390), ("fsmSamDmeStorageSystemSyncFsmFail", 1000407), ("fsmSamDmeSwFcSanBorderActivateZoneSetFsmFail", 1000421), ("fsmSamDmeExtpolEpRegisterFsmFsmFail", 1000422), ("fsmSamDmeExtpolRegistryCrossDomainConfigFsmFail", 1000423), ("fsmSamDmeExtpolRegistryCrossDomainDeleteFsmFail", 1000424), ("fsmSamDmeExtpolEpRepairCertFsmFail", 1000439), ("fsmSamDmePolicyControlEpOperateFsmFail", 1000440), ("fsmSamDmePolicyPolicyScopeReleasePolicyFsmFsmFail", 1000442), ("fsmSamDmePolicyPolicyScopeReleaseOperationFsmFsmFail", 1000443), ("fsmSamDmePolicyPolicyScopeReleaseStorageFsmFsmFail", 1000444), ("fsmSamDmePolicyPolicyScopeResolveManyPolicyFsmFsmFail", 1000445), ("fsmSamDmePolicyPolicyScopeResolveManyOperationFsmFsmFail", 1000446), ("fsmSamDmePolicyPolicyScopeResolveManyStorageFsmFsmFail", 1000447), ("fsmSamDmePolicyPolicyScopeReleaseManyPolicyFsmFsmFail", 1000448), ("fsmSamDmePolicyPolicyScopeReleaseManyOperationFsmFsmFail", 1000449), ("fsmSamDmePolicyPolicyScopeReleaseManyStorageFsmFsmFail", 1000450), ("fsmSamDmePolicyPolicyScopeResolveAllPolicyFsmFsmFail", 1000451), ("fsmSamDmePolicyPolicyScopeResolveAllOperationFsmFsmFail", 1000452), ("fsmSamDmePolicyPolicyScopeResolveAllStorageFsmFsmFail", 1000453), ("fsmSamDmePolicyPolicyScopeReleaseAllPolicyFsmFsmFail", 1000454), ("fsmSamDmePolicyPolicyScopeReleaseAllOperationFsmFsmFail", 1000455), ("fsmSamDmePolicyPolicyScopeReleaseAllStorageFsmFsmFail", 1000456), ("fsmSamDmeIdentIdentRequestUpdateIdentFsmFail", 1000458), ("fsmSamDmeIdentMetaSystemSyncFsmFail", 1000459), ("fsmSamDmeMgmtControllerRegistryConfigFsmFail", 1000460), ("fsmSamDmeObserveObservedResolvePolicyFsmFsmFail", 1000465), ("fsmSamDmeObserveObservedResolveResourceFsmFsmFail", 1000466), ("fsmSamDmeObserveObservedResolvevmfsmFsmFail", 1000467), ("fsmSamDmeObserveObservedResolveControllerFsmFsmFail", 1000468), ("fsmSamDmePortpioInCompatSfpReplacedFsmFail", 1000485), ("fsmSamDmeComputePhysicalResetIpmiFsmFail", 1000516), ("fsmSamDmeComputePhysicalFwUpgradeFsmFail", 1000517), ("fsmSamDmeComputeRackUnitAdapterResetFsmFail", 1000518), ("fsmSamDmeComputeServerDiscPolicyResolveScrubPolicyFsmFail", 1000523), ("fsmSamDmeExtpolProviderReportConfigImportFsmFail", 1000525), ("fsmSamDmeFabricVnetEpSyncEpPushVnetEpDeletionFsmFail", 1000639), ("fsmSamDmeGmetaHolderInventoryFsmFail", 1000641), ("fsmSamDmeComputePhysicalCimcSessionDeleteFsmFail", 1000642), ("unrVnicTemplStatsPolicyName", 4522530), ("unrVnicSanConnTemplQosPolicyName", 4522532), ("unrVnicIpV4PooledAddrName", 4522544), ("unrVnicVnicPinToGroupName", 4522556), ("unrVnicVnicStatsPolicyName", 4522561), ("unrVnicProfileQosPolicyName", 4522588), ("unrVnicFcNodeIdentPoolName", 4522603), ("unrLsServerSrcTemplName", 4525234), ("unrLsServerIdentPoolName", 4525239), ("unrLsServerBootPolicyName", 4525240), ("unrLsServerLocalDiskPolicyName", 4525241), ("unrLsServerScrubPolicyName", 4525247), ("unrLsServerDynamicConPolicyName", 4525248), ("unrLsServerHostFwPolicyName", 4525250), ("unrLsServerMgmtFwPolicyName", 4525251), ("unrLsServerMgmtAccessPolicyName", 4525252), ("unrLsServerSolPolicyName", 4525253), ("unrLsServerStatsPolicyName", 4525254), ("unrVnicEtherBaseQosPolicyName", 4526517), ("unrVnicEtherBaseNwCtrlPolicyName", 4526850), ("unrVnicProfileNwCtrlPolicyName", 4526851), ("unrLsServerVconProfileName", 4526901), ("unrLsServerBiosProfileName", 4526902), ("unrLsRequirementName", 4527601), ("unrLsServerPowerPolicyName", 4528591), ("unrLsServerMaintPolicyName", 4528596), ("unrVnicSanConnTemplIdentPoolName", 4528609), ("unrVnicLanConnTemplNwCtrlPolicyName", 4528611), ("unrVnicLanConnTemplIdentPoolName", 4528613), ("unrVnicFcBaseAdaptorProfileName", 4528616), ("unrVnicFcBaseIdentPoolName", 4528618), ("unrVnicFcBaseNwTemplName", 4528620), ("unrVnicEtherBaseAdaptorProfileName", 4528623), ("unrVnicEtherBaseIdentPoolName", 4528625), ("unrVnicEtherBaseNwTemplName", 4528627), ("unrVnicLanConnTemplQosPolicyName", 4528680), ("unrVnicFcBaseQosPolicyName", 4528682), ("unrTrigTriggerableScheduler", 4528842), ("unrFabricEthEstcEpNwCtrlPolicyName", 4529444), ("unrFabricEthEstcPcNwCtrlPolicyName", 4529447), ("unrVnicIscsiIdentPoolName", 4529601), ("unrVnicIscsiAuthProfileName", 4529604), ("unrVnicIscsiConfProfileName", 4529606), ("unrVnicIscsiStaticTargetIfAuthProfileName", 4529615), ("unrVnicIpv4PooledIscsiAddrIdentPoolName", 4529838), ("unrVnicIscsiIqnIdentPoolName", 4529847), ("unrVnicIscsiAdaptorProfileName", 4529849), ("unrVnicFcBasePinToGroupName", 4529971), ("unrVnicEtherBasePinToGroupName", 4529973), ("unrFaultSuppressTaskSuppressPolicyName", 4530050), ("unrVnicFcGroupTemplStorageConnPolicyName", 4530085), ("unrVnicAgroupStatsPolicyName", 4530100), ("unrVnicFcGroupDefStorageConnPolicyName", 4530109), ("unrVnicIscsiBaseIdentPoolName", 4530112), ("unrVnicIscsiBaseAdaptorProfileName", 4530114), ("unrVnicDynamicConPolicyRefConPolicyName", 4530117), ("unrVnicConnDefLanConnPolicyName", 4530119), ("unrVnicConnDefSanConnPolicyName", 4530121), ("unrFabricVlanMcastPolicyName", 4530139), ("unrVnicIscsiBootVnicIqnIdentPoolName", 4530389), ("unrVnicIscsiBootVnicAuthProfileName", 4530391), ("unrLsServerExtippoolName", 4530407), ("unrVnicIscsiNodeIqnIdentPoolName", 4531275))

class CucsConditionSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 0), ("info", 1), ("condition", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6))

class CucsConditionTag(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("network", 1), ("storage", 2), ("pod", 3), ("security", 4), ("operations", 5), ("fsmstagefail", 6), ("fsmstageretry", 7), ("fsmstageremoteinv", 8))

class CucsConditionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 65535))
    namedValues = NamedValues(("generic", 0), ("fsm", 1), ("management", 2), ("equipment", 3), ("network", 4), ("server", 5), ("configuration", 6), ("environmental", 7), ("connectivity", 8), ("sysdebug", 9), ("operational", 10), ("snmpUserNotDeployed", 11), ("profileConfigQualifier", 12), ("callhome", 17), ("any", 65535))

class CucsConfigImpactResponseState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notStarted", 0), ("waiting", 1), ("complete", 2))

class CucsConfigSorterDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ascending", 0), ("descending", 1))

class CucsDcxAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("enabled", 0), ("disabled", 1))

class CucsDcxNsAllocStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("available", 0), ("full", 1), ("exceeded", 2))

class CucsDcxOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("adminDown", 1), ("linkDown", 2), ("error", 3), ("active", 4), ("passive", 5))

class CucsDcxProtState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noProtection", 0), ("active", 1), ("passive", 2))

class CucsDcxState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("present", 1), ("creating", 2), ("modifying", 3), ("destroying", 4), ("createPend", 5), ("modifyPend", 6), ("destroyPend", 7))

class CucsDcxVIfProtRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unprotected", 0), ("primary", 1), ("backup", 2))

class CucsDiagAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ready", 0), ("trigger", 1), ("cancel", 2))

class CucsDiagBladeTestType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("disk", 0), ("processor", 1), ("memory", 2), ("memtest", 3), ("stress", 4), ("pci", 5))

class CucsDiagFailureAction(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("techSupport", 0), ("waitDebug", 1), ("skipRemaining", 2))

class CucsDiagNetworkTestType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("eth", 0), ("fc", 1))

class CucsDiagSrvCtrlType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 33))
    namedValues = NamedValues(("full", 1), ("efi", 33))

class CucsDiagStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("complete", 0), ("inProgress", 1), ("failed", 2), ("notRun", 3), ("cancelled", 4), ("scheduled", 5))

class CucsDiagStatusIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("testFailure", 0), ("runCancelled", 1), ("componentError", 2), ("stagesCompleted", 3), ("stageFailed", 4))

class CucsDiagSuccessAction(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("techSupport", 0), ("waitDebug", 1))

class CucsDiagTestOrder(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 64)

class CucsDpsecForgedTransmit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("allow", 0), ("deny", 1))

class CucsEpqosDefinitionDelTaskFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 319))
    namedValues = NamedValues(("nop", 0), ("remove", 319))

class CucsEpqosDefinitionDelTaskFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 319, 320, 321, 370, 371))
    namedValues = NamedValues(("nop", 0), ("removeBegin", 319), ("removeLocal", 320), ("removePeer", 321), ("removeFail", 370), ("removeSuccess", 371))

class CucsEpqosDefinitionDelTaskFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 319))
    namedValues = NamedValues(("nop", 0), ("remove", 319))

class CucsEpqosDefinitionFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 316))
    namedValues = NamedValues(("nop", 0), ("deploy", 316))

class CucsEpqosDefinitionFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 316, 317, 318, 372, 373))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 316), ("deployLocal", 317), ("deployPeer", 318), ("deployFail", 372), ("deploySuccess", 373))

class CucsEpqosDefinitionFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 316))
    namedValues = NamedValues(("nop", 0), ("deploy", 316))

class CucsEquipmentAdminPowerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("policy", 1), ("cycleImmediate", 2), ("cycleWait", 3))

class CucsEquipmentAirflowDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("frontToBack", 1), ("backToFront", 2))

class CucsEquipmentAsicType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("gatos", 1), ("carmel", 2))

class CucsEquipmentBeaconLedFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1135))
    namedValues = NamedValues(("nop", 0), ("illuminate", 1135))

class CucsEquipmentBeaconLedFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1135, 1136, 1137, 1138, 1139))
    namedValues = NamedValues(("nop", 0), ("illuminateBegin", 1135), ("illuminateExecuteA", 1136), ("illuminateExecuteB", 1137), ("illuminateFail", 1138), ("illuminateSuccess", 1139))

class CucsEquipmentBeaconLedFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1089))
    namedValues = NamedValues(("nop", 0), ("illuminate", 1089))

class CucsEquipmentBeaconLedState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("on", 1), ("off", 2), ("blinking", 3), ("eth", 4), ("fc", 5))

class CucsEquipmentBiosUpdateMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("managementController", 1), ("pnuos", 2))

class CucsEquipmentChassisId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsEquipmentChassisAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("acknowledged", 1), ("reAcknowledge", 2), ("decommission", 3), ("remove", 4), ("enablePortChannel", 5), ("disablePortChannel", 6), ("autoAcknowledge", 7))

class CucsEquipmentChassisConfigProgressIndicator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ackNotInProgress", 0), ("ackInProgress", 1))

class CucsEquipmentChassisConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 6, 7, 8, 9))
    namedValues = NamedValues(("unInitialized", 0), ("unAcknowledged", 1), ("unsupportedConnectivity", 2), ("ok", 3), ("removing", 4), ("ackInProgress", 6), ("evaluation", 7), ("acknowledged", 8), ("autoAck", 9))

class CucsEquipmentChassisFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 9, 140, 643, 1048))
    namedValues = NamedValues(("nop", 0), ("removeChassis", 9), ("psuPolicyConfig", 140), ("powerCap", 643), ("dynamicReallocation", 1048))

class CucsEquipmentChassisFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 9, 10, 11, 12, 13, 14, 140, 141, 374, 375, 376, 377, 643, 644, 980, 981, 1048, 1049, 1051, 1052))
    namedValues = NamedValues(("nop", 0), ("removeChassisBegin", 9), ("removeChassisDecomission", 10), ("removeChassisDisableEndPoint", 11), ("removeChassisUnIdentifyLocal", 12), ("removeChassisUnIdentifyPeer", 13), ("removeChassisWait", 14), ("psuPolicyConfigBegin", 140), ("psuPolicyConfigExecute", 141), ("psuPolicyConfigFail", 374), ("psuPolicyConfigSuccess", 375), ("removeChassisFail", 376), ("removeChassisSuccess", 377), ("powerCapBegin", 643), ("powerCapConfig", 644), ("powerCapFail", 980), ("powerCapSuccess", 981), ("dynamicReallocationBegin", 1048), ("dynamicReallocationConfig", 1049), ("dynamicReallocationFail", 1051), ("dynamicReallocationSuccess", 1052))

class CucsEquipmentChassisFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 9, 140, 829, 1048))
    namedValues = NamedValues(("nop", 0), ("removeChassis", 9), ("psuPolicyConfig", 140), ("powerCap", 829), ("dynamicReallocation", 1048))

class CucsEquipmentChassisIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("chassisThermal", 0), ("chassisInoperable", 1), ("chassisVoltage", 2), ("chassisPerf", 3), ("chassisPower", 4), ("removed", 5), ("config", 6), ("chassisPostFailure", 7), ("psuThermal", 8), ("psuInoperable", 9), ("psuVoltage", 10), ("psuPerf", 11), ("psuPower", 12), ("fanThermal", 13), ("fanInoperable", 14), ("fanVoltage", 15), ("fanPerf", 16), ("fanPower", 17), ("iocardThermal", 18), ("iocardInoperable", 19), ("iocardVoltage", 20), ("iocardPerf", 21), ("iocardPower", 22), ("computeThermal", 23), ("computeInoperable", 24), ("computeVoltage", 25), ("computePerf", 26), ("computePower", 27), ("iocardInaccessible", 28), ("fabricConnProblem", 29), ("fabricUnsupportedConn", 30), ("chassisLimitExceeded", 31), ("chassisVifCapacityReduced", 32), ("chassisPortChannelEnabled", 33), ("chassisUnsupported", 34))

class CucsEquipmentChassisPowerOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("failed", 2), ("inputFailed", 3), ("inputDegraded", 4), ("outputFailed", 5), ("outputDegraded", 6), ("redundancyFailed", 7), ("redundancyDegraded", 8))

class CucsEquipmentChassisStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("inputPower", 0), ("inputPowerAvg", 1), ("inputPowerMax", 2), ("inputPowerMin", 3), ("outputPower", 4), ("outputPowerAvg", 5), ("outputPowerMax", 6), ("outputPowerMin", 7))

class CucsEquipmentChassisStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("inputPower", 0), ("inputPowerAvg", 1), ("inputPowerMax", 2), ("inputPowerMin", 3), ("outputPower", 4), ("outputPowerAvg", 5), ("outputPowerMax", 6), ("outputPowerMin", 7))

class CucsEquipmentCommStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("connected", 1), ("disconnected", 2))

class CucsEquipmentConnectionStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("a", 0), ("b", 1))

class CucsEquipmentDiscoveryCapOperPowerRequirement(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("standby", 1), ("full", 2))

class CucsEquipmentDiscoveryState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("online", 1), ("offline", 2), ("discovered", 3), ("unsupportedConnectivity", 4), ("autoUpgrading", 5))

class CucsEquipmentFanId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsEquipmentFanModule(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsEquipmentFanTray(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsEquipmentFanModuleId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsEquipmentFanModuleTray(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 1)

class CucsEquipmentFanModuleStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3))

class CucsEquipmentFanModuleStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3))

class CucsEquipmentFanStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("speed", 0), ("speedAvg", 1), ("speedMax", 2), ("speedMin", 3))

class CucsEquipmentFanStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("speed", 0), ("speedAvg", 1), ("speedMax", 2), ("speedMin", 3))

class CucsEquipmentFexId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 255)

class CucsEquipmentFexCapProviderRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mgmt", 1), ("data", 2), ("full", 3))

class CucsEquipmentFexEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("die1", 0), ("die1Avg", 1), ("die1Max", 2), ("die1Min", 3), ("inlet", 4), ("inlet1", 5), ("inlet1Avg", 6), ("inlet1Max", 7), ("inlet1Min", 8), ("inletAvg", 9), ("inletMax", 10), ("inletMin", 11), ("outlet1", 12), ("outlet1Avg", 13), ("outlet1Max", 14), ("outlet1Min", 15), ("outlet2", 16), ("outlet2Avg", 17), ("outlet2Max", 18), ("outlet2Min", 19))

class CucsEquipmentFexEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("die1", 0), ("die1Avg", 1), ("die1Max", 2), ("die1Min", 3), ("inlet", 4), ("inlet1", 5), ("inlet1Avg", 6), ("inlet1Max", 7), ("inlet1Min", 8), ("inletAvg", 9), ("inletMax", 10), ("inletMin", 11), ("outlet1", 12), ("outlet1Avg", 13), ("outlet1Max", 14), ("outlet1Min", 15), ("outlet2", 16), ("outlet2Avg", 17), ("outlet2Max", 18), ("outlet2Min", 19))

class CucsEquipmentFexFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 636))
    namedValues = NamedValues(("nop", 0), ("removeFex", 636))

class CucsEquipmentFexFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 636, 637, 638, 639, 640, 982, 983))
    namedValues = NamedValues(("nop", 0), ("removeFexBegin", 636), ("removeFexDecomission", 637), ("removeFexUnIdentifyLocal", 638), ("removeFexCleanupEntries", 639), ("removeFexWait", 640), ("removeFexFail", 982), ("removeFexSuccess", 983))

class CucsEquipmentFexFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 887))
    namedValues = NamedValues(("nop", 0), ("removeFex", 887))

class CucsEquipmentFexPowerSummaryThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("modulePower", 0), ("modulePowerAvg", 1), ("modulePowerMax", 2), ("modulePowerMin", 3), ("availablePower", 4), ("availablePowerAvg", 5), ("availablePowerMax", 6), ("availablePowerMin", 7), ("reservedPower", 8), ("reservedPowerAvg", 9), ("reservedPowerMax", 10), ("reservedPowerMin", 11), ("totalPower", 12), ("totalPowerAvg", 13), ("totalPowerMax", 14), ("totalPowerMin", 15))

class CucsEquipmentFexPowerSummaryHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("modulePower", 0), ("modulePowerAvg", 1), ("modulePowerMax", 2), ("modulePowerMin", 3), ("availablePower", 4), ("availablePowerAvg", 5), ("availablePowerMax", 6), ("availablePowerMin", 7), ("reservedPower", 8), ("reservedPowerAvg", 9), ("reservedPowerMax", 10), ("reservedPowerMin", 11), ("totalPower", 12), ("totalPowerAvg", 13), ("totalPowerMax", 14), ("totalPowerMin", 15))

class CucsEquipmentFexPsuInputStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("current", 0), ("currentAvg", 1), ("currentMax", 2), ("currentMin", 3), ("power", 4), ("powerAvg", 5), ("powerMax", 6), ("powerMin", 7), ("voltage", 8), ("voltageAvg", 9), ("voltageMax", 10), ("voltageMin", 11))

class CucsEquipmentFexPsuInputStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("current", 0), ("currentAvg", 1), ("currentMax", 2), ("currentMin", 3), ("power", 4), ("powerAvg", 5), ("powerMax", 6), ("powerMin", 7), ("voltage", 8), ("voltageAvg", 9), ("voltageMax", 10), ("voltageMin", 11))

class CucsEquipmentHealthLedState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("normal", 0), ("minor", 1), ("critical", 2))

class CucsEquipmentIOCardId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 2)

class CucsEquipmentIOCardFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 461, 645, 817))
    namedValues = NamedValues(("nop", 0), ("fePresence", 1), ("feConn", 3), ("resetCmc", 461), ("muxOffline", 645), ("resetIom", 817))

class CucsEquipmentIOCardFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 378, 379, 380, 381, 461, 462, 465, 466, 544, 645, 646, 817, 818, 984, 985, 986, 987))
    namedValues = NamedValues(("nop", 0), ("fePresenceBegin", 1), ("fePresenceIdentify", 2), ("feConnBegin", 3), ("feConnConfigureSwMgmtEndPoint", 4), ("feConnConfigureVifNs", 5), ("feConnConfigureEndPoint", 6), ("feConnDiscoverChassis", 7), ("feConnEnableChassis", 8), ("feConnFail", 378), ("feConnSuccess", 379), ("fePresenceFail", 380), ("fePresenceSuccess", 381), ("resetCmcBegin", 461), ("resetCmcExecute", 462), ("resetCmcFail", 465), ("resetCmcSuccess", 466), ("fePresenceCheckLicense", 544), ("muxOfflineBegin", 645), ("muxOfflineCleanupEntries", 646), ("resetIomBegin", 817), ("resetIomExecute", 818), ("muxOfflineFail", 984), ("muxOfflineSuccess", 985), ("resetIomFail", 986), ("resetIomSuccess", 987))

class CucsEquipmentIOCardFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 3, 461, 961, 978))
    namedValues = NamedValues(("nop", 0), ("fePresence", 1), ("feConn", 3), ("resetCmc", 461), ("resetIom", 961), ("muxOffline", 978))

class CucsEquipmentIOCardIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("thermal", 0), ("inoperable", 1), ("voltage", 2), ("perf", 3), ("power", 4), ("removed", 5), ("fabricPortProblem", 6), ("postFailure", 7), ("serverPortProblem", 8), ("vifCapacityReduced", 9), ("fabricpcLinkAutoAckFailed", 10))

class CucsEquipmentIOCardStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("temp", 4), ("tempAvg", 5), ("tempMax", 6), ("tempMin", 7))

class CucsEquipmentIOCardStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("temp", 4), ("tempAvg", 5), ("tempMax", 6), ("tempMin", 7))

class CucsEquipmentInternalFanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("chassis", 0), ("switch", 1), ("fex", 2))

class CucsEquipmentIsSupported(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CucsEquipmentLedColor(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("green", 1), ("amber", 2), ("red", 3), ("blue", 4))

class CucsEquipmentLedLocatorState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inactive", 0), ("off", 1), ("on", 2))

class CucsEquipmentLedOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("on", 1), ("off", 2), ("blinking", 3), ("eth", 4), ("fc", 5))

class CucsEquipmentLocatorLedFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 15, 641, 1090))
    namedValues = NamedValues(("nop", 0), ("setLocatorLed", 15), ("setFeLocatorLed", 641), ("setFiLocatorLed", 1090))

class CucsEquipmentLocatorLedFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 15, 16, 382, 383, 641, 642, 988, 989, 1090, 1091, 1140, 1141))
    namedValues = NamedValues(("nop", 0), ("setLocatorLedBegin", 15), ("setLocatorLedExecute", 16), ("setLocatorLedFail", 382), ("setLocatorLedSuccess", 383), ("setFeLocatorLedBegin", 641), ("setFeLocatorLedExecute", 642), ("setFeLocatorLedFail", 988), ("setFeLocatorLedSuccess", 989), ("setFiLocatorLedBegin", 1090), ("setFiLocatorLedExecute", 1091), ("setFiLocatorLedFail", 1140), ("setFiLocatorLedSuccess", 1141))

class CucsEquipmentLocatorLedFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 15, 641, 1119))
    namedValues = NamedValues(("nop", 0), ("setLocatorLed", 15), ("setFeLocatorLed", 641), ("setFiLocatorLed", 1119))

class CucsEquipmentMemoryUnitDiscoveryModifierAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("setRevToOne", 1), ("setRev", 2), ("setRevStrict", 3))

class CucsEquipmentMethod(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("post", 0), ("configCheck", 1), ("diagCheck", 2), ("selCheck", 3))

class CucsEquipmentNetworkElementFanStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("drivePercentage", 0), ("drivePercentageAvg", 1), ("drivePercentageMax", 2), ("drivePercentageMin", 3), ("speed", 4), ("speedAvg", 5), ("speedMax", 6), ("speedMin", 7))

class CucsEquipmentNetworkElementFanStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("drivePercentage", 0), ("drivePercentageAvg", 1), ("drivePercentageMax", 2), ("drivePercentageMin", 3), ("speed", 4), ("speedAvg", 5), ("speedMax", 6), ("speedMin", 7))

class CucsEquipmentOperability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 51, 52, 81, 82, 83, 84, 100, 101, 102, 103, 104, 105, 106, 107, 108))
    namedValues = NamedValues(("unknown", 0), ("operable", 1), ("inoperable", 2), ("degraded", 3), ("poweredOff", 4), ("powerProblem", 5), ("removed", 6), ("voltageProblem", 7), ("thermalProblem", 8), ("performanceProblem", 9), ("accessibilityProblem", 10), ("identityUnestablishable", 11), ("biosPostTimeout", 12), ("disabled", 13), ("malformedFru", 14), ("fabricConnProblem", 51), ("fabricUnsupportedConn", 52), ("config", 81), ("equipmentProblem", 82), ("decomissioning", 83), ("chassisLimitExceeded", 84), ("notSupported", 100), ("discovery", 101), ("discoveryFailed", 102), ("identify", 103), ("postFailure", 104), ("upgradeProblem", 105), ("peerCommProblem", 106), ("autoUpgrade", 107), ("linkActivateBlocked", 108))

class CucsEquipmentPOSTRecoverability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("recoverable", 1), ("nonRecoverable", 2))

class CucsEquipmentPictureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("front", 1), ("back", 2), ("top", 3), ("bottom", 4), ("left", 5), ("right", 6))

class CucsEquipmentPowerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 100))
    namedValues = NamedValues(("unknown", 0), ("on", 1), ("test", 2), ("off", 3), ("online", 4), ("offline", 5), ("offduty", 6), ("degraded", 7), ("powerSave", 8), ("error", 9), ("ok", 10), ("failed", 11), ("notSupported", 100))

class CucsEquipmentPresence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 10, 11, 12, 13, 20, 21, 22, 30, 40, 100))
    namedValues = NamedValues(("unknown", 0), ("empty", 1), ("equipped", 10), ("missing", 11), ("mismatch", 12), ("equippedNotPrimary", 13), ("equippedIdentityUnestablishable", 20), ("mismatchIdentityUnestablishable", 21), ("equippedWithMalformedFru", 22), ("inaccessible", 30), ("unauthorized", 40), ("notSupported", 100))

class CucsEquipmentPsuType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ac", 1), ("dc", 2))

class CucsEquipmentPsuId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsEquipmentPsuInputStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("current", 0), ("currentAvg", 1), ("currentMax", 2), ("currentMin", 3), ("power", 4), ("powerAvg", 5), ("powerMax", 6), ("powerMin", 7), ("voltage", 8), ("voltageAvg", 9), ("voltageMax", 10), ("voltageMin", 11))

class CucsEquipmentPsuInputStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("current", 0), ("currentAvg", 1), ("currentMax", 2), ("currentMin", 3), ("power", 4), ("powerAvg", 5), ("powerMax", 6), ("powerMin", 7), ("voltage", 8), ("voltageAvg", 9), ("voltageMax", 10), ("voltageMin", 11))

class CucsEquipmentPsuOutputStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("current", 0), ("currentAvg", 1), ("currentMax", 2), ("currentMin", 3), ("power", 4), ("powerAvg", 5), ("powerMax", 6), ("powerMin", 7), ("voltage", 8), ("voltageAvg", 9), ("voltageMax", 10), ("voltageMin", 11))

class CucsEquipmentPsuOutputStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("current", 0), ("currentAvg", 1), ("currentMax", 2), ("currentMin", 3), ("power", 4), ("powerAvg", 5), ("powerMax", 6), ("powerMin", 7), ("voltage", 8), ("voltageAvg", 9), ("voltageMax", 10), ("voltageMin", 11))

class CucsEquipmentPsuStateQualifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 0), ("failure", 1), ("overCurrent", 2), ("overTemperature", 3), ("inputLoss", 4), ("fanFailure", 5), ("inputCurrentWarning", 6), ("inputVoltageWarning", 7), ("ambientTemperatureWarning", 8), ("outputCurrentWarning", 9))

class CucsEquipmentPsuStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("input210v", 4), ("input210vAvg", 5), ("input210vMax", 6), ("input210vMin", 7), ("output12v", 8), ("output12vAvg", 9), ("output12vMax", 10), ("output12vMin", 11), ("output3v3", 12), ("output3v3Avg", 13), ("output3v3Max", 14), ("output3v3Min", 15), ("outputCurrent", 16), ("outputCurrentAvg", 17), ("outputCurrentMax", 18), ("outputCurrentMin", 19), ("outputPower", 20), ("outputPowerAvg", 21), ("outputPowerMax", 22), ("outputPowerMin", 23))

class CucsEquipmentPsuStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("input210v", 4), ("input210vAvg", 5), ("input210vMax", 6), ("input210vMin", 7), ("output12v", 8), ("output12vAvg", 9), ("output12vMax", 10), ("output12vMin", 11), ("output3v3", 12), ("output3v3Avg", 13), ("output3v3Max", 14), ("output3v3Min", 15), ("outputCurrent", 16), ("outputCurrentAvg", 17), ("outputCurrentMax", 18), ("outputCurrentMin", 19), ("outputPower", 20), ("outputPowerAvg", 21), ("outputPowerMax", 22), ("outputPowerMin", 23))

class CucsEquipmentRackUnitFanStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("speed", 0), ("speedAvg", 1), ("speedMax", 2), ("speedMin", 3))

class CucsEquipmentRackUnitFanStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("speed", 0), ("speedAvg", 1), ("speedMax", 2), ("speedMin", 3))

class CucsEquipmentRackUnitPsuStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("inputPower", 4), ("inputPowerAvg", 5), ("inputPowerMax", 6), ("inputPowerMin", 7), ("inputVoltage", 8), ("inputVoltageAvg", 9), ("inputVoltageMax", 10), ("inputVoltageMin", 11), ("outputCurrent", 12), ("outputCurrentAvg", 13), ("outputCurrentMax", 14), ("outputCurrentMin", 15), ("outputPower", 16), ("outputPowerAvg", 17), ("outputPowerMax", 18), ("outputPowerMin", 19), ("outputVoltage", 20), ("outputVoltageAvg", 21), ("outputVoltageMax", 22), ("outputVoltageMin", 23))

class CucsEquipmentRackUnitPsuStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ambientTemp", 0), ("ambientTempAvg", 1), ("ambientTempMax", 2), ("ambientTempMin", 3), ("inputPower", 4), ("inputPowerAvg", 5), ("inputPowerMax", 6), ("inputPowerMin", 7), ("inputVoltage", 8), ("inputVoltageAvg", 9), ("inputVoltageMax", 10), ("inputVoltageMin", 11), ("outputCurrent", 12), ("outputCurrentAvg", 13), ("outputCurrentMax", 14), ("outputCurrentMin", 15), ("outputPower", 16), ("outputPowerAvg", 17), ("outputPowerMax", 18), ("outputPowerMin", 19), ("outputVoltage", 20), ("outputVoltageAvg", 21), ("outputVoltageMax", 22), ("outputVoltageMin", 23))

class CucsEquipmentRemovalConditions(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("notApplicable", 2), ("removableWhenOff", 3), ("removableWhenOnOrOff", 4))

class CucsEquipmentResetOn(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("update", 1), ("activate", 2))

class CucsEquipmentSecureBios(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("notSupported", 1), ("supported", 2))

class CucsEquipmentSensorThresholdStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 100))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("upperNonRecoverable", 2), ("upperCritical", 3), ("upperNonCritical", 4), ("lowerNonCritical", 5), ("lowerCritical", 6), ("lowerNonRecoverable", 7), ("notSupported", 100))

class CucsEquipmentSlotArrayLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("front", 1), ("back", 2), ("top", 3), ("bottom", 4), ("left", 5), ("right", 6))

class CucsEquipmentSlotArrayOrientation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("vertical", 1), ("horizontal", 2))

class CucsEquipmentSlotArraySelector(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("unknown", 0), ("psu", 1), ("fan", 2), ("iocard", 3), ("diskSlot", 5), ("driveSlot", 6), ("usbPort", 7), ("ethernetPort", 8), ("comPort", 9), ("parPort", 10), ("vgaPort", 11), ("dviPort", 12), ("keyboardPort", 13), ("mousePort", 14), ("gem", 15), ("blade", 16))

class CucsEquipmentSlotSpanOrientation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("inline", 1), ("transverse", 2))

class CucsEquipmentSlotStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 10, 11, 12, 13, 20, 21, 22, 30, 40))
    namedValues = NamedValues(("unknown", 0), ("empty", 1), ("equipped", 10), ("missing", 11), ("mismatch", 12), ("equippedNotPrimary", 13), ("equippedIdentityUnestablishable", 20), ("mismatchIdentityUnestablishable", 21), ("equippedWithMalformedFru", 22), ("inaccessible", 30), ("unauthorized", 40))

class CucsEquipmentStorageMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("singleFlash", 1), ("dualFlash", 2))

class CucsEquipmentUnifiedPortAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("slideRule", 1), ("unrestricted", 2))

class CucsEquipmentXcvrId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsEquipmentXcvrType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("unknown", 0), ("h10gcu1m", 1), ("h10gcu3m", 2), ("h10gcu5m", 3), ("h10gcu7m", 4), ("h10gusr", 5), ("h10glrmsm", 6), ("cwdm1471", 7), ("cwdm1531", 8), ("cwdm1551", 9), ("fet", 10), ("sfp", 11), ("x2", 12), ("n10gbasesr", 13), ("n10gbaselr", 14), ("n10gbaselrm", 15), ("n10gbaseer", 16))

class CucsEquipmentFabricEpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("chassis", 1), ("fex", 2), ("blade", 3), ("rackUnit", 4))

class CucsEtherCIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsEtherCloudType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unclassified", 1), ("lan", 2), ("san", 3))

class CucsEtherErrStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("alignDelta", 0), ("alignDeltaAvg", 1), ("alignDeltaMax", 2), ("alignDeltaMin", 3), ("deferredTxDelta", 4), ("deferredTxDeltaAvg", 5), ("deferredTxDeltaMax", 6), ("deferredTxDeltaMin", 7), ("fcsDelta", 8), ("fcsDeltaAvg", 9), ("fcsDeltaMax", 10), ("fcsDeltaMin", 11), ("intMacRxDelta", 12), ("intMacRxDeltaAvg", 13), ("intMacRxDeltaMax", 14), ("intMacRxDeltaMin", 15), ("intMacTxDelta", 16), ("intMacTxDeltaAvg", 17), ("intMacTxDeltaMax", 18), ("intMacTxDeltaMin", 19), ("outDiscardDelta", 20), ("outDiscardDeltaAvg", 21), ("outDiscardDeltaMax", 22), ("outDiscardDeltaMin", 23), ("rcvDelta", 24), ("rcvDeltaAvg", 25), ("rcvDeltaMax", 26), ("rcvDeltaMin", 27), ("underSizeDelta", 28), ("underSizeDeltaAvg", 29), ("underSizeDeltaMax", 30), ("underSizeDeltaMin", 31), ("xmitDelta", 32), ("xmitDeltaAvg", 33), ("xmitDeltaMax", 34), ("xmitDeltaMin", 35))

class CucsEtherErrStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("alignDelta", 0), ("alignDeltaAvg", 1), ("alignDeltaMax", 2), ("alignDeltaMin", 3), ("deferredTxDelta", 4), ("deferredTxDeltaAvg", 5), ("deferredTxDeltaMax", 6), ("deferredTxDeltaMin", 7), ("fcsDelta", 8), ("fcsDeltaAvg", 9), ("fcsDeltaMax", 10), ("fcsDeltaMin", 11), ("intMacRxDelta", 12), ("intMacRxDeltaAvg", 13), ("intMacRxDeltaMax", 14), ("intMacRxDeltaMin", 15), ("intMacTxDelta", 16), ("intMacTxDeltaAvg", 17), ("intMacTxDeltaMax", 18), ("intMacTxDeltaMin", 19), ("outDiscardDelta", 20), ("outDiscardDeltaAvg", 21), ("outDiscardDeltaMax", 22), ("outDiscardDeltaMin", 23), ("rcvDelta", 24), ("rcvDeltaAvg", 25), ("rcvDeltaMax", 26), ("rcvDeltaMin", 27), ("underSizeDelta", 28), ("underSizeDeltaAvg", 29), ("underSizeDeltaMax", 30), ("underSizeDeltaMin", 31), ("xmitDelta", 32), ("xmitDeltaAvg", 33), ("xmitDeltaMax", 34), ("xmitDeltaMin", 35))

class CucsEtherExternalEpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsEtherExternalEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsEtherExternalPcAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsEtherExternalPcLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsEtherFcoeInterfaceStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bytesRxDelta", 0), ("bytesRxDeltaAvg", 1), ("bytesRxDeltaMax", 2), ("bytesRxDeltaMin", 3), ("bytesTxDelta", 4), ("bytesTxDeltaAvg", 5), ("bytesTxDeltaMax", 6), ("bytesTxDeltaMin", 7), ("droppedRxDelta", 8), ("droppedRxDeltaAvg", 9), ("droppedRxDeltaMax", 10), ("droppedRxDeltaMin", 11), ("droppedTxDelta", 12), ("droppedTxDeltaAvg", 13), ("droppedTxDeltaMax", 14), ("droppedTxDeltaMin", 15), ("errorsRxDelta", 16), ("errorsRxDeltaAvg", 17), ("errorsRxDeltaMax", 18), ("errorsRxDeltaMin", 19), ("errorsTxDelta", 20), ("errorsTxDeltaAvg", 21), ("errorsTxDeltaMax", 22), ("errorsTxDeltaMin", 23), ("packetsRxDelta", 24), ("packetsRxDeltaAvg", 25), ("packetsRxDeltaMax", 26), ("packetsRxDeltaMin", 27), ("packetsTxDelta", 28), ("packetsTxDeltaAvg", 29), ("packetsTxDeltaMax", 30), ("packetsTxDeltaMin", 31))

class CucsEtherFcoeInterfaceStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bytesRxDelta", 0), ("bytesRxDeltaAvg", 1), ("bytesRxDeltaMax", 2), ("bytesRxDeltaMin", 3), ("bytesTxDelta", 4), ("bytesTxDeltaAvg", 5), ("bytesTxDeltaMax", 6), ("bytesTxDeltaMin", 7), ("droppedRxDelta", 8), ("droppedRxDeltaAvg", 9), ("droppedRxDeltaMax", 10), ("droppedRxDeltaMin", 11), ("droppedTxDelta", 12), ("droppedTxDeltaAvg", 13), ("droppedTxDeltaMax", 14), ("droppedTxDeltaMin", 15), ("errorsRxDelta", 16), ("errorsRxDeltaAvg", 17), ("errorsRxDeltaMax", 18), ("errorsRxDeltaMin", 19), ("errorsTxDelta", 20), ("errorsTxDeltaAvg", 21), ("errorsTxDeltaMax", 22), ("errorsTxDeltaMin", 23), ("packetsRxDelta", 24), ("packetsRxDeltaAvg", 25), ("packetsRxDeltaMax", 26), ("packetsRxDeltaMin", 27), ("packetsTxDelta", 28), ("packetsTxDeltaAvg", 29), ("packetsTxDeltaMax", 30), ("packetsTxDeltaMin", 31))

class CucsEtherIntFIoEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsEtherInternalPcLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsEtherLossStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("sqetestDelta", 0), ("sqetestDeltaAvg", 1), ("sqetestDeltaMax", 2), ("sqetestDeltaMin", 3), ("carrierSenseDelta", 4), ("carrierSenseDeltaAvg", 5), ("carrierSenseDeltaMax", 6), ("carrierSenseDeltaMin", 7), ("excessCollisionDelta", 8), ("excessCollisionDeltaAvg", 9), ("excessCollisionDeltaMax", 10), ("excessCollisionDeltaMin", 11), ("giantsDelta", 12), ("giantsDeltaAvg", 13), ("giantsDeltaMax", 14), ("giantsDeltaMin", 15), ("lateCollisionDelta", 16), ("lateCollisionDeltaAvg", 17), ("lateCollisionDeltaMax", 18), ("lateCollisionDeltaMin", 19), ("multiCollisionDelta", 20), ("multiCollisionDeltaAvg", 21), ("multiCollisionDeltaMax", 22), ("multiCollisionDeltaMin", 23), ("singleCollisionDelta", 24), ("singleCollisionDeltaAvg", 25), ("singleCollisionDeltaMax", 26), ("singleCollisionDeltaMin", 27), ("symbolDelta", 28), ("symbolDeltaAvg", 29), ("symbolDeltaMax", 30), ("symbolDeltaMin", 31))

class CucsEtherLossStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("sqetestDelta", 0), ("sqetestDeltaAvg", 1), ("sqetestDeltaMax", 2), ("sqetestDeltaMin", 3), ("carrierSenseDelta", 4), ("carrierSenseDeltaAvg", 5), ("carrierSenseDeltaMax", 6), ("carrierSenseDeltaMin", 7), ("excessCollisionDelta", 8), ("excessCollisionDeltaAvg", 9), ("excessCollisionDeltaMax", 10), ("excessCollisionDeltaMin", 11), ("giantsDelta", 12), ("giantsDeltaAvg", 13), ("giantsDeltaMax", 14), ("giantsDeltaMin", 15), ("lateCollisionDelta", 16), ("lateCollisionDeltaAvg", 17), ("lateCollisionDeltaMax", 18), ("lateCollisionDeltaMin", 19), ("multiCollisionDelta", 20), ("multiCollisionDeltaAvg", 21), ("multiCollisionDeltaMax", 22), ("multiCollisionDeltaMin", 23), ("singleCollisionDelta", 24), ("singleCollisionDeltaAvg", 25), ("singleCollisionDeltaMax", 26), ("singleCollisionDeltaMin", 27), ("symbolDelta", 28), ("symbolDeltaAvg", 29), ("symbolDeltaMax", 30), ("symbolDeltaMin", 31))

class CucsEtherPIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsEtherPIoFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1014, 1334))
    namedValues = NamedValues(("nop", 0), ("inCompatSfpPresence", 1014), ("inCompatSfpReplaced", 1334))

class CucsEtherPIoFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1014, 1015, 1034, 1035, 1334, 1335, 1461, 1462))
    namedValues = NamedValues(("nop", 0), ("inCompatSfpPresenceBegin", 1014), ("inCompatSfpPresenceShutdown", 1015), ("inCompatSfpPresenceFail", 1034), ("inCompatSfpPresenceSuccess", 1035), ("inCompatSfpReplacedBegin", 1334), ("inCompatSfpReplacedEnablePort", 1335), ("inCompatSfpReplacedFail", 1461), ("inCompatSfpReplacedSuccess", 1462))

class CucsEtherPauseStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("recvPauseDelta", 0), ("recvPauseDeltaAvg", 1), ("recvPauseDeltaMax", 2), ("recvPauseDeltaMin", 3), ("resetsDelta", 4), ("resetsDeltaAvg", 5), ("resetsDeltaMax", 6), ("resetsDeltaMin", 7), ("xmitPauseDelta", 8), ("xmitPauseDeltaAvg", 9), ("xmitPauseDeltaMax", 10), ("xmitPauseDeltaMin", 11))

class CucsEtherPauseStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("recvPauseDelta", 0), ("recvPauseDeltaAvg", 1), ("recvPauseDeltaMax", 2), ("recvPauseDeltaMin", 3), ("resetsDelta", 4), ("resetsDeltaAvg", 5), ("resetsDeltaMax", 6), ("resetsDeltaMin", 7), ("xmitPauseDelta", 8), ("xmitPauseDeltaAvg", 9), ("xmitPauseDeltaMax", 10), ("xmitPauseDeltaMin", 11))

class CucsEtherRxStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("broadcastPacketsDelta", 0), ("broadcastPacketsDeltaAvg", 1), ("broadcastPacketsDeltaMax", 2), ("broadcastPacketsDeltaMin", 3), ("jumboPacketsDelta", 4), ("jumboPacketsDeltaAvg", 5), ("jumboPacketsDeltaMax", 6), ("jumboPacketsDeltaMin", 7), ("multicastPacketsDelta", 8), ("multicastPacketsDeltaAvg", 9), ("multicastPacketsDeltaMax", 10), ("multicastPacketsDeltaMin", 11), ("totalBytesDelta", 12), ("totalBytesDeltaAvg", 13), ("totalBytesDeltaMax", 14), ("totalBytesDeltaMin", 15), ("totalPacketsDelta", 16), ("totalPacketsDeltaAvg", 17), ("totalPacketsDeltaMax", 18), ("totalPacketsDeltaMin", 19), ("unicastPacketsDelta", 20), ("unicastPacketsDeltaAvg", 21), ("unicastPacketsDeltaMax", 22), ("unicastPacketsDeltaMin", 23))

class CucsEtherRxStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("broadcastPacketsDelta", 0), ("broadcastPacketsDeltaAvg", 1), ("broadcastPacketsDeltaMax", 2), ("broadcastPacketsDeltaMin", 3), ("jumboPacketsDelta", 4), ("jumboPacketsDeltaAvg", 5), ("jumboPacketsDeltaMax", 6), ("jumboPacketsDeltaMin", 7), ("multicastPacketsDelta", 8), ("multicastPacketsDeltaAvg", 9), ("multicastPacketsDeltaMax", 10), ("multicastPacketsDeltaMin", 11), ("totalBytesDelta", 12), ("totalBytesDeltaAvg", 13), ("totalBytesDeltaMax", 14), ("totalBytesDeltaMin", 15), ("totalPacketsDelta", 16), ("totalPacketsDeltaAvg", 17), ("totalPacketsDeltaMax", 18), ("totalPacketsDeltaMin", 19), ("unicastPacketsDelta", 20), ("unicastPacketsDeltaAvg", 21), ("unicastPacketsDeltaMax", 22), ("unicastPacketsDeltaMin", 23))

class CucsEtherSatelliteConnectionDisc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("absent", 0), ("present", 1), ("misConnect", 2), ("missing", 3), ("new", 4))

class CucsEtherServerIntFIoIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsEtherServerIntFIoLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsEtherServerIntFIoTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsEtherServerIntFIoType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsEtherServerIntFIoFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1150))
    namedValues = NamedValues(("nop", 0), ("configSpeed", 1150))

class CucsEtherServerIntFIoFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1150, 1151, 1182, 1183))
    namedValues = NamedValues(("nop", 0), ("configSpeedBegin", 1150), ("configSpeedConfigure", 1151), ("configSpeedFail", 1182), ("configSpeedSuccess", 1183))

class CucsEtherServerIntFIoFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1150))
    namedValues = NamedValues(("nop", 0), ("configSpeed", 1150))

class CucsEtherServerIntFIoPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsEtherServerIntFIoPcPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1024, 4096)

class CucsEtherServerIntFIoPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsEtherServerIntFIoPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsEtherServerIntFIoPcEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsEtherServerIntFIoPcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 33)

class CucsEtherSwitchIntFIoAck(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 6, 7, 8, 9))
    namedValues = NamedValues(("unInitialized", 0), ("unAcknowledged", 1), ("unsupportedConnectivity", 2), ("ok", 3), ("removing", 4), ("ackInProgress", 6), ("evaluation", 7), ("acknowledged", 8), ("autoAck", 9))

class CucsEtherSwitchIntFIoIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsEtherSwitchIntFIoLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsEtherSwitchIntFIoTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsEtherSwitchIntFIoType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsEtherSwitchIntFIoPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsEtherSwitchIntFIoPcPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1024, 4096)

class CucsEtherSwitchIntFIoPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsEtherSwitchIntFIoPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsEtherSwitchIntFIoPcEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsEtherSwitchIntFIoPcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsEtherTxStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("broadcastPacketsDelta", 0), ("broadcastPacketsDeltaAvg", 1), ("broadcastPacketsDeltaMax", 2), ("broadcastPacketsDeltaMin", 3), ("jumboPacketsDelta", 4), ("jumboPacketsDeltaAvg", 5), ("jumboPacketsDeltaMax", 6), ("jumboPacketsDeltaMin", 7), ("multicastPacketsDelta", 8), ("multicastPacketsDeltaAvg", 9), ("multicastPacketsDeltaMax", 10), ("multicastPacketsDeltaMin", 11), ("totalBytesDelta", 12), ("totalBytesDeltaAvg", 13), ("totalBytesDeltaMax", 14), ("totalBytesDeltaMin", 15), ("totalPacketsDelta", 16), ("totalPacketsDeltaAvg", 17), ("totalPacketsDeltaMax", 18), ("totalPacketsDeltaMin", 19), ("unicastPacketsDelta", 20), ("unicastPacketsDeltaAvg", 21), ("unicastPacketsDeltaMax", 22), ("unicastPacketsDeltaMin", 23))

class CucsEtherTxStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("broadcastPacketsDelta", 0), ("broadcastPacketsDeltaAvg", 1), ("broadcastPacketsDeltaMax", 2), ("broadcastPacketsDeltaMin", 3), ("jumboPacketsDelta", 4), ("jumboPacketsDeltaAvg", 5), ("jumboPacketsDeltaMax", 6), ("jumboPacketsDeltaMin", 7), ("multicastPacketsDelta", 8), ("multicastPacketsDeltaAvg", 9), ("multicastPacketsDeltaMax", 10), ("multicastPacketsDeltaMin", 11), ("totalBytesDelta", 12), ("totalBytesDeltaAvg", 13), ("totalBytesDeltaMax", 14), ("totalBytesDeltaMin", 15), ("totalPacketsDelta", 16), ("totalPacketsDeltaAvg", 17), ("totalPacketsDeltaMax", 18), ("totalPacketsDeltaMin", 19), ("unicastPacketsDelta", 20), ("unicastPacketsDeltaAvg", 21), ("unicastPacketsDeltaMax", 22), ("unicastPacketsDeltaMin", 23))

class CucsEventEpCtrlLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 0), ("info", 1), ("condition", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6))

class CucsExtmgmtArpTargetsMaxDeadlineTimeout(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(5, 15)

class CucsExtmgmtArpTargetsNumberOfArpRequests(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 5)

class CucsExtmgmtGatewayPingMaxDeadlineTimeout(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(5, 15)

class CucsExtmgmtGatewayPingNumberOfPingRequests(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 5)

class CucsExtmgmtIfMonPolicyAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsExtmgmtIfMonPolicyMonitorMechanism(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("miiStatus", 0), ("arpTargetPing", 1), ("gatewayPing", 2))

class CucsExtmgmtMiiStatusMaxRetryCount(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 3)

class CucsExtmgmtMiiStatusRetryInterval(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(3, 10)

class CucsExtpolAppCapability(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("serviceReg", 0), ("identifierMgr", 1), ("operationMgr", 2), ("resourceMgr", 3), ("virtualSwitchingMgr", 4), ("policyMgr", 5), ("bootMgr", 6), ("vmMgr", 7), ("vmAdmin", 8), ("infraCryptoOffloa", 9), ("vmm", 10), ("vmVasw", 11), ("vmFw", 12), ("vmSlb", 13), ("infraFw", 14), ("infraSlb", 15), ("ipam", 16), ("pcm", 17), ("infraAggr", 18), ("infraWas", 19), ("infraWaf", 20), ("infraPasw", 21), ("infraPdsw", 22), ("storageBroker", 23), ("orgMgr", 24), ("statsMgr", 25))

class CucsExtpolConnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(5, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39))
    namedValues = NamedValues(("ape", 5), ("serviceReg", 27), ("identifierMgr", 28), ("operationMgr", 29), ("resourceMgr", 30), ("virtualSwitchingMgr", 31), ("policyMgr", 32), ("bootMgr", 33), ("vmMgr", 34), ("managedEndpoint", 35), ("mgmtController", 36), ("storageBroker", 37), ("resourceAggr", 38), ("statsMgr", 39))

class CucsExtpolConnectorOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unregistered", 0), ("lostVisibility", 1), ("registering", 2), ("synchronizing", 3), ("registered", 4), ("versionMismatch", 5), ("registryNotReachable", 6))

class CucsExtpolEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1193, 1349))
    namedValues = NamedValues(("nop", 0), ("repairCert", 1193), ("registerFsm", 1349))

class CucsExtpolEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1193, 1194, 1195, 1196, 1197, 1198, 1349, 1350, 1393, 1394, 1395, 1396))
    namedValues = NamedValues(("nop", 0), ("repairCertBegin", 1193), ("repairCertVerifyGuid", 1194), ("repairCertUnregister", 1195), ("repairCertCleanOldData", 1196), ("repairCertRequest", 1197), ("repairCertVerify", 1198), ("registerFsmBegin", 1349), ("registerFsmExecute", 1350), ("registerFsmFail", 1393), ("registerFsmSuccess", 1394), ("repairCertFail", 1395), ("repairCertSuccess", 1396))

class CucsExtpolEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1193, 1349))
    namedValues = NamedValues(("nop", 0), ("repairCert", 1193), ("registerFsm", 1349))

class CucsExtpolProviderFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1374))
    namedValues = NamedValues(("nop", 0), ("reportConfigImport", 1374))

class CucsExtpolProviderFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1374, 1375, 1398, 1399))
    namedValues = NamedValues(("nop", 0), ("reportConfigImportBegin", 1374), ("reportConfigImportReport", 1375), ("reportConfigImportFail", 1398), ("reportConfigImportSuccess", 1399))

class CucsExtpolProviderFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1374))
    namedValues = NamedValues(("nop", 0), ("reportConfigImport", 1374))

class CucsExtpolRegistryFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1351, 1354))
    namedValues = NamedValues(("nop", 0), ("crossDomainConfig", 1351), ("crossDomainDelete", 1354))

class CucsExtpolRegistryFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1351, 1352, 1353, 1354, 1355, 1356, 1397, 1398, 1399, 1400))
    namedValues = NamedValues(("nop", 0), ("crossDomainConfigBegin", 1351), ("crossDomainConfigSetLocal", 1352), ("crossDomainConfigSetPeer", 1353), ("crossDomainDeleteBegin", 1354), ("crossDomainDeleteSetLocal", 1355), ("crossDomainDeleteSetPeer", 1356), ("crossDomainConfigFail", 1397), ("crossDomainConfigSuccess", 1398), ("crossDomainDeleteFail", 1399), ("crossDomainDeleteSuccess", 1400))

class CucsExtpolRegistryFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1351, 1354))
    namedValues = NamedValues(("nop", 0), ("crossDomainConfig", 1351), ("crossDomainDelete", 1354))

class CucsExtpolState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("licenseOk", 1), ("licenseInsufficient", 2), ("licenseGraceperiod", 3), ("licenseExpired", 4), ("notApplicable", 5))

class CucsExtpolSuspendState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class CucsExtvmmEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1129))
    namedValues = NamedValues(("nop", 0), ("clusterRole", 1129))

class CucsExtvmmEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1129, 1130, 1131, 1142, 1143))
    namedValues = NamedValues(("nop", 0), ("clusterRoleBegin", 1129), ("clusterRoleSetPeer", 1130), ("clusterRoleSetLocal", 1131), ("clusterRoleFail", 1142), ("clusterRoleSuccess", 1143))

class CucsExtvmmEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1086))
    namedValues = NamedValues(("nop", 0), ("clusterRole", 1086))

class CucsExtvmmKeyStoreFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 539))
    namedValues = NamedValues(("nop", 0), ("certInstall", 539))

class CucsExtvmmKeyStoreFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 539, 540, 541, 561, 562))
    namedValues = NamedValues(("nop", 0), ("certInstallBegin", 539), ("certInstallSetLocal", 540), ("certInstallSetPeer", 541), ("certInstallFail", 561), ("certInstallSuccess", 562))

class CucsExtvmmKeyStoreFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 539))
    namedValues = NamedValues(("nop", 0), ("certInstall", 539))

class CucsExtvmmMasterExtKeyFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 575))
    namedValues = NamedValues(("nop", 0), ("config", 575))

class CucsExtvmmMasterExtKeyFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 575, 576, 577, 578, 579))
    namedValues = NamedValues(("nop", 0), ("configBegin", 575), ("configSetLocal", 576), ("configSetPeer", 577), ("configFail", 578), ("configSuccess", 579))

class CucsExtvmmMasterExtKeyFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 575))
    namedValues = NamedValues(("nop", 0), ("config", 575))

class CucsExtvmmOwnership(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("discovered", 1), ("managed", 2))

class CucsExtvmmProviderFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 536))
    namedValues = NamedValues(("nop", 0), ("config", 536))

class CucsExtvmmProviderFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 536, 537, 538, 563, 564, 581))
    namedValues = NamedValues(("nop", 0), ("configBegin", 536), ("configSetPeer", 537), ("configSetLocal", 538), ("configFail", 563), ("configSuccess", 564), ("configGetVersion", 581))

class CucsExtvmmProviderFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 536, 1130))
    namedValues = NamedValues(("nop", 0), ("config", 536), ("collectGarbage", 1130))

class CucsExtvmmSwitchDelTaskFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 542))
    namedValues = NamedValues(("nop", 0), ("removeProvider", 542))

class CucsExtvmmSwitchDelTaskFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 542, 543, 565, 566))
    namedValues = NamedValues(("nop", 0), ("removeProviderBegin", 542), ("removeProviderRemoveLocal", 543), ("removeProviderFail", 565), ("removeProviderSuccess", 566))

class CucsExtvmmSwitchDelTaskFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 542))
    namedValues = NamedValues(("nop", 0), ("removeProvider", 542))

class CucsExtvmmVcVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("kl", 1), ("klU1", 2))

class CucsFabricADceSwSrvEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAEthEstcEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricAEthEstcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAEthEstcEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricAEthLanEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAFcEstcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAFcEstcEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricAFcSanEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAFcoeEstcEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricAFcoeEstcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAFcoeEstcEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricAFcoeSanEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAVlanSharing(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("primary", 1), ("isolated", 2))

class CucsFabricAVlanTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAVlanType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricAVsanTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricAVsanType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricAccessType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("lan", 0), ("san", 1))

class CucsFabricAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsFabricBHVlanSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("dual", 3))

class CucsFabricBladeLifeCycle(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2), ("migrate", 3))

class CucsFabricCIoEpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsFabricCIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsFabricCloudType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ethlan", 0), ("ethestclan", 1), ("ethlanmon", 2), ("fcsan", 3), ("fcsanmon", 4), ("fcestc", 5))

class CucsFabricComputeEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricComputeEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricComputePhEpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("remove", 3))

class CucsFabricComputeSlotEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsFabricComputeSlotEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 20))
    namedValues = NamedValues(("nop", 0), ("identify", 20))

class CucsFabricComputeSlotEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 20, 21, 22, 390, 391))
    namedValues = NamedValues(("nop", 0), ("identifyBegin", 20), ("identifyExecuteLocal", 21), ("identifyExecutePeer", 22), ("identifyFail", 390), ("identifySuccess", 391))

class CucsFabricComputeSlotEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 20))
    namedValues = NamedValues(("nop", 0), ("identify", 20))

class CucsFabricConfMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("logicalConfigInvalid", 1), ("validatingConf", 2), ("applyPhysTrans", 3), ("confSwitch", 4))

class CucsFabricConfState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("logicalConfigInvalid", 1))

class CucsFabricConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("applied", 1), ("inconsistent", 2))

class CucsFabricDceSwSrvEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricDceSwSrvEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 1)

class CucsFabricDceSwSrvPcPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1024, 4096)

class CucsFabricDceSwSrvPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricDceSwSrvPcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 48)

class CucsFabricDceSwSrvPcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 3)

class CucsFabricDefaultZoningState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsFabricEpMgrFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1113))
    namedValues = NamedValues(("nop", 0), ("configure", 1113))

class CucsFabricEpMgrFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1113, 1114, 1115, 1116, 1117, 1144, 1145))
    namedValues = NamedValues(("nop", 0), ("configureBegin", 1113), ("configureValidateConfiguration", 1114), ("configureApplyPhysical", 1115), ("configureWaitOnPhys", 1116), ("configureApplyConfig", 1117), ("configureFail", 1144), ("configureSuccess", 1145))

class CucsFabricEpMgrFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeFabricEpMgrConfigurePhysChange", 51), ("samDmeFabricEpMgrConfigureModification", 52), ("samDmeFabricEpMgrConfigureEthServerConfig", 53), ("samDmeFabricEpMgrConfigureEthUplinkConfig", 54), ("samDmeFabricEpMgrConfigureFcUplinkConfig", 55), ("samDmeFabricEpMgrConfigureEthStorageConfig", 56), ("samDmeFabricEpMgrConfigureFcStorageConfig", 57))

class CucsFabricEpMgrFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1078))
    namedValues = NamedValues(("nop", 0), ("configure", 1078))

class CucsFabricEpVlanVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("regular", 0), ("default", 1), ("native", 2), ("fcoeuplinknative", 3))

class CucsFabricEstcEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricEstcPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricEstcPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthEstcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthEstcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthEstcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricEthEstcEpPrio(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("fc", 1), ("platinum", 2), ("gold", 3), ("silver", 4), ("bronze", 5), ("bestEffort", 6))

class CucsFabricEthEstcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 3)

class CucsFabricEthEstcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthEstcEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthEstcPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthEstcPcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricEthEstcPcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 3)

class CucsFabricEthEstcPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trunk", 1), ("access", 2))

class CucsFabricEthLanTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthLanEpVlanStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("missingPrimary", 1))

class CucsFabricEthLanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthLanPcVlanStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("missingPrimary", 1))

class CucsFabricEthMonTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthMonType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthMonDestEpAdminSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("indeterminate", 0), ("n1gbps", 1), ("n10gbps", 2), ("n20gbps", 3), ("n40gbps", 4))

class CucsFabricEthMonDestEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricEthMonDestEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricEthMonDestEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 3)

class CucsFabricEthMonDestEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthMonFiltEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthMonFiltRefType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthMonLanTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthMonLanType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthMonSrcEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthMonSrcRefType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricEthPcProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("static", 1), ("lacp", 2))

class CucsFabricEthSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20))
    namedValues = NamedValues(("vnic", 1), ("uplinkPort", 2), ("vlan", 3), ("serverPort", 4), ("portChannel", 5), ("hostPort", 6), ("storage", 7), ("nasPort", 8), ("fcoeuplinkPort", 9), ("fcoeuplinkPortchannel", 10), ("vmNic", 11), ("vhba", 20))

class CucsFabricEthTargetEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthVlanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricEthVlanPortEpVlanStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("missingPrimary", 1))

class CucsFabricExternalLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricExternalEpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsFabricExternalEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricExternalPcLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricFcEstcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcEstcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcEstcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricFcEstcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(2, 5)

class CucsFabricFcMonTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcMonType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcMonDestEpAdminSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("indeterminate", 0), ("n1gbps", 1), ("n2gbps", 2), ("n4gbps", 3), ("n8gbps", 4), ("auto", 5))

class CucsFabricFcMonDestEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricFcMonDestEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricFcMonDestEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(2, 5)

class CucsFabricFcMonDestEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcMonFiltEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcMonFiltRefType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcMonSanTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcMonSanType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcMonSrcEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcMonSrcRefType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricFcSanTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcSanUplinkTrunking(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsFabricFcSanEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricFcSanEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(2, 5)

class CucsFabricFcSanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcSanPcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricFcSanPcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(2, 5)

class CucsFabricFcSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("vhba", 1), ("uplinkPort", 2), ("vsan", 3), ("storage", 4), ("portChannel", 5))

class CucsFabricFcVsanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcVsanPortEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 256)

class CucsFabricFcVsanPortEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 5)

class CucsFabricFcZoneSharingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("coalesce", 0), ("clearUnmanagedZoneActive", 1), ("clearUnmanagedZoneAll", 2))

class CucsFabricFcoeEstcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricFcoeEstcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 3)

class CucsFabricFcoeSanEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 48)

class CucsFabricFcoeSanEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 5)

class CucsFabricFcoeSanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcoeSanPcEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 48)

class CucsFabricFcoeSanPcEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 5)

class CucsFabricFcoeVsanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricFcoeVsanPortEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 256)

class CucsFabricFcoeVsanPortEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 5)

class CucsFabricFillPattern(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("idle", 0), ("arbff", 1))

class CucsFabricInternalLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricInternalDceSrvTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsFabricInternalDceSrvType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricInternalEpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsFabricInternalEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricInternalPcLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricLanType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricLanCloudVlanCompression(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsFabricLanCloudFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 184))
    namedValues = NamedValues(("nop", 0), ("switchMode", 184))

class CucsFabricLanCloudFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 184, 185, 186, 392, 393))
    namedValues = NamedValues(("nop", 0), ("switchModeBegin", 184), ("switchModeSwConfigPeer", 185), ("switchModeSwConfigLocal", 186), ("switchModeFail", 392), ("switchModeSuccess", 393))

class CucsFabricLanCloudFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 184))
    namedValues = NamedValues(("nop", 0), ("switchMode", 184))

class CucsFabricLanEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricLanEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricLanPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricLanPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricLifeCycle(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2))

class CucsFabricMemberStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("up", 0), ("down", 1))

class CucsFabricMembershipStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("down", 1), ("up", 2), ("hotStandby", 3), ("suspended", 4), ("individual", 5), ("moduleRemoved", 6), ("incompatibleSpeed", 7), ("unknown", 8))

class CucsFabricMonAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsFabricMonOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("error", 3))

class CucsFabricMonOperStateReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("active", 0), ("noHardwareResource", 1), ("noOperationalSrcDst", 2), ("genericError", 3), ("noSourcesConfigured", 4), ("noDestinationConfigured", 5), ("noSourceDestinationConfigured", 6), ("sessionAdminShut", 7), ("wrongDestinationMode", 8), ("wrongSourceMode", 9), ("tunnelMisconfDown", 10), ("noFlowIdSpecified", 11), ("unknown", 12))

class CucsFabricNetGroupSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("dual", 3))

class CucsFabricNetGroupType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("mgmt", 0), ("vlanCompression", 1), ("vlanUncompressed", 2))

class CucsFabricOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("errorMisconfigured", 3))

class CucsFabricOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("policy", 1), ("management", 2))

class CucsFabricPIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsFabricPIoEpOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("errorMisconfigured", 3))

class CucsFabricPIoEpPortId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 40)

class CucsFabricPIoEpSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 3)

class CucsFabricPathEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsFabricPathEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricPcConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("applied", 1), ("incompatibleSpeed", 2))

class CucsFabricQuerierType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("enabled", 0), ("disabled", 1))

class CucsFabricReqIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("permitUnresolved", 0))

class CucsFabricSanType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricSanCloudFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 871))
    namedValues = NamedValues(("nop", 0), ("switchMode", 871))

class CucsFabricSanCloudFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 871, 872, 873, 992, 993))
    namedValues = NamedValues(("nop", 0), ("switchModeBegin", 871), ("switchModeSwConfigPeer", 872), ("switchModeSwConfigLocal", 873), ("switchModeFail", 992), ("switchModeSuccess", 993))

class CucsFabricSanCloudFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 875))
    namedValues = NamedValues(("nop", 0), ("switchMode", 875))

class CucsFabricSanEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricSanEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricSanPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricSanPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricSlotAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 3))
    namedValues = NamedValues(("acknowledged", 1), ("reacknowledge", 3))

class CucsFabricSnoopingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("enabled", 0), ("disabled", 1))

class CucsFabricStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("modified", 0), ("created", 1), ("deleted", 2), ("intentDeletion", 3))

class CucsFabricSwChEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricSwChEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricSwChPhEpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("remove", 3))

class CucsFabricSwSrvEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricSwSrvEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricSwSrvPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricSwSrvPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricSwitchingMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("endHost", 0), ("switch", 1))

class CucsFabricTargetEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsFabricTargetStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("valid", 0), ("invalid", 1))

class CucsFabricTrafficDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("both", 3))

class CucsFabricVConInstType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auto", 1), ("manual", 2), ("policy", 3))

class CucsFabricVConMappingScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3))
    namedValues = NamedValues(("roundRobin", 2), ("linearOrdered", 3))

class CucsFabricVConPlacementPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("physical", 1), ("auto", 2))

class CucsFabricVConSelectPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 7))
    namedValues = NamedValues(("assignedOnly", 1), ("unassignedOnly", 2), ("excludeDynamic", 3), ("dynamicOnly", 4), ("excludeUnassigned", 5), ("all", 7))

class CucsFabricVConSharePref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("exclusiveOnly", 1), ("exclusivePreferred", 2), ("sameTransport", 3), ("differentTransport", 4), ("shared", 5))

class CucsFabricVConTransportPref(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("fc", 0), ("ethernet", 1))

class CucsFabricVlanSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("dual", 3))

class CucsFabricVlanCompType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("included", 1), ("excluded", 2))

class CucsFabricVlanConfigIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("conflictingVlanAccess", 0), ("unsupportedMulticastPolicy", 1))

class CucsFabricVlanOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("errorMisconfigured", 2))

class CucsFabricVnetEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsFabricVnetEpLcCtrlState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3))

class CucsFabricVnetEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsFabricVnetEpPolicyOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("local", 0), ("policy", 1), ("pendingPolicy", 2))

class CucsFabricVnetEpSyncEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1474))
    namedValues = NamedValues(("nop", 0), ("pushVnetEpDeletion", 1474))

class CucsFabricVnetEpSyncEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1474, 1475, 1482, 1483))
    namedValues = NamedValues(("nop", 0), ("pushVnetEpDeletionBegin", 1474), ("pushVnetEpDeletionSync", 1475), ("pushVnetEpDeletionFail", 1482), ("pushVnetEpDeletionSuccess", 1483))

class CucsFabricVnetEpSyncEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1474))
    namedValues = NamedValues(("nop", 0), ("pushVnetEpDeletion", 1474))

class CucsFabricVsanSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("dual", 3))

class CucsFabricVsanOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("errorMisconfigured", 2), ("errorReserved", 3))

class CucsFabricWarnings(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("fcZoningEnabled", 0), ("configurationError", 1))

class CucsFabricZoningState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsFaultBasePolicyClearAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("retain", 0), ("delete", 1))

class CucsFaultBasePolicySoakingSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("info", 1), ("condition", 2), ("warning", 3))

class CucsFaultPolicyClearAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("retain", 0), ("delete", 1))

class CucsFcErrStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("crcRxDelta", 0), ("crcRxDeltaAvg", 1), ("crcRxDeltaMax", 2), ("crcRxDeltaMin", 3), ("discardRxDelta", 4), ("discardRxDeltaAvg", 5), ("discardRxDeltaMax", 6), ("discardRxDeltaMin", 7), ("discardTxDelta", 8), ("discardTxDeltaAvg", 9), ("discardTxDeltaMax", 10), ("discardTxDeltaMin", 11), ("linkFailuresDelta", 12), ("linkFailuresDeltaAvg", 13), ("linkFailuresDeltaMax", 14), ("linkFailuresDeltaMin", 15), ("rxDelta", 16), ("rxDeltaAvg", 17), ("rxDeltaMax", 18), ("rxDeltaMin", 19), ("signalLossesDelta", 20), ("signalLossesDeltaAvg", 21), ("signalLossesDeltaMax", 22), ("signalLossesDeltaMin", 23), ("syncLossesDelta", 24), ("syncLossesDeltaAvg", 25), ("syncLossesDeltaMax", 26), ("syncLossesDeltaMin", 27), ("tooLongRxDelta", 28), ("tooLongRxDeltaAvg", 29), ("tooLongRxDeltaMax", 30), ("tooLongRxDeltaMin", 31), ("tooShortRxDelta", 32), ("tooShortRxDeltaAvg", 33), ("tooShortRxDeltaMax", 34), ("tooShortRxDeltaMin", 35), ("txDelta", 36), ("txDeltaAvg", 37), ("txDeltaMax", 38), ("txDeltaMin", 39))

class CucsFcErrStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("crcRxDelta", 0), ("crcRxDeltaAvg", 1), ("crcRxDeltaMax", 2), ("crcRxDeltaMin", 3), ("discardRxDelta", 4), ("discardRxDeltaAvg", 5), ("discardRxDeltaMax", 6), ("discardRxDeltaMin", 7), ("discardTxDelta", 8), ("discardTxDeltaAvg", 9), ("discardTxDeltaMax", 10), ("discardTxDeltaMin", 11), ("linkFailuresDelta", 12), ("linkFailuresDeltaAvg", 13), ("linkFailuresDeltaMax", 14), ("linkFailuresDeltaMin", 15), ("rxDelta", 16), ("rxDeltaAvg", 17), ("rxDeltaMax", 18), ("rxDeltaMin", 19), ("signalLossesDelta", 20), ("signalLossesDeltaAvg", 21), ("signalLossesDeltaMax", 22), ("signalLossesDeltaMin", 23), ("syncLossesDelta", 24), ("syncLossesDeltaAvg", 25), ("syncLossesDeltaMax", 26), ("syncLossesDeltaMin", 27), ("tooLongRxDelta", 28), ("tooLongRxDeltaAvg", 29), ("tooLongRxDeltaMax", 30), ("tooLongRxDeltaMin", 31), ("tooShortRxDelta", 32), ("tooShortRxDeltaAvg", 33), ("tooShortRxDeltaMax", 34), ("tooShortRxDeltaMin", 35), ("txDelta", 36), ("txDeltaAvg", 37), ("txDeltaMax", 38), ("txDeltaMin", 39))

class CucsFcPIoFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1014, 1334))
    namedValues = NamedValues(("nop", 0), ("inCompatSfpPresence", 1014), ("inCompatSfpReplaced", 1334))

class CucsFcPIoFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1014, 1015, 1034, 1035, 1334, 1335, 1461, 1462))
    namedValues = NamedValues(("nop", 0), ("inCompatSfpPresenceBegin", 1014), ("inCompatSfpPresenceShutdown", 1015), ("inCompatSfpPresenceFail", 1034), ("inCompatSfpPresenceSuccess", 1035), ("inCompatSfpReplacedBegin", 1334), ("inCompatSfpReplacedEnablePort", 1335), ("inCompatSfpReplacedFail", 1461), ("inCompatSfpReplacedSuccess", 1462))

class CucsFcStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bytesRxDelta", 0), ("bytesRxDeltaAvg", 1), ("bytesRxDeltaMax", 2), ("bytesRxDeltaMin", 3), ("bytesTxDelta", 4), ("bytesTxDeltaAvg", 5), ("bytesTxDeltaMax", 6), ("bytesTxDeltaMin", 7), ("packetsRxDelta", 8), ("packetsRxDeltaAvg", 9), ("packetsRxDeltaMax", 10), ("packetsRxDeltaMin", 11), ("packetsTxDelta", 12), ("packetsTxDeltaAvg", 13), ("packetsTxDeltaMax", 14), ("packetsTxDeltaMin", 15))

class CucsFcStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bytesRxDelta", 0), ("bytesRxDeltaAvg", 1), ("bytesRxDeltaMax", 2), ("bytesRxDeltaMin", 3), ("bytesTxDelta", 4), ("bytesTxDeltaAvg", 5), ("bytesTxDeltaMax", 6), ("bytesTxDeltaMin", 7), ("packetsRxDelta", 8), ("packetsRxDeltaAvg", 9), ("packetsRxDeltaMax", 10), ("packetsRxDeltaMin", 11), ("packetsTxDelta", 12), ("packetsTxDeltaAvg", 13), ("packetsTxDeltaMax", 14), ("packetsTxDeltaMin", 15))

class CucsFcpoolBootTargetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("primary", 0), ("secondary", 1))

class CucsFcpoolInitiatorPurpose(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("portWwn", 0), ("nodeWwn", 1), ("derived", 2))

class CucsFcpoolInitiatorEpPurpose(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("portWwn", 0), ("nodeWwn", 1))

class CucsFcpoolInitiatorsAssignmentOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("default", 0), ("sequential", 1))

class CucsFcpoolInitiatorsMaxPortsPerNode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 7, 15, 31, 63))
    namedValues = NamedValues(("upto3", 3), ("upto7", 7), ("upto15", 15), ("upto31", 31), ("upto63", 63))

class CucsFcpoolInitiatorsPurpose(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nodeAndPortWwnAssignment", 0), ("portWwnAssignment", 1), ("nodeWwnAssignment", 2))

class CucsFirmwareAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("active", 0), ("deleted", 1))

class CucsFirmwareBootUnitImage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("running", 0), ("backup", 1))

class CucsFirmwareCatalogPackConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ok", 0), ("notApplied", 1), ("failed", 2))

class CucsFirmwareCompleteness(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("partial", 0), ("complete", 1))

class CucsFirmwareComponentType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("kernel", 0), ("system", 1), ("combined", 2), ("bootLoader", 3))

class CucsFirmwareDependencyRelationship(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("special", 0), ("ancestor", 1), ("descendent", 2))

class CucsFirmwareDependencyScope(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("blade", 1), ("chassis", 2), ("system", 4), ("switch", 8), ("global", 16))

class CucsFirmwareDependencySensitivity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("global", 0), ("fabric", 1), ("path", 2))

class CucsFirmwareDistributableFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 594))
    namedValues = NamedValues(("nop", 0), ("delete", 594))

class CucsFirmwareDistributableFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 594, 595, 596, 597, 598))
    namedValues = NamedValues(("nop", 0), ("deleteBegin", 594), ("deleteLocal", 595), ("deleteRemote", 596), ("deleteFail", 597), ("deleteSuccess", 598))

class CucsFirmwareDistributableFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 594))
    namedValues = NamedValues(("nop", 0), ("delete", 594))

class CucsFirmwareDistributableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("image", 1), ("fullBundle", 2), ("infrastructureBundle", 3), ("bSeriesBundle", 4), ("cSeriesBundle", 5), ("catalog", 6))

class CucsFirmwareDownloadActivity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("restart", 0), ("idle", 1))

class CucsFirmwareDownloaderFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 233))
    namedValues = NamedValues(("nop", 0), ("download", 233))

class CucsFirmwareDownloaderFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 233, 234, 235, 236, 239, 394, 395))
    namedValues = NamedValues(("nop", 0), ("downloadBegin", 233), ("downloadLocal", 234), ("downloadUnpackLocal", 235), ("downloadCopyRemote", 236), ("downloadDeleteLocal", 239), ("downloadFail", 394), ("downloadSuccess", 395))

class CucsFirmwareDownloaderFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 233))
    namedValues = NamedValues(("nop", 0), ("download", 233))

class CucsFirmwareEquipmentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 0), ("system", 1), ("switch", 2), ("iocard", 3), ("server", 4), ("cimc", 5), ("adaptor", 6), ("storageController", 7), ("boardController", 8), ("bios", 9), ("serviceProfile", 10))

class CucsFirmwareFwState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("sameRelease", 1), ("compatible", 2), ("incompatible", 3), ("multipleReleases", 4))

class CucsFirmwareHostPackConfigQualifier(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("biosImageNotSelected", 0))

class CucsFirmwareImageDeleted(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("a", 0), ("b", 1))

class CucsFirmwareImageError(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("checksumFailure", 1), ("filesystemError", 2), ("mgmtConnectError", 3), ("bootConfMissing", 4), ("crcFailure", 5), ("unknownError", 6))

class CucsFirmwareImageFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 240))
    namedValues = NamedValues(("nop", 0), ("delete", 240))

class CucsFirmwareImageFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 240, 241, 242, 396, 397))
    namedValues = NamedValues(("nop", 0), ("deleteBegin", 240), ("deleteLocal", 241), ("deleteRemote", 242), ("deleteFail", 396), ("deleteSuccess", 397))

class CucsFirmwareImageFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 240))
    namedValues = NamedValues(("nop", 0), ("delete", 240))

class CucsFirmwareImagePresence(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("a", 0), ("b", 1))

class CucsFirmwareImageState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("ready", 0), ("scheduled", 1), ("updating", 2), ("activating", 3), ("failed", 4), ("setStartup", 5), ("rebooting", 6), ("pendingNextBoot", 7), ("throttled", 8), ("upgrading", 9), ("autoUpdating", 10), ("badImage", 11))

class CucsFirmwareImpactType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("activate", 0), ("noimpact", 1), ("reset", 2), ("update", 3))

class CucsFirmwareInstallState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("ready", 0), ("scheduled", 1), ("inProgress", 2), ("failed", 3), ("pendingUserAck", 4), ("startPendingExtPermission", 5))

class CucsFirmwareItemType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("unspecified", 0), ("switchKernel", 1), ("switchSoftware", 2), ("system", 3), ("bladeController", 4), ("iocard", 5), ("bladeBios", 6), ("adaptor", 7), ("storageController", 8), ("hostNic", 9), ("hostHba", 10), ("hostHbaOptionrom", 11), ("hostNicOptionrom", 12), ("boardController", 13), ("localDisk", 14))

class CucsFirmwarePackMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("staged", 0), ("oneShot", 1))

class CucsFirmwarePackItemPresence(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("missing", 1), ("present", 2))

class CucsFirmwareRunningDeployment(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unspecified", 0), ("kernel", 1), ("bootLoader", 2), ("system", 3))

class CucsFirmwareSystemFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1362, 1378))
    namedValues = NamedValues(("nop", 0), ("deploy", 1362), ("applyCatalogPack", 1378))

class CucsFirmwareSystemFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1401, 1402, 1403, 1404))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 1362), ("deployWaitForDeploy", 1363), ("deployResolveDistributableNames", 1364), ("deployResolveDistributable", 1365), ("deployResolveImages", 1366), ("deployActivateUCSM", 1367), ("deployPollActivateOfUCSM", 1368), ("deployUpdateIOM", 1369), ("deployPollUpdateOfIOM", 1370), ("deployActivateIOM", 1371), ("deployPollActivateOfIOM", 1372), ("deployActivateRemoteFI", 1373), ("deployPollActivateOfRemoteFI", 1374), ("deployWaitForUserAck", 1375), ("deployActivateLocalFI", 1376), ("deployPollActivateOfLocalFI", 1377), ("applyCatalogPackBegin", 1378), ("applyCatalogPackResolveDistributableNames", 1379), ("applyCatalogPackResolveDistributable", 1380), ("applyCatalogPackResolveImages", 1381), ("applyCatalogPackActivateCatalog", 1382), ("applyCatalogPackFail", 1401), ("applyCatalogPackSuccess", 1402), ("deployFail", 1403), ("deploySuccess", 1404))

class CucsFirmwareSystemFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeFirmwareSystemDeployApplyInfra", 8))

class CucsFirmwareSystemFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1362, 1378))
    namedValues = NamedValues(("nop", 0), ("deploy", 1362), ("applyCatalogPack", 1378))

class CucsFirmwareTransferState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("init", 0), ("downloading", 1), ("downloaded", 2), ("failed", 3))

class CucsFirmwareTransport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ftp", 0), ("tftp", 1), ("scp", 2), ("sftp", 3), ("local", 4))

class CucsFirmwareTriggerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("triggered", 0), ("trigger", 1))

class CucsFirmwareType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("unspecified", 0), ("switchKernel", 1), ("switchSoftware", 2), ("system", 3), ("bladeController", 4), ("iocard", 5), ("fex", 6), ("adaptor", 7), ("storageController", 8), ("hostNic", 9), ("hostHba", 10), ("hostHbaOptionrom", 11), ("hostNicOptionrom", 12), ("boardController", 13), ("localDisk", 14), ("diag", 15), ("catalog", 16), ("mgmtExt", 17), ("debugPlugIn", 18), ("switch", 19))

class CucsFirmwareUpdatableDeployment(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4))
    namedValues = NamedValues(("unspecified", 0), ("backup", 4))

class CucsFirmwareUpgradeCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 0), ("dataLoad", 1), ("catalog", 2), ("config", 3), ("serverReboot", 4), ("faults", 5))

class CucsFirmwareUpgradeSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("fatal", 1), ("error", 2), ("warn", 3), ("info", 4))

class CucsFirmwareUpgradeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("inProgress", 1), ("failed", 2), ("success", 3), ("warnings", 4), ("skipped", 5))

class CucsFlowctrlFlowControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class CucsFlowctrlPriorityPause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("auto", 0), ("on", 1))

class CucsFsmCompletion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("scheduled", 0), ("processing", 1), ("completed", 2), ("cancelled", 3))

class CucsFsmFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("unused", 1))

class CucsFsmFsmStageStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 255))
    namedValues = NamedValues(("fail", 0), ("success", 1), ("skip", 2), ("pending", 3), ("inProgress", 4), ("throttled", 5), ("nop", 255))

class CucsFsmLifecycle(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3))

class CucsGmetaCategory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unknown", 0), ("inventory", 1))

class CucsGmetaHolderFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1476))
    namedValues = NamedValues(("nop", 0), ("inventory", 1476))

class CucsGmetaHolderFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1476, 1477, 1484, 1485, 1486))
    namedValues = NamedValues(("nop", 0), ("inventoryBegin", 1476), ("inventoryReportFullInventory", 1477), ("inventoryFail", 1484), ("inventorySuccess", 1485), ("inventoryCheckInventoryStatus", 1486))

class CucsGmetaHolderFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeGmetaHolderInventoryRegister", 12))

class CucsGmetaHolderFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1476))
    namedValues = NamedValues(("nop", 0), ("inventory", 1476))

class CucsGmetaInventoryStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("invDisable", 0), ("invEnable", 1), ("invStop", 2), ("invThrottled", 3))

class CucsGmetaPollInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 5, 10, 15, 30))
    namedValues = NamedValues(("never", 0), ("n1min", 1), ("n2min", 2), ("n5min", 5), ("n10min", 10), ("n15min", 15), ("n30min", 30))

class CucsHostagAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("none", 0))

class CucsHostagAgentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("indeterminate", 0), ("pnuosAgent", 1), ("hostAgent", 2))

class CucsHostagEvent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("none", 0))

class CucsHostimgComposition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("complete", 0), ("componentized", 1))

class CucsHostimgDistribution(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unknown", 0), ("fedora", 1))

class CucsHostimgImgType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("esxi", 1), ("kvm", 2), ("xen", 3), ("linux", 4), ("windows", 5), ("gpxeScript", 6))

class CucsHostimgType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("complete", 0), ("kernel", 1), ("fileSystem", 2), ("module", 3), ("gpxeScript", 4))

class CucsIdentConsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("vnic", 1), ("vhba", 2), ("server", 3), ("chassis", 4), ("vm", 5), ("vmnic", 6))

class CucsIdentIdDefinedInIdm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("no", 0), ("yes", 1))

class CucsIdentIdentReqIntent(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("requisition", 1), ("assign", 2), ("unassign", 3), ("addPooled", 4), ("deletePooled", 5))

class CucsIdentIdentRequestFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1336))
    namedValues = NamedValues(("nop", 0), ("updateIdent", 1336))

class CucsIdentIdentRequestFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1336, 1337, 1405, 1406))
    namedValues = NamedValues(("nop", 0), ("updateIdentBegin", 1336), ("updateIdentExecute", 1337), ("updateIdentFail", 1405), ("updateIdentSuccess", 1406))

class CucsIdentIdentRequestFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1336))
    namedValues = NamedValues(("nop", 0), ("updateIdent", 1336))

class CucsIdentIdentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("mac", 1), ("wwnn", 2), ("wwpn", 3), ("uuid", 4), ("vlan", 5), ("ipV4", 6), ("ipV6", 7), ("iqn", 8))

class CucsIdentMetaSystemFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1338))
    namedValues = NamedValues(("nop", 0), ("sync", 1338))

class CucsIdentMetaSystemFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1338, 1339, 1340, 1407, 1408))
    namedValues = NamedValues(("nop", 0), ("syncBegin", 1338), ("syncPing", 1339), ("syncExecute", 1340), ("syncFail", 1407), ("syncSuccess", 1408))

class CucsIdentMetaSystemFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1338))
    namedValues = NamedValues(("nop", 0), ("sync", 1338))

class CucsIdentRetStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("succeeded", 1), ("assignedByOther", 2), ("outOfSync", 3), ("failed", 4), ("synced", 5))

class CucsImgsecKeyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("public", 0), ("private", 1), ("shared", 2))

class CucsInitiatorFcInitiatorEpProt(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("derived", 0), ("fc", 1), ("iscsi", 2))

class CucsInitiatorGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("dedicated", 1), ("shared", 2), ("policy", 3))

class CucsInitiatorIScsiInitiatorEpProt(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("derived", 0), ("fc", 1), ("iscsi", 2))

class CucsInitiatorInitiatorEpPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("preferred", 0), ("alternate", 1))

class CucsIpIPv4DnsPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("preferred", 0), ("alternate", 1))

class CucsIpIpV4StaticAddrPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("preferred", 0), ("alternate", 1))

class CucsIpProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tcp", 1), ("udp", 2))

class CucsIpServiceIfPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("preferred", 0), ("alternate", 1))

class CucsIppoolPoolAssignmentOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("default", 0), ("sequential", 1))

class CucsIqnpoolBlockFrom(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CucsIqnpoolBlockTo(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CucsIqnpoolPoolAssignmentOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("default", 0), ("sequential", 1))

class CucsIscsiProtocolProfileConnectionTimeOut(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 255)

class CucsIscsiProtocolProfileDhcpTimeOut(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(60, 300)

class CucsIscsiProtocolProfileLunBusyRetryCount(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 60)

class CucsLicenseDownloadActivity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("restart", 0), ("idle", 1))

class CucsLicenseDownloaderFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 916))
    namedValues = NamedValues(("nop", 0), ("download", 916))

class CucsLicenseDownloaderFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 916, 917, 918, 919, 920, 921, 922, 994, 995))
    namedValues = NamedValues(("nop", 0), ("downloadBegin", 916), ("downloadLocal", 917), ("downloadValidateLocal", 918), ("downloadCopyRemote", 919), ("downloadDeleteLocal", 920), ("downloadValidateRemote", 921), ("downloadDeleteRemote", 922), ("downloadFail", 994), ("downloadSuccess", 995))

class CucsLicenseDownloaderFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 853))
    namedValues = NamedValues(("nop", 0), ("download", 853))

class CucsLicenseFeatureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("counted", 0), ("boolean", 1))

class CucsLicenseFileFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 923, 926))
    namedValues = NamedValues(("nop", 0), ("install", 923), ("clear", 926))

class CucsLicenseFileFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 923, 924, 925, 926, 927, 928, 996, 997, 998, 999))
    namedValues = NamedValues(("nop", 0), ("installBegin", 923), ("installLocal", 924), ("installRemote", 925), ("clearBegin", 926), ("clearLocal", 927), ("clearRemote", 928), ("clearFail", 996), ("clearSuccess", 997), ("installFail", 998), ("installSuccess", 999))

class CucsLicenseFileFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 858, 861))
    namedValues = NamedValues(("nop", 0), ("install", 858), ("clear", 861))

class CucsLicenseFileState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 0), ("installPending", 1), ("installing", 2), ("stale", 3), ("installed", 4), ("installFailed", 5), ("deletePending", 6), ("deleting", 7), ("deleted", 8), ("deleteFailed", 9), ("validated", 10))

class CucsLicenseInstanceFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 929))
    namedValues = NamedValues(("nop", 0), ("updateFlexlm", 929))

class CucsLicenseInstanceFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 929, 930, 931, 1000, 1001))
    namedValues = NamedValues(("nop", 0), ("updateFlexlmBegin", 929), ("updateFlexlmLocal", 930), ("updateFlexlmRemote", 931), ("updateFlexlmFail", 1000), ("updateFlexlmSuccess", 1001))

class CucsLicenseInstanceFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 864))
    namedValues = NamedValues(("nop", 0), ("updateFlexlm", 864))

class CucsLicensePeerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noPeer", 0), ("unknown", 1), ("lacks", 2), ("matching", 3))

class CucsLicenseScope(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("a", 1), ("b", 2), ("server", 3), ("unknown", 4))

class CucsLicenseState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("licenseOk", 1), ("licenseInsufficient", 2), ("licenseGraceperiod", 3), ("licenseExpired", 4), ("notApplicable", 5))

class CucsLicenseTransferState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("init", 0), ("downloading", 1), ("downloaded", 2), ("failed", 3))

class CucsLicenseTransport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ftp", 0), ("tftp", 1), ("scp", 2), ("sftp", 3), ("local", 4))

class CucsLicenseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("increment", 0), ("upgrade", 1), ("feature", 2))

class CucsLsAgentCapability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16))
    namedValues = NamedValues(("l2IfConfig", 1), ("l3IfConfig", 2), ("hostNameConfig", 4), ("stats", 8), ("states", 16))

class CucsLsAgentMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("noAgent", 1), ("readOnly", 2), ("full", 4))

class CucsLsApply(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("onAssociation", 1), ("runTime", 2))

class CucsLsAssignment(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unassigned", 0), ("assigned", 1), ("failed", 2))

class CucsLsAssocState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unassociated", 0), ("associating", 1), ("associated", 2), ("disassociating", 3), ("failed", 4))

class CucsLsComputeBindingOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unused", 0), ("used", 1), ("failedToApply", 2))

class CucsLsConfigIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("insufficientResources", 0), ("vnicCapacity", 1), ("vhbaCapacity", 2), ("fcoeCapacity", 3), ("switchVirtualIfCapacity", 4), ("macAddressAssignment", 5), ("wwpnAssignment", 6), ("wwnnAssignment", 7), ("systemUuidAssignment", 8), ("bootOrderSanImagePath", 9), ("bootOrderPxe", 10), ("computeUndiscovered", 11), ("adaptorProtectedEthCapability", 12), ("adaptorFcoeCapability", 13), ("incompatibleNumberOfLocalDisks", 14), ("adaptorRequirement", 15), ("memoryRequirement", 16), ("processorRequirement", 17), ("serverPositionRequirement", 18), ("computeUnavailable", 19), ("wwnnDerivationFromVhba", 20), ("bootConfigurationInvalid", 21), ("connectionPlacement", 22), ("wwpnDerivationVirtualizedPort", 23), ("macDerivationVirtualizedPort", 24), ("qosPolicyInvalid", 25), ("vlanPortCapacity", 26), ("physicalRequirement", 27), ("destructiveLocalDiskConfig", 28), ("powerGroupRequirement", 29), ("migration", 30), ("incompatibleBiosImage", 31), ("incompatibleDiskTypes", 32), ("incompatibleRaidLevel", 33), ("invalidWwn", 34), ("insufficientPowerBudget", 35), ("bootipPolicyInvalid", 36), ("hostimgPolicyInvalid", 37), ("imgsecPolicyInvalid", 38), ("provsrvPolicyInvalid", 39), ("pinningInvalid", 40), ("iscsiConfig", 41), ("vnicNotHaReady", 42), ("iscsiOverlayVnic", 43), ("missingPrimaryVlan", 44), ("missingRaidKey", 45), ("iscsiBootInvalid", 46), ("vifResourcesOverprovisioned", 47), ("bootOrderIscsi", 48), ("iscsiVnicInitiatorName", 49), ("iscsiVnicInvalidVlan", 50), ("storagePathConfigurationError", 51), ("zoneCapacity", 52), ("iscsiInitiatorIpAddress", 53), ("vfcVnicPvlanConflict", 54), ("vnicVconProvisioningChange", 55), ("namedVlanInaccessible", 56), ("iscsiIncompatibleOffloadSetting", 57), ("nonInterruptFsmRunning", 58), ("pinningVlanMismatch", 59), ("vnicVlanAssignmentError", 60), ("resourceOwnershipConflict", 61))

class CucsLsConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplied", 0), ("applying", 1), ("failedToApply", 2), ("applied", 3))

class CucsLsFcZoneGroupSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("dual", 3))

class CucsLsFcZoneState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notApplied", 0), ("applied", 1), ("applying", 2), ("applyPending", 3), ("notActive", 4), ("active", 5), ("created", 6), ("createFailed", 7), ("deleted", 8), ("zoneMergeFailure", 9))

class CucsLsOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 10, 11, 12, 13, 14, 15, 20, 21, 29, 30, 31, 32, 33, 34, 35, 36, 40, 41, 50, 60, 61, 62, 63, 101, 201, 202, 203, 204, 210, 211))
    namedValues = NamedValues(("indeterminate", 0), ("unassociated", 1), ("ok", 10), ("discovery", 11), ("config", 12), ("unconfig", 13), ("powerOff", 14), ("restart", 15), ("maintenance", 20), ("test", 21), ("computeMismatch", 29), ("computeFailed", 30), ("degraded", 31), ("discoveryFailed", 32), ("configFailure", 33), ("unconfigFailed", 34), ("testFailed", 35), ("maintenanceFailed", 36), ("removed", 40), ("disabled", 41), ("inaccessible", 50), ("thermalProblem", 60), ("powerProblem", 61), ("voltageProblem", 62), ("inoperable", 63), ("decomissioning", 101), ("biosRestore", 201), ("cmosReset", 202), ("diagnostics", 203), ("diagnosticsFailed", 204), ("pendingReboot", 210), ("pendingReassociation", 211))

class CucsLsOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))
    namedValues = NamedValues(("management", 1), ("physicalInherit", 2), ("physicalDefaultConfig", 4), ("tier", 8))

class CucsLsPowerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 31, 32, 33))
    namedValues = NamedValues(("down", 0), ("up", 1), ("cycleImmediate", 2), ("cycleWait", 3), ("hardResetImmediate", 4), ("hardResetWait", 5), ("softShutDown", 6), ("softShutDownOnly", 7), ("cmosResetImmediate", 12), ("bmcResetImmediate", 13), ("bmcResetWait", 14), ("diagnosticInterrupt", 15), ("kvmReset", 16), ("adminUp", 31), ("adminDown", 32), ("ipmiReset", 33))

class CucsLsServerFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 857))
    namedValues = NamedValues(("nop", 0), ("configure", 857))

class CucsLsServerFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 1002, 1003, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333, 1468, 1469, 1470))
    namedValues = NamedValues(("nop", 0), ("configureBegin", 857), ("configureApplyTemplate", 858), ("configureApplyIdentifiers", 859), ("configureApplyPolicies", 860), ("configureResolveBootConfig", 861), ("configureEvaluateAssociation", 862), ("configureAnalyzeImpact", 863), ("configureWaitForMaintPermission", 864), ("configureWaitForMaintWindow", 865), ("configureApplyConfig", 866), ("configureFail", 1002), ("configureSuccess", 1003), ("configureResolveIdentifiers", 1321), ("configureApplyDefaultIdentifiers", 1322), ("configureResolveDefaultIdentifiers", 1323), ("configureResolvePolicies", 1324), ("configureResolveDistributableNames", 1325), ("configureResolveDistributable", 1326), ("configureResolveImages", 1327), ("configureResolveSchedule", 1328), ("configureProvisionStorage", 1329), ("configureWaitForStorageProvision", 1330), ("configureCommitStorage", 1331), ("configureWaitForCommitStorage", 1332), ("configureWaitForAssocCompletion", 1333), ("configureResolveNetworkPolicies", 1468), ("configureResolveNetworkTemplates", 1469), ("configureValidatePolicyOwnership", 1470))

class CucsLsServerFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeLsServerConfigureLsRename", 7), ("samDmeLsServerConfigureModification", 49), ("samDmeLsServerConfigureFinalDisassoc", 50))

class CucsLsServerFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 965))
    namedValues = NamedValues(("nop", 0), ("configure", 965))

class CucsLsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("instance", 0), ("initialTemplate", 1), ("updatingTemplate", 2))

class CucsLsbootIScsiAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("readWrite", 0), ("readOnly", 1))

class CucsLsbootIScsiOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("n1", 1), ("n2", 2), ("n3", 3), ("n4", 4), ("n5", 5))

class CucsLsbootIScsiType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("virtualMedia", 1), ("storage", 2), ("lan", 3), ("iscsi", 4))

class CucsLsbootIScsiImagePathType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("primary", 0), ("secondary", 1))

class CucsLsbootLanAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("readWrite", 0), ("readOnly", 1))

class CucsLsbootLanOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("n1", 1), ("n2", 2), ("n3", 3), ("n4", 4), ("n5", 5))

class CucsLsbootLanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("virtualMedia", 1), ("storage", 2), ("lan", 3), ("iscsi", 4))

class CucsLsbootLanBootProt(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("pxe", 0), ("gpxe", 1), ("iSCSI", 2))

class CucsLsbootLanImagePathType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("primary", 0), ("secondary", 1))

class CucsLsbootPurpose(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("utility", 1), ("operational", 2))

class CucsLsbootSanImageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("primary", 0), ("secondary", 1))

class CucsLsbootSanImagePathType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("primary", 0), ("secondary", 1))

class CucsLsbootStorageAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("readWrite", 0), ("readOnly", 1))

class CucsLsbootStorageOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("n1", 1), ("n2", 2), ("n3", 3), ("n4", 4), ("n5", 5))

class CucsLsbootStorageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("virtualMedia", 1), ("storage", 2), ("lan", 3), ("iscsi", 4))

class CucsLsbootVirtualMediaAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("readWrite", 0), ("readOnly", 1))

class CucsLsbootVirtualMediaOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("n1", 1), ("n2", 2), ("n3", 3), ("n4", 4), ("n5", 5))

class CucsLsbootVirtualMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("virtualMedia", 1), ("storage", 2), ("lan", 3), ("iscsi", 4))

class CucsLsmaintAckChangeDetails(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("binding", 0), ("hostVirtEthIf", 1), ("hostNonvirtEthIf", 2), ("hostEthIfQos", 3), ("hostEthIfNwCtrl", 4), ("hostVirtFcIf", 6), ("hostNonvirtFcIf", 7), ("hostVirtFcIfPersBind", 8), ("hostNonvirtFcIfPersBind", 9), ("vif", 10), ("vlan", 11), ("vsan", 12), ("ip", 13), ("bootOrder", 14), ("bootLocalStorage", 16), ("bootVirtVnic", 18), ("bootNonvirtVnic", 19), ("biosFw", 20), ("storageControllerFw", 21), ("bootNonvirtPxe", 22), ("adaptorNwFw", 23), ("mgmtControllerFw", 24), ("localDiskPolicy", 25), ("pin", 26), ("sol", 27), ("epAuth", 28), ("biosProfile", 29), ("checkpoint", 30), ("implicitReboot", 31), ("implicitHostFcIfProfileRedeploy", 32), ("boardControllerFw", 33), ("hostEthIfQosHostControl", 40), ("localDiskFw", 41), ("implicitHostEthIfProfileRedeploy", 42), ("storagePath", 43), ("hostIfPcie", 45), ("flexflashConfig", 46), ("flexflashReboot", 47))

class CucsLsmaintAckChanges(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("serverIdentity", 0), ("storage", 1), ("networking", 2), ("vnicVhbaPlacement", 3), ("serverAssignment", 4), ("operationalPolicies", 5))

class CucsLsmaintAckDisr(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("upTime", 0))

class CucsLsmaintChangeMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 16, 32, 64, 128, 256))
    namedValues = NamedValues(("noChange", 0), ("unconfig", 1), ("forceUnconfig", 2), ("rediscover", 4), ("config", 8), ("diagConfig", 16), ("diagUnconfig", 32), ("removeConfig", 64), ("diag", 128), ("configEvaluation", 256))

class CucsMacpoolPoolAssignmentOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("default", 0), ("sequential", 1))

class CucsMemoryAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("policy", 1), ("resetErrors", 2))

class CucsMemoryArrayId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 8)

class CucsMemoryArrayEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("inputCurrent", 0), ("inputCurrentAvg", 1), ("inputCurrentMax", 2), ("inputCurrentMin", 3))

class CucsMemoryArrayEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("inputCurrent", 0), ("inputCurrentAvg", 1), ("inputCurrentMax", 2), ("inputCurrentMin", 3))

class CucsMemoryBufferUnitId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 16)

class CucsMemoryBufferUnitEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("temperature", 0), ("temperatureAvg", 1), ("temperatureMax", 2), ("temperatureMin", 3))

class CucsMemoryBufferUnitEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("temperature", 0), ("temperatureAvg", 1), ("temperatureMax", 2), ("temperatureMin", 3))

class CucsMemoryErrorCorrection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undiscovered", 0), ("other", 1), ("unknown", 2), ("none", 3), ("parity", 4), ("singleBitECC", 5), ("multiBitECC", 6), ("crc", 7))

class CucsMemoryErrorStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("addressParityErrors", 0), ("eccMultibitErrors", 1), ("eccSinglebitErrors", 2), ("mismatchErrors", 3))

class CucsMemoryFormFactor(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 9, 10, 12, 13, 14, 15))
    namedValues = NamedValues(("undiscovered", 0), ("other", 1), ("unknown", 2), ("simm", 3), ("dimm", 9), ("tsop", 10), ("rimm", 12), ("sodimm", 13), ("srimm", 14), ("fbDimm", 15))

class CucsMemoryIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("uncorrectableEccError", 0), ("correctableEccError", 1), ("addressParityError", 2), ("memoryMismatchError", 3))

class CucsMemoryRuntimeThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("available", 0), ("availableAvg", 1), ("availableMax", 2), ("availableMin", 3), ("cached", 4), ("cachedAvg", 5), ("cachedMax", 6), ("cachedMin", 7), ("total", 8), ("totalAvg", 9), ("totalMax", 10), ("totalMin", 11))

class CucsMemoryRuntimeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("swap", 1), ("total", 2))

class CucsMemoryRuntimeHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("available", 0), ("availableAvg", 1), ("availableMax", 2), ("availableMin", 3), ("cached", 4), ("cachedAvg", 5), ("cachedMax", 6), ("cachedMin", 7), ("total", 8), ("totalAvg", 9), ("totalMax", 10), ("totalMin", 11))

class CucsMemoryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25))
    namedValues = NamedValues(("undiscovered", 0), ("other", 1), ("unknown", 2), ("dram", 3), ("edram", 4), ("vram", 5), ("sram", 6), ("ram", 7), ("rom", 8), ("flash", 9), ("eeprom", 10), ("feprom", 11), ("eprom", 12), ("cdram", 13), ("n3DRAM", 14), ("sdram", 15), ("sgram", 16), ("rdram", 17), ("ddr", 18), ("ddr2", 19), ("ddr2FbDimm", 20), ("ddr3", 24), ("fbd2", 25))

class CucsMemoryUnitId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 256)

class CucsMemoryUnitOperability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 51, 52, 81, 82, 83, 84, 100, 101, 102, 103, 104, 105, 106, 107, 108))
    namedValues = NamedValues(("unknown", 0), ("operable", 1), ("inoperable", 2), ("degraded", 3), ("poweredOff", 4), ("powerProblem", 5), ("removed", 6), ("voltageProblem", 7), ("thermalProblem", 8), ("performanceProblem", 9), ("accessibilityProblem", 10), ("identityUnestablishable", 11), ("biosPostTimeout", 12), ("disabled", 13), ("malformedFru", 14), ("fabricConnProblem", 51), ("fabricUnsupportedConn", 52), ("config", 81), ("equipmentProblem", 82), ("decomissioning", 83), ("chassisLimitExceeded", 84), ("notSupported", 100), ("discovery", 101), ("discoveryFailed", 102), ("identify", 103), ("postFailure", 104), ("upgradeProblem", 105), ("peerCommProblem", 106), ("autoUpgrade", 107), ("linkActivateBlocked", 108))

class CucsMemoryUnitEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("temperature", 0), ("temperatureAvg", 1), ("temperatureMax", 2), ("temperatureMin", 3))

class CucsMemoryUnitEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("temperature", 0), ("temperatureAvg", 1), ("temperatureMax", 2), ("temperatureMin", 3))

class CucsMemoryVisibility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("yes", 1), ("no", 2))

class CucsMgmtAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("unspecified", 0), ("inBand", 1), ("outOfBand", 2), ("internal", 4), ("virtual", 8))

class CucsMgmtAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class CucsMgmtBackupPostAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("remove", 1))

class CucsMgmtBackupProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("ftp", 1), ("tftp", 2), ("scp", 3), ("http", 4), ("sftp", 5), ("nfsCopy", 6))

class CucsMgmtBackupFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 290))
    namedValues = NamedValues(("nop", 0), ("backup", 290))

class CucsMgmtBackupFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 290, 291, 292, 398, 399))
    namedValues = NamedValues(("nop", 0), ("backupBegin", 290), ("backupBackupLocal", 291), ("backupUpload", 292), ("backupFail", 398), ("backupSuccess", 399))

class CucsMgmtBackupFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 290))
    namedValues = NamedValues(("nop", 0), ("backup", 290))

class CucsMgmtBackupInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(86400, 604800, 1209600))
    namedValues = NamedValues(("n1day", 86400), ("n1week", 604800), ("n2week", 1209600))

class CucsMgmtBackupJob(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2))
    namedValues = NamedValues(("immediate", 2))

class CucsMgmtBackupPolicyFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1187))
    namedValues = NamedValues(("nop", 0), ("reportConfigCopy", 1187))

class CucsMgmtBackupPolicyFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1187, 1188, 1411, 1412))
    namedValues = NamedValues(("nop", 0), ("reportConfigCopyBegin", 1187), ("reportConfigCopyReport", 1188), ("reportConfigCopyFail", 1411), ("reportConfigCopySuccess", 1412))

class CucsMgmtBackupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("fullState", 1), ("configAll", 2), ("configSystem", 3), ("configLogical", 4))

class CucsMgmtCfgExportPolicyFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1187))
    namedValues = NamedValues(("nop", 0), ("reportConfigCopy", 1187))

class CucsMgmtCfgExportPolicyFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1187, 1188, 1411, 1412))
    namedValues = NamedValues(("nop", 0), ("reportConfigCopyBegin", 1187), ("reportConfigCopyReport", 1188), ("reportConfigCopyFail", 1411), ("reportConfigCopySuccess", 1412))

class CucsMgmtConnectionState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unInitialized", 0), ("acknowledged", 1), ("unsupportedConnectivity", 2))

class CucsMgmtControllerFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 17, 248, 253, 256, 259, 262, 467, 474, 1059, 1191))
    namedValues = NamedValues(("nop", 0), ("extMgmtIfConfig", 17), ("updateSwitch", 248), ("updateIOM", 253), ("activateIOM", 256), ("updateBMC", 259), ("activateBMC", 262), ("updateUCSManager", 467), ("sysConfig", 474), ("online", 1059), ("registryConfig", 1191))

class CucsMgmtControllerFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 17, 18, 19, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 412, 413, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 1059, 1060, 1061, 1062, 1063, 1075, 1076, 1191, 1192, 1357, 1358, 1359, 1360, 1409, 1410))
    namedValues = NamedValues(("nop", 0), ("extMgmtIfConfigBegin", 17), ("extMgmtIfConfigPrimary", 18), ("extMgmtIfConfigSecondary", 19), ("updateSwitchBegin", 248), ("updateSwitchUpdateLocal", 249), ("updateSwitchResetLocal", 250), ("updateSwitchUpdateRemote", 251), ("updateSwitchResetRemote", 252), ("updateIOMBegin", 253), ("updateIOMUpdateRequest", 254), ("updateIOMPollUpdateStatus", 255), ("activateIOMBegin", 256), ("activateIOMActivate", 257), ("activateIOMReset", 258), ("updateBMCBegin", 259), ("updateBMCUpdateRequest", 260), ("updateBMCPollUpdateStatus", 261), ("activateBMCBegin", 262), ("activateBMCActivate", 263), ("activateBMCReset", 264), ("activateBMCFail", 400), ("activateBMCSuccess", 401), ("activateIOMFail", 402), ("activateIOMSuccess", 403), ("extMgmtIfConfigFail", 404), ("extMgmtIfConfigSuccess", 405), ("updateBMCFail", 406), ("updateBMCSuccess", 407), ("updateIOMFail", 408), ("updateIOMSuccess", 409), ("updateSwitchFail", 412), ("updateSwitchSuccess", 413), ("updateUCSManagerBegin", 467), ("updateUCSManagerExecute", 468), ("updateUCSManagerFail", 469), ("updateUCSManagerSuccess", 470), ("updateUCSManagerStart", 471), ("updateSwitchVerifyLocal", 472), ("updateSwitchVerifyRemote", 473), ("sysConfigBegin", 474), ("sysConfigPrimary", 475), ("sysConfigSecondary", 476), ("sysConfigFail", 477), ("sysConfigSuccess", 478), ("onlineBegin", 1059), ("onlineBmcConfigureConnLocal", 1060), ("onlineSwConfigureConnLocal", 1061), ("onlineBmcConfigureConnPeer", 1062), ("onlineSwConfigureConnPeer", 1063), ("onlineFail", 1075), ("onlineSuccess", 1076), ("registryConfigBegin", 1191), ("registryConfigRemove", 1192), ("updateUCSManagerCopyExtToLocal", 1357), ("updateUCSManagerCopyExtToPeer", 1358), ("updateSwitchCopyToLocal", 1359), ("updateSwitchCopyToPeer", 1360), ("registryConfigFail", 1409), ("registryConfigSuccess", 1410))

class CucsMgmtControllerFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeMgmtControllerUpdateSwitchActivate", 14), ("samDmeMgmtControllerUpdateSwitchReset", 15))

class CucsMgmtControllerFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 17, 248, 253, 256, 259, 262, 467, 474, 1059, 1191))
    namedValues = NamedValues(("nop", 0), ("extMgmtIfConfig", 17), ("updateSwitch", 248), ("updateIOM", 253), ("activateIOM", 256), ("updateBMC", 259), ("activateBMC", 262), ("updateUCSManager", 467), ("sysConfig", 474), ("online", 1059), ("registryConfig", 1191))

class CucsMgmtEntityChassisDeviceIoState1(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("openError", 2), ("readError", 3), ("writeError", 4))

class CucsMgmtEntityChassisDeviceIoState2(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("openError", 2), ("readError", 3), ("writeError", 4))

class CucsMgmtEntityChassisDeviceIoState3(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("ok", 1), ("openError", 2), ("readError", 3), ("writeError", 4))

class CucsMgmtEntityHaFailureReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 0), ("nodeDown", 1), ("peerNodeDown", 2), ("mgmtServicesUnresponsive", 3), ("peerMgmtServicesUnresponsive", 4), ("chassisConfigIncomplete", 5), ("peerChassisConfigIncomplete", 6), ("networkInterfaceDown", 7))

class CucsMgmtEntityHaReadiness(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("ready", 1), ("downgraded", 2), ("notReady", 3))

class CucsMgmtEntityLeadership(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("primary", 1), ("subordinate", 2), ("inapplicable", 3), ("electionInProgress", 4), ("electionFailed", 5))

class CucsMgmtEntityMgmtServicesState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("up", 1), ("unresponsive", 2), ("down", 3), ("switchoverInProgress", 4))

class CucsMgmtEntityProblems(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("leadership", 0), ("membership", 1), ("umbilical", 2), ("haReady", 3), ("versionMismatch", 4))

class CucsMgmtEntityState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("up", 1), ("down", 2))

class CucsMgmtEntityUmbilicalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("degraded", 1), ("full", 2), ("failed", 3))

class CucsMgmtExportPolicyAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class CucsMgmtExportPolicyProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("ftp", 1), ("tftp", 2), ("scp", 3), ("http", 4), ("sftp", 5), ("nfsCopy", 6))

class CucsMgmtExportPolicyFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1187))
    namedValues = NamedValues(("nop", 0), ("reportConfigCopy", 1187))

class CucsMgmtExportPolicyFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1187, 1188, 1411, 1412))
    namedValues = NamedValues(("nop", 0), ("reportConfigCopyBegin", 1187), ("reportConfigCopyReport", 1188), ("reportConfigCopyFail", 1411), ("reportConfigCopySuccess", 1412))

class CucsMgmtExportPolicyFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1187))
    namedValues = NamedValues(("nop", 0), ("reportConfigCopy", 1187))

class CucsMgmtIfFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 277, 279, 281, 284, 286, 288))
    namedValues = NamedValues(("nop", 0), ("swMgmtOobIfConfig", 277), ("swMgmtInbandIfConfig", 279), ("virtualIfConfig", 281), ("enableVip", 284), ("disableVip", 286), ("enableHA", 288))

class CucsMgmtIfFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425))
    namedValues = NamedValues(("nop", 0), ("swMgmtOobIfConfigBegin", 277), ("swMgmtOobIfConfigSwitch", 278), ("swMgmtInbandIfConfigBegin", 279), ("swMgmtInbandIfConfigSwitch", 280), ("virtualIfConfigBegin", 281), ("virtualIfConfigLocal", 282), ("virtualIfConfigRemote", 283), ("enableVipBegin", 284), ("enableVipLocal", 285), ("disableVipBegin", 286), ("disableVipPeer", 287), ("enableHABegin", 288), ("enableHALocal", 289), ("disableVipFail", 414), ("disableVipSuccess", 415), ("enableHAFail", 416), ("enableHASuccess", 417), ("enableVipFail", 418), ("enableVipSuccess", 419), ("swMgmtInbandIfConfigFail", 420), ("swMgmtInbandIfConfigSuccess", 421), ("swMgmtOobIfConfigFail", 422), ("swMgmtOobIfConfigSuccess", 423), ("virtualIfConfigFail", 424), ("virtualIfConfigSuccess", 425))

class CucsMgmtIfFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 277, 279, 281, 284, 286, 288))
    namedValues = NamedValues(("nop", 0), ("swMgmtOobIfConfig", 277), ("swMgmtInbandIfConfig", 279), ("virtualIfConfig", 281), ("enableVip", 284), ("disableVip", 286), ("enableHA", 288))

class CucsMgmtImportAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("merge", 0), ("replace", 1))

class CucsMgmtImportStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("downloadSuccess", 0), ("configSuccess", 1))

class CucsMgmtImporterPostAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("remove", 1))

class CucsMgmtImporterProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("ftp", 1), ("tftp", 2), ("scp", 3), ("http", 4), ("sftp", 5), ("nfsCopy", 6))

class CucsMgmtImporterFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 293, 1189))
    namedValues = NamedValues(("nop", 0), ("import", 293), ("reportConfigImport", 1189))

class CucsMgmtImporterFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 293, 294, 426, 427, 580, 626, 1189, 1190, 1413, 1414))
    namedValues = NamedValues(("nop", 0), ("importBegin", 293), ("importDownloadLocal", 294), ("importFail", 426), ("importSuccess", 427), ("importConfig", 580), ("importReportResults", 626), ("reportConfigImportBegin", 1189), ("reportConfigImportReport", 1190), ("reportConfigImportFail", 1413), ("reportConfigImportSuccess", 1414))

class CucsMgmtImporterFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 293, 1189))
    namedValues = NamedValues(("nop", 0), ("import", 293), ("reportConfigImport", 1189))

class CucsMgmtIntAuthPolicyMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("password", 1))

class CucsMgmtPmonEntryState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 0), ("idle", 1), ("running", 2), ("pending", 3), ("failed", 4), ("error", 5), ("exitPending", 6), ("terminated", 7), ("killed", 8))

class CucsMgmtSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unspecified", 0), ("sharedLom", 1), ("sideband", 2))

class CucsMgmtStateQual(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unspecified", 0), ("valid", 1), ("misconnected", 2))

class CucsMgmtSubject(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 16, 32, 64))
    namedValues = NamedValues(("unknown", 0), ("blade", 1), ("chassis", 2), ("system", 4), ("switch", 8), ("adaptor", 16), ("iocard", 32), ("boardController", 64))

class CucsMgmtUpgradeStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("hwChangeDetected", 0), ("fwChangeDetected", 1), ("hwIncompatible", 2), ("fwIncompatible", 3), ("unsupportedHwVersion", 4), ("unsupportedFwVersion", 5), ("hwChangeSuccess", 6), ("fwChangeSuccess", 7))

class CucsMoMoClassId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254), SingleValueConstraint(255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511), SingleValueConstraint(512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779), SingleValueConstraint(780, 781, 789, 790, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 817, 818, 819, 820, 822, 823, 825, 826, 828, 830, 831, 832, 835, 838, 840, 841, 842, 843, 845, 848, 849, 850, 851, 852, 853, 854, 857, 860, 861, 862, 863, 864, 869, 870, 871, 873, 874, 876, 879, 882, 884, 886, 888, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 926, 931, 932, 933, 934, 935, 936, 937, 938, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089), SingleValueConstraint(1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1282, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353), SingleValueConstraint(1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608), SingleValueConstraint(1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627, 1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646, 1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665, 1666, 1667, 1668, 1669, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1681, 1682, 1683, 1684, 1685, 1686, 1688, 1689, 1690, 1691, 1692, 1693, 1694, 1695, 1696, 1697, 1698, 1699, 1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709, 1710, 1711, 1712, 1713, 1714))
    namedValues = NamedValues(("unspecified", 0), ("moTopProps", 1), ("topRoot", 2), ("topSystem", 3), ("fsmTask", 4), ("namingNamedObject", 5), ("namingNamedIdentifiedObject", 6), ("conditionInfo", 7), ("conditionReportable", 8), ("conditionMutable", 9), ("conditionImmutable", 10), ("conditionMultiInstanceImmutable", 11), ("conditionPolicy", 12), ("conditionLog", 13), ("conditionLoggable", 14), ("aaaLog", 15), ("aaaUserAction", 16), ("aaaModLR", 17), ("aaaSessionLR", 18), ("eventEpCtrl", 19), ("eventLog", 20), ("eventRecord", 21), ("eventHolder", 22), ("eventInst", 23), ("eventPolicy", 24), ("faultHolder", 25), ("faultInst", 26), ("faultPolicy", 27), ("statsItem", 28), ("statsCurr", 29), ("statsHist", 30), ("statsHolder", 31), ("statsCollectionPolicy", 32), ("statsThresholdPolicy", 33), ("statsThresholdClass", 34), ("statsThresholdDefinition", 35), ("statsThr32Definition", 36), ("statsThr64Definition", 37), ("statsThrFloatDefinition", 38), ("statsThresholdValue", 39), ("statsThr32Value", 40), ("statsThr64Value", 41), ("statsThrFloatValue", 42), ("equipmentPOSTCodeReporter", 43), ("equipmentPOSTCodeData", 44), ("equipmentPOSTCode", 45), ("equipmentPOST", 46), ("swatInjection", 47), ("swatTrigger", 48), ("swatCondition", 49), ("swatTarget", 50), ("swatAction", 51), ("swatResultstats", 52), ("apeControllerManager", 53), ("apeControllerChassis", 54), ("apeControllerEeprom", 55), ("apeNicAgManager", 56), ("apeAdapter", 57), ("apeMenlo", 58), ("apePalo", 59), ("apeAdapterVnic", 60), ("apeMenloVnic", 61), ("apeMenloVnicStats", 62), ("apeManager", 63), ("apeMc", 64), ("apeMcTable", 65), ("apeFru", 66), ("apeSdr", 67), ("apeReading", 68), ("apeParam", 69), ("apeBootMethod", 70), ("apeLANBoot", 71), ("apeSANBoot", 72), ("apeLocalDiskBoot", 73), ("apeVirtualMediaBoot", 74), ("apeHostAgent", 75), ("clitestTypeTest", 76), ("clitestTypeTestParent", 77), ("clitestTypeTestChild", 78), ("clitestTypeTest2", 79), ("fabricInternalDceSrv", 80), ("fabricDceSrv", 81), ("fabricDceSwSrv", 82), ("fabricSwSrvEp", 83), ("fabricADceSwSrvEp", 84), ("fabricDceSwSrvEp", 85), ("fabricSan", 86), ("fabricFcSan", 87), ("fabricSanEp", 88), ("fabricAFcSanEp", 89), ("fabricFcSanEp", 90), ("fabricFcSanPcEp", 91), ("fabricSanPc", 92), ("fabricFcSanPc", 93), ("fabricFcVsanPortEp", 94), ("fabricSanPinGroup", 95), ("fabricSanPinTarget", 96), ("fabricEp", 97), ("fabricCloud", 98), ("fabricSanCloud", 99), ("fabricLanCloud", 100), ("fabricDomain", 101), ("fabricExternal", 102), ("fabricInternal", 103), ("fabricPIoEp", 104), ("fabricExternalEp", 105), ("fabricInternalEp", 106), ("fabricCIoEp", 107), ("fabricExternalPc", 108), ("fabricInternalPc", 109), ("fabricPinGroup", 110), ("fabricPinTarget", 111), ("fabricLan", 112), ("fabricEthLan", 113), ("fabricLanEp", 114), ("fabricAEthLanEp", 115), ("fabricEthLanEp", 116), ("fabricEthLanPcEp", 117), ("fabricLanPc", 118), ("fabricEthLanPc", 119), ("fabricLanPinGroup", 120), ("fabricLanPinTarget", 121), ("fabricLocale", 122), ("fabricPath", 123), ("fabricPathEp", 124), ("fabricPathConn", 125), ("fabricVnetEp", 126), ("fabricAVlan", 127), ("fabricEpVlan", 128), ("fabricAVsan", 129), ("fabricEpVsan", 130), ("fabricVsan", 131), ("fabricVsanEp", 132), ("fabricVlan", 133), ("fabricSwChEp", 134), ("fabricSwChPhEp", 135), ("fabricComputeEp", 136), ("fabricChassisEp", 137), ("fabricComputeSlotEp", 138), ("fabricIf", 139), ("fabricComputePhEp", 140), ("fabricLastAckedSlot", 141), ("processorUnit", 142), ("processorComponent", 143), ("processorCore", 144), ("processorThread", 145), ("processorRuntime", 146), ("processorRuntimeHist", 147), ("processorQual", 148), ("fcPIo", 149), ("fcConfig", 150), ("fcIfConfig", 151), ("fcSwIfConfig", 152), ("fcNicIfConfig", 153), ("fcStats", 154), ("fcStatsHist", 155), ("fcErrStats", 156), ("fcErrStatsHist", 157), ("biosUnit", 158), ("vnicTempl", 159), ("vnicSanConnTempl", 160), ("vnicLanConnTempl", 161), ("vnicL3If", 162), ("vnicIPIf", 163), ("vnicIPv4If", 164), ("vnicIpAddr", 165), ("vnicIpV4Addr", 166), ("vnicIpV4StaticAddr", 167), ("vnicIpV4PooledAddr", 168), ("vnicIPv4Dhcp", 169), ("vnicIPv4Dns", 170), ("vnicIPv4StaticRoute", 171), ("vnicConnection", 172), ("vnicNicConn", 173), ("vnicVnic", 174), ("vnicIf", 175), ("vnicL2Lif", 176), ("vnicEthLif", 177), ("vnicFcLif", 178), ("vnicLifVlan", 179), ("vnicLifVsan", 180), ("vnicL2If", 181), ("vnicAFcIf", 182), ("vnicEtherBaseIf", 183), ("vnicAEtherIf", 184), ("vnicAIpcIf", 185), ("vnicAScsiIf", 186), ("vnicFcOEIf", 187), ("vnicFcIf", 188), ("vnicEtherIf", 189), ("vnicIpcIf", 190), ("vnicScsiIf", 191), ("vnicProfileSet", 192), ("vnicProfile", 193), ("vnicProfileAlias", 194), ("vnicDynamicConReq", 195), ("vnicDynamicConPolicy", 196), ("vnicDynamicCon", 197), ("vnicDynamicIdUniverse", 198), ("vnicDynamicProvider", 199), ("vnicDynamicProviderEp", 200), ("vnicFcNode", 201), ("vnicFcBase", 202), ("vnicFc", 203), ("vnicEtherBase", 204), ("vnicEther", 205), ("vnicIpc", 206), ("vnicScsi", 207), ("vnicBootTarget", 208), ("lsbootItem", 209), ("lsbootADef", 210), ("lsbootPolicy", 211), ("lsbootDef", 212), ("lsbootCategory", 213), ("lsbootStorage", 214), ("lsbootLan", 215), ("lsbootVirtualMedia", 216), ("lsbootImage", 217), ("lsbootRemoteImage", 218), ("lsbootSanImage", 219), ("lsbootLocalImage", 220), ("lsbootLocalStorage", 221), ("lsbootImagePath", 222), ("lsbootLanImagePath", 223), ("lsbootSanImagePath", 224), ("procManager", 225), ("procProcCounts", 226), ("procTxCounts", 227), ("procStimulusCounts", 228), ("procPrtCounts", 229), ("procProcs", 230), ("procPrt", 231), ("procDoer", 232), ("storageController", 233), ("storageUnit", 234), ("storagePhysical", 235), ("storageLogical", 236), ("storageLocalLun", 237), ("storageLocalDisk", 238), ("storageLunDisk", 239), ("storageQual", 240), ("storageItem", 241), ("storageLocalDiskConfig", 242), ("storageLocalDiskConfigPolicy", 243), ("storageLocalDiskConfigDef", 244), ("storageLocalDiskPartition", 245), ("memoryArray", 246), ("memoryUnit", 247), ("memoryRuntime", 248), ("memoryRuntimeHist", 249), ("memoryQual", 250), ("aaaRealm", 251), ("aaaAuthRealm", 252), ("aaaEp", 253), ("aaaRadiusEp", 254)) + NamedValues(("aaaLdapEp", 255), ("aaaTacacsPlusEp", 256), ("aaaProvider", 257), ("aaaRadiusProvider", 258), ("aaaLdapProvider", 259), ("aaaTacacsPlusProvider", 260), ("pkiEp", 261), ("pkiItem", 262), ("pkiCertReq", 263), ("pkiKeyRing", 264), ("pkiTP", 265), ("aaaDefinition", 266), ("commDefinition", 267), ("pkiDefinition", 268), ("commSvcEp", 269), ("commSvcChannel", 270), ("commWebChannel", 271), ("commEvtChannel", 272), ("commSvc", 273), ("commWeb", 274), ("commHttp", 275), ("commHttps", 276), ("commWsman", 277), ("commCimxml", 278), ("commShell", 279), ("commTelnet", 280), ("commSsh", 281), ("commSmashCLP", 282), ("commSnmp", 283), ("commDateTime", 284), ("commSnmpTrap", 285), ("commDns", 286), ("commClient", 287), ("commNtpProvider", 288), ("commDnsProvider", 289), ("commSyslog", 290), ("commSyslogConsole", 291), ("commSyslogMonitor", 292), ("commSyslogFile", 293), ("commSyslogClient", 294), ("aaaUserEp", 295), ("aaaSystemUser", 296), ("aaaEpAuthProfile", 297), ("aaaUserLogin", 298), ("aaaShellLogin", 299), ("aaaWebLogin", 300), ("aaaEpLogin", 301), ("aaaRemoteUser", 302), ("aaaEpUser", 303), ("aaaUser", 304), ("aaaSshAuth", 305), ("aaaUserRole", 306), ("aaaRole", 307), ("aaaUserLocale", 308), ("aaaLocale", 309), ("aaaOrg", 310), ("aaaSession", 311), ("dcxVifEp", 312), ("dcxVc", 313), ("dcxVIf", 314), ("dcxUniverse", 315), ("dcxNs", 316), ("adaptorFruCapProvider", 317), ("adaptorFwCapProvider", 318), ("adaptorCapDef", 319), ("adaptorCapQual", 320), ("adaptorCapSpec", 321), ("adaptorQual", 322), ("adaptorBehCap", 323), ("adaptorLanCap", 324), ("adaptorMgmtCap", 325), ("adaptorNwMgmtCap", 326), ("adaptorHostMgmtCap", 327), ("adaptorUnit", 328), ("adaptorHostIf", 329), ("adaptorHostEthIf", 330), ("adaptorHostFcIf", 331), ("adaptorExtIf", 332), ("adaptorExtEthIf", 333), ("adaptorVsan", 334), ("adaptorFcOEIf", 335), ("adaptorVlan", 336), ("adaptorEthPortStats", 337), ("adaptorEthPortStatsHist", 338), ("adaptorEthPortBySizeSmallStats", 341), ("adaptorEthPortBySizeSmallStatsHist", 342), ("adaptorEthPortBySizeLargeStats", 343), ("adaptorEthPortBySizeLargeStatsHist", 344), ("adaptorEthPortOutsizedStats", 345), ("adaptorEthPortOutsizedStatsHist", 346), ("adaptorEthPortMcastStats", 347), ("adaptorEthPortMcastStatsHist", 348), ("adaptorEthPortErrStats", 349), ("adaptorEthPortErrStatsHist", 350), ("adaptorFcPortStats", 351), ("adaptorFcPortStatsHist", 352), ("adaptorVnicStats", 353), ("adaptorVnicStatsHist", 354), ("adaptorFcIfFC4Stats", 355), ("adaptorFcIfFC4StatsHist", 356), ("adaptorMenloBaseErrorStats", 357), ("adaptorMenloBaseErrorStatsHist", 358), ("adaptorMenloMcpuStats", 359), ("adaptorMenloMcpuStatsHist", 360), ("adaptorMenloMcpuErrorStats", 361), ("adaptorMenloMcpuErrorStatsHist", 362), ("adaptorMenloEthStats", 363), ("adaptorMenloEthStatsHist", 364), ("adaptorMenloEthErrorStats", 365), ("adaptorMenloEthErrorStatsHist", 366), ("adaptorMenloFcStats", 367), ("adaptorMenloFcStatsHist", 368), ("adaptorMenloFcErrorStats", 369), ("adaptorMenloFcErrorStatsHist", 370), ("adaptorMenloQStats", 371), ("adaptorMenloQStatsHist", 372), ("adaptorMenloQErrorStats", 373), ("adaptorMenloQErrorStatsHist", 374), ("adaptorMenloNetEgStats", 375), ("adaptorMenloNetEgStatsHist", 376), ("adaptorMenloNetInStats", 377), ("adaptorMenloNetInStatsHist", 378), ("adaptorMenloHostPortStats", 379), ("adaptorMenloHostPortStatsHist", 380), ("adaptorMenloDcePortStats", 381), ("adaptorMenloDcePortStatsHist", 382), ("adaptorEtherIfStats", 383), ("adaptorEtherIfStatsHist", 384), ("adaptorFcIfFrameStats", 385), ("adaptorFcIfFrameStatsHist", 386), ("adaptorFcIfEventStats", 387), ("adaptorFcIfEventStatsHist", 388), ("adaptorHostIfProfile", 389), ("adaptorHostEthIfProfile", 390), ("adaptorHostFcIfProfile", 391), ("adaptorProfileItem", 392), ("adaptorQueueProfile", 393), ("adaptorFcLogiProfile", 394), ("adaptorEthQueueProfile", 395), ("adaptorFcQueueProfile", 396), ("adaptorEthWorkQueueProfile", 397), ("adaptorEthRecvQueueProfile", 398), ("adaptorEthCompQueueProfile", 399), ("adaptorEthInterruptProfile", 400), ("adaptorRssProfile", 401), ("adaptorRssHashProfile", 402), ("adaptorTcpIpRssHashProfile", 403), ("adaptorIpV4RssHashProfile", 404), ("adaptorIpV6RssHashProfile", 405), ("adaptorExtIpV6RssHashProfile", 406), ("adaptorEthOffloadProfile", 407), ("adaptorEthFailoverProfile", 408), ("adaptorFcRecvQueueProfile", 409), ("adaptorFcWorkQueueProfile", 410), ("adaptorFcCdbWorkQueueProfile", 411), ("adaptorFcPortFLogiProfile", 412), ("adaptorFcPortPLogiProfile", 413), ("adaptorFcPortProfile", 414), ("adaptorFcErrorRecoveryProfile", 415), ("sysfileEp", 416), ("sysfileRepository", 417), ("sysfileExporter", 418), ("sysfileImporter", 419), ("sysfileMutation", 420), ("sysfileInstance", 421), ("sysdebugEp", 422), ("sysdebugRepository", 423), ("sysdebugCoreFileRepository", 424), ("sysdebugExporter", 425), ("sysdebugCoreFileExportTarget", 426), ("sysdebugAutoCoreFileExportTarget", 427), ("sysdebugManualCoreFileExportTarget", 428), ("sysdebugFile", 429), ("sysdebugCore", 430), ("sysdebugLogControlEp", 431), ("sysdebugLogControlDomain", 432), ("sysdebugLogControlModule", 433), ("sysdebugLogControlDestinationFile", 434), ("sysdebugLogControlDestinationSyslog", 435), ("ruleDefinition", 436), ("ruleItem", 437), ("ruleRequirement", 438), ("ruleSizeRequirement", 439), ("swDomain", 440), ("swPIoEp", 441), ("swCIoEp", 442), ("swBorderDomain", 443), ("swBorderEp", 444), ("swBorderPc", 445), ("swLanBorder", 446), ("swLanEp", 447), ("swLanPc", 448), ("swEthLanBorder", 449), ("swEthLanEp", 450), ("swEthLanPc", 451), ("swVlan", 452), ("swUlan", 453), ("swAccessDomain", 454), ("swAccessEp", 455), ("swUtilityDomain", 456), ("swSanBorder", 457), ("swSanEp", 458), ("swFcSanBorder", 459), ("swFcSanEp", 460), ("swVsan", 461), ("swEnvStats", 462), ("swEnvStatsHist", 463), ("swSystemStats", 464), ("swSystemStatsHist", 465), ("networkruleDefinition", 466), ("networkruleItem", 467), ("networkruleRequirement", 468), ("etherPIo", 469), ("etherServerIntFIo", 470), ("etherSwitchIntFIo", 471), ("etherConfig", 472), ("etherIfConfig", 473), ("etherSwIfConfig", 474), ("etherNicIfConfig", 475), ("etherTxStats", 476), ("etherTxStatsHist", 477), ("etherRxStats", 478), ("etherRxStatsHist", 479), ("etherErrStats", 480), ("etherErrStatsHist", 481), ("etherLossStats", 482), ("etherLossStatsHist", 483), ("syntheticDirectory", 484), ("syntheticFile", 485), ("syntheticFsObj", 486), ("syntheticTime", 487), ("syntheticFileSystem", 488), ("firmwareCapProvider", 489), ("firmwareCatalogue", 490), ("firmwareUnit", 491), ("firmwareRunning", 492), ("firmwareUpdatable", 493), ("firmwareBootUnit", 494), ("firmwareBootDefinition", 495), ("firmwareImage", 496), ("firmwareInstallable", 497), ("firmwareDistImage", 498), ("firmwareDistributable", 499), ("firmwareDownloader", 500), ("firmwareCompItem", 501), ("firmwareCompSource", 502), ("firmwareCompTarget", 503), ("firmwarePack", 504), ("firmwarePackItem", 505), ("firmwareComputePack", 506), ("firmwareComputeHostPack", 507), ("firmwareComputeMgmtPack", 508), ("firmwareType", 509), ("firmwareDependency", 510), ("osInstance", 511)) + NamedValues(("osAgent", 512), ("capabilityCatalogue", 513), ("capabilityProvider", 514), ("capabilityDef", 515), ("capabilityItem", 516), ("portGroup", 517), ("portPhysSwitchIo", 518), ("portPIo", 519), ("portIntFIo", 520), ("portServerIntFIo", 521), ("portSwitchIntFIo", 522), ("portDomainEp", 523), ("policyObject", 524), ("policyHolder", 525), ("policyBinding", 526), ("policyDefinition", 527), ("orgOrg", 528), ("callhomeEp", 529), ("callhomeSource", 530), ("callhomeSmtp", 531), ("callhomePeriodicSystemInventory", 532), ("callhomeProfile", 533), ("callhomeDest", 534), ("callhomePolicy", 535), ("callhomeTestAlert", 536), ("networkEp", 537), ("networkIfEp", 538), ("networkPhysEp", 539), ("networkPIoEp", 540), ("networkCIoEp", 541), ("networkVnetEp", 542), ("networkDomainEp", 543), ("networkElement", 544), ("networkConn", 545), ("networkIfStats", 546), ("uuidpoolPool", 547), ("uuidpoolPooled", 548), ("uuidpoolBlock", 549), ("uuidpoolAddr", 550), ("uuidpoolFormat", 551), ("uuidpoolPoolable", 552), ("uuidpoolUniverse", 553), ("mgmtEntity", 554), ("mgmtBackup", 555), ("mgmtImporter", 556), ("mgmtAccessPolicy", 557), ("mgmtAccessPolicyItem", 558), ("mgmtAccessPort", 559), ("mgmtIntAuthPolicy", 560), ("mgmtController", 561), ("mgmtIf", 562), ("ippoolPool", 563), ("ippoolPooled", 564), ("ippoolBlock", 565), ("ippoolAddr", 566), ("ippoolPoolable", 567), ("ippoolUniverse", 568), ("poolUniverse", 569), ("poolElement", 570), ("poolPoolable", 571), ("poolPoolMember", 572), ("poolPool", 573), ("computeConfigPolicy", 574), ("computeInitConfigPolicy", 575), ("computeAutoconfigPolicy", 576), ("computeBladeInheritPolicy", 577), ("computeScrubPolicy", 578), ("computeDiscPolicy", 579), ("computeBladeDiscPolicy", 580), ("computeChassisDiscPolicy", 581), ("computePsuDef", 582), ("computePsuPolicy", 583), ("computePsuControl", 584), ("computePool", 585), ("computePoolable", 586), ("computePooled", 587), ("computePooledPhysical", 588), ("computePooledSlot", 589), ("computePoolingPolicy", 590), ("computeQual", 591), ("computeQualItem", 592), ("computeBladePosQual", 593), ("computeChassisQual", 594), ("computeSlotQual", 595), ("computeQualifiedPolicy", 596), ("computeContainer", 597), ("computeItem", 598), ("computePhysical", 599), ("computeLogical", 600), ("computeVirtualContainer", 601), ("computeVirtual", 602), ("computePartition", 603), ("computeBlade", 604), ("computeBoard", 605), ("computeMbPowerStats", 606), ("computeMbPowerStatsHist", 607), ("computeMbTempStats", 608), ("computeMbTempStatsHist", 609), ("lsTier", 614), ("lsServer", 615), ("lsPower", 616), ("lsComputeBinding", 617), ("lsBinding", 618), ("lsRequirement", 619), ("lsAgentPolicy", 620), ("vmEp", 621), ("vmInstance", 622), ("vmAdaptor", 623), ("vmNic", 624), ("vmHba", 625), ("vmVlan", 626), ("vmVsan", 627), ("extvmmEp", 628), ("extvmmProvider", 629), ("fcpoolInitiators", 632), ("fcpoolInitiator", 633), ("fcpoolBlock", 634), ("fcpoolFormat", 635), ("fcpoolAddr", 636), ("fcpoolPoolable", 637), ("fcpoolUniverse", 638), ("fcpoolBootTarget", 639), ("macpoolPool", 640), ("macpoolPooled", 641), ("macpoolFormat", 642), ("macpoolBlock", 643), ("macpoolAddr", 644), ("macpoolPoolable", 645), ("macpoolUniverse", 646), ("solDef", 647), ("solConfig", 648), ("solPolicy", 649), ("solIf", 650), ("dpsecMac", 651), ("qosclassDefinition", 652), ("qosclassItem", 653), ("qosclassFc", 654), ("qosclassEth", 655), ("qosclassEthBE", 656), ("qosclassEthClassified", 658), ("qosDefinition", 659), ("qosItem", 660), ("epqosDefinition", 661), ("epqosDefinitionDelTask", 662), ("epqosItem", 663), ("epqosEgress", 664), ("equipmentHwCapProvider", 665), ("equipmentBehCap", 666), ("equipmentFruCapProvider", 667), ("equipmentIntegratedComponentCapProvider", 668), ("equipmentHolderCapProvider", 669), ("equipmentSwitchCapProvider", 670), ("equipmentMgmtCapProvider", 671), ("equipmentChassisCapProvider", 672), ("equipmentBladeCapProvider", 673), ("equipmentBaseBoardCapProvider", 674), ("equipmentBladeBiosCapProvider", 675), ("equipmentLocalDiskCapProvider", 676), ("equipmentLocalDiskControllerCapProvider", 677), ("equipmentHostIfCapProvider", 678), ("equipmentProcessorUnitCapProvider", 679), ("equipmentMemoryUnitCapProvider", 680), ("equipmentIOCardCapProvider", 681), ("equipmentPsuCapProvider", 682), ("equipmentFanModuleCapProvider", 683), ("equipmentGemCapProvider", 684), ("equipmentManufacturingDef", 685), ("equipmentPhysicalDef", 686), ("equipmentServiceDef", 687), ("equipmentAdaptorDef", 688), ("equipmentProcessorUnitDef", 689), ("equipmentSlotArrayRef", 690), ("equipmentSlotArray", 691), ("equipmentItem", 692), ("equipmentStateful", 693), ("equipmentHolder", 694), ("equipmentStatefulChComp", 695), ("equipmentStatefulBladeComp", 696), ("equipmentPsu", 697), ("equipmentFanModule", 698), ("equipmentFan", 699), ("equipmentEnvSensor", 700), ("equipmentCard", 701), ("equipmentSwitchCard", 702), ("equipmentChassis", 703), ("equipmentIOCard", 704), ("equipmentLed", 705), ("equipmentIndicatorLed", 706), ("equipmentLocatorLed", 707), ("equipmentChassisStats", 708), ("equipmentChassisStatsHist", 709), ("equipmentPsuStats", 712), ("equipmentPsuStatsHist", 713), ("equipmentPsuInputStats", 714), ("equipmentPsuInputStatsHist", 715), ("equipmentFanModuleStats", 716), ("equipmentFanModuleStatsHist", 717), ("equipmentFanStats", 718), ("equipmentFanStatsHist", 719), ("flowctrlDefinition", 720), ("flowctrlItem", 721), ("aaaEpFsmTask", 722), ("aaaRealmFsmTask", 723), ("aaaUserEpFsmTask", 724), ("adaptorHostFcIfFsmTask", 725), ("callhomeEpFsmTask", 726), ("commSvcEpFsmTask", 727), ("computeBladeFsmTask", 728), ("epqosDefinitionDelTaskFsmTask", 729), ("epqosDefinitionFsmTask", 730), ("equipmentChassisFsmTask", 731), ("equipmentIOCardFsmTask", 732), ("equipmentLocatorLedFsmTask", 733), ("extvmmEpFsmTask", 734), ("fabricComputeSlotEpFsmTask", 737), ("fabricLanCloudFsmTask", 738), ("firmwareDownloaderFsmTask", 739), ("firmwareImageFsmTask", 740), ("mgmtBackupFsmTask", 741), ("mgmtControllerFsmTask", 742), ("mgmtIfFsmTask", 743), ("mgmtImporterFsmTask", 744), ("pkiEpFsmTask", 745), ("qosclassDefinitionFsmTask", 746), ("statsCollectionPolicyFsmTask", 747), ("swAccessDomainFsmTask", 748), ("swEthLanBorderFsmTask", 749), ("swFcSanBorderFsmTask", 750), ("swUtilityDomainFsmTask", 751), ("syntheticFsObjFsmTask", 752), ("sysdebugAutoCoreFileExportTargetFsmTask", 753), ("sysdebugLogControlEpFsmTask", 754), ("sysdebugManualCoreFileExportTargetFsmTask", 755), ("sysfileMutationFsmTask", 756), ("vnicProfileSetFsmTask", 757), ("vnicDefBeh", 758), ("equipmentLocalDiskDef", 759), ("sysdebugMEpLog", 762), ("adaptorExtEthIfFsmTask", 763), ("equipmentIOCardStats", 764), ("equipmentIOCardStatsHist", 765), ("adaptorHostEthIfFsmTask", 766), ("commSnmpUser", 767), ("biosBOT", 768), ("biosBootDevGrp", 769), ("biosBootDev", 770), ("etherPauseStats", 771), ("etherPauseStatsHist", 772), ("adaptorSanCap", 773), ("memoryArrayEnvStats", 774), ("memoryArrayEnvStatsHist", 775), ("memoryUnitEnvStats", 776), ("memoryUnitEnvStatsHist", 777), ("processorEnvStats", 778), ("processorEnvStatsHist", 779)) + NamedValues(("aaaExtMgmtCutThruTkn", 780), ("nwctrlDefinition", 781), ("fabricVCon", 789), ("fabricVConProfile", 790), ("vmCont", 793), ("vmDirCont", 794), ("vmDCOrg", 795), ("vmDC", 796), ("vmOrg", 797), ("vmSwitch", 798), ("vmVnicProfInst", 799), ("vmVnicProfCl", 800), ("vmVirtual", 801), ("vmHv", 802), ("extvmmMasterExtKey", 803), ("extvmmKeyInst", 804), ("extvmmKeyStore", 805), ("extvmmKeyRing", 806), ("extvmmSwitchDelTask", 807), ("biosVfIntelTurboBoostTech", 808), ("biosVfEnhancedIntelSpeedStepTech", 809), ("biosVfIntelHyperThreadingTech", 810), ("biosVfCoreMultiProcessing", 811), ("biosVfExecuteDisableBit", 812), ("biosVfIntelVirtualizationTechnology", 813), ("biosVfIntelVTForDirectedIO", 814), ("biosVfDirectCacheAccess", 817), ("biosVfSelectMemoryRASConfiguration", 818), ("biosVfNUMAOptimized", 819), ("biosVfIntelEntrySASRAIDModule", 820), ("biosVfOnboardSATAController", 822), ("biosVfSerialPortAEnable", 823), ("biosVfMaximumMemoryBelow4GB", 825), ("biosVfMemoryMappedIOAbove4GB", 826), ("biosVfFrontPanelLockout", 828), ("biosVfAssertNMIOnSERR", 830), ("biosVfAssertNMIOnPERR", 831), ("biosVfResumeOnACPowerLoss", 832), ("biosVfConsoleRedirection", 835), ("biosVfBootOptionRetry", 838), ("biosVfQuietBoot", 840), ("biosVfPOSTErrorPause", 841), ("biosVProfile", 842), ("biosVFeat", 843), ("powerAGroup", 845), ("powerABudget", 848), ("powerGroup", 849), ("powerBudget", 850), ("sysdebugMEpLogDef", 851), ("sysdebugMEpLogPolicy", 852), ("sysdebugLogBehavior", 853), ("sysdebugBackupBehavior", 854), ("bmcSELCounter", 857), ("computeBehCap", 860), ("computePciCap", 861), ("extvmmKeyStoreFsmTask", 862), ("extvmmProviderFsmTask", 863), ("extvmmSwitchDelTaskFsmTask", 864), ("biosVfUSBBootConfig", 869), ("biosVfProcessorC3Report", 870), ("biosVfProcessorC6Report", 871), ("biosVfOSBootWatchdogTimer", 873), ("biosVfOSBootWatchdogTimerPolicy", 874), ("biosVfACPI10Support", 876), ("computeMemoryUnitConstraintDef", 879), ("computePCIeFatalProtocolStats", 882), ("computePCIeFatalReceiveStats", 884), ("computePCIeFatalCompletionStats", 886), ("computePCIeFatalStats", 888), ("vmLifeCyclePolicy", 892), ("diagSrvCapProvider", 893), ("diagCtrl", 894), ("diagRslt", 895), ("diagSrvCtrl", 896), ("equipmentSwitchCap", 897), ("equipmentMemoryUnitDiscoveryModifierDef", 898), ("extvmmMasterExtKeyFsmTask", 899), ("adaptorFcInterruptProfile", 900), ("capabilityEp", 901), ("capabilityUpdater", 902), ("capabilityUpdate", 903), ("equipmentCatalogCapProvider", 904), ("capabilityUpdaterFsmTask", 905), ("firmwareDistributableFsmTask", 906), ("topMetaInf", 907), ("storageRaidBattery", 908), ("computeRtcBattery", 909), ("vmVif", 910), ("memoryBufferUnit", 912), ("memoryBufferUnitEnvStats", 913), ("memoryBufferUnitEnvStatsHist", 914), ("computeIOHub", 915), ("computeBoardController", 916), ("computeIOHubEnvStats", 917), ("computeIOHubEnvStatsHist", 918), ("diagRunPolicy", 919), ("diagTest", 920), ("diagBladeTest", 921), ("diagNetworkTest", 922), ("biosSettings", 926), ("computeDefaults", 931), ("computePlatform", 932), ("capabilityCatalogueFsmTask", 933), ("swVlanPortNs", 934), ("processorErrorStats", 935), ("biosVfSparingMode", 936), ("biosVfMirroringMode", 937), ("biosVfLvDIMMSupport", 938), ("memoryErrorStats", 940), ("commXmlClConnPolicy", 941), ("computePhysicalQual", 942), ("procSvc", 943), ("apeDcosAgManager", 944), ("apeSwitchFirmwareInv", 945), ("equipmentLocalDiskControllerDef", 946), ("equipmentBoardControllerDef", 947), ("biosARef", 948), ("biosRef", 949), ("biosFeatureRef", 950), ("biosParameterRef", 951), ("biosSettingRef", 952), ("adaptorDiagCap", 953), ("equipmentPOSTCodeContainer", 954), ("equipmentPOSTCodeTemplate", 955), ("fabricFcVsanPc", 956), ("fabricLanMonCloud", 957), ("fabricSanMonCloud", 958), ("fabricEthMonLan", 959), ("fabricFcMonSan", 960), ("fabricMon", 961), ("fabricEthMon", 962), ("fabricFcMon", 963), ("fabricMonDestEp", 964), ("fabricEthMonDestEp", 965), ("fabricFcMonDestEp", 966), ("fabricMonSrcEp", 967), ("fabricEthMonSrcEp", 968), ("fabricFcMonSrcEp", 969), ("fabricMonSrcRef", 970), ("fabricEthMonSrcRef", 971), ("fabricFcMonSrcRef", 972), ("fabricMonSrcFiltEp", 973), ("fabricEthMonFiltEp", 974), ("fabricFcMonFiltEp", 975), ("fabricMonFiltRef", 976), ("fabricEthMonFiltRef", 977), ("fabricFcMonFiltRef", 978), ("fabricFcEstcCloud", 979), ("fabricEthEstcCloud", 980), ("fabricEthVlanPortEp", 981), ("fabricVlanEp", 982), ("fabricExternalEstc", 983), ("fabricFcEstc", 984), ("fabricEthEstc", 985), ("fabricEstcEp", 986), ("fabricAFcEstcEp", 987), ("fabricFcEstcEp", 988), ("fabricAFcoeEstcEp", 989), ("fabricFcoeEstcEp", 990), ("fabricEthEstcEp", 991), ("fabricTargetEp", 992), ("fabricEthTargetEp", 993), ("processorUnitAssocCtx", 994), ("biosVfUEFIOSUseLegacyVideo", 998), ("vnicIpV4AddrConf", 999), ("vnicIpV4AddrExplConf", 1000), ("vnicIpV4ProfDerivedAddr", 1001), ("storageDevice", 1002), ("storageDrive", 1003), ("aaaConfig", 1004), ("aaaAuthMethod", 1005), ("aaaDefaultAuth", 1006), ("aaaConsoleAuth", 1007), ("aaaDomainAuth", 1008), ("aaaDomain", 1009), ("aaaLdapGroupRule", 1010), ("aaaUserGroup", 1011), ("aaaLdapGroup", 1012), ("aaaProviderGroup", 1013), ("aaaProviderRef", 1014), ("adaptorHwAddrCap", 1015), ("adaptorUplinkHwAddrCap", 1016), ("adaptorHostethHwAddrCap", 1017), ("adaptorHostfcHwAddrCap", 1018), ("adaptorUnitAssocCtx", 1019), ("sysdebugTechSupFileRepository", 1020), ("sysdebugTechSupport", 1021), ("sysdebugTechSupportCmdOpt", 1022), ("powerEp", 1023), ("powerPrioWght", 1024), ("powerPolicy", 1025), ("powerPlacement", 1026), ("powerGroupAdditionPolicy", 1027), ("powerGroupMember", 1028), ("powerChassisMember", 1029), ("powerRackUnitMember", 1030), ("powerGroupQual", 1031), ("powerMgmtPolicy", 1032), ("powerGroupStats", 1033), ("powerGroupStatsHist", 1034), ("swMonSrcEp", 1035), ("swEthMonSrcEp", 1036), ("swFcMonSrcEp", 1037), ("swEstcEp", 1038), ("swFcEstcEp", 1039), ("swEthEstcEp", 1040), ("swTargetEp", 1041), ("swEthTargetEp", 1042), ("swFcoeEstcEp", 1043), ("swMonDomain", 1044), ("swLanMon", 1045), ("swSanMon", 1046), ("swEthLanMon", 1047), ("swFcSanMon", 1048), ("swMon", 1049), ("swEthMon", 1050), ("swFcMon", 1051), ("swMonDestEp", 1052), ("swEthMonDestEp", 1053), ("swFcMonDestEp", 1054), ("swSanPc", 1055), ("swFcSanPc", 1056), ("capabilityMgmtExtension", 1057), ("pciCard", 1058), ("pciUnit", 1059), ("licenseEp", 1060), ("licenseFeature", 1061), ("licenseServerHostId", 1062), ("licenseFile", 1063), ("licenseSource", 1064), ("licenseContents", 1065), ("licenseFeatureLine", 1066), ("licenseInstance", 1067), ("licenseSourceFile", 1068), ("licenseProp", 1069), ("licenseDownloader", 1070), ("licenseCapProvider", 1071), ("licenseFeatureCapProvider", 1072), ("portTrustMode", 1073), ("computePoolPolicyRef", 1074), ("computePooledRackUnit", 1075), ("computePhysicalAssocCtx", 1076), ("computeComputeDiscPolicy", 1077), ("computeServerDiscPolicy", 1078), ("computeRackUnit", 1079), ("lsServerAssocCtx", 1080), ("lsmaintMaintPolicy", 1081), ("lsmaintAck", 1082), ("equipmentPicture", 1083), ("equipmentMgmtExtCapProvider", 1084), ("equipmentRackUnitCapProvider", 1085), ("equipmentBladeAGLibrary", 1086), ("equipmentFexCapProvider", 1087), ("equipmentPciDef", 1088), ("equipmentRaidDef", 1089)) + NamedValues(("equipmentPortGroupDef", 1090), ("equipmentAssocCtx", 1091), ("equipmentFexEnvStats", 1092), ("equipmentFexEnvStatsHist", 1093), ("equipmentFexPowerSummary", 1094), ("equipmentFexPowerSummaryHist", 1095), ("equipmentFexPsuInputStats", 1096), ("equipmentFexPsuInputStatsHist", 1097), ("equipmentRackUnitPsuStats", 1098), ("equipmentRackUnitPsuStatsHist", 1099), ("equipmentRackUnitFanStats", 1100), ("equipmentRackUnitFanStatsHist", 1101), ("equipmentFex", 1102), ("dhcpInst", 1103), ("dhcpLease", 1104), ("dhcpAcquired", 1105), ("trigInst", 1106), ("trigWindow", 1107), ("trigSched", 1108), ("trigSchedWindow", 1109), ("trigAbsWindow", 1110), ("trigRecurrWindow", 1111), ("trigMeta", 1112), ("trigTriggered", 1113), ("trigTriggerable", 1114), ("trigTest", 1115), ("trigAck", 1116), ("trigConfAck", 1117), ("trigResAck", 1118), ("capabilityMgmtExtensionFsmTask", 1119), ("computePhysicalFsmTask", 1120), ("computeRackUnitFsmTask", 1121), ("equipmentFexFsmTask", 1122), ("fabricSanCloudFsmTask", 1124), ("licenseDownloaderFsmTask", 1125), ("licenseFileFsmTask", 1126), ("licenseInstanceFsmTask", 1127), ("lsServerFsmTask", 1128), ("swEthMonFsmTask", 1129), ("swFcMonFsmTask", 1130), ("sysdebugTechSupportFsmTask", 1131), ("fabricBHVlan", 1132), ("imgprovPolicy", 1133), ("imgprovTarget", 1134), ("imgsecPolicy", 1135), ("imgsecKey", 1136), ("hostimgPolicy", 1137), ("hostimgTarget", 1138), ("equipmentGemPortCap", 1143), ("equipmentXcvr", 1144), ("portPIoFsmTask", 1145), ("vnicBootIpPolicy", 1146), ("adaptorLldpCap", 1147), ("lldpAcquired", 1148), ("extmgmtIf", 1149), ("extmgmtIfMonPolicy", 1150), ("extmgmtMiiStatus", 1151), ("extmgmtGatewayPing", 1152), ("extmgmtArpTargets", 1153), ("biosVfOptionROMLoad", 1154), ("firmwareBundleTypeCapProvider", 1155), ("firmwareBundleType", 1156), ("storageEnclosure", 1157), ("sysdebugCoreFsmTask", 1158), ("fabricAEthEstcEp", 1159), ("fabricEstcPc", 1160), ("fabricEthEstcPc", 1161), ("fabricEthEstcPcEp", 1162), ("fabricEthVlanPc", 1163), ("swEthEstcPc", 1164), ("commSyslogSource", 1165), ("firmwareSpec", 1166), ("computeRackUnitMbTempStats", 1167), ("computeRackUnitMbTempStatsHist", 1168), ("storageLocalDiskSlotEp", 1169), ("computeRackPosQual", 1170), ("computeRackQual", 1171), ("biosVfCPUPerformance", 1172), ("fabricFcoeVsanPortEp", 1173), ("pciEquipSlot", 1174), ("equipmentDbgPluginCapProvider", 1175), ("commSvcLimits", 1176), ("commShellSvcLimits", 1177), ("commWebSvcLimits", 1178), ("adaptorFruCapRef", 1179), ("biosVfMaxVariableMTRRSetting", 1180), ("biosVfUSBSystemIdlePowerOptimizingSetting", 1181), ("biosVfUSBFrontPanelAccessLock", 1182), ("biosVfUCSMBootOrderRuleControl", 1183), ("equipmentLocalDiskControllerCapRef", 1184), ("equipmentDiscoveryCap", 1185), ("topSysDefaults", 1186), ("iqnpoolPool", 1187), ("iqnpoolPooled", 1188), ("iqnpoolBlock", 1189), ("iqnpoolAddr", 1190), ("iqnpoolFormat", 1191), ("iqnpoolPoolable", 1192), ("iqnpoolUniverse", 1193), ("fabricSwSrvPc", 1194), ("fabricDceSwSrvPc", 1195), ("fabricDceSwSrvPcEp", 1196), ("fabricEpMgr", 1197), ("biosVfProcessorCState", 1198), ("biosVfProcessorC1E", 1199), ("biosVIdentityParams", 1200), ("vnicIPv4IscsiAddr", 1201), ("vnicIPv4PooledIscsiAddr", 1202), ("vnicVProfileAlias", 1203), ("vnicOProfileAlias", 1204), ("vnicInternalProfile", 1205), ("vnicVlan", 1206), ("vnicIScsiNode", 1207), ("vnicIScsi", 1208), ("vnicIScsiTargetIf", 1209), ("vnicIScsiStaticTargetIf", 1210), ("vnicLun", 1211), ("vnicIScsiAutoTargetIf", 1212), ("lsbootIScsi", 1213), ("lsbootIScsiImagePath", 1214), ("aaaBanner", 1215), ("aaaPreLoginBanner", 1216), ("aaaPwdProfile", 1217), ("aaaUserData", 1218), ("adaptorIScsiCap", 1219), ("adaptorHostIscsiIfProfile", 1220), ("adaptorProtocolProfile", 1221), ("adaptorCIoEp", 1222), ("adaptorExternalPc", 1223), ("adaptorExtIfPc", 1224), ("adaptorExtEthIfPc", 1225), ("adaptorPIoEp", 1226), ("adaptorExternalEp", 1227), ("adaptorExtIfEp", 1228), ("adaptorExtEthIfPcEp", 1229), ("adaptorHostIscsiIf", 1230), ("adaptorIscsiTargetIf", 1231), ("adaptorIscsiProt", 1232), ("adaptorIscsiAuth", 1233), ("swPhys", 1234), ("swPhysEtherEp", 1235), ("swPhysFcEp", 1236), ("swVlanPortNsOverride", 1237), ("etherPortChanIdElem", 1238), ("etherPortChanIdUniverse", 1239), ("etherCIoEp", 1240), ("etherPc", 1241), ("etherInternalPc", 1242), ("etherExternalPc", 1243), ("etherServerIntFIoPc", 1244), ("etherSwitchIntFIoPc", 1245), ("etherPIoEp", 1246), ("etherExternalEp", 1247), ("etherIntFIoEp", 1248), ("etherServerIntFIoPcEp", 1249), ("etherSwitchIntFIoPcEp", 1250), ("mgmtPmonEntry", 1251), ("iscsiAuthProfile", 1252), ("iscsiProtocolProfile", 1253), ("computeAChassisDiscPolicy", 1254), ("computeChassisConnPolicy", 1255), ("vmClientContainer", 1256), ("vmComputeEp", 1257), ("extvmmSwitchSet", 1258), ("equipmentUnifiedPortCapProvider", 1259), ("equipmentBeaconCapProvider", 1260), ("equipmentHDDFaultMonDef", 1261), ("equipmentFanModuleDef", 1262), ("equipmentPsuDef", 1263), ("equipmentPortGroupAggregationDef", 1264), ("equipmentPortGroupSwComplexDef", 1265), ("equipmentPortSwComplexRef", 1266), ("equipmentBeaconLed", 1267), ("equipmentPsuOutputStats", 1268), ("equipmentPsuOutputStatsHist", 1269), ("equipmentNetworkElementFanStats", 1270), ("equipmentNetworkElementFanStatsHist", 1271), ("equipmentBeaconLedFsmTask", 1272), ("fabricEpMgrFsmTask", 1273), ("swPhysFsmTask", 1274), ("vmLifeCyclePolicyFsmTask", 1275), ("firmwareUpgradeConstraint", 1276), ("adaptorFamilyTypeDef", 1277), ("adaptorUnitExtn", 1278), ("biosVfProcessorC7Report", 1279), ("biosVfOptionROMEnable", 1280), ("biosVfPCISlotOptionROMEnable", 1281), ("biosVfPackageCStateLimit", 1282), ("lsVersionBeh", 1287), ("equipmentBiosDef", 1288), ("equipmentDimmMapping", 1289), ("equipmentDimmEntry", 1290), ("equipmentBladeConnDef", 1291), ("equipmentAdaptorConnDef", 1292), ("equipmentIOCardTypeDef", 1293), ("computePnuOSImage", 1294), ("etherServerIntFIoFsmTask", 1295), ("equipmentServerFeatureCap", 1296), ("equipmentBladeIOMConnDef", 1297), ("biosVfOnboardStorage", 1298), ("biosVfOSBootWatchdogTimerTimeout", 1299), ("fsmFsm", 1300), ("fsmStage", 1301), ("faultBaseHolder", 1302), ("faultLocalTypedHolder", 1303), ("faultBasePolicy", 1304), ("faultExtPolicy", 1305), ("faultSuppressPolicy", 1306), ("faultSuppressPolicyItem", 1307), ("faultSuppressTask", 1308), ("faultAffectedClass", 1309), ("apePaloVnic", 1310), ("apeVnicStats", 1311), ("apePaloVnicStats", 1312), ("vnicFcGroupTempl", 1313), ("vnicSanConnPolicy", 1314), ("vnicLanConnPolicy", 1315), ("vnicAGroup", 1316), ("vnicFcGroupDef", 1317), ("vnicIScsiBase", 1318), ("vnicIScsiLCP", 1319), ("vnicDynamicConPolicyRef", 1320), ("vnicConnDef", 1321), ("vnicABeh", 1322), ("vnicVnicBehPolicy", 1323), ("vnicVhbaBehPolicy", 1324), ("biosVfSriovConfig", 1325), ("fabricVnetPermit", 1326), ("fabricVlanPermit", 1327), ("fabricMulticastPolicy", 1328), ("storageIniGroup", 1329), ("storageInitiator", 1330), ("storageADef", 1331), ("storageConnectionPolicy", 1332), ("policyItem", 1333), ("fsmStatus", 1334), ("swVlanGroup", 1335), ("swVlanRef", 1336), ("swFcoeSanEp", 1337), ("swFcoeSanPc", 1338), ("swFcZoneSet", 1339), ("swFcServerZoneGroup", 1340), ("swZoneInitiatorMember", 1341), ("swFcZone", 1342), ("swFcZoneMember", 1343), ("swZoneTargetMember", 1344), ("swFabricZoneNs", 1345), ("swFabricZoneNsOverride", 1346), ("swCardEnvStats", 1347), ("swCardEnvStatsHist", 1348), ("etherPIoEndPoint", 1349), ("etherFcoeInterfaceStats", 1350), ("etherFcoeInterfaceStatsHist", 1351), ("mgmtExportPolicy", 1352), ("mgmtCfgExportPolicy", 1353)) + NamedValues(("mgmtBackupPolicy", 1354), ("mgmtConnection", 1355), ("commClientItem", 1356), ("aaaItem", 1357), ("commItem", 1358), ("vnicRackServerDiscoveryProfile", 1359), ("vnicIScsiBootParams", 1360), ("vnicIScsiBootVnic", 1361), ("sysfileDigest", 1362), ("versionEp", 1363), ("versionVersion", 1364), ("versionApplication", 1365), ("fcpoolInitiatorEp", 1366), ("lsFcLocale", 1367), ("lsFcZoneGroup", 1368), ("lsZoneInitiatorMember", 1369), ("lsFcZone", 1370), ("lsFcZoneMember", 1371), ("lsZoneTargetMember", 1372), ("lsVConAssign", 1373), ("policyPolicyEp", 1374), ("policyPolicyScopeCont", 1375), ("policyPolicyScopeContext", 1376), ("policyPolicyScope", 1377), ("policyPolicyRequestor", 1378), ("policyDigest", 1379), ("policyControlEp", 1380), ("policyControl", 1381), ("policyDateTime", 1382), ("policyCommunication", 1383), ("policyDns", 1384), ("policySecurity", 1385), ("policyMonitoring", 1386), ("policyFault", 1387), ("policyInfraFirmware", 1388), ("policyConfigBackup", 1389), ("policyMEp", 1390), ("policyDiscovery", 1391), ("policyPowerMgmt", 1392), ("policyPsu", 1393), ("policyControlled", 1394), ("policyControlledInstance", 1395), ("policyControlledType", 1396), ("computeServerMgmtPolicy", 1397), ("nfsEp", 1398), ("nfsMountDef", 1399), ("nfsMountInst", 1400), ("trigToken", 1401), ("trigClientToken", 1402), ("trigBaseSched", 1403), ("trigLocalSched", 1404), ("trigBaseAbsWindow", 1405), ("trigLocalAbsWindow", 1406), ("capabilityFeatureLimits", 1407), ("capabilitySystemLimits", 1408), ("capabilityNetworkLimits", 1409), ("capabilityStorageLimits", 1410), ("identIdentCtx", 1411), ("identSysInfo", 1412), ("identMetaVerse", 1413), ("identMetaSystem", 1414), ("identIdentRequest", 1415), ("identRequestEp", 1416), ("fabricLanAccessMgr", 1417), ("fabricZoneIdUniverse", 1418), ("fabricAFcoeSanEp", 1419), ("fabricFcoeSanEp", 1420), ("fabricFcoeSanPcEp", 1421), ("fabricFcoeSanPc", 1422), ("fabricFcoeVsanPc", 1423), ("fabricNetGroup", 1424), ("fabricPooledVlan", 1425), ("fabricPoolableVlan", 1426), ("fabricVsanMembership", 1427), ("fabricVnetReq", 1428), ("fabricVlanReq", 1429), ("fabricVnetGroupReq", 1430), ("fabricVlanGroupReq", 1431), ("fabricOrgVlanPolicy", 1432), ("observeObservedCont", 1433), ("observeObserved", 1434), ("observeFilter", 1435), ("configSorter", 1436), ("extpolConnectorContainer", 1437), ("extpolEp", 1438), ("extpolConnector", 1439), ("extpolSvc", 1440), ("extpolRegistry", 1441), ("extpolProviderCont", 1442), ("extpolProvider", 1443), ("extpolControllerCont", 1444), ("extpolController", 1445), ("extpolClientCont", 1446), ("extpolClient", 1447), ("extpolSystemContext", 1448), ("callhomeItem", 1449), ("firmwareBundleInfo", 1450), ("firmwareInfraPack", 1451), ("firmwareCatalogPack", 1452), ("firmwareSystem", 1453), ("firmwareInfra", 1454), ("firmwareHost", 1455), ("firmwareBlade", 1456), ("firmwareRack", 1457), ("firmwareStatus", 1458), ("firmwareSystemCompCheckResult", 1459), ("firmwareInstallImpact", 1460), ("firmwareHostPackModImpact", 1461), ("firmwareAck", 1462), ("firmwareUpgradeInfo", 1463), ("firmwareUpgradeDetail", 1464), ("firmwareBundleInfoDigest", 1465), ("storageDomainEp", 1466), ("storageVirtualDrive", 1467), ("storageConnectionDef", 1468), ("storageTarget", 1469), ("storageFcTargetEp", 1470), ("storageVsanRef", 1471), ("initiatorEp", 1472), ("initiatorRequestorEp", 1473), ("initiatorGroupEp", 1474), ("initiatorInitiatorEp", 1475), ("initiatorIScsiInitiatorEp", 1476), ("initiatorFcInitiatorEp", 1477), ("initiatorStoreEp", 1478), ("initiatorUnitEp", 1479), ("initiatorLunEp", 1480), ("initiatorRequestorGrpEp", 1481), ("initiatorMemberEp", 1482), ("storageEp", 1483), ("storageNodeEp", 1484), ("storageEpUser", 1485), ("storageAuthKey", 1486), ("storageTransportIf", 1487), ("storageTargetIf", 1488), ("storageIScsiTargetIf", 1489), ("storageFcTargetIf", 1490), ("storageL2If", 1491), ("storageFcIf", 1492), ("storageEtherIf", 1493), ("storageSystem", 1494), ("ipIpV4Addr", 1495), ("ipIPv4Dns", 1496), ("ipServiceIf", 1497), ("ipIpV4StaticAddr", 1498), ("computeServerDiscPolicyFsmTask", 1499), ("extpolEpFsmTask", 1500), ("extpolRegistryFsmTask", 1501), ("firmwareSystemFsmTask", 1502), ("identIdentRequestFsmTask", 1503), ("identMetaSystemFsmTask", 1504), ("mgmtExportPolicyFsmTask", 1505), ("nfsMountDefFsmTask", 1506), ("nfsMountInstFsmTask", 1507), ("observeObservedFsmTask", 1508), ("policyControlEpFsmTask", 1509), ("policyPolicyScopeFsmTask", 1510), ("storageSystemFsmTask", 1511), ("aaaEpFsm", 1512), ("aaaEpFsmStage", 1513), ("aaaLdapEpFsm", 1514), ("aaaLdapEpFsmStage", 1515), ("aaaRadiusEpFsm", 1516), ("aaaRadiusEpFsmStage", 1517), ("aaaTacacsPlusEpFsm", 1518), ("aaaTacacsPlusEpFsmStage", 1519), ("aaaRealmFsm", 1520), ("aaaRealmFsmStage", 1521), ("aaaAuthRealmFsm", 1522), ("aaaAuthRealmFsmStage", 1523), ("aaaUserEpFsm", 1524), ("aaaUserEpFsmStage", 1525), ("adaptorExtEthIfFsm", 1526), ("adaptorExtEthIfFsmStage", 1527), ("adaptorHostEthIfFsm", 1528), ("adaptorHostEthIfFsmStage", 1529), ("adaptorHostFcIfFsm", 1530), ("adaptorHostFcIfFsmStage", 1531), ("callhomeEpFsm", 1532), ("callhomeEpFsmStage", 1533), ("capabilityCatalogueFsm", 1534), ("capabilityCatalogueFsmStage", 1535), ("capabilityMgmtExtensionFsm", 1536), ("capabilityMgmtExtensionFsmStage", 1537), ("capabilityUpdaterFsm", 1538), ("capabilityUpdaterFsmStage", 1539), ("commSvcEpFsm", 1540), ("commSvcEpFsmStage", 1541), ("computeBladeFsm", 1542), ("computeBladeFsmStage", 1543), ("computePhysicalFsm", 1544), ("computePhysicalFsmStage", 1545), ("computeRackUnitFsm", 1546), ("computeRackUnitFsmStage", 1547), ("computeServerDiscPolicyFsm", 1548), ("computeServerDiscPolicyFsmStage", 1549), ("epqosDefinitionDelTaskFsm", 1550), ("epqosDefinitionDelTaskFsmStage", 1551), ("epqosDefinitionFsm", 1552), ("epqosDefinitionFsmStage", 1553), ("equipmentBeaconLedFsm", 1554), ("equipmentBeaconLedFsmStage", 1555), ("equipmentChassisFsm", 1556), ("equipmentChassisFsmStage", 1557), ("equipmentFexFsm", 1558), ("equipmentFexFsmStage", 1559), ("equipmentIOCardFsm", 1560), ("equipmentIOCardFsmStage", 1561), ("equipmentLocatorLedFsm", 1562), ("equipmentLocatorLedFsmStage", 1563), ("etherServerIntFIoFsm", 1564), ("etherServerIntFIoFsmStage", 1565), ("extpolEpFsm", 1566), ("extpolEpFsmStage", 1567), ("extpolRegistryFsm", 1568), ("extpolRegistryFsmStage", 1569), ("extvmmEpFsm", 1570), ("extvmmEpFsmStage", 1571), ("extvmmKeyStoreFsm", 1572), ("extvmmKeyStoreFsmStage", 1573), ("extvmmMasterExtKeyFsm", 1574), ("extvmmMasterExtKeyFsmStage", 1575), ("extvmmProviderFsm", 1576), ("extvmmProviderFsmStage", 1577), ("extvmmSwitchDelTaskFsm", 1578), ("extvmmSwitchDelTaskFsmStage", 1579), ("fabricComputeSlotEpFsm", 1580), ("fabricComputeSlotEpFsmStage", 1581), ("fabricEpMgrFsm", 1582), ("fabricEpMgrFsmStage", 1583), ("fabricLanCloudFsm", 1584), ("fabricLanCloudFsmStage", 1585), ("fabricSanCloudFsm", 1586), ("fabricSanCloudFsmStage", 1587), ("firmwareDistributableFsm", 1588), ("firmwareDistributableFsmStage", 1589), ("firmwareDownloaderFsm", 1590), ("firmwareDownloaderFsmStage", 1591), ("firmwareImageFsm", 1592), ("firmwareImageFsmStage", 1593), ("firmwareSystemFsm", 1594), ("firmwareSystemFsmStage", 1595), ("identIdentRequestFsm", 1596), ("identIdentRequestFsmStage", 1597), ("identMetaSystemFsm", 1598), ("identMetaSystemFsmStage", 1599), ("licenseDownloaderFsm", 1600), ("licenseDownloaderFsmStage", 1601), ("licenseFileFsm", 1602), ("licenseFileFsmStage", 1603), ("licenseInstanceFsm", 1604), ("licenseInstanceFsmStage", 1605), ("lsServerFsm", 1606), ("lsServerFsmStage", 1607), ("mgmtBackupFsm", 1608)) + NamedValues(("mgmtBackupFsmStage", 1609), ("mgmtControllerFsm", 1610), ("mgmtControllerFsmStage", 1611), ("mgmtExportPolicyFsm", 1612), ("mgmtExportPolicyFsmStage", 1613), ("mgmtBackupPolicyFsm", 1614), ("mgmtBackupPolicyFsmStage", 1615), ("mgmtCfgExportPolicyFsm", 1616), ("mgmtCfgExportPolicyFsmStage", 1617), ("mgmtIfFsm", 1618), ("mgmtIfFsmStage", 1619), ("mgmtImporterFsm", 1620), ("mgmtImporterFsmStage", 1621), ("nfsMountDefFsm", 1622), ("nfsMountDefFsmStage", 1623), ("nfsMountInstFsm", 1624), ("nfsMountInstFsmStage", 1625), ("observeObservedFsm", 1626), ("observeObservedFsmStage", 1627), ("pkiEpFsm", 1628), ("pkiEpFsmStage", 1629), ("policyControlEpFsm", 1630), ("policyControlEpFsmStage", 1631), ("policyPolicyScopeFsm", 1632), ("policyPolicyScopeFsmStage", 1633), ("portPIoFsm", 1634), ("portPIoFsmStage", 1635), ("etherPIoFsm", 1636), ("etherPIoFsmStage", 1637), ("fcPIoFsm", 1638), ("fcPIoFsmStage", 1639), ("qosclassDefinitionFsm", 1640), ("qosclassDefinitionFsmStage", 1641), ("statsCollectionPolicyFsm", 1642), ("statsCollectionPolicyFsmStage", 1643), ("storageSystemFsm", 1644), ("storageSystemFsmStage", 1645), ("swAccessDomainFsm", 1646), ("swAccessDomainFsmStage", 1647), ("swEthLanBorderFsm", 1648), ("swEthLanBorderFsmStage", 1649), ("swEthMonFsm", 1650), ("swEthMonFsmStage", 1651), ("swFcMonFsm", 1652), ("swFcMonFsmStage", 1653), ("swFcSanBorderFsm", 1654), ("swFcSanBorderFsmStage", 1655), ("swPhysFsm", 1656), ("swPhysFsmStage", 1657), ("swUtilityDomainFsm", 1658), ("swUtilityDomainFsmStage", 1659), ("syntheticFsObjFsm", 1660), ("syntheticFsObjFsmStage", 1661), ("sysdebugAutoCoreFileExportTargetFsm", 1662), ("sysdebugAutoCoreFileExportTargetFsmStage", 1663), ("sysdebugCoreFsm", 1664), ("sysdebugCoreFsmStage", 1665), ("sysdebugLogControlEpFsm", 1666), ("sysdebugLogControlEpFsmStage", 1667), ("sysdebugManualCoreFileExportTargetFsm", 1668), ("sysdebugManualCoreFileExportTargetFsmStage", 1669), ("sysdebugTechSupportFsm", 1670), ("sysdebugTechSupportFsmStage", 1671), ("sysfileMutationFsm", 1672), ("sysfileMutationFsmStage", 1673), ("vmLifeCyclePolicyFsm", 1674), ("vmLifeCyclePolicyFsmStage", 1675), ("vnicProfileSetFsm", 1676), ("vnicProfileSetFsmStage", 1677), ("gmetaEp", 1681), ("gmetaHolder", 1682), ("gmetaClass", 1683), ("gmetaProp", 1684), ("gmetaPolicyMapHolder", 1685), ("configImpact", 1686), ("changeChangedObjectRef", 1688), ("aaaCimcSession", 1689), ("aaaSessionInfoTable", 1690), ("aaaSessionInfo", 1691), ("fabricVnetEpSyncEp", 1692), ("fabricChangedObjectRef", 1693), ("gmetaPolicyMapElement", 1694), ("biosVfDramRefreshRate", 1695), ("configImpactResponse", 1696), ("configManagedEpImpactResponse", 1697), ("computeHealthLedSensorAlarm", 1698), ("equipmentHealthLed", 1699), ("equipmentRackFanModuleDef", 1700), ("equipmentFirmwareConstraint", 1701), ("equipmentVersionConstraint", 1702), ("networkOperLevel", 1703), ("orgSourceMask", 1704), ("storageTransportableFlashModule", 1705), ("policyLocalMap", 1706), ("policyElement", 1707), ("policyCentraleSync", 1708), ("fabricVnetEpSyncEpFsmTask", 1709), ("gmetaHolderFsmTask", 1710), ("fabricVnetEpSyncEpFsm", 1711), ("fabricVnetEpSyncEpFsmStage", 1712), ("gmetaHolderFsm", 1713), ("gmetaHolderFsmStage", 1714))

class CucsNetworkConnectionType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsNetworkElementOperability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("operable", 1), ("inoperable", 2))

class CucsNetworkIfStatsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("generic", 0), ("broadcast", 1), ("multicast", 2), ("unicast", 3), ("total", 4))

class CucsNetworkIfStatsUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("raw", 0), ("packets", 1), ("octets", 2))

class CucsNetworkIfStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("down", 1), ("up", 2))

class CucsNetworkInventoryStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("switchFru", 0), ("vlanPortCount", 1), ("cardInventory", 2), ("ethPortInventory", 3), ("fcPortInventory", 4), ("mgmtPortInventory", 5), ("ethPcInventory", 6), ("fcPcInventory", 7), ("switchInventory", 8), ("xcvrInventory", 9), ("remoteEthPortInventory", 10), ("vlanCompGrpInventory", 11))

class CucsNetworkLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsNetworkOperLevelNumPrimaryVlansStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("withinLimit", 0), ("aboveLimit", 1))

class CucsNetworkPhysEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsNetworkPortOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("indeterminate", 0), ("up", 1), ("adminDown", 2), ("linkDown", 3), ("failed", 4), ("noLicense", 5), ("linkUp", 6), ("hardwareFailure", 7), ("softwareFailure", 8), ("errorDisabled", 9), ("sfpNotPresent", 10))

class CucsNetworkPortRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsNetworkPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsNetworkSide(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("left", 0), ("right", 1))

class CucsNetworkSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2))

class CucsNetworkTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsNetworkVnetEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsNfsClientConfigState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unregistered", 0), ("registered", 1), ("configured", 2), ("failed", 3))

class CucsNfsDefAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1), ("suspended", 2))

class CucsNfsMntAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("unmount", 1), ("mount", 2), ("remount", 3))

class CucsNfsMntOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unmounted", 0), ("mounted", 1))

class CucsNfsMountDefFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1241))
    namedValues = NamedValues(("nop", 0), ("reportNfsMountSuspend", 1241))

class CucsNfsMountDefFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1241, 1242, 1415, 1416))
    namedValues = NamedValues(("nop", 0), ("reportNfsMountSuspendBegin", 1241), ("reportNfsMountSuspendReport", 1242), ("reportNfsMountSuspendFail", 1415), ("reportNfsMountSuspendSuccess", 1416))

class CucsNfsMountDefFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1241))
    namedValues = NamedValues(("nop", 0), ("reportNfsMountSuspend", 1241))

class CucsNfsMountInstFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1233, 1238))
    namedValues = NamedValues(("nop", 0), ("mount", 1233), ("unmount", 1238))

class CucsNfsMountInstFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1417, 1418, 1419, 1420))
    namedValues = NamedValues(("nop", 0), ("mountBegin", 1233), ("mountRegisterClient", 1234), ("mountVerifyRegistration", 1235), ("mountMountLocal", 1236), ("mountMountPeer", 1237), ("unmountBegin", 1238), ("unmountUnmountLocal", 1239), ("unmountUnmountPeer", 1240), ("mountFail", 1417), ("mountSuccess", 1418), ("unmountFail", 1419), ("unmountSuccess", 1420))

class CucsNfsMountInstFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1233, 1238))
    namedValues = NamedValues(("nop", 0), ("mount", 1233), ("unmount", 1238))

class CucsNfsPurpose(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("image", 0), ("backup", 1))

class CucsNwctrlAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsNwctrlLinkFailAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("linkDown", 0), ("warning", 1))

class CucsNwctrlRegistrationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("onlyNativeVlan", 0), ("allHostVlans", 1))

class CucsObserveObservedFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1341, 1343, 1345, 1347))
    namedValues = NamedValues(("nop", 0), ("resolvePolicyFsm", 1341), ("resolveResourceFsm", 1343), ("resolveVMFsm", 1345), ("resolveControllerFsm", 1347))

class CucsObserveObservedFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428))
    namedValues = NamedValues(("nop", 0), ("resolvePolicyFsmBegin", 1341), ("resolvePolicyFsmExecute", 1342), ("resolveResourceFsmBegin", 1343), ("resolveResourceFsmExecute", 1344), ("resolveVMFsmBegin", 1345), ("resolveVMFsmExecute", 1346), ("resolveControllerFsmBegin", 1347), ("resolveControllerFsmExecute", 1348), ("resolveControllerFsmFail", 1421), ("resolveControllerFsmSuccess", 1422), ("resolvePolicyFsmFail", 1423), ("resolvePolicyFsmSuccess", 1424), ("resolveResourceFsmFail", 1425), ("resolveResourceFsmSuccess", 1426), ("resolveVMFsmFail", 1427), ("resolveVMFsmSuccess", 1428))

class CucsObserveObservedFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1341, 1343, 1345, 1347))
    namedValues = NamedValues(("nop", 0), ("resolvePolicyFsm", 1341), ("resolveResourceFsm", 1343), ("resolveVMFsm", 1345), ("resolveControllerFsm", 1347))

class CucsOrgLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("root", 0), ("n1", 1), ("n2", 2), ("n3", 3), ("n4", 4), ("n5", 5))

class CucsOrgSrcMask(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("local", 0), ("global", 1))

class CucsOsOsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unspecified", 0), ("pnuOS", 1), ("linux", 2), ("windows", 3), ("solaris", 4), ("vmwareESX", 5))

class CucsPciEquipSlotId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 5000)

class CucsPkiCertStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("valid", 0), ("expired", 1), ("revoked", 2), ("notYetValid", 3), ("emptyCert", 4), ("unknown", 5), ("failedToVerifyWithTp", 6), ("failedToVerifyWithPrivateKey", 7), ("certChainTooLong", 8))

class CucsPkiEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 206))
    namedValues = NamedValues(("nop", 0), ("updateEp", 206))

class CucsPkiEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 206, 207, 208, 428, 429))
    namedValues = NamedValues(("nop", 0), ("updateEpBegin", 206), ("updateEpSetKeyRingLocal", 207), ("updateEpSetKeyRingPeer", 208), ("updateEpFail", 428), ("updateEpSuccess", 429))

class CucsPkiEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 206))
    namedValues = NamedValues(("nop", 0), ("updateEp", 206))

class CucsPkiKeyringState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("started", 1), ("created", 2), ("reqCreated", 3), ("tpSet", 4), ("completed", 5))

class CucsPkiModulus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 512, 1024, 1536, 2048, 2560, 3072, 3584, 4096))
    namedValues = NamedValues(("modinvalid", 0), ("mod512", 512), ("mod1024", 1024), ("mod1536", 1536), ("mod2048", 2048), ("mod2560", 2560), ("mod3072", 3072), ("mod3584", 3584), ("mod4096", 4096))

class CucsPolicyControlSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("local", 0), ("policy", 1), ("pendingPolicy", 2))

class CucsPolicyControlEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1199))
    namedValues = NamedValues(("nop", 0), ("operate", 1199))

class CucsPolicyControlEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1199, 1200, 1429, 1430))
    namedValues = NamedValues(("nop", 0), ("operateBegin", 1199), ("operateResolve", 1200), ("operateFail", 1429), ("operateSuccess", 1430))

class CucsPolicyControlEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1199))
    namedValues = NamedValues(("nop", 0), ("operate", 1199))

class CucsPolicyControlEpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("policy", 0))

class CucsPolicyPolicyOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ok", 0), ("resolved", 1), ("released", 2))

class CucsPolicyPolicyOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("local", 0), ("policy", 1), ("pendingPolicy", 2))

class CucsPolicyPolicyResolveType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("name", 0), ("rn", 1))

class CucsPolicyPolicyScopeFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1201, 1203, 1205, 1207, 1209, 1211, 1213, 1215, 1217, 1219, 1221, 1223, 1225, 1227, 1229))
    namedValues = NamedValues(("nop", 0), ("releasePolicyFsm", 1201), ("releaseOperationFsm", 1203), ("releaseStorageFsm", 1205), ("resolveManyPolicyFsm", 1207), ("resolveManyOperationFsm", 1209), ("resolveManyStorageFsm", 1211), ("releaseManyPolicyFsm", 1213), ("releaseManyOperationFsm", 1215), ("releaseManyStorageFsm", 1217), ("resolveAllPolicyFsm", 1219), ("resolveAllOperationFsm", 1221), ("resolveAllStorageFsm", 1223), ("releaseAllPolicyFsm", 1225), ("releaseAllOperationFsm", 1227), ("releaseAllStorageFsm", 1229))

class CucsPolicyPolicyScopeFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460))
    namedValues = NamedValues(("nop", 0), ("releasePolicyFsmBegin", 1201), ("releasePolicyFsmRelease", 1202), ("releaseOperationFsmBegin", 1203), ("releaseOperationFsmRelease", 1204), ("releaseStorageFsmBegin", 1205), ("releaseStorageFsmRelease", 1206), ("resolveManyPolicyFsmBegin", 1207), ("resolveManyPolicyFsmResolveMany", 1208), ("resolveManyOperationFsmBegin", 1209), ("resolveManyOperationFsmResolveMany", 1210), ("resolveManyStorageFsmBegin", 1211), ("resolveManyStorageFsmResolveMany", 1212), ("releaseManyPolicyFsmBegin", 1213), ("releaseManyPolicyFsmReleaseMany", 1214), ("releaseManyOperationFsmBegin", 1215), ("releaseManyOperationFsmReleaseMany", 1216), ("releaseManyStorageFsmBegin", 1217), ("releaseManyStorageFsmReleaseMany", 1218), ("resolveAllPolicyFsmBegin", 1219), ("resolveAllPolicyFsmResolveAll", 1220), ("resolveAllOperationFsmBegin", 1221), ("resolveAllOperationFsmResolveAll", 1222), ("resolveAllStorageFsmBegin", 1223), ("resolveAllStorageFsmResolveAll", 1224), ("releaseAllPolicyFsmBegin", 1225), ("releaseAllPolicyFsmReleaseAll", 1226), ("releaseAllOperationFsmBegin", 1227), ("releaseAllOperationFsmReleaseAll", 1228), ("releaseAllStorageFsmBegin", 1229), ("releaseAllStorageFsmReleaseAll", 1230), ("releaseAllOperationFsmFail", 1431), ("releaseAllOperationFsmSuccess", 1432), ("releaseAllPolicyFsmFail", 1433), ("releaseAllPolicyFsmSuccess", 1434), ("releaseAllStorageFsmFail", 1435), ("releaseAllStorageFsmSuccess", 1436), ("releaseManyOperationFsmFail", 1437), ("releaseManyOperationFsmSuccess", 1438), ("releaseManyPolicyFsmFail", 1439), ("releaseManyPolicyFsmSuccess", 1440), ("releaseManyStorageFsmFail", 1441), ("releaseManyStorageFsmSuccess", 1442), ("releaseOperationFsmFail", 1443), ("releaseOperationFsmSuccess", 1444), ("releasePolicyFsmFail", 1445), ("releasePolicyFsmSuccess", 1446), ("releaseStorageFsmFail", 1447), ("releaseStorageFsmSuccess", 1448), ("resolveAllOperationFsmFail", 1449), ("resolveAllOperationFsmSuccess", 1450), ("resolveAllPolicyFsmFail", 1451), ("resolveAllPolicyFsmSuccess", 1452), ("resolveAllStorageFsmFail", 1453), ("resolveAllStorageFsmSuccess", 1454), ("resolveManyOperationFsmFail", 1455), ("resolveManyOperationFsmSuccess", 1456), ("resolveManyPolicyFsmFail", 1457), ("resolveManyPolicyFsmSuccess", 1458), ("resolveManyStorageFsmFail", 1459), ("resolveManyStorageFsmSuccess", 1460))

class CucsPolicyPolicyScopeFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1201, 1203, 1205, 1207, 1209, 1211, 1213, 1215, 1217, 1219, 1221, 1223, 1225, 1227, 1229))
    namedValues = NamedValues(("nop", 0), ("releasePolicyFsm", 1201), ("releaseOperationFsm", 1203), ("releaseStorageFsm", 1205), ("resolveManyPolicyFsm", 1207), ("resolveManyOperationFsm", 1209), ("resolveManyStorageFsm", 1211), ("releaseManyPolicyFsm", 1213), ("releaseManyOperationFsm", 1215), ("releaseManyStorageFsm", 1217), ("resolveAllPolicyFsm", 1219), ("resolveAllOperationFsm", 1221), ("resolveAllStorageFsm", 1223), ("releaseAllPolicyFsm", 1225), ("releaseAllOperationFsm", 1227), ("releaseAllStorageFsm", 1229))

class CucsPolicyRegistrationStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("registering", 0), ("registered", 1), ("failed", 2), ("lostVisibility", 3), ("unregistered", 4))

class CucsPolicyRepairStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("done", 0), ("notDone", 1))

class CucsPolicyResumeAckState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("noAck", 0), ("acked", 1))

class CucsPolicyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("outOfSync", 1))

class CucsPolicySuspendState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class CucsPoolElementOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("endPoint", 0), ("pool", 1))

class CucsPoolPoolAssignmentOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("default", 0), ("sequential", 1))

class CucsPortEncap(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("dot1q", 1), ("isl", 2), ("negotiate", 3), ("proprietary", 4))

class CucsPortEthAdminSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("indeterminate", 0), ("n1gbps", 1), ("n10gbps", 2), ("n20gbps", 3), ("n40gbps", 4))

class CucsPortEthSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("indeterminate", 0), ("n1gbps", 1), ("n10gbps", 2), ("n20gbps", 3), ("n40gbps", 4))

class CucsPortGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 4, 8, 16, 32, 64, 128, 256, 512))
    namedValues = NamedValues(("switchEther", 1), ("switchFc", 4), ("host", 8), ("fabric", 16), ("fabricPc", 32), ("hostPc", 64), ("adaptorExt", 128), ("adaptorPc", 256), ("serverPc", 512))

class CucsPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("access", 1), ("trunk", 2), ("fabric", 3), ("nProxy", 4), ("f", 5), ("e", 6), ("sd", 7))

class CucsPortPIoFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1014, 1334))
    namedValues = NamedValues(("nop", 0), ("inCompatSfpPresence", 1014), ("inCompatSfpReplaced", 1334))

class CucsPortPIoFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1014, 1015, 1034, 1035, 1334, 1335, 1461, 1462))
    namedValues = NamedValues(("nop", 0), ("inCompatSfpPresenceBegin", 1014), ("inCompatSfpPresenceShutdown", 1015), ("inCompatSfpPresenceFail", 1034), ("inCompatSfpPresenceSuccess", 1035), ("inCompatSfpReplacedBegin", 1334), ("inCompatSfpReplacedEnablePort", 1335), ("inCompatSfpReplacedFail", 1461), ("inCompatSfpReplacedSuccess", 1462))

class CucsPortPIoFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1014, 1334))
    namedValues = NamedValues(("nop", 0), ("inCompatSfpPresence", 1014), ("inCompatSfpReplaced", 1334))

class CucsPortSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("indeterminate", 0), ("n1gbps", 1), ("n2gbps", 2), ("n4gbps", 3), ("n8gbps", 4), ("auto", 5))

class CucsPortTrust(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("trusted", 0), ("untrusted", 1))

class CucsPowerCapAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nothing", 0), ("clockDown", 1), ("throttled", 2))

class CucsPowerChThrAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nothing", 0), ("throttleBladeDisc", 1), ("stopBladeDisc", 2))

class CucsPowerGroupState(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capOk", 0), ("capMismatch", 1))

class CucsPowerGroupStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("power", 0), ("powerAvg", 1), ("powerMax", 2), ("powerMin", 3))

class CucsPowerGroupStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("power", 0), ("powerAvg", 1), ("powerMax", 2), ("powerMin", 3))

class CucsPowerMemberState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("uninitialized", 0), ("capOk", 1), ("fwMismatch", 2), ("psuInsufficient", 3), ("psuRedundancyFailed", 4), ("capInsufficient", 5))

class CucsPowerMgmtStyle(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("manualPerBlade", 0), ("intelligentPolicyDriven", 1))

class CucsPowerOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3, 6, 7, 10, 11, 12, 13))
    namedValues = NamedValues(("notCapped", 0), ("discoveryRetry", 3), ("nonCompliant", 6), ("firmwareMismatch", 7), ("budgeting", 10), ("budgeted", 11), ("deploying", 12), ("deployed", 13))

class CucsPowerPrioritySharing(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noPreference", 0), ("highestPrioInChassis", 1), ("highestPrioInPowerGroup", 2))

class CucsPowerPsuState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("insufficient", 1))

class CucsPowerReallocation(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("chassis", 0))

class CucsPowerReqConflict(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ignore", 0), ("failPlacement", 1))

class CucsProcStatAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("on", 1), ("clearStats", 2), ("logStats", 3))

class CucsProcessorEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("inputCurrent", 0), ("inputCurrentAvg", 1), ("inputCurrentMax", 2), ("inputCurrentMin", 3), ("temperature", 4), ("temperatureAvg", 5), ("temperatureMax", 6), ("temperatureMin", 7))

class CucsProcessorEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("inputCurrent", 0), ("inputCurrentAvg", 1), ("inputCurrentMax", 2), ("inputCurrentMin", 3), ("temperature", 4), ("temperatureAvg", 5), ("temperatureMax", 6), ("temperatureMin", 7))

class CucsProcessorErrorStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("mirroringInterSockErrors", 0), ("mirroringIntraSockErrors", 1), ("smiLinkCorrErrors", 2), ("smiLinkUncorrErrors", 3), ("sparingErrors", 4))

class CucsProcessorQualArch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 132, 134, 135, 178, 179, 181))
    namedValues = NamedValues(("any", 0), ("intelP4C", 1), ("opteron", 132), ("turion64", 134), ("dualCoreOpteron", 135), ("pentium4", 178), ("xeon", 179), ("xeonMP", 181))

class CucsProcessorRuntimeThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("load", 0), ("loadAvg", 1), ("loadMax", 2), ("loadMin", 3))

class CucsProcessorRuntimeHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("load", 0), ("loadAvg", 1), ("loadMax", 2), ("loadMin", 3))

class CucsProcessorUnitArch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 132, 134, 135, 178, 179, 181))
    namedValues = NamedValues(("any", 0), ("intelP4C", 1), ("opteron", 132), ("turion64", 134), ("dualCoreOpteron", 135), ("pentium4", 178), ("xeon", 179), ("xeonMP", 181))

class CucsQosHostControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("full", 1), ("fullWithException", 2))

class CucsQosPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("fc", 1), ("platinum", 2), ("gold", 3), ("silver", 4), ("bronze", 5), ("bestEffort", 6))

class CucsQosclassDefinitionFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 313))
    namedValues = NamedValues(("nop", 0), ("configGlobalQoS", 313))

class CucsQosclassDefinitionFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 313, 314, 315, 430, 431))
    namedValues = NamedValues(("nop", 0), ("configGlobalQoSBegin", 313), ("configGlobalQoSSetLocal", 314), ("configGlobalQoSSetPeer", 315), ("configGlobalQoSFail", 430), ("configGlobalQoSSuccess", 431))

class CucsQosclassDefinitionFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 313))
    namedValues = NamedValues(("nop", 0), ("configGlobalQoS", 313))

class CucsQosclassEthBEAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsQosclassEthBEDrop(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("drop", 0), ("noDrop", 1))

class CucsQosclassEthBEPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("fc", 1), ("platinum", 2), ("gold", 3), ("silver", 4), ("bronze", 5), ("bestEffort", 6))

class CucsQosclassEthClassifiedAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsQosclassEthClassifiedDrop(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("drop", 0), ("noDrop", 1))

class CucsQosclassEthClassifiedPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("fc", 1), ("platinum", 2), ("gold", 3), ("silver", 4), ("bronze", 5), ("bestEffort", 6))

class CucsQosclassFcAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsQosclassFcDrop(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("drop", 0), ("noDrop", 1))

class CucsQosclassFcPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("fc", 1), ("platinum", 2), ("gold", 3), ("silver", 4), ("bronze", 5), ("bestEffort", 6))

class CucsSolAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class CucsSolSpeed(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(6, 7, 8, 9, 10, 9600))
    namedValues = NamedValues(("n9600", 6), ("n19200", 7), ("n38400", 8), ("n57600", 9), ("n115200", 10), ("defaultValue", 9600))

class CucsStatsCollectionDomain(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 0), ("chassis", 2), ("port", 4), ("host", 5), ("adapter", 6), ("server", 7), ("fex", 8))

class CucsStatsCollectionInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(30, 60, 120, 300))
    namedValues = NamedValues(("n30seconds", 30), ("n1minute", 60), ("n2minutes", 120), ("n5minutes", 300))

class CucsStatsCollectionPolicyFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 310))
    namedValues = NamedValues(("nop", 0), ("updateEp", 310))

class CucsStatsCollectionPolicyFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 310, 311, 312, 432, 433))
    namedValues = NamedValues(("nop", 0), ("updateEpBegin", 310), ("updateEpSetEpA", 311), ("updateEpSetEpB", 312), ("updateEpFail", 432), ("updateEpSuccess", 433))

class CucsStatsCollectionPolicyFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 310))
    namedValues = NamedValues(("nop", 0), ("updateEp", 310))

class CucsStatsReportingInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(120, 900, 1800, 3600, 7200, 14400, 28800))
    namedValues = NamedValues(("n2minutes", 120), ("n15minutes", 900), ("n30minutes", 1800), ("n60minutes", 3600), ("n2hours", 7200), ("n4hours", 14400), ("n8hours", 28800))

class CucsStatsThr32DefinitionPropType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("uint32", 1), ("uint64", 2), ("float", 3))

class CucsStatsThr32ValuePropType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("uint32", 1), ("uint64", 2), ("float", 3))

class CucsStatsThr64DefinitionPropType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("uint32", 1), ("uint64", 2), ("float", 3))

class CucsStatsThr64ValuePropType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("uint32", 1), ("uint64", 2), ("float", 3))

class CucsStatsThrFloatDefinitionPropType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("uint32", 1), ("uint64", 2), ("float", 3))

class CucsStatsThrFloatValuePropType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("uint32", 1), ("uint64", 2), ("float", 3))

class CucsStatsThresholdDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("aboveNormal", 1), ("belowNormal", 2))

class CucsStorageAllocState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("allocating", 1), ("allocated", 2), ("failed", 3))

class CucsStorageBatteryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("battery", 1), ("supercap", 2))

class CucsStorageConfiguration(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("supported", 1), ("notSupported", 2))

class CucsStorageConnectionProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unspecified", 0), ("sas", 1), ("sata", 2))

class CucsStorageControllerFaultMonitoring(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("supported", 1), ("notSupported", 2))

class CucsStorageControllerId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(1, 64)

class CucsStorageControllerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sas", 1), ("sata", 2), ("flash", 3))

class CucsStorageControllerForm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("none", 0), ("onBoard", 1), ("mezzanine", 2), ("pci", 3), ("embedded", 4))

class CucsStorageDisklessAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unspecified", 0), ("yes", 1), ("no", 2))

class CucsStorageEpAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("readonly", 1), ("admin", 2))

class CucsStorageEtherIfVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("regular", 0), ("default", 1), ("native", 2))

class CucsStorageFcZoningType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("sist", 1), ("simt", 2))

class CucsStorageFileSystemStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("clean", 1), ("notClean", 2))

class CucsStorageIniGroupOperProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("derived", 0), ("fc", 1), ("iscsi", 2))

class CucsStorageIniGroupOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("policy", 2), ("logical", 4), ("connPolicy", 8))

class CucsStorageIniGroupProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("derived", 0), ("fc", 1), ("iscsi", 2))

class CucsStorageKeyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("initiator", 1), ("target", 2))

class CucsStorageLocalDiskConfigFlexFlashRAIDReportingState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class CucsStorageLocalDiskConfigFlexFlashState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class CucsStorageLocalDiskMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("noLocalStorage", 1), ("singleDisk", 2), ("dualDisk", 3), ("raidStriped", 4), ("raidMirrored", 5), ("bestEffortMirrored", 6), ("bestEffortStriped", 7), ("anyConfiguration", 8), ("noRaid", 9), ("raidStripedParity", 10), ("raidStripedDualParity", 11), ("raidMirroredStriped", 12), ("bestEffortStripedParity", 13), ("bestEffortStripedDualParity", 14), ("bestEffortMirroredStriped", 15))

class CucsStorageLocalDiskPartitionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("swap", 2), ("ext2", 3), ("ext3", 4), ("ntfs", 5), ("fat32", 6))

class CucsStorageLunType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unspecified", 0), ("simple", 1), ("mirror", 2), ("stripe", 3), ("raid", 4), ("stripeParity", 5), ("stripeDualParity", 6), ("mirrorStripe", 7), ("stripeParityStripe", 8), ("stripeDualParityStripe", 9))

class CucsStorageOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("misconfigured", 1))

class CucsStoragePathHA(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("initiator", 0), ("target", 1), ("fabric", 2))

class CucsStorageProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("derived", 0), ("fc", 1), ("iscsi", 2))

class CucsStorageRaidBatteryOperabilityQualifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("unknown", 0))

class CucsStorageRaidType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("raid0", 0), ("raid1", 1), ("raid5", 2), ("raid6", 3), ("raid00", 4), ("raid10", 5), ("raid50", 6), ("raid60", 7))

class CucsStorageSystemFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1383))
    namedValues = NamedValues(("nop", 0), ("sync", 1383))

class CucsStorageSystemFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1383, 1384, 1463, 1464))
    namedValues = NamedValues(("nop", 0), ("syncBegin", 1383), ("syncExecute", 1384), ("syncFail", 1463), ("syncSuccess", 1464))

class CucsStorageSystemFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1383))
    namedValues = NamedValues(("nop", 0), ("sync", 1383))

class CucsStorageTargetPath(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("dual", 3))

class CucsStorageTechnology(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unspecified", 0), ("hdd", 1), ("ssd", 2))

class CucsStorageVsanRefSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("dual", 3))

class CucsSwAccessDomainLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwAccessDomainType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwAccessDomainFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 222))
    namedValues = NamedValues(("nop", 0), ("deploy", 222))

class CucsSwAccessDomainFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 222, 223, 434, 435))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 222), ("deployUpdateConnectivity", 223), ("deployFail", 434), ("deploySuccess", 435))

class CucsSwAccessDomainFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 222))
    namedValues = NamedValues(("nop", 0), ("deploy", 222))

class CucsSwAccessEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwAccessEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwBorderDomainLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwBorderEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwBorderPcLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwCIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsSwCardEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("slotOutlet1", 0), ("slotOutlet1Avg", 1), ("slotOutlet1Max", 2), ("slotOutlet1Min", 3), ("slotOutlet2", 4), ("slotOutlet2Avg", 5), ("slotOutlet2Max", 6), ("slotOutlet2Min", 7), ("slotOutlet3", 8), ("slotOutlet3Avg", 9), ("slotOutlet3Max", 10), ("slotOutlet3Min", 11))

class CucsSwCardEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("slotOutlet1", 0), ("slotOutlet1Avg", 1), ("slotOutlet1Max", 2), ("slotOutlet1Min", 3), ("slotOutlet2", 4), ("slotOutlet2Avg", 5), ("slotOutlet2Max", 6), ("slotOutlet2Min", 7), ("slotOutlet3", 8), ("slotOutlet3Avg", 9), ("slotOutlet3Max", 10), ("slotOutlet3Min", 11))

class CucsSwConfMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("inProgress", 1), ("verifying", 2), ("failed", 3))

class CucsSwConfigStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("noVlanComp", 2))

class CucsSwEnvStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("fanCtrlrInlet1", 0), ("fanCtrlrInlet1Avg", 1), ("fanCtrlrInlet1Max", 2), ("fanCtrlrInlet1Min", 3), ("fanCtrlrInlet2", 4), ("fanCtrlrInlet2Avg", 5), ("fanCtrlrInlet2Max", 6), ("fanCtrlrInlet2Min", 7), ("fanCtrlrInlet3", 8), ("fanCtrlrInlet3Avg", 9), ("fanCtrlrInlet3Max", 10), ("fanCtrlrInlet3Min", 11), ("fanCtrlrInlet4", 12), ("fanCtrlrInlet4Avg", 13), ("fanCtrlrInlet4Max", 14), ("fanCtrlrInlet4Min", 15), ("mainBoardOutlet1", 16), ("mainBoardOutlet1Avg", 17), ("mainBoardOutlet1Max", 18), ("mainBoardOutlet1Min", 19), ("mainBoardOutlet2", 20), ("mainBoardOutlet2Avg", 21), ("mainBoardOutlet2Max", 22), ("mainBoardOutlet2Min", 23), ("psuCtrlrInlet1", 24), ("psuCtrlrInlet1Avg", 25), ("psuCtrlrInlet1Max", 26), ("psuCtrlrInlet1Min", 27), ("psuCtrlrInlet2", 28), ("psuCtrlrInlet2Avg", 29), ("psuCtrlrInlet2Max", 30), ("psuCtrlrInlet2Min", 31))

class CucsSwEnvStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("fanCtrlrInlet1", 0), ("fanCtrlrInlet1Avg", 1), ("fanCtrlrInlet1Max", 2), ("fanCtrlrInlet1Min", 3), ("fanCtrlrInlet2", 4), ("fanCtrlrInlet2Avg", 5), ("fanCtrlrInlet2Max", 6), ("fanCtrlrInlet2Min", 7), ("fanCtrlrInlet3", 8), ("fanCtrlrInlet3Avg", 9), ("fanCtrlrInlet3Max", 10), ("fanCtrlrInlet3Min", 11), ("fanCtrlrInlet4", 12), ("fanCtrlrInlet4Avg", 13), ("fanCtrlrInlet4Max", 14), ("fanCtrlrInlet4Min", 15), ("mainBoardOutlet1", 16), ("mainBoardOutlet1Avg", 17), ("mainBoardOutlet1Max", 18), ("mainBoardOutlet1Min", 19), ("mainBoardOutlet2", 20), ("mainBoardOutlet2Avg", 21), ("mainBoardOutlet2Max", 22), ("mainBoardOutlet2Min", 23), ("psuCtrlrInlet1", 24), ("psuCtrlrInlet1Avg", 25), ("psuCtrlrInlet1Max", 26), ("psuCtrlrInlet1Min", 27), ("psuCtrlrInlet2", 28), ("psuCtrlrInlet2Avg", 29), ("psuCtrlrInlet2Max", 30), ("psuCtrlrInlet2Min", 31))

class CucsSwEstcEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwEthEstcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthEstcPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthLanBorderTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthLanBorderFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 224))
    namedValues = NamedValues(("nop", 0), ("deploy", 224))

class CucsSwEthLanBorderFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 224, 225, 436, 437, 1184))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 224), ("deployUpdateConnectivity", 225), ("deployFail", 436), ("deploySuccess", 437), ("deployUpdateVlanGroups", 1184))

class CucsSwEthLanBorderFsmTaskFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("samDmeSwEthLanBorderDeployVlanGroupConfig", 59), ("samDmeSwEthLanBorderDeployVlanGroupRetry", 60), ("samDmeSwEthLanBorderDeployPortConfig", 61))

class CucsSwEthLanBorderFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 224))
    namedValues = NamedValues(("nop", 0), ("deploy", 224))

class CucsSwEthLanEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthLanEpVlanStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("missingPrimary", 1))

class CucsSwEthLanMonTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthLanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthLanPcVlanStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ok", 0), ("missingPrimary", 1))

class CucsSwEthMonTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthMonType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwEthMonDestEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthMonFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 867))
    namedValues = NamedValues(("nop", 0), ("deploy", 867))

class CucsSwEthMonFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 867, 868, 1004, 1005))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 867), ("deployUpdateEthMon", 868), ("deployFail", 1004), ("deploySuccess", 1005))

class CucsSwEthMonFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 953))
    namedValues = NamedValues(("nop", 0), ("deploy", 953))

class CucsSwEthMonSrcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwEthTargetEpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsSwEthTargetEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFabricZoneNsAllocStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("available", 0), ("full", 1))

class CucsSwFcEstcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcMonTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcMonType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwFcMonDestEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcMonFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 869))
    namedValues = NamedValues(("nop", 0), ("deploy", 869))

class CucsSwFcMonFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 869, 870, 1006, 1007))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 869), ("deployUpdateFcMon", 870), ("deployFail", 1006), ("deploySuccess", 1007))

class CucsSwFcMonFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 955))
    namedValues = NamedValues(("nop", 0), ("deploy", 955))

class CucsSwFcMonSrcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcSanBorderTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcSanBorderUplinkTrunking(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsSwFcSanBorderFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 226, 1185))
    namedValues = NamedValues(("nop", 0), ("deploy", 226), ("activateZoneSet", 1185))

class CucsSwFcSanBorderFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 226, 227, 438, 439, 1185, 1186, 1465, 1466))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 226), ("deployUpdateConnectivity", 227), ("deployFail", 438), ("deploySuccess", 439), ("activateZoneSetBegin", 1185), ("activateZoneSetUpdateZones", 1186), ("activateZoneSetFail", 1465), ("activateZoneSetSuccess", 1466))

class CucsSwFcSanBorderFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 226, 1185))
    namedValues = NamedValues(("nop", 0), ("deploy", 226), ("activateZoneSet", 1185))

class CucsSwFcSanEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcSanMonTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcSanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcServerZoneGroupLc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3))

class CucsSwFcZoneLc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3))

class CucsSwFcZoneMemberLc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3))

class CucsSwFcZoneSetLc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3))

class CucsSwFcoeEstcEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcoeSanEpTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwFcoeSanPcTransport(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ether", 0), ("dce", 1), ("fc", 2))

class CucsSwLanBorderType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwLanEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsSwLanEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwLanMonType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwLanPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsSwLanPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwMonAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsSwMonDomainLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwMonLifeCycle(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("new", 2), ("deleted", 3))

class CucsSwMonSrcEpLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwPIoEpIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("aggregation", 2), ("virtual", 3))

class CucsSwPIoEpLc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3), ("pending", 4))

class CucsSwPeerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("existing", 1), ("nonexisting", 2))

class CucsSwPhysFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1121))
    namedValues = NamedValues(("nop", 0), ("confPhysical", 1121))

class CucsSwPhysFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128))
    namedValues = NamedValues(("nop", 0), ("confPhysicalBegin", 1121), ("confPhysicalPortInventorySwA", 1122), ("confPhysicalPortInventorySwB", 1123), ("confPhysicalConfigSwA", 1124), ("confPhysicalConfigSwB", 1125), ("confPhysicalVerifyPhysConfig", 1126), ("confPhysicalSuccess", 1127), ("confPhysicalFail", 1128))

class CucsSwPhysFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1082))
    namedValues = NamedValues(("nop", 0), ("confPhysical", 1082))

class CucsSwSanBorderType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwSanEpIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsSwSanEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwSanMonType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwSanPcIfRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("unknown", 0), ("network", 1), ("server", 2), ("mgmt", 3), ("diag", 4), ("storage", 5), ("monitor", 6), ("fcoeStorage", 7), ("nasStorage", 8), ("fcoeNasStorage", 9), ("fcoeUplink", 10), ("networkFcoeUplink", 11))

class CucsSwSanPcType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwSystemStatsThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("load", 0), ("loadAvg", 1), ("loadMax", 2), ("loadMin", 3), ("memAvailable", 4), ("memAvailableAvg", 5), ("memAvailableMax", 6), ("memAvailableMin", 7), ("memCached", 8), ("memCachedAvg", 9), ("memCachedMax", 10), ("memCachedMin", 11))

class CucsSwSystemStatsHistThresholded(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("load", 0), ("loadAvg", 1), ("loadMax", 2), ("loadMin", 3), ("memAvailable", 4), ("memAvailableAvg", 5), ("memAvailableMax", 6), ("memAvailableMin", 7), ("memCached", 8), ("memCachedAvg", 9), ("memCachedMax", 10), ("memCachedMin", 11))

class CucsSwTargetEpType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwUlanPurpose(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("management", 1), ("boot", 2), ("reserved1", 3), ("reserved2", 4))

class CucsSwUtilityDomainLocale(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("server", 0), ("chassis", 1), ("internal", 2), ("external", 3))

class CucsSwUtilityDomainType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("lan", 0), ("san", 1), ("ipc", 2))

class CucsSwUtilityDomainFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 228))
    namedValues = NamedValues(("nop", 0), ("deploy", 228))

class CucsSwUtilityDomainFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 228, 229, 440, 441))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 228), ("deployUpdateConnectivity", 229), ("deployFail", 440), ("deploySuccess", 441))

class CucsSwUtilityDomainFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 228))
    namedValues = NamedValues(("nop", 0), ("deploy", 228))

class CucsSwVlanLc(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3), ("pending", 4), ("provisioned", 5))

class CucsSwVlanCompType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("included", 1), ("excluded", 2))

class CucsSwVlanConfigStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("applied", 1), ("unApplied", 2))

class CucsSwVlanGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("compressed", 1), ("uncompressed", 2))

class CucsSwVlanPortNsAllocStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("available", 0), ("exceeded", 1))

class CucsSysdebugAutoCoreFileExportTargetProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("ftp", 1), ("tftp", 2), ("scp", 3), ("http", 4), ("sftp", 5), ("nfsCopy", 6))

class CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 216))
    namedValues = NamedValues(("nop", 0), ("configure", 216))

class CucsSysdebugAutoCoreFileExportTargetFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 216, 217, 218, 444, 445))
    namedValues = NamedValues(("nop", 0), ("configureBegin", 216), ("configureLocal", 217), ("configurePeer", 218), ("configureFail", 444), ("configureSuccess", 445))

class CucsSysdebugAutoCoreFileExportTargetFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 216))
    namedValues = NamedValues(("nop", 0), ("configure", 216))

class CucsSysdebugBackupBehaviorInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3600, 7200, 14400, 28800, 86400, 604800, 2592000))
    namedValues = NamedValues(("never", 0), ("n1hour", 3600), ("n2hours", 7200), ("n4hours", 14400), ("n8hours", 28800), ("n24hours", 86400), ("n1week", 604800), ("n1month", 2592000))

class CucsSysdebugBackupBehaviorProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("ftp", 1), ("tftp", 2), ("scp", 3), ("http", 4), ("sftp", 5), ("nfsCopy", 6))

class CucsSysdebugBackupFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ascii", 1), ("binary", 2))

class CucsSysdebugCoreExportStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("success", 1), ("failure", 2))

class CucsSysdebugCoreFileAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("init", 0), ("prepareDownload", 1), ("downloaded", 2))

class CucsSysdebugCoreFileOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unavailable", 0), ("available", 1), ("availableOnSubordinate", 2), ("inProgress", 3), ("failed", 4))

class CucsSysdebugCoreFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1041))
    namedValues = NamedValues(("nop", 0), ("download", 1041))

class CucsSysdebugCoreFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1041, 1042, 1043, 1044, 1045, 1053, 1054))
    namedValues = NamedValues(("nop", 0), ("downloadBegin", 1041), ("downloadCopySub", 1042), ("downloadCopyPrimary", 1043), ("downloadDeleteSub", 1044), ("downloadDeletePrimary", 1045), ("downloadFail", 1053), ("downloadSuccess", 1054))

class CucsSysdebugCoreFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1041))
    namedValues = NamedValues(("nop", 0), ("download", 1041))

class CucsSysdebugEpLogAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("policy", 0), ("backup", 1), ("clear", 2))

class CucsSysdebugEpLogBackupAction(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("logFull", 0), ("onClear", 1), ("timer", 2), ("onAssocChange", 3))

class CucsSysdebugEpLogCapacity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("available", 1), ("low", 2), ("veryLow", 3), ("full", 4))

class CucsSysdebugEpLogType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sel", 1), ("obfl", 2), ("syslog", 3))

class CucsSysdebugLogControlDomainEnum(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("sysmgmt", 0))

class CucsSysdebugLogControlEpFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 219))
    namedValues = NamedValues(("nop", 0), ("logControlPersist", 219))

class CucsSysdebugLogControlEpFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 219, 220, 221, 446, 447))
    namedValues = NamedValues(("nop", 0), ("logControlPersistBegin", 219), ("logControlPersistLocal", 220), ("logControlPersistPeer", 221), ("logControlPersistFail", 446), ("logControlPersistSuccess", 447))

class CucsSysdebugLogControlEpFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 219))
    namedValues = NamedValues(("nop", 0), ("logControlPersist", 219))

class CucsSysdebugLogControlLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("debug0", 0), ("debug1", 1), ("debug2", 2), ("debug3", 3), ("debug4", 4), ("info", 5), ("warn", 6), ("minor", 7), ("major", 8), ("crit", 9))

class CucsSysdebugMEpLogOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ok", 0), ("permissionDeniedError", 1), ("remoteCommunicationError", 2), ("bmcCommunicationError", 3), ("internalUcsmError", 4))

class CucsSysdebugManualCoreFileExportTargetAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class CucsSysdebugManualCoreFileExportTargetProto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("ftp", 1), ("tftp", 2), ("scp", 3), ("http", 4), ("sftp", 5), ("nfsCopy", 6))

class CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 214))
    namedValues = NamedValues(("nop", 0), ("export", 214))

class CucsSysdebugManualCoreFileExportTargetFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 214, 215, 448, 449))
    namedValues = NamedValues(("nop", 0), ("exportBegin", 214), ("exportExecute", 215), ("exportFail", 448), ("exportSuccess", 449))

class CucsSysdebugManualCoreFileExportTargetFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 214))
    namedValues = NamedValues(("nop", 0), ("export", 214))

class CucsSysdebugTSCmdOptMajorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("chassis", 0), ("fex", 1), ("server", 2), ("ucsm", 3), ("ucsmMgmt", 4))

class CucsSysdebugTechSupportAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("init", 0), ("start", 1), ("created", 2), ("prepareDownload", 3), ("delete", 4))

class CucsSysdebugTechSupportFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 881, 883, 886))
    namedValues = NamedValues(("nop", 0), ("initiate", 881), ("deleteTechSupFile", 883), ("download", 886))

class CucsSysdebugTechSupportFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 1008, 1009, 1010, 1011, 1012, 1013))
    namedValues = NamedValues(("nop", 0), ("initiateBegin", 881), ("initiateLocal", 882), ("deleteTechSupFileBegin", 883), ("deleteTechSupFileLocal", 884), ("deleteTechSupFilePeer", 885), ("downloadBegin", 886), ("downloadCopySub", 887), ("downloadCopyPrimary", 888), ("downloadDeleteSub", 889), ("downloadDeletePrimary", 890), ("deleteTechSupFileFail", 1008), ("deleteTechSupFileSuccess", 1009), ("downloadFail", 1010), ("downloadSuccess", 1011), ("initiateFail", 1012), ("initiateSuccess", 1013))

class CucsSysdebugTechSupportFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 881, 883, 886))
    namedValues = NamedValues(("nop", 0), ("initiate", 881), ("deleteTechSupFile", 883), ("download", 886))

class CucsSysdebugTechSupportOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unavailable", 0), ("available", 1), ("availableOnSubordinate", 2), ("inProgress", 3), ("failed", 4))

class CucsSysfileExporterPostAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("remove", 1))

class CucsSysfileMutationAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("remove", 1))

class CucsSysfileMutationFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 209, 211))
    namedValues = NamedValues(("nop", 0), ("single", 209), ("global", 211))

class CucsSysfileMutationFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 209, 210, 211, 212, 213, 450, 451, 452, 453))
    namedValues = NamedValues(("nop", 0), ("singleBegin", 209), ("singleExecute", 210), ("globalBegin", 211), ("globalLocal", 212), ("globalPeer", 213), ("globalFail", 450), ("globalSuccess", 451), ("singleFail", 452), ("singleSuccess", 453))

class CucsSysfileMutationFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 209, 211))
    namedValues = NamedValues(("nop", 0), ("single", 209), ("global", 211))

class CucsTopMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unspecified", 0), ("standAlone", 1), ("cluster", 2))

class CucsTrigAckOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("untriggered", 0), ("evaluationPending", 1), ("evaluated", 2), ("waitingForUser", 3), ("waitingForMaintWindow", 4), ("applyPending", 5), ("applied", 6), ("waitingForDependency", 7), ("none", 8), ("expired", 9), ("pending", 10), ("active", 11))

class CucsTrigAckPrevOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("untriggered", 0), ("evaluationPending", 1), ("evaluated", 2), ("waitingForUser", 3), ("waitingForMaintWindow", 4), ("applyPending", 5), ("applied", 6), ("waitingForDependency", 7), ("none", 8), ("expired", 9), ("pending", 10), ("active", 11))

class CucsTrigAckChangeDetails(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("binding", 0), ("hostVirtEthIf", 1), ("hostNonvirtEthIf", 2), ("hostEthIfProfile", 3), ("hostEthIfQos", 4), ("hostEthIfNwCtrl", 5), ("hostVirtFcIf", 6), ("hostNonvirtFcIf", 7), ("hostVirtFcIfPersBind", 8), ("hostNonvirtFcIfPersBind", 9), ("hostFcIfProfile", 10), ("hostFcIfQos", 11), ("hostFcoeIf", 12), ("vif", 13), ("vlan", 14), ("vsan", 15), ("ip", 16), ("bootOrder", 17), ("bootVirtVnic", 18), ("bootNonvirtVnic", 19), ("bootLocalStorage", 20), ("bootVirtPxe", 21), ("bootNonvirtPxe", 22), ("bladeIdentity", 24), ("agentPolicy", 25), ("biosFw", 26), ("storageControllerFw", 27), ("adaptorHostFw", 28), ("adaptorNwFw", 29), ("mgmtControllerFw", 30), ("localDiskPolicy", 31), ("pin", 32), ("sol", 33), ("epAuth", 34), ("biosProfile", 35), ("checkpoint", 36), ("implicitReboot", 37), ("implicitHostFcIfProfileRedeploy", 38), ("boardControllerFw", 39), ("hostEthIfQosHostControl", 40), ("localDiskFw", 41), ("implicitHostEthIfProfileRedeploy", 42), ("storagePath", 43), ("bmcUpdateBiosFw", 44), ("hostIfPcie", 45), ("flexflashConfig", 46), ("flexflashReboot", 47))

class CucsTrigAckChanges(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("serverIdentity", 0), ("storage", 1), ("networking", 2), ("vnicVhbaPlacement", 3), ("bootOrder", 4), ("serverAssignment", 5), ("operationalPolicies", 6))

class CucsTrigAckDisr(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("upTime", 0))

class CucsTrigAckMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("immediate", 0), ("userAck", 1), ("timerAutomatic", 2))

class CucsTrigAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))
    namedValues = NamedValues(("triggerImmediate", 0), ("triggered", 1), ("untriggered", 2), ("userAck", 4))

class CucsTrigDay(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("oddDay", 8), ("evenDay", 9), ("everyDay", 10))

class CucsTrigOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("pending", 0), ("inProgress", 1), ("failed", 2), ("triggered", 3), ("capReached", 4))

class CucsTrigTokenOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("valid", 0), ("expired", 1))

class CucsTrigTrigOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("untriggered", 0), ("evaluationPending", 1), ("evaluated", 2), ("waitingForUser", 3), ("waitingForMaintWindow", 4), ("applyPending", 5), ("applied", 6), ("waitingForDependency", 7), ("none", 8), ("expired", 9), ("pending", 10), ("active", 11))

class CucsTrigTriggeredState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("pending", 0), ("inProgress", 1), ("failed", 2), ("triggered", 3))

class CucsUuidpoolPoolAssignmentOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("default", 0), ("sequential", 1))

class CucsVmAdaptorOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("policy", 2), ("logical", 4), ("connPolicy", 8))

class CucsVmComputeEpClInstType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("vm", 0), ("hv", 1), ("computeEp", 2))

class CucsVmHbaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVmHvClInstType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("vm", 0), ("hv", 1), ("computeEp", 2))

class CucsVmHvType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unspecified", 0), ("esx", 1), ("kvm", 2), ("hyperv", 3), ("xen", 4))

class CucsVmInstType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("vm", 0), ("hv", 1), ("computeEp", 2))

class CucsVmLifeCyclePolicyFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1132))
    namedValues = NamedValues(("nop", 0), ("config", 1132))

class CucsVmLifeCyclePolicyFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1132, 1133, 1134, 1146, 1147))
    namedValues = NamedValues(("nop", 0), ("configBegin", 1132), ("configLocal", 1133), ("configPeer", 1134), ("configFail", 1146), ("configSuccess", 1147))

class CucsVmLifeCyclePolicyFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1142))
    namedValues = NamedValues(("nop", 0), ("config", 1142))

class CucsVmMgmtPlane(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unmanaged", 0), ("vcenter", 1), ("rhevM", 2), ("scvmm", 3))

class CucsVmNicType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVmOsHvVendor(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unspecified", 0), ("vmware", 1), ("redhat", 2), ("microsoft", 3), ("novell", 4), ("oracle", 5), ("citrix", 6))

class CucsVmStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("online", 1), ("offline", 2))

class CucsVmSwitchAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disable", 0), ("enable", 1))

class CucsVnicAEtherIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicAFcIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicAIpcIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicAScsiIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicConfigIssues(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pinningVlanMismatch", 0), ("vnicVlanAssignmentError", 1), ("missingPrimaryVlan", 2), ("pinnedTargetMisconfig", 3), ("unresolvedVlanName", 4), ("inaccessibleVlan", 5), ("unresolvedVsanName", 6), ("unresolvedRemoteVlanName", 7), ("unresolvedRemoteVsanName", 8), ("unableToUpdateUcsm", 9))

class CucsVnicConnectionLcCtrlState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("available", 0), ("allocated", 1), ("deallocated", 2), ("repurposed", 3))

class CucsVnicConnectionOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("policy", 2), ("logical", 4), ("connPolicy", 8))

class CucsVnicConnectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicDefBehType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("vnic", 1), ("vhba", 2))

class CucsVnicDefaultAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("hwInherit", 1))

class CucsVnicDynamicConReqProtection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("protectedPrefA", 1), ("protectedPrefB", 2), ("protected", 3))

class CucsVnicEtherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicEtherBaseSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 5, 6))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("aB", 5), ("bA", 6))

class CucsVnicExternalMgmtIPMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("static", 2), ("pooled", 3))

class CucsVnicFcBasePersBind(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 4))
    namedValues = NamedValues(("disabled", 0), ("enabled", 4))

class CucsVnicFcBaseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicFcNodeOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("policy", 2), ("logical", 4), ("connPolicy", 8))

class CucsVnicHostNwIOPerfPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("none", 0), ("highPerfReqd", 1))

class CucsVnicIPv4DnsPref(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("preferred", 0), ("alternate", 1))

class CucsVnicIScsiIfDefType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))
    namedValues = NamedValues(("static", 0), ("dynamicNw", 1), ("option17", 2), ("option43", 4))

class CucsVnicIScsiNodeOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))
    namedValues = NamedValues(("unknown", 0), ("physical", 1), ("policy", 2), ("logical", 4), ("connPolicy", 8))

class CucsVnicIfOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))
    namedValues = NamedValues(("indeterminate", 0), ("up", 1), ("down", 2), ("failed", 4))

class CucsVnicInstantiation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("manual", 0), ("default", 1), ("dynamic", 2), ("dynamicVf", 3))

class CucsVnicIpcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicL2IfSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 5, 6))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("aB", 5), ("bA", 6))

class CucsVnicLanConnTemplSwitchId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 5, 6))
    namedValues = NamedValues(("none", 0), ("a", 1), ("b", 2), ("aB", 5), ("bA", 6))

class CucsVnicLunId(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CucsVnicMezzMappingScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("physicalCapFirst", 1), ("capLoadDistribute", 2))

class CucsVnicOrderScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("zeroFuncAll", 0), ("multiFuncAll", 1), ("staticZeroFunc", 2))

class CucsVnicPlacement(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("allVnic", 0), ("staticAllFirst", 1), ("dynamicAllLast", 2))

class CucsVnicProfileConfigQualifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("invalidName", 1))

class CucsVnicProfileSetFsmCurrentFsm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 187, 1118))
    namedValues = NamedValues(("nop", 0), ("deploy", 187), ("deployAlias", 1118))

class CucsVnicProfileSetFsmStageName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 187, 188, 189, 456, 457, 1118, 1119, 1120, 1148, 1149))
    namedValues = NamedValues(("nop", 0), ("deployBegin", 187), ("deployLocal", 188), ("deployPeer", 189), ("deployFail", 456), ("deploySuccess", 457), ("deployAliasBegin", 1118), ("deployAliasLocal", 1119), ("deployAliasPeer", 1120), ("deployAliasFail", 1148), ("deployAliasSuccess", 1149))

class CucsVnicProfileSetFsmTaskItem(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 187, 1123))
    namedValues = NamedValues(("nop", 0), ("deploy", 187), ("deployAlias", 1123))

class CucsVnicSanConnTemplTarget(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("vm", 0), ("adaptor", 1))

class CucsVnicScsiType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4, 8, 16))
    namedValues = NamedValues(("unknown", 0), ("ether", 1), ("fc", 4), ("scsi", 8), ("ipc", 16))

class CucsVnicTemplateTarget(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("vm", 0), ("adaptor", 1))

class CucsVnicTemplateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("initialTemplate", 1), ("updatingTemplate", 2))

class CucsVnicVhbaBehPolicyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("vnic", 1), ("vhba", 2))

class CucsVnicVirtualizationPreferenceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2))
    namedValues = NamedValues(("none", 0), ("sriov", 2))

class CucsVnicVnicBootDev(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class CucsVnicVnicBehPolicyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("vnic", 1), ("vhba", 2))

mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", CucsComputeBladeFsmCurrentFsm=CucsComputeBladeFsmCurrentFsm, CucsStorageLocalDiskMode=CucsStorageLocalDiskMode, CucsLsbootLanOrder=CucsLsbootLanOrder, CucsCommSvcEpFsmStageName=CucsCommSvcEpFsmStageName, CucsLicensePeerStatus=CucsLicensePeerStatus, CucsEtherSwitchIntFIoTransport=CucsEtherSwitchIntFIoTransport, CucsMgmtEntityHaFailureReason=CucsMgmtEntityHaFailureReason, CucsSysdebugCoreFileOperState=CucsSysdebugCoreFileOperState, CucsFabricEthLanPcVlanStatus=CucsFabricEthLanPcVlanStatus, CucsDiagStatusIssues=CucsDiagStatusIssues, CucsMgmtCfgExportPolicyFsmCurrentFsm=CucsMgmtCfgExportPolicyFsmCurrentFsm, CucsAdaptorMenloHostPortStatsHistThresholded=CucsAdaptorMenloHostPortStatsHistThresholded, CucsBiosVpIntelVirtualizationTechnology=CucsBiosVpIntelVirtualizationTechnology, CucsSwFcMonFsmCurrentFsm=CucsSwFcMonFsmCurrentFsm, CucsIdentMetaSystemFsmTaskItem=CucsIdentMetaSystemFsmTaskItem, CucsAdaptorAdapterStatsTrafficDir=CucsAdaptorAdapterStatsTrafficDir, CucsEtherServerIntFIoFsmCurrentFsm=CucsEtherServerIntFIoFsmCurrentFsm, CucsEtherSwitchIntFIoAck=CucsEtherSwitchIntFIoAck, CucsAdaptorEthOffloadProfileTcpTxChecksum=CucsAdaptorEthOffloadProfileTcpTxChecksum, CucsMemoryRuntimeHistThresholded=CucsMemoryRuntimeHistThresholded, CucsFabricEthPcProtocol=CucsFabricEthPcProtocol, CucsFabricWarnings=CucsFabricWarnings, CucsNfsMountInstFsmTaskItem=CucsNfsMountInstFsmTaskItem, CucsEpqosDefinitionFsmCurrentFsm=CucsEpqosDefinitionFsmCurrentFsm, CucsEquipmentLedColor=CucsEquipmentLedColor, CucsPortMode=CucsPortMode, CucsVnicFcNodeOwner=CucsVnicFcNodeOwner, CucsVnicAEtherIfType=CucsVnicAEtherIfType, CucsSwUtilityDomainType=CucsSwUtilityDomainType, CucsMemoryArrayEnvStatsThresholded=CucsMemoryArrayEnvStatsThresholded, CucsAdaptorHostEthIfFsmStageName=CucsAdaptorHostEthIfFsmStageName, CucsEpqosDefinitionFsmStageName=CucsEpqosDefinitionFsmStageName, CucsAdaptorIscsiProtLunBusyRetryCount=CucsAdaptorIscsiProtLunBusyRetryCount, CucsAdaptorMenloEthErrorStatsThresholded=CucsAdaptorMenloEthErrorStatsThresholded, CucsComputeIOHubEnvStatsHistThresholded=CucsComputeIOHubEnvStatsHistThresholded, CucsMemoryIssues=CucsMemoryIssues, CucsEtherTxStatsThresholded=CucsEtherTxStatsThresholded, CucsEquipmentBeaconLedFsmStageName=CucsEquipmentBeaconLedFsmStageName, CucsSwBorderEpLocale=CucsSwBorderEpLocale, CucsFabricFcoeEstcEpSlotId=CucsFabricFcoeEstcEpSlotId, CucsVnicVhbaBehPolicyType=CucsVnicVhbaBehPolicyType, CucsQosclassFcPriority=CucsQosclassFcPriority, CucsFabricVnetEpLocale=CucsFabricVnetEpLocale, CucsIdentIdentRequestFsmCurrentFsm=CucsIdentIdentRequestFsmCurrentFsm, CucsGmetaHolderFsmCurrentFsm=CucsGmetaHolderFsmCurrentFsm, CucsBiosVpSelectMemoryRASConfiguration=CucsBiosVpSelectMemoryRASConfiguration, CucsAdaptorHostMgmtCapPreboot=CucsAdaptorHostMgmtCapPreboot, CucsVnicProfileConfigQualifier=CucsVnicProfileConfigQualifier, CucsLicenseFileFsmCurrentFsm=CucsLicenseFileFsmCurrentFsm, CucsMgmtImporterPostAction=CucsMgmtImporterPostAction, CucsFabricEthEstcEpTransport=CucsFabricEthEstcEpTransport, CucsFabricEthLanTransport=CucsFabricEthLanTransport, CucsExtmgmtGatewayPingNumberOfPingRequests=CucsExtmgmtGatewayPingNumberOfPingRequests, CucsFirmwareUpgradeStatus=CucsFirmwareUpgradeStatus, CucsComputeRackUnitMbTempStatsHistThresholded=CucsComputeRackUnitMbTempStatsHistThresholded, CucsEpqosDefinitionDelTaskFsmTaskItem=CucsEpqosDefinitionDelTaskFsmTaskItem, CucsEquipmentXcvrId=CucsEquipmentXcvrId, CucsTrigAckPrevOperState=CucsTrigAckPrevOperState, CucsFabricEpVlanVlanType=CucsFabricEpVlanVlanType, CucsFabricADceSwSrvEpTransport=CucsFabricADceSwSrvEpTransport, CucsAdaptorMgmtCapOperPowerRequirement=CucsAdaptorMgmtCapOperPowerRequirement, CucsFirmwareDownloaderFsmCurrentFsm=CucsFirmwareDownloaderFsmCurrentFsm, CucsSysdebugManualCoreFileExportTargetFsmTaskItem=CucsSysdebugManualCoreFileExportTargetFsmTaskItem, CucsFaultBasePolicyClearAction=CucsFaultBasePolicyClearAction, CucsCapabilityMgmtExtensionFsmTaskItem=CucsCapabilityMgmtExtensionFsmTaskItem, CucsMgmtConnectionState=CucsMgmtConnectionState, CucsExtvmmEpFsmCurrentFsm=CucsExtvmmEpFsmCurrentFsm, CucsVnicDefBehType=CucsVnicDefBehType, CucsVnicConnectionOwner=CucsVnicConnectionOwner, CucsFabricVsanOperState=CucsFabricVsanOperState, CucsFabricAEthLanEpTransport=CucsFabricAEthLanEpTransport, CucsAdaptorMenloQErrorStatsThresholded=CucsAdaptorMenloQErrorStatsThresholded, CucsPowerReallocation=CucsPowerReallocation, CucsComputePsuClusterState=CucsComputePsuClusterState, CucsStatsCollectionDomain=CucsStatsCollectionDomain, CucsNetworkTransport=CucsNetworkTransport, CucsFabricPcConfigStatus=CucsFabricPcConfigStatus, CucsComputeLinkAggregationCap=CucsComputeLinkAggregationCap, CucsMemoryUnitEnvStatsHistThresholded=CucsMemoryUnitEnvStatsHistThresholded, CucsCommSnmpConfigState=CucsCommSnmpConfigState, CucsFabricSwChEpType=CucsFabricSwChEpType, CucsLsOwner=CucsLsOwner, CucsExtmgmtArpTargetsMaxDeadlineTimeout=CucsExtmgmtArpTargetsMaxDeadlineTimeout, CucsCommSnmpVersion=CucsCommSnmpVersion, CucsEtherSwitchIntFIoPcEpIfRole=CucsEtherSwitchIntFIoPcEpIfRole, CucsStatsReportingInterval=CucsStatsReportingInterval, CucsSwEthLanPcVlanStatus=CucsSwEthLanPcVlanStatus, CucsFabricAFcoeSanEpTransport=CucsFabricAFcoeSanEpTransport, CucsFabricAVlanTransport=CucsFabricAVlanTransport, CucsExtpolConnectorOperState=CucsExtpolConnectorOperState, CucsFcpoolInitiatorEpPurpose=CucsFcpoolInitiatorEpPurpose, CucsLsmaintChangeMode=CucsLsmaintChangeMode, CucsEquipmentChassisStatsHistThresholded=CucsEquipmentChassisStatsHistThresholded, CucsFirmwareDistributableFsmTaskItem=CucsFirmwareDistributableFsmTaskItem, CucsFabricFcMonFiltRefType=CucsFabricFcMonFiltRefType, CucsEquipmentFexEnvStatsThresholded=CucsEquipmentFexEnvStatsThresholded, CucsExtvmmSwitchDelTaskFsmStageName=CucsExtvmmSwitchDelTaskFsmStageName, CucsFabricFcVsanPortEpSlotId=CucsFabricFcVsanPortEpSlotId, CucsSwPIoEpIfType=CucsSwPIoEpIfType, CucsEtherPauseStatsHistThresholded=CucsEtherPauseStatsHistThresholded, CucsLicenseFileFsmStageName=CucsLicenseFileFsmStageName, CucsBiosVfPCISlotOptionROMEnableVpSlot5State=CucsBiosVfPCISlotOptionROMEnableVpSlot5State, CucsCallhomeAlertGroups=CucsCallhomeAlertGroups, CucsSysfileMutationFsmTaskItem=CucsSysfileMutationFsmTaskItem, CucsDcxOperState=CucsDcxOperState, CucsPortPIoFsmStageName=CucsPortPIoFsmStageName, CucsQosclassEthBEPriority=CucsQosclassEthBEPriority, CucsEquipmentSlotSpanOrientation=CucsEquipmentSlotSpanOrientation, CucsEtherServerIntFIoPcEpIfRole=CucsEtherServerIntFIoPcEpIfRole, CucsLicenseInstanceFsmTaskItem=CucsLicenseInstanceFsmTaskItem, CucsSysdebugCoreFileAdminState=CucsSysdebugCoreFileAdminState, CucsProcessorEnvStatsThresholded=CucsProcessorEnvStatsThresholded, CucsFabricEthEstcPortMode=CucsFabricEthEstcPortMode, CucsFabricFcSanPcEpPortId=CucsFabricFcSanPcEpPortId, CucsFaultPolicyClearAction=CucsFaultPolicyClearAction, CucsFabricEthSourceType=CucsFabricEthSourceType, PYSNMP_MODULE_ID=cucsTextualConventionsObjects, CucsSwCIoEpIfType=CucsSwCIoEpIfType, CucsAdaptorNwMgmtCapMgmtTransport=CucsAdaptorNwMgmtCapMgmtTransport, CucsEtherIntFIoEpType=CucsEtherIntFIoEpType, CucsFabricVnetEpLcCtrlState=CucsFabricVnetEpLcCtrlState, CucsCommWebProto=CucsCommWebProto, CucsVmMgmtPlane=CucsVmMgmtPlane, CucsBiosVfProcessorC3ReportVpProcessorC3Report=CucsBiosVfProcessorC3ReportVpProcessorC3Report, CucsEquipmentBeaconLedFsmCurrentFsm=CucsEquipmentBeaconLedFsmCurrentFsm, CucsStorageFcZoningType=CucsStorageFcZoningType, CucsAdaptorHostFcIfFsmTaskItem=CucsAdaptorHostFcIfFsmTaskItem, CucsSwEthMonFsmCurrentFsm=CucsSwEthMonFsmCurrentFsm, CucsAdaptorMenloEthStatsThresholded=CucsAdaptorMenloEthStatsThresholded, CucsMemoryBufferUnitId=CucsMemoryBufferUnitId, CucsFabricInternalEpAdminState=CucsFabricInternalEpAdminState, CucsCommSyslogClientEnum=CucsCommSyslogClientEnum, CucsFirmwareDownloaderFsmTaskItem=CucsFirmwareDownloaderFsmTaskItem, CucsLicenseDownloadActivity=CucsLicenseDownloadActivity, CucsVnicTemplateTarget=CucsVnicTemplateTarget, CucsEquipmentIOCardId=CucsEquipmentIOCardId, CucsIpServiceIfPref=CucsIpServiceIfPref, CucsEquipmentPsuStatsHistThresholded=CucsEquipmentPsuStatsHistThresholded, CucsBiosVfConsoleRedirectionVpTerminalType=CucsBiosVfConsoleRedirectionVpTerminalType, CucsFabricLanEpType=CucsFabricLanEpType, CucsComputeSlotQualMinId=CucsComputeSlotQualMinId, CucsDiagAdminState=CucsDiagAdminState, CucsSwFabricZoneNsAllocStatus=CucsSwFabricZoneNsAllocStatus, CucsBiosVfPCISlotOptionROMEnableVpSlot4State=CucsBiosVfPCISlotOptionROMEnableVpSlot4State, CucsFabricPIoEpPortId=CucsFabricPIoEpPortId, CucsAaaSession=CucsAaaSession, CucsBiosVfPCISlotOptionROMEnableVpSlot6State=CucsBiosVfPCISlotOptionROMEnableVpSlot6State, CucsGmetaInventoryStatus=CucsGmetaInventoryStatus, CucsSwPeerStatus=CucsSwPeerStatus, CucsVnicFcBaseType=CucsVnicFcBaseType, CucsSwMonSrcEpLocale=CucsSwMonSrcEpLocale, CucsAdaptorExtIfEpType=CucsAdaptorExtIfEpType, CucsFabricDceSwSrvPcEpPortId=CucsFabricDceSwSrvPcEpPortId, CucsSysdebugMEpLogOperState=CucsSysdebugMEpLogOperState, CucsMemoryBufferUnitEnvStatsThresholded=CucsMemoryBufferUnitEnvStatsThresholded, CucsCapabilityOperStatus=CucsCapabilityOperStatus, CucsFabricCIoEpAdminState=CucsFabricCIoEpAdminState, CucsVmLifeCyclePolicyFsmStageName=CucsVmLifeCyclePolicyFsmStageName, CucsNetworkLocale=CucsNetworkLocale, CucsFirmwareDependencyRelationship=CucsFirmwareDependencyRelationship, CucsAdaptorEthPortOutsizedStatsHistThresholded=CucsAdaptorEthPortOutsizedStatsHistThresholded, CucsSysdebugBackupBehaviorProto=CucsSysdebugBackupBehaviorProto, CucsEpqosDefinitionFsmTaskItem=CucsEpqosDefinitionFsmTaskItem, CucsAdaptorExtEthIfPcTransport=CucsAdaptorExtEthIfPcTransport, CucsFabricBladeLifeCycle=CucsFabricBladeLifeCycle, CucsEquipmentLocatorLedFsmCurrentFsm=CucsEquipmentLocatorLedFsmCurrentFsm, CucsExtvmmSwitchDelTaskFsmTaskItem=CucsExtvmmSwitchDelTaskFsmTaskItem, CucsCallhomeAdminState=CucsCallhomeAdminState, CucsAdaptorUnitId=CucsAdaptorUnitId, CucsPkiEpFsmTaskItem=CucsPkiEpFsmTaskItem, CucsEquipmentPictureType=CucsEquipmentPictureType, CucsAdaptorVnicStatsThresholded=CucsAdaptorVnicStatsThresholded, CucsConditionTag=CucsConditionTag, CucsInitiatorFcInitiatorEpProt=CucsInitiatorFcInitiatorEpProt, CucsCapabilityCatalogueFsmStageName=CucsCapabilityCatalogueFsmStageName, CucsEquipmentRemovalConditions=CucsEquipmentRemovalConditions, CucsMgmtCfgExportPolicyFsmStageName=CucsMgmtCfgExportPolicyFsmStageName, CucsEtherSatelliteConnectionDisc=CucsEtherSatelliteConnectionDisc, CucsAaaLdapVendor=CucsAaaLdapVendor, CucsFirmwareImageState=CucsFirmwareImageState, CucsComputePCIeFatalReceiveStatsThresholded=CucsComputePCIeFatalReceiveStatsThresholded, CucsMemoryRuntimeType=CucsMemoryRuntimeType, CucsSwFcMonFsmStageName=CucsSwFcMonFsmStageName, CucsStorageSystemFsmStageName=CucsStorageSystemFsmStageName, CucsSwSystemStatsHistThresholded=CucsSwSystemStatsHistThresholded, CucsVnicL2IfSwitchId=CucsVnicL2IfSwitchId, CucsSysdebugCoreFsmStageName=CucsSysdebugCoreFsmStageName, CucsBiosVfOnboardSATAControllerVpSATAMode=CucsBiosVfOnboardSATAControllerVpSATAMode, CucsOsOsType=CucsOsOsType, CucsProcStatAdminState=CucsProcStatAdminState, CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech=CucsBiosVfIntelTurboBoostTechVpIntelTurboBoostTech, CucsAaaUserInterface=CucsAaaUserInterface, CucsLsPowerState=CucsLsPowerState, CucsSwSanPcType=CucsSwSanPcType, CucsEquipmentChassisId=CucsEquipmentChassisId, CucsSysfileMutationFsmStageName=CucsSysfileMutationFsmStageName, CucsLsbootPurpose=CucsLsbootPurpose, CucsQosHostControl=CucsQosHostControl, CucsAdaptorExternalEpLocale=CucsAdaptorExternalEpLocale, CucsFsmFlags=CucsFsmFlags, CucsFabricFcSanEpSlotId=CucsFabricFcSanEpSlotId, CucsComputeAvailability=CucsComputeAvailability, CucsHostimgComposition=CucsHostimgComposition, CucsFabricEthMonLanTransport=CucsFabricEthMonLanTransport, CucsNfsMountDefFsmCurrentFsm=CucsNfsMountDefFsmCurrentFsm, CucsFabricLifeCycle=CucsFabricLifeCycle, CucsBiosVfPOSTErrorPauseVpPOSTErrorPause=CucsBiosVfPOSTErrorPauseVpPOSTErrorPause, CucsFabricSwSrvEpIfRole=CucsFabricSwSrvEpIfRole, CucsAdaptorHostVisibility=CucsAdaptorHostVisibility, CucsComputeServerMgmtDiscAction=CucsComputeServerMgmtDiscAction, CucsFabricSanCloudFsmCurrentFsm=CucsFabricSanCloudFsmCurrentFsm, CucsAaaSessionState=CucsAaaSessionState, CucsPolicyPolicyResolveType=CucsPolicyPolicyResolveType, CucsFabricFcMonFiltEpType=CucsFabricFcMonFiltEpType, CucsIdentRetStatus=CucsIdentRetStatus, CucsIqnpoolBlockTo=CucsIqnpoolBlockTo, CucsStorageAllocState=CucsStorageAllocState, CucsFabricVnetEpSyncEpFsmCurrentFsm=CucsFabricVnetEpSyncEpFsmCurrentFsm, CucsDcxAdminState=CucsDcxAdminState, CucsStatsThr64ValuePropType=CucsStatsThr64ValuePropType, CucsQosclassEthClassifiedAdminState=CucsQosclassEthClassifiedAdminState, CucsSwEthMonFsmStageName=CucsSwEthMonFsmStageName, CucsBiosVfPCISlotOptionROMEnableVpSlot2State=CucsBiosVfPCISlotOptionROMEnableVpSlot2State, CucsCommNtpProviderAdminState=CucsCommNtpProviderAdminState, CucsFirmwareEquipmentType=CucsFirmwareEquipmentType, CucsLsAssocState=CucsLsAssocState, CucsEquipmentNetworkElementFanStatsHistThresholded=CucsEquipmentNetworkElementFanStatsHistThresholded, CucsSwEthMonFsmTaskItem=CucsSwEthMonFsmTaskItem, CucsAdaptorMenloQErrorStatsHistThresholded=CucsAdaptorMenloQErrorStatsHistThresholded, CucsBiosVfOnboardSATAControllerVpOnboardSATAController=CucsBiosVfOnboardSATAControllerVpOnboardSATAController, CucsAdaptorCapDefFwVersionOpr=CucsAdaptorCapDefFwVersionOpr, CucsMgmtEntityProblems=CucsMgmtEntityProblems, CucsFirmwareDownloaderFsmStageName=CucsFirmwareDownloaderFsmStageName, CucsFabricEthEstcTransport=CucsFabricEthEstcTransport, CucsAaaSshStr=CucsAaaSshStr, CucsPowerCapAction=CucsPowerCapAction, CucsVnicEtherType=CucsVnicEtherType, CucsDiagNetworkTestType=CucsDiagNetworkTestType, CucsEtherServerIntFIoPcType=CucsEtherServerIntFIoPcType, CucsNetworkInventoryStatus=CucsNetworkInventoryStatus, CucsComputeChassisConnPolicyChassisId=CucsComputeChassisConnPolicyChassisId, CucsCommSyslogForwardingFacility=CucsCommSyslogForwardingFacility, CucsTrigAckChangeDetails=CucsTrigAckChangeDetails, CucsAaaRealm=CucsAaaRealm, CucsExtvmmKeyStoreFsmStageName=CucsExtvmmKeyStoreFsmStageName, CucsPkiCertStatus=CucsPkiCertStatus, CucsEquipmentIOCardFsmTaskItem=CucsEquipmentIOCardFsmTaskItem, CucsSysfileMutationFsmCurrentFsm=CucsSysfileMutationFsmCurrentFsm, CucsVmHvClInstType=CucsVmHvClInstType, CucsEquipmentRackUnitFanStatsHistThresholded=CucsEquipmentRackUnitFanStatsHistThresholded, CucsVnicIpcType=CucsVnicIpcType, CucsLicenseScope=CucsLicenseScope, CucsSwEthLanBorderFsmStageName=CucsSwEthLanBorderFsmStageName, CucsCallhomeAlertMessageType=CucsCallhomeAlertMessageType)
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", CucsProcessorUnitArch=CucsProcessorUnitArch, CucsStatsThrFloatValuePropType=CucsStatsThrFloatValuePropType, CucsComputeAdminPowerState=CucsComputeAdminPowerState, CucsPortEncap=CucsPortEncap, CucsEtherServerIntFIoPcTransport=CucsEtherServerIntFIoPcTransport, CucsFirmwareImageFsmCurrentFsm=CucsFirmwareImageFsmCurrentFsm, CucsPolicyRegistrationStateType=CucsPolicyRegistrationStateType, CucsBiosBootDevGrpType=CucsBiosBootDevGrpType, CucsFabricLanPcIfRole=CucsFabricLanPcIfRole, CucsHostimgImgType=CucsHostimgImgType, CucsBiosDefaultAction=CucsBiosDefaultAction, CucsFabricEthEstcPcTransport=CucsFabricEthEstcPcTransport, CucsCommSyslogFileSize=CucsCommSyslogFileSize, CucsComputePsuRedundancy=CucsComputePsuRedundancy, CucsExtmgmtMiiStatusMaxRetryCount=CucsExtmgmtMiiStatusMaxRetryCount, CucsFabricAEthEstcEpTransport=CucsFabricAEthEstcEpTransport, CucsFabricFcVsanPortEpPortId=CucsFabricFcVsanPortEpPortId, CucsSysdebugTSCmdOptMajorType=CucsSysdebugTSCmdOptMajorType, CucsComputeAssociation=CucsComputeAssociation, CucsHostimgDistribution=CucsHostimgDistribution, CucsAdaptorIscsiProtDhcpTimeOut=CucsAdaptorIscsiProtDhcpTimeOut, CucsVnicFcBasePersBind=CucsVnicFcBasePersBind, CucsFabricPIoEpSlotId=CucsFabricPIoEpSlotId, CucsStatsThr32ValuePropType=CucsStatsThr32ValuePropType, CucsFabricFcVsanPcTransport=CucsFabricFcVsanPcTransport, CucsComputeChassisQualMaxId=CucsComputeChassisQualMaxId, CucsPkiEpFsmCurrentFsm=CucsPkiEpFsmCurrentFsm, CucsConfigSorterDirection=CucsConfigSorterDirection, CucsVmLifeCyclePolicyFsmTaskItem=CucsVmLifeCyclePolicyFsmTaskItem, CucsLsFcZoneGroupSwitchId=CucsLsFcZoneGroupSwitchId, CucsFabricEthMonType=CucsFabricEthMonType, CucsStorageFileSystemStatus=CucsStorageFileSystemStatus, CucsExtvmmMasterExtKeyFsmCurrentFsm=CucsExtvmmMasterExtKeyFsmCurrentFsm, CucsFabricAdminState=CucsFabricAdminState, CucsExtpolProviderFsmTaskItem=CucsExtpolProviderFsmTaskItem, CucsCallhomeAlertGroup=CucsCallhomeAlertGroup, CucsBiosVfQuietBootVpQuietBoot=CucsBiosVfQuietBootVpQuietBoot, CucsFabricEthEstcType=CucsFabricEthEstcType, CucsFabricFcSanTransport=CucsFabricFcSanTransport, CucsSwAccessEpTransport=CucsSwAccessEpTransport, CucsFabricComputeSlotEpFsmStageName=CucsFabricComputeSlotEpFsmStageName, CucsFabricVlanSwitchId=CucsFabricVlanSwitchId, CucsAdaptorIpV4RssHashProfileTcpHash=CucsAdaptorIpV4RssHashProfileTcpHash, CucsSysdebugEpLogCapacity=CucsSysdebugEpLogCapacity, CucsFabricFcSourceType=CucsFabricFcSourceType, CucsFirmwareHostPackConfigQualifier=CucsFirmwareHostPackConfigQualifier, CucsFabricEstcPcType=CucsFabricEstcPcType, CucsFabricTrafficDirection=CucsFabricTrafficDirection, CucsVnicSanConnTemplTarget=CucsVnicSanConnTemplTarget, CucsFabricEpMgrFsmCurrentFsm=CucsFabricEpMgrFsmCurrentFsm, CucsEquipmentPsuStateQualifier=CucsEquipmentPsuStateQualifier, CucsVnicIfOperState=CucsVnicIfOperState, CucsSwConfigStatus=CucsSwConfigStatus, CucsBiosVfLvDIMMSupportVpLvDDRMode=CucsBiosVfLvDIMMSupportVpLvDDRMode, CucsAdaptorReachability=CucsAdaptorReachability, CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing=CucsBiosVfCoreMultiProcessingVpCoreMultiProcessing, CucsEquipmentChassisIssues=CucsEquipmentChassisIssues, CucsFcpoolBootTargetType=CucsFcpoolBootTargetType, CucsLicenseDownloaderFsmCurrentFsm=CucsLicenseDownloaderFsmCurrentFsm, CucsVnicIScsiNodeOwner=CucsVnicIScsiNodeOwner, CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule=CucsBiosVfUCSMBootOrderRuleControlVpUCSMBootOrderRule, CucsAdaptorIScsiCapBootOrderType=CucsAdaptorIScsiCapBootOrderType, CucsCommTimeZoneConfigState=CucsCommTimeZoneConfigState, CucsTrigAckChanges=CucsTrigAckChanges, CucsFabricEstcEpIfRole=CucsFabricEstcEpIfRole, CucsExtmgmtMiiStatusRetryInterval=CucsExtmgmtMiiStatusRetryInterval, CucsEtherInternalPcLocale=CucsEtherInternalPcLocale, CucsStorageSystemFsmTaskItem=CucsStorageSystemFsmTaskItem, CucsBiosVfMirroringModeVpMirroringMode=CucsBiosVfMirroringModeVpMirroringMode, CucsQosclassFcAdminState=CucsQosclassFcAdminState, CucsFabricLanEpIfRole=CucsFabricLanEpIfRole, CucsEquipmentFanStatsHistThresholded=CucsEquipmentFanStatsHistThresholded, CucsFabricComputeEpType=CucsFabricComputeEpType, CucsPolicyControlSource=CucsPolicyControlSource, CucsEquipmentLedLocatorState=CucsEquipmentLedLocatorState, CucsFabricDceSwSrvPcEpSlotId=CucsFabricDceSwSrvPcEpSlotId, CucsEquipmentLedOperState=CucsEquipmentLedOperState, CucsSwLanPcIfRole=CucsSwLanPcIfRole, CucsMgmtBackupPolicyFsmStageName=CucsMgmtBackupPolicyFsmStageName, CucsBiosVfSriovConfigVpSriov=CucsBiosVfSriovConfigVpSriov, CucsHostagAction=CucsHostagAction, CucsPowerGroupState=CucsPowerGroupState, CucsEquipmentResetOn=CucsEquipmentResetOn, CucsEquipmentLocatorLedFsmStageName=CucsEquipmentLocatorLedFsmStageName, CucsHostimgType=CucsHostimgType, CucsQosclassDefinitionFsmStageName=CucsQosclassDefinitionFsmStageName, CucsCommHttpRedirectState=CucsCommHttpRedirectState, CucsLsServerFsmCurrentFsm=CucsLsServerFsmCurrentFsm, CucsFabricFcZoneSharingMode=CucsFabricFcZoneSharingMode, CucsPowerMemberState=CucsPowerMemberState, CucsSwUlanPurpose=CucsSwUlanPurpose, CucsConditionCause=CucsConditionCause, CucsCommProtocol=CucsCommProtocol, CucsPolicyControlEpFsmCurrentFsm=CucsPolicyControlEpFsmCurrentFsm, CucsEtherCIoEpIfType=CucsEtherCIoEpIfType, CucsLsComputeBindingOperState=CucsLsComputeBindingOperState, CucsEquipmentChassisPowerOperState=CucsEquipmentChassisPowerOperState, CucsFabricConfMode=CucsFabricConfMode, CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport=CucsBiosVfIntelVTForDirectedIOVpIntelVTDPassThroughDMASupport, CucsFabricVsanSwitchId=CucsFabricVsanSwitchId, CucsCallhomeEpFsmTaskItem=CucsCallhomeEpFsmTaskItem, CucsComputePooledRackUnitId=CucsComputePooledRackUnitId, CucsExtpolEpFsmStageName=CucsExtpolEpFsmStageName, CucsVnicInstantiation=CucsVnicInstantiation, CucsSwEthEstcPcTransport=CucsSwEthEstcPcTransport, CucsTrigAckMode=CucsTrigAckMode, CucsSwFcMonType=CucsSwFcMonType, CucsBiosVfDirectCacheAccessVpDirectCacheAccess=CucsBiosVfDirectCacheAccessVpDirectCacheAccess, CucsExtvmmSwitchDelTaskFsmCurrentFsm=CucsExtvmmSwitchDelTaskFsmCurrentFsm, CucsStorageConfiguration=CucsStorageConfiguration, CucsMemoryUnitId=CucsMemoryUnitId, CucsFabricInternalPcLocale=CucsFabricInternalPcLocale, CucsAdaptorExtEthIfPcEpSlotId=CucsAdaptorExtEthIfPcEpSlotId, CucsVnicIPv4DnsPref=CucsVnicIPv4DnsPref, CucsFirmwareDependencyScope=CucsFirmwareDependencyScope, CucsAdaptorEthPortErrStatsHistThresholded=CucsAdaptorEthPortErrStatsHistThresholded, CucsComputeScrubAction=CucsComputeScrubAction, CucsFabricEthMonDestEpAdminSpeed=CucsFabricEthMonDestEpAdminSpeed, CucsLsType=CucsLsType, CucsFabricAFcEstcEpTransport=CucsFabricAFcEstcEpTransport, CucsStorageRaidType=CucsStorageRaidType, CucsMemoryType=CucsMemoryType, CucsFabricSwitchingMode=CucsFabricSwitchingMode, CucsBiosVfPCISlotOptionROMEnableVpSlot3State=CucsBiosVfPCISlotOptionROMEnableVpSlot3State, CucsSysdebugBackupFormat=CucsSysdebugBackupFormat, CucsAdaptorMenloFcErrorStatsHistThresholded=CucsAdaptorMenloFcErrorStatsHistThresholded, CucsSysdebugTechSupportAdminState=CucsSysdebugTechSupportAdminState, CucsNetworkPortOperState=CucsNetworkPortOperState, CucsComputeRackUnitFsmStageName=CucsComputeRackUnitFsmStageName, CucsEquipmentFexFsmCurrentFsm=CucsEquipmentFexFsmCurrentFsm, CucsLsbootVirtualMediaType=CucsLsbootVirtualMediaType, CucsNetworkSwitchId=CucsNetworkSwitchId, CucsMgmtEntityUmbilicalState=CucsMgmtEntityUmbilicalState, CucsAdaptorMenloEthErrorStatsHistThresholded=CucsAdaptorMenloEthErrorStatsHistThresholded, CucsStatsCollectionPolicyFsmCurrentFsm=CucsStatsCollectionPolicyFsmCurrentFsm, CucsCallhomeUrgency=CucsCallhomeUrgency, CucsProcessorRuntimeHistThresholded=CucsProcessorRuntimeHistThresholded, CucsFabricEthMonFiltEpType=CucsFabricEthMonFiltEpType, CucsFirmwareImpactType=CucsFirmwareImpactType, CucsAdaptorEtherIfStatsThresholded=CucsAdaptorEtherIfStatsThresholded, CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport=CucsBiosVfOnboardStorageVpOnboardSCUStorageSupport, CucsFabricFcoeEstcEpPortId=CucsFabricFcoeEstcEpPortId, CucsGmetaPollInterval=CucsGmetaPollInterval, CucsAdaptorLinkState=CucsAdaptorLinkState, CucsSwAccessDomainFsmCurrentFsm=CucsSwAccessDomainFsmCurrentFsm, CucsFabricEthEstcEpType=CucsFabricEthEstcEpType, CucsFcpoolInitiatorsAssignmentOrder=CucsFcpoolInitiatorsAssignmentOrder, CucsSysfileExporterPostAction=CucsSysfileExporterPostAction, CucsEquipmentDiscoveryState=CucsEquipmentDiscoveryState, CucsFirmwareUpgradeSeverity=CucsFirmwareUpgradeSeverity, CucsComputeBladeFsmStageName=CucsComputeBladeFsmStageName, CucsMemoryFormFactor=CucsMemoryFormFactor, CucsStorageLocalDiskConfigFlexFlashRAIDReportingState=CucsStorageLocalDiskConfigFlexFlashRAIDReportingState, CucsNfsMntOperState=CucsNfsMntOperState, CucsEtherErrStatsThresholded=CucsEtherErrStatsThresholded, CucsFirmwareTransferState=CucsFirmwareTransferState, CucsPkiModulus=CucsPkiModulus, CucsAdaptorMenloStatsIndex=CucsAdaptorMenloStatsIndex, CucsEtherServerIntFIoPcPortId=CucsEtherServerIntFIoPcPortId, CucsObserveObservedFsmTaskItem=CucsObserveObservedFsmTaskItem, CucsAaaRadiusEpFsmStageName=CucsAaaRadiusEpFsmStageName, CucsFabricVConMappingScheme=CucsFabricVConMappingScheme, CucsSysdebugLogControlDomainEnum=CucsSysdebugLogControlDomainEnum, CucsCommSyslogAdminState=CucsCommSyslogAdminState, CucsComputeMbPowerStatsThresholded=CucsComputeMbPowerStatsThresholded, CucsFabricComputeSlotEpSlotId=CucsFabricComputeSlotEpSlotId, CucsEquipmentFabricEpType=CucsEquipmentFabricEpType, CucsFirmwareSystemFsmTaskItem=CucsFirmwareSystemFsmTaskItem, CucsMgmtUpgradeStatus=CucsMgmtUpgradeStatus, CucsSysdebugTechSupportOperState=CucsSysdebugTechSupportOperState, CucsIppoolPoolAssignmentOrder=CucsIppoolPoolAssignmentOrder, CucsBiosVfCPUPerformanceVpCPUPerformance=CucsBiosVfCPUPerformanceVpCPUPerformance, CucsComputeMemoryUnitConstraintType=CucsComputeMemoryUnitConstraintType, CucsCapabilityCatalogueFsmCurrentFsm=CucsCapabilityCatalogueFsmCurrentFsm, CucsMemoryErrorStatsThresholded=CucsMemoryErrorStatsThresholded, CucsBmcSELCntEqptInstIdPropId=CucsBmcSELCntEqptInstIdPropId, CucsMgmtEntityState=CucsMgmtEntityState, CucsAdaptorOffloadMethod=CucsAdaptorOffloadMethod, CucsConditionCode=CucsConditionCode, CucsSwFcSanMonTransport=CucsSwFcSanMonTransport, CucsPowerReqConflict=CucsPowerReqConflict, CucsMgmtImporterFsmTaskItem=CucsMgmtImporterFsmTaskItem, CucsEtherSwitchIntFIoType=CucsEtherSwitchIntFIoType, CucsBiosVfOptionROMEnableVpState=CucsBiosVfOptionROMEnableVpState, CucsLsbootVirtualMediaAccess=CucsLsbootVirtualMediaAccess, CucsConditionRemoteInvRslt=CucsConditionRemoteInvRslt, CucsFirmwareItemType=CucsFirmwareItemType, CucsComputeCheckPoint=CucsComputeCheckPoint, CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock=CucsBiosVfUSBFrontPanelAccessLockVpUSBFrontPanelLock, CucsEquipmentSensorThresholdStatus=CucsEquipmentSensorThresholdStatus, CucsSwEthTargetEpTransport=CucsSwEthTargetEpTransport, CucsLsbootSanImagePathType=CucsLsbootSanImagePathType, CucsIpProtocol=CucsIpProtocol, CucsEquipmentFexFsmStageName=CucsEquipmentFexFsmStageName, CucsAdaptorNwMgmtCapApi=CucsAdaptorNwMgmtCapApi, CucsAdaptorPurpose=CucsAdaptorPurpose, CucsFabricVlanOperState=CucsFabricVlanOperState, CucsBiosVfSparingModeVpSparingMode=CucsBiosVfSparingModeVpSparingMode, CucsMacpoolPoolAssignmentOrder=CucsMacpoolPoolAssignmentOrder, CucsSwSanMonType=CucsSwSanMonType, CucsMgmtBackupFsmStageName=CucsMgmtBackupFsmStageName, CucsEtherSwitchIntFIoPcPortId=CucsEtherSwitchIntFIoPcPortId, CucsAdaptorHostFcIfFsmCurrentFsm=CucsAdaptorHostFcIfFsmCurrentFsm, CucsSwEthMonTransport=CucsSwEthMonTransport, CucsComputeConnectivityRebalancing=CucsComputeConnectivityRebalancing, CucsAdaptorIpV6RssHashProfileTcpHash=CucsAdaptorIpV6RssHashProfileTcpHash, CucsCommSyslogProto=CucsCommSyslogProto, CucsMgmtControllerFsmCurrentFsm=CucsMgmtControllerFsmCurrentFsm, CucsEquipmentChassisConfigProgressIndicator=CucsEquipmentChassisConfigProgressIndicator, CucsInitiatorInitiatorEpPref=CucsInitiatorInitiatorEpPref, CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport=CucsBiosVfIntelVTForDirectedIOVpIntelVTDCoherencySupport, CucsFabricNetGroupType=CucsFabricNetGroupType, CucsTrigAdminState=CucsTrigAdminState, CucsFabricStatus=CucsFabricStatus, CucsSysdebugEpLogAdminState=CucsSysdebugEpLogAdminState, CucsAdaptorExtEthIfFsmTaskItem=CucsAdaptorExtEthIfFsmTaskItem, CucsEquipmentSlotArrayLocation=CucsEquipmentSlotArrayLocation, CucsEquipmentPsuInputStatsThresholded=CucsEquipmentPsuInputStatsThresholded, CucsAdaptorHostFcIfFsmStageName=CucsAdaptorHostFcIfFsmStageName, CucsIscsiProtocolProfileDhcpTimeOut=CucsIscsiProtocolProfileDhcpTimeOut, CucsFabricAFcoeEstcEpIfRole=CucsFabricAFcoeEstcEpIfRole, CucsFabricAVlanSharing=CucsFabricAVlanSharing, CucsStorageIniGroupOperProtocol=CucsStorageIniGroupOperProtocol, CucsSwBorderPcLocale=CucsSwBorderPcLocale, CucsBiosVfProcessorCStateVpProcessorCState=CucsBiosVfProcessorCStateVpProcessorCState, CucsVnicProfileSetFsmTaskItem=CucsVnicProfileSetFsmTaskItem, CucsCommSnmpV3Privilege=CucsCommSnmpV3Privilege, CucsSysdebugManualCoreFileExportTargetFsmStageName=CucsSysdebugManualCoreFileExportTargetFsmStageName, CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo=CucsBiosVfUEFIOSUseLegacyVideoVpUEFIOSUseLegacyVideo, CucsFabricSanEpType=CucsFabricSanEpType, CucsAaaExtMgmtAccess=CucsAaaExtMgmtAccess, CucsAdaptorEthInterruptProfileCoalescingType=CucsAdaptorEthInterruptProfileCoalescingType, CucsAdaptorMenloMcpuStatsThresholded=CucsAdaptorMenloMcpuStatsThresholded, CucsSwFcSanBorderFsmCurrentFsm=CucsSwFcSanBorderFsmCurrentFsm, CucsAdaptorFcErrorRecoveryProfileFcpErrorRecovery=CucsAdaptorFcErrorRecoveryProfileFcpErrorRecovery, CucsPolicyPolicyScopeFsmTaskItem=CucsPolicyPolicyScopeFsmTaskItem, CucsAdaptorHostFcIfPersBind=CucsAdaptorHostFcIfPersBind, CucsEquipmentRackUnitPsuStatsThresholded=CucsEquipmentRackUnitPsuStatsThresholded, CucsEquipmentIOCardFsmStageName=CucsEquipmentIOCardFsmStageName, CucsComputeChassisDiscAction=CucsComputeChassisDiscAction, CucsAdaptorCapSpecType=CucsAdaptorCapSpecType, CucsMgmtBackupType=CucsMgmtBackupType, CucsFlowctrlPriorityPause=CucsFlowctrlPriorityPause, CucsComputePhysicalFsmTaskFlags=CucsComputePhysicalFsmTaskFlags, CucsFirmwareDistributableFsmCurrentFsm=CucsFirmwareDistributableFsmCurrentFsm, CucsVmHbaType=CucsVmHbaType, CucsFirmwareImageFsmTaskItem=CucsFirmwareImageFsmTaskItem, CucsComputeDiscovery=CucsComputeDiscovery, CucsLicenseTransport=CucsLicenseTransport, CucsDcxState=CucsDcxState, CucsStorageControllerType=CucsStorageControllerType, CucsPolicyRepairStateType=CucsPolicyRepairStateType, CucsBiosVfPackageCStateLimitVpPackageCStateLimit=CucsBiosVfPackageCStateLimitVpPackageCStateLimit, CucsFabricFcEstcEpSlotId=CucsFabricFcEstcEpSlotId)
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", CucsMgmtImporterFsmCurrentFsm=CucsMgmtImporterFsmCurrentFsm, CucsSwEthLanBorderFsmTaskFlags=CucsSwEthLanBorderFsmTaskFlags, CucsPolicyPolicyOperStatus=CucsPolicyPolicyOperStatus, CucsFabricVnetEpSyncEpFsmTaskItem=CucsFabricVnetEpSyncEpFsmTaskItem, CucsFabricEthMonSrcEpType=CucsFabricEthMonSrcEpType, CucsAdaptorFcIfFC4StatsHistThresholded=CucsAdaptorFcIfFC4StatsHistThresholded, CucsPolicyResumeAckState=CucsPolicyResumeAckState, CucsEtherFcoeInterfaceStatsHistThresholded=CucsEtherFcoeInterfaceStatsHistThresholded, CucsComputeBladeFsmTaskFlags=CucsComputeBladeFsmTaskFlags, CucsEquipmentFexPsuInputStatsThresholded=CucsEquipmentFexPsuInputStatsThresholded, CucsDiagFailureAction=CucsDiagFailureAction, CucsStorageTargetPath=CucsStorageTargetPath, CucsNetworkPortType=CucsNetworkPortType, CucsComputeRackQualMinId=CucsComputeRackQualMinId, CucsIdentMetaSystemFsmStageName=CucsIdentMetaSystemFsmStageName, CucsSysdebugBackupBehaviorInterval=CucsSysdebugBackupBehaviorInterval, CucsNetworkOperLevelNumPrimaryVlansStatus=CucsNetworkOperLevelNumPrimaryVlansStatus, CucsAdaptorIpV6RssHashProfileIpHash=CucsAdaptorIpV6RssHashProfileIpHash, CucsEquipmentStorageMethod=CucsEquipmentStorageMethod, CucsLsFcZoneState=CucsLsFcZoneState, CucsFabricSwChEpIfRole=CucsFabricSwChEpIfRole, CucsVnicScsiType=CucsVnicScsiType, CucsEtherServerIntFIoTransport=CucsEtherServerIntFIoTransport, CucsQosPriority=CucsQosPriority, CucsSolSpeed=CucsSolSpeed, CucsEventEpCtrlLevel=CucsEventEpCtrlLevel, CucsEtherSwitchIntFIoPcTransport=CucsEtherSwitchIntFIoPcTransport, CucsFabricEthLanPcTransport=CucsFabricEthLanPcTransport, CucsCommSmashCLPProto=CucsCommSmashCLPProto, CucsStorageLunType=CucsStorageLunType, CucsIdentIdentRequestFsmStageName=CucsIdentIdentRequestFsmStageName, CucsFirmwareImageFsmStageName=CucsFirmwareImageFsmStageName, CucsNfsPurpose=CucsNfsPurpose, CucsVnicProfileSetFsmStageName=CucsVnicProfileSetFsmStageName, CucsSwPhysFsmStageName=CucsSwPhysFsmStageName, CucsFabricEthMonSrcRefType=CucsFabricEthMonSrcRefType, CucsExtvmmKeyStoreFsmCurrentFsm=CucsExtvmmKeyStoreFsmCurrentFsm, CucsMemoryVisibility=CucsMemoryVisibility, CucsFcpoolInitiatorPurpose=CucsFcpoolInitiatorPurpose, CucsFabricFcoeVsanPortEpPortId=CucsFabricFcoeVsanPortEpPortId, CucsCommSvcEpFsmTaskItem=CucsCommSvcEpFsmTaskItem, CucsFabricFcMonTransport=CucsFabricFcMonTransport, CucsFsmLifecycle=CucsFsmLifecycle, CucsAdaptorExtEthIfPcEpPortId=CucsAdaptorExtEthIfPcEpPortId, CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout=CucsBiosVfOSBootWatchdogTimerTimeoutVpOSBootWatchdogTimerTimeout, CucsFabricFcEstcTransport=CucsFabricFcEstcTransport, CucsAdaptorExtEthIfFsmCurrentFsm=CucsAdaptorExtEthIfFsmCurrentFsm, CucsAaaRealmFsmTaskItem=CucsAaaRealmFsmTaskItem, CucsFabricFcMonDestEpAdminSpeed=CucsFabricFcMonDestEpAdminSpeed, CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer=CucsBiosVfOSBootWatchdogTimerVpOSBootWatchdogTimer, CucsAaaLdapGroupRuleAuthorization=CucsAaaLdapGroupRuleAuthorization, CucsFabricEthVlanPortEpVlanStatus=CucsFabricEthVlanPortEpVlanStatus, CucsIdentMetaSystemFsmCurrentFsm=CucsIdentMetaSystemFsmCurrentFsm, CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss=CucsBiosVfResumeOnACPowerLossVpResumeOnACPowerLoss, CucsFsmFsmStageStatus=CucsFsmFsmStageStatus, CucsEtherLossStatsHistThresholded=CucsEtherLossStatsHistThresholded, CucsSysdebugManualCoreFileExportTargetProto=CucsSysdebugManualCoreFileExportTargetProto, CucsSwEthLanMonTransport=CucsSwEthLanMonTransport, CucsFabricDceSwSrvEpPortId=CucsFabricDceSwSrvEpPortId, CucsSwUtilityDomainFsmStageName=CucsSwUtilityDomainFsmStageName, CucsLsbootIScsiImagePathType=CucsLsbootIScsiImagePathType, CucsFirmwareImagePresence=CucsFirmwareImagePresence, CucsComputePCIeFatalCompletionStatsThresholded=CucsComputePCIeFatalCompletionStatsThresholded, CucsFabricEstcPcIfRole=CucsFabricEstcPcIfRole, CucsDiagSrvCtrlType=CucsDiagSrvCtrlType, CucsStorageLocalDiskPartitionType=CucsStorageLocalDiskPartitionType, CucsFirmwareInstallState=CucsFirmwareInstallState, CucsFabricTargetStatus=CucsFabricTargetStatus, CucsBiosVfFrontPanelLockoutVpFrontPanelLockout=CucsBiosVfFrontPanelLockoutVpFrontPanelLockout, CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO=CucsBiosVfIntelVTForDirectedIOVpIntelVTForDirectedIO, CucsAdaptorMenloNetEgStatsHistThresholded=CucsAdaptorMenloNetEgStatsHistThresholded, CucsUuidpoolPoolAssignmentOrder=CucsUuidpoolPoolAssignmentOrder, CucsFabricEpMgrFsmStageName=CucsFabricEpMgrFsmStageName, CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy=CucsBiosVfOSBootWatchdogTimerPolicyVpOSBootWatchdogTimerPolicy, CucsAdaptorMenloMcpuErrorStatsHistThresholded=CucsAdaptorMenloMcpuErrorStatsHistThresholded, CucsStorageBatteryType=CucsStorageBatteryType, CucsFabricSwSrvEpType=CucsFabricSwSrvEpType, CucsEquipmentRackUnitFanStatsThresholded=CucsEquipmentRackUnitFanStatsThresholded, CucsFabricPIoEpOperState=CucsFabricPIoEpOperState, CucsEtherSwitchIntFIoPcType=CucsEtherSwitchIntFIoPcType, CucsFabricAFcoeEstcEpTransport=CucsFabricAFcoeEstcEpTransport, CucsIscsiProtocolProfileConnectionTimeOut=CucsIscsiProtocolProfileConnectionTimeOut, CucsComputeLinkAggregation=CucsComputeLinkAggregation, CucsAdaptorEthPortMcastStatsThresholded=CucsAdaptorEthPortMcastStatsThresholded, CucsExtpolRegistryFsmTaskItem=CucsExtpolRegistryFsmTaskItem, CucsVnicDefaultAction=CucsVnicDefaultAction, CucsEquipmentChassisConfigState=CucsEquipmentChassisConfigState, CucsComputePhysicalLowVoltageMemory=CucsComputePhysicalLowVoltageMemory, CucsSwVlanPortNsAllocStatus=CucsSwVlanPortNsAllocStatus, CucsFabricEpMgrFsmTaskItem=CucsFabricEpMgrFsmTaskItem, CucsAdaptorMenloNetInStatsHistThresholded=CucsAdaptorMenloNetInStatsHistThresholded, CucsFirmwareCatalogPackConfigState=CucsFirmwareCatalogPackConfigState, CucsFabricVConTransportPref=CucsFabricVConTransportPref, CucsComputeIssues=CucsComputeIssues, CucsStorageIniGroupProtocol=CucsStorageIniGroupProtocol, CucsCapabilityMgmtExtensionFsmStageName=CucsCapabilityMgmtExtensionFsmStageName, CucsAdaptorEthOffloadProfileLargeReceive=CucsAdaptorEthOffloadProfileLargeReceive, CucsComputeRackUnitFsmTaskItem=CucsComputeRackUnitFsmTaskItem, CucsGmetaHolderFsmTaskItem=CucsGmetaHolderFsmTaskItem, CucsVmStatus=CucsVmStatus, CucsAdaptorEthPortOutsizedStatsThresholded=CucsAdaptorEthPortOutsizedStatsThresholded, CucsAdaptorExtEthIfFsmStageName=CucsAdaptorExtEthIfFsmStageName, CucsAdaptorMenloMcpuErrorStatsThresholded=CucsAdaptorMenloMcpuErrorStatsThresholded, CucsAdaptorMenloFcStatsHistThresholded=CucsAdaptorMenloFcStatsHistThresholded, CucsLsbootLanImagePathType=CucsLsbootLanImagePathType, CucsSwMonAdminState=CucsSwMonAdminState, CucsLsApply=CucsLsApply, CucsBiosVfConsoleRedirectionVpConsoleRedirection=CucsBiosVfConsoleRedirectionVpConsoleRedirection, CucsComputeAdminState=CucsComputeAdminState, CucsLicenseInstanceFsmCurrentFsm=CucsLicenseInstanceFsmCurrentFsm, CucsLsbootLanType=CucsLsbootLanType, CucsPortEthSpeed=CucsPortEthSpeed, CucsSwPhysFsmTaskItem=CucsSwPhysFsmTaskItem, CucsCapabilityPlatform=CucsCapabilityPlatform, CucsBiosVfProcessorC7ReportVpProcessorC7Report=CucsBiosVfProcessorC7ReportVpProcessorC7Report, CucsGmetaCategory=CucsGmetaCategory, CucsQosclassDefinitionFsmCurrentFsm=CucsQosclassDefinitionFsmCurrentFsm, CucsEquipmentFexPowerSummaryHistThresholded=CucsEquipmentFexPowerSummaryHistThresholded, CucsTrigAckOperState=CucsTrigAckOperState, CucsFirmwareImageError=CucsFirmwareImageError, CucsEquipmentPowerState=CucsEquipmentPowerState, CucsOrgSrcMask=CucsOrgSrcMask, CucsCapabilityFeatureStatus=CucsCapabilityFeatureStatus, CucsSwFcMonDestEpTransport=CucsSwFcMonDestEpTransport, CucsFabricEthVlanPcTransport=CucsFabricEthVlanPcTransport, CucsComputePsuControlRedundancy=CucsComputePsuControlRedundancy, CucsHostagAgentType=CucsHostagAgentType, CucsSysdebugManualCoreFileExportTargetAdminState=CucsSysdebugManualCoreFileExportTargetAdminState, CucsEquipmentChassisFsmCurrentFsm=CucsEquipmentChassisFsmCurrentFsm, CucsHostagEvent=CucsHostagEvent, CucsLicenseFileFsmTaskItem=CucsLicenseFileFsmTaskItem, CucsFabricAFcoeEstcEpType=CucsFabricAFcoeEstcEpType, CucsEquipmentLocatorLedFsmTaskItem=CucsEquipmentLocatorLedFsmTaskItem, CucsEquipmentPsuId=CucsEquipmentPsuId, CucsVnicConnectionType=CucsVnicConnectionType, CucsExtvmmProviderFsmCurrentFsm=CucsExtvmmProviderFsmCurrentFsm, CucsSwFcMonFsmTaskItem=CucsSwFcMonFsmTaskItem, CucsVnicDynamicConReqProtection=CucsVnicDynamicConReqProtection, CucsFcpoolInitiatorsPurpose=CucsFcpoolInitiatorsPurpose, CucsQosclassEthClassifiedDrop=CucsQosclassEthClassifiedDrop, CucsAdaptorExternalPcLocale=CucsAdaptorExternalPcLocale, CucsSysdebugEpLogBackupAction=CucsSysdebugEpLogBackupAction, CucsFabricEpMgrFsmTaskFlags=CucsFabricEpMgrFsmTaskFlags, CucsAdaptorFcIfFC4StatsThresholded=CucsAdaptorFcIfFC4StatsThresholded, CucsEtherExternalEpAdminState=CucsEtherExternalEpAdminState, CucsCommSyslogSeverity=CucsCommSyslogSeverity, CucsEquipmentSlotStatus=CucsEquipmentSlotStatus, CucsNetworkIfStatsUnits=CucsNetworkIfStatsUnits, CucsFabricExternalEpAdminState=CucsFabricExternalEpAdminState, CucsExtpolRegistryFsmStageName=CucsExtpolRegistryFsmStageName, CucsConditionRule=CucsConditionRule, CucsDiagTestOrder=CucsDiagTestOrder, CucsAdaptorMgmtCapRebootActionOnDestructive=CucsAdaptorMgmtCapRebootActionOnDestructive, CucsAdaptorHostFcIfAdminState=CucsAdaptorHostFcIfAdminState, CucsFabricFcoeVsanPcTransport=CucsFabricFcoeVsanPcTransport, CucsAdaptorEthOffloadProfileTcpSegment=CucsAdaptorEthOffloadProfileTcpSegment, CucsFabricSwSrvPcType=CucsFabricSwSrvPcType, CucsFabricVnetEpPolicyOwner=CucsFabricVnetEpPolicyOwner, CucsFirmwareUpgradeCategory=CucsFirmwareUpgradeCategory, CucsEquipmentFexCapProviderRole=CucsEquipmentFexCapProviderRole, CucsFirmwareCompleteness=CucsFirmwareCompleteness, CucsFabricMonOperState=CucsFabricMonOperState, CucsFabricEthMonDestEpType=CucsFabricEthMonDestEpType, CucsNetworkIfStatus=CucsNetworkIfStatus, CucsFabricVConSelectPref=CucsFabricVConSelectPref, CucsFabricAVlanType=CucsFabricAVlanType, CucsFabricAEthEstcEpType=CucsFabricAEthEstcEpType, CucsAdaptorMenloNetEgStatsThresholded=CucsAdaptorMenloNetEgStatsThresholded, CucsAdaptorEthPortMcastStatsHistThresholded=CucsAdaptorEthPortMcastStatsHistThresholded, CucsSwFcSanBorderUplinkTrunking=CucsSwFcSanBorderUplinkTrunking, CucsEquipmentChassisFsmStageName=CucsEquipmentChassisFsmStageName, CucsVmOsHvVendor=CucsVmOsHvVendor, CucsAaaClear=CucsAaaClear, CucsSwFcSanEpTransport=CucsSwFcSanEpTransport, CucsEtherSwitchIntFIoPcEpPortId=CucsEtherSwitchIntFIoPcEpPortId, CucsConditionType=CucsConditionType, CucsQosclassFcDrop=CucsQosclassFcDrop, CucsAdaptorCIoEpIfType=CucsAdaptorCIoEpIfType, CucsCommCipherSuiteMode=CucsCommCipherSuiteMode, CucsAdaptorUnitExtnId=CucsAdaptorUnitExtnId, CucsExtpolAppCapability=CucsExtpolAppCapability, CucsDiagStatus=CucsDiagStatus, CucsFcpoolInitiatorsMaxPortsPerNode=CucsFcpoolInitiatorsMaxPortsPerNode, CucsCallhomeAlertMessageSubtype=CucsCallhomeAlertMessageSubtype, CucsConditionCallHomeCause=CucsConditionCallHomeCause, CucsCallhomeEpFsmStageName=CucsCallhomeEpFsmStageName, CucsAaaRealmFsmStageName=CucsAaaRealmFsmStageName, CucsEquipmentPsuType=CucsEquipmentPsuType, CucsExtpolEpFsmCurrentFsm=CucsExtpolEpFsmCurrentFsm, CucsFabricVConSharePref=CucsFabricVConSharePref, CucsFabricInternalLocale=CucsFabricInternalLocale, CucsStorageSystemFsmCurrentFsm=CucsStorageSystemFsmCurrentFsm, CucsIdentIdentReqIntent=CucsIdentIdentReqIntent, CucsAdaptorFcIfEventStatsHistThresholded=CucsAdaptorFcIfEventStatsHistThresholded, CucsFabricVnetEpSyncEpFsmStageName=CucsFabricVnetEpSyncEpFsmStageName, CucsFabricBHVlanSwitchId=CucsFabricBHVlanSwitchId, CucsPowerPrioritySharing=CucsPowerPrioritySharing, CucsSwAccessEpLocale=CucsSwAccessEpLocale, CucsMemoryBufferUnitEnvStatsHistThresholded=CucsMemoryBufferUnitEnvStatsHistThresholded, CucsEquipmentDiscoveryCapOperPowerRequirement=CucsEquipmentDiscoveryCapOperPowerRequirement, CucsExtpolRegistryFsmCurrentFsm=CucsExtpolRegistryFsmCurrentFsm, CucsLsmaintAckDisr=CucsLsmaintAckDisr, CucsNetworkPortRole=CucsNetworkPortRole, CucsEquipmentPOSTRecoverability=CucsEquipmentPOSTRecoverability, CucsCommClientAdminState=CucsCommClientAdminState, CucsComputePciCapOrder=CucsComputePciCapOrder, CucsFabricComputeSlotEpFsmCurrentFsm=CucsFabricComputeSlotEpFsmCurrentFsm, CucsDiagSuccessAction=CucsDiagSuccessAction, CucsNfsMountInstFsmStageName=CucsNfsMountInstFsmStageName, CucsPkiKeyringState=CucsPkiKeyringState, CucsStorageControllerId=CucsStorageControllerId, CucsEquipmentBeaconLedState=CucsEquipmentBeaconLedState, CucsAaaAuthRealmFsmStageName=CucsAaaAuthRealmFsmStageName, CucsAaaAccountStatus=CucsAaaAccountStatus, CucsSwVlanConfigStatusType=CucsSwVlanConfigStatusType, CucsImgsecKeyType=CucsImgsecKeyType, CucsCommDnsProviderAdminState=CucsCommDnsProviderAdminState, CucsFcErrStatsThresholded=CucsFcErrStatsThresholded, CucsMemoryArrayEnvStatsHistThresholded=CucsMemoryArrayEnvStatsHistThresholded, CucsFabricQuerierType=CucsFabricQuerierType, CucsComputePooledSlotSlotId=CucsComputePooledSlotSlotId, CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech=CucsBiosVfEnhancedIntelSpeedStepTechVpEnhancedIntelSpeedStepTech, CucsFabricSanEpIfRole=CucsFabricSanEpIfRole, CucsMemoryAdminState=CucsMemoryAdminState, CucsBiosVfProcessorC1EVpProcessorC1E=CucsBiosVfProcessorC1EVpProcessorC1E, CucsSysdebugCoreExportStatus=CucsSysdebugCoreExportStatus, CucsPolicyControlEpFsmStageName=CucsPolicyControlEpFsmStageName, CucsMgmtIntAuthPolicyMethod=CucsMgmtIntAuthPolicyMethod, CucsEtherTxStatsHistThresholded=CucsEtherTxStatsHistThresholded, CucsFabricFcMonDestEpPortId=CucsFabricFcMonDestEpPortId, CucsEtherPIoFsmCurrentFsm=CucsEtherPIoFsmCurrentFsm, CucsSwFcZoneLc=CucsSwFcZoneLc, CucsAdaptorExtIpV6RssHashProfileIpHash=CucsAdaptorExtIpV6RssHashProfileIpHash, CucsMgmtSubject=CucsMgmtSubject, CucsExtmgmtGatewayPingMaxDeadlineTimeout=CucsExtmgmtGatewayPingMaxDeadlineTimeout, CucsVnicMezzMappingScheme=CucsVnicMezzMappingScheme, CucsVnicConfigIssues=CucsVnicConfigIssues, CucsComputePsuRedundancyOperState=CucsComputePsuRedundancyOperState, CucsMemoryUnitOperability=CucsMemoryUnitOperability, CucsAdaptorCapDefType=CucsAdaptorCapDefType, CucsFabricMembershipStatus=CucsFabricMembershipStatus, CucsFabricSanPcIfRole=CucsFabricSanPcIfRole, CucsSwAccessDomainLocale=CucsSwAccessDomainLocale, CucsVmAdaptorOwner=CucsVmAdaptorOwner, CucsPowerPsuState=CucsPowerPsuState, CucsFirmwareAdminState=CucsFirmwareAdminState, CucsAdaptorEthPortStatsThresholded=CucsAdaptorEthPortStatsThresholded, CucsEquipmentPsuInputStatsHistThresholded=CucsEquipmentPsuInputStatsHistThresholded, CucsFabricComputePhEpAdminState=CucsFabricComputePhEpAdminState, CucsCallhomeAlertLevel=CucsCallhomeAlertLevel, CucsSwPIoEpLc=CucsSwPIoEpLc, cucsTextualConventionsObjects=cucsTextualConventionsObjects, CucsSwFcServerZoneGroupLc=CucsSwFcServerZoneGroupLc, CucsFabricDceSwSrvPcPortId=CucsFabricDceSwSrvPcPortId)
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", CucsFabricSlotAdminState=CucsFabricSlotAdminState, CucsEtherLossStatsThresholded=CucsEtherLossStatsThresholded, CucsFabricEthTargetEpTransport=CucsFabricEthTargetEpTransport, CucsFirmwareType=CucsFirmwareType, CucsFaultBasePolicySoakingSeverity=CucsFaultBasePolicySoakingSeverity, CucsSwMonLifeCycle=CucsSwMonLifeCycle, CucsBiosVfExecuteDisableBitVpExecuteDisableBit=CucsBiosVfExecuteDisableBitVpExecuteDisableBit, CucsFirmwareFwState=CucsFirmwareFwState, CucsVnicPlacement=CucsVnicPlacement, CucsMgmtControllerFsmTaskFlags=CucsMgmtControllerFsmTaskFlags, CucsMgmtAdminState=CucsMgmtAdminState, CucsEquipmentFanModule=CucsEquipmentFanModule, CucsMgmtBackupFsmCurrentFsm=CucsMgmtBackupFsmCurrentFsm, CucsBmcSELCntEqptClassId=CucsBmcSELCntEqptClassId, CucsEtherErrStatsHistThresholded=CucsEtherErrStatsHistThresholded, CucsFabricEthEstcEpPrio=CucsFabricEthEstcEpPrio, CucsStatsThresholdDirection=CucsStatsThresholdDirection, CucsAdaptorEthPortBySizeLargeStatsThresholded=CucsAdaptorEthPortBySizeLargeStatsThresholded, CucsEtherSwitchIntFIoIfRole=CucsEtherSwitchIntFIoIfRole, CucsPolicyPolicyScopeFsmCurrentFsm=CucsPolicyPolicyScopeFsmCurrentFsm, CucsFcPIoFsmCurrentFsm=CucsFcPIoFsmCurrentFsm, CucsAaaAuthRealmFsmCurrentFsm=CucsAaaAuthRealmFsmCurrentFsm, CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping=CucsBiosVfIntelVTForDirectedIOVpIntelVTDInterruptRemapping, CucsEquipmentMethod=CucsEquipmentMethod, CucsExtmgmtIfMonPolicyMonitorMechanism=CucsExtmgmtIfMonPolicyMonitorMechanism, CucsSwAccessDomainFsmTaskItem=CucsSwAccessDomainFsmTaskItem, CucsSwPhysFsmCurrentFsm=CucsSwPhysFsmCurrentFsm, CucsStorageIniGroupOwner=CucsStorageIniGroupOwner, CucsFabricFcoeSanPcEpSlotId=CucsFabricFcoeSanPcEpSlotId, CucsSwEthLanBorderTransport=CucsSwEthLanBorderTransport, CucsNfsMntAdminState=CucsNfsMntAdminState, CucsLsAgentMode=CucsLsAgentMode, CucsMoMoClassId=CucsMoMoClassId, CucsMemoryArrayId=CucsMemoryArrayId, CucsFirmwarePackItemPresence=CucsFirmwarePackItemPresence, CucsFabricEthMonDestEpSlotId=CucsFabricEthMonDestEpSlotId, CucsSwFcoeEstcEpTransport=CucsSwFcoeEstcEpTransport, CucsIpIPv4DnsPref=CucsIpIPv4DnsPref, CucsComputeMbTempStatsThresholded=CucsComputeMbTempStatsThresholded, CucsSwMonDomainLocale=CucsSwMonDomainLocale, CucsCapabilityUpdaterFsmStageName=CucsCapabilityUpdaterFsmStageName, CucsEtherFcoeInterfaceStatsThresholded=CucsEtherFcoeInterfaceStatsThresholded, CucsCommSyslogSourceFaults=CucsCommSyslogSourceFaults, CucsFabricFcoeSanPcEpPortId=CucsFabricFcoeSanPcEpPortId, CucsEtherExternalPcAdminState=CucsEtherExternalPcAdminState, CucsExtvmmEpFsmStageName=CucsExtvmmEpFsmStageName, CucsAaaNoRolePolicy=CucsAaaNoRolePolicy, CucsAdaptorExtIpV6RssHashProfileTcpHash=CucsAdaptorExtIpV6RssHashProfileTcpHash, CucsComputeServerDiscPolicyFsmTaskItem=CucsComputeServerDiscPolicyFsmTaskItem, CucsSysdebugEpLogType=CucsSysdebugEpLogType, CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState=CucsBiosVfPCISlotOptionROMEnableVpSlotMezzState, CucsFabricEthLanEpVlanStatus=CucsFabricEthLanEpVlanStatus, CucsFabricDceSwSrvEpSlotId=CucsFabricDceSwSrvEpSlotId, CucsAdaptorEthOffloadProfileTcpRxChecksum=CucsAdaptorEthOffloadProfileTcpRxChecksum, CucsFabricFcMonSrcEpType=CucsFabricFcMonSrcEpType, CucsMgmtImporterProto=CucsMgmtImporterProto, CucsMgmtIfFsmTaskItem=CucsMgmtIfFsmTaskItem, CucsComputeAdminTrigger=CucsComputeAdminTrigger, CucsCallhomeEpConfigState=CucsCallhomeEpConfigState, CucsEquipmentFexFsmTaskItem=CucsEquipmentFexFsmTaskItem, CucsEquipmentOperability=CucsEquipmentOperability, CucsCommSyslogSourceAudits=CucsCommSyslogSourceAudits, CucsSwConfMode=CucsSwConfMode, CucsFabricAVsanTransport=CucsFabricAVsanTransport, CucsFcStatsHistThresholded=CucsFcStatsHistThresholded, CucsFabricFcMonSanTransport=CucsFabricFcMonSanTransport, CucsFabricAVsanType=CucsFabricAVsanType, CucsStatsThr32DefinitionPropType=CucsStatsThr32DefinitionPropType, CucsAddressMACMask=CucsAddressMACMask, CucsFirmwareDistributableFsmStageName=CucsFirmwareDistributableFsmStageName, CucsComputeRackQualMaxId=CucsComputeRackQualMaxId, CucsFabricLanCloudFsmStageName=CucsFabricLanCloudFsmStageName, CucsEtherPIoEpIfType=CucsEtherPIoEpIfType, CucsAdaptorMenloEthStatsHistThresholded=CucsAdaptorMenloEthStatsHistThresholded, CucsCapabilityAdminState=CucsCapabilityAdminState, CucsFabricExternalPcLocale=CucsFabricExternalPcLocale, CucsSwVlanCompType=CucsSwVlanCompType, CucsEtherServerIntFIoLocale=CucsEtherServerIntFIoLocale, CucsMgmtSource=CucsMgmtSource, CucsSwFcSanBorderTransport=CucsSwFcSanBorderTransport, CucsStorageEtherIfVlanType=CucsStorageEtherIfVlanType, CucsExtpolConnType=CucsExtpolConnType, CucsEquipmentChassisStatsThresholded=CucsEquipmentChassisStatsThresholded, CucsPoolElementOwner=CucsPoolElementOwner, CucsFabricZoningState=CucsFabricZoningState, CucsSwLanBorderType=CucsSwLanBorderType, CucsMgmtBackupPostAction=CucsMgmtBackupPostAction, CucsSwFcoeSanEpTransport=CucsSwFcoeSanEpTransport, CucsFabricEthMonTransport=CucsFabricEthMonTransport, CucsVmSwitchAdminState=CucsVmSwitchAdminState, CucsSwEthLanPcTransport=CucsSwEthLanPcTransport, CucsNetworkElementOperability=CucsNetworkElementOperability, CucsFabricPIoEpIfType=CucsFabricPIoEpIfType, CucsComputeServerDiscPolicyFsmStageName=CucsComputeServerDiscPolicyFsmStageName, CucsAaaRadiusEpFsmCurrentFsm=CucsAaaRadiusEpFsmCurrentFsm, CucsPortPIoFsmTaskItem=CucsPortPIoFsmTaskItem, CucsAdaptorEthPortBySizeSmallStatsHistThresholded=CucsAdaptorEthPortBySizeSmallStatsHistThresholded, CucsStorageControllerFaultMonitoring=CucsStorageControllerFaultMonitoring, CucsBiosSupportedAction=CucsBiosSupportedAction, CucsEquipmentFanModuleStatsHistThresholded=CucsEquipmentFanModuleStatsHistThresholded, CucsLicenseState=CucsLicenseState, CucsBiosVfOptionROMLoadVpLoad=CucsBiosVfOptionROMLoadVpLoad, CucsIdentIdentType=CucsIdentIdentType, CucsSwSanBorderType=CucsSwSanBorderType, CucsAaaUserEpFsmTaskItem=CucsAaaUserEpFsmTaskItem, CucsSysdebugAutoCoreFileExportTargetProto=CucsSysdebugAutoCoreFileExportTargetProto, CucsAdaptorEthPortBySizeSmallStatsThresholded=CucsAdaptorEthPortBySizeSmallStatsThresholded, CucsAdaptorRssProfileReceiveSideScaling=CucsAdaptorRssProfileReceiveSideScaling, CucsVnicEtherBaseSwitchId=CucsVnicEtherBaseSwitchId, CucsExtpolProviderFsmCurrentFsm=CucsExtpolProviderFsmCurrentFsm, CucsLsmaintAckChangeDetails=CucsLsmaintAckChangeDetails, CucsBiosVfUSBBootConfigVpLegacyUSBSupport=CucsBiosVfUSBBootConfigVpLegacyUSBSupport, CucsPolicyControlEpType=CucsPolicyControlEpType, CucsFirmwareComponentType=CucsFirmwareComponentType, CucsSwFcEstcEpTransport=CucsSwFcEstcEpTransport, CucsSwVlanGroupType=CucsSwVlanGroupType, CucsAaaLdapEpFsmCurrentFsm=CucsAaaLdapEpFsmCurrentFsm, CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR=CucsBiosVfAssertNMIOnSERRVpAssertNMIOnSERR, CucsComputeChassisQualMinId=CucsComputeChassisQualMinId, CucsFabricFcSanEpPortId=CucsFabricFcSanEpPortId, CucsFabricAccessType=CucsFabricAccessType, CucsStorageKeyType=CucsStorageKeyType, CucsTrigTriggeredState=CucsTrigTriggeredState, CucsAdaptorMenloFcErrorStatsThresholded=CucsAdaptorMenloFcErrorStatsThresholded, CucsComputePCIeFatalProtocolStatsThresholded=CucsComputePCIeFatalProtocolStatsThresholded, CucsAaaEpFsmCurrentFsm=CucsAaaEpFsmCurrentFsm, CucsEquipmentSlotArraySelector=CucsEquipmentSlotArraySelector, CucsNetworkIfStatsType=CucsNetworkIfStatsType, CucsSwLanMonType=CucsSwLanMonType, CucsFabricFcoeSanEpPortId=CucsFabricFcoeSanEpPortId, CucsEquipmentIsSupported=CucsEquipmentIsSupported, CucsFabricInternalEpLocale=CucsFabricInternalEpLocale, CucsLsbootLanAccess=CucsLsbootLanAccess, CucsFabricSnoopingType=CucsFabricSnoopingType, CucsEtherServerIntFIoFsmTaskItem=CucsEtherServerIntFIoFsmTaskItem, CucsIpIpV4StaticAddrPref=CucsIpIpV4StaticAddrPref, CucsVmComputeEpClInstType=CucsVmComputeEpClInstType, CucsObserveObservedFsmStageName=CucsObserveObservedFsmStageName, CucsEquipmentUnifiedPortAlgorithm=CucsEquipmentUnifiedPortAlgorithm, CucsAdaptorFcIfEventStatsThresholded=CucsAdaptorFcIfEventStatsThresholded, CucsIdentConsType=CucsIdentConsType, CucsMgmtEntityLeadership=CucsMgmtEntityLeadership, CucsVnicAIpcIfType=CucsVnicAIpcIfType, CucsSwFcSanPcTransport=CucsSwFcSanPcTransport, CucsComputeRackUnitFsmTaskFlags=CucsComputeRackUnitFsmTaskFlags, CucsMgmtImporterFsmStageName=CucsMgmtImporterFsmStageName, CucsFlowctrlFlowControl=CucsFlowctrlFlowControl, CucsLsbootStorageOrder=CucsLsbootStorageOrder, CucsLsAssignment=CucsLsAssignment, CucsNwctrlLinkFailAction=CucsNwctrlLinkFailAction, CucsSysdebugCoreFsmCurrentFsm=CucsSysdebugCoreFsmCurrentFsm, CucsMgmtStateQual=CucsMgmtStateQual, CucsFirmwareTransport=CucsFirmwareTransport, CucsFabricLanType=CucsFabricLanType, CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech=CucsBiosVfIntelHyperThreadingTechVpIntelHyperThreadingTech, CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport=CucsBiosVfIntelVTForDirectedIOVpIntelVTDATSSupport, CucsEtherCloudType=CucsEtherCloudType, CucsStorageEpAccess=CucsStorageEpAccess, CucsEquipmentConnectionStatus=CucsEquipmentConnectionStatus, CucsFabricSwSrvPcIfRole=CucsFabricSwSrvPcIfRole, CucsSwEthLanBorderFsmTaskItem=CucsSwEthLanBorderFsmTaskItem, CucsSwEthEstcEpTransport=CucsSwEthEstcEpTransport, CucsNwctrlRegistrationMode=CucsNwctrlRegistrationMode, CucsDiagBladeTestType=CucsDiagBladeTestType, CucsSysfileMutationAction=CucsSysfileMutationAction, CucsQosclassDefinitionFsmTaskItem=CucsQosclassDefinitionFsmTaskItem, CucsCommShellProto=CucsCommShellProto, CucsSwEthMonSrcEpTransport=CucsSwEthMonSrcEpTransport, CucsFabricVlanCompType=CucsFabricVlanCompType, CucsMgmtAccess=CucsMgmtAccess, CucsFirmwareTriggerState=CucsFirmwareTriggerState, CucsCallhomeFormat=CucsCallhomeFormat, CucsAdaptorMenloDcePortStatsThresholded=CucsAdaptorMenloDcePortStatsThresholded, CucsFabricEthMonFiltRefType=CucsFabricEthMonFiltRefType, CucsCommSvcEpFsmCurrentFsm=CucsCommSvcEpFsmCurrentFsm, CucsEpqosDefinitionDelTaskFsmCurrentFsm=CucsEpqosDefinitionDelTaskFsmCurrentFsm, CucsEtherSwitchIntFIoLocale=CucsEtherSwitchIntFIoLocale, CucsVnicVirtualizationPreferenceType=CucsVnicVirtualizationPreferenceType, CucsEquipmentIOCardIssues=CucsEquipmentIOCardIssues, CucsEquipmentFexId=CucsEquipmentFexId, CucsSwEthLanEpTransport=CucsSwEthLanEpTransport, CucsLsbootStorageAccess=CucsLsbootStorageAccess, CucsAaaEpAccess=CucsAaaEpAccess, CucsBiosVfNUMAOptimizedVpNUMAOptimized=CucsBiosVfNUMAOptimizedVpNUMAOptimized, CucsConditionAckAction=CucsConditionAckAction, CucsStatsCollectionInterval=CucsStatsCollectionInterval, CucsSwLanEpType=CucsSwLanEpType, CucsTrigTrigOperState=CucsTrigTrigOperState, CucsComputeServerDiscPolicyFsmCurrentFsm=CucsComputeServerDiscPolicyFsmCurrentFsm, CucsMgmtEntityMgmtServicesState=CucsMgmtEntityMgmtServicesState, CucsPortTrust=CucsPortTrust, CucsSwFcMonSrcEpTransport=CucsSwFcMonSrcEpTransport, CucsAdaptorDefaultAction=CucsAdaptorDefaultAction, CucsAaaEpFsmTaskItem=CucsAaaEpFsmTaskItem, CucsCallhomeLevel=CucsCallhomeLevel, CucsBiosVfProcessorC6ReportVpProcessorC6Report=CucsBiosVfProcessorC6ReportVpProcessorC6Report, CucsEquipmentInternalFanType=CucsEquipmentInternalFanType, CucsMgmtIfFsmStageName=CucsMgmtIfFsmStageName, CucsProcessorErrorStatsThresholded=CucsProcessorErrorStatsThresholded, CucsDcxVIfProtRole=CucsDcxVIfProtRole, CucsSysdebugAutoCoreFileExportTargetFsmStageName=CucsSysdebugAutoCoreFileExportTargetFsmStageName, CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr=CucsBiosVfMaxVariableMTRRSettingVpProcessorMtrr, CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB=CucsBiosVfMemoryMappedIOAbove4GBVpMemoryMappedIOAbove4GB, CucsExtmgmtArpTargetsNumberOfArpRequests=CucsExtmgmtArpTargetsNumberOfArpRequests, CucsFabricSanType=CucsFabricSanType, CucsAaaLdapEpFsmStageName=CucsAaaLdapEpFsmStageName, CucsEquipmentFexPsuInputStatsHistThresholded=CucsEquipmentFexPsuInputStatsHistThresholded, CucsComputeBladeSlotId=CucsComputeBladeSlotId, CucsDcxNsAllocStatus=CucsDcxNsAllocStatus, CucsEtherRxStatsHistThresholded=CucsEtherRxStatsHistThresholded, CucsAaaLdapGroupRuleTraversal=CucsAaaLdapGroupRuleTraversal, CucsFcStatsThresholded=CucsFcStatsThresholded, CucsSwAccessDomainType=CucsSwAccessDomainType, CucsMgmtEntityHaReadiness=CucsMgmtEntityHaReadiness, CucsMemoryErrorCorrection=CucsMemoryErrorCorrection, CucsFabricCloudType=CucsFabricCloudType, CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm=CucsSysdebugAutoCoreFileExportTargetFsmCurrentFsm, CucsEtherServerIntFIoType=CucsEtherServerIntFIoType, CucsExtvmmMasterExtKeyFsmTaskItem=CucsExtvmmMasterExtKeyFsmTaskItem, CucsEquipmentFanModuleId=CucsEquipmentFanModuleId, CucsAdaptorInterruptMode=CucsAdaptorInterruptMode, CucsLsOperState=CucsLsOperState, CucsLsmaintAckChanges=CucsLsmaintAckChanges, CucsFabricFcMonSanType=CucsFabricFcMonSanType, CucsLsConfigState=CucsLsConfigState, CucsProcessorQualArch=CucsProcessorQualArch, CucsTrigTokenOperState=CucsTrigTokenOperState, CucsInitiatorGroupType=CucsInitiatorGroupType, CucsFabricFcSanPcTransport=CucsFabricFcSanPcTransport, CucsConditionSeverity=CucsConditionSeverity, CucsFabricSwChPhEpAdminState=CucsFabricSwChPhEpAdminState, CucsCommSnmpAuth=CucsCommSnmpAuth, CucsLicenseFeatureType=CucsLicenseFeatureType, CucsMgmtEntityChassisDeviceIoState1=CucsMgmtEntityChassisDeviceIoState1, CucsAddressUIDSuffxMask=CucsAddressUIDSuffxMask, CucsSwCardEnvStatsHistThresholded=CucsSwCardEnvStatsHistThresholded, CucsFabricEthMonDestEpIfRole=CucsFabricEthMonDestEpIfRole, CucsEtherServerIntFIoPcIfRole=CucsEtherServerIntFIoPcIfRole, CucsSwBorderDomainLocale=CucsSwBorderDomainLocale, CucsEquipmentRackUnitPsuStatsHistThresholded=CucsEquipmentRackUnitPsuStatsHistThresholded, CucsStorageTechnology=CucsStorageTechnology, CucsAdaptorExtEthIfPcPortId=CucsAdaptorExtEthIfPcPortId, CucsExtvmmProviderFsmStageName=CucsExtvmmProviderFsmStageName, CucsLicenseDownloaderFsmTaskItem=CucsLicenseDownloaderFsmTaskItem, CucsFabricConfigState=CucsFabricConfigState, CucsFabricFcSanUplinkTrunking=CucsFabricFcSanUplinkTrunking, CucsMgmtBackupProto=CucsMgmtBackupProto, CucsVnicVnicBehPolicyType=CucsVnicVnicBehPolicyType, CucsFabricAFcEstcEpType=CucsFabricAFcEstcEpType, CucsPowerMgmtStyle=CucsPowerMgmtStyle, CucsSwFcSanBorderFsmStageName=CucsSwFcSanBorderFsmStageName, CucsEquipmentCommStatus=CucsEquipmentCommStatus, CucsSwEthLanEpVlanStatus=CucsSwEthLanEpVlanStatus, CucsAdaptorLanCapDefaultVlan=CucsAdaptorLanCapDefaultVlan)
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize=CucsBiosVfUSBSysIdlePowerOptimizingSettingVpUSBIdlePowerOptimize, CucsAdaptorHostIfBootDev=CucsAdaptorHostIfBootDev, CucsComputePhysicalFsmTaskItem=CucsComputePhysicalFsmTaskItem, CucsProcessorEnvStatsHistThresholded=CucsProcessorEnvStatsHistThresholded, CucsSwFcoeSanPcTransport=CucsSwFcoeSanPcTransport, CucsFabricInternalDceSrvTransport=CucsFabricInternalDceSrvTransport, CucsSysdebugCoreFsmTaskItem=CucsSysdebugCoreFsmTaskItem, CucsConditionLifecycle=CucsConditionLifecycle, CucsSwFcMonTransport=CucsSwFcMonTransport, CucsFirmwareSystemFsmTaskFlags=CucsFirmwareSystemFsmTaskFlags, CucsEquipmentPsuOutputStatsHistThresholded=CucsEquipmentPsuOutputStatsHistThresholded, CucsPowerChThrAction=CucsPowerChThrAction, CucsAdaptorEthPortBySizeLargeStatsHistThresholded=CucsAdaptorEthPortBySizeLargeStatsHistThresholded, CucsIqnpoolPoolAssignmentOrder=CucsIqnpoolPoolAssignmentOrder, CucsStorageOperState=CucsStorageOperState, CucsSysdebugTechSupportFsmCurrentFsm=CucsSysdebugTechSupportFsmCurrentFsm, CucsAdaptorIpV4RssHashProfileIpHash=CucsAdaptorIpV4RssHashProfileIpHash, CucsMemoryUnitEnvStatsThresholded=CucsMemoryUnitEnvStatsThresholded, CucsVnicLunId=CucsVnicLunId, CucsAdaptorEthPortStatsHistThresholded=CucsAdaptorEthPortStatsHistThresholded, CucsConditionAdminState=CucsConditionAdminState, CucsFabricEthMonLanType=CucsFabricEthMonLanType, CucsAdaptorFcIfFrameStatsHistThresholded=CucsAdaptorFcIfFrameStatsHistThresholded, CucsAdaptorFcPortStatsThresholded=CucsAdaptorFcPortStatsThresholded, CucsNetworkPhysEpIfType=CucsNetworkPhysEpIfType, CucsFabricCIoEpIfType=CucsFabricCIoEpIfType, CucsDpsecForgedTransmit=CucsDpsecForgedTransmit, CucsEquipmentSecureBios=CucsEquipmentSecureBios, CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR=CucsBiosVfAssertNMIOnPERRVpAssertNMIOnPERR, CucsCapabilityMgmtExtensionFsmCurrentFsm=CucsCapabilityMgmtExtensionFsmCurrentFsm, CucsEquipmentFanModuleStatsThresholded=CucsEquipmentFanModuleStatsThresholded, CucsEquipmentIOCardStatsHistThresholded=CucsEquipmentIOCardStatsHistThresholded, CucsFabricLanCloudVlanCompression=CucsFabricLanCloudVlanCompression, CucsEquipmentSlotArrayOrientation=CucsEquipmentSlotArrayOrientation, CucsAdaptorSanCapHostNvram=CucsAdaptorSanCapHostNvram, CucsVnicIScsiIfDefType=CucsVnicIScsiIfDefType, CucsVnicProfileSetFsmCurrentFsm=CucsVnicProfileSetFsmCurrentFsm, CucsComputeRackUnitMbTempStatsThresholded=CucsComputeRackUnitMbTempStatsThresholded, CucsPoolPoolAssignmentOrder=CucsPoolPoolAssignmentOrder, CucsFirmwareUpdatableDeployment=CucsFirmwareUpdatableDeployment, CucsFabricSanCloudFsmTaskItem=CucsFabricSanCloudFsmTaskItem, CucsCommSyslogSourceEvents=CucsCommSyslogSourceEvents, CucsVnicOrderScheme=CucsVnicOrderScheme, CucsComputeRackUnitFsmCurrentFsm=CucsComputeRackUnitFsmCurrentFsm, CucsVnicTemplateType=CucsVnicTemplateType, CucsBiosVfSerialPortAEnableVpSerialPortAEnable=CucsBiosVfSerialPortAEnableVpSerialPortAEnable, CucsAaaUserEpFsmCurrentFsm=CucsAaaUserEpFsmCurrentFsm, CucsSwAccessDomainFsmStageName=CucsSwAccessDomainFsmStageName, CucsFabricLanCloudFsmCurrentFsm=CucsFabricLanCloudFsmCurrentFsm, CucsExtvmmKeyStoreFsmTaskItem=CucsExtvmmKeyStoreFsmTaskItem, CucsCommChannel=CucsCommChannel, CucsQosclassEthClassifiedPriority=CucsQosclassEthClassifiedPriority, CucsCommSyslogRestrictedSeverity=CucsCommSyslogRestrictedSeverity, CucsCommFilePathProtocol=CucsCommFilePathProtocol, CucsComputeAdminLinkAggregation=CucsComputeAdminLinkAggregation, CucsCommXmlClConnPolicyClientType=CucsCommXmlClConnPolicyClientType, CucsSwFcZoneSetLc=CucsSwFcZoneSetLc, CucsAdaptorExtIfPcIfRole=CucsAdaptorExtIfPcIfRole, CucsFabricVnetEpIfRole=CucsFabricVnetEpIfRole, CucsEquipmentBiosUpdateMethod=CucsEquipmentBiosUpdateMethod, CucsCapabilityUpdaterFsmTaskItem=CucsCapabilityUpdaterFsmTaskItem, CucsEquipmentHealthLedState=CucsEquipmentHealthLedState, CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID=CucsBiosVfIntelEntrySASRAIDModuleVpSASRAID, CucsAaaPwdPolicy=CucsAaaPwdPolicy, CucsFirmwarePackMode=CucsFirmwarePackMode, CucsFabricTargetEpType=CucsFabricTargetEpType, CucsSwSanEpType=CucsSwSanEpType, CucsVnicLanConnTemplSwitchId=CucsVnicLanConnTemplSwitchId, CucsCommSnmpProto=CucsCommSnmpProto, CucsEtherRxStatsThresholded=CucsEtherRxStatsThresholded, CucsExtvmmMasterExtKeyFsmStageName=CucsExtvmmMasterExtKeyFsmStageName, CucsLsbootLanBootProt=CucsLsbootLanBootProt, CucsExtvmmOwnership=CucsExtvmmOwnership, CucsEquipmentFanId=CucsEquipmentFanId, CucsPolicyPolicyOwner=CucsPolicyPolicyOwner, CucsBmcSELCntStatsClassId=CucsBmcSELCntStatsClassId, CucsIdentIdDefinedInIdm=CucsIdentIdDefinedInIdm, CucsFabricMonOperStateReason=CucsFabricMonOperStateReason, CucsLsbootIScsiType=CucsLsbootIScsiType, CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule=CucsBiosVfIntelEntrySASRAIDModuleVpSASRAIDModule, CucsSwEstcEpLocale=CucsSwEstcEpLocale, CucsBiosVfPCISlotOptionROMEnableVpSlot7State=CucsBiosVfPCISlotOptionROMEnableVpSlot7State, CucsFabricConfState=CucsFabricConfState, CucsPolicyControlEpFsmTaskItem=CucsPolicyControlEpFsmTaskItem, CucsComputeOwner=CucsComputeOwner, CucsEpqosDefinitionDelTaskFsmStageName=CucsEpqosDefinitionDelTaskFsmStageName, CucsIqnpoolBlockFrom=CucsIqnpoolBlockFrom, CucsVnicAScsiIfType=CucsVnicAScsiIfType, CucsExtmgmtIfMonPolicyAdminState=CucsExtmgmtIfMonPolicyAdminState, CucsComputeBoardPower=CucsComputeBoardPower, CucsMgmtIfFsmCurrentFsm=CucsMgmtIfFsmCurrentFsm, CucsEquipmentChassisFsmTaskItem=CucsEquipmentChassisFsmTaskItem, CucsNfsMountDefFsmStageName=CucsNfsMountDefFsmStageName, CucsStorageRaidBatteryOperabilityQualifier=CucsStorageRaidBatteryOperabilityQualifier, CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable=CucsBiosVfUSBBootConfigVpMakeDeviceNonBootable, CucsAdaptorExtIfAdminState=CucsAdaptorExtIfAdminState, CucsFabricExternalLocale=CucsFabricExternalLocale, CucsFabricMemberStatus=CucsFabricMemberStatus, CucsFabricMonAdminState=CucsFabricMonAdminState, CucsFabricDceSwSrvPcTransport=CucsFabricDceSwSrvPcTransport, CucsSolAdminState=CucsSolAdminState, CucsSysdebugLogControlEpFsmCurrentFsm=CucsSysdebugLogControlEpFsmCurrentFsm, CucsCallhomePolicyAdminState=CucsCallhomePolicyAdminState, CucsCapabilityUpdaterFsmCurrentFsm=CucsCapabilityUpdaterFsmCurrentFsm, CucsFabricFcSanPcEpSlotId=CucsFabricFcSanPcEpSlotId, CucsVnicAFcIfType=CucsVnicAFcIfType, CucsEquipmentPsuOutputStatsThresholded=CucsEquipmentPsuOutputStatsThresholded, CucsEtherPIoFsmStageName=CucsEtherPIoFsmStageName, CucsEquipmentIOCardStatsThresholded=CucsEquipmentIOCardStatsThresholded, CucsEquipmentFexPowerSummaryThresholded=CucsEquipmentFexPowerSummaryThresholded, CucsAdaptorMenloBaseErrorStatsThresholded=CucsAdaptorMenloBaseErrorStatsThresholded, CucsExtpolEpFsmTaskItem=CucsExtpolEpFsmTaskItem, CucsFabricInternalDceSrvType=CucsFabricInternalDceSrvType, CucsAaaTacacsPlusEpFsmCurrentFsm=CucsAaaTacacsPlusEpFsmCurrentFsm, CucsComputePsuRedundancyOperQualifier=CucsComputePsuRedundancyOperQualifier, CucsMgmtExportPolicyFsmStageName=CucsMgmtExportPolicyFsmStageName, CucsMgmtBackupFsmTaskItem=CucsMgmtBackupFsmTaskItem, CucsStorageDisklessAction=CucsStorageDisklessAction, CucsVnicHostNwIOPerfPref=CucsVnicHostNwIOPerfPref, CucsIdentIdentRequestFsmTaskItem=CucsIdentIdentRequestFsmTaskItem, CucsPortGroupType=CucsPortGroupType, CucsAdaptorMgmtCapMode=CucsAdaptorMgmtCapMode, CucsComputeRackUnitId=CucsComputeRackUnitId, CucsFabricFcMonDestEpIfRole=CucsFabricFcMonDestEpIfRole, CucsSwEthMonType=CucsSwEthMonType, CucsFirmwareRunningDeployment=CucsFirmwareRunningDeployment, CucsPowerOperState=CucsPowerOperState, CucsEquipmentNetworkElementFanStatsThresholded=CucsEquipmentNetworkElementFanStatsThresholded, CucsSwUtilityDomainLocale=CucsSwUtilityDomainLocale, CucsComputeAlarmSeverity=CucsComputeAlarmSeverity, CucsBiosVfDramRefreshRateVpDramRefreshRate=CucsBiosVfDramRefreshRateVpDramRefreshRate, CucsAdaptorFcIfFrameStatsThresholded=CucsAdaptorFcIfFrameStatsThresholded, CucsNfsClientConfigState=CucsNfsClientConfigState, CucsSwCardEnvStatsThresholded=CucsSwCardEnvStatsThresholded, CucsInitiatorIScsiInitiatorEpProt=CucsInitiatorIScsiInitiatorEpProt, CucsMgmtImportStatus=CucsMgmtImportStatus, CucsMgmtControllerFsmStageName=CucsMgmtControllerFsmStageName, CucsQosclassEthBEAdminState=CucsQosclassEthBEAdminState, CucsSysdebugTechSupportFsmStageName=CucsSysdebugTechSupportFsmStageName, CucsPortPIoFsmCurrentFsm=CucsPortPIoFsmCurrentFsm, CucsAdaptorMenloHostPortStatsThresholded=CucsAdaptorMenloHostPortStatsThresholded, CucsEtherServerIntFIoPcEpPortId=CucsEtherServerIntFIoPcEpPortId, CucsAdaptorMenloMcpuStatsHistThresholded=CucsAdaptorMenloMcpuStatsHistThresholded, CucsCallhomeEpFsmCurrentFsm=CucsCallhomeEpFsmCurrentFsm, CucsAddressType=CucsAddressType, CucsStorageConnectionProtocol=CucsStorageConnectionProtocol, CucsFabricEthMonDestEpPortId=CucsFabricEthMonDestEpPortId, CucsAaaRealmFsmCurrentFsm=CucsAaaRealmFsmCurrentFsm, CucsFirmwareSystemFsmStageName=CucsFirmwareSystemFsmStageName, CucsFirmwareSystemFsmCurrentFsm=CucsFirmwareSystemFsmCurrentFsm, CucsMgmtExportPolicyProto=CucsMgmtExportPolicyProto, CucsFirmwareDistributableType=CucsFirmwareDistributableType, CucsNwctrlAdminState=CucsNwctrlAdminState, CucsNfsDefAdminState=CucsNfsDefAdminState, CucsFabricEthEstcPcEpPortId=CucsFabricEthEstcPcEpPortId, CucsAdaptorExtIfPcType=CucsAdaptorExtIfPcType, CucsFirmwareBootUnitImage=CucsFirmwareBootUnitImage, CucsAdaptorHostMgmtCapPresence=CucsAdaptorHostMgmtCapPresence, CucsDcxProtState=CucsDcxProtState, CucsEtherExternalEpLocale=CucsEtherExternalEpLocale, CucsCommSvcEpFsmTaskFlags=CucsCommSvcEpFsmTaskFlags, CucsFabricReqIssues=CucsFabricReqIssues, CucsMgmtBackupPolicyFsmCurrentFsm=CucsMgmtBackupPolicyFsmCurrentFsm, CucsVnicExternalMgmtIPMode=CucsVnicExternalMgmtIPMode, CucsAdaptorMenloFcStatsThresholded=CucsAdaptorMenloFcStatsThresholded, CucsFabricLanPcType=CucsFabricLanPcType, CucsSwUtilityDomainFsmCurrentFsm=CucsSwUtilityDomainFsmCurrentFsm, CucsFabricPathEpIfType=CucsFabricPathEpIfType, CucsComputeMbTempStatsHistThresholded=CucsComputeMbTempStatsHistThresholded, CucsPortSpeed=CucsPortSpeed, CucsBiosVfPCISlotOptionROMEnableVpSlot1State=CucsBiosVfPCISlotOptionROMEnableVpSlot1State, CucsAdaptorAdminPowerState=CucsAdaptorAdminPowerState, CucsSysdebugLogControlLevel=CucsSysdebugLogControlLevel, CucsSysdebugLogControlEpFsmTaskItem=CucsSysdebugLogControlEpFsmTaskItem, CucsExtvmmProviderFsmTaskItem=CucsExtvmmProviderFsmTaskItem, CucsEquipmentAirflowDirection=CucsEquipmentAirflowDirection, CucsEquipmentFanStatsThresholded=CucsEquipmentFanStatsThresholded, CucsFabricVConPlacementPref=CucsFabricVConPlacementPref, CucsEquipmentFanTray=CucsEquipmentFanTray, CucsFabricExternalEpLocale=CucsFabricExternalEpLocale, CucsLsServerFsmTaskFlags=CucsLsServerFsmTaskFlags, CucsAdaptorIscsiProtConnectionTimeOut=CucsAdaptorIscsiProtConnectionTimeOut, CucsConditionActionIndicator=CucsConditionActionIndicator, CucsAaaAccess=CucsAaaAccess, CucsSwSystemStatsThresholded=CucsSwSystemStatsThresholded, CucsLsConfigIssues=CucsLsConfigIssues, CucsLicenseType=CucsLicenseType, CucsAaaUserEpFsmStageName=CucsAaaUserEpFsmStageName, CucsFabricLanCloudFsmTaskItem=CucsFabricLanCloudFsmTaskItem, CucsAdaptorFcPortStatsHistThresholded=CucsAdaptorFcPortStatsHistThresholded, CucsEtherServerIntFIoFsmStageName=CucsEtherServerIntFIoFsmStageName, CucsTrigDay=CucsTrigDay, CucsAdaptorHostEthIfFsmCurrentFsm=CucsAdaptorHostEthIfFsmCurrentFsm, CucsStorageControllerForm=CucsStorageControllerForm, CucsFabricPathEpLocale=CucsFabricPathEpLocale, CucsFabricVConInstType=CucsFabricVConInstType, CucsSwEthMonDestEpTransport=CucsSwEthMonDestEpTransport, CucsMgmtPmonEntryState=CucsMgmtPmonEntryState, CucsStoragePathHA=CucsStoragePathHA, CucsPowerGroupStatsHistThresholded=CucsPowerGroupStatsHistThresholded, CucsSwEthTargetEpAdminState=CucsSwEthTargetEpAdminState, CucsIscsiProtocolProfileLunBusyRetryCount=CucsIscsiProtocolProfileLunBusyRetryCount, CucsConfigImpactResponseState=CucsConfigImpactResponseState, CucsFabricNetGroupSwitchId=CucsFabricNetGroupSwitchId, CucsEtherPauseStatsThresholded=CucsEtherPauseStatsThresholded, CucsNfsMountInstFsmCurrentFsm=CucsNfsMountInstFsmCurrentFsm, CucsFirmwareDependencySensitivity=CucsFirmwareDependencySensitivity, CucsSwEnvStatsHistThresholded=CucsSwEnvStatsHistThresholded, CucsCommAdminState=CucsCommAdminState, CucsFabricDefaultZoningState=CucsFabricDefaultZoningState, CucsEquipmentFexEnvStatsHistThresholded=CucsEquipmentFexEnvStatsHistThresholded, CucsStatsCollectionPolicyFsmTaskItem=CucsStatsCollectionPolicyFsmTaskItem, CucsBiosVfBootOptionRetryVpBootOptionRetry=CucsBiosVfBootOptionRetryVpBootOptionRetry, CucsEtherSwitchIntFIoPcIfRole=CucsEtherSwitchIntFIoPcIfRole, CucsSwUtilityDomainFsmTaskItem=CucsSwUtilityDomainFsmTaskItem, CucsFabricOwner=CucsFabricOwner, CucsEquipmentFanModuleTray=CucsEquipmentFanModuleTray, CucsFcErrStatsHistThresholded=CucsFcErrStatsHistThresholded, CucsSwEnvStatsThresholded=CucsSwEnvStatsThresholded, CucsStatsThr64DefinitionPropType=CucsStatsThr64DefinitionPropType, CucsPolicySuspendState=CucsPolicySuspendState, CucsExtvmmEpFsmTaskItem=CucsExtvmmEpFsmTaskItem, CucsEquipmentMemoryUnitDiscoveryModifierAction=CucsEquipmentMemoryUnitDiscoveryModifierAction, CucsFirmwareImageDeleted=CucsFirmwareImageDeleted, CucsStorageLocalDiskConfigFlexFlashState=CucsStorageLocalDiskConfigFlexFlashState, CucsChangeStatus=CucsChangeStatus, CucsEtherServerIntFIoIfRole=CucsEtherServerIntFIoIfRole, CucsAdaptorMenloBaseErrorStatsHistThresholded=CucsAdaptorMenloBaseErrorStatsHistThresholded, CucsLsbootSanImageType=CucsLsbootSanImageType, CucsAdaptorVnicStatsHistThresholded=CucsAdaptorVnicStatsHistThresholded, CucsExtpolProviderFsmStageName=CucsExtpolProviderFsmStageName, CucsLicenseDownloaderFsmStageName=CucsLicenseDownloaderFsmStageName, CucsSwFcZoneMemberLc=CucsSwFcZoneMemberLc, CucsEquipmentXcvrType=CucsEquipmentXcvrType, CucsNetworkSide=CucsNetworkSide, CucsMgmtEntityChassisDeviceIoState3=CucsMgmtEntityChassisDeviceIoState3, CucsNetworkVnetEpIfType=CucsNetworkVnetEpIfType, CucsAdaptorEtherIfStatsHistThresholded=CucsAdaptorEtherIfStatsHistThresholded, CucsEquipmentChassisAdminState=CucsEquipmentChassisAdminState, CucsAaaEpFsmStageName=CucsAaaEpFsmStageName, CucsFirmwareDownloadActivity=CucsFirmwareDownloadActivity, CucsFsmCompletion=CucsFsmCompletion, CucsEquipmentPresence=CucsEquipmentPresence, CucsStorageProtocol=CucsStorageProtocol, CucsOrgLevel=CucsOrgLevel, CucsLicenseInstanceFsmStageName=CucsLicenseInstanceFsmStageName, CucsAdaptorMenloQueueStatsComponent=CucsAdaptorMenloQueueStatsComponent, CucsNfsMountDefFsmTaskItem=CucsNfsMountDefFsmTaskItem, CucsAdaptorProtocolProfileLunBusyRetryCount=CucsAdaptorProtocolProfileLunBusyRetryCount, CucsAdaptorProtocolProfileConnectionTimeOut=CucsAdaptorProtocolProfileConnectionTimeOut, CucsTopMode=CucsTopMode, CucsAaaRadiusService=CucsAaaRadiusService, CucsMgmtExportPolicyFsmCurrentFsm=CucsMgmtExportPolicyFsmCurrentFsm, CucsBiosVfConsoleRedirectionVpLegacyOSRedirection=CucsBiosVfConsoleRedirectionVpLegacyOSRedirection)
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", CucsFabricFcMonDestEpSlotId=CucsFabricFcMonDestEpSlotId, CucsSwLanPcType=CucsSwLanPcType, CucsMgmtBackupInterval=CucsMgmtBackupInterval, CucsExtpolState=CucsExtpolState, CucsFabricFcMonSrcRefType=CucsFabricFcMonSrcRefType, CucsMemoryRuntimeThresholded=CucsMemoryRuntimeThresholded, CucsAaaCimcSessionType=CucsAaaCimcSessionType, CucsAdaptorMenloQStatsThresholded=CucsAdaptorMenloQStatsThresholded, CucsPkiEpFsmStageName=CucsPkiEpFsmStageName, CucsAdaptorExtIfEpIfRole=CucsAdaptorExtIfEpIfRole, CucsAdaptorEthPortErrStatsThresholded=CucsAdaptorEthPortErrStatsThresholded, CucsLicenseTransferState=CucsLicenseTransferState, CucsBiosVfConsoleRedirectionVpBaudRate=CucsBiosVfConsoleRedirectionVpBaudRate, CucsBiosVfACPI10SupportVpACPI10Support=CucsBiosVfACPI10SupportVpACPI10Support, CucsPolicyPolicyScopeFsmStageName=CucsPolicyPolicyScopeFsmStageName, CucsStatsThrFloatDefinitionPropType=CucsStatsThrFloatDefinitionPropType, CucsFabricOperState=CucsFabricOperState, CucsTrigOperState=CucsTrigOperState, CucsVnicConnectionLcCtrlState=CucsVnicConnectionLcCtrlState, CucsSysdebugTechSupportFsmTaskItem=CucsSysdebugTechSupportFsmTaskItem, CucsAdaptorMenloQStatsHistThresholded=CucsAdaptorMenloQStatsHistThresholded, CucsComputePhysicalFsmCurrentFsm=CucsComputePhysicalFsmCurrentFsm, CucsObserveObservedFsmCurrentFsm=CucsObserveObservedFsmCurrentFsm, CucsExtvmmVcVersion=CucsExtvmmVcVersion, CucsSwVlanLc=CucsSwVlanLc, CucsVmHvType=CucsVmHvType, CucsMgmtBackupJob=CucsMgmtBackupJob, CucsNetworkConnectionType=CucsNetworkConnectionType, CucsEquipmentPsuStatsThresholded=CucsEquipmentPsuStatsThresholded, CucsLicenseFileState=CucsLicenseFileState, CucsMgmtExportPolicyFsmTaskItem=CucsMgmtExportPolicyFsmTaskItem, CucsTrigAckDisr=CucsTrigAckDisr, CucsAdaptorMenloNetInStatsThresholded=CucsAdaptorMenloNetInStatsThresholded, CucsFabricFcoeVsanPortEpSlotId=CucsFabricFcoeVsanPortEpSlotId, CucsFabricFcEstcType=CucsFabricFcEstcType, CucsFabricFcMonType=CucsFabricFcMonType, CucsBiosBootDevOrder=CucsBiosBootDevOrder, CucsComputeMbPowerStatsHistThresholded=CucsComputeMbPowerStatsHistThresholded, CucsAdaptorHostIfAdminState=CucsAdaptorHostIfAdminState, CucsCommSnmpNotificationType=CucsCommSnmpNotificationType, CucsVnicVnicBootDev=CucsVnicVnicBootDev, CucsFcPIoFsmStageName=CucsFcPIoFsmStageName, CucsComputeSlotQualMaxId=CucsComputeSlotQualMaxId, CucsFabricEthEstcPcEpSlotId=CucsFabricEthEstcPcEpSlotId, CucsFabricFcEstcEpPortId=CucsFabricFcEstcEpPortId, CucsMgmtEntityChassisDeviceIoState2=CucsMgmtEntityChassisDeviceIoState2, CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB=CucsBiosVfMaximumMemoryBelow4GBVpMaximumMemoryBelow4GB, CucsSysdebugLogControlEpFsmStageName=CucsSysdebugLogControlEpFsmStageName, CucsSysdebugAutoCoreFileExportTargetFsmTaskItem=CucsSysdebugAutoCoreFileExportTargetFsmTaskItem, CucsBiosVfOSBootWatchdogTimerTimeOutVpOSBootWatchdogTimerPolicy=CucsBiosVfOSBootWatchdogTimerTimeOutVpOSBootWatchdogTimerPolicy, CucsFabricFcoeSanEpSlotId=CucsFabricFcoeSanEpSlotId, CucsFabricComputeSlotEpFsmTaskItem=CucsFabricComputeSlotEpFsmTaskItem, CucsSwTargetEpType=CucsSwTargetEpType, CucsLsbootVirtualMediaOrder=CucsLsbootVirtualMediaOrder, CucsAaaDomainAuthRealm=CucsAaaDomainAuthRealm, CucsCapabilityCatalogueFsmTaskItem=CucsCapabilityCatalogueFsmTaskItem, CucsProcessorRuntimeThresholded=CucsProcessorRuntimeThresholded, CucsComputePCIeFatalStatsThresholded=CucsComputePCIeFatalStatsThresholded, CucsLsbootStorageType=CucsLsbootStorageType, CucsFabricSanCloudFsmStageName=CucsFabricSanCloudFsmStageName, CucsStorageVsanRefSwitchId=CucsStorageVsanRefSwitchId, CucsFabricFillPattern=CucsFabricFillPattern, CucsVmNicType=CucsVmNicType, CucsComputePhysicalFsmStageName=CucsComputePhysicalFsmStageName, CucsPortEthAdminSpeed=CucsPortEthAdminSpeed, CucsAdaptorLldpCapSupport=CucsAdaptorLldpCapSupport, CucsMgmtControllerFsmTaskItem=CucsMgmtControllerFsmTaskItem, CucsVmLifeCyclePolicyFsmCurrentFsm=CucsVmLifeCyclePolicyFsmCurrentFsm, CucsSwFcSanBorderFsmTaskItem=CucsSwFcSanBorderFsmTaskItem, CucsSwSanPcIfRole=CucsSwSanPcIfRole, CucsLsAgentCapability=CucsLsAgentCapability, CucsPowerGroupStatsThresholded=CucsPowerGroupStatsThresholded, CucsLsbootIScsiOrder=CucsLsbootIScsiOrder, CucsPciEquipSlotId=CucsPciEquipSlotId, CucsGmetaHolderFsmStageName=CucsGmetaHolderFsmStageName, CucsMgmtExportPolicyAdminState=CucsMgmtExportPolicyAdminState, CucsComputeIOHubEnvStatsThresholded=CucsComputeIOHubEnvStatsThresholded, CucsFabricFcMonDestEpType=CucsFabricFcMonDestEpType, CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm=CucsSysdebugManualCoreFileExportTargetFsmCurrentFsm, CucsPolicyState=CucsPolicyState, CucsLsServerFsmTaskItem=CucsLsServerFsmTaskItem, CucsAdaptorHostEthIfFsmTaskItem=CucsAdaptorHostEthIfFsmTaskItem, CucsAdaptorPIoEpIfType=CucsAdaptorPIoEpIfType, CucsFabricAEthEstcEpIfRole=CucsFabricAEthEstcEpIfRole, CucsEquipmentBeaconLedFsmTaskItem=CucsEquipmentBeaconLedFsmTaskItem, CucsFabricFcoeSanPcTransport=CucsFabricFcoeSanPcTransport, CucsCallhomeAlertThrottlingAdminState=CucsCallhomeAlertThrottlingAdminState, CucsVmInstType=CucsVmInstType, CucsEtherExternalPcLocale=CucsEtherExternalPcLocale, CucsGmetaHolderFsmTaskFlags=CucsGmetaHolderFsmTaskFlags, CucsQosclassEthBEDrop=CucsQosclassEthBEDrop, CucsAaaConfigState=CucsAaaConfigState, CucsEquipmentIOCardFsmCurrentFsm=CucsEquipmentIOCardFsmCurrentFsm, CucsEquipmentAsicType=CucsEquipmentAsicType, CucsComputeBladeFsmTaskItem=CucsComputeBladeFsmTaskItem, CucsAddressWWNMask=CucsAddressWWNMask, CucsAdaptorMenloDcePortStatsHistThresholded=CucsAdaptorMenloDcePortStatsHistThresholded, CucsSwLanEpIfRole=CucsSwLanEpIfRole, CucsMgmtImportAction=CucsMgmtImportAction, CucsEquipmentAdminPowerState=CucsEquipmentAdminPowerState, CucsSwSanEpIfRole=CucsSwSanEpIfRole, CucsFabricEthEstcEpSlotId=CucsFabricEthEstcEpSlotId, CucsAaaTacacsPlusEpFsmStageName=CucsAaaTacacsPlusEpFsmStageName, CucsFabricVlanConfigIssues=CucsFabricVlanConfigIssues, CucsExtpolSuspendState=CucsExtpolSuspendState, CucsFabricAFcSanEpTransport=CucsFabricAFcSanEpTransport, CucsFabricComputeEpIfRole=CucsFabricComputeEpIfRole, CucsSwEthLanBorderFsmCurrentFsm=CucsSwEthLanBorderFsmCurrentFsm, CucsFabricEthEstcEpPortId=CucsFabricEthEstcEpPortId, CucsStatsCollectionPolicyFsmStageName=CucsStatsCollectionPolicyFsmStageName, CucsLsServerFsmStageName=CucsLsServerFsmStageName, CucsLsbootIScsiAccess=CucsLsbootIScsiAccess, CucsBiosVfConsoleRedirectionVpFlowControl=CucsBiosVfConsoleRedirectionVpFlowControl, CucsFabricSanPcType=CucsFabricSanPcType)
