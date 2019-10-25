#install the Pillow package if the code doesn't run
from PIL import Image
imgname = input("Enter the filename of the image.")
im = Image.open(imgname) # Can be many different formats.
pix = im.load()
thing = float(input("Enter how many shades of colour you want for red,green and blue"))
values = [0]
section = 0
pixels = 0
for g in range(round(int(thing),0) - 1):
  values.append(section + int(255/thing))
  section += int(thing)
if 255 % thing != 0:
  values.append(255)
def checkred():
  global values
  for h in range(len(values) - 1):
    if pix[x,y][0] != 0:
      if pix[x,y][0] > values[h] and pix[x,y][0] < values[h + 1]:
        pix[x,y] = (values[h + 1],pix[x,y][1],pix[x,y][2])

def checkgreen():
  global values
  for h in range(len(values) - 1):
    if pix[x,y][1] != 0:
      if pix[x,y][1] > values[h] and pix[x,y][1] < values[h + 1]:
        pix[x,y] = (pix[x,y][0],values[h + 1],pix[x,y][2])

def checkblue():
  global values
  for h in range(len(values) - 1):
    if pix[x,y][2] != 0:
      if pix[x,y][2] > values[h] and pix[x,y][2] < values[h + 1]:
        pix[x,y] = (pix[x,y][0],pix[x,y][1],values[h + 1])

print("Compressing image...")
for y in range(im.size[1]):
  for x in range(im.size[0]):
    checkred()
    checkgreen()
    checkblue()
    '''pixels += 1
    if pixels == im.size[0] * im.size[1] / 10*1:
      print("10% completed")
    if pixels == im.size[0] * im.size[1] / 10*2:
      print("20% completed")
    if pixels == im.size[0] * im.size[1] / 10*3:
      print("30% completed")
    if pixels == im.size[0] * im.size[1] / 10*4:
      print("40% completed")
    if pixels == im.size[0] * im.size[1] / 10*5:
      print("50% completed")
    if pixels == im.size[0] * im.size[1] / 10*6:
      print("60% completed")
    if pixels == im.size[0] * im.size[1] / 10*7:
      print("70% completed")
    if pixels == im.size[0] * im.size[1] / 10*8:
      print("80% completed")
    if pixels == im.size[0] * im.size[1] / 10*9:
      print("90% completed")
    if pixels == im.size[0] * im.size[1] / 10*10:
      print("100% completed")'''
print("Compression finished.")
print("Image size: " , im.size[0] * im.size[1] , " pixels.")
im.save('modified-image.jpg')
