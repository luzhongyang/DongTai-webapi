#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# software: PyCharm
# project: lingzhi-webapi
import time

from dongtai.endpoint import UserEndPoint, R
from dongtai.models.agent import IastAgent
from django.utils.translation import gettext_lazy as _


class AgentUninstall(UserEndPoint):
    name = "api-v1-agent-uninstall"
    description = _("Uninstall Agent")

    def post(self, request):
        agent_id = request.data.get('id')
        agent = IastAgent.objects.filter(user=request.user, id=agent_id).first()
        if agent:
            if agent.control != 2 and agent.is_control == 0:
                agent.control = 2
                agent.is_control = 1
                agent.latest_time = int(time.time())
                agent.save(update_fields=['latest_time', 'control', 'is_control'])
                return R.success(msg=_('Uninstalling ...'))
            else:
                return R.failure(msg=_('Agent is being installed or uninstalled, please try again later'))
        else:
            return R.failure(msg=_('Engine does not exist or no right to operate'))
