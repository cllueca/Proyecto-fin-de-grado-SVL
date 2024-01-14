import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '../store/index'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      meta:{
        requiresAuth: false
      },
      component: HomeView
    },
    {
      path: '/registro',
      name: 'registro',
      meta:{
        requiresAuth: false
      },
      component: () => import('../views/RegistroView.vue')
    },
    {
      path: '/inicioSesion',
      name: 'inicioSesion',
      meta:{
        requiresAuth: false
      },
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/perfil',
      name: 'perfil',
      meta:{
        requiresAuth: true
      },
      component: () => import('../views/PerfilView.vue')
    }
  ]
})


router.beforeEach((to, from, next) => {
  const auth = $cookies.get('auth');//store.state.token;

  if((to.meta.requiresAuth) && (auth == null))
  {
    next('inicioSesion')
  }
  else if(!(to.meta.requiresAuth) && (auth != null))
  {
    next('perfil')
  }
  else{
    next()
  }
});

export default router
