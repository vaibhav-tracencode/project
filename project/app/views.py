from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"app/index.html")


def app_chat(request):
    return render(request,"app/apps-chat.html")

def app_contact(request):
    return render(request,"app/apps-contact-list.html")

def app_calendar(request):
    return render(request,"app/apps-calendar.html")

def app_files(request):
    return render(request,"app/apps-files.html")

def app_invoice(request):
    return render(request,"app/apps-invoice.html")

def app_task(request):
    return render(request,"app/apps-tasks.html")

def app_overview(request):
    return render(request,"app/apps-project-overview.html")

def app_project(request):
    return render(request,"app/apps-project-projects.html")

def app_board(request):
    return render(request,"app/apps-project-board.html")

def app_teams(request):
    return render(request,"app/apps-project-teams.html")

def app_project_files(request):
    return render(request,"app/apps-project-files.html")


def app_new_project(request):
    return render(request,"app/apps-new-project.html")

def e_product(request):
    return render(request,"app/apps-ecommerce-products.html")

def e_product_list(request):
    return render(request,"app/apps-ecommerce-product-list.html")

def e_checkout(request):
    return render(request,"app/apps-ecommerce-checkout.html")

def e_cart(request):
    return render(request,"app/apps-ecommerce-cart.html")

def e_product_detail(request):
    return render(request,"app/apps-ecommerce-product-detail.html")

def a_login(request):
    return render(request,"app/auth-login.html")

def a_register(request):
    return render(request,"app/auth-register.html")

def a_recover(request):
    return render(request,"app/auth-recover-pw.html")

def a_lockscreen(request):
    return render(request,"app/auth-lock-screen.html")

def error404(request):
    return render(request,"app/auth-404.html")

def error500(request):
    return render(request,"app/auth-500.html")


def ui_alert(request):
    return render(request,"app/ui-alerts.html")

def ui_avtar(request):
    return render(request,"app/ui-avatar.html")

def ui_buttons(request):
    return render(request,"app/ui-buttons.html")

def ui_badges(request):
    return render(request,"app/ui-badges.html")

def ui_cards(request):
    return render(request,"app/ui-cards.html")

def ui_carousels(request):
    return render(request,"app/ui-carousels.html")

def ui_checkradio(request):
    return render(request,"app/ui-check-radio.html")

def ui_dropdown(request):
    return render(request,"app/ui-dropdowns.html")

def ui_grid(request):
    return render(request,"app/ui-grid.html")

def ui_images(request):
    return render(request,"app/ui-images.html")

def ui_list(request):
    return render(request,"app/ui-list.html")

def ui_modals(request):
    return render(request,"app/ui-modals.html")

def ui_navbar(request):
    return render(request,"app/ui-navbar.html")

def ui_navs(request):
    return render(request,"app/ui-navs.html")    

def ui_paginations(request):
    return render(request,"app/ui-paginations.html")

def ui_progress(request):
    return render(request,"app/ui-progress.html")

def ui_tool(request):
    return render(request,"app/ui-popover-tooltips.html")

def ui_spinners(request):
    return render(request,"app/ui-spinners.html")

def ui_accordions(request):
    return render(request,"app/ui-tabs-accordions.html")

def ui_toasts(request):
    return render(request,"app/ui-toasts.html")

def ui_typography(request):
    return renderI(request,"app/ui-typography.html")

def ui_videos(request):
    return render(request,"app/ui-videos.html")

def ui_widgets(request):
    return render(request,"widgets.html")

def advance_animation(request):
    return render(request,"advanced-animation.html")

def advance_clipboard(request):
    return render(request,"app/advanced-clipboard.html")

def advance_highlight(request):
    return render(request,"app/advanced-highlight.html")

def advance_timer(request):
    return render(request,"app/advanced-idle-timer.html")

def advance_kanban(request):
    return render(request,"app/advanced-kanban.html")

def advance_lightbox(request):
    return render(request,"app/advanced-lightbox.html")
def advance_nestable(request):
    return render(request,"app/advanced-nestable.html")

def advance_rangeslider(request):
    return render(request,"app/advanced-rangeslider.html")

def advance_rating(request):
    return render(request,"app/advanced-ratings.html")

def advance_ribbons(request):
    return render(request,"app/advanced-ribbons.html")

def advance_session(request):
    return render(request,"app/advanced-session.html")

def advance_sweetalerts(request):
    return render(request,"app/advanced-sweetalerts.html")

