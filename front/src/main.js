import './assets/fonts/styles.css'
import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import mitt from 'mitt'
const emitter = mitt()
const app = createApp(App)
app.use(router)

import VueMobileDetection from 'vue-mobile-detection'
app.use(VueMobileDetection)

// console.log(app.config)

app.config.globalProperties.DEBUG_MODE = (process.env.NODE_ENV === 'development')
app.config.globalProperties.emitter = emitter
app.config.globalProperties.MAX_CARS_COUNTER = 777
app.config.globalProperties.MAX_CARS_LIMIT = 333
app.config.globalProperties.SEND_INFO_PERIOD_LIMIT = 10*60*1000
app.config.globalProperties.GET_INFO_PERIOD = 64*1000
app.config.globalProperties.GET_COMMENTS_PERIOD = 32*1000
app.config.globalProperties.COMPLAINT_MARK = 11000
app.config.globalProperties.FUZZY_CARS_COUNT_MARK = 10000
app.config.globalProperties.KPP_NAMES = [
    'Успенка',
    'Мариновка',
    'Новоазовск',
    'Шрамко',
]
app.config.globalProperties.RADIO_CARS_COUNT = {
    'Много машин': app.config.globalProperties.FUZZY_CARS_COUNT_MARK,
    'Очень много машин!': 10001,
    'Мало машин': 10002,
    'Машин нет': 0,
    'Указать количество': -1,
}
app.config.globalProperties.RADIO_WAYS = {
    'В сторону РФ': 0,
    'В сторону ДНР': 1,
}
app.config.globalProperties.RADIO_CAR_TYPES = {
    'Легковые': 0,
    'Грузовые': 1,
}
if(app.config.globalProperties.DEBUG_MODE)
    app.config.globalProperties.URL = 'http://127.0.0.1:8008'
else
    app.config.globalProperties.URL = 'https://kppshka.ru'
app.config.globalProperties.URL += '/api/v1/'

app.mount('#app')

window.onafterprint = function() {
  router.go(-1)
}
