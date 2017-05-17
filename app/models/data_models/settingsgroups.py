from django.db import models

class SettingsUserGroups(models.Model):
    """
    Classe auxiliar, apenas verifica se o usuário pertence a um grupo chamado
    público ou a um grupo chamado vip. Para isso tem membros de dados internos
    representando as chaves primárias de ambos os grupos.
    """

    PublicGroup = 1
    VipGroup = 2

    def isPublic(self, user):
    	return user.groups.filter(pk=self.PublicGroup).exists()

    def isVip(self, user):
    	return user.groups.filter(pk=self.VipGroup).exists()