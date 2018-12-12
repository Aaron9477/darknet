#!/bin/bash

# 得到预训练网络(就是基础网络)
#./darknet partial cfg/yolov3-tiny.cfg weights/yolov3-tiny.weights yolov3-tiny.conv.15 15


# 训练网络origin
#./darknet detector train cfg_wyz/turtlebot/turtlebot.data cfg_wyz/turtlebot/yolov3-tiny.cfg pretrain_network/yolov3-tiny.conv.15 -map \
# | tee output.txt
# 使用训练后的网络
# 
# ./darknet detector train cfg_wyz/turtlebot/turtlebot.data cfg_wyz/turtlebot/yolov3-tiny.cfg backup/yolov3-tiny_final.weights -map \
# | tee output.txt

# 计算recall直接输出到终端,修改darknet的路径之后好使了
# ./darknet detector recall cfg_wyz/turtlebot/turtlebot.data cfg_wyz/turtlebot/yolov3-tiny.cfg backup/yolov3-tiny_final.weights

# 使用valid文件,并保存到result文件夹
# ./darknet detector valid cfg_wyz/turtlebot/turtlebot.data cfg_wyz/turtlebot/yolov3-tiny.cfg backup/yolov3-tiny_final.weights

# test
./darknet detector test cfg_wyz/turtlebot/turtlebot.data cfg_wyz/turtlebot/yolov3-tiny.cfg backup/yolov3-tiny_final.weights
# /media/zq610/2C9BDE0469DC4DFC/ubuntu/dl_dataset/turtlebot/VOC_type/turtlebot/JPEGImages/000087.jpg
