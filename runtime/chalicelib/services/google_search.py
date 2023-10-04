import csv
import time

import requests
from bs4 import BeautifulSoup
from googlesearch import search

search("Amazon AWS Certified DevOps Engineer", num_results=10)

to_search_cert_name = "Amazon AWS Certified DevOps Engineer"
exam_provider = "https://www.examtopics.com/discussions"
max_question_no = 142


# Path: runtime/chalicelib/services/google_search.py
def do_search(cert_name, start_question_no, end_question_no, save_excel=False):
    res = []
    try:
        for i in range(start_question_no, end_question_no):
            search_term = "{cert_name} {no}".format(cert_name=cert_name, no=str(i))
            time.sleep(1)
            results = search(search_term, num_results=5)
            wanted_url = [url for url in results if exam_provider in url]
            if not wanted_url:
                continue

            question_url = [i, wanted_url[-1]]
            res.append(question_url)
    except Exception as e:
        print(e)
    finally:
        print(res)
        if save_excel and res:
            with open(
                f"/tmp/{cert_name.replace(' ','_')}_{start_question_no}_{end_question_no}.csv",
                "w",
                encoding="UTF8",
                newline="",
            ) as f:
                writer = csv.writer(f)

                # write the header
                writer.writerow(["QuestionNo", "URL"])

                # write multiple rows
                writer.writerows(res)

        return res


# do_search(
#     cert_name=to_search_cert_name,
#     start_question_no=1,
#     end_question_no=19,
#     save_excel=True,
# )
