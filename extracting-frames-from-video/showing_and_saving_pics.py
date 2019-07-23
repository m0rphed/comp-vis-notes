import cv2
import copy


def show_and_save_pics(frames, keypoints_and_descriptors):
    should_show_pics = bool(int(input("\nShow made pics? (0 - no; 1 - yes): ")))
    should_save_pics = bool(int(input("Save made pics? (0 - no; 1 - yes): ")))
    if should_show_pics or should_save_pics:
        for i in range(len(frames)):
            keypoints, descriptors = keypoints_and_descriptors[i]
            img = copy.deepcopy(frames[i])
            img = cv2.drawKeypoints(img, keypoints, img)

            if should_save_pics:
                cv2.imwrite(f'./made_pics/img{i}.jpg', frames[i])
                cv2.imwrite(f'./made_pics/img{i}_sifted.jpg', img)

            if should_show_pics:
                cv2.imshow('Sifted picture', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
