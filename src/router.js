import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/HelloWorld.vue'
import About from './components/about.vue'
import Slide from './components/slide.vue'
import Webapp from './components/webapp'

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/profile/about',
      name: "about",
      component: About
    },
    {
      path: '/slide',
      name: "slide",
      component: Slide
    },
    {
      path: '/product/webapps',
      name: "webapp",
      component: Webapp
    }
  ]
})
