<template>
    <v-navigation-drawer
        permanent
        expand-on-hover
        app
        @mouseover.native="hover = false"
        @mouseleave.native="hover = true"
    >
        <v-list
          dense
          rounded
        >
        <v-list-item class="px-0">
          <v-list-item-avatar>
            <v-img :src="nav_profile.ppic"></v-img>
          </v-list-item-avatar>

          <v-list-item-title></v-list-item-title>
        </v-list-item>

        <v-list-item class="px-1">
            <v-list-item-icon v-if="hover">
            </v-list-item-icon>
            <v-list-item-content>
            <v-list-item-title class="title">{{ nav_profile.user_name }}</v-list-item-title>
          <v-list-item-subtitle>{{ nav_profile.email }}</v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list
        nav
        dense
        rounded
        >
            <v-list-item 
            link
            v-for="item in items"
            :key="item.title"
            router
            color="primary"
            :to="item.route"
            >
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
// import axios from 'axios';
// import store from "@/store/index";
// import router from "@/router/index.js";
// import Vue from 'vue';
// import VueCookies from 'vue-cookies';

// Vue.use(VueCookies);


export default {
    data () {
      return {
        hover: true,
        items: [
          { title: 'Schedule', icon: 'mdi-view-dashboard', route: '/dashboard' },
            { title: 'Template', icon: 'mdi-dns', route: '/template' },
              { title: 'Lists', icon: 'mdi-view-dashboard', route: '/dashboard' },
                { title: 'Report', icon: 'mdi-view-dashboard', route: '/dashboard' },
                  { title: 'Integration', icon: 'mdi-view-dashboard', route: '/dashboard' },
                    { title: 'Campaign', icon: 'mdi-view-dashboard', route: '/dashboard' },
                      { title: 'Contact', icon: 'mdi-view-dashboard', route: '/dashboard' },
                        { title: 'Account', icon: 'mdi-view-dashboard', route: '/dashboard' },
        ],
      }
    },
    methods: {
    },
    computed: {
      nav_profile(){
        return this.$store.state.profile
      }
    }
};
</script>
