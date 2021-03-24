<template>
  <div class="card card-custom">
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <h3 class="card-label font-weight-bolder text-dark">Email Settings</h3>
        <span class="text-muted font-weight-bold font-size-sm mt-1"
          >Change your email settings</span
        >
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
      <div class="card-body">
            <div class="row justify-content-center my-20">
                <!--begin: Pricing-->
                <div class="col-md-4 col-xxl-3">
                    <div class="pt-30 pt-md-25 pb-15 px-5 text-center">
                        <!--begin::Icon-->
                        <div class="d-flex flex-center position-relative mb-25">
                            <span class="svg svg-fill-primary opacity-4 position-absolute">
                                <svg width="175" height="200">
                                    <polyline points="87,0 174,50 174,150 87,200 0,150 0,50 87,0"></polyline>
                                </svg>
                            </span>
                            <span class="svg-icon svg-icon-5x svg-icon-primary">
                                <img width="100" src="@/assets/gmail.png" alt="gmail">
                            </span>
                        </div>
                        <!--end::Icon-->
                        <!--begin::Content-->
                        <span class="font-size-h1 d-block d-block font-weight-boldest text-dark-75 py-2">Gmail</span>
                        <h4 class="font-size-h6 d-block d-block font-weight-bold mb-7 text-dark-50">API Integration</h4>
                        <p class="mb-15 d-flex flex-column">
                            <span>Integrate with gmails easy to use mail server api developed by google and used by many all over the world</span>
                        </p>
                        <a href="javascript:;" v-if="!gmail" @click="changeView(1)" class="btn btn-success text-uppercase font-weight-bolder px-15 py-3">Connect</a>
                        <a href="javascript:;" v-if="gmail" @click="Disconnect(1)" class="btn btn-primary text-uppercase font-weight-bolder px-15 py-3">DisConnect</a>
                        <!--end::Content-->
                    </div>
                </div>
                <!--end: Pricing-->
                <!--begin: Pricing-->
                <div class="col-md-4 col-xxl-3 border-x-0 border-x-md border-y border-y-md-0">
                    <div class="pt-30 pt-md-25 pb-15 px-5 text-center">
                        <!--begin::Icon-->
                        <div class="d-flex flex-center position-relative mb-25">
                            <span class="svg svg-fill-primary opacity-4 position-absolute">
                                <svg width="175" height="200">
                                    <polyline points="87,0 174,50 174,150 87,200 0,150 0,50 87,0"></polyline>
                                </svg>
                            </span>
                            <span class="svg-icon svg-icon-5x svg-icon-primary">
                                <img width="100" src="@/assets/outlook.png" alt="outlook">
                            </span>
                        </div>
                        <!--end::Icon-->
                        <!--begin::Content-->
                        <span class="font-size-h1 d-block d-block font-weight-boldest text-dark-75 py-2">Outlook</span>
                        <h4 class="font-size-h6 d-block d-block font-weight-bold mb-7 text-dark-50">SMTP/IMAP Integration</h4>
                        <p class="mb-15 d-flex flex-column">
                            <span>Integrate with outlooks highly advanced and easily managable SMTP and IMAP Servers to send emails</span>
                        </p>
                        <a href="javascript:;" v-if="!outlook" @click="changeView(2)" class="btn btn-success text-uppercase font-weight-bolder px-15 py-3">Connect</a>
                        <a href="javascript:;" v-if="outlook" @click="Disconnect(2)" class="btn btn-primary text-uppercase font-weight-bolder px-15 py-3">DisConnect</a>
                        <!--end::Content-->
                    </div>
                </div>
                <!--end: Pricing-->
                <!--begin: Pricing-->
                <div class="col-md-4 col-xxl-3">
                    <div class="pt-30 pt-md-25 pb-15 px-5 text-center">
                        <!--begin::Icon-->
                        <div class="d-flex flex-center position-relative mb-25">
                            <span class="svg svg-fill-primary opacity-4 position-absolute">
                                <svg width="175" height="200">
                                    <polyline points="87,0 174,50 174,150 87,200 0,150 0,50 87,0"></polyline>
                                </svg>
                            </span>
                            <span class="svg-icon svg-icon-5x svg-icon-primary">
                                <img width="130" src="@/assets/custom.png" alt="custom">
                            </span>
                        </div>
                        <!--end::Icon-->
                        <!--begin::Content-->
                        <span class="font-size-h1 d-block d-block font-weight-boldest text-dark-75 py-2">Custom</span>
                        <h4 class="font-size-h6 d-block d-block font-weight-bold mb-7 text-dark-50">SMTP/IMAP Integrations</h4>
                        <p class="mb-15 d-flex flex-column">
                            <span>ALLow you to connect with a wide variety of SMTP and IMAP Servers providing support for millions of Services.</span>
                        </p>
                        <a href="javascript:;" v-if="!custom" @click="changeView(3)" class="btn btn-success text-uppercase font-weight-bolder px-15 py-3">Connect</a>
                        <a href="javascript:;" v-if="custom" @click="Disconnect(3)" class="btn btn-primary text-uppercase font-weight-bolder px-15 py-3">DisConnect</a>
                        <!--end::Content-->
                    </div>
                </div>
                <!--end: Pricing-->
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
import router from "@/router.js";
Vue.use(VueCookies)

export default {
  name: "List",
  data: () => {
    return {
    };
  },
  created() {
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
        axios.defaults.headers.post["Content-Type"] = "application/json";
        axios.defaults.headers.common["Authorization"] =
            "Token " + Vue.$cookies.get("key");
        axios
            .get("api/user/get/active/clients/")
            .then(function (response) {
                store.state.outlook = response['data']['outlook'];
                store.state.gmail = response['data']['gmail'];
                store.state.custom = response['data']['custom'];
            })
            .catch(function (error) {
            if (error.response) {
                Swal.fire({
                title: "Error",
                text: "Failed to connect to service!",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
                });
            }
            });
  },
  methods: {
      changeView(number){
          store.state.integration.view = number;
      },
      Disconnect(number){
          var link = ""
          if(number == 1){
              link = 'api/user/google/disconnect/';
          } else if(number == 2){
              link = 'api/user/outlook/disconnect/';
          } else if(number == 3){
              link = 'api/user/custom/disconnect/';
          }
          
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
        axios.defaults.headers.post["Content-Type"] = "application/json";
        axios.defaults.headers.common["Authorization"] =
            "Token " + Vue.$cookies.get("key");
        axios
            .get(link)
            .then(function () {
              router.go();
            })
            .catch(function (error) {
            if (error.response) {
                Swal.fire({
                title: "Error",
                text: "Failed to connect to service!",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
                });
            }
            });
      }
  },
  computed: {
    outlook(){
        return store.state.outlook;
    },
    gmail(){
        return store.state.gmail;
    },
    custom(){
        return store.state.custom;
    }
  },
};
</script>
