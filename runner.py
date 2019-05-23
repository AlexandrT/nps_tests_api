import subprocess


pytest_run_arr = ['py.test', '-v', '-l', \
        '--html=reports/report.html','--self-contained-html']

tests_proc = subprocess.run(pytest_run_arr)

if tests_proc.returncode != 0:
    raise Exception('Some tests is failed.')
