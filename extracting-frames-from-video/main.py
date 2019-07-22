from extract_frames import extract_frames_from_video
from apply_sift_to_frame import make_sift


def main():
    video_name = input("Enter name of video: ")
    list_of_frames = extract_frames_from_video(video_name)
    list_of_keypoints = make_sift(list_of_frames)