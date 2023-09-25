import rclpy
import socket
from rclpy.node import Node

def todo():
    host_ip = '192.168.1.102'
    host_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host_ip, host_port))

    server_socket.listen(1)

    print("待機中")

    client_socket, client_address = server_socket.accept()

    data = client_socket.recv(1024)

    print("受信メッセージ：", data.decode())

    client_socket.close()
    server_socket.close()

def main():
    rclpy.init()
    node = Node('hello_node')
    todo()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
