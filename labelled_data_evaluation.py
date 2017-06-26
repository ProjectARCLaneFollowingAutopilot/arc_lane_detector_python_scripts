#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

filename_raw_r = '/home/nikhilesh/Desktop/labelled_data/Zurich/Uberland/ueberland1.txt'
filename_result_w = '/home/nikhilesh/Desktop/labelled_data/Zurich/Uberland/ueberland1_result.txt'


# Read in data.
left_bottom_vec_algo_x = []
left_bottom_vec_algo_y = []

left_top_vec_algo_x = []
left_top_vec_algo_y = []

right_bottom_vec_algo_x = []
right_bottom_vec_algo_y = []

right_top_vec_algo_x = []
right_top_vec_algo_y = []

left_bottom_vec_hand_x = []
left_bottom_vec_hand_y = []

left_top_vec_hand_x = []
left_top_vec_hand_y = []

right_bottom_vec_hand_x = []
right_bottom_vec_hand_y = []

right_top_vec_hand_x = []
right_top_vec_hand_y = []

data = open(filename_raw_r, 'r')
for lines in data:
	currentline = lines.split(" ")

	left_bottom_vec_algo_x.append(currentline[0])
	left_bottom_vec_algo_y.append(currentline[1])

	left_top_vec_algo_x.append(currentline[2])
	left_top_vec_algo_y.append(currentline[3])

	right_bottom_vec_algo_x.append(currentline[4])
	right_bottom_vec_algo_y.append(currentline[5])

	right_top_vec_algo_x.append(currentline[6])
	right_top_vec_algo_y.append(currentline[7])

	left_bottom_vec_hand_x.append(currentline[8])
	left_bottom_vec_hand_y.append(currentline[9])

	left_top_vec_hand_x.append(currentline[10])
	left_top_vec_hand_y.append(currentline[11])

	right_bottom_vec_hand_x.append(currentline[12])
	right_bottom_vec_hand_y.append(currentline[13])

	right_top_vec_hand_x.append(currentline[14])
	right_top_vec_hand_y.append(currentline[15])
data.close()

# Calculate slopes and intersections.
slope_left_algo = []
intersection_left_algo = []
slope_right_algo = []
intersection_right_algo = []
slope_left_hand = []
intersection_left_hand = []
slope_right_hand = []
intersection_right_hand = []

for i in range(0, len(left_bottom_vec_algo_x)):
	slope_left_algo.append((float(left_top_vec_algo_y[i]) - float(left_bottom_vec_algo_y[i]))/(float(left_top_vec_algo_x[i]) - float(left_bottom_vec_algo_x[i])))
	intersection_left_algo.append( float(left_top_vec_algo_y[i]) - slope_left_algo[i]*float(left_top_vec_algo_x[i]))
	slope_right_algo.append((float(right_top_vec_algo_y[i]) - float(right_bottom_vec_algo_y[i]))/(float(right_top_vec_algo_x[i]) - float(right_bottom_vec_algo_x[i])))
	intersection_right_algo.append( float(right_top_vec_algo_y[i]) - slope_right_algo[i]*float(right_top_vec_algo_x[i]))
	slope_left_hand.append((float(left_top_vec_hand_y[i]) - float(left_bottom_vec_hand_y[i]))/(float(left_top_vec_hand_x[i]) - float(left_bottom_vec_hand_x[i])))
	intersection_left_hand.append( float(left_top_vec_hand_y[i]) - slope_left_hand[i]*float(left_top_vec_hand_x[i]))
	slope_right_hand.append((float(right_top_vec_hand_y[i]) - float(right_bottom_vec_hand_y[i]))/(float(right_top_vec_hand_x[i]) - float(right_bottom_vec_hand_x[i])))
	intersection_right_hand.append( float(right_top_vec_hand_y[i]) - slope_right_hand[i]*float(right_top_vec_hand_x[i]))

error_rms_slope_left = 0
error_rms_intersection_left = 0
error_rms_slope_right = 0
error_rms_intersection_right = 0


for i in range(0, len(left_bottom_vec_algo_x)):
	error_rms_slope_left = error_rms_slope_left + pow(slope_left_algo[i] - slope_left_hand[i], 2) 
	error_rms_intersection_left = error_rms_intersection_left + pow(intersection_left_algo[i] - intersection_left_hand[i], 2) 
	error_rms_slope_right = error_rms_slope_right + pow(slope_right_algo[i] - slope_right_hand[i], 2) 
	error_rms_intersection_right = error_rms_intersection_right + pow(intersection_right_algo[i] - intersection_right_hand[i], 2) 

error_rms_slope_left = error_rms_slope_left/len(slope_left_algo)
error_rms_intersection_left = error_rms_intersection_left/len(intersection_left_algo)
error_rms_slope_right = error_rms_slope_right/len(slope_right_algo)
error_rms_intersection_right = error_rms_intersection_right/len(intersection_right_algo)

error_rms_slope_left = sqrt(error_rms_slope_left)
error_rms_intersection_left = sqrt(error_rms_intersection_left)
error_rms_slope_right = sqrt(error_rms_slope_right)
error_rms_intersection_right = sqrt(error_rms_intersection_right)

error = open(filename_result_w, 'w')
error.write("Error_RMS in Slope left = " + str(error_rms_slope_left) + '\n')
error.write("Error_RMS in Intersection left = " + str(error_rms_intersection_left) + '\n')
error.write("Error_RMS in Slope right = " + str(error_rms_slope_right) + '\n')
error.write("Error_RMS in Intersection right = " + str(error_rms_intersection_right) + '\n')
error.close()