import sys

class ColorPrint:

    @staticmethod
    def print_colour(message, colour : str, end : str | int | None='\n'):
        if colour == "black":
            sys.stdout.write('\x1b[0;30m' + message.strip() + '\x1b[0m' + end)
        elif colour == "blue":
            sys.stdout.write('\x1b[0;34m' + message.strip() + '\x1b[0m' + end)
        elif colour == "red":
            sys.stdout.write('\x1b[0;31m' + message.strip() + '\x1b[0m' + end)
        elif colour == "green":
            sys.stdout.write('\x1b[0;32m' + message.strip() + '\x1b[0m' + end)
        elif colour == "yellow":
            sys.stdout.write('\x1b[0;33m' + message.strip() + '\x1b[0m' + end)
        elif colour == "purple":
            sys.stdout.write('\x1b[0;35m' + message.strip() + '\x1b[0m' + end)
        elif colour == "cyan":
            sys.stdout.write('\x1b[0;36m' + message.strip() + '\x1b[0m' + end)
        elif colour == "white":
            sys.stdout.write('\x1b[0;37m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_background(message, colour : str ,end : str | int | None='\n'):
        if colour == "black":
            sys.stdout.write('\x1b[40m' + message.strip() + '\x1b[0m' + end)
        elif colour == "blue":
            sys.stdout.write('\x1b[44m' + message.strip() + '\x1b[0m' + end)
        elif colour == "green":
            sys.stdout.write('\x1b[42m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_fail(message, end = '\n'):
        sys.stderr.write('\x1b[1;31m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_pass(message, end = '\n'):
        sys.stdout.write('\x1b[1;32m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_warn(message, end = '\n'):
        sys.stderr.write('\x1b[1;33m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_info(message, end = '\n'):
        sys.stdout.write('\x1b[1;34m' + message.strip() + '\x1b[0m' + end)

    @staticmethod
    def print_bold(message, end = '\n'):
        sys.stdout.write('\x1b[1;37m' + message.strip() + '\x1b[0m' + end)