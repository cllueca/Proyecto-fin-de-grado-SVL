import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueCookies from 'vue-cookies'

import './assets/main.css'
import './assets/main.css'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';

const app = createApp(App)

app.config.productionTip = false

app.use(router).use(store).use(VueCookies, {expires: '1d', path: '/'}).mount('#app')
