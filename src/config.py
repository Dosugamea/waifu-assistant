import os
from dotenv import dotenv_values


class Config:
    MODEL_PROVIDER = ""
    MODEL_NAME = ""
    HUGGINGFACEHUB_API_TOKEN = ""
    OPENAI_API_KEY = ""
    COHERE_API_KEY = ""
    SERPAPI_API_KEY = ""
    GOOGLE_CSE_ID = ""
    GOOGLE_API_KEY = ""

    def __init__(self):
        config = {
            **dotenv_values(".env"),
            **os.environ,
        }
        self.MODEL_PROVIDER = self.__get_key(config, "MODEL_PROVIDER")
        self.MODEL_NAME = self.__get_key(config, "MODEL_NAME")
        self.HUGGINGFACEHUB_API_TOKEN = self.__get_key(
            config, "HUGGINGFACEHUB_API_TOKEN"
        )
        self.OPENAI_API_KEY = self.__get_key(config, "OPENAI_API_KEY")
        self.COHERE_API_KEY = self.__get_key(config, "COHERE_API_KEY")
        self.SERPAPI_API_KEY = self.__get_key(config, "SERPAPI_API_KEY")
        self.GOOGLE_CSE_ID = self.__get_key(config, "GOOGLE_CSE_ID")
        self.GOOGLE_API_KEY = self.__get_key(config, "GOOGLE_API_KEY")

    def __get_key(self, config: dict[str, str], key: str) -> str:
        return config[key] if key in config else ""
