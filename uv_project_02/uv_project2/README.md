create uv project with pkg
uv init --package uv_project2  
when we run --package command this will add src directory
change directory main to inner directory  cd uv_project2
then open code editor  code .

create custom file select uv_project2 and create new file

terminal commands  for running and checking custom file code 
cd uv_project2 
uv run main.py

if i wanna see what is in __init__.py in package run :
uv run uv-project2

this is most important script

[project.scripts]
uv-project2 = "uv_project2:main"
