from django.urls import path
import main.views
 
#미디어 파일 사용을 위해

urlpatterns = [
    path('main/',main.views.index , name='main'),
    path('guest/<int:pk>',main.views.guest, name='guest'),
    path('diary/<int:pk>',main.views.diary, name='diary'),
    path('profile/', main.views.profile, name='profile'),
    path('picture/',main.views.picture, name='picture'),
    path('updateProfile/',main.views.updateProfile, name='updateProfile'),
    path('updateTitle/',main.views.updateTitle, name='updateTitle'),
    path('search/', main.views.search, name = 'search'),
    path('index_detail/<int:pk>', main.views.index_detail, name = 'index_detail'),
    path('guest_detail/<int:pk>',main.views.guest_detail, name='guest_detail'),
    path('friendsay/<int:pk>', main.views.friendsay, name='friendsay'),
    path('diary_detail/<int:pk>',main.views.diary_detail, name='diary_detail'),
    path('diary_create/<int:pk>',main.views.diary_create, name='diary_create'),
    path('comment_delete/<int:pk>',main.views.comment_delete, name='comment_delete'),
]

