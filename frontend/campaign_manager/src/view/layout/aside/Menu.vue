<template>
  <ul class="menu-nav">
    <router-link
      to="/dashboard"
      v-slot="{ href, navigate, isActive, isExactActive }"
    >
      <li
        aria-haspopup="true"
        data-menu-toggle="hover"
        class="menu-item"
        :class="[
          isActive && 'menu-item-active',
          isExactActive && 'menu-item-active'
        ]"
      >
        <a :href="href" class="menu-link" @click="navigate">
          <i class="menu-icon flaticon2-architecture-and-city"></i>
          <span class="menu-text">Dashboard</span>
        </a>
      </li>
    </router-link>

    <li class="menu-section">
      <h4 class="menu-text">Contacts</h4>
      <i class="menu-icon flaticon-more-v2"></i>
    </li>
    <router-link
      to="/contacts"
      v-slot="{ href, navigate, isActive, isExactActive }"
    >
      <li
        aria-haspopup="true"
        data-menu-toggle="hover"
        class="menu-item"
        :class="[
          isActive && 'menu-item-active',
          isExactActive && 'menu-item-active'
        ]"
      >
        <a :href="href" class="menu-link" @click="navigate">
          <i class="menu-icon flaticon2-user"></i>
          <span class="menu-text">All Contacts</span>
        </a>
      </li>
    </router-link>

    <li class="menu-section">
      <h4 class="menu-text">Settings</h4>
      <i class="menu-icon flaticon-more-v2"></i>
    </li>
    <router-link
      to="/profile"
      v-slot="{ href, navigate, isActive, isExactActive }"
    >
      <li
        aria-haspopup="true"
        data-menu-toggle="hover"
        class="menu-item"
        :class="[
          isActive && 'menu-item-active',
          isExactActive && 'menu-item-active'
        ]"
      >
        <a :href="href" class="menu-link" @click="navigate">
          <i class="menu-icon flaticon2-user"></i>
          <span class="menu-text">Profile</span>
        </a>
      </li>
    </router-link>

    <li class="menu-section">
      <h4 class="menu-text mr-3">Use Face Detection</h4>
      <span class="switch switch-icon">
        <label>
        <input type="checkbox" name="select" @click="faceCheck()" />
        <span></span>
        </label>
      </span>
    </li>
  </ul>
</template>

<script>
import store from "@/core/services/store/store.js";
import * as tf from "@tensorflow/tfjs";
import * as facemesh from "@tensorflow-models/facemesh";
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
  name: "KTMenu",
  methods: {
    hasActiveChildren(match) {
      return this.$route["path"].indexOf(match) !== -1;
    },
    async faceCheck() {
      store.state.start_cam = !store.state.start_cam;
      if(store.state.start_cam){
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
      }
    },
  },
  computed: {
  }
};
</script>
