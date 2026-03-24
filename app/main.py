import socket  # noqa: F401


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
            message_size = len(data).to_bytes(4, "big")
            correlation_id = data[4:8]
            connection.sendall(message_size)
            connection.sendall(correlation_id)



if __name__ == "__main__":
    main()
