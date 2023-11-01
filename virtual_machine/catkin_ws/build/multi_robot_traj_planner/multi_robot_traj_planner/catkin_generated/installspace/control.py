import rospy
import math
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseWithCovarianceStamped
## 一些函数
def quart_to_rpy(x, y, z, w):
    roll = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
    pitch = math.asin(2 * (w * y - x * z))
    yaw = math.atan2(2 * (w * z + x * y), 1 - 2 * (z * z + y * y))
    yaw = yaw * 180 / math.pi
    print("roll:", roll, "; pitch:", pitch, "; yaw:", yaw)
    return roll, pitch, yaw

def path_callback(msg):
    global x_tar, y_tar, z_tar,is_move
    if is_move == 0:
        print("receiving...")
        print("length:",len(coordinates))
    for pose_stamped in msg.poses:
        x_tar = pose_stamped.pose.position.x
        y_tar = pose_stamped.pose.position.y
        z_tar = pose_stamped.pose.position.z
    if not coordinates:
        coordinates.append([x_tar, y_tar, z_tar])
    else:
        last_coordinate = coordinates[-1]
        if last_coordinate == [x_tar, y_tar, z_tar]:
            is_move = 1
        else:
            coordinates.append([x_tar, y_tar, z_tar])


def pose_callback(msg):
    global x_cur, y_cur, z_cur, z_o, w_o
    x_cur = msg.pose.pose.position.x
    y_cur = msg.pose.pose.position.y
    z_cur = msg.pose.pose.position.z
    z_o = msg.pose.pose.orientation.z
    w_o = msg.pose.pose.orientation.w

def get_angle(x_tar, y_tar, x_cur, y_cur, z_o, w_o):
    dx = x_tar - x_cur
    dy = y_tar - y_cur
    angle_cur = quart_to_rpy(0, 0, z_o, w_o)[2]
    angle_tar = math.atan2(dy, dx) * 180 / math.pi
    dis = math.sqrt((x_cur - x_tar) ** 2 + (y_cur - y_tar) ** 2)
    return angle_tar, angle_cur, dis

def distance(coor1,coor2):
    dis = math.sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)
    return dis


def extract(coor,coordinates,sp):  #coor为当前坐标,coordinates为坐标数组,sp为当前坐标在数组中的索引
    radius = 1.2
    coor_out = []
    sp_new = sp
    for item in coordinates[sp:]:
        coor_out = item
        if(distance(coor,coor_out) >= radius):
            break
        sp_new += 1
    return coor_out,sp_new 


def main():

    ## 参数初始化
    global x_tar, y_tar, z_tar, x_cur, y_cur, z_cur, z_o,w_o,is_move,coordinates,done
    #coordinates储存所有的坐标点，在回调函数里赋值，is_move表示小车是否移动,0不移动,1移动
    is_move = 0
    coordinates = []

    x_tar = 0.0
    y_tar = 0.0
    z_tar = 0.0

    x_cur = 0.0
    y_cur = 0.0
    z_cur = 0.0
    z_o = 0.0
    w_o = 0.0

    # servo_PWM = 1600
    # motor_stop_PWM = 1560
    # motor_forward_PWM = motor_stop_PWM + 60
    
    ## 订阅话题
    rospy.init_node('path_subscriber')
    sub1 = rospy.Subscriber('/desired_trajectory/mav1',Path,path_callback)
    # sub2 = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, pose_callback)
    rate = rospy.Rate(1)
    done = 0
    sp = 0
    path = []
    while not (done or rospy.is_shutdown()):
        print("x",x_tar)
        print("y",y_tar)
        print("z",z_tar)
        print("ismove:",is_move)
        if is_move == 1 and done == 0:
            print("file_writing/..\../..\../..\../..\../..\../..\..")
            file_path = "/home/labory/catkin_ws/src/multi_robot_traj_planner/multi_robot_traj_planner/scripts/output.txt"
            with open(file_path, "w") as file:
                for item in coordinates:
                    file.write(f"{item}\n")
            print("file_write complete^-^")
            print("extracting/..\../..\../..\../..\../..\../..\..")
            l = len(coordinates)
            path.append(coordinates[0])
            while(sp<l):
                coor,sp = extract(path[-1],coordinates,sp)
                path.append(coor)
            
            targets = [(round(x, 2), round(y, 2)) for x, y, _ in path]

            file_path = "/home/labory/catkin_ws/src/multi_robot_traj_planner/multi_robot_traj_planner/scripts/extract.txt"
            with open(file_path, "w") as file:
                for item in targets:
                    file.write(f"{item}\n")
                done = 1

            print("extracting complete^-^")
    
    print("all complete")
    rospy.spin()
if __name__ == '__main__':
    main()


