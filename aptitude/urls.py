from app import views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login , name='Login'),
    # path('aptitude_start/', views.aptitude_start, name='aptitude_start'),
    path('Register/', views.Register , name='Register'),
    path('regdetails/', views.regdetails , name='regdetails'),
    path('saved/<int:id>', views.saved, name='saved'),
    path('aptitude_catagory/', views.aptitude_catagory, name='aptitude_catagory'),
    path('start/<int:id>',views.start, name='start'),
    path('total/', views.total, name='total'),
   
#**************************Admin and HR**************************  

    path('logout/', views.logout, name='logout'),
    path('admin_dashboard/', views.admin_dashboard , name='admin_dashboard'),
    path('Dashboard/', views.Dashboard , name='Dashboard'),
    path('admin_add_limit/', views.admin_add_limit , name='admin_add_limit'),
    path('add_question/', views.add_question , name='add_question'),
    path('view_questions/<int:id1>/<int:id2>/', views.view_questions , name='view_questions'),
    path('view_question_update/<int:id>', views.view_question_update , name='view_question_update'),
    path('view_question_delete/<int:id>', views.view_question_delete , name='view_question_delete'),
    path('admin_allMembers/', views.admin_allMembers , name='admin_allMembers'),
    path('admin_allMembers_reference/', views.admin_allMembers_reference , name='admin_allMembers_reference'),
    path('HR/', views.HR , name='HR'),
    path('HR_view/', views.HR_view , name='HR_view'),
    path('HR_view_update/<int:id>', views.HR_view_update , name='HR_view_update'),
    path('HR_add/', views.HR_add , name='HR_add'),
    path('HR_view_delete/<int:id>', views.HR_view_delete , name='HR_view_delete'),
    path('hr_dashboard/', views.hr_dashboard , name='hr_dashboard'),
    path('hr_allMembers/', views.hr_allMembers , name='hr_allMembers'),
    path('NO_ref/', views.NO_ref , name='NO_ref'),
    path('BY_ref/', views.BY_ref , name='BY_ref'),
    path('admin_question_view/',views.admin_question_view,name="admin_question_view"),
    path('admin_question_view_dep/<int:id>/',views.admin_question_view_dep,name="admin_question_view_dep"),
    path('admin_question_category/',views.admin_question_category, name='admin_question_category'),
    path('admin_view_category/',views.admin_view_category, name='admin_view_category'),
    path('admin_view_update/<int:id>', views.admin_view_update , name='admin_view_update'),
    path('admin_view_delete/<int:id>', views.admin_view_delete , name='admin_view_delete'),
    path('admin_add_question/',views.admin_add_question, name='admin_add_question'),
  
    path('admin_hr_depmt/<int:id>', views.admin_hr_depmt , name='admin_hr_depmt'),
   
    path('admin_allMembers_category/<int:pk>/<int:id>/',views.admin_allMembers_category , name='admin_allMembers_category'),
    path('admin_category_contactedlist/<int:id>/',views.admin_category_contactedlist , name='admin_category_contactedlist'),
    path('admin_contactsave1/',views.admin_contactsave1 , name='admin_contactsave1'),
    path('admin_contactsave2/',views.admin_contactsave2 , name='admin_contactsave2'),
    path('admin_category_history/<int:id>/',views.admin_category_history , name='admin_category_history'),
    path('admin_category_intrestedlist/<int:id>/',views.admin_category_intrestedlist , name='admin_category_intrestedlist'),
    path('admin_category_newlist/<int:pk>/<int:id>',views.admin_category_newlist , name='admin_category_newlist'),
   
    path('admin_contactsave/',views.admin_contactsave , name='admin_contactsave'),
    path('admin_category_rejectedlist/<int:id>/',views.admin_category_rejectedlist , name='admin_category_rejectedlist'),
    path('admin_department/', views.admin_department,name="admin_department"),
    path('admin_add_department/', views.admin_add_department,name="admin_add_department"),
    path('admin_department_view/', views.admin_department_view,name="admin_department_view"),
    path('admin_view_department_delete/<int:id>/', views.admin_view_department_delete,name="admin_view_department_delete"),
    path('admin_view_department_update/<int:id>', views.admin_view_department_update , name='admin_view_department_update'),
    
    path('hr_department/', views.hr_department, name='hr_department'),
    path('hr_allMembers_category/<int:id>/', views.hr_allMembers_category , name='hr_allMembers_category'),
    path('hr_category_newlist/<int:id>/', views.hr_category_newlist , name='hr_category_newlist'),
   
    path('hr_category_contactedlist/', views.hr_category_contactedlist , name='hr_category_contactedlist'),
    path('hr_category_intrestedlist/', views.hr_category_intrestedlist , name='hr_category_intrestedlist'),
    path('hr_category_rejectedlist/', views.hr_category_rejectedlist, name='hr_category_rejectedlist'),
    path('hr_category_history/', views.hr_category_history, name='hr_category_history'),
    path('contactsave/', views.contactsave, name='contactsave'),
    path('replaysaveintrest/', views.replaysaveintrest, name='replaysaveintrest'),
    path('replaysavenotintrest/', views.replaysavenotintrest, name='replaysavenotintrest'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
