from django.shortcuts import render
from django.http import HttpResponse
from docxtpl import DocxTemplate

def index(request):
    return render(request, 'hello/authorization/index.html')

def first_page(request):
    values = {"count": 5}
    return render(request, 'hello/firstPage/firstPage.html', values)

def work_permit(request):
    return render(request, 'hello/workPermit/workPermit.html')

def current_permit(request):
    return render(request, 'hello/currentWorkPermits/currentWork.html')


def insert_into_doc(manager, managerPost, executor, executorPost,
                    countMember, member, work, dateStart, timeStart, dateEnd,
                    timeEnd, conditions, director, directorPost,
                    personal, personalPost):
    doc = DocxTemplate("C:\\Users\\Сергей\\Desktop\\диплом\\test.docx")
    context = {
                'manager': manager,
                'managerPost': managerPost,
                'executor': executor,
                'executorPost': executorPost,
                'countMember': countMember,
                'member': member,
                'work': work,
                'dateStart': dateStart,
                'timeStart': timeStart,
                'dateEnd': dateEnd,
                'timeEnd': timeEnd,
                'conditions': conditions,
                'director': director,
                'directorPost': directorPost,
                'personal': personal,
                'personalPost': personalPost
    }
    doc.render(context)
    doc.save("final.docx")
    return {"message": "sucessy"}




def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные

    #Можно сделать класс Руководитель, производитель
    manager = request.POST.get("manager")
    managerPost = request.POST.get("managerPost")

    #Производитель
    executor = request.POST.get("executor")
    executorPost = request.POST.get("executorPost")

    #Член бригады
    countMember = request.POST.get("countMember")
    member = request.POST.get("member")

    # #Работа
    work = request.POST.get("work")
    dateStart = request.POST.get("dateStart")
    timeStart = request.POST.get("timeStart")

    dateEnd = request.POST.get("dateEnd")
    timeEnd = request.POST.get("timeEnd")

    conditions = request.POST.get("conditions")

    director = request.POST.get("director")
    directorPost = request.POST.get("directorPost")

    personal = request.POST.get("personal")
    personalPost = request.POST.get("personalPost")


    insert_into_doc(manager, managerPost, executor, executorPost,
                    countMember, member, work, dateStart, timeStart, dateEnd,
                    timeEnd, conditions, director, directorPost,
                    personal, personalPost)

    return HttpResponse(f'Руководитель: {manager}, Производитель: {executor}, '
                        f'Количество членов бригады: {countMember}, Члены бригады: {member},'
                        f'{work}')
