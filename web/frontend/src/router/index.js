import Vue from 'vue'
import Router from 'vue-router'
import Classification from '@/views/Classification'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/cls'
    },
    {
      path: '/cls',
      name: 'Classification',
      component: Classification
    }
  ]
})
