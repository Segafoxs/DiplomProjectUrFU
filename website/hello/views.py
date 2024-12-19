from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django_filters import FilterSet
from django_filters.views import FilterView
from django_tables2 import SingleTableView, SingleTableMixin

from .myModels import Work_is_mymodel, Manager_is_mymodel, Executor_is_mymodel, Director_is_mymodel, Permit_is_mymodel, ShiftManager_is_mymodel
from .myFunc import insert_into_doc
from .dbFunc import select_in_db

from .models import Employee, Permit, Department

from .forms import LinePermit, ChoiceDirector, ChoiceManager, DepartmentForm
from .tables import PersonTable
from .filters import MyFilter
import random

user_from_permit = {}

class ListViews(SingleTableMixin, FilterView):
    model = Permit
    table_class = PersonTable
    template_name = 'hello/currentWorkPermits/currentWork.html'
    filterset_class = MyFilter




def authFunc(request):

    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/currentPermit/")
        else:
            return HttpResponse("<h2>{\nmessage: Неверный логин или пароль}</h2>", status=401, reason="Incorrect data")

    return render(request, 'hello/authorization/index.html')

def first_page(request):
    values = {"count": 5}
    return render(request, 'hello/firstPage/firstPage.html', values)

def work_permit(request):

    form_department = DepartmentForm()

    context = {
        "form_department": form_department,
    }
    return render(request, 'hello/workPermit/workPermit.html', context)


def docx_sign(request):
    latest_permit_list = Permit.objects.filter(status="approval")
    if latest_permit_list:
        for id in latest_permit_list:
            id_master = id.master_of_work_id
            master = Employee.objects.get(id=id_master)

            context = {
                "permit_list": latest_permit_list,
                "master": master
            }
            return render(request, 'hello/docsSign/docsSign.html', context)
    return render(request, 'hello/docsSign/docsSign.html')




def lists(request):
    model = Permit.objects.all()
    filterset_class = MyFilter(request.GET, model)
    table = PersonTable(filterset_class.qs)
    return render(request=request, template_name='hello/currentWorkPermits/currentWork.html',
                  context={"model":model, "table":table, "filterset_class":filterset_class})

def current_permit(request):
    latest_permit_list = Permit.objects.filter(status="work")
    if latest_permit_list:
        for id in latest_permit_list:
            id_master = id.master_of_work_id
            master = Employee.objects.get(id=id_master)

            context = {
                "permit_list": latest_permit_list,
                "master": master
            }
            return render(request, 'hello/currentWorkPermits/currentWork.html', context)
    return render(request, 'hello/currentWorkPermits/currentWork.html')


def postDirector(request):

    try:
        if request.method == "POST":
            search_query = request.POST.get('search_director')
            user_from_db = select_in_db(search_query)
            if user_from_db is not None:
                for user in user_from_db:
                    post = user.role
                    if user.role != "DIRECTOR":
                        return HttpResponse(f"{post} не может выдавать наряд-допуск")
                    director_id = user.id
                    user_from_permit['director'] = director_id

                    # insert_into_doc(manager)
                    print(f'{user.id} {user.name} {user.role}')
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
                if user.role != "MASTER":
                    return HttpResponse("Руководитель не может быть из числа рабочих")
                manager_id = user.id
                user_from_permit['manager'] = manager_id

                # insert_into_doc(manager)
                print(f'{user.id} {user.name} {user.role}')
        else:
            return HttpResponse("USER IS NOT FOUND")

        return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': user_from_db})
    return render(request, "hello/workPermit/searchUser.html", {})


def postExecutor(request):
    if request.method == "POST":
        search_query = request.POST.get('search_executor')
        user_from_db = select_in_db(search_query)
        if user_from_db is not None:
            for user in user_from_db:
                executor_id = user.id

                user_from_permit['executor'] = executor_id

                # insert_into_doc(executor)
                print(f'{user.id} {user.name} {user.role}')
        else:
            return HttpResponse("USER IS NOT FOUND")

        return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': user_from_db})
    return render(request, "hello/workPermit/searchUser.html", {})


def postShiftManager(request):

    try:
        if request.method == "POST":
            search_query = request.POST.get('search_shiftManager')
            users = select_in_db(search_query)
            if users is not None:
                for user in users:
                    shiftManager_id = user.id

                    user_from_permit['shiftManager'] = shiftManager_id

                    # insert_into_doc(executor)
                    print(f'{user.id} {user.name} {user.role}')
            else:
                return HttpResponse("USER IS NOT FOUND")

            return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': users})
        return render(request, "hello/workPermit/searchUser.html", {})
    except Exception as err:
        return HttpResponse(f"{err}")

def postStateEngineer(request):

    try:
        if request.method == "POST":
            search_query = request.POST.get('search_state_engineer')
            users = select_in_db(search_query)
            if users is not None:
                for user in users:
                    stateEngineer_id = user.id

                    user_from_permit['stateEngineer'] = stateEngineer_id

                    # insert_into_doc(executor)
                    print(f'{user.id} {user.name} {user.role}')
            else:
                return HttpResponse("USER IS NOT FOUND")

            return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': users})
        return render(request, "hello/workPermit/searchUser.html", {})
    except Exception as err:
        return HttpResponse(f"{err}")

def postWorker(request):

    try:
        if request.method == "POST":
            search_query = request.POST.get('search_worker')
            users = select_in_db(search_query)
            if users is not None:
                for user in users:
                    worker_id = user.id

                    user_from_permit['worker'] = worker_id

                    # insert_into_doc(executor)
                    print(f'{user.id} {user.name} {user.role}')
            else:
                return HttpResponse("USER IS NOT FOUND")

            return render(request, "hello/workPermit/searchUser.html", {'query': search_query, 'user': users})
        return render(request, "hello/workPermit/searchUser.html", {})
    except Exception as err:
        return HttpResponse(f"{err}")

def resultPermit(request):

    try:

        if request.method == "POST":

            new_permit = Permit()
            new_permit.number = request.POST.get("number_permit")
            #new_permit.type_of_permit = "LINEAR"

            new_permit.department = Department.objects.get(id=request.POST.get("department"))
            new_permit.master_of_work = Employee.objects.get(id=user_from_permit['manager'])
            # #new_permit.master_signature
            new_permit.executor = Employee.objects.get(id=user_from_permit['executor'])
            new_permit.daily_manager = Employee.objects.get(id=user_from_permit['shiftManager'])
            new_permit.station_engineer = Employee.objects.get(id=user_from_permit['stateEngineer'])
            new_permit.employ = Employee.objects.get(id=user_from_permit['worker'])
            new_permit.director = Employee.objects.get(id=user_from_permit['director'])

            new_permit.work_description = request.POST.get("work")
            new_permit.start_of_work = request.POST.get("dateStart")
            new_permit.end_of_work = request.POST.get("dateEnd")
            new_permit.condition = request.POST.get("conditions")



            new_permit.to_docx()
            data = Permit(number=new_permit.number, master_of_work=new_permit.master_of_work,
                          executor=new_permit.executor, director=new_permit.director,
                          station_engineer=new_permit.station_engineer, work_description=new_permit.work_description,
                          start_of_work=new_permit.start_of_work, end_of_work=new_permit.end_of_work)
            data.save()
            return HttpResponse("SUC")

        #     #Тут собираем данные о месте проведении работы и датах
        #     work = Work_is_mymodel()
        #     work.name = request.POST.get("work")
        #     work.dateStart = request.POST.get("dateStart")
        #     work.timeStart = request.POST.get("timeStart")
        #     work.dateEnd = request.POST.get("dateEnd")
        #     work.timeEnd = request.POST.get("timeEnd")
        #
        #     #Особые условия
        #     conditions = request.POST.get("conditions")
        #
        #     #Дата выдачи наряда, тут надо сделать функцию присвоения наряду номера!!!!!!!
        #     permit = Permit_is_mymodel()
        #     permit.dateDelivery = request.POST.get("dateDelivery")
        #     permit.timeDelivery = request.POST.get("timeDelivery")



            #return render(request, "hello/workPermit/resultWorkPermit.html", {"permit": new_permit})
    except KeyError:
        return HttpResponse("<h1>Заполните все поля<h1>")

    except Exception as err:
        return HttpResponse(f"{err}")


def add_permit_in_bd(request):

    pass


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