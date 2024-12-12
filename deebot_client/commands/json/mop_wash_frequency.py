"""Mop Auto-Wash Frequency command module."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Any

from deebot_client.command import InitParam
from deebot_client.events import MopWashFrequency, MopWashFrequencyEvent
from deebot_client.message import HandlingResult
from deebot_client.util import get_enum

from .common import JsonGetCommand, JsonSetCommand

if TYPE_CHECKING:
    from deebot_client.event_bus import EventBus


class GetMopWashFrequency(JsonGetCommand):
    """Get Mop Auto-Wash Frequency command."""

    name = "getWashInfo"

    @classmethod
    def _handle_body_data_dict(
        cls, event_bus: EventBus, data: dict[str, Any]
    ) -> HandlingResult:
        """Handle message->body->data and notify the correct event subscribers.

        :return: A message response
        """
        event_bus.notify(MopWashFrequencyEvent(MopWashFrequency(int(data["interval"]))))
        return HandlingResult.success()


class SetMopWashFrequency(JsonSetCommand):
    """Set Mop Auto-Wash Frequency command."""

    name = "setWashInfo"
    get_command = GetMopWashFrequency
    _mqtt_params = MappingProxyType({"interval": InitParam(MopWashFrequency)})

    def __init__(self, interval: MopWashFrequency | str) -> None:
        if isinstance(interval, str):
            interval = get_enum(MopWashFrequency, interval)
        super().__init__({"interval": interval.value})
