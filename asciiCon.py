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
        for y in range(height):      
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

# Ascii_Png_converter.create_ascii_from_bytes(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00*\x00\x00\x00(\x04\x03\x00\x00\x00z%uc\x00\x00\x00$PLTE\x00\x00\x00\xff\xe2\xd9\xf4\xb0\xff\xeb\xa6\x87\xdba\xff\xcd\x86G\xa5\x00\xeci(\xa5n;\x1dR \x7fI&\x10-\x12?\xdc\xa8\x10k\x00\x00\x00\x01tRNS\x00@\xe6\xd8f\x00\x00\x00dIDATx\xda\xb5\xce1\x15\x80@\x10\x03\xd1X\xc0\x02\x16\xd6\x02\x16\xd6\x02\x16\xb0\x10\x0bga,\xac9\x04\xd0\x84\xe2R\xfe7E\xf4\xd9\xccZ\xa12\xf7\x19*\xe5\xeb\x99Hi?\x9eL]v\xa1L\x8fj\x14)m\xa3D\xa1\x91\x94(\xd5(S\x17\x84\xea\xc3\x92\x02\xdd\x94BY\xa9\x16\xda\xa04\n4N\xff\x1f\x00\x85\xfa\x02^\xaaR\xe1\xe7[OC\x00\x00\x00\x00IEND\xaeB`\x82', True)
