import rclpy
from rclpy.node import Node

def todo():
    while True:
        print("hello world")

def main():
    rclpy.init()
    node = Node('hello_node')
    todo()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
