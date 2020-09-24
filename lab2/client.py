import argparse
import array
import collections
import socket
import struct


def compute_checksum(msg):
    s = 0  # Binary Sum

    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
        if (i + 1) < len(msg):
            a = msg[i]
            b = msg[i + 1]
            s = s + (a + (b << 8))
        elif (i + 1) == len(msg):
            s += msg[i]
        else:
            raise "Something Wrong here"

    # One's Complement
    s = s + (s >> 16)
    s = ~s & 0xFFFF

    return s


def get_checksum(header, data, source_ip, destination_ip):
    source_address = socket.inet_aton(source_ip)
    destination_address = socket.inet_aton(destination_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(header) + len(data)

    pseudo_header = struct.pack(
        "!4s4sBBH",
        source_address,
        destination_address,
        placeholder,
        protocol,
        tcp_length,
    )

    pseudo_header = pseudo_header + header + data
    print(pseudo_header)
    return compute_checksum(pseudo_header)


def run(host, port, sid):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data = b"hello world"

        flag = 1
        checksum = 0
        keyword = b"paco"
        sid = 20190046
        length = 64 * 2 + len(data)

        header = struct.pack("!HH4sll", flag, checksum, keyword, sid, length)
        checksum = get_checksum(header, data, "127.0.0.1", host)
        print(checksum)
        header = struct.pack("!HH4sll", flag, checksum, keyword, sid, length) + data

        s.send(header)

        res = s.recv(1024)
        print(res)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="python client.py --host=143.248.56.39 --port=4000 -studentID=20xxxxxx"
    )
    parser.add_argument("--host", help="host ip", required=True)
    parser.add_argument("--port", help="port number", required=True)
    parser.add_argument("--studentID", help="student id", required=True)

    args = parser.parse_args()
    run(host=args.host, port=int(args.port), sid=int(args.studentID))
