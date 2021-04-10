from pprint import pprint

from scrapper.indeed         import get_jobs as get_indeed_jobs
from scrapper.so             import get_jobs as get_so_jobs
from scrapper.saramin        import get_jobs as get_sramin_jobs
from scrapper.csv_exporter   import save_to_file


indeed   = get_indeed_jobs()
# so       = get_so_jobs()
# saraimin = get_sramin_jobs()

print(indeed_jobs)

# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)


