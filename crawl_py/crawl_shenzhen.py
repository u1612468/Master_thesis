import requests
from bs4 import BeautifulSoup
import sqlite3
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["job_name","salary","company_name","company_category","company_size","location","work_exp","edu_level"])


# 建立数据库连接
conn = sqlite3.connect('job_info_shenzhen.db')
cursor = conn.cursor()

# 创建表格
cursor.execute('CREATE TABLE IF NOT EXISTS job (job_name TEXT, salary TEXT, company_name TEXT, company_category TEXT, company_size TEXT, location TEXT, work_exp TEXT, edu_level TEXT)')

page_num = 34 # 要爬取的页数

for i in range(1, page_num+1):
    url = f"https://sou.zhaopin.com/?jl=765&p={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    job_list = soup.find_all("div", class_="joblist-box__item clearfix")

    for job in job_list:
        job_name = job.find("span", class_="iteminfo__line1__jobname__name").text
        salary = job.find("p", class_="iteminfo__line2__jobdesc__salary").text.strip()
        company_name = job.find("span", class_="iteminfo__line1__compname__name").text
        company_category= job.find_all("span",{"class": "iteminfo__line2__compdesc__item"})[0].text.strip()
        company_size = job.find_all("span",{"class": "iteminfo__line2__compdesc__item"})[1].text.strip()
        location = job.find_all("li", {"class": "iteminfo__line2__jobdesc__demand__item"})[0].text
        work_exp = job.find_all("li", {"class": "iteminfo__line2__jobdesc__demand__item"})[1].text
        edu_level = job.find_all("li", {"class": "iteminfo__line2__jobdesc__demand__item"})[2].text
        # print(f"job_name：{job_name}\nsalary：{salary}\n公司名称：{company_name}\n公司规模：{company_size}\n地点：{location}\n工作经验：{work_exp}\n学历要求：{edu_level}\n")

        cursor.execute('INSERT INTO job (job_name, salary, company_name, company_category, company_size, location, work_exp, edu_level) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (job_name, salary, company_name, company_category,company_size, location, work_exp, edu_level))
        conn.commit()
wb.save("job_info_shenzhen.xlsx")
# 关闭数据库连接
conn.close()