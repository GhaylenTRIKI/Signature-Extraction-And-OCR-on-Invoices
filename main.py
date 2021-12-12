import document_scanner as dc
import ocr_extraction as oe

path_query = 'Query/Modele Facture.jpg'
img_path = 'After_scan/Image_after_scan.jpg' ######### img_path hia taswira supposé ba3d scan ################
img_nonscan = 'Test_images/5.jpg' ##################### img_nonscan hia taswira avant scan ################


roi = [
        [(1924, 196), (2528, 380), 'text', 'num facture'], [(1936, 390), (2524, 550), 'text', 'date de creation'],[(1988, 560), (2532, 720), 'text', 'date limite de paiement'],
        [(500, 936), (1328, 1070), 'text', 'nom de la societe'], [(320, 1080), (1344, 1276), 'text', 'adresse'],[(1730, 904), (2536, 1060), 'text', 'telephone'], [(1640, 1070), (2528, 1280), 'text', 'email'],
        [(1844, 2504), (2548, 2684), 'text', 'total ht'], [(1844, 2708), (2540, 2852), 'text', 'tva'], [(1964, 2872), (2464, 3000), 'text', 'total ttc'],
        [(92, 1408), (1212, 1544), 'text', 'description 1'],[(1228, 1420), (1504, 1532), 'digit', 'quantite 1'],[(1516, 1408), (1964, 1548), 'text', 'prix uni HT 1'],[(1964, 1416), (2464, 1548), 'text', 'total ht 1'],
        [(92, 1552), (1220, 1672), 'text', 'description 2'],[(1232, 1556), (1504, 1664), 'digit', 'quantite 2'],[(1512, 1544), (1964, 1676), 'text', 'prix uni HT 2'],[(1968, 1544), (2464, 1672), 'text', 'total ht 2'],
        [(92, 1676), (1216, 1804), 'text', 'description 3'],[(1224, 1684), (1504, 1800), 'digit', 'quantite 3'],[(1520, 1672), (1964, 1808), 'text', 'prix uni HT 3'],[(1964, 1676), (2464, 1808), 'text', 'total ht 3'],
        [(88, 1812), (1216, 1936), 'text', 'description 4'],[(1224, 1820), (1508, 1928), 'digit', 'quantite 4'],[(1516, 1808), (1960, 1940), 'text', 'prix uni HT 4'],[(1968, 1812), (2464, 1940), 'text', 'total ht 4'],
        [(92, 1936), (1212, 2068), 'text', 'description 5'],[(1224, 1948), (1500, 2068), 'digit', 'quantite 5'],[(1516, 1944), (1964, 2076), 'text', 'prix uni HT 5'],[(1968, 1940), (2468, 2076), 'text', 'total ht 5'],
        [(88, 2080), (1220, 2200), 'text', 'description 6'], [(1224, 2088), (1504, 2196), 'digit', 'quantite 6'], [(1512, 2072), (1960, 2200), 'text', 'prix uni HT 6'],  [(1964, 2072), (2464, 2204), 'text', 'total ht 6'],
        [(96, 2204), (1212, 2336), 'text', 'description 7'], [(1224, 2220), (1504, 2328), 'digit', 'quantite 7'],[(1512, 2204), (1960, 2336), 'text', 'prix uni HT 7'], [(1964, 2200), (2468, 2336), 'text', 'total ht 7'],
        [(92, 2340), (1212, 2472), 'text', 'description 8'],[(1228, 2356), (1500, 2456), 'digit', 'quantite 8'],[(1512, 2344), (1964, 2460), 'text', 'prix uni HT 8'],[(1960, 2340), (2464, 2464), 'text', 'total ht 8'],
        [(25, 2572), (1500, 3136), 'signature', 'remarque/signature']
]


dc.DocScanner(img_nonscan)
imgscan,imgq = oe.features_ORB(path_query,img_path)
data = oe.extraction(roi,imgscan,imgq)
oe.write_csv(data)