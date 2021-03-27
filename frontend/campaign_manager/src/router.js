import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

var router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
        path: "/",
        name: 'login',
        component: () =>
            import ("@/view/login.vue")
    }, {
        path: "/profile",
        name: 'Profile',
        component: () =>
            import ("@/view/profile.vue")
    }, {
        path: "/dashboard",
        name: 'Dashboard',
        component: () =>
            import ("@/view/dashboard.vue")
    }, {
        path: "/contacts",
        name: 'Contacts',
        component: () =>
            import ("@/view/contacts.vue")
    }, {
        path: "/contactslist",
        name: 'ContactList',
        component: () =>
            import ("@/view/contactList.vue")
    }, {
        path: "/templates",
        name: 'Templates',
        component: () =>
            import ("@/view/templates.vue")
    }, {
        path: "/campaigns",
        name: 'Campaign',
        component: () =>
            import ("@/view/Campaigns.vue")
    }, {
        path: "/campaignCreate",
        name: 'CreateCampaign',
        component: () =>
            import ("@/view/CreateCampaign.vue")
    }, ]
});

export default router;