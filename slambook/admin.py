from django.contrib import admin
from .models import (CharacterTemplate,CQuestion,
                     RCTemplateCQuestions,Slams,Slam,SlamChart,
<<<<<<< Updated upstream
                     Answer,UserExtension,Gifts,GiftChart,Gift)
=======
                     Answer,UserExtension,Gifts,GiftChart,Contributor)
>>>>>>> Stashed changes

# Register your models here.

class CharacterTemplateAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(CharacterTemplate)
admin.site.register(CQuestion)
admin.site.register(RCTemplateCQuestions)
admin.site.register(Slams)
admin.site.register(Slam)
admin.site.register(SlamChart)
admin.site.register(Answer)
admin.site.register(Gifts)
admin.site.register(UserExtension)
admin.site.register(GiftChart)
<<<<<<< Updated upstream
admin.site.register(Gift)
=======
admin.site.register(Contributor)
>>>>>>> Stashed changes
