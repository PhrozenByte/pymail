"""
pymail

pymail is a simple Python script to synchronously send emails via SMTP.
It is often used on satellite systems without a fully-featured MTA.

Copyright (C) 2017-2022  Daniel Rudolf <https://www.daniel-rudolf.de>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License only.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

SPDX-License-Identifier: GPL-3.0-only
"""

from distutils.core import setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="pymail",
    version="0.0.1",
    description="Simple Python script to synchronously send emails via SMTP. " +
        "It is often used on satellite systems without a fully-featured MTA.",
    long_description=readme,
    author="Daniel Rudolf",
    author_email="pymail@daniel-rudolf.de",
    url="https://github.com/PhrozenByte/pymail",
    license=license,
    py_modules=[ "pymail" ],
    scripts=[ "pymail" ]
)
