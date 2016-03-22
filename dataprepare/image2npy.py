from PIL import Image
import numpy as np

def ConvertImage2Npy(filepath):
	return np.array(Image.open(filepath))
