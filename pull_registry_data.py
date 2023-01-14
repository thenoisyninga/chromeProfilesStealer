from winreg import *


def read_values(key_path):
    key = OpenKey(HKEY_CURRENT_USER, fr'{key_path}')
    t = []
    i = 0
    while True:
        try:
            t.append(EnumValue(key, i))
            i += 1
        except OSError:
            break
    return t


def read_keys(key_path):
    key = OpenKey(HKEY_CURRENT_USER, fr'{key_path}')
    t = []
    i = 0
    while True:
        try:
            t.append(EnumKey(key, i))
            i += 1
        except OSError:
            break
    return t


def scan_all_key_contents(key_path, file_to_write):
    values = read_values(key_path)
    keys = read_keys(key_path)

    file_to_write.write(f"\n\n" + rf"[HKEY_CURRENT_USER\{key_path}]")
    for value in values:
        file_to_write.write(f'\n"{value[0]}"="{value[1]}"')

    for key in keys:
        scan_all_key_contents(key_path=key_path + rf"\{key}", file_to_write=file_to_write)


def export_reg_key(key_path, filename):
    file = open(filename, 'w')
    file.write("Windows Registry Editor Version 5.00")
    scan_all_key_contents(key_path=key_path, file_to_write=file)
    file.close()


