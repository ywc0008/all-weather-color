from scipy.spatial import distance
import copy
import math
import operator

def is_warm(lab_b, a):
    # standard of skin, eyebrow, eye
    warm_b_std = [11.6518, 11.71445, 3.6484]
    cool_b_std = [4.64255, 4.86635, 0.18735]

    warm_dist = 0
    cool_dist = 0

    body_part = ['skin', 'eyebrow', 'eye']
    for i in range(3):
        warm_dist += abs(lab_b[i] - warm_b_std[i]) * a[i]
        #print(body_part[i],"의 warm 기준값과의 거리")
        #print(abs(lab_b[i] - warm_b_std[i]))
        cool_dist += abs(lab_b[i] - cool_b_std[i]) * a[i]
        #print(body_part[i],"의 cool 기준값과의 거리")
        #print(abs(lab_b[i] - cool_b_std[i]))
    if(warm_dist <= cool_dist):
        return 1 #warm
    else:
        return 0 #cool

def is_spr(hsv_s, a):
    #skin, hair, eye
    spr_s_std = [18.59296, 30.30303, 25.80645]
    fal_s_std = [27.13987, 39.75155, 37.5]

    spr_dist = 0
    fal_dist = 0

    body_part = ['skin', 'eyebrow', 'eye']
    for i in range(3):
        spr_dist += abs(hsv_s[i] - spr_s_std[i]) * a[i]
        print(body_part[i],"의 spring 기준값과의 거리")
        print(abs(hsv_s[i] - spr_s_std[i]) * a[i])
        fal_dist += abs(hsv_s[i] - fal_s_std[i]) * a[i]
        print(body_part[i],"의 fall 기준값과의 거리")
        print(abs(hsv_s[i] - fal_s_std[i]) * a[i])

    if(spr_dist <= fal_dist):
        return 1 #spring
    else:
        return 0 #fall

def is_smr(hsv_s, a):
    #skin, eyebrow, eye
    smr_s_std = [12.5, 21.7195, 24.77064]
    wnt_s_std = [16.73913, 24.8276, 31.3726]
    a[1] = 0.5 # eyebrow 영향력 적기 때문에 가중치 줄임

    smr_dist = 0
    wnt_dist = 0

    body_part = ['skin', 'eyebrow', 'eye']
    for i in range(3):
        smr_dist += abs(hsv_s[i] - smr_s_std[i]) * a[i]
        print(body_part[i],"의 summer 기준값과의 거리")
        print(abs(hsv_s[i] - smr_s_std[i]) * a[i])
        wnt_dist += abs(hsv_s[i] - wnt_s_std[i]) * a[i]
        print(body_part[i],"의 winter 기준값과의 거리")
        print(abs(hsv_s[i] - wnt_s_std[i]) * a[i])

    if(smr_dist <= wnt_dist):
        return 1 #summer
    else:
        return 0 #winter
