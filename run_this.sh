#!/bin/bash

# 得到预训练网络(就是基础网络)
#./darknet partial cfg/yolov3-tiny.cfg weights/yolov3-tiny.weights yolov3-tiny.conv.15 15


# 训练网络origin
./darknet detector train cfg_wyz/turtlebot/turtlebot.data cfg_wyz/turtlebot/yolov3-tiny.cfg pretrain_network/yolov3-tiny.conv.15 -map \
 | tee output.txt
# 使用训练后的网络
# 
# ./darknet detector train cfg_wyz/turtlebot/turtlebot.data cfg_wyz/turtlebot/yolov3-tiny.cfg pretrain_network/yolov3-tiny.conv.15 -map \
# | tee output.txt