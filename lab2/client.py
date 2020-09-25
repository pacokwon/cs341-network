import argparse
import array
import collections
import socket
import struct


def compute_checksum(msg):
    s = 0  # Binary Sum

    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        s += msg[i] + (msg[i + 1] << 8)

    # One's Complement
    s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xFFFF

    return s


def get_header(flag, keyword, sid, data):
    checksum = 0
    data = bytes(data)
    length = 16 + len(data)

    pseudo_header = struct.pack("!HH4sll", flag, checksum, keyword, sid, length)
    checksum = compute_checksum(pseudo_header + data)
    header = struct.pack("!HH4sll", flag, checksum, keyword, sid, length) + data
    return header


def run(host, port, sid):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))

        fields = {"data": "hi", "flag": 1, "keyword": b"paco", "sid": 20190046}
        header = get_header(**fields)
        client.send(header)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="python client.py --host=143.248.56.39 --port=4000 -studentID=20xxxxxx"
    )
    parser.add_argument("--host", help="host ip", required=True)
    parser.add_argument("--port", help="port number", required=True)
    parser.add_argument("--studentID", help="student id", required=True)

    args = parser.parse_args()
    run(host=args.host, port=int(args.port), sid=int(args.studentID))
