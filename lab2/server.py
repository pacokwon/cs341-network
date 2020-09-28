#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
server.py file task 2 of Practice #2
"""

import argparse
import select
import socket
import re
import uuid


def fibonacci(n):
    """
    compute the nth number in the fibonacci sequence

    :param n: number of fibonacci sequence to be computed
    :type n: int
    :return: nth number in the fibonacci sequence
    :rtype: int
    """
    if n == 0:
        return 0

    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b

    return b


def factorial(n):
    """
    compute n!

    :param n: operand to factorial operator
    :type n: int
    :return: n!
    :rtype: int
    """
    if n == 0:
        return 0  # client recognizes 0! as 0
    if n == 1:
        return 1
    return n * factorial(n - 1)


def main(ip="127.0.0.1", port=1234):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen()

    sockets = [server]
    clients = {}

    while True:
        readables, _, _ = select.select(sockets, [], [])
        for sock in readables:
            if sock == server:
                client, address = server.accept()
                uid = str(uuid.uuid4())
                print(f"Client {uid} accepted from {address}")
                client.send(uid.encode("utf-8"))
                sockets.append(client)
                clients[client] = uid
                continue

            res = sock.recv(4).decode("utf-8")  # Get the first 4 byte sequences
            if res == "FIBO":
                # handle fibonacci
                sock.recv(5)  # throw away the rest
                n = int(sock.recv(1).decode("utf-8"))
                answer = fibonacci(n)
                print(f"{clients[sock]}\tFibonacci:\tReceived {n}. Sending {answer}")
                sock.send(f"{str(answer)}_{clients[sock]}".encode("utf-8"))
            elif res == "FILE":
                # handle file
                length = int(sock.recv(6).decode("utf-8"))
                file = sock.recv(length, socket.MSG_WAITALL).decode("utf-8")
                answer = len(file.split(" "))
                print(f"{clients[sock]}\tFile:\tReceived file. Sending {answer}")
                sock.send(f"{str(answer)}_{clients[sock]}".encode("utf-8"))
            elif res == "FACT":
                # handle factorial
                sock.recv(5)  # throw away the rest
                n = int(sock.recv(1).decode("utf-8"))
                answer = factorial(n)
                print(f"{clients[sock]}\tFactorial:\tReceived {n}. Sending {answer}")
                sock.send(f"{str(answer)}_{clients[sock]}".encode("utf-8"))
            elif res == "COMP":
                sock.close()
                sockets.remove(sock)
                print(f"Client {clients[sock]} disconnected")

                if len(sockets) == 1:
                    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="port number", required=True)
    args = parser.parse_args()
    main(port=int(args.port))
