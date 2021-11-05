from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from turist.models import Turist, Category
from turist.forms import CreateTuristForm


# Create your views here.
# Create your views here.
def import_data(request):
    import csv
    import os

    settings_dir = os.path.dirname(__file__)
    # print(settings_dir)
    # path = settings_dir + "\ourism.csv"
    info = ''
    categories = {}
    with open(settings_dir + "\category.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            categories[row[0]] = Category.objects.create(
                pk=int(row[0]),
                name=row[1]
            )
            info = f"{info}\n{row[0]}. {row[1]}"

    info = info + "\n\n\n"
    with open(settings_dir + "\ourism.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            Turist.objects.create(
                name=row[1],
                content=row[2],
                rasmi=row[0],
                category=categories[row[4]]
            )
            info = f"{info}\n {row[1]}\n"
    return HttpResponse("Success")


def get_product(request):
    categories = Category.objects.all()
    products = Turist.objects.all()
    products_by = {}
    for c in categories:
        lst = []
        for p in products:
            if c == p.category:
                lst.append(p)
        if len(lst) != 0:
            products_by[c.name] = lst
    context = {
        "categories": categories,
        "products_by": products_by}
    return render(request, 'traveluz/turist.html', context)


def get_by_category_id(request, category_id):
    categories = Category.objects.all()
    products = Turist.objects.filter(category=category_id)
    products_by = {}
    for c in categories:
        lst = []
        for p in products:
            if c == p.category:
                lst.append(p)
        if len(lst) != 0:
            products_by[c.name] = lst
    context = {
        "categories": categories,
        "products_by": products_by}
    return render(request, 'traveluz/turist.html', context)


class CreateTuristView(CreateView):
    template_name = 'traveluz/create.html'
    form_class = CreateTuristForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        return context

