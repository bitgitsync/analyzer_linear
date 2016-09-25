# -*- coding: utf-8 -*-
#import debug

#debug = debug.debug_struct().debug

#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei'] 
mpl.rcParams['axes.unicode_minus']=False
mpl.rcParams['xtick.labelsize']=16 
#支持显示中文 

def LineFunction(x,a,b):
    return a * x + b
#线性方程

if __name__ == '__main__':
    
    plt.title(u"线性重复性区间演示")
    plt.xlabel(u"x 轴")
    plt.ylabel(u"y 轴")
    
    ScalLowPointValue =  400
    #小量程设定 值
    ScalHighPointValue = 1000
    #大量程 设定值 
    LowHighfillalpha =0.3
    # 填充区透明度 ，越大透明度越低，最高 1
    
    ScalLowPointValueRepeatability = 0.7
    #小量程重复性 设定 
    ScalHighPointValueRepeatability = 0.1
    #大量程 重复性设定 
    
    LineTextXPointValue = 1100
    #标注文字坐标    
    LineTextYPointValue = 1100
    
    LowScalLinePointtoXPositiveDirectionValue = 230
    
    LowScalLinePointtoXNegativeDirectionValue = 300
    
    #标注文字坐标
    
    x = np.linspace(0, ScalHighPointValue+100)
    #绘图坐标范围设定 
    
    y = np.linspace(0, ScalHighPointValue+100)
    
    LineBetwenZeroandL = x[np.where((x>=0 )&(x<=ScalLowPointValue +5))]
    #填充范围设定 零点到小量程 ，在边界有无法完全填充的现象
    LineBetwenZeroandH = x[np.where((x>=0)&(x<=ScalHighPointValue ))]
    #填充范围设定 零点到大量程 
    LineBetwenLandH = x[np.where((x>=ScalLowPointValue)&(x<=ScalHighPointValue))]
    #填充范围设定 小量程到大量程     
    LineYBetwenZeroandH = x[np.where((x>=ScalHighPointValue*ScalHighPointValueRepeatability))]
    LineYBetwenZeroandL = x[np.where((x>=ScalLowPointValue*ScalLowPointValueRepeatability))]
    
    line, = plt.plot(x, LineFunction(x, 1, 0), '-', linewidth=2)
    plt.annotate('y=x', xy=(LineTextXPointValue, LineTextXPointValue), xytext=(LineTextXPointValue+50, LineTextXPointValue+50), arrowprops=dict(facecolor='blue', shrink=0.1))
    # 方程 y=x 是中线，即在理想状态下的结果变化曲线
    
    line, = plt.plot(x, LineFunction(x,(1-ScalHighPointValueRepeatability),0), '-.', linewidth=1)
#    plt.annotate('HighScalMaxDeviationPositiveDirection 大量程正向最大偏差', xy=(1100, 1210), xytext=(950, 1300), arrowprops=dict(facecolor='green', shrink=0.1))
    plt.annotate(u'高量程正向最大偏差', xy=(1100, 1210), xytext=(950, 1300), arrowprops=dict(facecolor='green', shrink=0.1))

    # 大量程段最低偏差曲线 
    
    line, = plt.plot(x, LineFunction(x,(1+ScalHighPointValueRepeatability),0) , '-.', linewidth=1)
#    plt.annotate('HighScalMaxDeviationNegativeDirection大量程负向最大偏差', xy=(1100, 1000), xytext=(1000, 850), arrowprops=dict(facecolor='red', shrink=0.1))
    plt.annotate(u'高量程负向最大偏差', xy=(1100, 1000), xytext=(1000, 850), arrowprops=dict(facecolor='red', shrink=0.1))

    # 大量程段最高偏差曲线 
    
    line, = plt.plot(0 * x + ScalHighPointValue , x, '-', linewidth=1)
    # 大量程的标志线
    line, = plt.plot(0 * x + ScalLowPointValue , x, '-', linewidth=1)
    # 小量程的标志线
    
    line, = plt.plot(x, LineFunction(x, (1+ScalLowPointValueRepeatability),0), '.-', linewidth=1)
#    plt.annotate('LowScalMaxDeviationPositiveDirection', xy=(260, 300), xytext=(50, 500),arrowprops=dict(facecolor='orange', shrink=0.1))
    plt.annotate(u'低量程正向最大偏差', xy=(LowScalLinePointtoXPositiveDirectionValue, LineFunction(LowScalLinePointtoXPositiveDirectionValue, (1+ScalLowPointValueRepeatability),0)), xytext=(50, 500),arrowprops=dict(facecolor='orange', shrink=0.1))

    #小量程段最高偏差曲线
    
    line, = plt.plot(x, LineFunction(x, (1-ScalLowPointValueRepeatability),0), '.-', linewidth=1)
    plt.annotate(u'低量程负向最大偏差', xy=(LowScalLinePointtoXNegativeDirectionValue, LineFunction(LowScalLinePointtoXNegativeDirectionValue, (1-ScalLowPointValueRepeatability),0)), xytext=(350, 10),arrowprops=dict(facecolor='black', shrink=0.1))
    #大量程段最低偏差曲线
#    line, = plt.plot(x, 0 * x + 900, '.', linewidth=1)
#    plt.annotate('y=900', xy=(800, 200), xytext=(800, 200))
#    line, = plt.plot(x, 0 * x + 1100, '.', linewidth=1)
#    plt.annotate('y=900', xy=(800, 200), xytext=(800, 200))

    linex = [ScalLowPointValue, ScalHighPointValue]
    liney = [ScalLowPointValue * (1- ScalLowPointValueRepeatability), ScalHighPointValue * (1 - ScalHighPointValueRepeatability)]
    plt.plot(linex, liney)
    #小量程偏差低点 连接 大量程 偏差低点
         
    linex = [ScalLowPointValue, ScalHighPointValue]
    liney = [ScalLowPointValue * (1+ScalLowPointValueRepeatability), ScalHighPointValue * (1+ ScalHighPointValueRepeatability)]
    plt.plot(linex, liney)
    #小量程偏差高点 连接 大量程 偏差高点
    
    
    a1 = (ScalHighPointValue*(1-ScalHighPointValueRepeatability)-ScalLowPointValue*(1-ScalLowPointValueRepeatability))/(ScalHighPointValue - ScalLowPointValue)
    b1 = ScalHighPointValue*(1-ScalHighPointValueRepeatability) - a1*ScalHighPointValue
    line, = plt.plot(LineBetwenLandH, LineFunction(LineBetwenLandH, a1,b1), '.', linewidth=1)
    #高量程最大偏差和低量程最大偏差的连线
    plt.fill_between(LineBetwenZeroandL , LineFunction(LineBetwenZeroandL , (1+ ScalLowPointValueRepeatability),0),LineFunction(LineBetwenZeroandL, 1, 0) ,color='blue',alpha=LowHighfillalpha)

#    plt.fill_between(LineBetwenLandH , LineFunction(LineBetwenLandH , (1+ ScalHighPointValueRepeatability),0),LineFunction(LineBetwenLandH, 1, 0) ,color='blue',alpha=LowHighfillalpha)
    
#    plt.fill_between(LineBetwenZeroandL , LineFunction(x , a1,b1), '.', linewidth=1)

    #小量程偏差低点 连接 大量程 偏差低点 方程
    
    a2 = (ScalHighPointValue*(1+ScalHighPointValueRepeatability)-ScalLowPointValue*(1+ScalLowPointValueRepeatability))/(ScalHighPointValue - ScalLowPointValue)
    b2 = ScalHighPointValue*(1+ScalHighPointValueRepeatability) - a2*ScalHighPointValue
    line, = plt.plot(LineBetwenLandH, LineFunction(LineBetwenLandH, a2,b2), '.', linewidth=2)
    #高量程最大偏差和低量程最大偏差的连线
    
##    plt.fill_between(LineBetwenLandH , LineFunction(LineBetwenLandH , a2,b2),LineFunction(LineBetwenLandH, 1, 0) ,color='red',alpha=LowHighfillalpha)
    plt.fill_between(LineBetwenZeroandH , LineFunction(LineBetwenZeroandH , (1+ScalHighPointValueRepeatability),0),LineFunction(LineBetwenZeroandH, 1, 0) ,color='red',alpha=LowHighfillalpha)

    plt.fill_between(LineBetwenLandH , LineFunction(LineBetwenLandH , (1+ScalHighPointValueRepeatability),0),LineFunction(LineBetwenLandH, a2, b2) ,color='green',alpha=LowHighfillalpha)
      
    #小量程偏差高点 连接 大量程 偏差高点 方程 

    line, = plt.plot(LineYBetwenZeroandH, LineFunction(LineYBetwenZeroandH ,1, - ScalHighPointValueRepeatability* ScalHighPointValue), '-', linewidth=1)
    #高量程偏差绝对值
    
    line, = plt.plot(LineYBetwenZeroandL, LineFunction(LineYBetwenZeroandL,1, - ScalLowPointValueRepeatability* ScalLowPointValue), '-', linewidth=1)
    #低量程偏差绝对值

    plt.annotate(u'高低量程变换点A', xy=(405, 670), xytext=(250, 750), arrowprops=dict(facecolor='green', shrink=0.1))
    plt.annotate(u'高低量程变换点B', xy=(410, 420), xytext=(200, 650), arrowprops=dict(facecolor='red', shrink=0.1))
    plt.annotate(u'高量程正向偏差C', xy=(1010, 1110), xytext=(800, 1150), arrowprops=dict(facecolor='red', shrink=0.1))
    plt.annotate(u'高低量程偏差交叉点D', xy=(135, 50), xytext=(100, -200), arrowprops=dict(facecolor='red', shrink=0.1))

    fillLowHighRepeatability = 0
#    plt.fill(,,alpha=0.3)
#    fig, (ax1) = plt.subplots(3, 1, sharex=True)

#    plt.fill_between(x, ScalLowPointValue ,ScalHighPointValue * (1-ScalHighPointValueRepeatability))
#    plt.fill_between(y, ScalLowPointValue,ScalHighPointValue)
    
       
    plt.grid(True)
    
#    line, = plt.plot(x, 0.8 * x, '.-', linewidth=1)
#    plt.annotate('y=0.8*x', xy=(1400, 1200), xytext=(1450, 1100))

    
#    dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
#    line.set_dashes(dashes)
    
    plt.show()
