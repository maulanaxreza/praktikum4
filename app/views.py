from django.shortcuts import render,redirect
from . import models

# Create your views here.

# 1 : bikin fungsi retrieve objects dari database
def index(reqeust):
    # Ambil data dari pelanggan
    # All
    allpelangganobj = models.pelanggan.objects.all()
    # Get 
    getpelangganobj = models.pelanggan.objects.get(idpelanggan=1)
    # Filter
    filterpelangganobj = models.pelanggan.objects.filter(jeniskelamin = 'Perempuan')

    return render(reqeust,'pelanggan.html',{
        "allpelangganobj" : allpelangganobj,
        'getpelangganobj' : getpelangganobj,
        'filterpelangganobj' : filterpelangganobj
    })
# 2 : Bikin file pelanggan.html di folder templates
# 3 : Bikin fungsi Create data
def createdata(request):
    if request.method == "GET":
        return render(request,'createdata.html')
# 4 : Bikin file createdata.html
    else:
        print(request.POST)
        nama = request.POST['nama']
        tanggal = request.POST['tanggal']
        jeniskelamin = request.POST['jeniskelamin']
        nohp = request.POST['nohp']
        newpelanggan = models.pelanggan(
            nama = nama,
            tanggallahir = tanggal,
            jeniskelamin = jeniskelamin,
            nohp = nohp
        ).save()
# 5 : Jangan lupa tambahin redirect setelah render di line 1
        return redirect('index')
# 6 : Bikin fungsi update data
def updatedata(request,id):
    pelangganobj = models.pelanggan.objects.get(idpelanggan=id)
    if request.method == 'GET':
        return render(request,'updatedata.html',{
            'pelangganobj':pelangganobj
        })
    else:
        nama = request.POST['nama']
        tanggal = request.POST['tanggal']
        jeniskelamin = request.POST['jeniskelamin']
        nohp = request.POST['nohp']
        pelangganobj.nama = nama
        pelangganobj.tanggal = tanggal
        pelangganobj.jeniskelamin = jeniskelamin
        pelangganobj.nohp = nohp
        pelangganobj.save()

        return redirect('index')
# 7 : Bikin fungsi delete data
def deletedata(request,id):
    pelangganobj = models.pelanggan.objects.get(idpelanggan = id)
    pelangganobj.delete()
    return redirect('index')