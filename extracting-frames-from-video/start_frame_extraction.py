import sys
import os
import shutil
from extract_frames import extract_frames_from_video
from apply_sift_to_frame import apply_sift
from showing_and_saving_pics import show_and_save_pics


def start():
    print("PWD:\n\t", sys.path[0])
    frames = extract_frames_from_video()
    keypoints_and_descriptors = apply_sift(frames)
    show_and_save_pics(frames, keypoints_and_descriptors)


def clear_folder():
    folder = './made_pics'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print('Running start_frame_extraction.py from MODULE: extracting-frames-from-video')
    clear_folder()
    start()
    print('MODULE start_frame_extraction.py is done')
