from pathlib import Path
from grpc_tools import protoc

from src.logger import new_stream_logger
import logging

def main() -> None:
    logger = new_stream_logger(level=logging.DEBUG)
    logger.info("Starting generating python proto files.")

    ROOT = Path(__file__).resolve().parents[2]
    PROTO = ROOT / 'protobuf'
    SRC_PROTO = ROOT / 'python' / 'src' / 'proto'

    logger.info(f"listing .proto files from {str(PROTO)}...")
    files = (str(p) for p in PROTO.glob("*.proto"))
    files = " ".join(files)
    logger.info(f"These files will be compiled: {files}")

    protoc.main(("", f"-I={str(PROTO)}", f"--python_out={str(SRC_PROTO)}",
            f"--grpc_out={str(SRC_PROTO)}", ""))
    logger.info("Finished generating python proto files.")


if __name__ == "__main__":
    main()
