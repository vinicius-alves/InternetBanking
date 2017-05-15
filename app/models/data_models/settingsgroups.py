from django.db import models

#primary keys

class SettingsUserGroups(models.Model):
    PublicGroup = 1
    VipGroup = 2

    def isPublic(self, user):
    	return user.groups.filter(pk=self.PublicGroup).exists()

    def isVip(self, user):
    	return user.groups.filter(pk=self.VipGroup).exists()