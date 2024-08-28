# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 10:46
# @Author  : shenyuming
# @FileName: p_venv.py
# @Software: PyCharm

import os

def list_virtual_environments(directory):
    envs = []
    for entry in os.scandir(directory):
        if entry.is_dir() and os.path.exists(os.path.join(entry.path, 'bin', 'activate')):
            envs.append(entry.name)
    return envs

if __name__ == "__main__":
    directory = os.path.expanduser('~/Envs')
    envs = list_virtual_environments(directory)
    print("Virtual environments found:")
    for env in envs:
        print(env)