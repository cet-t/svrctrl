import enum

ERR_MASK = 0x1000


class Result(enum.IntEnum):
    Ok = 0x0000
    Err = 0x1000
    AlreadyBoot = 0x1001
    NotBoot = 0x1002

    @classmethod
    def is_ok(cls) -> bool:
        return cls == cls.Ok

    @classmethod
    def is_err(cls) -> bool:
        return not cls.is_ok()
