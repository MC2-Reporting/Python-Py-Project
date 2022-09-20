git init 
gh repo create MC2-Reporting/Python-Py-Project  --private 
git branch -M master 
git remote add origin https://github.com/MC2-Reporting/Python-Py-Project.git 
poetry install --no-dev 
pre-commit install 
git add . 
git commit -m "Initial commit, repo structure"
git push -u origin master
pause
