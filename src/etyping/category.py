from __future__ import annotations

import enum


class Category(
    enum.IntEnum,
):
    ROMA: int = 0
    ENGLISH: int = 2

    @classmethod
    def from_str(
        cls,
        s: str,
    ) -> Category:
        return cls.ROMA if s == "roma" else cls.ENGLISH
