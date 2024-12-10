from __future__ import annotations

from typing import Any

import pytest

from deebot_client.commands.json import GetMopWashFrequency, SetMopWashFrequency
from deebot_client.events import MopWashFrequency, MopWashFrequencyEvent
from tests.helpers import (
    get_request_json,
    get_success_body,
)

from . import assert_command, assert_set_command


@pytest.mark.parametrize(
    ("json", "expected"),
    [
        ({"interval": 10}, MopWashFrequencyEvent(MopWashFrequency.TEN_MINUTES)),
        ({"interval": 15}, MopWashFrequencyEvent(MopWashFrequency.FIFTEEN_MINUTES)),
        ({"interval": 25}, MopWashFrequencyEvent(MopWashFrequency.TWENTY_FIVE_MINUTES)),
    ],
)
async def test_GetMopWashFrequency(
    json: dict[str, Any], expected: MopWashFrequencyEvent
) -> None:
    json = get_request_json(get_success_body(json))
    await assert_command(GetMopWashFrequency(), json, expected)


@pytest.mark.parametrize(("value"), [MopWashFrequency.TEN_MINUTES, "10"])
async def test_SetMopWashFrequency(value: MopWashFrequency | str) -> None:
    command = SetMopWashFrequency(value)
    args = {"interval": 10}
    await assert_set_command(
        command, args, MopWashFrequencyEvent(MopWashFrequency.TEN_MINUTES)
    )
