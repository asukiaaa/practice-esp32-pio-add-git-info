Import("projenv")
import os
import subprocess

try:
  str_info_git = subprocess.check_output(['git', 'log', '-n', '1', '--pretty=\'format:%cd\' --date=format:\'%Y-%m-%d %H:%M:%S\'']).strip()
  projenv.AppendUnique(CPPDEFINES=[("STR_INFO_GIT", env.StringifyMacro(str_info_git))])
except:
  print("cannot assign str")
