import PIL
from PIL import Image
import hashlib
import time
from datetime import datetime
import os
from flask import current_app,url_for
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 保存图片
def save_image(files,photos):
    images = []
    for img in files:
    # if files:
        # 处理文件名
        filename = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()[:10]
        image = photos.save(img,name=filename+'.')
        file_url = photos.url(image)
        url_t = create_thumbnail(image,photos)  # 创建缩略图
        images.append((file_url, url_t))

    return images

# 创建缩略图
def create_thumbnail(image,photos):
    filename, ext = os.path.splitext(image)
    base_width = 300
    img = Image.open(photos.path(image))  # # 从上传集获取path
    if img.mode == "P":
        img = img.convert('RGB')
    if img.size[0] <= 300:  # 如果图片宽度小于300，不作处理
        return photos.url(image)  # 从上传集获取url
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((base_width, h_size))
    img.save(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST']+'/thumb', filename+'_t' + ext))

    return url_for('uploaded_file',filename=filename + '_t' + ext)