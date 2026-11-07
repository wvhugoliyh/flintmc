from flintmc.output.err_output import err_output


def warn(message: str, /) -> None:
    err_output.print(message, style="warning")