import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.prototype.$API_URL = "http://127.0.0.1:8000/"
Vue.prototype.$VERSION = 1.0
Vue.prototype.$PHOTO_URL = "http://127.0.0.1:8000/Photos/"

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
