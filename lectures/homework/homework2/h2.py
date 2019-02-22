from PIL import Image 

def new_pixels():
    final_pixels = []
    im1 = Image.open('1.png')
    im2 = Image.open('2.png')
    im3 = Image.open('3.png')
    im4 = Image.open('4.png')
    im5 = Image.open('5.png')
    im6 = Image.open('6.png')
    im7 = Image.open('7.png')
    im8 = Image.open('8.png')
    im9 = Image.open('9.png')
    im10 = Image.open('10.png')
    im11 = Image.open('11.png')
    
    width, height = im1.size
    pixels = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11]
    for h in range(height):
        for w in range(width):
            f_pi = []
            for image in pixels:
                f_pi.append(image.getpixel((w, h)))
            f_pi.sort()
            img_row.append(f_pi[len(f_pi)//2])

    final_image = Image.new('RGB', (width, height))
    final_image.putdata(img_row)
    final_image.save('nofox.png')

new_pixels()
