#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np
#%%
pencil = cv2.imread("index.jpg", cv2.IMREAD_COLOR)
cv2.imshow("pencil", pencil)
cv2.line(pencil, [0,0], [150,150], (255,0,0), 5)
cv2.imshow("pencil", pencil)
# plt.imshow(pencil, cmap="gray")
# plt.xticks([]), plt.yticks([])
# plt.plot([50,100], [50,100], "r", linewidth=5)
# plt.show()
#%%
cv2.waitKey(0)
cv2.destroyAllWindows()
