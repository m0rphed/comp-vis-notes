from extract_frames_by_list_of_frame_numbers import extract_frames_by_list_of_frame_numbers


def extract_frames_by_number(cap):
    number_of_frames = int(input("Enter number of extracting frames: "))
    if number_of_frames < 1:
        exit(0)

    total = int(cap.get(7))
    step = int(total / (number_of_frames + 1))
    if step == 0:
        step = 1

    frame_numbers = []

    counter = step
    for i in range(number_of_frames):
        if counter >= total:
            break
        frame_numbers.append(counter)
        counter += step

    return extract_frames_by_list_of_frame_numbers(cap, frame_numbers)
