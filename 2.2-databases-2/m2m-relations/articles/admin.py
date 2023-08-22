from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = 0

        for form in self.forms:
            if form.cleaned_data['is_main']:
                flag += 1
        
        if flag == 0:
            raise ValidationError('Определите основоной тег')

        if flag > 1:
            raise ValidationError('Определите Один основоной тег')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


