import cv2
from enum import Enum


class ExtractingFramesType(Enum):
    BY_TIME = 0
    BY_NUM = 1
    BY_RANGES = 2
    BY_RANGES_AND_NUM = 3


def extract_frames_by_list_of_frame_numbers(captured, list_of_frame_numbers):
    list_of_frame_numbers.sort()
    total = int(captured.get(7))
    list_of_frames = []
    counter = 0
    while True:
        '''
        if ~captured.grap():
            print("Wrong try of graping video while extracting frames")
            exit(-1)

        is_retrieved_right, frame = captured.retrieve
        if ~is_retrieved_right:
            print("Wrong try of retrieving frame while extracting one")
            exit(-1)
        '''

        is_read_right, frame = captured.read()
        if not is_read_right:
            print("Wrong try of reading video while extracting frames")
            exit(-1)

        if counter == list_of_frame_numbers[len(list_of_frames)]:
            list_of_frames.append(frame)
            if len(list_of_frames) == len(list_of_frame_numbers):
                break

        counter += 1
        if counter == total:
            break

    return list_of_frames


def extract_frames_by_number(cap):
    number_of_frames = int(input("Enter number of extracting frames: "))
    if number_of_frames < 1:
        exit(0)

    total = cap.get(7)
    step = total / number_of_frames
    frame_numbers = []

    for i in range(0, total, step):
        frame_numbers.append(i)

    return extract_frames_by_list_of_frame_numbers(cap, frame_numbers)


def enter_one_time_code(hinting_string):
    time_code = input(hinting_string)
    time = 0
    if ':' in time_code:
        splitted_time = time_code.split(':')
        for time_value in splitted_time:
            time = time * 60 + int(time_value)
    else:
        time = int(time_code)

    return time


def extract_frames_by_timecodes(cap):
    fps = int(cap.get(5))
    total = int(cap.get(7))
    frame_numbers = []
    number_of_entering_values = int(input("Enter number of entering timecodes: "))
    if number_of_entering_values < 1:
        exit(0)

    print(f'Be aware: timecodes in range 0-{int(total / fps)} seconds / 0:00-{int(total / 25 / 60)}:{int(total / 25 % 60)} minutes')
    for i in range(number_of_entering_values):
        while True:
            frame_number = enter_one_time_code('Enter timecode: ') * fps
            if frame_number < 0 or frame_number >= total:
                print('Wrong timecode\n')
                continue
            else:
                break
        frame_numbers.append(frame_number)

    return extract_frames_by_list_of_frame_numbers(cap, frame_numbers)


def extract_frames_by_ranges(cap):
    total = int(cap.get(7))
    fps = int(cap.get(5))
    number_of_ranges = int(input("Enter number of extracting ranges: "))
    if number_of_ranges < 1:
        exit(0)

    print(f'Be aware: timecodes in range 0-{int(total / fps)} seconds / 0:00-{int(total / 25 / 60)}:{int(total / 25 % 60)} minutes')
    frame_numbers = []
    for i in range(number_of_ranges):
        while True:
            while True:
                frames_range_beginning = int(enter_one_time_code('Enter beginning timecode: ') * fps)
                if frames_range_beginning < 0 or frames_range_beginning >= total:
                    print('Entered wrong timecode\n')
                    continue
                else:
                    break

            while True:
                frames_range_ending = int(enter_one_time_code('Enter beginning timecode: ') * fps)
                if frames_range_ending < 0 or frames_range_ending >= total:
                    print('Entered wrong timecode\n')
                    continue
                else:
                    break

            if frames_range_beginning > frames_range_ending:
                print('Beginning timecode is after ending one')
                continue
            else:
                break

        for j in range(frames_range_beginning, frames_range_ending):
            frame_numbers.append(j)

    return extract_frames_by_list_of_frame_numbers(cap, frame_numbers)


def extract_frames_by_ranges_and_number(cap):
    total = int(cap.get(7))
    fps = int(cap.get(5))
    number_of_ranges = int(input("Enter number of extracting ranges: "))
    if number_of_ranges < 1:
        exit(0)

    print(f'Be aware: timecodes in range 0-{int(total / fps)} seconds / 0:00-{int(total / 25 / 60)}:{int(total / 25 % 60)} minutes')
    frame_numbers = []
    for i in range(number_of_ranges):
        while True:
            while True:
                frames_range_beginning = int(enter_one_time_code('Enter beginning timecode: ') * fps)
                if frames_range_beginning < 0 or frames_range_beginning >= total:
                    print('Entered wrong timecode\n')
                    continue
                else:
                    break

            while True:
                frames_range_ending = int(enter_one_time_code('Enter beginning timecode: ') * fps)
                if frames_range_ending < 0 or frames_range_ending >= total:
                    print('Entered wrong timecode\n')
                    continue
                else:
                    break

            if frames_range_beginning > frames_range_ending:
                print('Beginning timecode is after ending one')
                continue
            else:
                break

        while True:
            number_of_extracting_frames_in_range = int(input('Enter number of frames to be extracted from the range: '))
            if number_of_extracting_frames_in_range < 1:
                print('Do not joke, enter normal number of frames\n')
                continue
            else:
                break

        for j in range(frames_range_beginning, frames_range_ending, number_of_extracting_frames_in_range):
            frame_numbers.append(j)

    return extract_frames_by_list_of_frame_numbers(cap, frame_numbers)


def extract_frames_from_video():
    # video_name = input("Enter name of video: ")
    video_name = "winter-saint-petersburg.mp4"

    cap = cv2.VideoCapture(video_name)
    if not cap.isOpened():
        print("Video hasn't opened\n")
        exit(-1)

    list_of_frames = []
    print('Be aware of types: 0 - by timecodes; 1 - by number, 2 - by ranges, 3 - by ranges and numbers')
    type = ExtractingFramesType(int(input("Enter type of extracting : ")))
    if type == ExtractingFramesType.BY_TIME:
        list_of_frames = extract_frames_by_timecodes(cap)

    elif type == ExtractingFramesType.BY_NUM:
        list_of_frames = extract_frames_by_number(cap)

    elif type == ExtractingFramesType.BY_RANGES:
        list_of_frames = extract_frames_by_ranges(cap)

    elif type == ExtractingFramesType.BY_RANGES_AND_NUM:
        list_of_frames = extract_frames_by_ranges_and_number(cap)

    else:
        print('Wrong type number')
        exit(-1)

    return list_of_frames
