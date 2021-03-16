import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        token: "",
        baseURL: "http://127.0.0.1:8000",
        profile: {
            user_name: "user",
            ppic: "../assets/logo.png",
            email: "user"
        },
        start_cam: false,
        cam_available: false,
    },
    mutations: {
        updateToken: (state, payload) => {
            state.token = payload;
        },
        updateProfile: (state, payload) => {
            // state.profile.ppic = state.baseURL + payload['profile_pic'];
            state.profile.user_name = payload['username'];
            state.profile.email = payload['email'];
        },
    },
    actions: {
        executeUpdateToken: (context, payload) => {
            context.commit("updateToken", payload)
        },
        executeUpdateProfile: (context, payload) => {
            context.commit("updateProfile", payload)
        },
    },
    modules: {}
})