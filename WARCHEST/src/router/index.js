import Vue from 'vue'
import VueRouter from 'vue-router'
import Homepage from '../views/Homepage.vue'
import App1 from '../views/App1.vue'
import Map1 from '../views/Map1.vue'
import Map2 from '../views/Map2.vue'
import Admin from '../views/Admin.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/login',
  //   name: 'login',
  //   component: () => import('@/components/Login.vue'),
  //   meta: {
  //    hideNavbar: true,
  //   }
  //  },
 {
    path: '/homepage',
    name: 'Homepage',
    component: Homepage
  },
  {
    path: '/app1',
    name: 'App1',
    component: App1
  },
  {
    path: '/map1',
    name: 'Map1',
    component: Map1
  },
  {
    path: '/map2',
    name: 'Map2',
    component: Map2
  },
  {
    path: '/admin',
    name: 'Admin',
    component: Admin
  },
  {
    path: '/list1',
    name: 'List1',
    component: () => import('@/laterViews/List1.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
