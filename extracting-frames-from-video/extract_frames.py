import cv2
from enum import Enum


class ExtractingFramesType(Enum):
    BY_TIME = 0
    BY_NUM = 1


def extract_frames_by_list_of_frame_numbers(cap, list_of_frame_numbers):
    list_of_frame_numbers.sort()
    total = cap.get(7)
    list_of_frames = []
    counter = 0
    while True:
        if ~cap.grap():
            print("Wrong try of graping video while extracting frames\n")
            exit(-1)

        is_retrieved_right, frame = cap.retrieve
        if ~is_retrieved_right:
            print("Wrong try of retrieving frame while extracting one\n")
            exit(-1)

        if counter == list_of_frame_numbers[list_of_frames.count()]:
            list_of_frames += frame

        if counter == total:
            break

    return list_of_frames


def extract_frames_by_number(cap, num):
    total = cap.get(7)
    step = total / num
    list_of_frame_numbers = []
    counter = 0
    while counter < total:
        list_of_frame_numbers += counter
        counter += step

    return extract_frames_by_list_of_frame_numbers(cap, list_of_frame_numbers)


def extract_frames_by_time(cap, list_of_time_codes):
    list_of_frame_numbers = []
    fps = cap.get(5)
    total = cap.get(7)

    for i in list_of_time_codes:
        frame_number = i * fps
        if frame_number < 0 | frame_number >= total:
            continue
        list_of_frame_numbers += frame_number

    return extract_frames_by_list_of_frame_numbers(cap, list_of_frame_numbers)


def extract_frames_from_video(video_name):
    cap = cv2.VideoCapture(video_name)

    if ~cap.isOpened():
        print("Video hasn't opened\n")
        exit(-1)

    list_of_frames = []
    if type == ExtractingFramesType.BY_TIME:
        list_of_time_codes = []

        number_of_entering_values = int(input("Enter number of entering time codes: "))
        for i in range(number_of_entering_values):
            list_of_time_codes += input("Enter time code: ")

        list_of_frames = extract_frames_by_time(cap, list_of_time_codes)

    elif type == ExtractingFramesType.BY_NUM:
        number_of_frames = int(input("Enter number of extracting frames: "))
        list_of_frames = extract_frames_by_number(cap, number_of_frames)

    return list_of_frames
