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

 stage('Deploy') {
 steps {
 echo 'Déploiement de l application Flask'
 sh 'pkill -f "flask --app app" || true'
 sh 'nohup python3 -m flask --app app run --host=0.0.0.0 --port=5000 > flask.log 2>&1 &'
 }
 }
 }
}
