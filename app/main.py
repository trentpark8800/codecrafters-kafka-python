import socket
from dataclasses import dataclass
from typing import List


@dataclass
class Message:
    correlation_id: int
    request_api_version: int
    request_api_key: int
    message_size: int


@dataclass
class Response:
    correlation_id: int
    error_code: int


def read_message(data: bytes) -> Message:

    message: Message = Message(
        correlation_id=int.from_bytes(data[8:12]),
        message_size=int.from_bytes(data[0:4]),
        request_api_key=int.from_bytes(data[4:6]),
        request_api_version=int.from_bytes(data[6:8]),
    )

    return message


def parse_message(message: Message) -> Response:

    supported_versions: List[int] = [4]

    error_code: int = 0

    if message.request_api_version not in supported_versions:
        print(f"Unsupported version {message.request_api_version}.")
        error_code = 35
    
    response: Response = Response(
        correlation_id=message.correlation_id,
        error_code=error_code,
    )

    return response


def parse_response(response: Response) -> bytes:

    response_data: bytes = response.correlation_id.to_bytes(4, "big") + response.error_code.to_bytes(2, "big")

    response_size = len(response_data).to_bytes(4, "big")

    return response_size + response_data


def send_response(connection: socket.SocketType, data: bytes) -> None:

    connection.sendall(data)


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, address = server.accept()

    print(f"New client connected from {address}.")

    with connection:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            message: Message = read_message(data)
            response: Response = parse_message(message)
            response_bytes: bytes = parse_response(response)
            send_response(connection, response_bytes)


if __name__ == "__main__":
    main()
