# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from bedrock.base.config_manager import config


@pytest.fixture(scope="session")
def base_url(base_url, request):
    return base_url or request.getfixturevalue("live_server").url


@pytest.fixture(scope="session")
def pocket_base_url(request):
    base_url = config("BASE_POCKET_URL", parser=str, default="")
    if not base_url:
        pytest.skip("No BASE_POCKET_URL detected in env vars")
    return base_url
