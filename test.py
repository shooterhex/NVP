# 读取文件内容
with open('new_environment.yaml', 'r') as file:
    lines = file.readlines()

# 处理每一行，并去除等号及其后面的内容
processed_lines = [line.split('=')[0] + '\n' for line in lines]

# 将处理后的内容写入新文件
with open('new_environment_2.0.yaml', 'w') as file:
    file.writelines(processed_lines)
