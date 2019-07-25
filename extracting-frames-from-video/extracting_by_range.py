from extract_frames_by_list_of_frame_numbers import extract_frames_by_list_of_frame_numbers
from extracting_by_timecode import enter_one_time_code


def extract_frames_by_ranges(cap):
    total = int(cap.get(7))
    fps = int(cap.get(5))
    number_of_ranges = int(input("Enter number of extracting ranges: "))
    if number_of_ranges < 1:
        exit(0)

    print('\nBe aware: intersecting ranges are grouping into one')
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
                frames_range_ending = int(enter_one_time_code('Enter ending timecode: ') * fps)
                if frames_range_ending < 0 or frames_range_ending >= total:
                    print('Entered wrong timecode\n')
                    continue
                else:
                    break

            if frames_range_beginning > frames_range_ending:
                print('Beginning timecode is after ending one\n')
                continue
            else:
                break

        for j in range(frames_range_beginning, frames_range_ending + 1):
            frame_numbers.append(j)
        print()

    return extract_frames_by_list_of_frame_numbers(cap, frame_numbers)
