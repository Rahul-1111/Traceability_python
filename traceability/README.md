conda create -p traceability_env python==3.11 -y
conda activate traceability_env/
conda env list

ls traceability_env

python manage.py runserver
daphne -b 0.0.0.0 -p 8000 traceability.asgi:application


--------------------------------------------------------------------------------------------------------------------------

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic


--------------------------------------------------------------------------------------------------------------------------

echo "# Traceability_python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Rahul-1111/Traceability_python.git
git push -u origin main

git remote add origin https://github.com/Rahul-1111/Traceability_python.git
git branch -M main
git push -u origin main

--------------------------------------------------------------------------------------------------------------------------

git clone https://github.com/Rahul-1111/plc_conn.git