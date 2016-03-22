#-*- coding:utf-8 -*-   #�����ĵ���������
"""
��ԭʼtxt�����ļ�ת��Ϊnpy�ļ�����Ϊdbn�����ļ�
������
1.ת��ѵ�����ݵ�txt�ļ���npy�ļ�
2.ת����ǩ������txt�ļ���npy�ļ�
"""

import shutil
from global_para import *


def isfloat(str):   #�ж��ַ����Ƿ��Ǹ�����
    if str.isdigit():
        return True
    minpp = 1
    for i in range(0,len(str)):
        c = str[i]
        if c.isdigit():
            continue
        if c=='-' and i==0:
            minpp = 2
            continue
        if c=='.' and i>=minpp and i<(len(str)-1):
            continue
        return False
    return True


def extract_data_from_txt(txt,npy,dtype):  #��txt�����ļ���ȡ����ת��Ϊnpy�ļ�
    f = open(txt)
    x = []
    cnt = 0
    dim = 0 #ά��

    for line in f:
        line = line.rstrip('\n')
        if len(line) < 1:
            continue
        if cnt == 0:  #��һ����ÿ�����ά��
            dim = (int)(line)
            print 'Dimention:',line
            x = np.ndarray((0, dim), dtype=dtype)
        else:   #���µ�ÿ����ÿ�����ֵ
            items = line.split()
            for i in range(0,len(items)):
                if isfloat(items[i]):
                    items[i] = float(items[i])
            if len(items)!=dim: #��ǰ���ά������ȷ
                print 'line:',cnt,'has',len(items),'items instead of',dim
                continue
            tmp = np.array([items])
            tmp = tmp.astype('f')   #����ת��Ϊfloat����
            #print tmp
            x = np.append(x, tmp, axis=0)   #����axis���������һά����
        cnt += 1

    np.save(npy, x)
    
    print "length:", len(x)
    print "shape:", x.shape
    print ''

def extract_filename(fname):    #ȡ�ļ�����ȥ���ļ�·���ͺ�׺
    left = fname.rfind('\\')+1
    right = fname.rfind('.')
    if left <= 0:
        left = 0
    if right < 0:
        right = len(fname)

    return fname[left:right]

def extract_songname(fname):    #
    left = fname.rfind('-')+1
    if left <= 0:
        left = 0

    return fname[left:]


def extract_label_from_txt(txt,npy,clus_col):  #��txt�����ļ���ȡ��ǩת��Ϊnpy�ļ�,clus_colΪ�����������ڵ���,һ��Ϊ�ļ������ڵ���
    f = open(txt)
    y = []
    cnt = 0
    dim = 0 #ά��
    clus = {}
    now = ''    #��ǰ���ݵ�����

    for line in f:
        line = line.rstrip('\n')
        if len(line) < 1:
            continue
        if cnt == 0:  #��һ����ÿ�����ά��
            dim = (int)(line)
            print 'Dimention:',line
            if clus_col >= dim:
                print 'cluster column exceed Dimention.'
                sys.exit(-1)

        else:   #���µ�ÿ����ÿ�����ֵ
            items = line.split()
            #print items
            if len(items)!=dim: #��ǰ���ά������ȷ
                print 'line:',cnt,'has',len(items),'items instead of',dim
                continue
            now = items[clus_col].decode('gbk')
            now = extract_filename(now)
            now = extract_songname(now)
            #print now
            clus[now] = 1
            #print now
            y.append(now)
            
        cnt += 1

    yy = np.array(y)
    np.save(npy, yy)

    print "length:", len(y)
    print "shape:", yy.shape
    print 'clus_cnt',len(clus)
    print ''

if __name__ == '__main__':
    #��LSH�������ת��Ϊnpy�ļ�����Ϊѵ����
    extract_data_from_txt(DATASET+'/LSHVector.txt',DATASET+"/train_xdata.npy",X_DTYPE)
    extract_label_from_txt(DATASET+'/LSHIndex.txt',DATASET+"/train_ylabels_song.npy",1)

    #������������Ĳ�ѯLSH��ת��Ϊnpy�ļ�����Ϊ��ѯ��
    extract_data_from_txt(DATASET+'/QueryLSHLSVector.txt',DATASET+"/query_xdata.npy",X_DTYPE)
    extract_label_from_txt(DATASET+'/QueryLSHLSIndex.txt',DATASET+"/query_ylabels_song.npy",0)

    #�����ļ�
    # shutil.copyfile(DATASET+"/train_xdata.npy",DATASET+"/test_xdata.npy")
    # shutil.copyfile(DATASET+"/train_ylabels.npy",DATASET+"/test_ylabels.npy")
    #extract_from_txt('NLSHVector.txt','NLSHVector.npy')
    print 'Done'