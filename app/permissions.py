from rest_framework.permissions import BasePermission
from rest_framework.compat import is_authenticated
from django.contrib.auth.models import User, Group
from .models import SettingsUserGroups

settingsUserGroups = SettingsUserGroups()

class AllowAll(BasePermission):

   #Allows access only to authenticated users.

	def has_permission(self, request, view):
		return request.user and is_authenticated(request.user)

class VipOnly(BasePermission):
    
    #Allows access only to authenticated Vip users.
	def has_permission(self, request, view):

		if  request.user and is_authenticated(request.user):
			return request.user.groups.filter(pk=settingsUserGroups.VipGroup).exists()
		else:
			return False


