import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [{
        path: '/file',
        name: 'File',
        component: () => import('../src/pages/File.vue')
    },
    {
        path: '/share',
        name: 'Share',
        component: () => import('../src/pages/Share.vue')
    }];
const router = createRouter({
    history: createWebHashHistory(),
    routes
})
export default router