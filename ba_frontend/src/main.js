import Vue from 'vue';
// import axios from 'axios';
import App from './App.vue';
import router from './router';

// axios.defaults.baseURL = process.env.VUE_APP_BACKEND;
// console.log(`baseURL: ${process.env.VUE_APP_BACKEND}`);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
