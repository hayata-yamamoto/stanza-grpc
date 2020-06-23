from logging import Logger, StreamHandler, Formatter, getLogger


def new_stream_logger(level: int, fmt: str = "text") -> Logger:
    """
    `level` のログを標準出力に流すルートロガーを生成する。
    Args:
        level:
        fmt: text / json
    """
    logger = getLogger()
    logger.setLevel(level)
    handler = StreamHandler()
    handler.setLevel(level)

    if fmt == "text":
        formatter = Formatter("[%(levelname)s] %(asctime)s - %(pathname)s:%(lineno)d %(funcName)s - %(message)s")
        handler.setFormatter(formatter)
    elif fmt == "json":
        raise NotImplementedError("Json formatter not implemented")
    else:
        raise ValueError(f"Unsupported format: {fmt}")

    logger.addHandler(handler)
    return logger