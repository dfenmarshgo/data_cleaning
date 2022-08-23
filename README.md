# data_cleaning
[![Python application test with Github Actions](https://github.com/dfenmarshgo/data_cleaning/actions/workflows/devops.yml/badge.svg)](https://github.com/dfenmarshgo/data_cleaning/actions/workflows/devops.yml)




1. Create virtual environment "python3 -m venv ~/.venv" or "virtualenv ~/.venv" and then automate into bash file "vim ~/.bashrc" type "i" for insert mode in vim then add "#Python Virtual Environment" at bottom and add "source ~/.venv/bin/activate" then press escape and type ":wq!" to save changes
2. Create empty files 'requirements.txt', 'Dockerfile', 'Makefile', 'mylib', '__init__.py', 'logic.py', 'main.py'
3. Populate Makefile 
4. 	#install commands
		pip install --upgrade pip &&\
		pip install -r requirements.txt
5. Push to github ("git status" to check status of files, "git add *" to add and then git commit -m "description"  to commit changes and finally "git push" to push the changes)        
type in "make install" to install pip packages 
6. pip freeze to get actual versions of packages for version control then copy/paste appropriately in requirements.txt
7. push changes
8. Go to Github Actions and create new workflow using .yml file then copy and paste status badge into readme file.
9. Create logic in logic.py
10. Add black *.py mylib/*.py to the Makefile under "format"
11. Run "make format"
12. Make changes to main.py (This is where the main code goes, it imports mylib.logic.py file)
13. Git push changes but git pull first because of the changes made in github actions inside github itself "git pull" and then "git config pull.rebase false  # merge" then "git pull" again and finally "git push"
14. Add linting to Makefile = pylint --disable=R,C *.py mylib/*.py, test with "make lint"
15. git add .github/
16. git push changes (make sure workflows are enabled for gitpod -> check dashboard and preferences)
17. Create a test file "test_logic.py" 
18. Add this to the Makefile under "test" python -m pytest -vv --cov=mylib test_logic.py then type make test to test
19. Update the .yml file to include this
20. Create a CLI for the application/script using Google Fire and give user permissions  chmod +x cli-fire.py - then run it with this: ./cli-fire.py --help to test logic
21. Add FastAPI and Uvicorn and testing capabilities
22. Change Makefile and Dockerfile -> Use from python:3.8.13-slim-buster in DockerFile
