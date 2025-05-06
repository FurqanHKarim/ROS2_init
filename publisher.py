import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class ROS2_Node(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'hello_ROS2', 10)
        self.i = 0
        self.timer = self.create_timer(1.0, self.sendMsg)
        self.get_logger().info('Publisher node started')
        
    def sendMsg(self):
        msg = String()
        msg.data = 'Hello ROS2 %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main():
    rclpy.init()
    
    pubNode = ROS2_Node()

    rclpy.spin(pubNode)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()

    