import cv2
import copy


def show_and_save_pics(frames, keypoints_and_descriptors):
    should_show_pics = int(input("\nShow made pics? (0 - no; 1 - yes): "))
    should_save_pics = int(input("Save made pics? (0 - no; 1 - yes): "))
    if should_show_pics or should_save_pics:
        for i in enumerate(frames):
            keypoints, descriptors = keypoints_and_descriptors[i]
            img_sifted = copy.deepcopy(frames[i])
            img_sifted = cv2.drawKeypoints(img_sifted, keypoints, img_sifted)

            if should_save_pics:
                cv2.imwrite('./made_pics/img{}.jpg'.format(i), frames[i])
                cv2.imwrite('./made_pics/img{}_sifted.jpg'.format(i), img_sifted)

            if should_show_pics:
                cv2.imshow('Sifted picture', img_sifted)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
