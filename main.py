#Лытов Михаил ККСО-03-20
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/library")
def libary_page():
    return {"авторы": "Михаил_Булгаков, Эрих_Мария_Ремарк, А_С_Пушкин"}
@app.get("/library/{author}")
def libary_author(author):

    if author == "А_С_Пушкин":
        return {"А_С_Пушкин": "Керн, Сожженное_письмо, Признание"}
    if author == "Эрих_Мария_Ремарк":
        return {"Эрих_Мария_Ремарк": "Три_товарища, обичай_ближния_си"}
    if author == "Михаил_Булгаков":
        return{"Михаил_Булгаков": "Дон_Кихот, Египетская_мумия, Записи_на_манжетаках"}
    if author != "Михаил_Булгаков" and author != "Эрих_Мария_Ремарк" and author != "А_С_Пушкин":
        return {"error" : "404"}
@app.get("/library/{author}/{work}")
#127.0.0.1:8000/library/{author}/{work}?begin=a&end=b
def libary_author_work(author,work,begin: str=None, end: str=None):
    if author == "Михаил_Булгаков":
        if work == 'Дон_Кихот':
            file = open('Дон_Кихот.txt',"r")
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return arr[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return arr[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work == "Египетская_мумия":
            file = open('Египетская_мумия.txt',"r")
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return arr[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return arr[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work == "Записи_на_манжетаках":
            file = open('Записи_на_манжетаках.txt',"r")
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return arr[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return v[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work != 'Дон_Кихот' and work != 'Египетская_мумия' and work != 'Записи_на_манжетаках':
            return{"error": "404"}
    if author == "Эрих_Мария_Ремарк":
        if work == "Три_товарища":
            file = open('Три_товарища.txt',"r")
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return arr[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return arr[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work =="обичай_ближния_си":
            file = open('обичай_ближния_си.txt')
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return arr[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return arr[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work != "Три_товарища" and work != "обичай_ближния_си":
            return {"error": "404"}
    if author == "А_С_Пушкин":
        if work == 'Керн':
            file = open('Керн.txt',"r")
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return str[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return str[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work == 'Сожженное_письмо':
            file = open('Сожженное_письмо.txt',"r")
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return arr[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return arr[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work == 'Сожженное_письмо':
            file = open('Признание.txt',"r")
            arr = file.read()
            file.close()
            if begin != None and end == None:
                a = arr.find(begin)
                return arr[a:].split('\n')
            if begin != None and end != None:
                a = arr.find(begin)
                b = arr.find(end,a)
                return arr[a:b].split('\n')
            if begin == None and end != None:
                b = arr.find(end)
                return arr[:b].split('\n')
            if begin == None and end == None:
                return arr.split('\n')
        if work != "Керн" and work != "Сожженное_письмо" and work != "Признание":
            return {"error": "404"} 

if __name__ == "__main__":
    uvicorn.run(app)
