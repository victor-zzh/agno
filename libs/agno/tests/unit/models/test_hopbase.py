import os
from unittest.mock import patch

import pytest

from agno.exceptions import ModelAuthenticationError
from agno.models.hopbase import HopBase
from agno.models.utils import get_model, get_model_from_dict


def test_hopbase_initialization_with_api_key():
    model = HopBase(id="glm-5.3", api_key="test-api-key")
    assert model.id == "glm-5.3"
    assert model.api_key == "test-api-key"
    assert model.base_url == "https://api.hop-base.com/v1"


def test_hopbase_initialization_without_api_key():
    with patch.dict(os.environ, {}, clear=True):
        model = HopBase(id="glm-5.3")
        client_params = None
        with pytest.raises(ModelAuthenticationError):
            client_params = model._get_client_params()
        assert client_params is None


def test_hopbase_does_not_fall_back_to_openai_api_key():
    with patch.dict(os.environ, {"OPENAI_API_KEY": "sk-should-not-be-used"}, clear=True):
        model = HopBase(id="glm-5.3")
        with pytest.raises(ModelAuthenticationError):
            model._get_client_params()
        assert model.api_key != "sk-should-not-be-used"


def test_hopbase_initialization_with_env_api_key():
    with patch.dict(os.environ, {"HOPBASE_API_KEY": "env-api-key"}):
        model = HopBase(id="glm-5.3")
        assert model.api_key == "env-api-key"


def test_hopbase_client_params():
    model = HopBase(id="gpt-6.1-sol", api_key="test-api-key")
    client_params = model._get_client_params()
    assert client_params["api_key"] == "test-api-key"
    assert client_params["base_url"] == "https://api.hop-base.com/v1"


def test_hopbase_default_values():
    model = HopBase(api_key="test-api-key")
    assert model.id == "glm-5.3"
    assert model.name == "HopBase"
    assert model.provider == "HopBase"


def test_hopbase_resolves_from_string_syntax():
    model = get_model("hopbase:gpt-6.1-sol")
    assert isinstance(model, HopBase)
    assert model.id == "gpt-6.1-sol"


def test_hopbase_round_trips_through_dict():
    model = HopBase(id="claude-sonnet-5-5", api_key="test-api-key")
    rebuilt = get_model_from_dict(model.to_dict())
    assert isinstance(rebuilt, HopBase)
    assert rebuilt.id == "claude-sonnet-5-5"
