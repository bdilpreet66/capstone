<template>
  <div class="card card-custom">
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <h3 class="card-label font-weight-bolder text-dark">Gmail Integration</h3>
        <span class="text-muted font-weight-bold font-size-sm mt-1"
          >Connect to Gmail</span
        >
      </div>
      
      <div class="card-toolbar">
        <button
          class="btn btn-success mr-2"
          ref="kt_save_changes"
          @click="Integrate"
        >
          Save
        </button>
        <button
          class="btn btn-primary mr-2"
          ref="kt_save_changes"
          @click="changeView"
        >
          Cancel
        </button>
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
      <div class="card-body">
            <div class="row justify-content-between my-10">
                <v-card-text>
                    <v-row>
                        <H3>Give us permission to access your account: <a :href="google_api" @click="hide_key=false" target="_blank">click here to authenticate</a></H3>
                        
                    </v-row>
                    <v-row v-if="!hide_key" class="mt-12">
                        <v-text-field
                            v-model="gmail_code"
                            :rules="[rules.required]"
                            outlined
                            label="enter gmail code"
                        ></v-text-field>
                    </v-row>
                </v-card-text>
            </div>
        </div>
    <!--end::Form-->
  </div>
</template>

<script>
import store from "@/core/services/store/store.js";
import axios from "axios";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
import Swal from "sweetalert2";
Vue.use(VueCookies)

export default {
  name: "Gmail",
  data: () => {
    return {
        hide_key: true,
        gmail_code: "",
        rules: {
                required: value => !!value || 'Required.',
        }
    };
  },
  beforeMount(){
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
          axios.defaults.headers.common["Authorization"] =
            "Token " + Vue.$cookies.get("key");
      axios
        .get("api/user/google/connect/")
        .then(function (response) {
            store.dispatch("executeUpdategmail_link",response["data"][0])
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to get Url!",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            }).then(()=>{
                store.state.integration.view = 0;
            });
          }
        });
  },
  methods: {
    changeView(){
          store.state.integration.view = 0;
      },
    Integrate(){
        if(this.gmail_code == "") return;
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
          axios.defaults.headers.common["Authorization"] =
            "Token " + Vue.$cookies.get("key");
      axios
        .post("api/user/google/connect/",{"code":this.gmail_code})
        .then(function () {
            Swal.fire({
              title: "Success",
              text: "integration successful",
              icon: "success",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            }).then(()=>{
                store.state.integration.view = 0;
            });
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to get Url!",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            }).then(()=>{
                store.state.integration.view = 0;
            });
          }
        });
    }
  },
  computed: {
      google_api() {
          return store.state.integration.gmail_link;
      }
  }
};
</script>
