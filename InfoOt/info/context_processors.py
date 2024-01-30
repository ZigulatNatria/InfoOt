from django.core.cache import cache


def admin_user(request):
    return {'admin_user': request.user.groups.filter(name='admin').exists()}


def hr_user(request):
    return {'hr_user': request.user.groups.filter(name='hr').exists()}


def user_cash(request):
    return {'user_cash': cache.get('employ_id')}