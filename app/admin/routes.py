from app.admin import admin

@admin.route('/panel')
def panel():
    return "Bienvenido al panel de administracion"