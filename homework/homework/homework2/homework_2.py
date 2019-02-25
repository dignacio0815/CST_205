'''
File Name: h2.py
Name: Denize Ignacio
Partner: Jessica Politron
Date: 2/25/19
Description: Contains one function that will return a new image holding the original contents without the fox. 
             Including: new_pixels(). 
             The function will take in 11 images. The function will then take 11 pixels each time where one pixel
             comes from each photo each time. The images, after instantiated, are stored into their own list. The 
             list is then accessed and the pixels are appended into a seperate list, sorted, than the median pixel 
             is appended into my 'final_pixels' list where I instantiate a new image and put the data there to display
             the new image.
'''

from PIL import Image #Importing Pillow's Image class
import glob #Importing Glob's glob class

def new_pixels(): #Function defintion 
    final_pixels = [] #List declaration where the final pixels will be stored later
    pixels = [] #List to hold all image instantiations
    img_files = glob.glob("images/*.png") #Retrieving all images using glob
    for pic in img_files: #Iterating through img_files to append the img data into pixels
        pixels.append(Image.open(pic))

    width, height = pixels[0].size #Using .size method to retrieve the width and height so the function can navigate through the images using an (x, y) system
    #pixels = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11] #Created a list for easier retrieval of images 
    for h in range(height): #Iterating through width and height to get the pixels
        for w in range(width):
            tempoaray_pixel = [] #Tempoary list where I can appened the pixels, sort them, return the median pixel, clear the array, and reapeat for all pixels. 
            for image in pixels: #Grabbing  individual images from my pixels list containing the 11 images
                tempoaray_pixel.append(image.getpixel((w, h))) #Appeneding 11 pixels at a time to tempoaray list
            tempoaray_pixel.sort() #Sorting the 11 pixels appended to tempoaray list
            final_pixels.append(tempoaray_pixel[len(tempoaray_pixel)//2]) #Appending the median pixel from my tempoary pixel list into my final list filled with median pixels

    final_image = Image.new('RGB', (width, height)) #Instantiating a new image
    final_image.putdata(final_pixels) #Putting the pixels of my final pixel list to the image
    final_image.save('no_fox.png') #Saving the image where the fox will not be present
    final_image.show() #Showing the new image I saved
new_pixels() #Calling my funuction 
