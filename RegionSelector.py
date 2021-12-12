import cv2
import random

path_query = 'Query/Modele Facture.jpg'
scale = 0.25
circles = []
counter = 0
counter2 = 0
point1 = []
point2 = []
myPoints = []
myColor = []
'''
[[(92, 1408), (1212, 1544), 'text', 'description 1'], [(92, 1552), (1220, 1672), 'text', 'description 2'], [(92, 1676), (1216, 1812), 'text', 'description 3'], [(88, 1804), (1216, 1936), 'text', 'description 4'], [(92, 1936), (1212, 2068), 'text', 'description 5'], [(88, 2080), (1220, 2200), 'text', 'description 6'], [(96, 2204), (1212, 2336), 'text', 'description 7'], [(92, 2340), (1212, 2472), 'text', 'description 8']]
[[(1216, 1412), (1516, 1548), 'text', 'quantité 1'], [(1216, 1544), (1512, 1680), 'text', 'quantité 2'], [(1216, 1676), (1516, 1812), 'text', 'quantité 3'], [(1216, 1816), (1516, 1944), 'text', 'quantité 4 '], [(1216, 1940), (1516, 2080), 'text', 'quantité 5 '], [(1216, 2072), (1520, 2204), 'text', 'quantité 6'], [(1212, 2200), (1516, 2332), 'text', 'quantité 7'], [(1220, 2340), (1512, 2464), 'text', 'quantité 8']]
[[(1516, 1408), (1964, 1548), 'text', 'prix uni HT 1'], [(1512, 1544), (1964, 1676), 'text', 'prix uni HT 2'], [(1520, 1672), (1964, 1808), 'text', 'prix uni HT 3'], [(1516, 1808), (1960, 1940), 'text', 'prix uni HT 4'], [(1516, 1944), (1964, 2076), 'text', 'prix uni HT 5'], [(1512, 2072), (1960, 2200), 'text', 'prix uni HT 6'], [(1512, 2204), (1960, 2336), 'text', 'prix uni HT 7'], [(1512, 2344), (1964, 2460), 'text', 'prix uni HT 8']]
[[(1964, 1416), (2464, 1548), 'text', 'total ht 1'], [(1968, 1544), (2464, 1672), 'text', 'total ht 2'], [(1964, 1676), (2464, 1808), 'text', 'total ht 3'], [(1968, 1812), (2464, 1940), 'text', 'total ht 4'], [(1968, 1940), (2468, 2076), 'text', 'total ht 5'], [(1964, 2072), (2464, 2204), 'text', 'total ht 6'], [(1964, 2200), (2468, 2336), 'text', 'total ht 7'], [(1960, 2340), (2464, 2464), 'text', 'total ht 8']]
[[(100, 2572), (1456, 3136), 'signature', 'remarque/signature'], [(1844, 2504), (2548, 2684), 'text', 'total ht'], [(1844, 2708), (2540, 2852), 'text', 'tva'], [(1964, 2872), (2464, 3000), 'text', 'total ttc']]
[[(508, 936), (1328, 1076), 'text', 'nom de la societe'], [(340, 1060), (1344, 1276), 'text', 'adresse'], [(1764, 940), [(1768, 936), (2540, 1040), 'text', 'telephone'], [(1672, 1048), (2540, 1248), 'text', 'email']]
[[(1936, 400), (2524, 504), 'text', 'date de création'], [(1988, 556), (2532, 688), 'text', 'date limite de paiement'], [(1924, 196), (2528, 380), 'text', 'num facture']]

'''
def mousePoints(event,x,y,flags,params):
    global counter,point1,point2,counter2,circles,myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter == 0 :
            point1 = int(x//scale),int(y//scale)
            counter =+1
            myColor = (random.randint(0,2)*200, random.randint(0,2)*200,random.randint(0,2)*200)
        elif counter == 1 :
            point2 = int(x//scale),int(y//scale)
            type = input('Enter Type')
            name = input ('Enter Name')
            myPoints.append([point1,point2,type,name])
            counter=0
        circles.append([x,y,myColor])
        counter2 += 1

img = cv2.imread(path_query)
img = cv2.resize(img,(0,0), None, scale, scale)

while True :
    #to display points
    for x,y,color in circles :
        cv2.circle(img,(x,y),3,color,cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(myPoints)
        break

