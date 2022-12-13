import os

from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render
from utils.logger import write_log


# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")



def index(request):
    fp = os.getcwd()
    write_log(10,fp)
    #print(os.getcwd())

    return render(request,r"index.html")


def upload(request):
    """
        文件上传的功能
    :param request:
    :return: None

    """
    write_log(10,request.method)
    if request.method == "POST":
        myFile = request.FILES.get("myfile",None)
        fp = os.getcwd() + r"/file"
        f = open(os.path.join(fp,myFile.name),"wb+")

        #分块写入文件
        for chunk in myFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse("文件上传成功！")
    else:
        return render(request, r"index.html")


def click_download(request,fp):
    """
        点击下载按钮下载文件
    :param request:
    :param fp:
    :return:
    """
    try:
        response = FileResponse(open(fp,'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment;filename=' + os.path.basename(fp)
        return response
    except Exception:
        raise Http404


def switch_docx(request):
    """
        pdf转化为docx的函数
    :param fp: 文件路径
    :param file_name: 文件名称
    :return: 生产docx的文件
    """
    if request.method == "POST":
        file_name = request.POST
        print(file_name)
        write_log(30,request)
        write_log(30,"提交的文件名称是:{}".format(file_name))
        # fp = os.getcwd() + r"/file"
        # fp = os.getcwd() + r"/file"
        # # save_fp = fp +'/'+ file_name + ".docx"
        # cv = Converter(fp + "/" +file_name)
        # cv.convert(fp + file_name,start = 0,end=None)
        # cv.close
        return HttpResponse("111")

