<template>
  <v-app>
  <div id="screen" style="height:100vh; width:100vw; background-color:black; position: absolute; z-index:999; visibility:hidden">
    <video autoplay style="heigth:100%; width:100%;"></video>
  </div>
    <Navbar v-if="['login'].indexOf($route.name) == -1" />
    <v-app-bar
      app
      color="info"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />
      </div>
      <v-spacer></v-spacer><v-btn 
      id="ltctr"
      
      color="blue-grey"
      style="display:none;"
      class="ma-2 white--text"
      @click="logintoggle"
    >
      Login 
    
    </v-btn>
    <v-btn 
      id="rtctr"
   
      
      color="blue-grey"
      class="ma-2 white--text"
      @click="regtoggle"
    >
      Sign Up 
    
    </v-btn>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>


<script>
import Navbar from "@/components/Navbar"

export default {
  name: 'App',
  components: { Navbar },

  data: () => ({ 
    
    
  }),
  methods:{
    logintoggle()
    {
      document.getElementById('lform').style.display='block';
      document.getElementById('rform').style.display='none';
      document.getElementById('rtctr').style.display='block';
      document.getElementById('ltctr').style.display='none';
      
      },
       regtoggle()
    {
      document.getElementById('rform').style.display='block';
      document.getElementById('lform').style.display='none';
      document.getElementById('ltctr').style.display='block';
      document.getElementById('rtctr').style.display='none';
     
      },
  },
  computed: {
    
  },
};
</script>
