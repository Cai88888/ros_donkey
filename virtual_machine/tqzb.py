import rospy
import yaml
from PIL import Image
import numpy as np

# 初始化ROS节点
rospy.init_node('extract_obstacle_coordinates')

# 读取YAML文件
yaml_file_path = "/home/labory/map/floor2.yaml"  # 替换为您的YAML文件路径
with open(yaml_file_path, "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# 提取分辨率、原点、阈值等信息
resolution = yaml_data["resolution"]
origin = yaml_data["origin"]
occupied_thresh = yaml_data["occupied_thresh"]
free_thresh = yaml_data["free_thresh"]

# 读取PGM文件
pgm_file_path = "/home/labory/map/floor2.pgm"  # 替换为您的PGM文件路径
pgm_image = Image.open(pgm_file_path)
pgm_data = np.array(pgm_image)
#pgm_data=np.flipud(pgm_data)
# 提取障碍物坐标
obstacle_coordinates = []

for y in range(pgm_data.shape[0]):
    for x in range(pgm_data.shape[1]):
        pixel_value = pgm_data[y, x]
        if pixel_value < occupied_thresh:
            x_coord = origin[0] + x * resolution
            y_coord = origin[1] + y * resolution
            obstacle_coordinates.append((x_coord, y_coord))
# 将障碍物坐标写入文件
output_file_path = "/home/labory/map/obstacle_coordinates.txt"  # 替换为您希望保存的文件路径

with open(output_file_path, "w") as output_file:
    for coord in obstacle_coordinates:
        output_file.write(f"{coord[0]},{coord[1]}\n")
# 打印障碍物坐标
for coord in obstacle_coordinates:
    print("Obstacle Coordinate:", coord)

# 完成并关闭节点
rospy.spin()






