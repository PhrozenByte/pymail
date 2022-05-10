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

import email.mime.text, email.policy, email.utils, enum, getpass, smtplib, socket, ssl

__version__ = "0.0.1"

class PyMail(object):
    SECURE = enum.Enum("SECURE", "NONE SSL STARTTLS")

    _host = None
    _port = None
    _secure = SECURE.NONE
    _username = None
    _password = None

    _smtp = None

    def __init__(self, host, port=None, secure=None, username=None, password=None):
        if secure is None:
            secure = self.SECURE.STARTTLS

        if port is None:
            if secure == self.SECURE.STARTTLS:
                port = 587
            elif secure == self.SECURE.SSL:
                port = 465
            else:
                port = 25

        self._host = host
        self._port = port
        self._secure = secure
        self._username = username
        self._password = password

    @property
    def _server(self):
        if self._smtp is None:
            self._open()
            self._login()

        return self._smtp

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self._close()

    def _open(self):
        self._close()

        if self._secure == self.SECURE.SSL:
            context = ssl.create_default_context()
            self._smtp = smtplib.SMTP_SSL(self._host, self._port, context=context)
        else:
            self._smtp = smtplib.SMTP(self._host, self._port)
            if self._secure == self.SECURE.STARTTLS:
                context = ssl.create_default_context()
                self._smtp.starttls(context=context)

    def _login(self):
        if not self._smtp:
            raise RuntimeError("SMTP connection wasn't initialized yet")

        if self._username and self._password:
            self._smtp.login(self._username, self._password)

    def _close(self):
        if self._smtp:
            self._smtp.quit()
            self._smtp = None

    def message(self, body, subject=None, mailFrom=None, mailTo=None, headers=None):
        message = email.mime.text.MIMEText(body)
        message.policy = email.policy.SMTP

        if headers is not None:
            for header in headers:
                message[header] = headers[header]

        if "Date" not in message:
            message["Date"] = email.utils.formatdate()

        if subject:
            message["Subject"] = subject

        if mailFrom:
            message["From"] = mailFrom
        elif "From" not in message:
            message["From"] = _getDefaultMailFrom()

        if mailTo:
            if isinstance(mailTo, str):
                mailTo = [ mailTo ]
            for address in mailTo:
                message["To"] = address

        return message

    def send(self, message, mailFrom=None, mailTo=None):
        if mailFrom is None:
            if "Sender" in message:
                mailFrom = message["Sender"]
            elif "From" not in message:
                mailFrom = _getDefaultMailFrom()
            else:
                mailFrom = message["From"]

        if mailTo is None:
            if "To" not in message and "CC" not in message and "BCC" not in message:
                raise ValueError("No receiver specified")

            mailTo = []
            mailTo.extend(message.get_all("To", []))
            mailTo.extend(message.get_all("CC", []))
            mailTo.extend(message.get_all("BCC", []))
        elif isinstance(mailTo, str):
            mailTo = [ mailTo ]

        self._server.send_message(message, from_addr=mailFrom, to_addrs=mailTo)

def _getDefaultMailFrom():
    try:
        user = getpass.getuser()
    except ImportError:
        user = "nobody"

    return "{}@{}".format(user, socket.gethostname())
