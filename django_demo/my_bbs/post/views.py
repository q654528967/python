from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls.converters import IntConverter
from django.utils.decorators import method_decorator
from django.views import View
from .post_service import add_comment_to_topic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Topic, Comment
from .post_service import build_topic_base_info, build_comment_info, build_topic_detail_info


# Create your views here.


class FirstView(View):
    html = '(%s) Hello Django BBS'

    def get(self, request):
        return HttpResponse(self.html % 'GET')

    def post(self, request):
        return HttpResponse(self.html % 'POST')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FirstView, self).dispatch(request, *args, **kwargs)


def dynamic_hello(request, year, month, day):
    html = '<h1>(%s) Hello Django BBS'
    return HttpResponse(html % ('%s-%s-%s' % (year, month, day)))


class MonthConverter(IntConverter):
    regex = """0?[1-9]|1[0-2]"""


def topic_list_view(request):
    """
    话题列表
    :param request:
    """
    topic_qs = Topic.objects.all()
    for topic in topic_qs:
        print(topic.created_time)
    result = {
        'count': topic_qs.count(),
        'info': [build_topic_base_info(topic) for topic in topic_qs]
    }
    return JsonResponse(result)


def topic_detail_view(request, topic_id):
    """
    话题详情视图函数
    :param request:
    :param topic_id:
    :return:
    """
    result = {}
    try:
        result = build_topic_detail_info(Topic.objects.get(pk=topic_id))
    except Topic.DoesNotExist:
        pass
    return JsonResponse(result)


@csrf_exempt
def add_comment_to_topic_view(request):
    topic_id = int(request.POST.get('id', 0))
    content = request.POST.get('content', '')
    topic = None

    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        pass
    if topic and content:
        return JsonResponse({'id': add_comment_to_topic(topic, content).id})

    return JsonResponse({})
