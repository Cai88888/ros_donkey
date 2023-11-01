import rospy
import math
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseWithCovarianceStamped

# global forward_PWM,start_PWM,START

forward_PWM = 1612
start_PWM = forward_PWM + 20
START = 0


## 一些函数
def quart_to_rpy(x, y, z, w):
    roll = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
    pitch = math.asin(2 * (w * y - x * z))
    yaw = math.atan2(2 * (w * z + x * y), 1 - 2 * (z * z + y * y))
    yaw = yaw * 180 / math.pi
    print("roll:", roll, "; pitch:", pitch, "; yaw:", yaw)
    return roll, pitch, yaw


def path_callback(msg):
    global x_tar_, y_tar_, z_tar_, is_move
    if is_move == 0:
        print("receiving...")
        print("length:", len(coordinates))
    for pose_stamped in msg.poses:
        x_tar_ = pose_stamped.pose.position.x
        y_tar_ = pose_stamped.pose.position.y
        z_tar_ = pose_stamped.pose.position.z
    if not coordinates:
        coordinates.append([x_tar_, y_tar_, z_tar_])
    else:
        last_coordinate = coordinates[-1]
        if last_coordinate == [x_tar_, y_tar_, z_tar_]:
            is_move = 1
        else:
            coordinates.append([x_tar_, y_tar_, z_tar_])


def pose_callback(msg):
    global x_cur, y_cur, z_cur, z_o, w_o
    x_cur = msg.pose.pose.position.x
    y_cur = msg.pose.pose.position.y
    z_cur = msg.pose.pose.position.z
    z_o = msg.pose.pose.orientation.z
    w_o = msg.pose.pose.orientation.w
    print("x_cur:",x_cur)
    print("y_cur:",y_cur)


def get_angle(x_tar, y_tar, x_cur, y_cur, z_o, w_o):
    dx = x_tar - x_cur
    dy = y_tar - y_cur
    angle_cur = quart_to_rpy(0, 0, z_o, w_o)[2]
    angle_tar = math.atan2(dy, dx) * 180 / math.pi
    distance = math.sqrt((x_cur - x_tar) ** 2 + (y_cur - y_tar) ** 2)
    return angle_tar, angle_cur, distance

def getdistance(coor1, coor2):
    dis = math.sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)
    return dis

def extract(coor, coordinates, sp):  # coor为当前坐标,coordinates为坐标数组,sp为当前坐标在数组中的索引
    radius = 1.2
    coor_out = []
    sp_new = sp
    for item in coordinates[sp:]:
        coor_out = item
        if (getdistance(coor, coor_out) >= radius):
            break
        sp_new += 1
    return coor_out, sp_new

# 计算角度差，确定转向角度和转动方向
def angle2PWM(angle_tar, angle_cur):
    delta_angle = angle_cur - angle_tar
    abs_delta = abs(delta_angle)
    if abs_delta <= 180:
        if delta_angle >= 0:
            direction = -1
        else:
            direction = 1
    elif abs_delta > 180:
        abs_delta = 360 - abs_delta
        if delta_angle >= 0:
            direction = 1
        else:
            direction = -1
    return_angle = direction * abs_delta
    return return_angle


###############################################################

import time
import math
import smbus
import socket
from pynput import keyboard

class PCA9685:
    # Registers/etc.
    __SUBADR1 = 0x02
    __SUBADR2 = 0x03
    __SUBADR3 = 0x04
    __MODE1 = 0x00
    __PRESCALE = 0xFE
    __LED0_ON_L = 0x06
    __LED0_ON_H = 0x07
    __LED0_OFF_L = 0x08
    __LED0_OFF_H = 0x09
    __ALLLED_ON_L = 0xFA
    __ALLLED_ON_H = 0xFB
    __ALLLED_OFF_L = 0xFC
    __ALLLED_OFF_H = 0xFD

    def __init__(self, address=0x40, debug=False):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.debug = debug
        if (self.debug):
            print("Reseting PCA9685")
        self.write(self.__MODE1, 0x00)

    def write(self, reg, value):
        "Writes an 8-bit value to the specified register/address"
        self.bus.write_byte_data(self.address, reg, value)
        # if self.debug:
        #     print("I2C: Write 0x%02X to register 0x%02X" % (value, reg))

    def read(self, reg):
        "Read an unsigned byte from the I2C device"
        result = self.bus.read_byte_data(self.address, reg)
        # if self.debug:
        #     print("I2C: Device 0x%02X returned 0x%02X from reg 0x%02X" % (self.address, result & 0xFF, reg))
        return result

    def setPWMFreq(self, freq):
        "Sets the PWM frequency"
        prescaleval = 25000000.0  # 25MHz
        prescaleval /= 4096.0  # 12-bit
        prescaleval /= float(freq)
        prescaleval -= 1.0
        if self.debug:
            print("Setting PWM frequency to %d Hz" % freq)
            print("Estimated pre-scale: %d" % prescaleval)
        prescale = math.floor(prescaleval + 0.5)
        if self.debug:
            print("Final pre-scale: %d" % prescale)

        oldmode = self.read(self.__MODE1)
        newmode = (oldmode & 0x7F) | 0x10  # sleep
        self.write(self.__MODE1, newmode)  # go to sleep
        self.write(self.__PRESCALE, int(math.floor(prescale)))
        self.write(self.__MODE1, oldmode)
        time.sleep(0.005)
        self.write(self.__MODE1, oldmode | 0x80)

    def setPWM(self, channel, on, off):
        "Sets a single PWM channel"
        self.write(self.__LED0_ON_L + 4 * channel, on & 0xFF)
        self.write(self.__LED0_ON_H + 4 * channel, on >> 8)
        self.write(self.__LED0_OFF_L + 4 * channel, off & 0xFF)
        self.write(self.__LED0_OFF_H + 4 * channel, off >> 8)
        # if (self.debug):
        #     print("channel: %d  LED_ON: %d LED_OFF: %d" % (channel, on, off))

    def setServoPulse(self, channel, pulse):
        "Sets the Servo Pulse,The PWM frequency must be 50HZ"
        pulse = int(pulse * 4096 / 20000)  # PWM frequency is 50HZ,the period is 20000us
        self.setPWM(channel, 0, pulse)


###############################################################

import threading


def cmd_while():
    global target_list, target_num, target_index
    global done,sp,x_tar_,y_tar_,z_tar_
    global forward_PWM, start_PWM, START
    while not rospy.is_shutdown():
        #####
        if done == 0:
            print("x", x_tar_)
            print("y", y_tar_)
            print("z", z_tar_)
            print("ismove:", is_move)
            if is_move == 1 and done == 0:
                print("file_writing/..\../..\../..\../..\../..\../..\..")
                #file_path = "/home/vvt/catkin_ws/src/multi_robot_traj_planner/multi_robot_traj_planner/scripts/output.txt"
                # with open(file_path, "w") as file:
                #     for item in coordinates:
                #         file.write(f"{item}\n")
                print("file_write complete^-^")
                print("extracting/..\../..\../..\../..\../..\../..\..")
                l = len(coordinates)
                path.append(coordinates[0])
                while (sp < l):
                    coor, sp = extract(path[-1], coordinates, sp)
                    path.append(coor)

                target_list = [(round(x, 2), round(y, 2)) for x, y, _ in path]
                target_num = len(target_list)

                #file_path = "/home/vvt/catkin_ws/src/multi_robot_traj_planner/multi_robot_traj_planner/scripts/extract.txt"
                # with open(file_path, "w") as file:
                #     for item in targets:
                #         file.write(f"{item}\n")
                #     done = 1
                done = 1
                print("extracting complete^-^")
                print("------------------------RUN------------------------")
            ####
        else:
            # 读取目标点
            target = target_list[target_index]
            x_tar = target[0]
            y_tar = target[1]

            print("x_tar:", x_tar)
            print("y_tar:", y_tar)

            print("x_cur:", x_cur)
            print("y_cur:", y_cur)

            angle_tar, angle_cur, distance = get_angle(x_tar, y_tar, x_cur, y_cur, z_o, w_o)

            print("angle_tar:", angle_tar)
            print("angle_cur:", angle_cur)
            print("distance:", distance)

            # 舵机转向控制
            ## servo_PWM = 1650 + 方向系数 * 系数 * |angle_tar - angle_cur|
            # angle2PWM(angle_tar,angle_cur) 的值为+是右转，-是左转
            coe = 10
            servo_PWM = 1650 + 10 * angle2PWM(angle_tar, angle_cur)
            if servo_PWM > 2100:
                servo_PWM = 2100

            if servo_PWM < 1200:
                servo_PWM = 1200

            pwm.setServoPulse(0, servo_PWM)
            print("servo_PWM:", servo_PWM)

            print("###################################")

            #启动！！！
            if START == 0: #只执行一次
                pwm.setServoPulse(3, start_PWM)
                time.sleep(0.3)
                START = 1

            forward_PWM_angle = forward_PWM + abs(servo_PWM-1650)*0.01

            pwm.setServoPulse(3, forward_PWM_angle)

            if distance < 0.5:
                if target_index < target_num - 1:
                    target_index = target_index + 1

                elif distance < 0.4:
                    pwm.setServoPulse(3, stop_PWM)
                    print("Stop!")

            pass



def main():
    ## 参数初始化
    global x_tar, y_tar, z_tar, x_cur, y_cur, z_cur, z_o, w_o, is_move, coordinates,done,sp,path,x_tar_,y_tar_,z_tar_
    global pwm, stop_PWM
    global target_list, target_num, target_index

    '''
    stop_PWM = 1630
    start_PWM = stop_PWM + 50
    forward_PWM = stop_PWM + 40
    '''

    target_list = [(1.2, -0.6), (0, 0), (-1.2, 0)]
    target_num = len(target_list)  # 目标点列表个数
    target_index = 0  # 目标点序号值

    x_cur = 1000
    y_cur = 1000
    z_cur = 0.0
    z_o = 0.0
    w_o = 0.0
    is_move = 0
    coordinates = []
    done = 0
    sp = 0
    path = []
    x_tar_ = 0
    y_tar_ = 0
    z_tar_ = 0

    servo_PWM = 1600
    stop_PWM = 1500

    ## 运动控制
    pwm = PCA9685(0x40, debug=True)
    pwm.setPWMFreq(50)

    ## 订阅话题
    rospy.init_node('path_subscriber_0')
    sub1 = rospy.Subscriber('/desired_trajectory/mav0',Path,path_callback)
    sub2 = rospy.Subscriber('/car0/amcl_pose', PoseWithCovarianceStamped, pose_callback)
    rate = rospy.Rate(10)


    loop_thread = threading.Thread(target=cmd_while)
    loop_thread.start()

    rospy.spin()


# if __name__ == '__main__':
main()


