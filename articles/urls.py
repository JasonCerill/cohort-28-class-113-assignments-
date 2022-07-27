from django.urls import path
from articles import views


urlpatterns = [
    path('<int:secionts>/<int:status>/',
         views.ArticleListView.as_view(), name="article_list"),
    path('<int:pk>/edit/', views.Article)
]
