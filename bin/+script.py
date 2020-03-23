#!/usr/bin/env python3
import click
from plus import template
import plus
from plus import conf
from typing import Any
import os
import subprocess
import plus

@click.command()
@click.argument("name", nargs=1)
@click.argument("args", nargs=-11)
def main(name: str, args: Any) -> None:
    "Creates script"
    if name.endswith('.py'):
        template_ = 'plus_python_script'
    else:
        template_ = 'shell-template'

    source = template.expand(template_, sname=name, args=args)
    actual_path = os.path.join(os.path.abspath('./'), name)

    # here
    with open(actual_path, 'w') as fp:
        fp.write(source)
        os.chmod(name, 0o744)

    plus.edit(name)


if __name__ == '__main__':
    plus.monitored()
    main()
