import LCD_1in44
import LCD_Config

from PIL import Image,ImageDraw,ImageFont,ImageColor

#try:
def main():
    LCD = LCD_1in44.LCD()

    print("**********Init LCD**********")
    Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()
    image = Image.new("RGB", (LCD.width, LCD.height), "WHITE")
    draw = ImageDraw.Draw(image)
    print("***draw text")
    draw.text((33, 22), 'WaveShare ', fill = "BLUE")
    draw.text((32, 36), 'Electronic ', fill = "BLUE")
    draw.text((28, 48), '1.44inch LCD ', fill = "BLUE")


if __name__ == '__main__':
    main()