from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from .myModels import Work, Manager, Executor, Director, Permit, ShiftManager
from .myFunc import insert_into_doc
from .dbFunc import select_in_db
from .models import Employee

from .forms import LinePermit, ChoiceDirector, ChoiceManager

user_from_permit = {}

def authFunc(request):

    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/welcomePage/")
        else:
            return HttpResponse("<h2>{\nmessage: Неверный логин или пароль}</h2>", status=401, reason="Incorrect data")

    return render(request, 'hello/authorization/index.html')

def first_page(request):
    values = {"count": 5}
    return render(request, 'hello/firstPage/firstPage.html', values)

def work_permit(request):
    return render(request, 'hello/workPermit/workPermit.html')

def current_permit(request):
    return render(request, 'hello/currentWorkPermits/currentWork.html')


def postDirector(request):

    try:
        if request.method == "POST":
            search_query = request.POST.get('search_director')
            user_from_db = select_in_db(search_query)
            if user_from_db is not None:
                for user in user_from_db:
                    post = user.postemploee
                    if user.postemploee != "Начальник цеха":
                        return HttpResponse(f"{post} не может выдавать наряд-допуск")
                    director = Director(user.name, user.postemploee)
                    user_from_permit['director'] = director

                    # insert_into_doc(manager)
                    print(f'{director.name} {director.postemploee}')
            else:
                return HttpResponse("USER IS NOT FOUND")

            return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': user_from_db})
        return render(request, "hello/workPermit/searchUser.html", {})
    except KeyError:

        return HttpResponse("Заполните все поля")
    except Exception as err:
        print(f"{err}")
        return HttpResponse(f"Unexpected {err=}, {type(err)=}")


def postManager(request):
    if request.method == "POST":
        search_query = request.POST.get('search_manager')
        user_from_db = select_in_db(search_query)
        if user_from_db is not None:
            for user in user_from_db:
                if user.postemploee != "Мастер":
                    return HttpResponse("Руководитель не может быть из числа рабочих")
                manager = Manager(user.name, user.postemploee)
                user_from_permit['manager'] = manager

                # insert_into_doc(manager)
                print(f'{manager.name} {manager.postemploee}')
        else:
            return HttpResponse("USER IS NOT FOUND")

        return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': user_from_db})
    return render(request, "hello/workPermit/searchUser.html", {})


def postExecutor(request):
    if request.method == "POST":
        search_query = request.POST.get('search_executor')
        users = select_in_db(search_query)
        if users is not None:
            for user in users:
                executor = Executor(user.name, user.postemploee)

                user_from_permit['executor'] = executor

                # insert_into_doc(executor)
                print(f'{executor.name} {executor.postemploee}')
        else:
            return HttpResponse("USER IS NOT FOUND")

        return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': users})
    return render(request, "hello/workPermit/searchUser.html", {})


def postShiftManager(request):

    try:
        if request.method == "POST":
            search_query = request.POST.get('search_shiftManager')
            users = select_in_db(search_query)
            if users is not None:
                for user in users:
                    shiftManager = ShiftManager(user.name, user.postemploee)

                    user_from_permit['shiftManager'] = shiftManager

                    # insert_into_doc(executor)
                    print(f'{shiftManager.name} {shiftManager.postemploee}')
            else:
                return HttpResponse("USER IS NOT FOUND")

            return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': users})
        return render(request, "hello/workPermit/searchUser.html", {})
    except Exception as err:
        return HttpResponse(f"{err}")


def resultPermit(request):

    try:
        if request.method == "POST":
            userDirector = user_from_permit['director']
            userManager = user_from_permit['manager']
            userExecutor = user_from_permit['executor']
            userShiftManager = user_from_permit['shiftManager']

            #Тут собираем данные о месте проведении работы и датах
            work = Work()
            work.name = request.POST.get("work")
            work.dateStart = request.POST.get("dateStart")
            work.timeStart = request.POST.get("timeStart")
            work.dateEnd = request.POST.get("dateEnd")
            work.timeEnd = request.POST.get("timeEnd")

            #Особые условия
            conditions = request.POST.get("conditions")

            #Дата выдачи наряда, тут надо сделать функцию присвоения наряду номера!!!!!!!
            permit = Permit()
            permit.dateDelivery = request.POST.get("dateDelivery")
            permit.timeDelivery = request.POST.get("timeDelivery")



            return render(request, "hello/workPermit/resultWorkPermit.html", {'directorPost': userDirector.postemploee, 'directorName': userDirector.name,
                                                                              'managerPost': userManager.postemploee, 'managerName': userManager.name,
                                                                              'executorPost': userExecutor.postemploee, 'executorName': userExecutor.name,
                                                                              'shiftManagerPost': userShiftManager.postemploee, 'shiftManagerName': userShiftManager.name,
                                                                              'work': work, 'conditions': conditions,
                                                                              'permit': permit})
    except KeyError:
        return HttpResponse("<h1>Заполните все поля<h1>")

    except Exception as err:
        return HttpResponse(f"{err}")


def firePermit(request):

    if request.method == "POST":
        name = request.POST.get("your_name")
        post = request.POST.get("your_post")
        return HttpResponse(f"<h1>{name} {post}</h1>")
    else:
        userForm = LinePermit()
        return render(request, "hello/firePermit/firePermit.html", {"forms": userForm})


    #return render(request, "hello/firePermit/firePermit.html", {"form": userForm})





    # получаем из данных запроса POST отправленные через форму данные

    #Можно сделать класс Руководитель, производитель
    # manager = Manager()
    # manager.name = request.POST.get("manager")
    # manager.post = request.POST.get("managerPost")
    #
    # #Производитель
    # executor = Executor()
    # executor.name = request.POST.get("executor")
    # executor.post = request.POST.get("executorPost")
    #
    # #Член бригады
    # countMember = request.POST.get("countMember")
    # member = request.POST.get("member")
    #
    # # #Работа
    # work = Work()
    # work.name = request.POST.get("work")
    # work.dateStart = request.POST.get("dateStart")
    # work.timeStart = request.POST.get("timeStart")
    # work.dateEnd = request.POST.get("dateEnd")
    # work.timeEnd = request.POST.get("timeEnd")
    #
    # permit = Permit()
    # permit.dateDelivery = request.POST.get("dateDelivery")
    # permit.timeDelivery = request.POST.get("timeDelivery")
    # permit.conditions = request.POST.get("conditions")
    #
    #
    #
    # director = Director()
    # director.name = request.POST.get("director")
    # director.post = request.POST.get("directorPost")
    #
    # personal = Personal()
    # personal.name = request.POST.get("personal")
    # personal.post = request.POST.get("personalPost")
    #
    #
    # insert_into_doc(manager, executor, countMember, member, work, permit, director, personal)

    # return HttpResponse(f'Руководитель: {manager.name}, Производитель: {executor.name}, '
    #                     f'Количество членов бригады: {countMember}, Члены бригады: {member},'
    #                     f'{work.dateStart}')