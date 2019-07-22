import cv2


def apply_sift(frames):
    # Create SIFT object
    sift = cv2.xfeatures2d.SIFT_create()

    # result an array of tuples -> [ (frame_keypoints_sift, frame_descriptors_sift), ...]
    result = [sift.detectAndCompute(frame, None) for frame in frames]

    return result
