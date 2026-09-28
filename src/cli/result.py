import enum

ERR_MASK = 0x1000


class Result(enum.IntEnum):
    Ok = 0x0000
    Err = 0x1000
    AlreadyBoot = 0x1001
