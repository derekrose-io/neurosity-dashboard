git init                      # make the folder a repo
git remote add origin https://github.com/<YOUR_USER>/neurosity-dashboard.git
echo "streamlit\npandas\naltair" > requirements.txt
git add neuro_dashboard_app.py requirements.txt
git commit -m "Initial dashboard commit"
git branch -M main            # rename master→main if needed
git push -u origin main       # enter GitHub username/password or token
