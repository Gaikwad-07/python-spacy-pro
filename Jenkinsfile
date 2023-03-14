pipeline {
    agent any
    
    stages {
        stage('gitpull') {
            steps {
                git 'https://github.com/Gaikwad-07/python-spacy-pro.git'
                
        stage ('venv') {
            steps{
                sh '''#!/bin/bash/
sudo yum install python3-pip python3-dev nginx
sudo yum update && sudo yum upgrade
yum install python3-venv -y
sudo pip3 install virtualenv
source evn/bin/activate
pip install -r requirements.txt
pip install django==3.0.7
cd /root/.jenkins/workspace/python-pipeline
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
        
}
}
