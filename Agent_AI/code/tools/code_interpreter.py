import base64
import os
import re
from uuid import uuid4
from codeboxapi import CodeBox
from configs.setting import MEDIA_DIR


class CodeInterpreter:
    def __init__(self):
        self.output_files = [] # 修改1：从 "" 改为 []，用列表存储多个图片URL
        self.output_codes = ""
        self.codebox = CodeBox(api_key="local")
        self.codebox.start()

    # 添加获取 output_files 的方法
    def get_outputs(self):
        #return self.output_files, self.output_codes
        return "\n\n".join(self.output_files), self.output_codes  # 修改2：将列表用双换行符连接成字符串返回

    def run(self, code: str):
        clean_code = re.sub(r'(```python|```py|```)\s*', '', code, flags=re.IGNORECASE)
        # 去除首尾的空白字符
        clean_code = clean_code.strip()
        # 去除多余的空行
        lines = [line for line in clean_code.split('\n') if line.strip()]
        # 将处理后的行重新组合成字符串
        cleaned_code = '\n'.join(lines)
        output = self.codebox.run(cleaned_code)
        if output.type == "image/png":
            filename = f"{MEDIA_DIR}/image-{uuid4()}.png"
            decoded_image = base64.b64decode(output.content)

            # 将解码后的数据写入文件
            with open(filename, 'wb') as file:
                file.write(decoded_image)

            # 生成图片的URL
            image_url = f"/media/{os.path.basename(filename)}"
            #self.output_files = image_url
            self.output_files.append(image_url)  # 修改3：从 "=" 改为 ".append()"，追加而不是覆盖
            self.output_codes = cleaned_code
            return f"Image got send to the user."

        else:
            return output.content
code_interpreter = CodeInterpreter()
