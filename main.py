import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont

# Get the current working directory
cwd = os.getcwd()

# Join the current working directory with the desired directory
save_path = os.path.join(cwd, "C:/Excel")

# Read the excel file
df = pd.read_excel('C:/Excel/file.xlsx', header=0)

# Print the dataframe
print(df)

for index, row in df.iterrows():
    title = row['title']
    font_path = row['font']
    size = tuple(map(int, row['size'].split(',')))
    color = row['color']
    if color == "transparent" or color == "":
        img = Image.new('RGBA', size, (255,255,255,0))
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(font_path, 300)
        text_size = d.textsize(title, font=fnt)
        text_x = (size[0] - text_size[0]) / 2
        text_y = (size[1] - text_size[1]) / 2
        d.text((text_x, text_y), title, font=fnt, fill=(255,255,255,255))
        img.save(f'{save_path}/{title}.png', "PNG")
    else:
        img = Image.new('RGB', size, color)
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(font_path, 300)
        text_size = d.textsize(title, font=fnt)
        text_x = (size[0] - text_size[0]) / 2
        text_y = (size[1] - text_size[1]) / 2
        d.text((text_x, text_y), title, font=fnt, fill=(255,255,255,255))
        img.save(f'{save_path}/{title}.png', "PNG")
    print(f'saving image {title}.png')
    img.save(f'{save_path}/{title}.png')
    print(f'{title}.png saved successfully')

print("Script finished executing")