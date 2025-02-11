import cv2
import numpy as np

def hello() -> str:
    return "Hello from Black Hammer ImUtils!"

def cv2_draw_mask_overlay(img, mask, alpha=0.3):
    # mask = mask[0].astype(np.uint8) * 255

    overlay = np.zeros( (*mask.shape,3), np.uint8)
    overlay[mask>0] = 161, 14, 240

    # Perform the alpha blending
    blended_image = img * (1 - alpha) + overlay * alpha
    return blended_image.astype(np.uint8)