from extract_frames_by_list_of_frame_numbers import extract_frames_by_list_of_frame_numbers
from extracting_by_timecode import enter_one_time_code


def extract_frames_by_ranges_and_number(cap):
    total = int(cap.get(7))
    fps = int(cap.get(5))
    number_of_ranges = int(input("Enter number of extracting ranges: "))
    if number_of_ranges < 1:
        exit(0)

    print('\nBe aware: intersecting ranges are grouping into one,')
    print('\tbut gives max(n,m)_n+m frames, which numbers depend on starting ranges')
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
                print('Beginning timecode is after ending one')
                continue
            else:
                break

        if frames_range_beginning == frames_range_ending:
            print('Number of extracting frames is chosen automatically = 1')
            frame_numbers.append(frames_range_beginning)
        else:
            max_number_of_frames = frames_range_ending - frames_range_beginning
            print(f'Avaliable number of frames: 1-{max_number_of_frames}')
            while True:
                number_of_extracting_frames_in_range = int(input('Enter number of extracting frames from the range: '))
                if number_of_extracting_frames_in_range < 1 or number_of_extracting_frames_in_range > max_number_of_frames:
                    print('Do not joke, enter normal number of frames. Or given value > fps * secs\n')
                    continue

                elif number_of_extracting_frames_in_range == max_number_of_frames:
                    for h in range(frames_range_beginning, frames_range_ending):
                        frame_numbers.append(h)

                else:
                    step = (frames_range_ending - frames_range_beginning) / (number_of_extracting_frames_in_range + 2)
                    frame_counter = frames_range_beginning
                    counter = 0
                    while int(frame_counter) <= frames_range_ending and counter < number_of_extracting_frames_in_range:
                        frame_counter += step
                        frame_numbers.append(int(frame_counter))
                        counter += 1
                break
        print()

    return extract_frames_by_list_of_frame_numbers(cap, frame_numbers)
