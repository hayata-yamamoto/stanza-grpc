from pathlib import Path
from grpc_tools import protoc

from src.logger import new_stream_logger
import logging


def main() -> None:
    logger = new_stream_logger(level=logging.DEBUG)

    ROOT = Path(__file__).resolve().parents[1]
    PROTO = ROOT / 'proto'
    SRC_PROTO = ROOT / 'src' / 'pb2'
    SRC_PROTO.mkdir(parents=True, exist_ok=True)

    files = [str(p) for p in PROTO.glob("*.proto")]
    # files = " ".join(files)
    logger.info(f"These files will be compiled: {files}")

    for file in files:
        res = protoc.main([
            "", f"--proto_path={str(PROTO)}", f"--python_out={str(SRC_PROTO)}",
            f"--mypy_out={str(SRC_PROTO)}",
            f"--grpc_python_out={str(SRC_PROTO)}", file
        ])
    if res == 1:
        logger.error("compile error")
    else:
        logger.info("Finished generating python proto files.")


if __name__ == "__main__":
    main()
