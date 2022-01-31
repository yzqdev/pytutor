#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: run.py
@time: 2022/1/31 3:58
"""
import os.path
import sys
import winreg
import ctypes
default_text: str = """
-Xms128m
-Xmx1024m
-XX:ReservedCodeCacheSize=512m
-XX:+IgnoreUnrecognizedVMOptions
-XX:+UseG1GC
-XX:SoftRefLRUPolicyMSPerMB=50
-XX:CICompilerCount=2
-XX:+HeapDumpOnOutOfMemoryError
-XX:-OmitStackTraceInFastThrow
-ea
-Dsun.io.useCanonCaches=false
-Djdk.http.auth.tunneling.disabledSchemes=""
-Djdk.attach.allowAttachSelf=true
-Djdk.module.illegalAccess.silent=true
-Dkotlinx.coroutines.debug=off
-XX:ErrorFile=$USER_HOME/java_error_in_idea_%p.log
-XX:HeapDumpPath=$USER_HOME/java_error_in_idea.hprof
"""


def config_apth(app: str):
    split_txt = "#divide\n"
    conf = f"-Didea.config.path=D:\\configuration\\pycharmConf\\config\n-Didea.system.path=D:\\configuration\\{app}Conf\\system\n-Didea.log.path=D:\\configuration\\{app}Conf\\system\\log\n-javaagent:D:\ja-netfilter\ja-netfilter.jar=jetbrains"
    return default_text + split_txt + conf


def write_vmoptions():
    apps = ["idea", "clion", "phpstorm", "goland", "pycharm", "webstorm", "webide", "rider", "datagrip", "rubymine",
            "appcode", "dataspell", "gateway", "jetbrains_client", "jetbrainsclient"]
    vmdir = "vmoptionlist"
    if not os.path.exists(vmdir):
        os.mkdir(vmdir)
    for app in apps:
        with open(f"{vmdir}/{app}.vmoptions", "wb+") as f:
            f.write(bytes(config_apth(app), encoding="utf-8"))


def write_ref():
    pass

if __name__ == "__main__":
    write_vmoptions()
