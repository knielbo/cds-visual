import cv2
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def jimshow(image, title=False):
    """ 
    """
    # Acquire default dots per inch value of matplotlib
    dpi = mpl.rcParams['figure.dpi']

    height, width, depth = image.shape
    figsize = width / float(dpi), height / float(dpi)
    
    plt.figure(figsize=figsize)
    
    if depth == 1:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
      
    if title:
        plt.title(title)
    plt.axis('off')
    
    plt.show()

def translate(image, x, y):
    """Define the translation matrix and perform the translation
    """
    T = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, T, (image.shape[1], image.shape[0]))

    # Return the translated image
    return shifted

if __name__=="__main__":
    pass