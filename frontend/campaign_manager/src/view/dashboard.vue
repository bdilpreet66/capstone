<template>
    <div
        id="kt_content"
        class="content d-flex flex-column flex-column-fluid"
    >
    <!--begin::Entry-->
    <div class="d-flex flex-column-fluid">
        <!--begin::Container-->
        <div class="container">
            <div class="row">
                <div class="col-xl-4 col-lg-4 col-md-4">
                    <div class="card card-custom gutter-b card-shadowless" style="background-color:rgb(23, 23, 41)">
                        <!--begin::Header-->
                        <div class="card-header border-0">
                            <h3 class="card-title font-weight-bolder text-success">Welcome to your dashboard</h3>
                        </div>
                        <!--end::Header-->
                        <!--begin::Body-->
                        <div class="card-body pt-2">
                            <!--begin::Item-->
                            <p class="text-muted">Here you will find an overview of your most recent Campaigns and some other stuff</p>
                            <p><img width="100%" src="@/assets/random.png" /></p>
                            <p class="text-muted">If your feel that you have any questions or are facing any problems feel free to contact us anytime you want.</p>
                            <h3 class="font-weight-bolder text-success">we are there for you!</h3>
                            <!--end::Item-->
                        </div>
                        <!--end::Body-->
                    </div>
                </div>
                <div class="col-xl-8 col-lg-8 col-md-8">
                    <!--begin::Charts Widget 2-->
                    <div class="card card-custom bg-gray-100 gutter-b card-stretch card-shadowless">
                        <div class="card-header flex-wrap py-5">
                            <div class="card-title">
                                <h3 class="card-label">Campaigns
                                </h3>
                            </div>
                            <div class="card-toolbar">
                                <!--begin::Button-->
                                <router-link to="/campaigns" v-slot="{ href, navigate }">
                                <a
                                    :href="href"
                                    class="btn btn-primary font-weight-bolder"
                                    @click="navigate"
                                    >View All
                                </a>
                                </router-link>
                                <!--end::Button-->
                            </div>
                        </div>
                        <div class="card-body">
                            <!--begin::Table-->
                            <div class="table-responsive">
                                <table class="table table-borderless mb-0">
                                    <tbody>
                                        <!--begin::Item-->
                                        <tr v-for="item in data" :key="item.id">
                                            <td class="font-size-lg font-weight-bolder text-dark-75 align-middle w-200px pb-6">
                                                <h6 class="card-label">{{ item.campaign_name }}
                                                    <div class="pt-2 font-size-sm">Client:
                                                        <span class="text-muted">{{ item.client }}</span>
                                                    </div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-6">
                                                <h6 class="card-label">Created
                                                    <div class="text-muted pt-2 font-size-sm">{{ item.created.substring(0, 10) }}</div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-12">
                                                <span v-if="item.status=='Not yet started'" class="label label-lg font-weight-bold label-light-primary label-inline">{{ item.status }}</span>
                                                <span v-if="item.status=='started'" class="label label-lg font-weight-bold label-light-info label-inline">{{ item.status }}</span>
                                                <span v-if="item.status=='finished'" class="label label-lg font-weight-bold label-light-success label-inline">{{ item.status }}</span></td>
                                        </tr>
                                        <!--end::Item-->
                                    </tbody>
                                </table>
                            </div>
                            <!--end::Table-->
                        </div>
                    </div>
                    <!--end::Charts Widget 2-->
                </div>
            </div>
        </div>
        <!--end::Container-->
    </div>
    <!--end::Entry-->
    <!--begin::Entry-->
    <div class="d-flex flex-column-fluid">
        <!--begin::Container-->
        <div class="container">
            <div class="row">
                <div class="col-7">
                    <!--begin::Charts Widget 2-->
                    <div class="card card-custom bg-gray-100 gutter-b card-stretch card-shadowless">
                        <div class="card-header flex-wrap py-5">
                            <div class="card-title">
                                <h3 class="card-label">Contacts
                                </h3>
                            </div>
                            <div class="card-toolbar">
                                <!--begin::Button-->
                                <router-link to="/contacts" v-slot="{ href, navigate }">
                                <a
                                    :href="href"
                                    class="btn btn-primary font-weight-bolder"
                                    @click="navigate"
                                    >View All
                                </a>
                                </router-link>
                                <!--end::Button-->
                            </div>
                        </div>
                        <div class="card-body">
                            <!--begin::Table-->
                            <div class="table-responsive">
                                <table class="table table-borderless mb-0">
                                    <tbody>
                                        <!--begin::Item-->
                                        <tr v-for="item in contacts" :key="item.id">
                                            <td class="font-size-lg font-weight-bolder text-dark-75 align-middle w-200px pb-6">
                                                <h6 class="card-label">{{ item.first_name + " " + item.last_name }}
                                                    <div class="pt-2 font-size-sm">Email:
                                                        <span class="text-muted">{{ item.email }}</span>
                                                    </div>
                                                </h6>
                                            </td>
                                            <td class="font-weight-bold text-right align-middle pb-6">
                                                <h6 class="card-label">Description
                                                    <div class="text-muted pt-2 font-size-sm">{{ item.desc }}</div>
                                                </h6>
                                            </td>
                                        </tr>
                                        <!--end::Item-->
                                    </tbody>
                                </table>
                            </div>
                            <!--end::Table-->
                        </div>
                    </div>
                    <!--end::Charts Widget 2-->
                </div>
                <div class="col-5">
                    <!--begin::Charts Widget 2-->
                    <div class="card card-custom bg-gray-100 gutter-b card-stretch card-shadowless">
                        <div class="card-header flex-wrap py-5">
                            <div class="card-title">
                                <h3 class="card-label">Templates
                                </h3>
                            </div>
                            <div class="card-toolbar">
                                <!--begin::Button-->
                                <router-link to="/templates" v-slot="{ href, navigate }">
                                <a
                                    :href="href"
                                    class="btn btn-primary font-weight-bolder"
                                    @click="navigate"
                                    >View All
                                </a>
                                </router-link>
                                <!--end::Button-->
                            </div>
                        </div>
                        <div class="card-body">
                            <!--begin::Table-->
                            <div class="table-responsive">
                                <table class="table table-borderless mb-0">
                                    <tbody>
                                        <!--begin::Item-->
                                        <tr v-for="item in templates" :key="item.id">
                                            <td class="font-size-lg font-weight-bolder text-dark-75 align-middle w-200px pb-6">
                                                <h6 class="card-label">{{ item.name }}
                                                    <div class="pt-2 font-size-sm">Subject:
                                                        <span class="text-muted">{{ item.subject }}</span>
                                                    </div>
                                                </h6>
                                            </td>
                                        </tr>
                                        <!--end::Item-->
                                    </tbody>
                                </table>
                            </div>
                            <!--end::Table-->
                        </div>
                    </div>
                    <!--end::Charts Widget 2-->
                </div>
            </div>
        </div>
        <!--end::Container-->
    </div>
    <!--end::Entry-->
    </div>
</template>

<script>
import store from "@/core/services/store/store.js";
import Swal from "sweetalert2";
import axios from "axios";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
Vue.use(VueCookies)

export default {
  name: "Dashboard",
  beforeMount() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/campaign/get?limit=6&offset=0&ordering=created")
      .then(function (response) {
        store.dispatch("executeupdateCampaignList", response["data"]);
      })
      .catch(function (error) {
        if (error.response) {
          Swal.fire({
            title: "Error",
            text: "Unable to get contacts",
            icon: "error",
            confirmButtonClass: "btn btn-secondary",
            heightAuto: false,
          });
        }
      });

    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/contact/listContacts?limit=5&offset=0")
      .then(function (response) {
        store.dispatch("executeUpdateContact", response["data"]);
      })
      .catch(function (error) {
        if (error.response) {
          Swal.fire({
            title: "Error",
            text: "Unable to get contacts",
            icon: "error",
            confirmButtonClass: "btn btn-secondary",
            heightAuto: false,
          });
        }
      });

      
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/campaign/listTemplates?limit=10&offset=0")
      .then(function (response) {
        store.dispatch("executeupdateTemplates", response["data"]);
      })
      .catch(function (error) {
        if (error.response) {
          Swal.fire({
            title: "Error",
            text: "Unable to get contacts",
            icon: "error",
            confirmButtonClass: "btn btn-secondary",
            heightAuto: false,
          });
        }
      });
  },
  methods: {
  },
  computed: {
    data() {
      return store.state.CampaignList;
    },
    contacts() {
      return store.state.contacts;
    },
    templates(){
      return store.state.Templates;
    }
  },
};
</script>