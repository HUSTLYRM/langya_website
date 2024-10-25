import os
import pandas as pd
import yaml

# CSV 文件路径
CSV_FILE = "/Users/micdz/Projects/langya_website/_members/members.csv"  # 你的表格文件
MARKDOWN_FOLDER = "/Users/micdz/Projects/langya_website/_members"  # Markdown 文件所在文件夹

def load_csv(file_path):
    return pd.read_csv(file_path)

def update_markdown(md_path, updates):
    with open(md_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 找到 YAML 元数据部分
    start, end = None, None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if start is None:
                start = i
            else:
                end = i
                break

    # 如果没有找到 YAML 元数据，则跳过文件
    if start is None or end is None:
        print(f"File {md_path} has no YAML metadata.")
        return

    # 解析 YAML
    yaml_data = yaml.safe_load("".join(lines[start + 1:end]))

    # 更新 YAML 中的字段
    for key, value in updates.items():
        yaml_data[key] = value  # 如果字段缺失则添加


    # 写回更新的内容
    with open(md_path, 'w', encoding='utf-8') as file:
        file.writelines(lines[:start + 1])
        yaml.dump(yaml_data, file, allow_unicode=True)
        file.writelines(lines[end:])

def main():
    # 读取 CSV 文件
    df = load_csv(CSV_FILE)

    for index, row in df.iterrows():
        name = row['name']
        updates = {
            'affiliation': row['affiliation'],
            'role': row['role'],
            'type': row['type'],
            'time': row['time'],
            'echelon': row['echelon'],
            'grade': row['grade'],
        }
        
        # 根据名字找到对应的 Markdown 文件
        md_path = os.path.join(MARKDOWN_FOLDER, f"{name}.md")
        if os.path.exists(md_path):
            update_markdown(md_path, updates)
            print(f"Updated {md_path}")
        else:
            print(f"File {md_path} not found.")

if __name__ == "__main__":
    main()