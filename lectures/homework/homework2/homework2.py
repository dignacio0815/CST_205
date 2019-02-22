from PIL import Image
from glob import glob 


im1 = Image.open("1.png")

im3 =  glob("*3.png*"))
im4 = (glob("*4.png*"))
im5 = (glob("*5.png*"))
im6 = (glob("*6.png*"))
im7 = (glob("*7.png*"))
im8 = (glob("*8.png*"))
im9 = (glob("*9.png*"))
im10 = (glob("*10.png*"))
im11 = (glob("*11.png*"))



def get_rgbs(pictures): 
    for f in pictures: 
        im = Image.open(f)
        pix_list = list(im.getdata())
        '''
        rgb_im = im.convert('RGB')
        width, height = im.size
        for x in range(width):
            for y in range(height):
                pix_list.append((rgb_im.getpixel((x,y))))
    return pix_list
    '''
    return pix_list

def compare_pixels():
    final_pixels = []

    #im1 is now a list of rgb tuples
    im1 = get_rgbs(glob("*1.png*"))
    #print(im1)
    
    im2 = get_rgbs(glob("*2.png*"))
    im3 = get_rgbs(glob("*3.png*"))
    im4 = get_rgbs(glob("*4.png*"))
    im5 = get_rgbs(glob("*5.png*"))
    im6 = get_rgbs(glob("*6.png*"))
    im7 = get_rgbs(glob("*7.png*"))
    im8 = get_rgbs(glob("*8.png*"))
    im9 = get_rgbs(glob("*9.png*"))
    im10 = get_rgbs(glob("*10.png*"))
    im11 = get_rgbs(glob("*11.png*"))
  
    pics = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11]
    for p in pics[0:-1]:
        for p2 in pics[1:]:
            if p != p2:
                final_pixels.append(p2)
            else:
                final_pixels.append(p)
                
               # p2.getpixel((x,y))
               # total_image.putpixel((x,y))
    new_image = Image.new('RGB', [1452, 1028])
    new_image.putdata(final_pixels)
    im2.show()
    
compare_pixels()
