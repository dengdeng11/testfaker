from django.shortcuts import render
import faker

f = faker.Faker("zh_CN")

#��ȡ���֤��
def getIdcard(request):
    name = f.name()
    phone = f.phone_number()
    idcard = f.ssn()

    context = {}
    context["name"] = name
    context["phone"] = phone
    context["idcard"] = idcard
    return render(request, 'index.html', context)