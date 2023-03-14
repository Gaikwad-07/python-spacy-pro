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
                sh '''cd /var/lib/jenkins/workspace/python-spacy-pro
sudo apt-get install python3-pip python3-dev nginx
sudo apt-get update && sudo apt-get upgrade
apt-get install python3-venv -y
sudo apt-get pip3 install virtualenv
source evn/bin/activate
pip3 install -r requirements.txt
pip3 install django==3.0.7
cd /var/lib/jenkins/workspace/python-spacy-pro
systemctl start ngix
pip3 install gunicorn
pip3 install pandas==1.5.0
sudo ufw allow 8000
gunicorn --bind 0.0.0.0:8000 demo_spacy.wsgi
pip3 install spacy
pip3 install requests'''
            }
        }    
    }
}
