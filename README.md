# Job Search WebCrawler π

- μ§νκΈ°κ° : 2021λ 04μ 04μΌ ~ 2021λ 04μ 10μΌ

[μ¬μ§1]
![image](https://user-images.githubusercontent.com/57933835/114275508-c1dc2c00-9a5d-11eb-8d71-7e500cff9cdc.png)

[μ¬μ§2]
![image](https://user-images.githubusercontent.com/57933835/114275615-21d2d280-9a5e-11eb-9892-672475c9900b.png)

## **π ν μ΄ νλ‘μ νΈ μκ°**

> κ΅¬μΈ κ΅¬μ§ μ λ³΄ μ κ³΅ μ¬μ΄νΈ Stackoverflow, Indeed, Saramin, 3κ³³μ μ΄μ©νμ¬ κ°λ¨ν μ€ν¬λνΌλ₯Ό μμ±νμμ΅λλ€.


## **πΉκΈ°μ  μ€νπΉ**

### **FrontEnd**

- HTML / CSS / 

### **BackEnd**

- Python / Flask / poetry / bs4 / requests / 

### **κΈ°ν λκ΅¬**

- Slack / Git + GitHub / 

---

# β­οΈ **κ΅¬ν κΈ°λ₯**

## π± Backend

### Directories Structure
![image](https://user-images.githubusercontent.com/57933835/114275790-ca813200-9a5e-11eb-8d91-2cc8ade2a2f5.png)


- scrapper ν¨ν€μ§
  + csv_exporter : νμ΄μ¬ λ°μ΄ν°λ₯Ό csvνμΌλ‘ μ μ₯ν©λλ€.
    - ![image](https://user-images.githubusercontent.com/57933835/114276299-00271a80-9a61-11eb-8198-edb3e63e736d.png)
  
  + so.py        : μ΄ 4κ°μ ν¨μ(get_lastpage,extract_job,extract_jobs,get_jobs)λ‘ κ΅¬μ±λ λͺ¨λμλλ€.
    - ![image](https://user-images.githubusercontent.com/57933835/114276101-2b5d3a00-9a60-11eb-9680-93eab26bd246.png)
  
  + indeed.py    : μ΄ 4κ°μ ν¨μλ‘ κ΅¬μ±λ λͺ¨λμλλ€.
    - ![image](https://user-images.githubusercontent.com/57933835/114276336-2b116e80-9a61-11eb-80eb-0c899be49552.png)
  
  + saramin.py   : μ΄ 4κ°μ ν¨μλ‘ κ΅¬μ±λ λͺ¨λμλλ€.
    - ![image](https://user-images.githubusercontent.com/57933835/114276267-d837b700-9a60-11eb-8ad1-84c8b18fb152.png)
  
  + main.py      : indeed, so, saramin λͺ¨λλ€μ κ°κΈ° λ€λ₯Έ λ°μ΄ν°λ₯Ό λ¨μΌ λ°μ΄ν°λ‘ λ§λ­λλ€.
    - ![image](https://user-images.githubusercontent.com/57933835/114276115-3fa13700-9a60-11eb-8ded-edd9e4afbb3e.png)

- template ν΄λ  
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



### apps.py
- ('/')       : ν νλ©΄μμλ μλ ₯μ°½μ ν΅ν΄ μνλ μ‘°κ±΄μ λ§λ ν€μλ(ex. python)λ₯Ό κ²μνμ¬ λ°μ΄ν°λ₯Ό μ°ΎκΈ° μμν©λλ€.
- ('/report') : ν΄λΉ ν€μλμ λΆν©νλ κ²°κ³Όλ₯Ό λͺ¨λ htmlνμΌμ λλλ§νμ¬ μΉλΈλΌμ°μ λ‘ λ³΄μ¬μ£Όκ² λ©λλ€. 
- ('/export') : report νλ©΄μμ csv download λ§ν¬ ν΄λ¦­μ ν€μλλ₯Ό κ²μνμ¬ λμ¨ λͺ¨λ  λ°μ΄ν° κ²°κ³Όλ₯Ό νμΌλ‘ λ€μ΄λ°μ΅λλ€.

![image](https://user-images.githubusercontent.com/57933835/114275736-9b6ac080-9a5e-11eb-8c6f-77a74e342f09.png)
![image](https://user-images.githubusercontent.com/57933835/114275757-afaebd80-9a5e-11eb-8e29-fe0f226a228c.png)

---

# **λ νΌλ°μ€**

- μ΄ νλ‘μ νΈλ [stackoverflow], [saramin], [indeed]μ μ λ³΄λ₯Ό μ°Έμ‘°νμ¬ νμ΅λͺ©μ μΌλ‘ λ§λ€μμ΅λλ€.
- νμ΅μ©μΌλ‘ λ§λ€μκΈ° λλ¬Έμ μ΄ μ½λλ₯Ό νμ©νμ¬ μ΄λμ μ·¨νκ±°λ λ¬΄λ¨ λ°°ν¬ν  κ²½μ° λ²μ μΌλ‘ λ¬Έμ λ  μ μμ΅λλ€.

