import os
import re

ifpath = './main.txt'

files_id = 0

def start_script(tag, txt, start):
    global files_id
    if tag == 'py':
        with open(f"./running/running{files_id}.py", 'w', encoding='utf-8') as f:
            for i in txt:
                f.write(i)
        if start:
            os.system(f"start python ./running/running{files_id}.py")
            return
        os.system(f"python ./running/running{files_id}.py")

    if tag == 'node':
        with open(f"./running/running{files_id}.js", 'w', encoding='utf-8') as f:
            for i in txt:
                f.write(i)
        if start:
            os.system(f"start node ./running/running{files_id}.js")
            return
        os.system(f"node ./running/running{files_id}.js")
    files_id += 1

def process_file(lines):
    ispy = False
    isnode = False
    cmd_start = False
    script = ''
    for i in lines:
        if re.match(r'^\s*</py>\s*$', i):
            ispy = False
            start_script('py', script, cmd_start)
            script = ''
            cmd_start = False
        if re.match(r'^\s*</node>\s*$', i):
            isnode = False
            start_script('node', script, cmd_start)
            script = ''
            cmd_start = False
        if ispy:
            script += i
        if isnode:
            script += i
        if re.match(r'^\s*<py>\s*$', i):
            ispy = True
        if re.match(r'^\s*<node>\s*$', i):
            isnode = True
        if re.match(r'^\s*<py start=true>\s*$', i):
            ispy = True
            cmd_start = True
        if re.match(r'^\s*<node start=true>\s*$', i):
            cmd_start = True
            isnode = True

if __name__ == '__main__':
    with open(ifpath, "r", encoding='utf-8') as f:
        text = f.readlines()
        process_file(text)
