#
# PySNMP MIB module A3COM-HUAWEI-NDEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-NDEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
mlsr, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "mlsr")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Counter32, MibIdentifier, Counter64, ModuleIdentity, Unsigned32, Integer32, Bits, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32", "Integer32", "Bits", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
huaweiNDEC = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2))
huaweiNDEC.setRevisions(('2004-09-15 10:52',))
if mibBuilder.loadTexts: huaweiNDEC.setLastUpdated('200409150000Z')
if mibBuilder.loadTexts: huaweiNDEC.setOrganization('HUAWEI Technologies Co., Ltd.')
hipsNDECSAListTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1), )
if mibBuilder.loadTexts: hipsNDECSAListTable.setStatus('current')
hipsNDECSAListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-NDEC-MIB", "hipsPeerIpAddr"), (0, "A3COM-HUAWEI-NDEC-MIB", "hipsProtocol"), (0, "A3COM-HUAWEI-NDEC-MIB", "hipsSPI"))
if mibBuilder.loadTexts: hipsNDECSAListEntry.setStatus('current')
hipsPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsPeerIpAddr.setStatus('current')
hipsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(50, 51))).clone(namedValues=NamedValues(("ipsecEsp", 50), ("ipsecAh", 51)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsProtocol.setStatus('current')
hipsSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(256, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSPI.setStatus('current')
hipsEncAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ealgNone", 1), ("ealgDescbc", 2), ("ealg3desCbc", 3), ("ealgXBlf", 4), ("ealgXCast", 5), ("ealgXSkipjack", 6), ("ealgXAes", 7), ("ealgXQc5", 8), ("ealgXNsa", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsEncAlgorithm.setStatus('current')
hipsAuthAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("aalgNone", 1), ("aalgMd5Hmac", 2), ("aalgSha1Hmac", 3), ("aalgMd5Hmac96", 4), ("aalgSha1Hmac96", 5), ("aalgXRipeMd160Hmac96", 6), ("aalgXMd5", 7), ("aalgXSha1", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsAuthAlgorithm.setStatus('current')
hipsLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsLocalIpAddr.setStatus('current')
hipsSaLifeKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSaLifeKBytes.setStatus('current')
hipsSaLifeSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSaLifeSecond.setStatus('current')
hipsByCard = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsByCard.setStatus('current')
hipsNegotiateSaMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("isakmp", 2), ("manual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsNegotiateSaMode.setStatus('current')
hipsExpBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsExpBytes.setStatus('current')
hipsSoftBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSoftBytes.setStatus('current')
hipsExpTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsExpTimeout.setStatus('current')
hipsSoftTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 1, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsSoftTimeout.setStatus('current')
hikeSATable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2), )
if mibBuilder.loadTexts: hikeSATable.setStatus('current')
hikeSAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-NDEC-MIB", "hikeConnId"))
if mibBuilder.loadTexts: hikeSAEntry.setStatus('current')
hikeConnId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikeConnId.setStatus('current')
hikePeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikePeerIpAddr.setStatus('current')
hikeFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikeFlag.setStatus('current')
hikePhase = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unkown", 1), ("phase1", 2), ("phase2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikePhase.setStatus('current')
hikeDoi = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unkown", 1), ("ipsec", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hikeDoi.setStatus('current')
hikeClearSA = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hikeClearSA.setStatus('current')
hipsIKEPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3), )
if mibBuilder.loadTexts: hipsIKEPolicyTable.setStatus('current')
hipsIKEPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-NDEC-MIB", "hipsIsakmpPolPriority"))
if mibBuilder.loadTexts: hipsIKEPolicyEntry.setStatus('current')
hipsIsakmpPolPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolPriority.setStatus('current')
hipsIsakmpPolEncr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("ikeEncryptNone", 1), ("ikeEncryptDesCbc", 2), ("ikeEncryptIdeaCbc", 3), ("ikeEncryptBlowfishcbc", 4), ("ikeEncryptRc5R16B64cbc", 5), ("ikeEncrypt3DesCbc", 6), ("ikeEncryptCastCbc", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolEncr.setStatus('current')
hipsIsakmpPolHash = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ikeHashNone", 1), ("ikeHashMd5", 2), ("ikeHashSha", 3), ("ikeHashTiger", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolHash.setStatus('current')
hipsIsakmpPolAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ikeAuthPreNone", 1), ("ikeAuthPreShared", 2), ("ikeAuthDss", 3), ("ikeAuthRsaSig", 4), ("ikeAuthRsaEnc", 5), ("ikeAuthRsaEncRev", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolAuth.setStatus('current')
hipsIsakmpPolGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("dhGroup1", 2), ("dhGroup2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolGroup.setStatus('current')
hipsIsakmpPolLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 3, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsakmpPolLifetime.setStatus('current')
hipsStaticCryptomapTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4), )
if mibBuilder.loadTexts: hipsStaticCryptomapTable.setStatus('current')
hipsStaticCryptomapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-NDEC-MIB", "hipsStaticCryptomapName"), (0, "A3COM-HUAWEI-NDEC-MIB", "hipsStaticCryptomapSN"))
if mibBuilder.loadTexts: hipsStaticCryptomapEntry.setStatus('current')
hipsStaticCryptomapName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapName.setStatus('current')
hipsStaticCryptomapSN = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapSN.setStatus('current')
hipsStaticCryptomapNegMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("isakmp", 2), ("manual", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapNegMode.setStatus('current')
hipsStaticCryptomapMatchAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapMatchAddr.setStatus('current')
hipsStaticCryptomapPeerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapPeerIpAddr.setStatus('current')
hipsStaticCryptomapTransforName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapTransforName.setStatus('current')
hipsStaticCryptomapLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapLifetime.setStatus('current')
hipsStaticCryptomapLifesize = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapLifesize.setStatus('current')
hipsStaticCryptomapLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsStaticCryptomapLocalIpAddr.setStatus('current')
hipsIfNameUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIfNameUsed.setStatus('current')
hipsInAHSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInAHSPI.setStatus('current')
hipsInESPSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInESPSPI.setStatus('current')
hipsOutAHSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 13), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutAHSPI.setStatus('current')
hipsOutESPSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutESPSPI.setStatus('current')
hipsInAhHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInAhHexKeyString.setStatus('current')
hipsInEspCipherHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInEspCipherHexKeyString.setStatus('current')
hipsInEspAuthenHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInEspAuthenHexKeyString.setStatus('current')
hipsInAhStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInAhStringKeyString.setStatus('current')
hipsInEspStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInEspStringKeyString.setStatus('current')
hipsOutAhHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutAhHexKeyString.setStatus('current')
hipsOutEspCipherHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutEspCipherHexKeyString.setStatus('current')
hipsOutEspAuthenHexKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutEspAuthenHexKeyString.setStatus('current')
hipsOutAhStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutAhStringKeyString.setStatus('current')
hipsOutEspStringKeyString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 4, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutEspStringKeyString.setStatus('current')
hipsTransformNameSetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5), )
if mibBuilder.loadTexts: hipsTransformNameSetTable.setStatus('current')
hipsTransformNameSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1), ).setIndexNames((0, "A3COM-HUAWEI-NDEC-MIB", "hipsTransformName"))
if mibBuilder.loadTexts: hipsTransformNameSetEntry.setStatus('current')
hipsTransformName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsTransformName.setStatus('current')
hipsTransformMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tunnel", 1), ("transport", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsTransformMode.setStatus('current')
hipsTransformProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ipsecNone", 1), ("ipsecAhNew", 2), ("ipsecAhEspNew", 3), ("ipsecAhEspOld", 4), ("ipsecAhOld", 5), ("ipsecEspNew", 6), ("ipsecEspAhNew", 7), ("ipsecEspAhOld", 8), ("ipsecEspOld", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsTransformProtocol.setStatus('current')
hipsAH = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("aalgNone", 1), ("aalgMd5Hmac", 2), ("aalgSha1Hmac", 3), ("aalgMd5Hmac96", 4), ("aalgSha1Hmac96", 5), ("aalgXRipeMd160Hmac96", 6), ("aalgXMd5", 7), ("aalgXSha1", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsAH.setStatus('current')
hipsEespEn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ealgNone", 1), ("ealgDescbc", 2), ("ealg3desCbc", 3), ("ealgXBlf", 4), ("ealgXCast", 5), ("ealgXSkipjack", 6), ("ealgXAes", 7), ("ealgXQc5", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsEespEn.setStatus('current')
hipsEspAu = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("aalgNone", 1), ("aalgMd5Hmac", 2), ("aalgSha1Hmac", 3), ("aalgMd5Hmac96", 4), ("aalgSha1Hmac96", 5), ("aalgXRipeMd160Hmac96", 6), ("aalgXMd5", 7), ("aalgXSha1", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsEspAu.setStatus('current')
hipsIsCardTransform = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 5, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsIsCardTransform.setStatus('current')
hipsNDECInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6), )
if mibBuilder.loadTexts: hipsNDECInfoTable.setStatus('current')
hipsNDECInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1), ).setIndexNames((0, "A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"))
if mibBuilder.loadTexts: hipsNDECInfoEntry.setStatus('current')
hipsCardSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardSlot.setStatus('current')
hipsInPac = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInPac.setStatus('current')
hipsOutPac = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutPac.setStatus('current')
hipsInByte = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsInByte.setStatus('current')
hipsOutByte = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsOutByte.setStatus('current')
hipsDropPac = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsDropPac.setStatus('current')
hipsCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ecStateInvalid", 1), ("ecStateReady", 2), ("ecStateResetting", 3), ("ecStateProgramUpdating", 4), ("ecStateDisable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardStatus.setStatus('current')
hipsCardHardVer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardHardVer.setStatus('current')
hipsCardSoftVer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardSoftVer.setStatus('current')
hipsCardCPLDVer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsCardCPLDVer.setStatus('current')
hipsCardOperate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cardClearStatic", 1), ("cardReset", 2), ("cardSynTime", 3), ("cardSysLogOn", 4), ("cardSysLogOff", 5), ("cardSysLogClear", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hipsCardOperate.setStatus('current')
hipsDropPacInUnitTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 6, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsDropPacInUnitTime.setStatus('current')
hipsNDECLeaf = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 7))
hipsNDECConnections = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipsNDECConnections.setStatus('current')
hipsNDECBackup = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hipsNDECBackup.setStatus('current')
hipsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8))
hipsNDECNormalResetTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8, 1)).setObjects(("A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"), ("A3COM-HUAWEI-NDEC-MIB", "hipsCardHardVer"), ("A3COM-HUAWEI-NDEC-MIB", "hipsCardSoftVer"), ("A3COM-HUAWEI-NDEC-MIB", "hipsCardCPLDVer"))
if mibBuilder.loadTexts: hipsNDECNormalResetTrap.setStatus('current')
hipsNDECStateChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8, 2)).setObjects(("A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"), ("A3COM-HUAWEI-NDEC-MIB", "hipsCardStatus"))
if mibBuilder.loadTexts: hipsNDECStateChangeTrap.setStatus('current')
hipsNDECFlowTrap = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 33, 2, 8, 3)).setObjects(("A3COM-HUAWEI-NDEC-MIB", "hipsCardSlot"), ("A3COM-HUAWEI-NDEC-MIB", "hipsDropPacInUnitTime"))
if mibBuilder.loadTexts: hipsNDECFlowTrap.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-NDEC-MIB", hipsProtocol=hipsProtocol, hipsInAHSPI=hipsInAHSPI, hipsIsakmpPolPriority=hipsIsakmpPolPriority, hipsSoftTimeout=hipsSoftTimeout, hipsLocalIpAddr=hipsLocalIpAddr, hikePeerIpAddr=hikePeerIpAddr, hipsIsakmpPolHash=hipsIsakmpPolHash, hipsTransformNameSetTable=hipsTransformNameSetTable, hipsInAhHexKeyString=hipsInAhHexKeyString, hipsStaticCryptomapEntry=hipsStaticCryptomapEntry, hipsIsakmpPolEncr=hipsIsakmpPolEncr, hikeDoi=hikeDoi, hipsExpTimeout=hipsExpTimeout, hipsNDECNormalResetTrap=hipsNDECNormalResetTrap, hipsPeerIpAddr=hipsPeerIpAddr, hipsNDECStateChangeTrap=hipsNDECStateChangeTrap, hipsInEspAuthenHexKeyString=hipsInEspAuthenHexKeyString, hipsTransformName=hipsTransformName, hipsCardHardVer=hipsCardHardVer, hipsStaticCryptomapPeerIpAddr=hipsStaticCryptomapPeerIpAddr, hikePhase=hikePhase, hipsStaticCryptomapNegMode=hipsStaticCryptomapNegMode, hikeClearSA=hikeClearSA, hipsNDECFlowTrap=hipsNDECFlowTrap, hipsStaticCryptomapLocalIpAddr=hipsStaticCryptomapLocalIpAddr, hipsNDECSAListEntry=hipsNDECSAListEntry, hipsCardSoftVer=hipsCardSoftVer, hipsInAhStringKeyString=hipsInAhStringKeyString, hipsSPI=hipsSPI, hipsDropPac=hipsDropPac, hipsOutPac=hipsOutPac, hipsOutAhStringKeyString=hipsOutAhStringKeyString, hipsInByte=hipsInByte, hipsEncAlgorithm=hipsEncAlgorithm, hikeSATable=hikeSATable, hipsTransformNameSetEntry=hipsTransformNameSetEntry, hipsIsakmpPolGroup=hipsIsakmpPolGroup, hipsOutEspCipherHexKeyString=hipsOutEspCipherHexKeyString, hikeSAEntry=hikeSAEntry, hipsNDECInfoEntry=hipsNDECInfoEntry, hipsAuthAlgorithm=hipsAuthAlgorithm, hipsCardSlot=hipsCardSlot, hipsNDECSAListTable=hipsNDECSAListTable, hipsDropPacInUnitTime=hipsDropPacInUnitTime, hipsOutEspAuthenHexKeyString=hipsOutEspAuthenHexKeyString, PYSNMP_MODULE_ID=huaweiNDEC, hipsExpBytes=hipsExpBytes, hipsSoftBytes=hipsSoftBytes, hipsTransformMode=hipsTransformMode, hipsStaticCryptomapLifesize=hipsStaticCryptomapLifesize, hipsInEspStringKeyString=hipsInEspStringKeyString, hipsByCard=hipsByCard, hipsSaLifeSecond=hipsSaLifeSecond, hikeConnId=hikeConnId, hikeFlag=hikeFlag, hipsOutESPSPI=hipsOutESPSPI, hipsNDECLeaf=hipsNDECLeaf, hipsIsCardTransform=hipsIsCardTransform, hipsInESPSPI=hipsInESPSPI, hipsStaticCryptomapMatchAddr=hipsStaticCryptomapMatchAddr, hipsIfNameUsed=hipsIfNameUsed, hipsIsakmpPolAuth=hipsIsakmpPolAuth, hipsOutEspStringKeyString=hipsOutEspStringKeyString, hipsTraps=hipsTraps, hipsNDECInfoTable=hipsNDECInfoTable, hipsNegotiateSaMode=hipsNegotiateSaMode, hipsStaticCryptomapLifetime=hipsStaticCryptomapLifetime, hipsOutAhHexKeyString=hipsOutAhHexKeyString, hipsSaLifeKBytes=hipsSaLifeKBytes, hipsEspAu=hipsEspAu, hipsIKEPolicyTable=hipsIKEPolicyTable, hipsNDECBackup=hipsNDECBackup, hipsOutByte=hipsOutByte, hipsStaticCryptomapTransforName=hipsStaticCryptomapTransforName, hipsEespEn=hipsEespEn, hipsInEspCipherHexKeyString=hipsInEspCipherHexKeyString, hipsNDECConnections=hipsNDECConnections, hipsIKEPolicyEntry=hipsIKEPolicyEntry, hipsCardCPLDVer=hipsCardCPLDVer, hipsStaticCryptomapTable=hipsStaticCryptomapTable, hipsStaticCryptomapSN=hipsStaticCryptomapSN, hipsStaticCryptomapName=hipsStaticCryptomapName, hipsCardOperate=hipsCardOperate, hipsTransformProtocol=hipsTransformProtocol, hipsInPac=hipsInPac, hipsIsakmpPolLifetime=hipsIsakmpPolLifetime, hipsOutAHSPI=hipsOutAHSPI, hipsCardStatus=hipsCardStatus, hipsAH=hipsAH, huaweiNDEC=huaweiNDEC)
