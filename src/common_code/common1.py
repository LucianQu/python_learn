
def build_profile(first, last, **user_info):  # 两个*让python创建一个名为user_info的空字典
    profile = {}  # 创建字典
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value1 in user_info.items():
        profile[key] = value1
    return profile


def save(file_lines):
    with open("movice.txt", 'w') as movice_content:
        for content in file_lines:
            movice_content.write( content + "\n")
        movice_content.closed


"""
计算一本书单词量的函数
"""
def count_words(file_name):
    try:
        with open(file_name) as f_obj:
            f_obj_contents = f_obj.read()
    except:
        msg = " Sorry, the file" + file_name + "does not exist !"
        print(msg)
    else:
        words = f_obj_contents.split()
        num_words = len(words)
        print("The file" + file_name + "has about " + str(
            num_words) + " words .")