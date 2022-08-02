from pydantic import BaseSettings


class ModelSettings(BaseSettings):
    model_name: str = "/model"


model_settings = ModelSettings()
