import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueCookies from 'vue-cookies'

import './assets/main.css'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';



const app = createApp(App)

app.config.productionTip = false

app.use(router).use(store).use(VueCookies, {expires: '1d', path: '/'}).mount('#app')



// cookies.set('auth', 1000)
// cookies.get('auth')
// cookies.remove('auth')
// cookies.isKey('auth')
// cookes.keys()

// https://fareedidris.medium.com/cookie-based-authentication-using-flask-and-vue-js-part-1-c625a530c157
// https://fareedidris.medium.com/cookie-based-authentication-using-flask-and-vue-js-part-2-bd2b47545466