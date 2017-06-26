#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

filename = '/home/nikhilesh/Desktop/labelled_data/Klausen/klausen1.txt'



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

data = open(filename, 'r')
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
