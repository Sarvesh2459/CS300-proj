from pyclbr import Class
from pydoc import classname
from traceback import print_tb
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from django.shortcuts import render

all_questions=[]

def All_User_data(request):
    return render(request,"data.html",{'data':all_questions}) 


class Scrape:
    def __init__(self,uid):
        self.uid = uid
        self.handle()
    def handle(self):
        import requests
        page = requests.get('https://codeforces.com/submissions/'+self.uid)
        print(self.uid)
        all_questions.clear()
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table',class_="status-frame-datatable")
        table_rows = table.find_all("tr")
        question_id=[]
        date_time=[]
        language=[]
        question_name=[]
        verdict=[]
        for i in range(1,len(table_rows)):
            # print(trss[i][5].text)
            ct=0
            for j in table_rows[i]:
                if(ct==1):
                    question_id.append(j.text)
                if(ct==3):
                    date_time.append(j.text)
                if(ct==7):
                    question_name.append(j.text)
                if(ct==9):
                    language.append(j.text)
                if(ct==11):
                    verdict.append(j.text)
                ct+=1

        # print(question_id)


        for i in range(len(question_id)):
            one_question=[]
            one_question.append(question_id[i].rstrip().lstrip())
            one_question.append(question_name[i].rstrip().lstrip())
            one_question.append(language[i].rstrip().lstrip())
            one_question.append(date_time[i].rstrip().lstrip())
            one_question.append(verdict[i].rstrip().lstrip())
            all_questions.append(one_question)
        
        # print(all_questions)
        self.soup = soup


