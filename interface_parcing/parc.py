import re


regex = (
        '^(?P<intf>\S+) is up$'
        '|(?P<ierror>\S+ input error)'
        '|(?P<oerror>\S+ output error)'
        )

with open('10.177.177.237_16_11.log') as fa:
    for line in fa:
        match = re.search(regex, line)
        if match:
            Inerface = match.group('intf')
            IError = match.group('ierror')
            OError = match.group('oerror')
            with open("result237.txt", "a") as file:
                print(Inerface,IError, OError, file=file)
with open('10.177.177.238_16_11.log') as fs:
    for line in fs:
        match = re.search(regex, line)
        if match:
            Inerface = match.group('intf')
            IError = match.group('ierror')
            OError = match.group('oerror')
            with open("result238.txt", "a") as file:
                print(Inerface,IError, OError, file=file)
with open('10.177.177.239_16_11.log') as fd:
    for line in fd:
        match = re.search(regex, line)
        if match:
            Inerface = match.group('intf')
            IError = match.group('ierror')
            OError = match.group('oerror')
            with open("result239.txt", "a") as file:
                print(Inerface,IError, OError, file=file)
with open('10.177.177.240_16_11.log') as ff:
    for line in ff:
        match = re.search(regex, line)
        if match:
            Inerface = match.group('intf')
            IError = match.group('ierror')
            OError = match.group('oerror')
            with open("result240.txt", "a") as file:
                print(Inerface,IError, OError, file=file)
