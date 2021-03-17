<template>
  <div class="d-flex flex-column-fluid">
    <!--begin::Container-->
    <div class="container">
          <form
            class="form"
            id="create_item_form"
            novalidate="novalidate"
            style="margin: 25px"
          >
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              Update Contact
              <div class="text-muted pt-2 font-size-sm">Update previously created contact</div>
            </h3>
          </div>
          <div class="card-toolbar">
            <!--begin::Button-->
            <button
                type="submit"
                class="btn btn-success font-weight-bolder mx-3"
              >Submit</button
            >
            <!--end::Button-->
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
            <div class="form-group row">
              <div class="col-lg-6">
                <label>First Name</label>
                <input
                  type="text"
                  class="form-control"
                  name="fname"
                  placeholder="John"
                />
                <span class="form-text text-muted"
                  >Please enter name for your item</span
                >
              </div>
              <div class="col-lg-6">
                <label>Last Name</label>
                <input
                  class="form-control"
                  type="text"
                  name="lname"
                  placeholder="Wick"
                />
                <span class="form-text text-muted">Reference</span>
              </div>
            </div>
            <div class="form-group row">
              <div class="col-lg-6">
                <label>Email</label>
                <input
                  type="text"
                  class="form-control"
                  name="email"
                  placeholder="username@website.com"
                />
                <span class="form-text text-muted"
                  >Please enter email for your contact</span
                >
              </div>
              <div class="col-lg-6">
                <label>Phone Number</label>
                <input
                  class="form-control"
                  type="text"
                  name="mobile"
                  placeholder="(000)-1234-123456"
                />
                <span class="form-text text-muted"
                  >Please enter contacts contact number</span
                >
              </div>
            </div>
            <div class="form-group row">
              <div class="col-lg-6">
                <label>Address</label>
                <textarea
                  type="text"
                  class="form-control"
                  name="add"
                  cols="3"
                  placeholder="Cecilia Chapman 711-2880 Nulla St. Mankato Mississippi 96522 (257)"
                ></textarea>
              </div>
              <div class="col-lg-6">
                <label>Reference</label>
                <input
                  class="form-control"
                  type="text"
                  name="ref"
                  placeholder="A5162343"
                />
                <span class="form-text text-muted">This must be unique</span>
              </div>
            </div>
            <div class="form-group row">
              <div class="col-lg-6">
                <label>Bank Details</label>
                <textarea
                  type="text"
                  class="form-control"
                  name="bank"
                  cols="3"
                  placeholder="Anything related to bank you might want to use"
                ></textarea>
              </div>
              <div class="col-lg-6">
                <label>Description</label>
                <textarea
                  type="text"
                  class="form-control"
                  name="desc"
                  cols="3"
                  placeholder="This is a description for theis contact"
                ></textarea>
              </div>
            </div>
        </div>
      </div>
      <!--end::Card-->
          </form>
    </div>
    <!--end::Container-->
  </div>
</template>

<script>
import formValidation from "@/assets/plugins/formvalidation/dist/es6/core/Core";

// FormValidation plugins
import Trigger from "@/assets/plugins/formvalidation/dist/es6/plugins/Trigger";
import Bootstrap from "@/assets/plugins/formvalidation/dist/es6/plugins/Bootstrap";
import SubmitButton from "@/assets/plugins/formvalidation/dist/es6/plugins/SubmitButton";

import KTUtil from "@/assets/js/components/util";
import store from "@/core/services/store/store.js";
import Swal from "sweetalert2";
import axios from "axios";

export default {
  name: "ContactsUpdateForm",
  data: () => {
    return {};
  },
  mounted() {
    const form = KTUtil.getById("create_item_form");
    form[1].value = store.state.selectedContact.first_name;
    form[2].value = store.state.selectedContact.last_name;
    form[3].value = store.state.selectedContact.email;
    form[4].value = store.state.selectedContact.mobile;
    form[5].value = store.state.selectedContact.address;
    form[7].value = store.state.selectedContact.bank;
    form[6].value = store.state.selectedContact.ref;
    form[8].value = store.state.selectedContact.desc;
    this.fv = formValidation(form, {
      fields: {
        ref: {
          validators: {
            notEmpty: {
              message: "reference is required",
            },
            callback: {
              callback: function (input) {
                for (var i = 0; i < store.state.contacts.length; i++) {
                  if (store.state.contacts[i].ref == input.value) {
                    return {
                      valid: false,
                      message: "The reference must be unique",
                    };
                  }
                }
                return {
                  valid: true,
                };
              },
            },
          },
        },
        email: {
          validators: {
            notEmpty: {
              message: "Email is required",
            },
            emailAddress: {
              message: "The value is not a valid email address",
            },
          },
        },
      },
      plugins: {
        trigger: new Trigger(),
        submitButton: new SubmitButton(),
        bootstrap: new Bootstrap(),
      },
    });

    this.fv.on("core.form.valid", () => {
        var form = KTUtil.getById("create_item_form")
        var data = []
        for(var i=0; i<form.length;i++){
            data.push(form[i].value)
        }
        data = {
            first_name: data[1],
            last_name: data[2],
            email: data[3],
            mobile: data[4],
            address: data[5],
            bank: data[7],
            ref: data[6],
            desc: data[8]
        };
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios
        .put("api/contact/manage/"+store.state.selectedContact.id+"/", data)
        .then(function () {
            store.state.contactsPageControls.table = true;
            store.state.contactsPageControls.update = false;
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to create new user",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            });
          }
        });
    });

    this.fv.on("core.form.invalid", () => {
      Swal.fire({
        title: "Error",
        text: "Please, provide correct data!",
        icon: "error",
        confirmButtonClass: "btn btn-secondary",
        heightAuto: false,
      });
    });
  },
  methods: {
    close() {
      store.state.contactsPageControls.table = true;
      store.state.contactsPageControls.update = false;
    },
  },
  computed: {},
};
</script>