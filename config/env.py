import environ # type: ignore
from pathlib import Path

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

#environ.Env.read_env(os.path.join(BASE_DIR, '.env'))