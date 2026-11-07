import sys

from flintmc.output.err_output import err_output


def error(message: str, /, *, exit_code: int = 1) -> None:
    match exit_code:
        case 70:
            extra = (
                "This is likely an internal error, not an error of the "
                "source code. Please create an issue in the "
                "[link URL=https://github.com/wvhugoliyh/flintmc/issues]"
                "FlintMC GitHub repository[/link].")
        case _:
            extra = ""

    err_output.print(f"Error: {message}", style="error")

    if extra:
        err_output.print("\n")
        err_output.print(extra, style="error")

    sys.exit(exit_code)