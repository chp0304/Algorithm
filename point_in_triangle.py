'''
Author: chp
Date: 2023-04-11 12:40:25
LastEditTime: 2023-04-11 13:32:48
LastEditors: chp
Description: 判断点在三角形的内外部
FilePath: \python\algorithm\PIT\point_in_triangle.ipynb
Reference: https://blackpawn.com/texts/pointinpoly/
'''

import numpy as np

'''
description: 判断点point1与point2是否位于顶点a与b构成的向量的同一侧
param {*} point1 待判断的点的坐标
param {*} point2 不与三角形顶点a,b共线的三角形的另一顶点
param {*} a 三角形的一个顶点
param {*} b 三角形的另一个顶点
return {*} 在同一侧return True,不在同一侧return False
'''
def Sameside(point1,point2,a,b):
    cp1 = np.cross(point1 - a,b - a)
    cp2 = np.cross(point2 - a,b - a)
    if np.dot(cp1,cp2) >=0:
        return True
    else:
        return False

'''
description: 根据内部点与第三个顶点与三角形一边的同一侧来判断一点是否位于三角形的内部
param {*} point 待判断的点
param {*} a 三角形的一个顶点
param {*} b 同上
param {*} c 同上
return {*} 位于三角形的内部return True,位于外部,return False
'''
def PointTriangle1(point,a,b,c):
    flag1 = Sameside(point,a,b,c)
    flag2 = Sameside(point,b,a,c)
    flag3 = Sameside(point,c,a,b)
    if flag1 and flag2 and flag3:
        return True
    else:
        return False
      
      
      
'''
description: 根据三角形内部点可以三角形的两边来表示来判断一点是否位于三角形的内部
param {*} point 待判断的点
param {*} a 三角形的一个顶点
param {*} b 同上
param {*} c 同上
return {*} 位于三角形的内部return True,位于外部,return False
'''
def PointTriangle2(point,a,b,c):
    v1 = b - a
    v2 = c - a
    v = point - a
    a = (v2[1] * v[0] - v2[0] * v[1]) / (v1[0] * v2[1] - v1[1] * v2[0])
    b = (v1[1] * v[0] - v1[0] * v[1]) / (v1[1] * v2[0] - v1[0] * v2[1])
    if a < 0 or b < 0 :
        return False
    if a + b > 1 :
        return False
    if a > 1 or b > 1:
        return False
    return True
  
  

  if __name__ == "__main__":
    a = np.array([0,0])
    b = np.array([1,0])
    c = np.array([0,1])
    point = np.array([0.1,0.2])
    print(PointTriangle2(point,a,b,c))
