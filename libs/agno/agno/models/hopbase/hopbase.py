from dataclasses import dataclass, field
from os import getenv
from typing import Any, Dict, Optional

from agno.exceptions import ModelAuthenticationError
from agno.models.openai.like import OpenAILike


@dataclass
class HopBase(OpenAILike):
    """
    A class for interacting with HopBase, an OpenAI-compatible AI API gateway.

    HopBase serves GPT, Claude, Gemini and Grok models next to DeepSeek, GLM, Kimi and Qwen
    behind one base URL. `GET /v1/models` lists the model ids the API key can call.

    Attributes:
        id (str): The id of the HopBase model to use. Default is "glm-5.3".
        name (str): The name of this chat model instance. Default is "HopBase".
        provider (str): The provider of the model. Default is "HopBase".
        api_key (str): The api key to authorize request to HopBase.
        base_url (str): The base url to which the requests are sent.
            Defaults to "https://api.hop-base.com/v1".
    """

    id: str = "glm-5.3"
    name: str = "HopBase"
    provider: str = "HopBase"
    api_key: Optional[str] = field(default_factory=lambda: getenv("HOPBASE_API_KEY"))
    base_url: str = "https://api.hop-base.com/v1"

    def _get_client_params(self) -> Dict[str, Any]:
        """
        Returns client parameters for API requests, checking for HOPBASE_API_KEY.

        Returns:
            Dict[str, Any]: A dictionary of client parameters for API requests.
        """
        if not self.api_key:
            self.api_key = getenv("HOPBASE_API_KEY")
            if not self.api_key:
                raise ModelAuthenticationError(
                    message="HOPBASE_API_KEY not set. Please set the HOPBASE_API_KEY environment variable.",
                    model_name=self.name,
                )
        return super()._get_client_params()
