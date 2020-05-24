import stanza
from src.env import Env


def main() -> None:
    stanza.download(Env.LANGUAGE)


if __name__ == "__main__":
    main()
