from PIL import Image      
from PIL import ImageFilter
from PIL import ImageEnhance
          #підключення модуля
with Image.open('nikow.jpg') as pic_original:
    print('Розмір:', pic_original.size)
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode)
    pic_original.show()


    pic_gray = pic_original.convert('L')
    pic_gray.save('nikow_gray.jpg') #чорно біле зображення
    pic_gray.show()



    pic_blured = pic_gray.filter(ImageFilter.BLUR)  #розмите зображення
    pic_blured.save('nikow_blured.jpg')
    pic_blured.show()
  
    pic_up = pic_original.transpose(Image.ROTATE_180) #повертання
    pic_up.save('nikow_up.jpg')
    pic_up.show()

    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT) #відзеркалення
    pic_mirrow.save('nikow_mirrow.jpg')
    pic_up.show

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(2.3)
    pic_contrast.save('nikow_contr.jpg')
    pic_contrast.show