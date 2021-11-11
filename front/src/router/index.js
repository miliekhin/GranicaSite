import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import DeclarationPrint from '../components/Declaration/DeclarationPrint.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home,
        meta: {
            title: 'информация об очередях на КПП ДНР/РФ'
        }
    },
    {
        path: '/declaration_print',
        name: 'declaration_print',
        component: DeclarationPrint,
        props: true,
        meta: {
            title: 'Декларация - Печать/Сохранение'
        }
    },
    {
        path: '/declaration',
        name: 'declaration',
        component: DeclarationPrint,
        props: true,
        meta: {
            title: 'Декларация'
        }
    },
]

const scrollBehavior = (to, from, savedPosition) => {
    return savedPosition || { top: 0, left: 0 };
}

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior,
})

export default router