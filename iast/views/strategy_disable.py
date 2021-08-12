#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# software: PyCharm
# project: lingzhi-webapi
from dongtai.models.hook_type import HookType
from dongtai.models.hook_strategy import HookStrategy
from dongtai.utils import const

from dongtai.endpoint import R
from dongtai.endpoint import TalentAdminEndPoint
from django.utils.translation import gettext_lazy as _


class StrategyDisableEndpoint(TalentAdminEndPoint):
    def get(self, request, id):
        strategy_model = HookType.objects.filter(id=id).first()
        if strategy_model:
            counts = strategy_model.strategies.filter(enable=const.HOOK_TYPE_ENABLE).update(
                enable=const.HOOK_TYPE_DISABLE)
            strategy_model.enable = const.HOOK_TYPE_DISABLE
            strategy_model.save(update_fields=['enable'])

            return R.success(msg=_('Strategy is disabled, total {} hook rules').format(counts))
        else:
            return R.failure(status=202, msg=_('No strategy does not exist'))


if __name__ == '__main__':
    
    HookStrategy.objects.values("id").count()
