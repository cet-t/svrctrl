import enum


class Operation(enum.IntEnum):
    Boot = 0x01
    Reboot = 0x02
    Shutdown = 0x04
