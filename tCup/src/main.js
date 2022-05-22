// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import Vue from 'vue'
import App from './App'
import router from './router'
import "babel-polyfill"

import * as echarts from 'echarts'
Vue.prototype.$echarts = echarts

import axios from 'axios';
Vue.prototype.$axios=axios;

Vue.use(ElementUI)

Vue.config.productionTip = false

Vue.$httpRequestList = []

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

router.beforeEach((to, from, next) => {
  if (Vue.$httpRequestList.length > 0) {
    console.log('Pending request canceled!');
    Vue.$httpRequestList.forEach((item) => {
      item()
    })
    Vue.$httpRequestList = []
  }
  next();
})
