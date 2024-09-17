from pysnmp.smi import rfc1902
from config import mib
from log_config import setup_logger
import time


logger = setup_logger('system_log', 'systemlog.log')


class IpParser:
    def __init__(self, data) -> None:
        self.data = data

    def get_ip(self) -> str:
        return '.'.join(self.data[0:4])

    def get_mask(self) -> str:
        return '.'.join(self.data[5:9])

    def get_gw(self) -> str:
        return '.'.join(self.data[9:])

    def get_route(self) -> str:
        ip = self.get_ip()
        gw = self.get_gw()
        mask = self.get_mask()

        return (f'{ip} {mask} {gw}')


class MIBEntry:
    def __init__(self, entry: str) -> None:
        self.full_entry = entry
        self.parse_entry()

    def parse_entry(self) -> None:
        if "::" in self.full_entry:
            _, _, rest = self.full_entry.partition('::')
            self.name, *self.numbers = rest.split('.')
        else:
            self.name = self.full_entry
            self.numbers = self.full_entry

    def get_name(self) -> str:
        try:
            return self.name
        except Exception as e:
            logger.error("Failed to resolve: %s", str(e))
            return self.full_entry

    def get_numbers(self) -> list[str]:
        return self.numbers


class Resolve:
    def __init__(self, data: str) -> None:
        self.data = data
        self.resolved()

    def resolved(self) -> None:
        try:
            self.resolve = rfc1902.ObjectIdentity(self.data).resolveWithMib(mib)
        except Exception as e:
            self.resolve = self.data
            logger.error("Failed to resolve: %s", str(e))

    def get_resolve(self) -> str:
        if self.resolve:
            try:
                return self.resolve.prettyPrint()
            except Exception as e:
                self.resolve = self.data
                logger.error("Failed to resolve: %s", str(e))
        return self.resolve


def GetUptime(uptime):

    uptime_seconds = uptime / 100

    uptime_struct = time.gmtime(uptime_seconds)

    uptime_days = uptime_seconds // (24 * 3600)
    formatted_time = time.strftime(f"{int(uptime_days)} days, %H hours, %M minutes, %S seconds", uptime_struct)
    return formatted_time


if __name__ == "__main__":
    x = "1.3.6.1.4.1.2011.5.25.41.1.20"
    result = Resolve(x).get_resolve()
    print(result)
    print(MIBEntry(result).get_name())
    z = GetUptime("323231231")
    print(z)