import rospy
from geometry_msgs.msg import Twist

def draw_circle(time, radius):
    # Initialize the ROS node
    rospy.init_node('circle_turtle')

    # Create a publisher to control the turtle's movement
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Set the rate at which to publish the turtle's movement commands
    rate = rospy.Rate(10)

    # Calculate the linear velocity to complete the circle in the given time
    linear_velocity = 2 * radius * 3.14 / time

    # Calculate the angular velocity to move in a circular path
    angular_velocity = linear_velocity / radius

    # Create a Twist message to control the turtle's movement
    twist = Twist()
    twist.linear.x = linear_velocity
    twist.angular.z = angular_velocity

    # Calculate the number of iterations based on the rate and time
    num_iterations = int(time * rate.sleep_dur.to_sec())

    # Keep publishing the movement commands for the calculated iterations
    for _ in range(num_iterations):
        pub.publish(twist)
        rate.sleep()

    # Stop the turtle after completing the circle
    twist.linear.x = 0.0
    twist.angular.z = 0.0
    pub.publish(twist)

if __name__ == '__main__':
    try:
        time = float(input("Enter the time to complete the circle (in seconds): "))
        radius = float(input("Enter the radius of the circle: "))
        draw_circle(time, radius)
    except rospy.ROSInterruptException:
        pass

