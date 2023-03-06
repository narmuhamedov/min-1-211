from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

#не полная информация

class TvShowView(generic.ListView):
    template_name = 'tvshow.html'
    queryset = models.TvShow.objects.all

    def get_queryset(self):
        return models.TvShow.objects.all()

# def tvshow_view(requests):
#     show = models.TvShow.objects.all()
#     return render(requests, 'tvshow.html', {'show': show})


#детальная информация
class TvShowDetailView(generic.DetailView):
    template_name = 'tvshow_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=show_id)

# def tvshow_detail_view(request, id):
#     show_id = get_object_or_404(models.TvShow, id=id)
#     return render(request, 'tvshow_detail.html', {'show_id': show_id})


#добавление шоу
class TvShowCreateView(generic.CreateView):
    template_name = 'add_tv_show.html'
    form_class = forms.TvShowForm
    queryset = models.TvShow.objects.all()
    success_url = '/tvshow/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView, self).form_valid(form=form)

# def add_tv_show_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.TvShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Фильм Успешно добавлен')
#
#     else:
#         form = forms.TvShowForm()
#
#     return render(request, 'add_tv_show.html', {'form': form})

#Изменение шоу
class TvShowUpdateView(generic.UpdateView):
    template_name = 'update_tv.html'
    form_class = forms.TvShowForm
    success_url = '/tvshow/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=show_id)

    def form_valid(self, form):
        return super(TvShowUpdateView, self).form_valid(form=form)


# def update_tv_show(request, id):
#     show_object = get_object_or_404(models.TvShow, id=id)
#     if request.method == 'POST':
#         form = forms.TvShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно обновлено!!!')
#     else:
#         form = forms.TvShowForm(instance=show_object)
#
#     return render(request, 'update_tv.html',
#                   {
#                       'form': form,
#                       'object': show_object
#                   }
#                   )
#

#Удаление
class TvShowDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = "/tvshow/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.TvShow, id=show_id)
# def delete_tv_show(request,id):
#     show_object = get_object_or_404(models.TvShow,
#                                     id=id)
#     show_object.delete()
#     return HttpResponse('Успешно удален!!!')
#




