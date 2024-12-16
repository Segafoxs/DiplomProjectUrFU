from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from docxtpl import DocxTemplate
from .myModels import Work, Manager, Executor, Director, Permit, ShiftManager

def insert_into_doc(manager, executor, countMember, member, work, permit, director, personal):
    doc = DocxTemplate("C:\\Users\\Сергей\\Desktop\\диплом\\test.docx")
    context = {
                'manager': manager.name,
                'managerPost': manager.post,
                'executor': executor.name,
                'executorPost': executor.post,
                'countMember': countMember,
                'member': member,
                'work': work.name,
                'dateStart': work.dateStart,
                'timeStart': work.timeStart,
                'dateEnd': work.dateEnd,
                'timeEnd': work.timeEnd,
                'dateDelivery': permit.dateDelivery,
                'timeDelivery': permit.timeDelivery,
                'conditions': permit.conditions,
                'director': director.name,
                'directorPost': director.post,
                'personal': personal.name,
                'personalPost': personal.post
    }
    doc.render(context)
    doc.save("final.docx")
    return {"message": "success"}


