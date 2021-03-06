# The MIT License (MIT)
#
# Copyright (c) 2015 pjwards.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==================================================================================
""" Sets admin site """

from django.contrib import admin
from analysis.models import *


class SpamListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group', 'message', 'time', 'status')


class SpamWordAdmin(admin.ModelAdmin):
    list_display = ('group', 'word', 'count', 'status')


class ArchiveAnalysisWordAdmin(admin.ModelAdmin):
    list_display = ('group', 'word', 'count', 'likenum', 'commentnum', 'weigh', 'status')


class AnticipateArchiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'user', 'message', 'time')


class AnalysisDBSchemaAdmin(admin.ModelAdmin):
    list_display = ('group', 'avgpostlike', 'avgpostcomment', 'avgcomtlike', 'avgcomtcomment', 'lastupdatetime')


class UpdateListAdmin(admin.ModelAdmin):
    list_display = ('method', 'updated_time', 'data')
    
    
admin.site.register(SpamList, SpamListAdmin)
admin.site.register(SpamWordList, SpamWordAdmin)
admin.site.register(ArchiveAnalysisWord, ArchiveAnalysisWordAdmin)
admin.site.register(AnticipateArchive, AnticipateArchiveAdmin)
admin.site.register(AnalysisDBSchema, AnalysisDBSchemaAdmin)
admin.site.register(UpdateList, UpdateListAdmin)
