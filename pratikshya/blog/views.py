from django.shortcuts import render,get_object_or_404,redirect
from .forms import Journalform
from .models import Journal
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView,
    )



class JournalCreateView(CreateView):
	template_name = "blog/journal_create.html"
	form_class = Journalform
	queryset = Journal.objects.all()
	success_url ='/'

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)


class JournalListView(ListView):
	template_name = "blog/journal_list.html"
	queryset = Journal.objects.all()


class JournalUpdateView(UpdateView):
	template_name = "blog/journal_create.html"
	form_class = Journalform

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Journal,id=id_)


	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)




class JournalDeleteView(DeleteView):
	template_name = "blog/journal_delete.html"

	def get_object(Self):
		id_ = self.kwargs.get(id=id_)
		return get_object_or_404(Journal,id=id_)


	
	def get_success_url(self):
		return reverse("blog:journal_list")



class JournalDetailView(DetailView):
	template_name = "blog/journal_detail.html"


	def get_object(self):
		id_ = self.kwargs.get(id=id_)
		return get_object_or_404(Journal,id=id_)



























'''class JournalCreateView(View):
	template_name = "blog/journal_create.html"

	def get(self,request,*args,**kwargs):
		form = Journalform()
		context = { 'form' : form }
		return render(request,self.template_name,context)

	
	def post(self,request,*args,**kwargs):
		form = Journalform(request.POST)
		if form.is_valid():
			form.save()
		context = { 'form' : form }
		return render(request.self.template_name,context)


class JournalListView(View):
	template_name = "blog/journal_list.html"

	def get(self,request,*args,**kwargs):
		obj = Journal.objects.all()
		context = { 'object_list' : obj }
		return render(request,self.template_name,context)



class JournalDetailView(View):
	template_name = "blog/journal_detail.html"

	def get(self,request,*args,**kwargs):
		obj = get_object_or_404(Journal,id=id)
		context = { 'object_list' : obj }
		return render(request,self.template_name,context)



class JournalUpdateView(View):
	template_name = "blog/journal_create.html"

	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Journal,id=id)
		return obj

	
	def get(self,request,id=None,*args,**kwargs):
		context = { }
		obj = self.get_object()
		if obj is not None:
			form = Journalform(instance = obj)
			context['object'] = obj
			context['form'] = form
		return render(request,self.template_name,context)

	
	def post(self,request,id=None,*args,**kwargs):
		context = { }
		obj = self.get_object()
		if obj is not None:
			form =Journalform(request.POST,instance = obj)
			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request,self.template_name,context)
		


def journal_list_view(request):
	queryset = Journal.objects.all()
	context = { 'object_list' : queryset }
	return render(request,'blog/journal_list.html',context)



def journal_detail_view(request ,id):
	obj = get_object_or_404(Journal,id=id)
	context = { 'object' : obj }
	return render(request,'blog/journal_detail.html',context)



def journal_create_view(request):
	form = Journalform(request.POST or None)
	if form.is_valid():
		form.save()
	context = { 'form' : form }
	return render(request,'blog/journal_create.html',context)


def journal_update_view(request,id=id):
	obj = get_object_or_404(Journal,id=id)
	form = Journalform(request.POST or None , instance = obj)
	if form.is_valid():
		form.save()
	context = { 'form' : form }
	return render(request,'blog/journal_create.html',context)	


def journal_delete_view(request,id):
	obj = get_object_or_404(Journal,id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = { 'object' : obj }
	return render(request,'blog/journal_delete.html',context) '''







