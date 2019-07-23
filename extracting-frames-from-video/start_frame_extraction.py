import sys
from extract_frames import extract_frames_from_video
from apply_sift_to_frame import apply_sift
from showing_and_saving_pics import show_and_save_pics


def start():
    print("PWD:\n\t", sys.path[0])
    frames = extract_frames_from_video()
    keypoints_and_descriptors = apply_sift(frames)
    show_and_save_pics(frames, keypoints_and_descriptors)


if __name__ == '__main__':
    print('Running start_frame_extraction.py from MODULE: extracting-frames-from-video')
    start()
    print('MODULE start_frame_extraction.py is done')
