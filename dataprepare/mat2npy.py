from scipy.io import loadmat
import numpy

datafile = r"D:\heng\data\butterfly\test\butterflyData.mat"

data = loadmat(datafile, matlab_compatible=True)['data']
#data = numpy.transpose(data)
numpy.save(r"D:\heng\data\butterfly\test\butterflyData.npy",data)