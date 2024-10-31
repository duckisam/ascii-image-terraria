from PIL import Image as img
import io

class Ascii_Png_converter:
    
    def create_ascii_from_bytes(bytes, autoPrint, lAmount= 1):
        
        ascii_image = ''
        try:
            image = img.open(io.BytesIO(bytes))
        except:
            if autoPrint:
                print('not able to load bytes')
            else:
                return 'not able to load bytes'
        width, height = image.size
        
        for y in range(height):  # Always process rows first to maintain image structure
            for x in range(width):
                for i in range(lAmount):
                    pixels_rgb = image.convert('RGB')
                    r,g,b =pixels_rgb.getpixel((x,y))
                    
                    simga = (r+g+b)//3
                    
                    chars = '█'
                    if simga == 0:
                        the_char = ' '
                    else:
                        the_char = chars[int(simga/255 * (len(chars) - 1))]
                    
                    ascii_image += f"\033[;38;2;{r + 20};{g + 20};{b + 20}m{the_char}\033[0m"
            ascii_image += '\n'
        
                
                
                # # Assuming you want the RGB values
                # r, g, b = pixel[:3]  # Only take the first 3 values if it's RGBA or more
                
                # # Here, you can manipulate ascii_image as needed based on the pixel values
                # #ascii_image += f'{r},{g},{b} '  # Example concatenation, adjust as needed
                # print(r, g, b)
        
        if not autoPrint:
            return ascii_image
        else:
            print(ascii_image)