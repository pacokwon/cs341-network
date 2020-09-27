#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
client.py file for task 1 of Practice #2
"""

import argparse
import collections
import socket
import struct


def compute_checksum(msg):
    """
    compute checksum of given message

    :param msg: message whose checksum is deisred to be computed
    :type msg: bytes
    :return: computed checksum
    :rtype: int
    """
    checksum = 0
    for i in range(0, len(msg), 2):
        if (i + 1) == len(msg):
            checksum += msg[i]
        else:
            checksum += msg[i] + (msg[i + 1] << 8)

    checksum = (checksum & 0xFFFF) + (checksum >> 16)
    checksum = ~checksum & 0xFFFF

    return checksum


def get_header(flag, keyword, sid, data=""):
    """
    construct header from various given fields

    :param flag     : flag, as required from the protocol specs
    :param keyword  : keyword, as required from the protocol specs
    :param sid      : sid, as required from the protocol specs
    :param data     : data desired to be sent
    :type flag      : 0 | 1
    :type keyword   : bytes
    :type sid       : int
    :type data      : str
    :return         : constructed header
    :rtype          : bytes
    """
    checksum = 0
    data = bytes(data, "utf-8")
    length = 16 + len(data)

    pseudo_header = struct.pack("!HH4sll", flag, checksum, keyword, sid, length)
    checksum = compute_checksum(pseudo_header + data)
    header = struct.pack("!HH4sll", flag, checksum, keyword, sid, length) + data
    return header


def get_response(client, decipher=True):
    """
    read header and data from the socket server, following the protocol

    :param client   : client socket connected to the host
    :param decipher : whether or not the data should be deciphered or not
    :type client    : socket.socket
    :type decipher  : bool
    :return         : decrypted data
    :rtype          : str
    """
    response = client.recv(16)
    flag, _, keyword, sid, length = struct.unpack("!HH4sll", response)

    message_length = length - 16
    data = client.recv(message_length, socket.MSG_WAITALL)
    key = (message_length // len(keyword)) * keyword + keyword[
        : (message_length % len(keyword))
    ]

    decrypted = "".join([chr(d ^ k) for d, k in zip(data, key)]) if decipher else data

    return flag, keyword, sid, decrypted


def run(host, port, sid):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))

        fields = {"flag": 1, "keyword": b"sbmt", "sid": sid}
        header = get_header(**fields)
        client.send(header)

        flag = 0
        while flag == 0:
            flag, keyword, sid, decrypted = get_response(client)
            header = get_header(flag, keyword, sid, decrypted)
            client.send(header)

        flag, keyword, sid, decrypted = get_response(client, decipher=False)
        print(
            f"KEY: {keyword.decode('utf-8')}\nScore: {sid}\nMessage: {decrypted.decode('utf-8')}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="python client.py --host=143.248.56.39 --port=4000 -studentID=20xxxxxx"
    )
    parser.add_argument("--host", help="host ip", required=True)
    parser.add_argument("--port", help="port number", required=True)
    parser.add_argument("--studentID", help="student id", required=True)

    args = parser.parse_args()
    run(host=args.host, port=int(args.port), sid=int(args.studentID))
