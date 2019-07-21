import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('./images/watch.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('picture', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(image, cmap='gray', interpolation='bicubic')
# plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.show()

cv2.imwrite('./images/watch-gray.png', image)