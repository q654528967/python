from .models import Comment


def build_topic_base_info(topic):
    """
    构造Topic基本信息
    :param topic:
    """
    return {
        'id': topic.id,
        'title': topic.title,
        'user': topic.user.username,
        'created_time': topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    }


def build_comment_info(comment):
    """
    构造Topic详细信息
    :param comment:
    :return:
    """
    return {
        'id': comment.id,
        'content': comment.content,
        'up': comment.up,
        'down': comment.down,
        'created_time': comment.created_time.strftime('%Y-%m-%d %H:%M:%S'),
        'last_modified': comment.last_modified.strftime('%Y-%m-%d %H:%M:%S')
    }


def build_topic_detail_info(topic):
    """
    话题详情
    :param topic:
    :return:
    """
    comment_qs = Comment.objects.filter(topic=topic)
    return {
        'id': topic.id,
        'title': topic.title,
        'user': topic.user.username,
        'created_time': topic.created_time.strftime('%Y-%m-%d %H:%M:%S'),
        'last_modified': topic.last_modified.strftime('%Y-%m-%d %H:%M:%S'),
        'comments': [build_comment_info(comment) for comment in comment_qs]
    }


def add_comment_to_topic(topic, content):
    return Comment.objects.create(topic=topic, content=content)
