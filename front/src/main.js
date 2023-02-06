import { createApp } from "vue";
import App from "./App.vue";
import Axios from "axios";
import clip from "clipboard";
import moment from "moment";
import router from "./index.js";

import { ElNotification } from "element-plus";
import "element-plus/dist/index.css";

const app = createApp(App);

app.config.globalProperties.axios = Axios;
app.config.globalProperties.clip = clip;
app.config.globalProperties.moment = moment;
app.config.globalProperties.ElNotification = ElNotification;
app.use(router)

app.mount("#app");
