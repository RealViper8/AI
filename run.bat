chdir %cd%
@echo off
color 0a
title Main
%@Try%
  cls
  python3 main.py
%@EndTry%
:@Catch
  cls
  python main.py
:@EndCatch
pause