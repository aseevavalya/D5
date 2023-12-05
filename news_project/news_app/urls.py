from django.urls import path

from .views import PostsList, PostDetail, PostSearch, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, NewsDelete,\
   ArticleDelete

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostSearch.as_view(), name='search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('article/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
]
