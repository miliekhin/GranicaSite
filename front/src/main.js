import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import mitt from 'mitt'
const emitter = mitt()
const app = createApp(App)
app.use(router)

// console.log(app.config)

app.config.globalProperties.DEBUG_MODE = (process.env.NODE_ENV === 'development')
app.config.globalProperties.emitter = emitter
app.config.globalProperties.MAX_CARS = 777
app.config.globalProperties.SEND_INFO_PERIOD_LIMIT = 10*60*1000
app.config.globalProperties.GET_INFO_PERIOD = 64*1000
app.config.globalProperties.GET_COMMENTS_PERIOD = 32*1000
app.config.globalProperties.KPP_NAMES = ['Успенка', 'Мариновка', 'Новоазовск']
if(app.config.globalProperties.DEBUG_MODE)
    app.config.globalProperties.URL = 'http://127.0.0.1:8000'
else
    app.config.globalProperties.URL = 'https://kppshka.ru'
app.config.globalProperties.URL += '/api/v1/'

app.mount('#app')

window.onafterprint = function() {
  router.go(-1)
}
