import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        token: "",
        is_authenticated: false,
        baseURL: "http://127.0.0.1:8000",
        profile: {
            user_name: "user",
            ppic: "../assets/logo.png",
            email: "user"
        },
        start_cam: false,
        cam_available: false,
        contacts: [],
        selectedContact: null,
        ContatCount: "",
        ContatNext: "",
        ContatPrev: "",
        contactsPageControls: {
            table: true,
            create: false,
            update: false
        }
    },
    mutations: {
        updateToken: (state, payload) => {
            state.token = payload;
            state.is_authenticated = true;
        },
        updateProfile: (state, payload) => {
            // state.profile.ppic = state.baseURL + payload['profile_pic'];
            state.profile.user_name = payload['username'];
            state.profile.email = payload['email'];
        },
        updateContact: (state, payload) => {
            state.contacts = payload["results"];
            state.ContatCount = payload["count"];
            state.ContatNext = payload["next"];
            state.ContatPrev = payload["previous"];
        },
    },
    actions: {
        executeUpdateToken: (context, payload) => {
            context.commit("updateToken", payload)
        },
        executeUpdateProfile: (context, payload) => {
            context.commit("updateProfile", payload)
        },
        executeUpdateContact: (context, payload) => {
            context.commit("updateContact", payload)
        },
    },
    modules: {}
})