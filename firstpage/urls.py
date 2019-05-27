from django.conf.urls import url
from firstpage import views

urlpatterns =[
    url(r'^del_from_cart',views.del_from_cart,name="del_from_cart"),
    url(r'^add_cart/',views.add_cart,name="add_cart"),
    url(r'^cart/',views.cart,name="cart"),
    url(r'^logout_required/',views.logout_required,name="logout_required"),
    url(r'^log_out/',views.log_out,name="log_out"),
    url(r'^post_sign_up/',views.post_sign_up,name="post_sign_up"),
    url(r'^signup/',views.sign_up,name="signup"),
    url(r'^products/',views.products,name="products"),
    url(r'^addproduct/',views.addproduct,name="addproduct"),
    url(r'^search/',views.search,name="search"),
    url(r'^home/',views.home,name="home"),
    url(r'^post-login/',views.post_login,name="post_login"),
    url(r'^index/', views.index, name='index'),

]