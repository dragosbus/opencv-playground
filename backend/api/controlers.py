import cv2 as cv
import os
import io
import base64
import numpy as np
import gzip
from flask import send_from_directory

def _writenpy(X, path, *, dtype):
    np.save(path, X.astype(dtype=dtype, copy=False))
    
    return True

def writenpy32(X, path):
    return _writenpy(X, path, dtype='float32')

def writemda32(X, fname):
    return writenpy32(X, fname)

def _mda32_to_base64(d) -> str:
    # f = io.BytesIO()
 
    return base64.b64encode(d).decode('utf-8')


def read_numpy_array(image):
    image_arr = cv.imread(f"{os.path.abspath(os.getcwd())}/api/{image}", -1)
    
    f = gzip.GzipFile('image_arr.npy.gz', "wb", compresslevel=6)
    np.save(f, image_arr)
    
    g = send_from_directory(os.path.abspath(os.getcwd()),'image_arr.npy.gz',as_attachment=True)
    print(g.response)
    return g
