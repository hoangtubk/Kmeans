import numpy as np 
import sys
import csv
import math
import random
import copy
import argparse

def read_csv_to_array(path, data):
    """Đọc file .cvs vào mảng data"""
    file = open(path,'r')
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

    return

def get_first_point_to_array(data, array_point):
    """Lấy ra tất cả các điểm cho vào mảng ArrayPoint"""
    for smt in data:
        point = []
        point.append(smt)
        point.append(0)
        array_point.append(point)
        # print(point)

    return

def get_first_center_to_array(k, data, array_center):
    """Lấy ra k tâm cho vào mảng ArrayCenter"""
    X = random.sample(data, k)
    for i in range(0,k):
        center = []
        center.append(X[i])     # Tọa độ của Tâm
        center.append(0)           # Số lượng điểm thuộc tâm
        array_center.append(center)

    return True

def dis_euclide(point, center):
    """ Tính khoảng cách theo Euclide của 2 vector 
        return: giá trị khoảng cách"""
    dist = 0
    i = 0
    for p in point:
        x = (float)(point[0][i]) - (float)(center[0][i])
        dist = dist + x*x
        i = i + 1
    dist = math.sqrt(dist)
    return dist

def compute_distance(array_point, array_center):
    """Tính khoảng cách từ mỗi điểm đến tâm,
        gán lại tâm cho mỗi điểm""" 
    count_point = 0
    for ipoint in array_point:
        count_point = count_point + 1
        d = 1000000         # Thay bằng giá trị max
        count_center = 0
        for icenter in array_center:
            count_center = count_center + 1
            dis = dis_euclide(ipoint,icenter)
            if(dis < d):
                ipoint[1] = count_center
                d = dis 

    return

def compute_cnumber(array_point, array_center):
    """Tính và gán số lượng phần tử của mỗi tâm"""
    count_center = 0
    for icenter in array_center:
        icenter[1] = 0
        count_point = 0
        count_center = count_center + 1
        for ipoint in array_point:
            count_point = count_point + 1
            if(ipoint[1] == count_center):
                icenter[1] = icenter[1] + 1

    return

def compute_center_again(array_point, array_center):
    """ Tính lại tâm """
    # Cho các điểm cùng tâm vào 1 mảng ppoint
    count_center = 0
    for pcenter in array_center:
        array_ppoint = []
        count_center = count_center + 1
        count_point = 0
        for ppoint in array_point:
            if(ppoint[1] == count_center):
                array_ppoint.append(ppoint[0])
        # Tính tâm của mảng ppoint là giá trị trung bình các vector 
        i = -1
        new_center = []
        leng = len(array_ppoint)
        for a in array_ppoint[0]:
            i = i + 1
            j = -1
            sum = 0.0
            for b in array_ppoint:
                j = j + 1
                sum = sum + (float)(array_ppoint[j][i])
            avg = sum/leng
            new_center.append(avg)
        # Gán giá trị tâm mới
        pcenter[0] = new_center

    return

def check_stop_condition(old_arraycenter, new_array_center):
    """Kiểm tra điều kiện hội tụ
        Return: true nếu tâm không thay đổi và ngược lại"""
    if(old_arraycenter == new_array_center):
        return True
    else:
        return False 


if __name__ == "__main__":
    path = (str)(sys.argv[1])
    k = (int)(sys.argv[2])
    data = []
    point = []
    center = []
    array_center = []
    array_point = []

    read_csv_to_array(path, data)
    # print(data)
    get_first_point_to_array(data, array_point)
    # print(array_point)
    get_first_center_to_array(k, data, array_center)
    # print(array_center)
    old_arr_center = copy.deepcopy(array_center)
    count_while = 0
    while True:
        count_while = count_while + 1
        compute_distance(array_point, array_center)
        # print(array_point)
        compute_center_again(array_point, array_center)
        # print(array_center)
        compute_cnumber(array_point, array_center)
        # print(array_center)
        if(check_stop_condition(array_center, old_arr_center)):
            for ppoint in array_point:
                print(ppoint[1])
            print(array_center)
            print("Number Loop: " + (str)(count_while))
            print("Number of element: ")
            for np in array_center:
                print(np[1])
            break
        else:
            old_arr_center = copy.deepcopy(array_center)