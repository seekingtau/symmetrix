# Imports
from PIL import Image

# Opens image symmetry function
def findImgSymmetry(path, type):
    # Open image, find necessary things (width, height, image data)
    img = Image.open(path)

    w, h = img.size

    pixels = list(img.getdata())

    # Sorts pixels
    q = [pixels[n:n+w] for n in range(0, w*h, w)]

    # Setting to 0
    rowCount = 0

    # Lists to contain each half of the image
    imgHalf1 = []
    imgHalf2temp = []
    imgHalf2 = []

    # Calculate the size of half of the matrix based on type specified; splits image into two matrices
    if type == 'h':
        halfPoint = len(q) / 2
        
        for i in q:
            if rowCount < halfPoint:
                imgHalf1.append(i)
                
            if rowCount >= halfPoint:
                imgHalf2temp.append(i)
            
            rowCount +=1
    
    if type == 'v':
        halfPoint = len(q[1]) / 2
        
        # Works by iterating through list to find list; reconstructs on a tuple-by-tuple level (should be improved for best efficiency)
        for x in q:
            iterCount = 0 
            rowList1 = []
            rowList2 = []
            
            for y in x:
                if iterCount < halfPoint:
                    rowList1.append(y)
                    
                if iterCount >= halfPoint:
                    rowList2.append(y)
                    
                iterCount +=1
                
            imgHalf1.append(rowList1)
            imgHalf2temp.append(rowList2)

    # "reverses" image half two -> can now be used to compare directional similarity
    for i in imgHalf2temp:
        imgHalf2.insert(0, i)

    # Starts trying to count errors (just setting stuff to 0)
    errorCount = 0
    tryCount = 0
    rowCount = 0
    runCount = 0

    # Actual image counting engine; iterates through lists of lists to find tuples (overall grid is stored as a list made up of lists)
    for x in imgHalf1:
        tryCount = 0
        for y in x:
            try:
                y2 = imgHalf2[rowCount][tryCount]
            
            # Corrects for odd rows/columns of pixels
            except:
                y2 = (0, 0, 0, -1)
            
            # Below are commented out technical steps; helps you look into it/debug
            
            #print('Half1' + str(y))
            #print('Half2' + str(y2))
        
            #print(tryCount)
            
            # Test if the two pixels overlaid are the same
            if y != y2:
                errorCount +=1
                #print('Error Found!')
            
            tryCount += 1
            
            # Counts number of pixels / 2
            runCount +=1
        
        rowCount += 1
        
    print('Raw number of errors is ' + str(errorCount))
    print('Raw number of possible errors is ' + str(runCount))

    # Divides number of error pixels (non-matching -> non-symmetrical) by number of possible pixels; subtracts that from 1 (perfect symmetrical image would have nothing wrong and therefore a symmetry of 100)
    # then, multiplies by 100 to turn into a percent format
    symmetryVal = (1 - (errorCount / runCount)) * 100

    print('The provided picture is about {}% symmetrical'.format(str(symmetryVal)))
    
# Test w/ 1 image
imagePaths = ['pathshere']

# Simple loop used to put our stuff into practice
for i in imagePaths:
    print('Info for provided path {}:'.format(i))
    
    # Executes image function
    findImgSymmetry(
        i,
        'v'
    )
    
    print('')