import cv2
import matplotlib.pyplot as plt
from skimage import measure, morphology
from skimage.color import label2rgb
from skimage.measure import regionprops

class SignatureDetector():
    #def __init__(self):

    def traitement(self,img,path_extractor=''):
        the_biggest_component = 0
        total_area = 0
        counter = 0
        average = 0.0

        img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
        # Extract Blobs
        blobs = img > img.mean()
        blobs_labels = measure.label(blobs, background=1)  # exp: blob-labels=8 pour le 8eme regroupement de pixel noir
        #image_label_overlay = label2rgb(blobs_labels,
                                        #image=img)  # affecter une couleur a chaque regroupement de pixel noir
        #plt.imshow(image_label_overlay)
        # Area of Text


        for region in regionprops(blobs_labels):
            if (region.area > 10):
                total_area = total_area + region.area
                counter = counter + 1
            if (region.area >= 250):
                if (region.area > the_biggest_component):
                    the_biggest_component = region.area

        print("the_biggest_component: " + str(the_biggest_component))

        b = morphology.remove_small_objects(blobs_labels, the_biggest_component)

        plt.imsave(path_extractor+'pre_version.png', b)

        # read the pre-version
        img2 = cv2.imread(path_extractor+'pre_version.png', 0)
        # ensure binary
        img2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        if (the_biggest_component > 1500):
            cv2.imshow("img2", img2)
            return True
        else:
            return False






def main():
    img = cv2.imread('test.jpg ', 0)
    #img = cv2.bitwise_not(img)
    cv2.imshow("img",img)
    detector = SignatureDetector()
    if (detector.traitement(img,'signature image/')) : print("ok")
    else : print("non ok")
    cv2.waitKey(0)

if __name__ == "__main__":
    main()










