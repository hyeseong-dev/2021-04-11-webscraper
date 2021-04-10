from pprint import pprint

from scrapper.indeed         import get_jobs as get_indeed_jobs
from scrapper.so             import get_jobs as get_so_jobs
from scrapper.saramin        import get_jobs as get_sramin_jobs
from scrapper.csv_exporter   import save_to_file

def get_jobs(word):
    saramin = get_sramin_jobs(word)
    indeed  = get_indeed_jobs(word)
    so      = get_so_jobs(word)
    jobs    = indeed + so + saramin
    return jobs

save_to_file(jobs)


