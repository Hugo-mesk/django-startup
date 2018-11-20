@echo off
set myPath=%cd%
pushd ..
set parentPath=%cd%
popd


cmd.exe /k "%parentPath%"\env\Scripts\activate