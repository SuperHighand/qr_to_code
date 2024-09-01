# qr_to_code

图片转二维码字符串 

**因为图片识别的原因 这里需要把二维码的白边给剪切掉**

如

![](https://button-note.oss-cn-shanghai.aliyuncs.com/img/image-20240901210802455.png)

需要变成没有白边的样子

![image-20240901212017661](https://button-note.oss-cn-shanghai.aliyuncs.com/img/image-20240901212017661.png)

# 工具使用

需要手动计算二维码的码元

如

```
Version 1: 21x21
Version 2: 25x25
Version 3: 29x29
Version 4: 33x33
Version 5: 37x37
Version 10: 57x57
Version 20: 97x97
Version 40: 177x177
```

python3 qr_to_code.py

![image-20240901211153407](https://button-note.oss-cn-shanghai.aliyuncs.com/img/image-20240901211153407.png)

生成的字符串会写入qr_code.txt中

将生成的qr_code.txt导入qrazybox

https://merri.cx/qrazybox/

![image-20240901211606549](https://button-note.oss-cn-shanghai.aliyuncs.com/img/image-20240901211606549.png)

导入文本

![image-20240901211629586](https://button-note.oss-cn-shanghai.aliyuncs.com/img/image-20240901211629586.png)



![image-20240901211716563](https://button-note.oss-cn-shanghai.aliyuncs.com/img/image-20240901211716563.png)

即可获取文本内容

