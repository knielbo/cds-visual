# Assignments Cultural Data Science - Visual #

## In class assignments ##

### Lesson 1 ###

> **_Question:_** What does the `import cv2` statement do?
1. Imports our OpenCV Python bindings.
2. Imports the NumPy library for numerical processing.
3. Displays an image to our screen.
4. Imports the SciPy library for numerical processing.

> **_Question:_** Given the following NumPy array shape, how would we interpret the width, height, and number of channels in the image: (400, 600, 3):
1. width=600, height=400, channels=3
2. width=400, height=600, channels=3
3. width=600, height=3, channels=400
4. width=3, width=600, channels=400

> **_Question:_** Suppose our image has a width of 700 pixels, a height of 550 pixels, and 3 channels, one for each Red, Green, and Blue component. How would we express this image as a NumPy array shape?
1. (3, 550, 700)
2. (700, 550, 3)
3. (550, 700, 3)
4. (3, 700, 550)

> **_Question:_** Instead of the load_display_save.py script outputting a file named newimage.jpg, modify it so the output becomes my_output.png. What is the correct function call to make this change?
1. cv2.imsave("my_output.png", image)
2. cv2.imread("my_output.png", image)
3. cv2.imwrite("my_output.png", image)
4. cv2.imwrite(image, "my_output.png")

##### Comment #####
- Students must understand (height, width, channel) tuples and how they map onto (x, y) coordinates

### Lesson 2 ###
> **_Question:_** We have an image that is 393 pixels wide and 312 tall. How many total pixels are in the image?
1. 280,800
2. 122,616
3. 367,848
4. 93,600

> **_Question:_** OpenCV stores RGB pixels in what order?
1. BRG
2. GBR
3. RGB
4. BGR

> **_Question:_** The RGB tuple (255, 0, 0) codes for red. But OpenCV would actually interpret this color as:
1. Blue
2. Green
3. Yellow
4. Orange

> **_Question:_** Modify getting_and_setting.py script to display the Red, Green, and Blue values of the trex.png image for the pixel located at x=90, y=219. What is the (approximate) pixel value?
1. r=94, g=79, b=49
2. r=239, g=229, b=222
3. r=49, g=79, r=94
4. r=222, g=229, b=239

##### Comment #####
- Students must understand reverse color format and x, y coordinates in image

#### Lesson 3 ####
> **_Question:_** As the size of the blur kernel increases…
1. The kernel size has no impact on how much or how little an image is blurred.
2. The image will appear less blurred.
3. The image will appear to be more blurred.

> **_Question:_** The difference between simple average blurring and Gaussian blurring is…
1. The average blur is a weighted mean of the local pixels and the Gaussian blur is not.
2. There is no difference between average and Gaussian blurring.
3. A Gaussian blur is a weighted average of the local pixels and the average blur is not.

> **_Question:_** To obtain better edge maps, we often apply what pre-processing function prior to applying the cv2.Canny function?
1. Blurring/smoothing
2. Histogram equalization
3. Thresholding
4. Translation

> **_Question:_** Blur img/clonazepam_1mg.png slightly using a 5 x 5 Gaussian kernel. Then apply the cv2.Canny function to detect the outline of the pills in the image. Which set of Canny parameters obtain a “reasonable” edge map?
1. (10, 200)
2. (240, 250)
3. (200, 250)


#### Lesson 4 ####




#### Lesson 5 ####
#### Lesson 6 ####
#### Lesson 7 ####
#### Lesson 8 ####
#### Lesson 9 ####
#### Lesson 10 ####
#### Lesson 11 ####
#### Lesson 12 ####
#### Lesson 13 ####

## Home assignments ##
Exam: The portfolio will consist of 3-7 assignments.

### Assignment 1

__Image Search Engine__
_Tasks_
1. Show how to extract and visualize color histograms from an image.
2. Exemplify how to compare two histograms for similarity and access their similarity
3. Select $n$ images (for $n > 3$) and rank the images for similarity

#### Similarity
[for instructor](https://hiweller.github.io/colordistance/color-metrics.html)
1. `cv2.compareHist`
2. Earth Mover’s Distance (`scipy.stats.wasserstein_distance`)
3. Chi-squared
```py
def chi2_distance(p, q):
    # compute and return the chi-squared distance
    return 0.5 * np.sum((p - q) **2 / (p + q + 1e-10))


def chi2_distance(histA, histB, eps = 1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])
    # return the chi-squared distance
    return d
```
