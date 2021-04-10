from scrapper.main             import get_jobs
from scrapper.csv_exporter     import save_to_file
from flask                     import (
    Flask,
    render_template,
    request,
    redirect,
    send_file
)
app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/report")
def report():
    word = request.args.get('word')
    if not word:
        return redirect('/')
    else:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            # so_jobs = so_get_jobs(word)
            # indeed_jobs = indeed_get_jobs(word)
            jobs = get_jobs(word)
            db[word] = get_jobs(word)
    return render_template('report.html', 
                            search_by=word, 
                            many=len(jobs),
                            jobs=jobs
                        )

@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file('jobs.csv')
    except:
        return redirect('/')
   

if __name__ == "__main__":
    app.run(host='0.0.0.0')
