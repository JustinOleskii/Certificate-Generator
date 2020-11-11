from PIL import Image, ImageFont, ImageDraw
import os

print("Certificate Generator v1.0\nAuthor: JustinOleskii\n\n")

fileName = input("Enter the name of your base image (with extension)\nExample: sample.png\nEnter: ")
writingList = input("Enter the name of file containing names to write (with extension): ")
fontName = input("Enter the name of the font you want to use (with extension)\nEnter: ")
fontSize = int(input("Enter font size in pts: "))
distY = input("Enter Y coordinate: ")

names = open(writingList, 'r')
imgFont = ImageFont.truetype(fontName, fontSize)

count = 1
content = names.readlines()
size = len(content)

for line in content:
    certText = line.upper()
    
    img = Image.open(fileName)
    imgWidth = img.width

    editableImg = ImageDraw.Draw(img)
    w, h = editableImg.textsize(certText, imgFont)
    editableImg.text(((imgWidth - w) / 2, distY), certText, (255, 255, 255), font=imgFont)
    
    img.save('output/result.png')
    os.rename('output/result.png', f'output/{certText.strip()}.png')
    
    img.close()
    print(f'{count} of {size} processed.')
    count += 1

print("\nQueue ended. Program terminating...")