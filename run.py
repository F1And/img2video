#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @description：把照片合成视频。

import os
import cv2


def read_picture(path):
    """
    :param path:
    :return:
    """
    file_list = os.listdir(path)
    fps = 2
    height = 640
    weight = 480
    size = (height, weight)  # 需要转为视频的图片的尺寸
    return [path, fps, size, file_list]


def write_video(path):
    path, fps, size, file_list = read_picture(path)
    # AVI格式编码输出 XVID
    four_cc = cv2.VideoWriter_fourcc(*'MJPG')
    save_path = 'morgan.avi'
    video_writer = cv2.VideoWriter(save_path, four_cc, float(fps), size)
    # 视频保存在当前目录下
    for item in file_list:
        if item.endswith('.jpg') or item.endswith('.png'):
            # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
            item = path + '/' + item
            img = cv2.imread(item)
            re_pics = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)  # 定尺寸
            video_writer.write(re_pics)

    video_writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    write_video(path='Morgan')
