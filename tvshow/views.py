from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

#не полная информация
def tvshow_view(requests):
    show = models.TvShow.objects.all()
    return render(requests, 'tvshow.html', {'show': show})


#детальная информация
def tvshow_detail_view(request, id):
    show_id = get_object_or_404(models.TvShow, id=id)
    return render(request, 'tvshow_detail.html', {'show_id': show_id})


#добавление шоу
def add_tv_show_view(request):
    method = request.method
    if method == 'POST':
        form = forms.TvShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм Успешно добавлен')

    else:
        form = forms.TvShowForm()

    return render(request, 'add_tv_show.html', {'form': form})

#Изменение шоу
def update_tv_show(request, id):
    show_object = get_object_or_404(models.TvShow, id=id)
    if request.method == 'POST':
        form = forms.TvShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно обновлено!!!')
    else:
        form = forms.TvShowForm(instance=show_object)

    return render(request, 'update_tv.html',
                  {
                      'form': form,
                      'object': show_object
                  }
                  )


#Удаление
def delete_tv_show(request,id):
    show_object = get_object_or_404(models.TvShow,
                                    id=id)
    show_object.delete()
    return HttpResponse('Успешно удален!!!')





