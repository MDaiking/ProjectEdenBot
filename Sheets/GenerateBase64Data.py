import sys
import base64

export_path = "Credentials.txt"

args = sys.argv
json_file = args[1]


def convert_json_to_base64(_json_file):
    with open(_json_file, 'r') as f:
        s = f.read()
        return base64.b64encode(s.encode('utf-8'))


with open(export_path, mode='w') as f:
    f.write(convert_json_to_base64(json_file).decode('utf-8'))
