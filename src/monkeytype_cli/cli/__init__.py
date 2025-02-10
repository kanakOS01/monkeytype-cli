# SPDX-FileCopyrightText: 2025-present Kanak Tanwar <kanaktanwarpro@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from monkeytype_cli.__about__ import __version__
from monkeytype_cli.tui.main import page


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="monkeytype-cli")
def monkeytype_cli():
    page.run(inline=False)