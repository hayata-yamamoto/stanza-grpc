from src.server import init_server
from src.logger import new_stream_logger
import logging


def main() -> None:
    new_stream_logger(level=logging.DEBUG)
    server = init_server()

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
