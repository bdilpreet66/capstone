<template>
  <div class="d-flex flex-column-fluid mt-12">
    <!--begin::Container-->
    <div class="container">
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              Contacts
              <div class="text-muted pt-2 font-size-sm">
                Add or Remove contacts
              </div>
            </h3>
          </div>
          <div class="card-toolbar">
            <!--begin::Button-->
            <a
              href="javascript:;"
              @click="createForm()"
              class="btn btn-primary font-weight-bolder"
              >New Contact</a
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
                <th>Phone no.</th>
                <th>Address</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in data" :key="item.id">
                <td>{{ item.first_name + " " + item.last_name }}</td>
                <td>{{ item.email }}</td>
                <td>{{ item.ref }}</td>
                <td>{{ item.desc.substring(0, 25) + "..." }}</td>
                <td>{{ item.mobile }}</td>
                <td>{{ item.address.substring(0, 15) + "..." }}</td>
                <td>
                  <a
                    href="javascript:;"
                    class="btn btn-sm btn-clean btn-icon"
                    title="Edit details"
                    @click="updateContact(item)"
                    ><i class="la la-edit"></i
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

export default {
  name: "ContactsTable",
  data: () => {
    return {};
  },
  beforeMount() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + store.state.token;
    axios
      .get("api/contact/manage/")
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
    createForm() {
      store.state.contactsPageControls.table = false;
      store.state.contactsPageControls.create = true;
    },
    updateContact(x) {
      store.state.selectedContact = x;
      store.state.contactsPageControls.table = false;
      store.state.contactsPageControls.update = true;
    },
    deleteContact(id) {
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios
        .delete("api/contact/manage/" + id + "/")
        .then(function () {
          axios
            .get("api/contact/manage/")
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
  },
  computed: {
    data() {
      return store.state.contacts;
    },
  },
};
</script>