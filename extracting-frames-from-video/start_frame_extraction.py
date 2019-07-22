import sys
from extract_frames import extract_frames_from_video
from apply_sift_to_frame import apply_sift


def start():
    print("PWD:\n\t", sys.path[0])
    # video_name = input("Enter name of video: ")
    video_name = "winter-saint-petersburg.mp4"
    frames = extract_frames_from_video(video_name)
    keypoints = apply_sift(frames)


if __name__=='__main__':
    start()
    print('Running start_frame_extraction.py from MODULE: extracting-frames-from-video')
