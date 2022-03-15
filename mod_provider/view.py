from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import render

from datetime import datetime
import time
from os import walk
from urllib.parse import quote_plus
import urllib.request

# def hello(request):
# return HttpResponse("hello!");

JAR_DIR = '/home/qod/mc-server/mods'
CLIENT_ONLY_JAR = '.jarc'


def get_port():
    file = open('mc_port.yaml', 'r')
    text = file.read()
    file.close()

    return text[text.find('port:' + ' ') + 6:]


def get_mods():
    # get all file in JAR_DIR
    for root, dirs, files in walk(JAR_DIR):
        pass
    files.sort()

    for x in files:

        if len(x) < len('.server.jar'):
            pass
        elif x[:x.rfind('.')][-7:] == '.server':
            # print(x,x[:x.rfind('.')][-7:])
            files.remove(x)

    # convert name of jarc to jar
    names = []
    for x in files:
        if x.endswith(CLIENT_ONLY_JAR):
            names.append(x[:-1])
        else:
            names.append(x)
    # convert path to url format
    urls = []
    for x in files:
        urls.append(quote_plus(x))
    # convert name to url format
    url_names = []
    for x in names:
        url_names.append(quote_plus(x))

    # print(urls,'\n',url_names,'\n',names)

    return zip(urls, url_names, names)


def get_time():
    timeStamp = time.time()
    localTime = time.localtime(timeStamp)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)

    return strTime


def file_down(request):
    context = {}
    context['time'] = get_time()
    context['values'] = get_mods()
    context['port'] = get_port()

    # for x,y,z in context['values']:
    #     print(x,y,z)

    return render(request, 'modlist.html', context)


def download(request):
    file_name = request.GET.get('file')
    name = request.GET.get('name')

    try:
        file = open(JAR_DIR + '/' + file_name, 'rb')
    except FileNotFoundError:
        print('Not found Error>>>', JAR_DIR + '/' + file_name)
        return HttpResponse("File not found!")

    response = FileResponse(file)
    response['Content-Type'] = 'application/msword'
    response['Content-Disposition'] = 'attachment;filename=' + name
    return response


# def video(request):
#     html = '''<html>

# <video width="800" height="600" controls>
#   <source src="/media/qod/娱乐/你的名字F.mp4" type="video/mp4">
# 您的浏览器不支持Video标签。
# </video>

# <html/>'''
#     return HttpResponse(html)


"""
def get_html(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    html=response.read()
    return html
"""
