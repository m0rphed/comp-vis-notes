import cv2


def make_sift(list_of_frames):
    list_of_sifted_frames = []
    for i in list_of_frames:
        list_of_sifted_frames += cv2.SIFT(i)
    return list_of_sifted_frames
