<template>
  <div class="d-flex flex-column-fluid mt-5">
    <div class="container">
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              Camapign : {{ title }}
              <div class="text-muted pt-2 font-size-sm">
                total emails : {{ total_emails }}
              </div>
            </h3>
          </div>
          <div class="card-toolbar">
            <!--begin::Button-->
            <a
              href="javascript:;"
              @click="close()"
              class="btn btn-primary font-weight-bolder"
              >Close</a
            >
            <!--end::Button-->
          </div>
        </div>
        <div class="card-body">
          <blockquote class="blockquote text-center">
            <p class="display-1 text-success">SENT : {{ sent_emails }}
            </p>
          </blockquote>
          <v-row>
            <v-col>
              <div class="mt-14 text-center" style="width:100px;height:100px;">
                  <b-progress height="2rem" style="transform: rotate(270deg);" :value="delivered" :max="sent_emails" variant="success" show-progress animated></b-progress>
                  
                  <div style="margin-left:80px; margin-top:-50px; width:100%">
                      <h1 class="text-primary">{{ delivered }}</h1>
                      <span class="h5"><b>DELIVERED</b></span>
                  </div>
              </div>
            </v-col>
            <v-col>
              <div class="mt-14 text-center" style="width:100px;height:100px;">
                  <b-progress  height="2rem" style="transform: rotate(270deg);" :value="opened" :max="delivered" variant="success" show-progress animated></b-progress>
                  
                  <div style="margin-left:80px; margin-top:-50px; width:100%">
                      <h1 class="text-primary">{{ opened }}</h1>
                      <span class="h5"><b>OPENED</b></span>
                  </div>
              </div>
            </v-col>
            <v-col>
              <div class="mt-14 text-center" style="width:100px;height:100px;">
                  <b-progress  height="2rem" style="transform: rotate(270deg);" :value="clicked" variant="success" :max="delivered" show-progress animated></b-progress>
                  
                  <div style="margin-left:80px; margin-top:-50px; width:100%">
                      <h1 class="text-primary">{{ clicked }}</h1>
                      <span class="h5"><b>CLICKED</b></span>
                  </div>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <div class="mt-14 text-center" style="width:100px;height:100px;">
                  <b-progress  height="2rem" style="transform: rotate(270deg);" :value="invalid" :max="total_emails" variant="danger" show-progress animated></b-progress>
                  
                  <div style="margin-left:80px; margin-top:-50px; width:100%">
                      <h1 class="text-primary">{{ invalid }}</h1>
                      <span class="h5"><b>INVALID</b></span>
                  </div>
              </div>
            </v-col>
            <v-col>
              <div class="mt-14 text-center" style="width:100px;height:100px;">
                  <b-progress  height="2rem" style="transform: rotate(270deg);" :value="bounced" :max="total_emails" variant="danger" show-progress animated></b-progress>
                  
                  <div style="margin-left:80px; margin-top:-50px; width:100%">
                      <h1 class="text-primary">{{ bounced }}</h1>
                      <span class="h5"><b>BOUNCED</b></span>
                  </div>
              </div>
            </v-col>
            <v-col>
              <div class="mt-14 text-center" style="width:100px;height:100px;">
                  <b-progress  height="2rem" style="transform: rotate(270deg);" :value="unsubscribed" :max="sent_emails" variant="danger" show-progress animated></b-progress>
                  
                  <div style="margin-left:80px; margin-top:-50px; width:100%">
                      <h1 class="text-primary">{{ unsubscribed }}</h1>
                      <span class="h5"><b>UN-SUBS</b></span>
                  </div>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-simple-table 
                height="350" 
                :fixed-header="fixedHeader"
                style="width:1200px;"
            >
                <template v-slot:default>
                <thead>
                    <tr>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>Name</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>Email</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>Phone</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>Address</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>Invalid</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>Bounced</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>OPENS</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>CLICKS</h3></th>
                        <th style="background-color:#E65100; color:white" class="text-center"><h3>unsubscribe</h3></th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background-color:#CFD8DC;" v-for="data_item in list" :key="data_item[2]">
                        <td class="text-center">{{ data_item[0] + " " + data_item[1] }}</td>
                        <td class="text-center">{{ data_item[2] }}</td>
                        <td class="text-center">{{ data_item[3] }}</td>
                        <td class="text-center">{{ data_item[4] }}</td>
                        <td class="text-center">{{ data_item[5] }}</td>
                        <td class="text-center">{{ data_item[6] }}</td>
                        <td class="text-center">{{ data_item[7] }}</td>
                        <td class="text-center">{{ data_item[8] }}</td>
                        <td class="text-center">{{ data_item[9] }}</td>
                    </tr>
                </tbody>
                </template>
            </v-simple-table>
          </v-row>
          <blockquote class="blockquote text-center mt-12">
            <p class="text-success">This is an overview of the list, click on the download button bellow to get the entire data</p>
            <b-button :href='"http://127.0.0.1:8000/api/campaign/download/"+id+"/"' target="_blank" variant="outline-success">Download</b-button>
          </blockquote>
        </div>
      </div>
    </div>
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
  name: "Reports",
  data: () => {
    return {
      id: 0,
      title: "",
      delivered: 0,
      total_emails: 0,
      clicked: 0,
      opened: 0,
      invalid: 0,
      unsubscribed: 0,
      bounced: 0,
      sent_emails: 0,
      status: "",
      client: "",
      last_sent: "",
      created: "",
      subject: "",
      list: []
    };
  },
  beforeMount() {
    var self = this
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .put("api/campaign/viewReport/"+store.state.selectedReport+"/")
      .then(function (response) {
        self.title = response["data"]['campaign_name'];
        self.id = response["data"]['id'];
        self.total_emails = response["data"]['total_emails'];
        self.delivered = response["data"]['delivered'];
        self.total_emails = response["data"]['total_emails'];
        self.clicked = response["data"]['clicked'];
        self.opened = response["data"]['opened'];
        self.invalid = response["data"]['invalid'];
        self.unsubscribed = response["data"]['unsubscribed'];
        self.bounced = response["data"]['bounced'];
        self.sent_emails = response["data"]['sent_emails'];
        self.status = response["data"]['status'];
        self.client = response["data"]['client'];
        self.last_sent = response["data"]['last_sent'];
        self.created = response["data"]['created'];
        self.subject = response["data"]['subject'];
        self.list = response["data"]['list'];
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
    close() {
      store.state.campaign.table = true;
      store.state.campaign.reports = false;
    },
  },
  computed: {
  },
};
</script>