from extract_frames_by_list_of_frame_numbers import extract_frames_by_list_of_frame_numbers


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

    print(f'\nBe aware: timecodes in range 0-{0} seconds / 0:00-{1}:{2} minutes'.format(int(total / fps),
                                                                                        int(total / 25 / 60),
                                                                                        int(total / 25 % 60)))
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