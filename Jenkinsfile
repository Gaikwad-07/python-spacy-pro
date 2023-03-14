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
sudo apt-get install python3-pip python3-dev nginx -y
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3-venv -y
sudo pip3 install virtualenv
source evn/bin/activate
pip3 install -r requirements.txt -y
pip3 install django==3.0.7 -y
cd /var/lib/jenkins/workspace/python-spacy-pro
systemctl start ngix -y
pip3 install gunicorn -y
pip3 install pandas==1.5.0 -y
sudo ufw allow 8000
gunicorn --bind 0.0.0.0:8000 demo_spacy.wsgi
pip3 install spacy -y
pip3 install requests -y'''
            }
        }    
    }
}
