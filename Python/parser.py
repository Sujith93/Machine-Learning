# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:33:23 2017

@author: jagadeeshwr Reddy
"""

'''
################argument parser##############3
import math


def cylinder_volumn(radius,height):
    vol=(math.pi)*(radius**2)*(height)
    return vol

if __name__=='__main__':
    print(cylinder_volumn(2,4))
    

#run in cmd(excute the file ,it will show the result) 

'''
'''
#2
import math
import argparse

parser=argparse.ArgumentParser(description='calculate volumn of the cylinder')
parser.add_argument('-r','--radius',type=int,help='Radius of Cylinder') #short hand --r
parser.add_argument('-H','--height',type=int,help='Height of Cylinder') # short hand --H
args=parser.parse_args()

def cylinder_volumn(radius,height):
    vol=(math.pi)*(radius**2)*(height)
    return vol

if __name__=='__main__':
    print(cylinder_volumn(args.radius,args.height))




#cmd
#parser.py -h(help)
#parser.py 2 4(return the volumn)
#parser.py -r 2 -H  4
#parser.py -H 4 -r 2


'''
import argparse
parser = argparse.ArgumentParser(description='Train model')
parser.add_argument('--preset', type=str, help='model preset (features and hyperparams)')
parser.add_argument('--optimize', action='store_true', help='optimize model params')
parser.add_argument('--fold', type=int, help='specify fold')
parser.add_argument('--threads', type=int, default=4, help='specify thread count')


args = parser.parse_args()






