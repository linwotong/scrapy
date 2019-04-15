import time
from concurrent.futures import ThreadPoolExecutor
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times
execuror = ThreadPoolExecutor(max_workers=2)
task1 = execuror.submit(get_html,(3))
task2 = execuror.submit(get_html,(2))
print(task1.done())
print(task2.cancel())
time.sleep(4)
print(task1.done())
print(task1.result())