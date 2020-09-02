import Vue from 'vue';
import VueRouter from 'vue-router';
import VueMoment from 'vue-moment';
import SPU from '../components/SPU.vue';

Vue.use(VueRouter);
Vue.use(VueMoment);

const routes = [
  {
    path: '/',
    name: 'SPU',
    component: SPU,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
