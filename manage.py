from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:SUA_SENHA_NO_BANCO@127.0.0.1/alunos"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Alunos(db.Model):
          __tablename__='alunos'
          id = db.Column(db.Integer, primary_key=True, autoincrement=True)
          nome = db.Column(db.String(100), nullable=False)
          nota = db.Column(db.Integer, nullable=False)
with app.app_context():
    db.create_all()
@app.route('/')
def start():
       return render_template('inicio.html')
@app.route('/add' ,methods=['POST'])
def site():
       nome=request.form.get('nome')
       nota=request.form.get('nota')
       if nome and nota:
              try:
                nota=int(nota)
              except:
                    return 'nota tem que ser um numero!',400
              novo=Alunos(nome=nome,nota=nota)
              db.session.add(novo)
              db.session.commit()
              alunos=Alunos.query.order_by(Alunos.nota.desc()).all()
              return render_template('notas.html',alunos=alunos)
       else:
              return 'nota ou nome nao inseridos',400
       
if __name__=='__main__':
       app.run(debug=True)
