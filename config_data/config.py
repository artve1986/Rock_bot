from dataclasses import dataclass
from environs import Env  # pip install environs


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('Bot_tok')))


if __name__ == '__main__':
    print(load_config().tg_bot.token)
