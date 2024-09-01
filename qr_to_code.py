from PIL import Image

def qr_to_custom_string(image_path, qr_size=37, output_path=None):
    # 打开图像并将其转换为灰度图像
    img = Image.open(image_path).convert('L')
    
    # 确保图像被调整为指定的二维码大小
    img = img.resize((qr_size, qr_size))
    
    # 初始化一个空的字符串以保存结果
    custom_string = ''
    
    # 遍历图像的每个像素
    for y in range(qr_size):
        for x in range(qr_size):
            # 获取像素的灰度值
            pixel_value = img.getpixel((x, y))
            
            # 根据像素值确定符号
            if pixel_value < 128:
                custom_string += '#'
            elif 128 <= pixel_value < 200:
                custom_string += '?'
            else:
                custom_string += '_'
        
        # 每行末尾添加换行符
        custom_string += '\n'
    
    # 如果指定了输出路径，则将结果保存到文件
    if output_path:
        with open(output_path, 'w') as f:
            f.write(custom_string)
    
    return custom_string

# 获取用户输入
qr_size = int(input("请输入二维码的大小（如37表示37x37）："))
image_path = input("请输入二维码图像文件的名字（例如：qr.png）：")

# 生成并打印二维码字符图案
binary_qr = qr_to_custom_string(image_path, qr_size, 'qr_code.txt')
print(binary_qr)
