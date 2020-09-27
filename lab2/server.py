import argparse
import select
import socket
import uuid


def main(ip="127.0.0.1", port=1234):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen()

    sockets = [server]

    # while True:
    # readables, writables, _ = select.select(sockets, sockets, [])

    # for readable in readables:
    #     if readable == server:
    client, address = server.accept()
    client.send(bytes(str(uuid.uuid4()), "utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", help="port number", required=True)
    args = parser.parse_args()
    main(port=int(args.port))
