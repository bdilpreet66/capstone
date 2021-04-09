<template>
  <div class="d-flex flex-column-fluid mt-12">
    <!--begin::Container-->
    <div class="container">
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              New Contact List
              <div class="text-muted pt-2 font-size-sm">Create a new contact list</div>
            </h3>
          </div>
          <div class="card-toolbar">
            <!--begin::Button-->
            <a
              href="javascript:;"
              @click="close()"
              class="btn btn-primary font-weight-bolder mr-5"
              >Close</a
            >
            <!--end::Button-->
            <!--begin::Button-->
            <a
              href="javascript:;"
              @click="submit()"
              class="btn btn-success font-weight-bolder"
              >Submit</a
            >
            <!--end::Button-->
          </div>
        </div>
        <div class="card-body">
          
        <div class="form-group row">
            <label class="col-xl-3 col-lg-3 col-form-label text-right"
                >List Name</label
            >
            <div class="col-lg-9 col-xl-6">
                <div class="input-group input-group-lg input-group-solid">
                <input
                    v-model="name"
                    type="text"
                    class="form-control form-control-lg form-control-solid"
                    placeholder="New List"
                />
                </div>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-xl-3 col-lg-3 col-form-label text-right"
                >List Reference</label
            >
            <div class="col-lg-9 col-xl-6">
                <div class="input-group input-group-lg input-group-solid">
                <input
                    v-model="ref"
                    type="text"
                    class="form-control form-control-lg form-control-solid"
                    placeholder="List Reference"
                />
        </div>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-xl-3 col-lg-3 col-form-label text-right"
                >List Description</label
            >
            <div class="col-lg-9 col-xl-6">
                <div class="input-group input-group-lg input-group-solid">
                    <input
                        v-model="desc"
                        type="text"
                        class="form-control form-control-lg form-control-solid"
                        placeholder="Description"
                    />
                </div>
            </div>
        </div>
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
                <th></th>
                <th>NAME</th>
                <th>Email</th>
                <th>Refrence</th>
                <th>DESCRIPTION</th>
                <th>Phone no.</th>
                <th>Address</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in data" :key="item.id">
                <td>
                    <b-form-checkbox
                    v-model="selected"
                    :value="item.id"
                    size="lg"
                    >
                    </b-form-checkbox>
                </td>
                <td>{{ item.first_name + " " + item.last_name }}</td>
                <td>{{ item.email }}</td>
                <td>{{ item.ref }}</td>
                <td>{{ item.desc.substring(0, 25) + "..." }}</td>
                <td>{{ item.mobile }}</td>
                <td>{{ item.address.substring(0, 15) + "..." }}</td>
              </tr>
            </tbody>
          </table>
          <div class="row d-flex justify-content-end align-right"><ul class="pagination">
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
  name: "ContactsListCreateListForm",
  data: () => {
    return {
        searchField: "",
        per_page: "10",
        name: "",
        ref: "",
        desc: "",
        selected: []
    };
  },
  mounted() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/contact/listContacts?limit=10&offset=0")
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
  },
  methods: {
    submit(){
        if(this.name != "" && this.ref != ""){
            var data={
                'name': this.name,
                'ref': this.ref,
                'desc': this.desc,
                'list': this.selected
            };
            axios.defaults.baseURL = "http://127.0.0.1:8000/";
            axios.defaults.headers.post["Content-Type"] = "application/json";
                axios.defaults.headers.common["Authorization"] =
                    "Token " + Vue.$cookies.get("key");
            axios
                .post("api/contact/list/", data)
                .then(function () {
                    store.state.contactListPageControls.table = true;
                    store.state.contactListPageControls.new = false;
                })
                .catch(function (error) {
                if (error.response) {
                    Swal.fire({
                    title: "Error",
                    text: "Failed to upload CSV to server!",
                    icon: "error",
                    confirmButtonClass: "btn btn-secondary",
                    heightAuto: false,
                    });
                }
                });
        } else {
            Swal.fire({
                title: "",
                text: "List Name and referece are required field",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
            });
        }
    },
    close() {
      store.state.contactListPageControls.table = true;
      store.state.contactListPageControls.new = false;
    },
    onSearch(e) {
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios.defaults.headers.common["Authorization"] =
        "Token " + Vue.$cookies.get("key");
      axios
        .get(
          "api/contact/listContacts?limit=" +
            this.per_page +
            "&offset=0&search=" +
            e.target.value
        )
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
    },
    getPage(type){
      var link = ""
      if(type=="first"){
        link = "api/contact/listContacts?limit=" +this.per_page + "&offset=0";
      } else if (type=="next"){
        if (store.state.ContatNext == null)  return;
        link = store.state.ContatNext;
        link = link.replace("http://127.0.0.1:8000/","")
      } else if (type=="prev"){
        if (store.state.ContatPrev == null)  return;
        link = store.state.ContatPrev;
        link = link.replace("http://127.0.0.1:8000/","")
      } else{
        link = "api/contact/listContacts?limit=" +this.per_page + "&offset=" + parseInt(store.state.ContatCount-this.per_page-1);
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
    },
    setPageSize(e) {
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/contact/listContacts?limit="+e.target.value+"&offset=0&search=" + this.searchField)
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
    }
  },
  computed: {
      data() {
      return store.state.contacts;
    },
  },
};
</script>