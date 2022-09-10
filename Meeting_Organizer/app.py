from distutils.log import debug
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 

app = Flask(__name__)
app.secret_key = "ahmetkarayel"

DB_HOST = "localhost"
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "postgresql"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM meetings"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template("index.html", list_users = list_users)

@app.route('/add_meeting', methods=["POST"])
def add_meeting():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        start = request.form['start']
        end = request.form['end']
        members = request.form['members']
        cur.execute("INSERT INTO meetings (title, tarih, ilksaat, sonsaat, members) VALUES (%s, %s, %s, %s, %s)", (title, date, start, end, members))
        conn.commit()
        flash('Toplantı Eklendi.')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM meetings WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', meeting = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_meeting(id):
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        start = request.form['start']
        end = request.form['end']
        members = request.form['members']
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE meetings
            SET title = %s,
                tarih = %s,
                ilksaat = %s,
                sonsaat = %s,
                members = %s
            WHERE id = %s
        """, (title, date, start, end, members, id))
        flash('Toplantı Güncelleme Başarılı...')
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_meeting(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM meetings WHERE id = {0}'.format(id))
    conn.commit()
    flash('Toplantı Başarıyla Silindi...')
    return redirect(url_for('Index'))
 
if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)

