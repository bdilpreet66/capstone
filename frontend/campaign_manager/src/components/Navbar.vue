<template>
  <v-navigation-drawer
    permanent
    expand-on-hover
    app
    @mouseover.native="hover = false"
    @mouseleave.native="hover = true"
  >
    <v-list dense rounded>
      <v-list-item class="px-0">
        <v-list-item-avatar>
          <v-img :src="nav_profile.ppic"></v-img>
        </v-list-item-avatar>

        <v-list-item-title></v-list-item-title>
      </v-list-item>

      <v-list-item class="px-1">
        <v-list-item-icon v-if="hover"> </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="title">{{
            nav_profile.user_name
          }}</v-list-item-title>
          <v-list-item-subtitle>{{ nav_profile.email }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list nav dense rounded>
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
    <template v-if="!hover" v-slot:append>
      <v-divider></v-divider>
      <v-row class="py-6">
        <v-spacer></v-spacer>
        <v-switch
          v-model="$store.state.start_cam"
          label="Enable Face Monitor"
          @click="faceCheck()"
        ></v-switch>
        <v-spacer></v-spacer>
      </v-row>
    </template>
  </v-navigation-drawer>
</template>

<script>
// import axios from 'axios';
import store from "@/store/index";
// import router from "@/router/index.js";
// import Vue from 'vue';
// import VueCookies from 'vue-cookies';
import * as tf from "@tensorflow/tfjs";
import * as facemesh from "@tensorflow-models/facemesh";

// Vue.use(VueCookies);

console.log(tf);
var videoPlayer = null;
var model = null;

async function LoadModel() {
  model = await facemesh.load({
    inputResolution: { width: 640, height: 480 },
    scale: 0.8,
  });
}

async function detect() {
  if (store.state.cam_available && store.state.start_cam) {
    var a = document.querySelector("video");
    var canvas = document.createElement("canvas");
    canvas.width = 640;
    canvas.height = 480;
    canvas.getContext("2d").drawImage(a, 0, 0, 640, 480);
    const predictions = await model.estimateFaces(canvas);
    if (predictions.length == 0) {
      document.getElementById("screen").style.visibility = "visible";
    } else {
      document.getElementById("screen").style.visibility = "hidden";
    }
    setTimeout(() => {
      detect();
    }, 50);
  }
}

LoadModel();

export default {
  data() {
    return {
      hover: true,
      items: [
        { title: "Schedule", icon: "mdi-view-dashboard", route: "/dashboard" },
        { title: "Template", icon: "mdi-dns", route: "/template" },
      ],
    };
  },
  methods: {
    async faceCheck() {
      if (
        "mediaDevices" in navigator &&
        "getUserMedia" in navigator.mediaDevices
      ) {
        navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
          videoPlayer = document.querySelector("video");
          videoPlayer.srcObject = stream;
          videoPlayer.play();
          store.state.cam_available = true;
          detect();
        });
      }
    },
  },
  computed: {
    nav_profile() {
      return this.$store.state.profile;
    },
  },
};
</script>
