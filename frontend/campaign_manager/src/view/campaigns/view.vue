<template>
  <div class="d-flex flex-column-fluid mt-12">
    <!--begin::Container-->
    <div class="container">
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              Contact List : {{ title }}
              <div class="text-muted pt-2 font-size-sm">
                {{ desc }}
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
          <!--begin: Datatable-->
          <table
            class="table table-separate table-head-custom table-checkable"
            id="kt_datatable"
          >
            <thead>
              <tr>
                <th>NAME</th>
                <th>Email</th>
                <th>Refrence</th>
                <th>DESCRIPTION</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in data" :key="item.id">
                <td>{{ item.first_name + " " + item.last_name }}</td>
                <td>{{ item.email }}</td>
                <td>{{ item.ref }}</td>
                <td>{{ item.desc }}</td>
              </tr>
            </tbody>
          </table>
          <!--end: Datatable-->
        </div>
      </div>
      <!--end::Card-->
    </div>
    <!--end::Container-->
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
    };
  },
  beforeMount() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .put("api/contact/list/"+store.state.viewListID+"/")
      .then(function (response) {
        store.state.contacts = response["data"]['contact'];
        console.log(response["data"]['contact'])
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
      store.state.contactListPageControls.table = true;
      store.state.contactListPageControls.view = false;
    },
  },
  computed: {
    data() {
        return store.state.contacts;
    },
    title() {
        return store.state.viewListTitle;
    },
    desc(){
        return store.state.viewListdesc;
    }
  },
};
</script>