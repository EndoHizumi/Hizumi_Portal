import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(axios, VueAxios)

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
