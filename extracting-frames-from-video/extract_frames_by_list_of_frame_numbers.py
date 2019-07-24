import cv2


def extract_frames_by_list_of_frame_numbers(captured, frame_numbers):
    frame_numbers = list(dict.fromkeys(frame_numbers))
    frame_numbers.sort()
    print('\nVideo processing...')

    frame_numbers.sort()
    total = int(captured.get(7))
    list_of_frames = []
    counter = 0
    while counter < total:
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
            raise RuntimeError("Wrong try of reading video while extracting frames")

        if counter == frame_numbers[len(list_of_frames)]:
            list_of_frames.append(frame)
            if len(list_of_frames) == len(frame_numbers):
                break

        counter += 1

    print('Video has been processed')
    return list_of_frames
