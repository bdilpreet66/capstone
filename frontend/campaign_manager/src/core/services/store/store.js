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
        contactsList: [],
        viewListID: 0,
        viewListTitle: "",
        viewListdesc: "",
        ContatListCount: "",
        ContatListNext: "",
        ContatListPrev: "",
        contactsPageControls: {
            table: true,
            create: false,
            update: false
        },
        selectedTemplates: 0,
        Templates: [],
        TemplatesCount: "",
        TemplatesNext: "",
        TemplatesPrev: "",
        TemplatesPageControls: {
            table: true,
            create: false,
            update: false
        },
        contactListPageControls: {
            table: true,
            create: false,
            new: false,
            view: false
        },
        integration: {
            view: 0,
            active: [],
            gmail_link: ""
        },
        CampaignList: [],
        CampaignCount: "",
        CampaignNext: "",
        CampaignPrev: "",
        campaign: {
            table: true,
            reports: false
        },
        message: "",
        outlook: false,
        gmail: false,
        custom: false,
        TemplateList: [],
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
        updateTemplates: (state, payload) => {
            state.Templates = payload["results"];
            state.TemplatesCount = payload["count"];
            state.TemplatesNext = payload["next"];
            state.TemplatesPrev = payload["previous"];
        },
        updateContactList: (state, payload) => {
            state.contactsList = payload["results"];
            state.ContatListCount = payload["count"];
            state.ContatListNext = payload["next"];
            state.ContatListPrev = payload["previous"];
        },
        updateCampaignList: (state, payload) => {
            state.CampaignList = payload["results"];
            state.CampaignCount = payload["count"];
            state.CampaignNext = payload["next"];
            state.CampaignPrev = payload["previous"];
        },
        updategmail_link: (state, payload) => {
            state.integration.gmail_link = payload;
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
        executeUpdateListContact: (context, payload) => {
            context.commit("updateContactList", payload)
        },
        executeupdateTemplates: (context, payload) => {
            context.commit("updateTemplates", payload)
        },
        executeUpdategmail_link: (context, payload) => {
            context.commit("updategmail_link", payload)
        },
        executeupdateCampaignList: (context, payload) => {
            context.commit("updateCampaignList", payload)
        },
    },
    modules: {}
})