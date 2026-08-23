pipeline {
 agent any

 stages {
 stage('Installation') {
 steps {
 sh 'python3 -m pip install -r requirements.txt'
 sh 'python3 -m pip install pytest'
}
 }

 stage('Test') {
 steps {
 sh 'python3 -m py_compile app.py'
 sh 'python3 -m pytest test_app.py'
 echo 'Application Flask testée avec succès !'
 }
 }
 }
}
