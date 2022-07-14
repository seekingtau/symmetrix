# Symmetrix
![symmetrix(1)](https://user-images.githubusercontent.com/61752416/179073468-1ff6e40a-3802-4577-b1e5-887f183274f7.png)

Quantify symmetry! Symmetrix is a script (and soon-to-be application) inspired by a friend of mine, @e007k, to quantify symmetry.

## How to use it
*This is until a frontend is developed. I'm working on that right now.*
1. Add the path to your image under "imagePaths (line 108).
2. Under findImgSymmetry, select 'v' or 'h' for vertical or horizontal symmetry, respectively.
3. Run the script!

## How it works
1. First, the script opens the image and extracts the data (RGB values).
2. Then, the values are divided either horizontally (cut the list in half) or vertically (iterates through list to find half, then seperates the list along the halfway point).
3. Third, the second half is rewritten from back to front, to the effect of "mirroring" the half, so it can be compared directly to the first half.
4. The program then compares each pixel in a given position in both and determines if the two pixels are the same; whether or not they are is counted.
5. A formula is applied to determine symmetry: 
<html>1 - (p<sub>dif</sub>/p<sub>total</sub>)</html>
