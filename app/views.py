from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


def lotto(request):
    # 1~49 不重覆六個數字跟排序
    numbers = random.sample(range(1, 50), 6)
    spec_number = random.randint(1, 49)
    numbers = sorted(numbers)
    # numbers = " ".join([str(i) for i in numbers])
    numbers = " ".join(map(str, numbers))
    # 將numbers串成字串輸出跟排序

    result = {"numbers": numbers, "spec_number": spec_number}

    return render(request, "lotto.html", result)


# Create your views here.
def hello(request):
    result = {"message": "測試!", "data": 123, "label": "文字標籤"}
    return JsonResponse(result)
