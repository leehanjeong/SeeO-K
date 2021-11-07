Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
Copyright (c) 2021 KOBOTEN kobot1010@gmail.com.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

import cv2
import numpy as np
HSV = {
    (120/2, 100*(255/100), 100*(255/100)): '생기있는 초록색',
    (96/2, 81*(255/100), 65*(255/100)): '어두운 초록색',
    (240/2, 100*(255/100), 100*(255/100)): '차가운 파란색',
    (111, 91, 30): '어두운 남색',
    (35/2, 100*(255/100), 100*(255/100)): '밝은 주황색',
    (0, 0, 0): '검정색',
    (255/2, 0, 0): '빨간색',
    (0, 100*(255/100), 100*(255/100)): '화사한 분홍색',
    (0, 0, 100*(255/100)): '흰색',
    (0, 0, 50*(255/100)): '회색',
    (60/2, 1*(255/100), 85*(255/100)): '밝은 회색',
    (109, 53, 67): '어두운 회색',
    (95, 1*2.55, 29*2.55): '어두운 회색',
    (329/2, 81*(255/100), 50*(255/100)): '자주색',
    (347/2, 71*(255/100), 85*(255/100)): '라즈베리색',
    (327/2, 78*(255/100), 89*(255/100)): '형광 분홍색',
    (345/2, 33*(255/100), 95*(255/100)): '연한 분홍색',
    (18/2, 42*(255/100), 95*(255/100)): '복숭아색',
    (16/2, 69*(255/100), 100*(255/100)): '산호색',
    (48/2, 50*(255/100), 98*(255/100)): '밝은 노란색',
    #(54/2, 69*107,  25,  91(255/100), 99*(255/100)): '화사한 노란색',
    (39/2, 74*(255/100), 95*(255/100)): '귤색',
    (69/2, 68*(255/100), 93*(255/100)): '파스텔 연두색',
    (87/2, 70*(255/100), 78*(255/100)): '밝은 초록색',
    (168/2, 55*(255/100), 76*(255/100)): '상큼한 민트색',
    (69/2, 55*(255/100), 52*(255/100)): '올리브색',
    (58/2, 37*(255/100), 36*(255/100)): '카키색',
    (22/2, 50*(255/100), 25*(255/100)): '갈색',
    (196/2, 63*(255/100), 91*(255/100)): '밝은 하늘색',
    (168/2, 122*(255/100), 202*(255/100)): '라벤더색',
    (281/2, 86*(255/100), 42*(255/100)): '쨍한 보라색',
    (120/2, 34*(255/100), 47*(255/100)): '버건디색',
    (351/2, 72*(255/100), 47*(255/100)): '어두운 갈색',
    (37/2, 77*(255/100), 64*(255/100)): '겨자색',
    (36/2, 27*(255/100), 79*(255/100)): '모래색',
    (210/2, 14*(255/100), 88*(255/100)): '연청색',
    (40/2, 31*(255/100), 81*(255/100)): '진한 베이지색',
    (39/2, 14*(255/100), 99*(255/100)): '밝은 베이지색',
    (60/2, 6*(255/100), 97*(255/100)): '밝은 아이보리색',
    (87/2,45*(255/100),70*(255/100)): '녹차색',
    (182/2,82*(255/100),63*(255/100)): '에메랄드 초록색',
    
}
hsv = list(HSV.keys())
hsv_len = len(hsv)

# # 옷의 색에서 추출된 HSV 값들(hsv_list)을 위 자료구조에서의 HSV 값들과 비교해 가장 비슷한 색을 추출
def extract_color(rgb_list):
   
    for i in range(len(rgb_list)):
        print(rgb_list[i])
        rgb_list[i] = rgb_list[i].tolist()
        rgb_list[i] = np.uint8([[rgb_list[i]]])
        rgb_list[i] = cv2.cvtColor(rgb_list[i], cv2.COLOR_RGB2HSV)
        rgb_list[i] = rgb_list[i][0][0]

    print('rgb_list after: ', rgb_list)
    color_name_list = []

    for i in range(len(rgb_list)):
        minimum = 99999999
        for j in range(hsv_len):
            chai = 0
            # H, S, V 3가지 비교
            for k in range(3):
                chai += abs(rgb_list[i][k] - hsv[j][k]) * (3-k)

            if (chai == 0):
                chai +=abs(rgb_list[i][2] - hsv[j][2])
            if chai < minimum:
                minimum = chai
                closest_color = HSV[hsv[j]]
                

        color_name_list.append(closest_color)
    return color_name_list
