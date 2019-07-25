def extract_frames_by_list_of_frame_numbers(captured, frame_numbers):
    frame_numbers = list(dict.fromkeys(frame_numbers))
    frame_numbers.sort()
    print('\nVideo processing...')

    frame_numbers.sort()
    total = int(captured.get(7))
    list_of_frames = []
    counter = 0
    while counter < total:
        if not captured.grab():
            raise RuntimeError("Wrong try of grabing video while extracting frames")

        if counter == frame_numbers[len(list_of_frames)]:
            is_read_right, frame = captured.retrieve()
            if not is_read_right:
                raise RuntimeError("Wrong try of reading video while extracting frames")

            list_of_frames.append(frame)
            if len(list_of_frames) == len(frame_numbers):
                break

        counter += 1

    print('Video has been processed')
    return list_of_frames
