from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Person)
# admin.site.register(models.Advisor)
# admin.site.register(models.Item)
# admin.site.register(models.Report)


class ProductPerson(admin.ModelAdmin):
    model = models.Person
    list_display = ['name', 'age', 'email', 'gender', 'phone_no','password']
class ProductAdvisor(admin.ModelAdmin):
    model = models.Advisor
    list_display = ['name', 'email', 'specification','password']
class ProductItem(admin.ModelAdmin):
    model = models.Item
    list_display = ['item_name', 'category', 'calories', 'vitamin', 'ingredient']
class ProductReport(admin.ModelAdmin):
    model = models.Report
    list_display = ['date', 'total_calories','total_vitamins','consumed_items','total_ingredient' ]



admin.site.register(models.Person,ProductPerson)
admin.site.register(models.Advisor,ProductAdvisor)
admin.site.register(models.Item,ProductItem)
admin.site.register(models.Report,ProductReport)
admin.site.register(models.Favorite_list)
admin.site.register(models.Eaten)
admin.site.register(models.Target)
admin.site.register(models.Feedback)



