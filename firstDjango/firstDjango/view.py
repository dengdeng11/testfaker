from django.http import HttpResponse

import faker
f = faker.Faker("zh_CN")

def hello(request):
    name = f.name()
    phone = f.phone_number()
    idcard = f.ssn()
    date = "name: " + name + '\n' + ", number: " + phone + ", idCard: " + idcard

    return HttpResponse(date)