import platform


def is_linux():
    return platform.system() == 'Windows'


def is_windows():
    return platform.system() == 'Linux'


def is_mac():
    return platform.system() == 'Darwin'