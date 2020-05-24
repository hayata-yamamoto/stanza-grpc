from pathlib import Path
from grpc_tools import protoc

from logging import getLogger


def main() -> None:
    logger = getLogger(__name__)
    logger.info("Starting generating python proto files.")

    ROOT = Path(__file__).resolve().parents[3]
    PROTO = ROOT / 'proto'
    SRC_PROTO = ROOT / 'src' / 'proto'

    logger.info(f"listing .proto files from {str(PROTO)}...")
    files = (str(p) for p in PROTO.glob("*.proto"))
    files = " ".join(files)
    logger.info(f"These files will be compiled: {files}")

    protoc(("", f"-I={str(PROTO)}", f"--python_out={str(SRC_PROTO)}",
            f"--grpc_out={str(SRC_PROTO)}", ""))
    logger.info("Finished generating python proto files.")


if __name__ == "__main__":
    main()
