#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:06:20 2017
@author: wenyan bi
"""

import cv2
import os
print(cv2.__version__)

# Changeble parameters:
start_vid_index = 1
end_vid_index = 44


for i in range(start_vid_index, end_vid_index):
    # vid names
    filename = 'vid_' + str(i) + '.mov'

    # save paths
    path = os.getcwd() + '/' + 'vid_' + str(i)
    if not os.path.exists(path):
        os.makedirs(path)

    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        print 'Read a new frame: ', success
        if not success:
            break
        
        cv2.imwrite(os.path.join(path, "frame%d.jpg" % count), image)     # save frame as JPEG file
        count += 1
		
