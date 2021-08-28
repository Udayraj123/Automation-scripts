from skimage import io
from image_processing import ImageProc
import sys

before = io.imread(sys.argv[1])
after = io.imread(sys.argv[2])

before, after = ImageProc.pre_processing(before, after)
ssi, mse, hist_diff =  ImageProc.compare(before, after)

print(f"SSI value is {ssi}")
print(f"MSE value is {mse}")
print(f"Histogram difference is {hist_diff}")