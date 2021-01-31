# -*- coding: UTF-8 -*-
#matplotlib inline
from pylab import *
import random
import numpy as np
np.set_printoptions(threshold=np.inf)#npによる大型行列を全て表示
from math import sqrt#平方根
from math import fabs#少数まで扱う絶対値
import math
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
import networkx as nx
import statistics as sta
start=datetime.datetime.now()
fig = plt.figure(figsize=(7,7))

#-----------------------------変数定義-------------------------------------------

N=500
n=N-4#指定ノード以外のノード数
LONG=0.07#通信可能距離
long=1-LONG#周期境界条件を満たす通信可能距離

sd=4 #乱数の種．ネットワークモデルなどを変更する
#x=np.random.seed()#random.seedは毎回同じ乱数を発生させるもの
x=np.random.seed(sd-1)
x=np.random.rand(n)#0から1の乱数をノード数だけ発生．
y=np.random.seed(sd-2)
y=np.random.rand(n)
x=list(x)#npリストを標準化
y=list(y)
#CH以外のノードの初期分布値
#q=np.random.seed(sd+1)#初期値を割り振ると、クラスタ形成が遅くなる。
#q=np.random.rand(n)
q=[0 for i in range(n)]
q=list(q)

#CHを特定の位置に設置
x.insert(0, 0.25)#(リストの位置，追加する数)
y.insert(0, 0.25)
x.insert(0, 0.75)
y.insert(0, 0.25)
x.insert(0, 0.25)
y.insert(0, 0.75)
x.insert(0, 0.75)
y.insert(0, 0.75)


#CHの分布値
CH_q=3
for i in range(N-n):
    q.insert(0, CH_q)
link=[[0 for i in range(N)]for j in range(N)]
degree=[0 for i in range(N)]
CH_deg=[0 for i in range(N)]
#CH=[0 for i in range(N)]
CH_counter=0#クラスタヘッド数．隣接ノードの状態量が等しい場合も，正しくカウントしている．
CH_num=[0 for i in range(N)]#自分が所属するクラスタヘッドのノード番号
size=[0 for i in range(N)]
Q=[0 for i in range(N)]
previous_cv=0#計算を打ち切るために使用

#----------------------分布値の更新式につかう変数と式--------------------------------

#拡散の強さ
sigma=0.0001#拡散の強さに関するパラメータ
q_dec=0.99#CH以外の分布値の減少量
next_q=[0 for i in range(N)]
difference_q=[0 for i in range(N)]#状態量の変化量
difference_q_list=[]
time_list=[]
diffusion=[0 for i in range(N)]#更新式に用いる拡散の値
dd=[0 for i in range(N)]

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

        # else :#周期境界条件
        #     if not(x[i]>long and x[j]>long) and (x[i]>long or x[j]>long):#どちらか片方が右端に存在するとき
        #         dis=(1-fabs(x[i]-x[j]))*(1-fabs(x[i]-x[j]))+(y[i]-y[j])*(y[i]-y[j])#fabsは絶対値を少数まで扱いながら表現する．
        #         if sqrt(dis)<LONG and i!=j:
        #             link[i][j]=1
        #         if not(y[i]>long and y[j]>long) and (y[i]>long or y[j]>long):#さらに，どちらか片方が上端に存在するとき
        #             dis=(1-fabs(x[i]-x[j]))*(1-fabs(x[i]-x[j]))+(1-fabs(y[i]-y[j]))*(1-fabs(y[i]-y[j]))
        #             if sqrt(dis)<LONG and i!=j:
        #                 link[i][j]=1
        #     if not(y[i]>long and y[j]>long) and (y[i]>long or y[j]>long):#どちらか片方が上端に存在するとき
        #         dis=(x[i]-x[j])*(x[i]-x[j])+(1-fabs(y[i]-y[j]))*(1-fabs(y[i]-y[j]))
        #         if sqrt(dis)<LONG and i!=j:
        #             link[i][j]=1

#--------------------------ノードの次数とリンクチェック------------------------------

degree_total=0
for i in range(N):#各ノードの次数決定
    for j in range(N):
        if link[i][j]==1:
            degree[i]+=1

degree_max=0#ネットワーク上におけるノードの最大次数
for i in range(N):
    if degree_max<=degree[i]:
        degree_max=degree[i]
print(degree_max)

for i in range(N):#リンクチェック
    if degree[i]==0:
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
        if link[i][j]==1:
            if q[j]-q[i]>=MAX:#相手ー自分の値をより大きいものに更新し続ける．→自分が最も大きい場合，負の値となり、MAXは更新されない。
                MAX=q[j]-q[i]#あるiにおける，最終的なMAXの値を下のfor文で適用している．
    for j in range(N):
        if link[i][j]==1:
            if q[j]-q[i]==MAX:#jと最も差があるのはi
                max_grade[i]=j#ノードiともっとも差があるノードはノードj#ここまでで，隣接ノードとの状態量の差を把握している．

#クラスタサイズ判定
for i in range(N):
    grade1=0
    for j in range(50):#grade1=grade2の時の処理のために,jで回す必要がある．N=500は大きすぎる
        if j==0:#自分がCHの時の処理#j=0なのは，j=0が回し終わった時点で，自分自身がCHと判別でき，それ以降のjで回す必要がないから
            grade1=max_grade[i]#max_grade[i]は，ノードiと一番差があるノード番号
            if grade1==-1:#自分がCHの時の処理　#自分と一番差があるノード番号が-1→自分がクラスタヘッドということが分かる．
                CH_num[i]=i#ノードiが所属するクラスタのCH
                size[i]+=1#ノードiが属するクラスタサイズ
                break
        grade2=max_grade[grade1]#grade2は，あるiにとって一番差があるノードgrade1,にとってさらに一番差があるノード(iから2ホップ先)．この行の一番最後のgrade1=grade2が適用される
        if grade2==-1:#自分（ノードi）の隣がCH←隣から探し始めたら、自分がCH←grade2==-1より
            CH_num[i]=grade1#grade1=max_grade[i]#max_grade[i]は，ノードiと一番差があるノード番号(1ホップ先)
            size[grade1]+=1
            break
        if max_grade[grade2]==-1:#自分の２個となりcH
            CH_num[i]=grade2
            size[grade2]+=1
            break
        if grade2==max_grade[max_grade[grade2]]: #grade2と同じ値のCHの時#2ホップ先と3ホップ先の状態量が同じ場合の処理
            if grade2>max_grade[grade2]:#ノード番号が大きい方をクラスタヘッドに
                CH_num[i]=grade2
                size[grade2]+=1
                break
            if max_grade[grade2]>grade2:
                CH_num[i]=max_grade[grade2]
                size[max_grade[grade2]]+=1
                break

        grade1=grade2#どのif分にも引っかからない場合は，grade1をgrade2変換→jで回すことによりNホップ先まで判定可能に．

#----------------------初期状態におけるクラスタリングまで終了---------------------------

#-------------------------------初期状態における測定-------------------------------

print('---------------initial state-------------')
#クラスタ数をカウント
for i in range(N):
    if CH_num[i]==i:
        CH_counter+=1
#print('CH_counter',CH_counter)

#---------------------シミュレーション開始-----------------------------------------
time=1#シミュレーション時間
for k in range(time):
    time_list.append(k)
    #初期化
    for i in range(N):
        diffusion[i]=0
        dd[i]=0
        CH_num[i]=0
        size[i]=0
        max_grade[i]=-1
    CH_counter=0
    Csize=[]

    for h in range(1):#tが1進むごとに状態量を更新する回数
        #拡散項
        for i in range(N):
            diffusion[i]=0
            dd[i]=0
        for i in range(N):
            for j in range(N):
                if link[i][j]==1 and q[i]>q[j]:
                    diffusion[i]+=diffusion1(i, j, q)#総和の役割
                    diffusion[j]-=diffusion1(i, j, q)
                    dd[i]=diffusion[i]#プログラム高速化のため
                    dd[j]=diffusion[j]

        #next_qの計算・分布値の更新
        for i in range(N):
            if q[i]!=CH_q:
                next_q[i]=(q[i]-dd[i])*q_dec
                difference_q[i]=next_q[i]-q[i]
                q[i]=next_q[i]

        #CHの状態量追加
        for i in range(N):
            if i==0 or i==1 or i==2 or i==3:
                q[i]=CH_q

    #--------------------クラスタ判定--------------------------------------------

    for i in range(N):
        MAX=0.0
        for j in range(N):
            if link[i][j]==1:
                if q[j]-q[i]>=MAX:
                    MAX=q[j]-q[i]
                    max_grade[i]=j


    #クラスタサイズ判定
    for i in range(N):
        grade1=0
        for j in range(50):
            if j==0:
                grade1=max_grade[i]
                if grade1==-1:
                    CH_num[i]=i
                    size[i]+=1
                    break
            grade2=max_grade[grade1]
            if grade2==-1:
                CH_num[i]=grade1
                size[grade1]+=1
                break
            if max_grade[grade2]==-1:
                CH_num[i]=grade2
                size[grade2]+=1
                break
            if grade2==max_grade[max_grade[grade2]]:
                if(grade2>max_grade[grade2]):
                    CH_num[i]=grade2
                    size[grade2]+=1
                    break
                if max_grade[grade2]>grade2:
                    CH_num[i]=max_grade[grade2]
                    size[max_grade[grade2]]+=1
                    break

            grade1=grade2

    #------------------------クラスタ判定終了---------------------------------------

    #------------------------シミュレーション中のステータス測定----------------------

    '''
    #対象時間の様子をプロット
    if k!=0 and k%100==0:
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
        plt.savefig('/Users/kawasakirio/Desktop/b4result/1119qresult/'+'zisuu'+'dec='+str(q_dec)+'t='+str(k)+'sigma='+str(sigma)+'.png')#語尾に'.png'が必要
        plt.cla()


        #クラスタリングをプロット
        for i in range(N):#
            if CH_num[i]!=i:#CH以外
                plt.plot(x[i],y[i],marker='o')
        for i in range(N):#上と統合すると、プロットが被る
            if CH_num[i]==i:#CH
                plt.plot(x[i],y[i],markeredgecolor='black',marker='*')
        plt.xlim(xmin,1)
        plt.ylim(ymin,1)
        plt.xlabel('x-coordinate')
        plt.ylabel('y-coordinate')
        plt.savefig('/Users/kawasakirio/Desktop/b4result/1119qresult-clustering/'+'zisuu'+'dec='+str(q_dec)+'t='+str(k)+'sigma='+str(sigma)+'.png')#語尾に'.png'が必要
        plt.cla()
    '''

    #各クラスタサイズをカウント・さらに統計量を計算
    if k!=0 and k%100==0:
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
        print('q',q)

    if k==100:
        previous_cv=cv
    if k==500 and previous_cv==cv:
        break

    difference_q_list.append(sum(difference_q))
    #print(previous_cv)
#-------------------------シミュレーション終了------------------------------------
#-------------------------最終的なステータス測定-----------------------------------

print('-------------final state--------------')

# #各クラスタサイズをカウント・さらに統計量を計算
# Csize=[]
# print('-----size-----')
# for i in range(N):
#     if CH_num[i]==i:
#         #print(size[i])
#         Csize.append(size[i])
# mea=sta.mean(Csize)
# var=sta.variance(Csize)
# std=sta.stdev(Csize)
# cv=std/mea#変動係数
# print('mean',mea)
# print('stdev',std)
# print('cv',cv)

#------------------------------ホップ数判定プログラム------------------------------------------

#CHからのホップ数を計算
hop_count=[0 for i in range(N)]
hop_frag_0=[0 for i in range(N)]
for i in range(N):
    if CH_num[i]==i:
        hop_frag_0[i]=1
hop=50#目的ノードまでの十分なホップ数
for k in range(hop):#あるクラスタ内に存在するノードに対して，CHからのホップ数を出力
    for i in range(N):
        if hop_frag_0[i]==1:
            for j in range(N):
                if link[i][j]==1 and i!=j and hop_frag_0[j]==0 and CH_num[i]==CH_num[j]:
                    hop_frag_0[i]=2
                    hop_frag_0[j]=3
                    #print('node.No=',j,'hop_count=',k+1)
                    hop_count[j]=k+1
    for l in range(N):
        if hop_frag_0[l]==3:
            hop_frag_0[l]=1

# #print(hop_count)

#------------------------------AODV------------------------------------------

aodv_exp_counts = 10
num_packet_sum = 0
num_tra_packet_sum = 0
num_rec_packet_sum = 0
battery_consumption_tra_sum = 0
battery_consumption_rec_sum = 0
battery_consumption_sum = 0

for ii in range(aodv_exp_counts):
    #送信ノードからのホップ数を計算
    num_packet = 0
    num_tra_packet = 0
    num_rec_packet = 0
    aodv_hop_count = [0 for i in range(N)]
    start_mark = [0 for i in range(N)]
    hop_frag_s = [0 for i in range(N)]
    hop_frag_d = [0 for i in range(N)]
    random.seed(ii+3)
    seed_s = random.randrange(N)
    hop_frag_s[seed_s] = 1
    start_mark[seed_s] = 1

    random.seed((ii+7)*(ii+11))#タネが重複しないように複雑に
    seed_d = random.randrange(N)
    hop_frag_d[seed_d] = 1

    hop = 100  # 目的ノードまでの十分なホップ数
    for k in range(hop):
        for i in range(N):
            if hop_frag_s[i] == 1 and hop_frag_d[i] == 0:
                for j in range(N):
                    # 目的ノードにパケット送信
                    if hop_frag_d[j] == 1 and link[i][j] == 1 and i != j and hop_frag_s[j] == 0:
                        hop_frag_s[i] = 2
                        hop_frag_s[j] = 2  # パケットを止める
                        aodv_hop_count[j] = k+1  # ホップ数をカウント→一応．パケット量としては使わない
                    #パケット未送信のノードにパケット送信
                    elif link[i][j] == 1 and i != j and hop_frag_s[j] == 0:
                        hop_frag_s[i] = 2
                        hop_frag_s[j] = 3
                        aodv_hop_count[j] = k+1  # ホップ数をカウント→一応．パケット量としては使わない
        for i in range(N):
            if hop_frag_s[i] == 3:
                hop_frag_s[i] = 1


    for i in range(N):
        #RREQ送信数
        if aodv_hop_count[i] != 0:  # 送信ノードをカウントしない代わりに受信ノード分をカウント。実際は逆。
            num_tra_packet += 1
        #RREQ受信数
        if aodv_hop_count[i] != 0 or start_mark[i] == 1:
            num_rec_packet += degree[i]
            for j in range(N):
                if link[i][j] == 1 and hop_frag_d[j] == 1:  # 中継ノードは宛先ノードから受信しないので引き算
                    num_rec_packet -= 1
        if aodv_hop_count[i] == 0:  # 宛先ノードとパケットを受け取らなかったノード間のリンク数だけ引き算
            for j in range(N):
                if link[i][j] == 1 and hop_frag_d[j] == 1:
                    num_rec_packet -= 1
        #RREP送信数
        if hop_frag_d[i] == 1:
            num_tra_packet += aodv_hop_count[i]
            #RREP受信数
            for k in range(aodv_hop_count[i]):
                for j in range(N):
                    if link[i][j] == 1 and aodv_hop_count[i] - 1 == aodv_hop_count[j]:
                        num_rec_packet += degree[i]
                        i = j
                        break

    #消費電力
    battery_consumption_tra = 0.0
    battery_consumption_tra = num_tra_packet * 512 * (3.3 * (10 ** (-7)))
    battery_consumption_rec = 0.0
    battery_consumption_rec = num_rec_packet * 512 * (1.9 * (10 ** (-7)))
    battery_consumption = 0.0
    battery_consumption = battery_consumption_rec + battery_consumption_tra
    #全ての実験のパケット数
    num_tra_packet_sum += num_tra_packet
    num_rec_packet_sum += num_rec_packet
    num_packet = num_tra_packet + num_rec_packet
    num_packet_sum += num_packet
    #全ての実験の消費電力
    battery_consumption_tra_sum += battery_consumption_tra
    battery_consumption_rec_sum += battery_consumption_rec
    battery_consumption_sum += battery_consumption

    #結果の可視化
    fig, ax = plt.subplots()
    xmin = 0
    xmax = N-1
    ymin = 0
    ymax = 5
    for i in range(N):
        plt.plot(x[i], y[i], marker='o', color="blue")
        ax.annotate(str(aodv_hop_count[i]), (x[i], y[i]))  # GNからのホップ数を出力
    for i in range(N):  # 上と統合すると、プロットが被る
        if start_mark[i] == 1:  # CH
            plt.plot(x[i], y[i], markeredgecolor='black',
                    marker='^', markersize=20, color="blue")
            ax.annotate(str(aodv_hop_count[i]), (x[i], y[i]))  # GNからのホップ数を出力
        if hop_frag_d[i] == 1:
            plt.plot(x[i], y[i], markeredgecolor='black',
                    marker='X', markersize=20, color="blue")
            ax.annotate(str(aodv_hop_count[i]), (x[i], y[i]))  # GNからのホップ数を出力


    plt.xlim(xmin, 1)
    plt.ylim(ymin, 1)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.savefig('/Users/kawasakirio/Desktop/M2result/1019ゼミ/'+str(ii)+'aodv_hop.pdf')  # 語尾に'.pdf'が必要
    plt.cla()

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
# print("総パケット数", num_packet_sum)
print('総消費電力量', battery_consumption_sum, 'J')

#---------------------------各クラスタ構造のラプラシアン行列作成------------------------
'''
def cluster_evalue_1(ch):#クラスタ毎の媒介中心生を算出，GN.ver
    G=nx.Graph()
    for i in range(N):
        if CH_num[i]==ch:#chはクラスタ(CHノード)番号
            G.add_node(i)
            for j in range(N):
                if CH_num[i]==CH_num[j] and i>j and link[i][j]==1:#(i>j)を付けるとノード番号が正常になる
                    G.add_edge(i,j)
    L=nx.laplacian_matrix(G).todense().A#グラフGからarray型のラプラシアン行列Lを作成
    evalue,evector=np.linalg.eigh(L)#固有値(昇順)と固有ベクトル
    #return between_cent_CH_GN_normalization

lamb_list=[]
for k in range(N):
    if CH_num[k]==k:#CHの場合、関数を起動
        ch=k
        lamb1=cluster_evalue_1(ch)#returnの結果
        print('cluster number is', str(k),'connectivity is,',lamb1)
        lamb_list.append(lamb1)
'''

#---------------------------最終的なクラスタリングを可視化----------------------------

# fig,ax=plt.subplots()
# xmin=0
# xmax=N-1
# ymin=0
# ymax=5
# for i in range(N):
#     plt.plot(x[i], y[i], marker='o', color="blue")
#     ax.annotate(str(aodv_hop_count[i]), (x[i], y[i]))  # GNからのホップ数を出力
# for i in range(N):  # 上と統合すると、プロットが被る
#     if start_mark[i] == 1:  # CH
#         plt.plot(x[i], y[i], markeredgecolor='black',
#                  marker='^', markersize=20, color="blue")
#         ax.annotate(str(aodv_hop_count[i]), (x[i], y[i]))  # GNからのホップ数を出力
#     if hop_frag_d[i] == 1:
#         plt.plot(x[i], y[i], markeredgecolor='black',
#                  marker='X', markersize=20, color="blue")
#         ax.annotate(str(aodv_hop_count[i]), (x[i], y[i]))  # GNからのホップ数を出力


# plt.xlim(xmin,1)
# plt.ylim(ymin,1)
# plt.xlabel('x-coordinate')
# plt.ylabel('y-coordinate')
# plt.savefig('/Users/kawasakirio/Desktop/'+'aodv_hop.pdf')#語尾に'.pdf'が必要
# plt.cla()


'''
#クラスタ毎のネットワークトポロジを可視化
for k in range(N):
    if CH_num[k]==k:#CHの場合、関数を起動
        ch=k
        G=nx.Graph()
        for i in range(N):
            if CH_num[i]==ch:#chはクラスタ(CHノード)番号
                G.add_node(i)
                for j in range(N):
                    if CH_num[i]==CH_num[j] and i>j and link[i][j]==1:
                        G.add_edge(i,j)
        nx.draw_networkx(G,node_size=100,font_size=5)
        plt.savefig('/Users/kawasakirio/Desktop/M1result/0626/'+'CH'+str(ch)+'network'+'sd='+str(sd)+'.pdf')#語尾に'.pdf'が必要
        plt.cla()
'''
#-------------------------------------------------------------------------------
