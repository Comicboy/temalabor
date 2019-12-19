import cv2
import os
import glob

# Képek újraméretezése a CNN számára (256x256)
def fn_resize(folder,fpath, fname):
    path = folder
    files = [f for f in glob.glob(path + "**/*.jpg", recursive=True)]

    for i in range(len(files)):
        try:

            oriimg = cv2.imread(files[i], cv2.IMREAD_COLOR)
            newimg = cv2.resize(oriimg, (256, 256))
            cv2.imwrite(os.path.join(fpath , (fname+"{}"+".jpg").format(i),), newimg)
        except Exception as e:
            print(str(e))

fn_resize(r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\Dataset\tv",r"C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\datasetr\tvs","tv")