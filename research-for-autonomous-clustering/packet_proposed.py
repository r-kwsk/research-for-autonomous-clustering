# -*- coding: UTF-8 -*-
#matplotlib inline
from pylab import *
import random
import numpy as np
np.set_printoptions(threshold=np.inf)#npによる大型行列を全て表示
from math import sqrt#平方根
from math import fabs#少数まで扱う絶対値
import math
import result
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import networkx as nx
import statistics as sta
import os
fig = plt.figure(figsize=(7,7))


color_list=['#6e69ee', '#367e21', '#9bd8f6', '#f10274', '#25c03f', '#d32898', '#e006ce', '#fcf6b2', '#b2a79c', '#06cc6f', '#e6573d', '#63cfea', '#1cae9b', '#95c001', '#d18308', '#7686f1', '#9bfe01', '#bbbc2f', '#02c9b7', '#d51293', '#8a2426', '#64a282', '#a3bd0a', '#0d0981', '#99352d', '#592913', '#81eb65', '#ca94af', '#07a4d1', '#59bfb0', '#55affc', '#907308', '#93b836', '#23a28e', '#dc248e', '#2dc68b', '#42c8d0', '#e464aa', '#445738', '#a92b78', '#f2b2a1', '#81209d', '#adaa0b', '#3d675b', '#6964f3', '#72f55d', '#85c215', '#398137', '#52009f', '#8f5f73', '#038e21', '#b11a5f', '#ce1477', '#07767b', '#93bdf2', '#91a221', '#39e768', '#5ebcad', '#9c84c4', '#68e23f', '#7b0e84', '#deced1', '#f98bed', '#0e7f79', '#f567fe', '#9d1f63', '#a7662a', '#72d38f', '#b692eb', '#c874a9', '#122913', '#fa331b', '#3ae2c3', '#3a9787', '#bbeca5', '#ec0297', '#dbb435', '#7540d4', '#0cea12', '#ef45e1', '#4cfe6a', '#b9ec1f', '#3603c3', '#8326a2', '#eb3871', '#36a4b2', '#04dcd9', '#b3e5ef', '#86c928', '#ca6f31', '#05ea7b', '#338056', '#389f4d', '#fe8856', '#30f295', '#5e8336', '#1f0344', '#e98ccc', '#90f0da', '#ec9290', '#dbc602', '#924af2', '#066597', '#78fed2', '#6692e4', '#0176ed', '#dc070c', '#6beb76', '#b1caf0', '#7755c2', '#2fc26e', '#53a9a0', '#266b54', '#76c4ce', '#505d21', '#f243df', '#d842ed', '#a79283', '#ba71b9', '#ccb7b0', '#3a6071', '#b2231f', '#482725', '#633d1b', '#bc192a', '#36315e', '#ccf213', '#3fc63c', '#73ebca', '#b1ac89', '#64be9a', '#9cf98a', '#e88353', '#7e9f24', '#8b16c2', '#3669ca', '#4af74c', '#7e249f', '#2522c8', '#a545c0', '#5e00b8', '#187cf5', '#c47f27', '#c9c70e', '#9e9071', '#45421a', '#04517d', '#fe4d5d', '#1319a6', '#df43e3', '#fefed0', '#f581d8', '#bdce7d', '#e2e6de', '#6d3017', '#d77e82', '#31988e', '#cd1e0e', '#fc7524', '#80360f', '#a623f4', '#82cd1c', '#4b71a2', '#bf3384', '#7fd628', '#e35d4e', '#6e6dfa', '#d014ae', '#39d97a', '#bd9562', '#e130ea', '#477ff6', '#07923a', '#3c82e1', '#dbf8e9', '#0ccd3d', '#177d59', '#ede3fe', '#b6d935', '#1ddd5a', '#774f5c', '#b9e46a', '#1d22ac', '#2718a0', '#a87fd9', '#043a51', '#e3e8d3', '#79e1e4', '#424128', '#d1d41e', '#ab6124', '#3f5fe7', '#1e6d85', '#fbd717', '#07bafc', '#73a614', '#3fa1b1', '#37513e', '#dd3cfb', '#6feb75', '#e1869e', '#e28589', '#42f7b5', '#479117', '#18d7af', '#df4eb6', '#228239', '#3f4b9b', '#a285a0', '#e38fa9', '#f26658', '#bab8a4', '#1c5922', '#e6ea82', '#636a9c', '#a0e25f', '#ac15f9', '#84d21f', '#30d51c', '#3043e7', '#707c62', '#4ca8c1', '#c13889', '#9c362a', '#8ac13e', '#b45815', '#4bdfc0', '#09c374', '#1b6195', '#b5f12d', '#2a4019', '#c937a2', '#5a4432', '#e63c10', '#655e16', '#fecc17', '#132a2b', '#7a59cc', '#bd2b16', '#61aa7d', '#0dcd94', '#05d4e9', '#db4bcc', '#68d3ff', '#c40a15', '#90fcfb', '#069877', '#3a6ff9', '#764118', '#d4270a', '#32b4b5', '#aa9dbf', '#18dc4b', '#a3f499', '#b2b4d0', '#126ef7', '#e2a39e', '#54dc20', '#8b1984', '#45c283', '#190895', '#267a43', '#9e4797', '#e15836', '#b38137', '#3fb1e7', '#2203e7', '#e1797b', '#ca8172', '#c2c26c', '#fb3625', '#29e829', '#35c940', '#23bfc4', '#f53db0', '#0340c9', '#b4b989', '#875a50', '#232aa9', '#302755', '#c88fab', '#937d52', '#667758', '#297684', '#c330f9', '#dd3fbf', '#cfbf4e', '#1b0176', '#83eec3', '#8e325a', '#7bbf44', '#8cd083', '#f182f4', '#4ccc10', '#a55a22', '#cd024b', '#a67928', '#c7cd05', '#2de6b9', '#183c93', '#1f7d79', '#8f4264', '#d20e64', '#5c297a', '#ff4c7f', '#a90909', '#e385b4', '#bb0f5a', '#509904', '#05f860', '#05e333', '#adc74c', '#28f311', '#ab035d', '#0bbf59', '#e77331', '#0f18a7', '#703c8e', '#296bc7', '#6a98bd', '#214096', '#7b95a3', '#6a11d5', '#7019d4', '#3dd1b4', '#cf0b06', '#f703a7', '#ec9750', '#fae540', '#8b4a35', '#7bf860', '#670096', '#f15e7b', '#aad1bc', '#95f3ef', '#9d3ff0', '#a19a80', '#d770b3', '#aa0646', '#878b8e', '#bff057', '#08317a', '#62b97c', '#8a105e', '#06fc09', '#2b060c', '#4b42c9', '#2c50ce', '#25a7f0', '#3ebd4d', '#b2f0a4', '#fb554a', '#9ab555', '#aba480', '#8a02c5', '#f14323', '#03c64f', '#a2b861', '#38f96c', '#c12641', '#0bf095', '#eebb67', '#482f47', '#6d28f5', '#1ab118', '#6cedec', '#553575', '#5846a0', '#2ef21d', '#a3af8a', '#3bb787', '#a3cc03', '#dc7d46', '#ea0338', '#61f99f', '#af304b', '#f4f750', '#31cf41', '#6870ca', '#ec7bb3', '#48531e', '#7520d7', '#4633fb', '#4067c3', '#f03d0a', '#993704', '#70a81b', '#02fca3', '#fca9e0', '#56b79a', '#a4404c', '#67f599', '#93ef80', '#35508a', '#05b5b2', '#9c35b3', '#7152c3', '#fedd77', '#5ff0fd', '#dbac4a', '#587fc4', '#f89037', '#0ba952', '#1d6648', '#dccfec', '#f0d3a1', '#9fcabd', '#97ce1c', '#a23ae0', '#52d122', '#0ab087', '#fcd05f', '#2edaa0', '#591d53', '#5af906', '#9b6988', '#1b9217', '#40718e', '#867da2', '#7069e9', '#197306', '#4b431c', '#5e7e37', '#3c0a39', '#ca946e', '#445a53', '#7cd04e', '#721d80', '#dba01a', '#6ce796', '#789cfd', '#84d548', '#f8b5a1', '#90e904', '#39e2e1', '#5fc94a', '#2792b1', '#a2ab4c', '#59489c', '#841e83', '#3b0e18', '#609567', '#329367', '#569fbb', '#b8e7e8', '#40dc31', '#8a58c3', '#f33128', '#3e9ec2', '#deed51', '#21de7a', '#2a61c3', '#014cdf', '#8e5ab9', '#61be8f', '#d53653', '#74f5e9', '#512fe2', '#62b5ae', '#c774f8', '#cfcc7d', '#b85479', '#5d6348', '#50a9fc', '#225e3d', '#6a3b64', '#9f60dc', '#5b684c', '#0df3dc', '#4ffa42', '#7189e4', '#675317', '#975caa', '#c574ec', '#24be7c', '#578906', '#4c6f9f', '#86e1e6', '#fcb139', '#14b47e', '#b34a0e', '#cb7025', '#3795ae', '#37f012', '#14416f', '#cbc589', '#448432', '#ed8787', '#196753', '#416f04', '#1f37c9', '#fbda25', '#7b6bcc', '#1ea2b8', '#c7b4b1', '#6f6719', '#b1befb', '#a7c960', '#f7a85c', '#a34f17','#6e69ee', '#367e21', '#9bd8f6', '#f10274', '#25c03f', '#d32898', '#e006ce', '#fcf6b2', '#b2a79c', '#06cc6f', '#e6573d', '#63cfea', '#1cae9b', '#95c001', '#d18308', '#7686f1', '#9bfe01', '#bbbc2f', '#02c9b7', '#d51293', '#8a2426', '#64a282', '#a3bd0a', '#0d0981', '#99352d', '#592913', '#81eb65', '#ca94af', '#07a4d1', '#59bfb0', '#55affc', '#907308', '#93b836', '#23a28e', '#dc248e', '#2dc68b', '#42c8d0', '#e464aa', '#445738', '#a92b78', '#f2b2a1', '#81209d', '#adaa0b', '#3d675b', '#6964f3', '#72f55d', '#85c215', '#398137', '#52009f', '#8f5f73', '#038e21', '#b11a5f', '#ce1477', '#07767b', '#93bdf2', '#91a221', '#39e768', '#5ebcad', '#9c84c4', '#68e23f', '#7b0e84', '#deced1', '#f98bed', '#0e7f79', '#f567fe', '#9d1f63', '#a7662a', '#72d38f', '#b692eb', '#c874a9', '#122913', '#fa331b', '#3ae2c3', '#3a9787', '#bbeca5', '#ec0297', '#dbb435', '#7540d4', '#0cea12', '#ef45e1', '#4cfe6a', '#b9ec1f', '#3603c3', '#8326a2', '#eb3871', '#36a4b2', '#04dcd9', '#b3e5ef', '#86c928', '#ca6f31', '#05ea7b', '#338056', '#389f4d', '#fe8856', '#30f295', '#5e8336', '#1f0344', '#e98ccc', '#90f0da', '#ec9290', '#dbc602', '#924af2', '#066597', '#78fed2', '#6692e4', '#0176ed', '#dc070c', '#6beb76', '#b1caf0', '#7755c2', '#2fc26e', '#53a9a0', '#266b54', '#76c4ce', '#505d21', '#f243df', '#d842ed', '#a79283', '#ba71b9', '#ccb7b0', '#3a6071', '#b2231f', '#482725', '#633d1b', '#bc192a', '#36315e', '#ccf213', '#3fc63c', '#73ebca', '#b1ac89', '#64be9a', '#9cf98a', '#e88353', '#7e9f24', '#8b16c2', '#3669ca', '#4af74c', '#7e249f', '#2522c8', '#a545c0', '#5e00b8', '#187cf5', '#c47f27', '#c9c70e', '#9e9071', '#45421a', '#04517d', '#fe4d5d', '#1319a6', '#df43e3', '#fefed0', '#f581d8', '#bdce7d', '#e2e6de', '#6d3017', '#d77e82', '#31988e', '#cd1e0e', '#fc7524', '#80360f', '#a623f4', '#82cd1c', '#4b71a2', '#bf3384', '#7fd628', '#e35d4e', '#6e6dfa', '#d014ae', '#39d97a', '#bd9562', '#e130ea', '#477ff6', '#07923a', '#3c82e1', '#dbf8e9', '#0ccd3d', '#177d59', '#ede3fe', '#b6d935', '#1ddd5a', '#774f5c', '#b9e46a', '#1d22ac', '#2718a0', '#a87fd9', '#043a51', '#e3e8d3', '#79e1e4', '#424128', '#d1d41e', '#ab6124', '#3f5fe7', '#1e6d85', '#fbd717', '#07bafc', '#73a614', '#3fa1b1', '#37513e', '#dd3cfb', '#6feb75', '#e1869e', '#e28589', '#42f7b5', '#479117', '#18d7af', '#df4eb6', '#228239', '#3f4b9b', '#a285a0', '#e38fa9', '#f26658', '#bab8a4', '#1c5922', '#e6ea82', '#636a9c', '#a0e25f', '#ac15f9', '#84d21f', '#30d51c', '#3043e7', '#707c62', '#4ca8c1', '#c13889', '#9c362a', '#8ac13e', '#b45815', '#4bdfc0', '#09c374', '#1b6195', '#b5f12d', '#2a4019', '#c937a2', '#5a4432', '#e63c10', '#655e16', '#fecc17', '#132a2b', '#7a59cc', '#bd2b16', '#61aa7d', '#0dcd94', '#05d4e9', '#db4bcc', '#68d3ff', '#c40a15', '#90fcfb', '#069877', '#3a6ff9', '#764118', '#d4270a', '#32b4b5', '#aa9dbf', '#18dc4b', '#a3f499', '#b2b4d0', '#126ef7', '#e2a39e', '#54dc20', '#8b1984', '#45c283', '#190895', '#267a43', '#9e4797', '#e15836', '#b38137', '#3fb1e7', '#2203e7', '#e1797b', '#ca8172', '#c2c26c', '#fb3625', '#29e829', '#35c940', '#23bfc4', '#f53db0', '#0340c9', '#b4b989', '#875a50', '#232aa9', '#302755', '#c88fab', '#937d52', '#667758', '#297684', '#c330f9', '#dd3fbf', '#cfbf4e', '#1b0176', '#83eec3', '#8e325a', '#7bbf44', '#8cd083', '#f182f4', '#4ccc10', '#a55a22', '#cd024b', '#a67928', '#c7cd05', '#2de6b9', '#183c93', '#1f7d79', '#8f4264', '#d20e64', '#5c297a', '#ff4c7f', '#a90909', '#e385b4', '#bb0f5a', '#509904', '#05f860', '#05e333', '#adc74c', '#28f311', '#ab035d', '#0bbf59', '#e77331', '#0f18a7', '#703c8e', '#296bc7', '#6a98bd', '#214096', '#7b95a3', '#6a11d5', '#7019d4', '#3dd1b4', '#cf0b06', '#f703a7', '#ec9750', '#fae540', '#8b4a35', '#7bf860', '#670096', '#f15e7b', '#aad1bc', '#95f3ef', '#9d3ff0', '#a19a80', '#d770b3', '#aa0646', '#878b8e', '#bff057', '#08317a', '#62b97c', '#8a105e', '#06fc09', '#2b060c', '#4b42c9', '#2c50ce', '#25a7f0', '#3ebd4d', '#b2f0a4', '#fb554a', '#9ab555', '#aba480', '#8a02c5', '#f14323', '#03c64f', '#a2b861', '#38f96c', '#c12641', '#0bf095', '#eebb67', '#482f47', '#6d28f5', '#1ab118', '#6cedec', '#553575', '#5846a0', '#2ef21d', '#a3af8a', '#3bb787', '#a3cc03', '#dc7d46', '#ea0338', '#61f99f', '#af304b', '#f4f750', '#31cf41', '#6870ca', '#ec7bb3', '#48531e', '#7520d7', '#4633fb', '#4067c3', '#f03d0a', '#993704', '#70a81b', '#02fca3', '#fca9e0', '#56b79a', '#a4404c', '#67f599', '#93ef80', '#35508a', '#05b5b2', '#9c35b3', '#7152c3', '#fedd77', '#5ff0fd', '#dbac4a', '#587fc4', '#f89037', '#0ba952', '#1d6648', '#dccfec', '#f0d3a1', '#9fcabd', '#97ce1c', '#a23ae0', '#52d122', '#0ab087', '#fcd05f', '#2edaa0', '#591d53', '#5af906', '#9b6988', '#1b9217', '#40718e', '#867da2', '#7069e9', '#197306', '#4b431c', '#5e7e37', '#3c0a39', '#ca946e', '#445a53', '#7cd04e', '#721d80', '#dba01a', '#6ce796', '#789cfd', '#84d548', '#f8b5a1', '#90e904', '#39e2e1', '#5fc94a', '#2792b1', '#a2ab4c', '#59489c', '#841e83', '#3b0e18', '#609567', '#329367', '#569fbb', '#b8e7e8', '#40dc31', '#8a58c3', '#f33128', '#3e9ec2', '#deed51', '#21de7a', '#2a61c3', '#014cdf', '#8e5ab9', '#61be8f', '#d53653', '#74f5e9', '#512fe2', '#62b5ae', '#c774f8', '#cfcc7d', '#b85479', '#5d6348', '#50a9fc', '#225e3d', '#6a3b64', '#9f60dc', '#5b684c', '#0df3dc', '#4ffa42', '#7189e4', '#675317', '#975caa', '#c574ec', '#24be7c', '#578906', '#4c6f9f', '#86e1e6', '#fcb139', '#14b47e', '#b34a0e', '#cb7025', '#3795ae', '#37f012', '#14416f', '#cbc589', '#448432', '#ed8787', '#196753', '#416f04', '#1f37c9', '#fbda25', '#7b6bcc', '#1ea2b8', '#c7b4b1', '#6f6719', '#b1befb', '#a7c960', '#f7a85c', '#a34f17']

#-----------------------------計測対象の準備-------------------------------------------

#sd=4 #使えないsd=2,9,15,17,23,25,28,沖縄研究会のときsd=4
#一つの図に複数の拡散係数におけるグラフを描画する準備.研究ノートP.30裏面参照
z_num=3#グラフの本数
sigma_list=[]
rdec_list=[]
CH_timecount_list_of_list=[]
not_pattern_timecount_list_of_list=[]
connectivity_timecount_list_of_list=[]
CHswitch_timecount_list_of_list=[]
generate_timecount_list_of_list=[]
vanish_timecount_list_of_list=[]
#さらに複数のNWのサンプル数で平均する準備。研究ノートp.31表面参照
sd_list=[]
zz_num=1#実際のシミュレーション回数、リンク切れの初期位置を避けたもの
zz_num_dammy=1#zzを回す回数,zz_num==15の時22とする
TIME=100
CH_timecount_list_of_sdsumlist=[[0 for i in range(TIME)]for j in range(z_num)]
not_pattern_timecount_list_of_sdsumlist=[[0 for i in range(TIME)]for j in range(z_num)]
connectivity_timecount_list_of_sdsumlist=[[0 for i in range(TIME)]for j in range(z_num)]
CHswitch_timecount_list_of_sdsumlist=[[0 for i in range(TIME)]for j in range(z_num)]
generate_timecount_list_of_sdsumlist=[[0 for i in range(TIME)]for j in range(z_num)]
vanish_timecount_list_of_sdsumlist=[[0 for i in range(TIME)]for j in range(z_num)]
CH_bar_list=[0 for i in range(z_num)]
not_pattern_bar_list=[0 for i in range(z_num)]
connectivity_bar_list=[0 for i in range(z_num)]
generate_bar_list=[0 for i in range(z_num)]
vanish_bar_list=[0 for i in range(z_num)]

for zz in range(zz_num_dammy):
    sd=4+zz
    if(sd==3 or sd==4 or sd==5 or sd==6 or sd==7 or sd==8 or sd==11 or sd==12 or sd==13 or sd==14 or sd==18 or sd==20 or sd==21 or sd==22 or sd==24 or sd==27 or sd==29 or sd==30 or sd==31 or sd==33 or sd==34 or sd==38 or sd==39 or sd==40 or sd==41 or sd==42 or sd==45 or sd==46 or sd==47 or sd==49 or sd==50 or sd==51 or sd==52):
        time_list=[]
        sigma_list=[]
        rdec_list=[]
        CH_timecount_list_of_list=[]
        not_pattern_timecount_list_of_list=[]
        connectivity_timecount_list_of_list=[]
        CHswitch_timecount_list_of_list=[]
        generate_timecount_list_of_list=[]
        vanish_timecount_list_of_list=[]
        sd_list.append(sd)
        print('kaisuu',len(sd_list))
        for z in range(z_num):#変更する変数を定義可能。切り替える場合は1.変数のコメントアウトを変更する2.固定する変数を定義し直す3.rdec_listにappend
            if(z==0):
                #CH_rate = 1 * 10 ** (-5)#CHの自律生成確率．4 * 10 ** (-5)が50秒に1個の生成確率．
                N_CH = 5
            elif(z==1):
                #CH_rate = 2 * 10 ** (-5)
                N_CH = 10
            elif(z==2):
                #CH_rate = 6 * 10 ** (-5)
                N_CH = 15
            '''CH_rate = round(CH_rate, 7)
            rdec_list.append(CH_rate)'''
            #sigma_list.append(sigma)
            rdec_list.append(N_CH)

            #-----------------------------変数定義-------------------------------------------
            N=500
            #N_CH = 10 #初期指定ノード数
            n=N-N_CH
            LONG=0.07#通信可能距離
            long=1-LONG#周期境界条件を満たす通信可能距離
            #----------------------CH以外のノードの乱数配置---------------------------
            #x=np.random.seed()#random.seedは毎回同じ乱数を発生させるもの
            x=np.random.seed(sd-1)
            x=np.random.rand(N)#0から1の乱数をノード数だけ発生．
            y=np.random.seed(sd-2)
            y=np.random.rand(N)
            x=list(x)#npリストを標準化
            y=list(y)

            #CH以外のノードの初期分布値
            #q=np.random.seed(sd+1)#初期値を割り振ると、クラスタ形成が遅くなる。
            #q=np.random.rand(n)
            q=[0 for i in range(n)]
            '''
            #初期状態量あり
            q=np.random.seed(sd+1)
            q=np.random.rand(N)#0から1の乱数をノード数だけ発生．'''
            q=list(q)

            #---------------------CHノードを特定の位置に設置-----------------------------

            '''
            #静的環境下及びランダムウォークモデルにおけるCHの初期位置
            x.insert(0, 0.25)#(リストの位置，追加する数)
            y.insert(0, 0.25)
            x.insert(0, 0.75)
            y.insert(0, 0.25)
            x.insert(0, 0.25)
            y.insert(0, 0.75)
            x.insert(0, 0.75)
            y.insert(0, 0.75)'''

            #CHの分布値
            CH_q=3
            for i in range(N_CH):
                q.insert(0, CH_q)
            CH_flag = [0 for i in range(N)]
            for i in range(N_CH):
                CH_flag[i] = 1

            link=[[0 for i in range(N)]for j in range(N)]
            degree=[0 for i in range(N)]
            CH_deg=[0 for i in range(N)]
            #CH=[0 for i in range(N)]
            #CH_count=0#クラスタヘッド数

            #横軸をtimeとした場合の変数定義．詳しくは研究ノートp.30
            time_list=[]
            CH_counter=0#クラスタヘッド数．隣接ノードの状態量が等しい場合も，正しくカウントしている．
            CH_timecount=[]#時間毎のクラスタヘッド数
            not_pattern=0
            not_pattern_timecount=[]#時間毎の不適パターン数
            connectivity=0
            connectivity_timecount=[]#時間毎のクラスタ間辺連結性
            CHswitch=0
            CHswitch_timecount=[]#時間毎の指定ノードのCH数
            generate=0
            generate_timecount=[]#時間毎の指定ノードの生成数
            vanish=0
            vanish_timecount=[]#時間毎の指定ノードのC消滅数

            CH_num=[0 for i in range(N)]#自分が所属するクラスタヘッドのノード番号
            CH_num_prev = [-1 for i in range(N)]  # 前回自分が所属していたクラスタヘッドのノード番号
            CH_candidate_count = [0 for i in range(N)]
            size=[0 for i in range(N)]
            Q=[0 for i in range(N)]
            previous_cv=0#計算を打ち切るために使用

            #--------------------------移動モデルパラメータ-----------------------------------

            gap=[0 for i in range(N)]
            gapx=[0 for i in range(N)]
            gapy=[0 for i in range(N)]
            tangent=[0 for i in range(N)]
            theta=[0 for i in range(N)]
            radians=[0 for i in range(N)]
            next_x=[0 for i in range(N)]
            next_y=[0 for i in range(N)]

            #----------------------分布値の更新式につかう変数と式--------------------------------

            #拡散の強さ
            sigma=1#拡散の強さに関するパラメータ
            q_dec=0.01#CH以外の分布値の減少量
            CH_rate = 2 * 10 ** (-5)#CHの自律生成確率
            CH_time_rate = CH_rate * (N-N_CH) / N_CH
            CH_q = 3
            next_q=[0 for i in range(N)]
            difference_q=[0 for i in range(N)]#状態量の変化量
            difference_q_list=[]
            diffusion=[0 for i in range(N)]#更新式に用いる拡散の値
            dd=[0 for i in range(N)]
            dd_discharge=[0 for i in range(N)]
            dd_discharge_count=[0 for i in range(N)]
            zero_frag=[0 for i in range(N)]
            diffusion_individual=[[0 for i in range(N)]for j in range(N)]

            #拡散
            def diffusion1(i,j,q):
                diff=(sigma/(degree[i]+1))*(q[i]-q[j])
                return diff

            #---------------周期境界条件とUGDによる初期条件を反映したリンクを作成-------------------

            for i in range(N):
                for j in range(N):
                    dis=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])
                    #print(sqrt(dis))
                    if(sqrt(dis)<LONG and i!=j):#unit disk graph
                        link[i][j]=1
                    '''
                    else :#周期境界条件
                        if (not(x[i]>long and x[j]>long) and (x[i]>long or x[j]>long)):#どちらか片方が右端に存在するとき
                            dis=(1-fabs(x[i]-x[j]))*(1-fabs(x[i]-x[j]))+(y[i]-y[j])*(y[i]-y[j])#fabsは絶対値を少数まで扱いながら表現する．
                            if(sqrt(dis)<LONG and i!=j):
                                link[i][j]=1
                            if (not(y[i]>long and y[j]>long) and (y[i]>long or y[j]>long)):#さらに，どちらか片方が上端に存在するとき
                                dis=(1-fabs(x[i]-x[j]))*(1-fabs(x[i]-x[j]))+(1-fabs(y[i]-y[j]))*(1-fabs(y[i]-y[j]))
                                if(sqrt(dis)<LONG and i!=j):
                                    link[i][j]=1
                        if (not(y[i]>long and y[j]>long) and (y[i]>long or y[j]>long)):#どちらか片方が上端に存在するとき
                            dis=(x[i]-x[j])*(x[i]-x[j])+(1-fabs(y[i]-y[j]))*(1-fabs(y[i]-y[j]))
                            if(sqrt(dis)<LONG and i!=j):
                                link[i][j]=1
                    '''
            #--------------------------ノードの次数とリンクチェック------------------------------

            degree_total=0
            for i in range(N):#各ノードの次数決定
                for j in range(N):
                    if(link[i][j]==1):
                        degree[i]+=1

            degree_max=0#ネットワーク上におけるノードの最大次数
            for i in range(N):
                if(degree_max<=degree[i]):
                    degree_max=degree[i]
            #print(degree_max)

            for i in range(N):#リンクチェック
                if (degree[i]==0):
                    print('this is an Isorated Node !!!')
                    print(i)

            '''
            for i in range(N):#分布値が行き渡っているかチェック
                if(q[i]==0):
                    print('their q are 0 !!!')
                    print(i,degree[i])
            '''
            #print(B)

            #---------------------------------クラスタ判定------------------------------------

            max_grade=[-1 for i in range(N)]#自分と一番差があるノード番号 #自分の場合は-1のまま
            for i in range(N):
                MAX=0.0
                for j in range(N):
                    if(link[i][j]==1):
                        if(q[j]-q[i]>=MAX):#相手ー自分の値をより大きいものに更新し続ける．→自分が最も大きい場合，負の値となり、MAXは更新されない。
                            MAX=q[j]-q[i]#あるiにおける，最終的なMAXの値を下のfor文で適用している．
                for j in range(N):
                    if(link[i][j]==1):
                        if(q[j]-q[i]==MAX):#jと最も差があるのはi
                            max_grade[i]=j#ノードiともっとも差があるノードはノードj#ここまでで，隣接ノードとの状態量の差を把握している．


            #クラスタサイズ判定
            for i in range(N):
                grade1=0
                for j in range(50):#grade1=grade2の時の処理のために,jで回す必要がある．N=500は大きすぎる
                    if(j==0):#自分がCHの時の処理#j=0なのは，j=0が回し終わった時点で，自分自身がCHと判別でき，それ以降のjで回す必要がないから
                        grade1=max_grade[i]#max_grade[i]は，ノードiと一番差があるノード番号
                        if(grade1==-1):#自分がCHの時の処理　#自分と一番差があるノード番号が-1→自分がクラスタヘッドということが分かる．
                            CH_num[i]=i#ノードiが所属するクラスタのCH
                            size[i]+=1#ノードiが属するクラスタサイズ
                            break
                    grade2=max_grade[grade1]#grade2は，あるiにとって一番差があるノードgrade1,にとってさらに一番差があるノード(iから2ホップ先)．この行の一番最後のgrade1=grade2が適用される
                    if(grade2==-1):#自分（ノードi）の隣がCH←隣から探し始めたら、自分がCH←grade2==-1より
                        CH_num[i]=grade1#grade1=max_grade[i]#max_grade[i]は，ノードiと一番差があるノード番号(1ホップ先)
                        size[grade1]+=1
                        break
                    if(max_grade[grade2]==-1):#自分の２個となりcH
                        CH_num[i]=grade2
                        size[grade2]+=1
                        break
                    if(grade2==max_grade[max_grade[grade2]]): #grade2と同じ値のCHの時#2ホップ先と3ホップ先の状態量が同じ場合の処理
                        if(grade2>max_grade[grade2]):#ノード番号が大きい方をクラスタヘッドに
                            CH_num[i]=grade2
                            size[grade2]+=1
                            break
                        if(max_grade[grade2]>grade2):
                            CH_num[i]=max_grade[grade2]
                            size[max_grade[grade2]]+=1
                            break

                    grade1=grade2#どのif分にも引っかからない場合は，grade1をgrade2変換→jで回すことによりNホップ先まで判定可能に．

            #----------------------初期状態におけるクラスタリングまで終了---------------------------

            #-------------------------------初期状態における測定-------------------------------

            print('---------------initial state-------------')
            #クラスタ数をカウント
            for i in range(N):
                if(CH_num[i]==i):
                    CH_counter+=1
            #print('CH_counter',CH_counter)

            #---------------------シミュレーション開始-----------------------------------------

            time=TIME#シミュレーション時間、上で定義
            for k in range(time):
                time_list.append(k)
                LONG=0.07#TIME後に通信可能距離が二倍になる
                #初期化、リンクと次数はリンクを作成する直前に初期化している
                for i in range(N):
                    diffusion[i]=0
                    dd[i]=0
                    CH_num[i]=0
                    CH_candidate_count[i] = 0
                    size[i]=0
                    max_grade[i]=-1
                    gap[i]=0
                    gapx[i]=0
                    gapy[i]=0
                    tangent[i]=0
                    theta[i]=0
                    radians[i]=0
                    next_x[i]=0
                    next_y[i]=0
                CH_counter=0
                not_pattern=0
                connectivity=0
                CHswitch=0
                generate=0
                vanish=0
                Csize=[]


                #----------------------------------ノード移動-------------------------------
                '''
                #ランダムウォークモデル，CHの初期位置に注意！
                v_min=0.002#研究ノートp.30表面参照
                v_max=0.014
                for i in range(N):
                    #移動角度の決定
                    np.random.seed(i*i*3+k*k*6+sd*sd+9)#各ノードの方向が一致しないよう，タネを複雑に．
                    #theta[i]=random.uniform(0,360)
                    radians[i]=2*pi*np.random.random()
                    #移動距離の決定
                    gap[i]=np.random.uniform(v_min,v_max)
                    #通信可能距離に対応させて移動距離を操作
                    if(LONG != 0.07):
                        gap[i] = gap[i] + (k * (gap[i] / TIME))
                    #次の目的地を決定
                    next_x[i]=x[i]+gap[i]*math.cos(radians[i])
                    next_y[i]=y[i]+gap[i]*math.sin(radians[i])
                    #print(gap[i]*math.cos(theta[i]))
                    #print(gap[i]*math.sin(theta[i]))
                    #境界での跳ね返りを考慮してx座標を更新
                    if(next_x[i]<0):
                        x[i]=-next_x[i]
                    elif(1<next_x[i]):
                        x[i]=1-(next_x[i]-1)
                    elif(0<=next_x[i]<=1):
                        x[i]=next_x[i]
                    #境界での跳ね返りを考慮してy座標を更新
                    if(next_y[i]<0):
                        y[i]=-next_y[i]
                    elif(1<next_y[i]):
                        y[i]=1-(next_y[i]-1)
                    elif(0<=next_y[i]<=1):
                        y[i]=next_y[i]
                '''

                #----------------------------------リンク張り替え,次数再計算-------------------------

                for i in range(N):
                    degree[i]=0#次数初期化
                    for j in range(N):
                        link[i][j]=0#リンク初期化
                        dis=(x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])
                        #print(sqrt(dis))
                        if(sqrt(dis)<LONG and i!=j):#unit disk graph
                            link[i][j]=1
                            degree[i]+=1
                        '''
                        else :#周期境界条件
                            if (not(x[i]>long and x[j]>long) and (x[i]>long or x[j]>long)):#どちらか片方が右端に存在するとき
                                dis=(1-fabs(x[i]-x[j]))*(1-fabs(x[i]-x[j]))+(y[i]-y[j])*(y[i]-y[j])#fabsは絶対値を少数まで扱いながら表現する．
                                if(sqrt(dis)<LONG and i!=j):
                                    link[i][j]=1
                                    degree[i]+=1
                                if (not(y[i]>long and y[j]>long) and (y[i]>long or y[j]>long)):#さらに，どちらか片方が上端に存在するとき
                                    dis=(1-fabs(x[i]-x[j]))*(1-fabs(x[i]-x[j]))+(1-fabs(y[i]-y[j]))*(1-fabs(y[i]-y[j]))
                                    if(sqrt(dis)<LONG and i!=j):
                                        link[i][j]=1
                                        degree[i]+=1
                            if (not(y[i]>long and y[j]>long) and (y[i]>long or y[j]>long)):#どちらか片方が上端に存在するとき
                                dis=(x[i]-x[j])*(x[i]-x[j])+(1-fabs(y[i]-y[j]))*(1-fabs(y[i]-y[j]))
                                if(sqrt(dis)<LONG and i!=j):
                                    link[i][j]=1
                                    degree[i]+=1
                        '''
                #状態量の更新
                for h in range(1):
                    #拡散高速化処理
                    #拡散項
                    for i in range(N):
                        diffusion[i]=0
                        dd[i]=0
                        dd_discharge[i]=0
                        dd_discharge_count[i]=0
                        zero_frag[i]=0
                        for j in range(N):
                            diffusion_individual[i][j]=0
                    for i in range(N):
                        for j in range(N):
                            if(link[i][j]==1 and q[i]>q[j]):
                                diffusion_individual[i][j]=diffusion1(i,j,q)
                                diffusion_individual[j][i]=-1*diffusion1(i,j,q)
                                dd_discharge[i]+=diffusion1(i,j,q)
                                dd_discharge_count[i]+=1


                    #指定ノードも同じ振る舞い
                    for i in range(N):
                        if(q[i]-dd_discharge[i]<0):
                            zero_frag[i]=1
                            for j in range(N):
                                if(link[i][j]==1 and q[i]>q[j]):
                                    #print('check',i,sum(dd_discharge[i]))
                                    #diffusion_individual[i][j]=q[i]/dd_discharge_count[i]
                                    diffusion_individual[j][i]=-q[i]*(diffusion_individual[i][j]/dd_discharge[i])
                                    #print('check1',diffusion_individual[i][j])
                                    diffusion_individual[i][j]=0
                                    #print('check2',diffusion_individual[j][i])


                    #print('after',diffusion_individual)
                    for i in range(N):
                        dd[i]=sum(diffusion_individual[i])

                    #CHの自律生成処理
                    for i in range(N):
                        np.random.seed(i*i*i*7+k*7+sd^4)#一応タネは複雑に．
                        rate = np.random.random()
                        if(CH_flag[i] == 0 and rate < CH_rate):
                            CH_flag[i] = 1
                            generate += 1

                    #CHの消滅処理
                    for i in range(N):
                        np.random.seed(i*i*7+k*k*11+sd^4)#一応タネは複雑に．
                        rate2 = np.random.random()
                        if(CH_flag[i] == 1 and rate2 < CH_time_rate):
                            CH_flag[i] = 0
                            vanish += 1

                    #next_qの計算・分布値の更新
                    for i in range(N):
                        if(CH_flag[i] == 1):
                            next_q[i] = CH_q
                            difference_q[i]=next_q[i]-q[i]
                            q[i]=next_q[i]
                            #print("generate!time=",k)
                        else :
                            if(zero_frag[i]==0):
                                next_q[i]=(q[i]-dd[i])*(1-q_dec)
                                difference_q[i]=next_q[i]-q[i]
                                q[i]=next_q[i]
                            if(zero_frag[i]==1):
                                next_q[i]=(0-dd[i])*(1-q_dec)
                                difference_q[i]=next_q[i]-q[i]
                                q[i]=next_q[i]


                #--------------------クラスタ判定（CH候補は全てCHにしている）--------------------------------------------

                for i in range(N):
                    MAX = 0.0
                    if CH_flag[i] == 0:  # CH候補ノード以外の処理。CH候補ノードはmax_grade=-1のままで良い→CHとなる
                        for j in range(N):
                            if(link[i][j] == 1):
                                if(q[j]-q[i] >= MAX):
                                    MAX = q[j]-q[i]
                                    max_grade[i] = j
                                    if CH_flag[j] == 1:
                                        CH_candidate_count[i] += 1
                
                #複数の上流が周りに存在する場合、前回のCHとリンクが存在していたら、max_gradeを前回のCHとみなす。
                for i in range(N):
                    if CH_candidate_count[i] > 1:
                        if link[i][CH_num_prev[i]] == 1:
                            max_grade[i] = CH_num_prev[i]


                #クラスタサイズ判定
                for i in range(N):
                    grade1=0
                    for j in range(50):
                        if(j==0):
                            grade1=max_grade[i]
                            if(grade1==-1):
                                CH_num[i]=i
                                CH_num_prev[i] = i
                                size[i]+=1
                                break
                        grade2=max_grade[grade1]
                        if(grade2==-1):
                            CH_num[i]=grade1
                            CH_num_prev[i] = grade1
                            size[grade1]+=1
                            break
                        if(max_grade[grade2]==-1):
                            CH_num[i]=grade2
                            CH_num_prev[i] = grade2
                            size[grade2]+=1
                            break
                        # if(grade2==max_grade[max_grade[grade2]]):
                        #     if(grade2>max_grade[grade2]):
                        #         CH_num[i]=grade2
                        #         size[grade2]+=1
                        #         break
                        #     if(max_grade[grade2]>grade2):
                        #         CH_num[i]=max_grade[grade2]
                        #         size[max_grade[grade2]]+=1
                        #         break

                        grade1=grade2

                #------------------------クラスタ判定終了---------------------------------------

                #------------------------シミュレーション中のステータス測定----------------------

                #時間毎のCH数をカウント
                for i in range(N):
                    if(CH_num[i]==i):
                        CH_counter+=1
                CH_timecount.append(CH_counter)

                #指定ノードがCHかどうか判断
                for i in range(N):
                    if(CH_flag[i] == 1):
                        #if(CH_num[i]==i):
                            CHswitch+=1
                CHswitch_timecount.append(CHswitch)
                #指定ノードの生成・消滅回数を追加
                generate_timecount.append(generate)
                vanish_timecount.append(vanish)

                '''
                #指定ノード同士にリンクが存在しているかどうか。データ補正したい場合はコメントアウトを外す。川崎方式のプログラムとアルゴリズムを変更（研究ノートp.37参照）。
                for i in range(N):
                    if(CH_flag[i] == 1 and CH_num[i] == i):
                        for j in range(N):
                            if(i>j):
                                if(CH_flag[j] == 1 and CH_num[j] == i):
                                    if(link[i][j]==1):
                                        print('time=',k,'i=',i,'j=',j,'these are connected')
                                        CHswitch+=1#指定ノード同士にリンクがある場合は例外処理'''
                #CHswitch_timecount.append(CHswitch)

                '''
                #時間毎の不適パターン数をカウント
                hop_count=[0 for i in range(N)]
                hop_frag_0=[0 for i in range(N)]
                for i in range(N):
                    if(CH_num[i]==i):
                        hop_frag_0[i]=1

                hop=30#目的ノードまでの十分なホップ数
                for m in range(hop):#あるクラスタ内に存在するノードに対して，CHからのホップ数を全て出力
                    for i in range(N):
                        if(hop_frag_0[i]==1):
                            for j in range(N):
                                if(link[i][j]==1 and i!=j and hop_frag_0[j]==0 and CH_num[i]==CH_num[j]):
                                    hop_frag_0[i]=2
                                    hop_frag_0[j]=3
                                    #print('node.No=',j,'hop_count=',k+1)
                                    hop_count[j]=m+1
                    for l in range(N):
                        if(hop_frag_0[l]==3):
                            hop_frag_0[l]=1

                not_pattern=0
                #print('difference>=2')
                for i in range(N):
                    for j in range(N):
                        if(link[i][j]==1):
                            if(CH_num[i]!=CH_num[j] and abs(hop_count[i]-hop_count[j])>=2):
                                #print('node:',i,',CH_num:',CH_num[i],'hop_count',hop_count[i],'and node:',j,'CH_num:',CH_num[j],'hop_count',hop_count[j],'difference=',abs(hop_count[i]-hop_count[j]))
                                not_pattern+=1
                not_pattern_timecount.append(not_pattern/2)'''

      #---------------------------クラスタ間辺連結性の算出------------------------
                '''
                def cluster_edge_connectivity(ch):#クラスタ間のリンク数をリストに追加
                    cluster_edge_number=0
                    for i in range(N):
                        if(CH_num[i]==ch):
                            for j in range(N):
                                if(CH_num[j]!=CH_num[i] and link[i][j]==1):
                                    cluster_edge_number+=1
                    return cluster_edge_number

                cluster_edge_list=[]
                for m in range(N):
                    if(CH_num[m]==m):#CHの場合、関数を起動
                        ch=m
                        edge_connectivity=cluster_edge_connectivity(ch)#returnの結果
                        #print('cluster number is', str(ch),edge_connectivity)
                        cluster_edge_list.append(edge_connectivity)#全てのクラスタの次数のリスト

                #print(cluster_edge_list)
                connectivity=min(cluster_edge_list)#次数リストの最小値→クラスタ間の辺連結性
                connectivity_timecount.append(connectivity)
                #print(connectivity)'''

                '''
                #対象時間の様子をプロット
                if(k!=0 and k%10==0):
                    xmin=0
                    xmax=N-1
                    ymin=0
                    ymax=5

                    #分布値のプロット
                    for i in range(N):
                        plt.plot(i,q[i],color='red',marker='.')
                    plt.xlim(xmin,xmax)
                    plt.ylim(ymin,ymax)
                    plt.xlabel('node number')
                    plt.ylabel('distribution value')
                    plt.savefig('/Users/kawasakirio/Desktop/M1result/0916/'+'zisuu'+'dec='+str(q_dec)+'t='+str(k)+'sigma='+str(sigma)+'.png')#語尾に'.png'が必要
                    plt.cla()

                    #クラスタリングをプロット
                    for i in range(N):#
                        if(CH_num[i]!=i):#CH以外
                            plt.plot(x[i],y[i],color=color_list[CH_num[i]],marker='o')
                    for i in range(N):#上と統合すると、プロットが被る
                        if(CH_num[i]==i):#CH
                            plt.plot(x[i],y[i],color=color_list[CH_num[i]],markeredgecolor='black',marker='*',markersize=15)
                    plt.xlim(0,1)
                    plt.ylim(0,1)
                    plt.xlabel('x-coordinate')
                    plt.ylabel('y-coordinate')
                    plt.savefig('/Users/kawasakirio/Desktop/M1result/0916/'+'zisuu'+'dec='+str(q_dec)+'t='+str(k)+'sigma='+str(sigma)+'.pdf')#語尾に'.png'が必要
                    plt.cla()

                    #各クラスタサイズをカウント・さらに統計量を計算
                    Csize=[]
                    print('-----size-----')
                    for i in range(N):
                        if(CH_num[i]==i):
                            #print(size[i])
                            Csize.append(size[i])
                    mea=sta.mean(Csize)
                    var=sta.variance(Csize)
                    std=sta.stdev(Csize)
                    cv=std/mea#変動係数
                    print('time=',k)
                    print('mean',mea)
                    print('stdev',std)
                    print('cv',cv)
                '''

                difference_q_list.append(sum(difference_q))
                #print(previous_cv)
            #-------------------------シミュレーション終了------------------------------------
            #-------------------------最終的なステータス測定-----------------------------------

            print('-------------final state--------------')
            # print('q',q)

            #------------------------------Hi-AODV------------------------------------------
            aodv_exp_counts = 10#実験回数
            num_packet_sum = 0
            num_tra_packet_sum = 0
            num_rec_packet_sum = 0
            battery_consumption_tra_sum = 0
            battery_consumption_rec_sum = 0
            battery_consumption_sum = 0

            for ii in range(aodv_exp_counts):
                #送信ノードからのホップ数を計算
                num_packet = [0 for i in range(N)]#各ノードが宛先だった場合のパケット数をそれぞれカウント
                num_tra_packet = [0 for i in range(N)]
                num_rec_packet = [0 for i in range(N)]
                battery_consumption_tra = [0 for i in range(N)]
                battery_consumption_rec = [0 for i in range(N)]
                battery_consumption = [0 for i in range(N)]
                #2と着くのはクラスタ間通信で使用
                num_packet2 = [0 for i in range(N)]#各ノードが宛先だった場合のパケット数をそれぞれカウント
                num_tra_packet2 = [0 for i in range(N)]
                num_rec_packet2 = [0 for i in range(N)]
                battery_consumption_tra2 = [0 for i in range(N)]
                battery_consumption_rec2 = [0 for i in range(N)]
                battery_consumption2 = [0 for i in range(N)]
                hop_count = [0 for i in range(N)]#CHからのホップ数
                source_node = [0 for i in range(N)]
                destination_node = [0 for i in range(N)]
                random.seed(ii+3)
                seed_s = random.randrange(N)
                print('S', seed_s)
                source_node[seed_s] = 1

                random.seed((ii+7)*(ii+11))  # タネが重複しないように複雑に
                seed_d = random.randrange(N)
                print("D", seed_d)
                destination_node[seed_d] = 1

                #AODVプログラムの宛先ノードをCH以外に見立てる→宛先ノードを決定したら，CHからのパケット数などを計算
                for l in range(N):
                    if CH_num[l] != l:
                        hop_frag_d = [0 for i in range(N)]
                        hop_frag_d[l] = 1
                        start_mark = [0 for i in range(N)]
                        hop_frag_s = [0 for i in range(N)]
                        aodv_hop_count = [0 for i in range(N)]
                        #AODVプログラムの送信元ノードをCHに見立てる→このCHは宛先ノードに対するCH
                        for i in range(N):
                            if CH_num[i] == i and CH_num[i] == CH_num[l]:
                                hop_frag_s[i] = 1
                                start_mark[i] = 1
                        hop = 100  # 宛先ノードまでの十分なホップ数
                        for k in range(hop):
                            for i in range(N):
                                if hop_frag_s[i] == 1 and hop_frag_d[i] == 0 and CH_num[l]==CH_num[i]:
                                    for j in range(N):
                                        # 同じクラスタ内の宛先ノードにパケット送信
                                        if hop_frag_d[j] == 1 and link[i][j] == 1 and i != j and hop_frag_s[j] == 0 and CH_num[i] == CH_num[j]:
                                            hop_frag_s[i] = 2
                                            hop_frag_s[j] = 2  # パケットを止める
                                            aodv_hop_count[j] = k+1  # ホップ数をカウント→一応．パケット量としては使わない
                                        # クラスタ外にパケットが飛んで行った時→上記の宛先ノードのようにパケットを止める
                                        if link[i][j] == 1 and i != j and hop_frag_s[j] == 0 and CH_num[i] != CH_num[j]:
                                            hop_frag_s[i] = 2
                                            hop_frag_s[j] = 2  # パケットを止める
                                            # ホップ数をカウント→一応．パケット量としては使わない
                                            aodv_hop_count[j] = k+1
                                        #パケット未送信のノードにパケット送信
                                        elif link[i][j] == 1 and i != j and hop_frag_s[j] == 0 and CH_num[i] == CH_num[j]:
                                            hop_frag_s[i] = 2
                                            hop_frag_s[j] = 3
                                            aodv_hop_count[j] = k+1  # ホップ数をカウント→一応．パケット量としては使わない
                                            hop_count[j] = k+1
                                        
                            for i in range(N):
                                if hop_frag_s[i] == 3:
                                    hop_frag_s[i] = 1
                        #宛先ノードが決まっている状態でCHBTの構築にかかるパケット数をカウント。例えばnum_tra_packet[l]には宛先ノードがlの時のパケット数が入っている．
                        for i in range(N):
                            #RREQ送信数
                            # 送信ノードをカウントしない代わりに受信ノード分をカウント。実際は逆。
                            if aodv_hop_count[i] != 0 and CH_num[i] == CH_num[l]:#違うクラスタのノードはパケットを破棄
                                num_tra_packet[l] += 1
                            #RREQ受信数（クラスタ内）
                            if aodv_hop_count[i] != 0 or start_mark[i] == 1:
                                if CH_num[i] == CH_num[l]:
                                    num_rec_packet[l] += degree[i]
                                    for j in range(N):
                                        if link[i][j] == 1 and hop_frag_d[j] == 1:  # 中継ノードは宛先ノードから受信しないので引き算
                                            num_rec_packet[l] -= 1
                            # 宛先ノードとパケットを受け取らなかったノード間のリンク数だけ引き算
                            if aodv_hop_count[i] == 0 and CH_num[i] == CH_num[l]:
                                for j in range(N):
                                    if link[i][j] == 1 and hop_frag_d[j] == 1:
                                        num_rec_packet[l] -= 1
                            #RREQ受信数（クラスタ間）
                            if aodv_hop_count[i] != 0 and CH_num[i] != CH_num[l]:
                                for j in range(N):
                                    if link[i][j] == 1 and CH_num[i] == CH_num[l]:#クラスタ外のノードはクラスタlのGNからパケットを受け取る
                                        num_rec_packet[l] += 1
                            #RREP送信数
                            if hop_frag_d[i] == 1:
                                num_tra_packet[l] += aodv_hop_count[i]
                                #RREP受信数
                                for k in range(aodv_hop_count[i]):
                                    for j in range(N):
                                        if link[i][j] == 1 and aodv_hop_count[i] - 1 == aodv_hop_count[j]:
                                            num_rec_packet[l] += degree[i]
                                            i = j
                                            break
                    
                    #消費電力
                    battery_consumption_tra[l] = num_tra_packet[l] * 512 * (3.3 * (10 ** (-7)))
                    battery_consumption_rec[l] = num_rec_packet[l] * 512 * (1.9 * (10 ** (-7)))
                    battery_consumption[l] = battery_consumption_rec[l] + battery_consumption_tra[l]

                # print('テスト送信パケット数', num_tra_packet)
                # print('テスト受信パケット数', num_rec_packet)
                # print('テスト送信電力数', battery_consumption_tra)
                # print('テスト送信電力数', battery_consumption_tra)
                # print('テスト電力数', battery_consumption_tra)
                #各クラスタ毎にCHBTの作成に必要なパケット数と消費電力量の平均を測定
                num_tra_packet_cluster = [0 for i in range(N)]
                num_rec_packet_cluster = [0 for i in range(N)]
                battery_consumption_tra_cluster = [0 for i in range(N)]
                battery_consumption_rec_cluster = [0 for i in range(N)]
                battery_consumption_cluster = [0 for i in range(N)]
                for i in range(N):
                    if CH_num[i] == i:
                        for j in range(N):
                            if CH_num[i] == CH_num[j]:
                                num_tra_packet_cluster[i] += num_tra_packet[j]
                                num_rec_packet_cluster[i] += num_rec_packet[j]
                                battery_consumption_tra_cluster[i] += battery_consumption_tra[j]
                                battery_consumption_rec_cluster[i] += battery_consumption_rec[j]
                                battery_consumption_cluster[i] += battery_consumption[j]
                for i in range(N):
                    if CH_num[i] == i:
                        num_tra_packet_cluster[i] = num_tra_packet_cluster[i] / size[i]
                        num_rec_packet_cluster[i] = num_rec_packet_cluster[i] / size[i]
                        battery_consumption_tra_cluster[i] = battery_consumption_tra_cluster[i] / size[i]
                        battery_consumption_rec_cluster[i] = battery_consumption_rec_cluster[i] / size[i]
                        battery_consumption_cluster[i] = battery_consumption_cluster[i] / size[i]

                #各クラスタ毎にCHとGNの通信に必要なパケット数と消費電力量の平均を測定
                GN_frag = [0 for i in range(N)]
                for i in range(N):
                    for j in range(N):
                        if link[i][j] == 1 and CH_num[i]!=CH_num[j]:
                            GN_frag[i] = 1

                for l in range(N):
                    if GN_frag[l] == 1:
                        if CH_num[l] != l:
                            hop_frag_d = [0 for i in range(N)]
                            hop_frag_d[l] = 1
                            start_mark = [0 for i in range(N)]
                            hop_frag_s = [0 for i in range(N)]
                            aodv_hop_count = [0 for i in range(N)]
                            #AODVプログラムの送信元ノードをCHに見立てる→このCHは宛先ノードに対するCH
                            for i in range(N):
                                if CH_num[i] == i and CH_num[i] == CH_num[l]:
                                    hop_frag_s[i] = 1
                                    start_mark[i] = 1
                            hop = 100  # 宛先ノードまでの十分なホップ数
                            for k in range(hop):
                                for i in range(N):
                                    if hop_frag_s[i] == 1 and hop_frag_d[i] == 0 and CH_num[l] == CH_num[i]:
                                        for j in range(N):
                                            # 同じクラスタ内の宛先ノードにパケット送信
                                            if hop_frag_d[j] == 1 and link[i][j] == 1 and i != j and hop_frag_s[j] == 0 and CH_num[i] == CH_num[j]:
                                                hop_frag_s[i] = 2
                                                hop_frag_s[j] = 2  # パケットを止める
                                                # ホップ数をカウント→一応．パケット量としては使わない
                                                aodv_hop_count[j] = k+1
                                            # クラスタ外にパケットが飛んで行った時→上記の宛先ノードのようにパケットを止める
                                            if link[i][j] == 1 and i != j and hop_frag_s[j] == 0 and CH_num[i] != CH_num[j]:
                                                hop_frag_s[i] = 2
                                                hop_frag_s[j] = 2  # パケットを止める
                                                # ホップ数をカウント→一応．パケット量としては使わない
                                                aodv_hop_count[j] = k+1
                                            #パケット未送信のノードにパケット送信
                                            elif link[i][j] == 1 and i != j and hop_frag_s[j] == 0 and CH_num[i] == CH_num[j]:
                                                hop_frag_s[i] = 2
                                                hop_frag_s[j] = 3
                                                # ホップ数をカウント→一応．パケット量としては使わない
                                                aodv_hop_count[j] = k+1
                                                hop_count[j] = k+1

                                for i in range(N):
                                    if hop_frag_s[i] == 3:
                                        hop_frag_s[i] = 1
                            #宛先ノード（GN）が決まっている状態でCHとの通信にかかるパケット数をカウント。例えばnum_tra_packet[l]には宛先ノードがlの時のパケット数が入っている．
                            for i in range(N):
                                #RREP送信数
                                if hop_frag_d[i] == 1:
                                    num_tra_packet2[l] += aodv_hop_count[i]
                                    #RREP受信数
                                    for k in range(aodv_hop_count[i]):
                                        for j in range(N):
                                            if link[i][j] == 1 and aodv_hop_count[i] - 1 == aodv_hop_count[j]:
                                                num_rec_packet2[l] += degree[i]
                                                i = j
                                                break
                                

                    #消費電力
                    battery_consumption_tra2[l] = num_tra_packet2[l] * 512 * (3.3 * (10 ** (-7)))
                    battery_consumption_rec2[l] = num_rec_packet2[l] * 512 * (1.9 * (10 ** (-7)))
                    battery_consumption2[l] = battery_consumption_rec2[l] + battery_consumption_tra2[l]

                #各クラスタ毎にCHとGNの通信に必要なパケット数と消費電力量の平均を測定
                num_tra_packet_cluster2 = [0 for i in range(N)]
                num_rec_packet_cluster2 = [0 for i in range(N)]
                battery_consumption_tra_cluster2 = [0 for i in range(N)]
                battery_consumption_rec_cluster2 = [0 for i in range(N)]
                battery_consumption_cluster2 = [0 for i in range(N)]
                GN_counter = [0 for i in range(N)]

                for i in range(N):
                    if CH_num[i] == i:
                        for j in range(N):
                            if CH_num[i] == CH_num[j] and num_tra_packet2[j] != 0:
                                GN_counter[i] += 1
                                num_tra_packet_cluster2[i] += num_tra_packet2[j]
                                num_rec_packet_cluster2[i] += num_rec_packet2[j]
                                battery_consumption_tra_cluster2[i] += battery_consumption_tra2[j]
                                battery_consumption_rec_cluster2[i] += battery_consumption_rec2[j]
                                battery_consumption_cluster2[i] += battery_consumption2[j]

                for i in range(N):
                    if CH_num[i] == i and GN_counter[i] != 0:
                        num_tra_packet_cluster2[i] = 2 * num_tra_packet_cluster2[i] / GN_counter[i]
                        num_rec_packet_cluster2[i] = 2 * num_rec_packet_cluster2[i] / GN_counter[i]
                        battery_consumption_tra_cluster2[i] = 2 * battery_consumption_tra_cluster2[i] / GN_counter[i]
                        battery_consumption_rec_cluster2[i] = 2 * battery_consumption_rec_cluster2[i] / GN_counter[i]
                        battery_consumption_cluster2[i] = 2 * battery_consumption_cluster2[i] / GN_counter[i]

                #最終的な結果を算出
                for s in range(N):
                    if source_node[s] == 1:
                        for d in range(N):
                            if destination_node[d] == 1:
                                #num_tra_packet_clusterなどをaodv_exp_counts（実験回数）で割っているのは，CHBTは一回構築すれば良いため
                                #iとjが違うクラスタの場合
                                if CH_num[s] != CH_num[d]:
                                    for i in range(N):
                                        num_tra_packet_sum += num_tra_packet_cluster[i] / aodv_exp_counts + num_tra_packet_cluster2[i]
                                        num_rec_packet_sum += num_rec_packet_cluster[i] / aodv_exp_counts + num_rec_packet_cluster2[i]
                                        battery_consumption_tra_sum += battery_consumption_tra_cluster[i] / aodv_exp_counts + battery_consumption_tra_cluster2[i]
                                        battery_consumption_rec_sum += battery_consumption_rec_cluster[i] / aodv_exp_counts + battery_consumption_rec_cluster2[i]
                                        battery_consumption_sum += battery_consumption_cluster[i] / aodv_exp_counts + battery_consumption_cluster2[i]
                                #iとjが同じクラスタの場合
                                elif CH_num[s] == CH_num[d]:
                                    for i in range(N):
                                        if CH_num[i] == CH_num[s]:
                                            num_tra_packet_sum += num_tra_packet_cluster[i] / aodv_exp_counts + num_tra_packet_cluster2[i]
                                            num_rec_packet_sum += num_rec_packet_cluster[i] / aodv_exp_counts + num_rec_packet_cluster2[i]
                                            battery_consumption_tra_sum += battery_consumption_tra_cluster[i] / aodv_exp_counts + battery_consumption_tra_cluster2[i]
                                            battery_consumption_rec_sum += battery_consumption_rec_cluster[i] / aodv_exp_counts + battery_consumption_rec_cluster2[i]
                                            battery_consumption_sum += battery_consumption_cluster[i] / aodv_exp_counts + battery_consumption_cluster2[i]

            #実験回数で割る
            def DivisionAodvExp(var):
                var = var / aodv_exp_counts
                return var

            num_tra_packet_sum = DivisionAodvExp(num_tra_packet_sum)
            battery_consumption_tra_sum = DivisionAodvExp(battery_consumption_tra_sum)
            num_rec_packet_sum = DivisionAodvExp(num_rec_packet_sum)
            battery_consumption_rec_sum = DivisionAodvExp(battery_consumption_rec_sum)
            num_packet_sum = DivisionAodvExp(num_packet_sum)
            battery_consumption_sum = DivisionAodvExp(battery_consumption_sum)

            print("送信パケット数", num_tra_packet_sum)
            print("送信消費電力量", battery_consumption_tra_sum, 'J')
            print("受信パケット数", num_rec_packet_sum)
            print("送信消費電力量", battery_consumption_rec_sum, 'J')
            print("総パケット数", num_packet_sum)
            print('総消費電力量', battery_consumption_sum, 'J')

            #拡散係数毎の測定結果リストをリストのリストに追加していく
            CH_timecount_list_of_list.append(CH_timecount)
            '''
            not_pattern_timecount_list_of_list.append(not_pattern_timecount)
            connectivity_timecount_list_of_list.append(connectivity_timecount)'''
            CHswitch_timecount_list_of_list.append(CHswitch_timecount)
            generate_timecount_list_of_list.append(generate_timecount)
            vanish_timecount_list_of_list.append(vanish_timecount)

            if(z==z_num-1):
                #for文を併用してリスト内のリスト毎の要素同士を足し算
                for i in range(z_num):
                    CH_timecount_list_of_sdsumlist[i]=[k + l for (k,l) in zip(CH_timecount_list_of_sdsumlist[i],CH_timecount_list_of_list[i])]#2つのリストの要素同士を足し合わせる
                    '''
                    not_pattern_timecount_list_of_sdsumlist[i]=[k + l for (k,l) in zip(not_pattern_timecount_list_of_sdsumlist[i],not_pattern_timecount_list_of_list[i])]#2つのリストの要素同士を足し合わせる
                    connectivity_timecount_list_of_sdsumlist[i]=[k + l for (k,l) in zip(connectivity_timecount_list_of_sdsumlist[i],connectivity_timecount_list_of_list[i])]#2つのリストの要素同士を足し合わせる'''
                    CHswitch_timecount_list_of_sdsumlist[i]=[k + l for (k,l) in zip(CHswitch_timecount_list_of_sdsumlist[i], CHswitch_timecount_list_of_list[i])]#2つのリストの要素同士を足し合わせる
                    generate_timecount_list_of_sdsumlist[i]=[k + l for (k,l) in zip(generate_timecount_list_of_sdsumlist[i], generate_timecount_list_of_list[i])]#2つのリストの要素同士を足し合わせる
                    vanish_timecount_list_of_sdsumlist[i]=[k + l for (k,l) in zip(vanish_timecount_list_of_sdsumlist[i], vanish_timecount_list_of_list[i])]#2つのリストの要素同士を足し合わせる
                print('goukei',CH_timecount_list_of_sdsumlist)

            if(z==z_num-1 and zz==zz_num_dammy-1):#最後まで回したらプロット作業をする
                #NW数で各要素の数値を平均するためにarray型に変更．dtype=floatとすることで要素をfloat型に
                CH_timecount_list_of_sdsumlist=np.array(CH_timecount_list_of_sdsumlist,dtype=float)
                '''
                not_pattern_timecount_list_of_sdsumlist=np.array(not_pattern_timecount_list_of_sdsumlist,dtype=float)
                connectivity_timecount_list_of_sdsumlist=np.array(connectivity_timecount_list_of_sdsumlist,dtype=float)'''
                CHswitch_timecount_list_of_sdsumlist=np.array(CHswitch_timecount_list_of_sdsumlist,dtype=float)
                generate_timecount_list_of_sdsumlist=np.array(generate_timecount_list_of_sdsumlist,dtype=float)
                vanish_timecount_list_of_sdsumlist=np.array(vanish_timecount_list_of_sdsumlist,dtype=float)
                for i in range(z_num):
                    CH_timecount_list_of_sdsumlist[i]=CH_timecount_list_of_sdsumlist[i]/zz_num
                    '''
                    not_pattern_timecount_list_of_sdsumlist[i]=not_pattern_timecount_list_of_sdsumlist[i]/zz_num
                    connectivity_timecount_list_of_sdsumlist[i]=connectivity_timecount_list_of_sdsumlist[i]/zz_num'''
                    CHswitch_timecount_list_of_sdsumlist[i]=CHswitch_timecount_list_of_sdsumlist[i]/zz_num
                    generate_timecount_list_of_sdsumlist[i]=generate_timecount_list_of_sdsumlist[i]/zz_num
                    vanish_timecount_list_of_sdsumlist[i]=vanish_timecount_list_of_sdsumlist[i]/zz_num

                #list_of_sdsumlistを棒グラフとしてプロットする
                rdec_str_list=list(map(str,rdec_list))#rdecのリストの文字列版を生成
                for i in range(z_num):
                    CH_bar_list[i]=sum(CH_timecount_list_of_sdsumlist[i])/len(CH_timecount_list_of_sdsumlist[i])
                    '''
                    not_pattern_bar_list[i]=sum(not_pattern_timecount_list_of_sdsumlist[i])/len(not_pattern_timecount_list_of_sdsumlist[i])
                    connectivity_bar_list[i]=sum(connectivity_timecount_list_of_sdsumlist[i])/len(connectivity_timecount_list_of_sdsumlist[i])'''
                    generate_bar_list[i]=sum(generate_timecount_list_of_sdsumlist[i])#時間平均をする必要なし
                    vanish_bar_list[i]=sum(vanish_timecount_list_of_sdsumlist[i])#時間平均をする必要なし

                print('heikin',CH_timecount_list_of_sdsumlist)
                #ファイル作成
                now_time=datetime.datetime.now()
                os.makedirs('/Users/kawasakirio/Desktop/M2result/'+str(now_time))
                #CHの個数をプロット
                #折れ線グラフ
                for i in range(z_num):
                    plt.plot(time_list,CH_timecount_list_of_sdsumlist[i],color=color_list[i],label=str(rdec_list[i]))
                y_min=0
                y_max=max(np.ravel(CH_timecount_list_of_sdsumlist))#多重配列を１次元化したものの最大値
                plt.ylim(y_min, 70)
                plt.xlabel('Time',fontsize=20)
                plt.ylabel('Number of CH',fontsize=20)
                plt.legend(loc='upper left')
                plt.savefig('/Users/kawasakirio/Desktop/M2result/'+str(now_time)+'/'+'CH_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')#語尾に'.png'が必要
                plt.cla()
                #棒グラフ
                plt.bar(rdec_str_list,CH_bar_list,width=0.4,color='blue',edgecolor='black',align='center')
                print('number of ch=',CH_bar_list)
                plt.xlabel('r_dec')
                plt.ylabel('Number of CH')
                #plt.xlim(-0.5,1.5)#棒グラフの間隔を調整
                plt.savefig('/Users/kawasakirio/Desktop/M2result/'+str(now_time)+'/'+'bar_CH_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')
                plt.cla()

                '''
                #不適パターン数の個数をプロット
                #折れ線グラフ
                for i in range(z_num):
                    plt.plot(time_list,not_pattern_timecount_list_of_sdsumlist[i],color=color_list[i],label=str(rdec_list[i]))
                y_min=0
                y_max=max(np.ravel(not_pattern_timecount_list_of_sdsumlist))
                plt.ylim(y_min, y_max)
                plt.xlabel('Time',fontsize=20)
                plt.ylabel('Non-voronoi',fontsize=20)
                plt.legend(loc='upper left')
                plt.savefig('/Users/kawasakirio/Desktop/M1result/1205/'+'voronoi_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')#語尾に'.png'が必要
                plt.cla()
                #棒グラフ
                plt.bar(rdec_str_list,not_pattern_bar_list,width=0.4,color='blue',edgecolor='black',align='center')
                plt.xlabel('r_dec')
                plt.ylabel('Non-Voronoi pattern')
                #plt.xlim(-0.5,1.5)#棒グラフの間隔を調整
                plt.savefig('/Users/kawasakirio/Desktop/M1result/1205/'+'bar_voronoi_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')
                plt.cla()

                #クラスタ間連結性をプロット
                #折れ線グラフ
                for i in range(z_num):
                    plt.plot(time_list,connectivity_timecount_list_of_sdsumlist[i],color=color_list[i],label=str(rdec_list[i]))
                y_min=0
                y_max=max(np.ravel(connectivity_timecount_list_of_sdsumlist))
                plt.ylim(y_min, y_max)
                plt.xlabel('Time',fontsize=20)
                plt.ylabel('connectivity',fontsize=20)
                plt.legend(loc='upper left')
                plt.savefig('/Users/kawasakirio/Desktop/M1result/1205/'+'connectivity_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')#語尾に'.png'が必要
                plt.cla()
                #棒グラフ
                plt.bar(rdec_str_list,connectivity_bar_list,width=0.4,color='blue',edgecolor='black',align='center')
                plt.xlabel('r_dec')
                plt.ylabel('connectivity')
                #plt.xlim(-0.5,1.5)#棒グラフの間隔を調整
                plt.savefig('/Users/kawasakirio/Desktop/M1result/1205/'+'bar_connectivity'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')
                plt.cla()'''

                #指定ノードの個数をプロット
                #折れ線グラフのみ
                for i in range(z_num):
                    plt.plot(time_list,CHswitch_timecount_list_of_sdsumlist[i],color=color_list[i],label=str(rdec_list[i]))
                plt.ylim(0, 20)
                plt.xlabel('Time',fontsize=20)
                plt.ylabel('Number of specified nodes',fontsize=20)
                plt.legend(loc='upper left')
                plt.savefig('/Users/kawasakirio/Desktop/M2result/'+str(now_time)+'/'+'specified_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')#語尾に'.png'が必要
                plt.cla()

                #指定ノードの生成回数をプロット
                #折れ線グラフ
                for i in range(z_num):
                    plt.plot(time_list,generate_timecount_list_of_sdsumlist[i],color=color_list[i],label=str(rdec_list[i]))
                y_min=0
                y_max=max(np.ravel(generate_timecount_list_of_sdsumlist))#多重配列を１次元化したものの最大値
                #plt.ylim(y_min, 70)
                plt.xlabel('Time',fontsize=20)
                plt.ylabel('Number of generating',fontsize=20)
                plt.legend(loc='upper left')
                plt.savefig('/Users/kawasakirio/Desktop/M2result/'+str(now_time)+'/'+'generate_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')#語尾に'.png'が必要
                plt.cla()
                #棒グラフ
                plt.bar(rdec_str_list,generate_bar_list,width=0.4,color='blue',edgecolor='black',align='center')
                print('number of generate=',generate_bar_list)
                plt.xlabel('p')
                plt.ylabel('Number of generating')
                #plt.xlim(-0.5,1.5)#棒グラフの間隔を調整
                plt.savefig('/Users/kawasakirio/Desktop/M2result/'+str(now_time)+'/'+'bar_generate_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')
                plt.cla()

                #指定ノードの消滅回数をプロット
                #折れ線グラフ
                for i in range(z_num):
                    plt.plot(time_list,vanish_timecount_list_of_sdsumlist[i],color=color_list[i],label=str(rdec_list[i]))
                y_min=0
                y_max=max(np.ravel(vanish_timecount_list_of_sdsumlist))#多重配列を１次元化したものの最大値
                #plt.ylim(y_min, 70)
                plt.xlabel('Time',fontsize=20)
                plt.ylabel('Number of vanishing',fontsize=20)
                plt.legend(loc='upper left')
                plt.savefig('/Users/kawasakirio/Desktop/M2result/'+str(now_time)+'/'+'vanish_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')#語尾に'.png'が必要
                plt.cla()
                #棒グラフ
                plt.bar(rdec_str_list,vanish_bar_list,width=0.4,color='blue',edgecolor='black',align='center')
                print('number of vanish=',vanish_bar_list)
                plt.xlabel('p')
                plt.ylabel('Number of vanishing')
                #plt.xlim(-0.5,1.5)#棒グラフの間隔を調整
                plt.savefig('/Users/kawasakirio/Desktop/M2result/'+str(now_time)+'/'+'bar_vanish_count'+'dec='+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')
                plt.cla()


                #プロットした値の生データを保存
                file_name=str(now_time)+'sigma='+str(sigma)+'sd='+str(sd)+'TIME='+str(TIME)
                result.setup(file_name)
                for i in range(z_num):
                    result.dprint_csv_row(list(map(str,CH_timecount_list_of_sdsumlist[i])))
                result.dprint_csv_row(CH_bar_list)
                result.dprint_csv_row(q)#最後の実験結果の状態量も保存
                result.dprint_csv_row(generate_bar_list)
                result.dprint_csv_row(vanish_bar_list)
                for i in range(z_num):
                    result.dprint_csv_row(list(map(str,CHswitch_timecount_list_of_sdsumlist[i])))


            #---------------------------最終的なクラスタリングを可視化----------------------------
            
            # fig,ax=plt.subplots()
            # xmin=0
            # xmax=N-1
            # ymin=0
            # ymax=5
            # for i in range(N):
            #     if(CH_num[i]!=i):#CH以外
            #         plt.plot(x[i],y[i],color=color_list[CH_num[i]],marker='o')
            #         ax.annotate(str(hop_count_cluster[i]),(x[i],y[i]))#GNからのホップ数を出力

            # #GN可視化
            # for i in range(N):#所属クラスタが異なる隣接ノード
            #     for j in range(N):
            #         if(link[i][j]==1 and CH_num[i]!=CH_num[j]):
            #             plt.plot(x[i],y[i],color=color_list[CH_num[i]],marker='o',markeredgecolor='black')#GNを枠線で囲む
            #             ax.annotate(str(hop_count_cluster[i]),(x[i],y[i]))#GNをノード番号で出力

            # for i in range(N):#ノードやGNを最初にプロットしてから、星をプロット
            #     if(CH_num[i]==i):#CH
            #         plt.plot(x[i],y[i],color=color_list[CH_num[i]], markeredgecolor='black',marker='*',markersize=15)
            #         ax.annotate(str(hop_count_cluster[i]),(x[i],y[i]))#Sからのホップ数
            # for i in range(N):  # 上と統合すると、プロットが被る
            #     if source_node[i] == 1:  # CH
            #         plt.plot(x[i], y[i], markeredgecolor='black', marker='^', markersize=10, color=color_list[CH_num[i]])
            #         ax.annotate(str(hop_count_cluster[i]),(x[i],y[i]))#Sからのホップ数
                    
            #     if destination_node[i] == 1:
            #         plt.plot(x[i], y[i], markeredgecolor='black', marker='X', markersize=10, color=color_list[CH_num[i]])
            #         # Sからのホップ数
            #         ax.annotate(str(hop_count_cluster[i]), (x[i], y[i]))
                    

            # plt.xlim(0,1)
            # plt.ylim(0,1)
            # plt.xlabel('x-coordinate',fontsize=20)
            # plt.ylabel('y-coordinate',fontsize=20)
            # plt.savefig('/Users/kawasakirio/Desktop/M2result/1012/'+'dec='+str(q_dec)+'t='+str(time)+'sigma='+str(sigma)+'sd='+str(sd)+'.pdf')#語尾に'.pdf'が必要
            # plt.cla()
            

            '''
            #クラスタ毎のネットワークトポロジを可視化
            for k in range(N):
                if(CH_num[k]==k):#CHの場合、関数を起動
                    ch=k
                    G=nx.Graph()
                    for i in range(N):
                        if(CH_num[i]==ch):#chはクラスタ(CHノード)番号
                            G.add_node(i)
                            for j in range(N):
                                if(CH_num[i]==CH_num[j] and i>j and link[i][j]==1):
                                    G.add_edge(i,j)
                    nx.draw_networkx(G,node_size=100,font_size=5)
                    plt.savefig('/Users/kawasakirio/Desktop/M1result/0626/'+'CH'+str(ch)+'network'+'sd='+str(sd)+'.pdf')#語尾に'.pdf'が必要
                    plt.cla()
            '''
            #-------------------------------------------------------------------------------
