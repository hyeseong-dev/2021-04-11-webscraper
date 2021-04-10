# Job Search WebCrawler 🚄

- 진행기간 : 2021년 04월 04일 ~ 2021년 04월 10일
[사진1]
![image](https://user-images.githubusercontent.com/57933835/114275508-c1dc2c00-9a5d-11eb-8d71-7e500cff9cdc.png)

[사진2]
![image](https://user-images.githubusercontent.com/57933835/114275615-21d2d280-9a5e-11eb-9892-672475c9900b.png)

## **🏠토이 프로젝트 소개**

> 구인 구직 정보 제공 사이트 Stackoverflow, Indeed, Saramin, 3곳을 이용하여 간단한 스크래퍼를 작성하였습니다.

## **🏠**프로젝트 시연영상

https://youtu.be/AaUEtWd0aq4

## **🏠** 프로젝트 참가자 (Front & Back)

### 👍 **BackEnd**

- 이혜성, 

## **🌹기술 스택🌹**

### **FrontEnd**

- HTML / CSS / 

### **BackEnd**

- Python / Flask / poetry / bs4 / requests / 

### **기타 도구**

- Slack / Git + GitHub / 

---

# ⭐️ **구현 기능**

## 🌱 Backend

### Directories Structure
- scrapper 패키지
  + csv_exporter : 파이썬 데이터를 csv파일로 저장합니다.
  + so.py        : 총 4개의 함수로 구성된 모듈입니다.
  ![image](https://user-images.githubusercontent.com/57933835/114276101-2b5d3a00-9a60-11eb-9680-93eab26bd246.png)
  + indeed.py    : 총 4개의 함수로 구성된 모듈입니다.
  + saramin.py   : 총 4개의 함수로 구성된 모듈입니다.
  + main.py      : indeed, so, saramin 모듈들의 각기 다른 데이터를 단일 데이터로 만듭니다.
![image](https://user-images.githubusercontent.com/57933835/114276115-3fa13700-9a60-11eb-8ded-edd9e4afbb3e.png)

- template 폴더  
  + home.html   :
```html
<html>
  <head>
    <title>JobSearch</title>
  </head>
  <body>
    <h1>JobSearch</h1>
    <form action = "/report" method = "get">
    <input placeholder="Search for a Job" requried name = "word">
    <button>Search</button>

    </form>
  </body>
</html>
```

  + report.html :
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Job Search</title>
    <style>
      section{
        display:grid;
        gap:20px;
        grid-template-columns: repeat(4,1fr);
      }
    </style>
  </head>
  <body>
    <h1>Search Results</h1>
    <h1>Found {{many}} jobs for {{search_by}}<h1> 
    <a href="/export?word={{search_by}}">Export to CSV</a>
    <section>
      <h4>Title</h4>
      <h4>Company</h4>
      <h4>Location</h4>
      <h4>Link</h4>
      {% for job in jobs %}
        <span>{{job.title}}</span>
        <span>{{job.company}}</span>
        <span>{{job.location}}</span>
        <a href = "{{job.link}}" target="_blank">apply</a>
      {% endfor %}
    </section>
  </body>
</html>
```
![image](https://user-images.githubusercontent.com/57933835/114275790-ca813200-9a5e-11eb-8d91-2cc8ade2a2f5.png)


### apps.py
![image](https://user-images.githubusercontent.com/57933835/114275736-9b6ac080-9a5e-11eb-8c6f-77a74e342f09.png)
![image](https://user-images.githubusercontent.com/57933835/114275757-afaebd80-9a5e-11eb-8e29-fe0f226a228c.png)


---



# **레퍼런스**

- 이 프로젝트는 [stackoverflow], [saramin], [indeed]의 정보를 참조하여 학습목적으로 만들었습니다.
- 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.

