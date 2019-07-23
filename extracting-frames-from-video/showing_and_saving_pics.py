import cv2


def show_and_save_pics(frames, keypoints_and_descriptors):
    should_show_pics = bool(int(input("Show made pics? (0 - no; 1 - yes): ")))
    should_save_pics = bool(int(input("Save made pics? (0 - no; 1 - yes): ")))
    if should_show_pics or should_save_pics:
        for i in range(len(frames)):
            keypoints, descriptors = keypoints_and_descriptors[i]
            sifted_img = cv2.drawKeypoints(frames[i], keypoints, frames[i])

            if should_save_pics:
                cv2.imwrite(f'./Made pics/img{i}.jpg', frames[i])
                cv2.imwrite(f'./Made pics/img{i}_sifted.jpg', sifted_img)

            if should_show_pics:
                cv2.imshow('Sifted picture', sifted_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
