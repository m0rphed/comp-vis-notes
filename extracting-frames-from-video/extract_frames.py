import cv2
from enum import Enum
from extracting_by_timecode import extract_frames_by_timecodes
from extracting_by_number import extract_frames_by_number
from extracting_by_range import extract_frames_by_ranges
from extracting_by_range_and_number import extract_frames_by_ranges_and_number


class ExtractingFramesType(Enum):
    BY_TIME = 0
    BY_NUM = 1
    BY_RANGES = 2
    BY_RANGES_AND_NUM = 3


def extract_frames_from_video():
    print('Sample: winter-saint-petersburg.mp4')
    video_name = input("Enter name of video: ")

    cap = cv2.VideoCapture(video_name)
    if not cap.isOpened():
        print("Video hasn't opened\n")
        exit(-1)

    list_of_frames = []
    print('Be aware of types: 0 - by timecodes; 1 - by number, 2 - by ranges, 3 - by ranges and numbers')
    type_of_extracting = ExtractingFramesType(int(input("Enter type of extracting: ")))
    if type_of_extracting == ExtractingFramesType.BY_TIME:
        list_of_frames = extract_frames_by_timecodes(cap)

    elif type_of_extracting == ExtractingFramesType.BY_NUM:
        list_of_frames = extract_frames_by_number(cap)

    elif type_of_extracting == ExtractingFramesType.BY_RANGES:
        list_of_frames = extract_frames_by_ranges(cap)

    elif type_of_extracting == ExtractingFramesType.BY_RANGES_AND_NUM:
        list_of_frames = extract_frames_by_ranges_and_number(cap)

    else:
        print('Wrong type number')
        exit(-1)

    return list_of_frames
