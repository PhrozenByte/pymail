`pymail`
========

`pymail` is a simple Python script to synchroniously send emails via SMTP. It is often used on satellite systems without a fully-featured MTA.

Requires Python 3.4+

Usage
-----

```
usage: pymail [-a HEADER] [-b BCC_ADDR] [-c CC_ADDR] [-s SUBJECT] TO_ADDR...

pymail is a simple Python script to synchroniously send emails via SMTP. It is
often used on satellite systems without a fully-featured MTA.

Arguments:
  TO_ADDR      Send mail to TO_ADDR.

Application options:
  -a HEADER    Specify additional header fields on the command line such as
               "X-Loop: foo@bar" etc. You have to use quotes if the string
               contains spaces. This argument may be specified more than once,
               the headers will then be concatenated.
  -b BCC_ADDR  Send blind carbon copies to BCC_ADDR.
  -c CC_ADDR   Send carbon copies to list of users. CC_ADDR should be a comma
               separated list of names.
  -s SUBJECT   Specify subject on command line (only the first argument after
               the -s flag is used as a subject; be careful to quote subjects
               containing spaces).

Help options:
  --help       Display this help message and exit
  --version    Output version information and exit

Please report bugs using GitHub at <https://github.com/PhrozenByte/pymail>.
Besides, you will find general help and information about cron-notify there.
```

Config
------

Create `~/.config/pymail/pymail.ini` with the following contents:

```ini
[DEFAULT]
host = mail.example.com
username = sendmail-bot@example.com
password = SecretPasswordUseFilePermissions

[SOME_SECTION]
from = noreply@example.com

[OTHER_SECTION]
host = mail.example.net
port = 465
secure = SSL
username = user42
password = ItsTheAnswer
```

The `[DEFAULT]` section is inherited to all following sections and used by default. You can request any other section using the `PYMAIL_CONFIG` environment variable.

License & Copyright
-------------------

Copyright (C) 2017-2022  Daniel Rudolf <https://www.daniel-rudolf.de/>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 of the License only.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the [GNU General Public License](LICENSE) for more details.
