from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import markdown
import random as foo



from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_entry(request,entry):
    x = util.get_entry(entry)
    if x == None:
        return render(request, "encyclopedia/error.html", {"error": "requested page was not found"})
    x = markdown.markdown(x)
    print(x)
    return render(request, "encyclopedia/entry.html", {"entry": x , "title": entry})



def search(request):
    if request.method == 'POST':
        print(request.POST['query'])
        print("___________________________")
    value = request.POST['query']
    entry_list = util.list_entries()
    for i in range(len(entry_list)):
        entry_list[i] =entry_list[i].lower()
    value = value.lower()
    if value in entry_list:
        return redirect('/wiki/'+value)
    else:
        return_list = []
        for i in entry_list:
            if value in i:
                return_list.append(i)
        if len(return_list) > 0 :
            return render(request, "encyclopedia/search.html", {"search": return_list,"error": "None"})
    return render(request, "encyclopedia/search.html", {"search": 'None' , "error": 'no entry found'})

def create(request):
    return render(request, "encyclopedia/create.html")

def check_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        entry = request.POST['entry']
        entry_list = util.list_entries()
        for i in range(len(entry_list)):
            entry_list[i] =entry_list[i].lower()
        if title.lower() in  entry_list:
            return render(request, "encyclopedia/error.html",{'error' : 'the page alrady exist'})
        else:
            util.save_entry(title,entry)
            return redirect('/wiki/'+title)
    
    return render(request, "encyclopedia/create.html")

def edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        x = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {"entry": x.replace("\n",''), "title": title})
    else:
        return render(request, "encyclopedia/error.html",{'error' : 'the page alrady exist'})

def edit_submit(request):
    if request.method == 'POST':
        title = request.POST['title']
        entry = request.POST['entry']
        print(entry)
        util.save_entry(title, entry)
        return redirect('/wiki/'+title)
    else:
        return render(request, "encyclopedia/error.html",{'error' : 'the page alrady exist'})


def random(request):
    x = util.list_entries()
    print(x)
    print(foo.choice(x))
    y = foo.choice(x)
    return redirect('/wiki/'+ y)