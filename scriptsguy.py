import os

ifpath = './main.txt'

files_id = 0

def start_script(tag, txt):
    global files_id
    if tag == 'py':
        with open(f"./running/running{files_id}.py", 'w', encoding='utf-8') as f:
            for i in txt:
                f.write(i)
        os.system(f"python ./running/running{files_id}.py")
    if tag == 'node':
        with open(f"./running/running{files_id}.js", 'w', encoding='utf-8') as f:
            for i in txt:
                f.write(i)
        os.system(f"node ./running/running{files_id}.js")
    files_id += 1

def process_file(lines):
    ispy = False
    isnode = False
    script = ''
    for i in lines:
        if '</py>' in i:
            ispy = False
            start_script('py', script)
            script = ''
        if '</node>' in i:
            isnode = False
            start_script('node', script)
            script = ''
        if ispy:
            script += i
        if isnode:
            script += i
        if i == '<py>\n':
            ispy = True
        if i == '<node>\n':
            isnode = True

def delete_running(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    with open(ifpath, "r", encoding='utf-8') as f:
        text = f.readlines()
        process_file(text)
        delete_running('./running')