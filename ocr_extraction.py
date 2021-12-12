import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import signature_extractor as se

detector = se.SignatureDetector()


def features_ORB(path_query,img_path) :
    imgQ = cv2.imread(path_query)
    per = 25
    h, w, c = imgQ.shape
    # imgQ = cv2.resize(imgQ,(w//3,h//3)

    orb = cv2.ORB_create(10000)

    kp1, des1 = orb.detectAndCompute(imgQ, None)

    img = cv2.imread(img_path)
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.match(des2, des1)
    matches = sorted(matches, key=lambda x: x.distance)
    good = matches[:int(len(matches) * (per / 100))]
    imgMatch = cv2.drawMatches(img, kp2, imgQ, kp1, good[:100], None, flags=2)
    srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)
    imgScan = cv2.warpPerspective(img, M, (w, h))
    # imgScan = cv2.resize(imgScan,(w//3,h//3))
    # cv2.imshow(img_path,imgScan)
    return (imgScan,imgQ)

def extraction(roi,imgScan,imgQ) :
    # imgScan = cv2.imread(path + "/" + img_path)
    imgShow = imgScan.copy()
    imgMask = np.zeros_like(imgShow)
    myData = []

    print(f'################ Extracting Data from Form ############"')
    for x, r in enumerate(roi):
        cv2.rectangle(imgMask, (r[0][0], r[0][1]), (r[1][0], r[1][1]), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(imgQ, (r[0][0], r[0][1]), (r[1][0], r[1][1]), (0, 255, 0), cv2.FILLED)

        imgShow = cv2.addWeighted(imgShow, 0.99, imgMask, 0.1, 0)

        imgCrop = imgScan[r[0][1]:r[1][1], r[0][0]:r[1][0]]

        # cv2.imshow(str(x),imgCrop)

        if r[2] == 'text':
            print(f'{r[3]} : {pytesseract.image_to_string(imgCrop)}')
            myData.append(pytesseract.image_to_string(imgCrop))
        if r[2] == 'digit':
            print(
                f'{r[3]} : {pytesseract.image_to_string(imgCrop, config="--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789")}')
            myData.append(
                pytesseract.image_to_string(imgCrop, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
        if r[2] == 'signature' :
            if (detector.traitement(cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY ),'signature image/')):
                print(f'{r[3]} :ok')
            else:
                print(f'{r[3]} :ok')
        if(r[2]!='signature'):
            cv2.putText(imgShow, str(myData[x]), (r[0][0], r[0][1]), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 255), 4)
    return myData

def write_csv (myData):
    x = 0
    with open('DataOutput.csv', 'a+') as f:
        f.write(
            'num facture, date de creation, date limite de paiement,nom societe,adresse,telephone,email,total ht,total tva,total ttc')
        f.write('\n')
        for data in myData:
            if x == 10:
                f.write('\n')
                f.write('description,quantite,prix unitaire,total HT')
                f.write('\n')
                f.write((str(data) + ','))
            elif (x == 14) or (x == 18) or (x == 22) or (x == 26) or (x == 30) or (x == 34) or (x == 38):
                f.write('\n')
                f.write((str(data) + ','))
            else:
                f.write((str(data) + ','))
            x += 1

        f.write('\n')


