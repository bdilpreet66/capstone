<template>
  <div class="d-flex flex-column-fluid">
    <!--begin::Container-->
    <div class="container">
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              Contact List
              <div class="text-muted pt-2 font-size-sm">
                Add or Remove contact lists
              </div>
            </h3>
          </div>
          <div class="card-toolbar">
            <!--begin::Button-->
            <router-link to="/campaignCreate" v-slot="{ href, navigate }">
              <a
                :href="href"
                class="btn btn-primary font-weight-bolder"
                @click="navigate"
                >Create Campaign
              </a>
            </router-link>
            <!--end::Button-->
          </div>
        </div>
        <div class="card-body">
          <!--begin: Datatable-->
          <div class="row">
            <div class="col-sm-12 col-md-6">
              <div class="dataTables_length" id="kt_datatable_length">
                <label
                  >Show
                  <select
                    name="kt_datatable_length"
                    aria-controls="kt_datatable"
                    v-model="per_page"
                    @change="setPageSize"
                    class="custom-select custom-select-sm form-control form-control-sm"
                  >
                    <option value="5">5</option>
                    <option value="10">10</option>
                    <option value="25">25</option>
                    <option value="50">50</option>
                    <option value="75">75</option>
                    <option value="100">100</option>
                    <option value="200">200</option>
                    <option value="300">300</option>
                    <option value="400">400</option>
                    <option value="500">500</option>
                  </select>
                  entries</label
                >
              </div>
            </div>
            <div class="col-sm-12 col-md-6">
              <div
                id="kt_datatable_filter"
                class="dataTables_filter"
                align="right"
              >
                <label
                  >Search:<input
                    type="search"
                    v-model="searchField"
                    class="form-control form-control-sm"
                    style="cursor: auto"
                    placeholder=""
                    @input="onSearch"
                    aria-controls="kt_datatable"
                /></label>
              </div>
            </div>
          </div>
          <table
            class="table table-separate table-head-custom table-checkable"
            id="kt_datatable"
          >
            <thead>
              <tr>
                <th>Campaign NAME</th>
                <th>E-mail Client</th>
                <th>Created</th>
                <th>Last Email Sent</th>
                <th>Status</th>
                <th class="text-right">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in data" :key="item.id">
                <td>{{ item.campaign_name }}</td>
                <td>{{ item.client }}</td>
                <td>{{ item.created.substring(0, 10) }}</td>
                <td>
                    <span v-if="item.status!='Not yet started'">{{ item.last_sent.substring(0, 10) }}</span>
                    <span v-if="item.status=='Not yet started'">-</span>
                </td>
                <td>{{ item.status }}</td>
                <td class="text-right">
                  <a
                    href="javascript:;"
                    class="btn btn-sm btn-clean btn-icon"
                    @click="ViewList(item.id)"
                    title="View List Content"
                  >
                    <i class="la la-eye"></i
                  ></a>
                  <a
                    href="javascript:;"
                    class="btn btn-sm btn-clean btn-icon"
                    @click="deleteContact(item.id)"
                    title="Delete"
                  >
                    <i class="la la-trash"></i
                  ></a>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="row d-flex justify-content-end align-right">
                <ul class="pagination">
                  <li
                    class="paginate_button page-item previous"
                  >
                    <a
                      href="javascript:;"
                      aria-controls="kt_datatable"
                      data-dt-idx="0"
                      class="page-link"
                      @click="getPage('first')"
                      >First</a>
                  </li>
                  <li
                    class="paginate_button page-item previous"
                  >
                    <a
                      href="javascript:;"
                      aria-controls="kt_datatable"
                      data-dt-idx="0"
                      class="page-link"
                      @click="getPage('prev')"
                      ><i class="ki ki-arrow-back"></i
                    ></a>
                  </li>
                  <li
                    class="paginate_button page-item next"
                  >
                    <a
                      href="javascript:;"
                      aria-controls="kt_datatable"
                      data-dt-idx="1"
                      class="page-link"
                      @click="getPage('next')"
                      ><i class="ki ki-arrow-next"></i
                    ></a>
                  </li>
                  <li
                    class="paginate_button page-item previous"
                  >
                    <a
                      href="javascript:;"
                      aria-controls="kt_datatable"
                      data-dt-idx="0"
                      class="page-link"
                      @click="getPage('last')"
                      >Last</a>
                  </li>
                </ul>
            
          </div>
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
  name: "CampaignList",
  data: () => {
    return {
      per_page: 10,
      current_page: 1,
      searchField: ""
    };
  },
  beforeMount() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/campaign/get?limit=10&offset=0")
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
  },
  methods: {
    createForm() {
      store.state.contactListPageControls.table = false;
      store.state.contactListPageControls.create = true;
    },
    ViewList(id) {
      store.state.selectedReport = id;
      store.state.campaign.table = false;
      store.state.campaign.reports = true;
    },
    deleteContact(id) {
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios
        .delete("api/campaign/delete/" + id + "/")
        .then(function () {
          for(var i=0; i< store.state.CampaignList.length; i++){
            if(store.state.CampaignList[i]['id'] == id){
              store.state.CampaignList.splice(i,1)
            }
          }
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to delete user",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            });
          }
        });
    },
    onSearch(e) {
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios.defaults.headers.common["Authorization"] =
        "Token " + Vue.$cookies.get("key");
      axios
        .get(
          "api/campaign/get?limit=" +
            this.per_page +
            "&offset=0&search=" +
            e.target.value
        )
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
    },
    getPage(type){
      var link = ""
      if(type=="first"){
        link = "api/campaign/get?limit=" +this.per_page + "&offset=0";
      } else if (type=="next"){
        if (store.state.ContatNext == null)  return;
        link = store.state.ContatNext;
        link = link.replace("http://127.0.0.1:8000/","")
      } else if (type=="prev"){
        if (store.state.ContatPrev == null)  return;
        link = store.state.ContatPrev;
        link = link.replace("http://127.0.0.1:8000/","")
      } else{
        link = "api/campaign/get?limit=" +this.per_page + "&offset=" + parseInt(store.state.ContatCount-this.per_page-1);
      }
      if(this.searchField != ""){
        link = link + "&search=" + this.searchField;
      }
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios.defaults.headers.common["Authorization"] =
        "Token " + Vue.$cookies.get("key");
      axios
        .get(link)
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
    },
    setPageSize(e) {
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/campaign/get?limit="+e.target.value+"&offset=0&search=" + this.searchField)
      .then(function (response) {
        store.dispatch("executeupdateCampaignList", response["data"]);
      })
      .catch(function (error) {
        if (error.response) {
          Swal.fire({
            title: "Error",
            text: "Unable to get contacts list",
            icon: "error",
            confirmButtonClass: "btn btn-secondary",
            heightAuto: false,
          });
        }
      });
    }
  },
  computed: {
    data() {
      return store.state.CampaignList;
    },
  },
};
</script>