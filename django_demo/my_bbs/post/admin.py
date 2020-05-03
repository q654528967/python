from django.contrib import admin
from .models import Topic, Comment
from django.utils.translation import ugettext_lazy as _

# Register your models here.

# admin.site.register([Topic, Comment])


class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    # 增加Changelist动作
    actions = ['topic_online', 'topic_offline']
    # ChangeList 显示字段
    list_display = ('title', 'content', 'topic_is_online', 'user', 'created_time')
    # ChangeList 搜索栏设置
    search_fields = ['^title', '=user__username']
    # 设置ChangeForm想显示字段
    # fields = ['user', 'title', 'is_online']
    # fields小技巧
    # fields = [('user', 'title'), 'content', 'is_online']
    # 设置ChangeForm不想显示的字段
    # exclude = ['content']
    # 第一种ChangeList排序方式
    # ordering = ['id']
    # 设置每页的要显示的数量
    # list_per_page = 2
    # 设置的总页数小于实际总页数，所以显示全部不显示
    # list_max_show_all = 2
    # 利用readonly_fields将部分字段设置为只读
    # readonly_fields = ('user', 'title', 'content_length')
    # raw_id_fields = ('user',)
    #
    # def content_length(self, obj):
    #     return len(obj.content)
    # content_length.short_description = u'话题内容长度'
    # fields = [('user', 'title'), 'is_online', 'content_length']
    # readonly_fields = ('user', 'content', 'content_length')
    #
    # def content_length(self, obj):
    #     return len(obj.content)
    #
    # content_length.short_description = u'话题内容长度'
    # 用fieldsets自定义ChangeForm
    # fieldsets = (
    #     ('Topic Part A', {
    #         'fields': ('title', 'user'),
    #         'description': 'Topic 的 title 和 user'
    #     }),
    #     ('Topic Part B', {
    #         'fields': ('content', 'is_online'),
    #         'classes': ['collapse', 'wide'],
    #         'description': 'Topic 的 content 和 is_online'
    #     })
    # )
    # 自定义ChangeList显示数据
    # def get_queryset(self, request):
    #     return self.model._default_manager.filter(title__contains='first')

    # 第二种ChangeList排序方式
    # def get_ordering(self, request):
    #     if request.user.is_superuser:
    #         return ['id']
    #     else:
    #         return self.ordering

    def save_model(self, request, obj, form, change):
        if change and 'is_online' in form.changed_data and not obj.is_online:
            self.message_user(request, 'Topic (%s) 被管理员删除了' % obj.id)
            obj.title = '%s (%s)' % (obj.title, '管路员删除了')
        super(TopicAdmin, self).save_model(request, obj, form, change)

    class TitleFilter(admin.SimpleListFilter):
        title = _('标题过滤')
        parameter_name = 'tf'

        def lookups(self, request, model_admin):
            return (
                ('first', _('包含first')),
                ('!first', _('不包含first'))
            )

        def queryset(self, request, queryset):
            if self.value() == 'first':
                return queryset.filter(title__contains=self.value())
            elif self.value() == '!first':
                return queryset.exclude(title__contains=self.value()[1:])
            else:
                return queryset

    list_filter = [TitleFilter, 'user__username']

    def topic_is_online(self, obj):
        return u'是' if obj.is_online else u'否'
    topic_is_online.short_description = u'话题是否在线'

    def topic_content(self, obj):
        return obj.content[:30]
    topic_content.short_description = u'话题内容'

    def topic_online(self, request, queryset):
        rows_updated = queryset.update(is_online=True)
        self.message_user(request, u'%s topics online' % rows_updated)
    topic_online.short_description = u'上线所选的%s' % Topic._meta.verbose_name

    def topic_offline(self, request, queryset):
        rows_updated = queryset.update(is_online=False)
        self.message_user(request, u'%s topics offline' % rows_updated)
    topic_offline.short_description = u'下线所选的%s' % Topic._meta.verbose_name


# admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
