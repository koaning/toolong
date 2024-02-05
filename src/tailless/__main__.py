import click

from tailless.ui import UI


@click.command()
@click.argument("files", metavar="FILE1 FILE2", nargs=-1)
@click.option("-m", "--merge", is_flag=True, help="Merge files")
def run(files: list[str], merge: bool):
    """View / tail / search log files."""
    if not files:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()
    ui = UI(files, merge=merge)
    ui.run()


if __name__ == "__main__":
    run()
