import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ROS2_Node(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'hello_ROS2',
            self.listener_callback,
            10)
        self.get_logger().info('Subscriber node started')

    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)
        

def main(args=None):
    rclpy.init(args=args)

    subNode = ROS2_Node()

    rclpy.spin(subNode)

    subNode.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
        main()