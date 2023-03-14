pipeline {
    agent any
    
    stages{
        stage ('gitpull') {
            steps{
                git 'https://github.com/Gaikwad-07/python-spacy-pro.git'
            }
            
        }        
        stage ('Built') {
            steps{
                sh '''#!/bin/bash/
sudo apt-get install python3-pip python3-dev nginx
sudo apt-get update && sudo yum upgrade
apt-get install python3-venv -y
sudo apt-get pip3 install virtualenv
source evn/bin/activate
pip install -r requirements.txt
pip install django==3.0.7
cd /var/lib/jenkins/workspace/python-spacy-pro
systemctl start ngix
pip install gunicorn
pip install pandas==1.5.0
sudo ufw allow 8000
gunicorn --bind 0.0.0.0:8000 demo_spacy.wsgi
pip install spacy
pip install requests'''
            }
        }    
    }
}
