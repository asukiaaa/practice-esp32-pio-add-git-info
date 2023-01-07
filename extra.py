Import("env", "projenv")
import os
import subprocess

try:
    cmd = "git log -1 --pretty='%cd' --date=format:'%Y-%m-%d-%H:%M:%S%z'"
    # str_info_git = subprocess.check_output(['git', 'log', '-1', "--pretty='format:\%cd'", "--date=format:'\%Y-\%m-\%d \%H:\%M:\%S'"]).strip()
    str_info_git = subprocess.check_output(cmd.split()).strip().decode('utf-8')
    cmd = 'git diff --name-only'
    str_diff_files = subprocess.check_output(cmd.split()).strip()
    if str_diff_files == b'':
        str_info_git = str_info_git + '-no-diff'
    else:
        str_info_git = str_info_git + '-modified'
    print(str_info_git)
    # print(str_info_git.decode('utf-8'))
    projenv.AppendUnique(CPPDEFINES=[("STR_INFO_GIT", env.StringifyMacro(str_info_git))])
except Exception as e:
    print("cannot assign str")
    print(e)
    # raise e
