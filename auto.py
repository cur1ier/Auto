from subprocess import *
import os
import tkinter as tk


def get_answer(ans_path, test_txt):
    cmd = "g++ " + ans_path + " -o " + ans_path.split(".")[0]
    call(cmd, shell=True)
    cmd = ans_path.split(".")[0] + ".exe < " + test_txt
    ans = check_output(cmd, shell=True).decode('ascii')
    return ans

def get_result(res_path, test_txt):
    # res = subprocess.check_output(res_path.split(".")[0] + ".exe").decode('ascii')
    cmd = ".\\exe\\" + res_path + " < " + test_txt
    res = check_output(cmd, shell=True).decode('ascii')
    return res

def compile_all():
    filenum = 0
    if not os.path.isdir("./exe"):
        os.mkdir("./exe")
    for filename in os.listdir("./cpp"):
        if filename.endswith(".cpp"):
            filenum += 1
            cmd = "g++ ./cpp/" + filename + " -o ./exe/" + filename.split(".")[0]
            call(cmd, shell=True)
    return filenum

def test():
    answer = get_answer("answer.cpp")

    for filename in os.listdir("./exe"):
        if filename == "A3-107502018.exe":
            result = get_result(filename)
            if result == answer:
                print("yes")
            else:
                print("answer: \n" + answer + "\n===================")
                print("result: \n" + result + "\n===================")


def get_filename(dir_path):
    file_list = []
    for filename in os.listdir(dir_path):
        file_list.append(filename)
    return file_list

