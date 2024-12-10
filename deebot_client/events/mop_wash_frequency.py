"""Mop Auto-Wash Frequency event module."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, unique

from .base import Event


@unique
class MopWashFrequency(IntEnum):
    """Enum class for all possible mop auto-wash frequencies."""

    TEN_MINUTES = 10
    FIFTEEN_MINUTES = 15
    TWENTY_FIVE_MINUTES = 25


@dataclass(frozen=True)
class MopWashFrequencyEvent(Event):
    """Mop Auto-Wash Frequency event representation."""

    interval: MopWashFrequency