from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql 
app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
@app.route('/index', methods=['post', 'get'])
def index():
    if request.method=='POST': 
        conn = sql.connect('db_web.db') 
        cur = conn.cursor()
        id_tel = request.form['id_tel']
        nome = request.form['nome']
        conf = request.form['conf']
        print(nome)
        if conf == "1":
            doc = request.form['doc']
            acomp = request.form['acomp']
            rest_alim_list = request.form.getlist('rest_alim')
            rest_alim = ' '.join([str(i) for i  in rest_alim_list])
            cur.execute('insert into conv(id_tel, nome, conf, doc, rest_alim, acomp) values (?, ?, ?, ?, ?, ?)', (id_tel, nome, conf, doc, rest_alim, acomp))  
            if int(acomp) > 0:
                id_tel1 = request.form['id_tel1']
                nome1 = request.form['nome1']
                doc1 = request.form['doc1']
                rest_alim_list1 = request.form.getlist('rest_alim1')
                rest_alim1 = ' '.join([str(i) for i  in rest_alim_list1])
                cur.execute('insert into conv(id_tel, nome, conf, doc, rest_alim) values (?, ?, 1, ?, ?)', (id_tel1, nome1, doc1, rest_alim1))  
                if int(acomp) > 1:
                    id_tel2 = request.form['id_tel2']
                    nome2 = request.form['nome2']
                    doc2 = request.form['doc2']
                    rest_alim_list2 = request.form.getlist('rest_alim2')
                    rest_alim2 = ' '.join([str(i) for i  in rest_alim_list2])
                    cur.execute('insert into conv(id_tel, nome, conf, doc, rest_alim) values (?, ?, 1, ?, ?)', (id_tel2, nome2, doc2, rest_alim2)) 
                    if int(acomp) > 2:
                        id_tel3 = request.form['id_tel3']
                        nome3 = request.form['nome3']
                        doc3 = request.form['doc3']
                        rest_alim_list3 = request.form.getlist('rest_alim3')
                        rest_alim3 = ' '.join([str(i) for i  in rest_alim_list3])
                        cur.execute('insert into conv(id_tel, nome, conf, doc, rest_alim) values (?, ?, 1, ?, ?)', (id_tel3, nome3, doc3, rest_alim3)) 
        else: 
            cur.execute('insert into conv(id_tel, nome, conf) values (?, ?, ?)', (id_tel, nome, conf))   
        conn.commit()
        flash('User Added','success')
        return render_template("index.html", anchor="mensagem")
    return render_template("index.html")
    
@app.route('/edit_conv', methods=['post', 'get'])
def edit_conv():
    if request.method=='POST': 
        conn = sql.connect('db_web.db') 
        cur = conn.cursor()
        id_tel = request.form['id_tel']
        conf = request.form['conf']
        if conf == '1':
            doc = request.form['doc']
            acomp = request.form['acomp']
            rest_alim_list = request.form.getlist('rest_alim')
            rest_alim = ' '.join([str(i) for i  in rest_alim_list])
            cur.execute('update conv set conf=1, doc=?, rest_alim=?, acomp=? where id_tel=?', (doc, rest_alim, acomp, id_tel))   
            if int(acomp) > 0:
                id_tel1 = request.form['id_tel1']
                nome1 = request.form['nome1']
                doc1 = request.form['doc1']
                rest_alim_list1 = request.form.getlist('rest_alim1')
                rest_alim1 = ' '.join([str(i) for i  in rest_alim_list1])
                cur.execute('insert into conv(id_tel, nome, conf, doc, rest_alim) values (?, ?, 1, ?, ?)', (id_tel1, nome1, doc1, rest_alim1))  
                if int(acomp) > 1:
                    id_tel2 = request.form['id_tel2']
                    nome2 = request.form['nome2']
                    doc2 = request.form['doc2']
                    rest_alim_list2 = request.form.getlist('rest_alim2')
                    rest_alim2 = ' '.join([str(i) for i  in rest_alim_list2])
                    cur.execute('insert into conv(id_tel, nome, conf, doc, rest_alim) values (?, ?, 1, ?, ?)', (id_tel2, nome2, doc2, rest_alim2)) 
                    if int(acomp) > 2:
                        id_tel3 = request.form['id_tel3']
                        nome3 = request.form['nome3']
                        doc3 = request.form['doc3']
                        rest_alim_list3 = request.form.getlist('rest_alim3')
                        rest_alim3 = ' '.join([str(i) for i  in rest_alim_list3])
                        cur.execute('insert into conv(id_tel, nome, conf, doc, rest_alim) values (?, ?, 1, ?, ?)', (id_tel3, nome3, doc3, rest_alim3)) 
        else: 
           cur.execute('update conv set conf=0 where id_tel=?', ([id_tel]))   
        conn.commit()
        return redirect(url_for('index')+"#mensagem")
    conn=sql.connect('db_web.db')
    conn.row_factory=sql.Row
    cur=conn.cursor()
    return render_template('edit_conv.html')

@app.route('/index#mensagem', methods=['post', 'get'])
def mensagem():
    if request.method=='POST': 
        conn = sql.connect('db_web.db') 
        cur = conn.cursor()
        msg = request.form['message']
        cur.execute('insert into msg(text) values (?)', [msg]) 
        conn.commit()
        return render_template('index.html')
    return redirect(url_for('index')+"#mensagem")
    
if __name__ == '__main__': 
    app.secret_key='Eu25ANOS#29052001'
    app.run(debug=True)     
        