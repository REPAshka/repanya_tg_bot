from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    bots: TgBot
    misc: Miscellaneous



def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        bots=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        misc=Miscellaneous()
    )


settings = load_config('/home/repa/my_projects/repanya_tg_bot/.env')