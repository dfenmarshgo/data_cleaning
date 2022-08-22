# data_cleaning

1. Create virtual environment "python3 -m venv ~/.venv" or "virtualenv ~/.venv" and then automate into bash file "vim ~/.bashrc" type "i" for insert mode in vim then add "#Python Virtual Environment" at bottom and add "source ~/.venv/bin/activate" then press escape and type ":wq!" to save changes
2. Create empty files 'requirements.txt', 'Dockerfile', 'Makefile', 'mylib', '__init__.py', 'logic.py', 'main.py'
3. Populate Makefile 
4. 	#install commands
		pip install --upgrade pip &&\
		pip install -r requirements.txt
5. Push to github ("git status" to check status of files, "git add *" to add and then git commit -m "description"  to commit changes)        
type in "make install" to install pip packages 
6. pip freeze to get actual versions of packages for version control then copy/paste appropriately in requirements.txt

