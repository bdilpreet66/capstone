<template>
  <!--begin::Card-->
  <div class="card card-custom">
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <h3 class="card-label font-weight-bolder text-dark">Change Password</h3>
        <span class="text-muted font-weight-bold font-size-sm mt-1"
          >Change your account password</span
        >
      </div>
      <div class="card-toolbar">
        <button
          type="submit"
          class="btn btn-success mr-2"
          @click="save()"
          ref="kt_save_changes"
        >
          Save Changes
        </button>
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
    <form class="form" id="kt_password_change_form">
      <div class="card-body">
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-alert"
            >Current Password</label
          >
          <div class="col-lg-9 col-xl-6">
            <input
              type="password"
              class="form-control form-control-lg form-control-solid mb-2"
              v-model="cpassword"
              placeholder="Current password"
              name="current_password"
              ref="current_password"
            />
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-alert"
            >New Password</label
          >
          <div class="col-lg-9 col-xl-6">
            <input
              type="password"
              class="form-control form-control-lg form-control-solid"
              v-model="npassword"
              placeholder="New password"
              name="new_password"
              ref="new_password"
            />
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-alert"
            >Verify Password</label
          >
          <div class="col-lg-9 col-xl-6">
            <input
              type="password"
              class="form-control form-control-lg form-control-solid"
              value=""
              placeholder="Verify password"
              name="verify_password"
              ref="verify_password"
            />
          </div>
        </div>
      </div>
    </form>
    <!--end::Form-->
  </div>
</template>

<script>
import KTUtil from "@/assets/js/components/util";

import formValidation from "@/assets/plugins/formvalidation/dist/es6/core/Core";

// FormValidation plugins
import Trigger from "@/assets/plugins/formvalidation/dist/es6/plugins/Trigger";
import Bootstrap from "@/assets/plugins/formvalidation/dist/es6/plugins/Bootstrap";
import SubmitButton from "@/assets/plugins/formvalidation/dist/es6/plugins/SubmitButton";
import Swal from "sweetalert2";
import router from "@/router.js";
import axios from "axios";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
Vue.use(VueCookies)

export default {
  name: "ChangePassword",
  data() {
    return {
      cpassword: "",
      npassword: "",
      status: "",
      valid: true
    };
  },
  mounted() {
    const password_change_form = KTUtil.getById("kt_password_change_form");

    this.fv = formValidation(password_change_form, {
      fields: {
        current_password: {
          validators: {
            notEmpty: {
              message: "Current password is required"
            }
          }
        },
        new_password: {
          validators: {
            notEmpty: {
              message: "New password is required"
            }
          }
        },
        verify_password: {
          validators: {
            notEmpty: {
              message: "Confirm password is required"
            },
            identical: {
              compare: function() {
                return password_change_form.querySelector(
                  '[name="new_password"]'
                ).value;
              },
              message: "The password and its confirm are not the same"
            }
          }
        }
      },
      plugins: {
        trigger: new Trigger(),
        bootstrap: new Bootstrap(),
        submitButton: new SubmitButton()
      }
    });

      this.fv.on("core.form.valid", () => {
        var data = {
          'cpass': this.cpassword,
          'pass': this.npassword,
        }
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
          axios.defaults.headers.common["Authorization"] =
            "Token " + Vue.$cookies.get("key");
      axios
        .post("api/user/update/password/", data)
        .then(function () {
            Vue.$cookies.remove("key");
            Swal.fire({
              title: "Success",
              text: "Password Updated Successfully.",
              icon: "success",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            }).then(()=>{
              router.replace({ name: "login" });
            });
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to update Password!",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            });
          }
        });
      });

      this.fv.on("core.form.invalid", () => {
        Swal.fire({
          title: "",
          text: "Please, provide correct data!",
          icon: "error",
          confirmButtonClass: "btn btn-secondary"
        });
      });
    
  },
  methods: {
    save() {
      this.fv.validate();},
  },
  computed: {
  }
};
</script>
