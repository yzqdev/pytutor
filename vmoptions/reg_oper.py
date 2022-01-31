#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: reg_oper.py
@time: 2022/1/31 20:47
"""

import ctypes
import sys
import winreg

import zlib
def admin():
    aa = ctypes.windll.shell32.IsUserAnAdmin()
    return aa


def reg_query(path, key):
    try:
        path = path.replace("/", "\\")
        rootName = path[:path.find("\\")]
        subPath = path[path.find("\\") + 1:]
        rootKey = _query_root(rootName)

        if rootKey is None:
            return ""
        print(path)
        root = winreg.OpenKey(rootKey, subPath)
        value, type = winreg.QueryValueEx(root, key)
        return value
    except:
        # log.exception(traceback.format_exc())
        return ""
def _query_root(rootName):
    rootKey = None
    if rootName == "HKEY_LOCAL_MACHINE":
        rootKey = winreg.HKEY_LOCAL_MACHINE
    elif rootName == "HKEY_CLASSES_ROOT":
        rootKey = winreg.HKEY_CLASSES_ROOT
    elif rootName == "HKEY_CURRENT_USER":
        rootKey = winreg.HKEY_CURRENT_USER
    elif rootName == "HKEY_USERS":
        rootKey = winreg.HKEY_USERS
    elif rootName == "HKEY_CURRENT_CONFIG":
        rootKey = winreg.HKEY_CURRENT_CONFIG
    return rootKey

def reg_add(path, key, value, type=winreg.REG_SZ):
    try:
        path = path.replace("/", "\\")
        rootName = path[:path.find("\\")]
        subPath = path[path.find("\\") + 1:]
        rootKey = _query_root(rootName)

        if rootKey is None:
            return ""
        print(path)
        root = winreg.OpenKey(rootKey, subPath, 0, winreg.KEY_ALL_ACCESS)
        # subKey = winreg.CreateKeyEx(root, key)
        winreg.SetValueEx(root, key, 0, type, value)
        return True
    except:
        return False
if __name__ == '__main__':
    if admin() == 1:  # 有管理员权限可打开远程注册表
        winreg.ConnectRegistry('\\计算机名', winreg.HKEY_LOCAL_MACHINE)
    else:

        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    print("hhhh")
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Control\Session Manager\Environment")

    reg_add(r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\Python.exe", "test", "test")