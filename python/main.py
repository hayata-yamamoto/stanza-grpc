from src.env import Env
from src import init_server, init_route, init_reflection


def main() -> None:
    server = init_server(Env.NUM_THREADS)
    init_route(server)
    init_reflection(server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
