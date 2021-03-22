<template>
  <!--begin::Card-->
  <div class="card card-custom">
    <!--begin::Header-->
    <div class="card-header py-3">
      <div class="card-title align-items-start flex-column">
        <h3 class="card-label font-weight-bolder text-dark">
          Personal Information
        </h3>
        <span class="text-muted font-weight-bold font-size-sm mt-1"
          >Update your personal informaiton</span
        >
      </div>
      <div class="card-toolbar">
        <button
          type="submit"
          class="btn btn-success mr-2"
          ref="kt_save_changes"
          @click="save"
        >
          Save Changes
        </button>
      </div>
    </div>
    <!--end::Header-->
    <!--begin::Form-->
    <form class="form" id="profileinfoForm">
      <!--begin::Body-->
      <div class="card-body">
        <div class="row">
          <label class="col-xl-3"></label>
          <div class="col-lg-9 col-xl-6">
            <h5 class="font-weight-bold mb-6">User Info</h5>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >Avatar</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="image-input image-input-outline" id="kt_profile_avatar">
              <div
                class="image-input-wrapper"
                :style="{ backgroundImage: `url(${photo})` }"
              ></div>
              <label
                class="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                data-action="change"
                data-toggle="tooltip"
                title=""
                data-original-title="Change avatar"
              >
                <i class="fa fa-pen icon-sm text-muted"></i>
                <input
                  type="file"
                  name="profile_avatar"
                  accept=".png, .jpg, .jpeg"
                  @change="onFileChange($event)"
                />
                <input type="hidden" name="profile_avatar_remove" />
              </label>
            </div>
            <span class="form-text text-muted"
              >Allowed file types: png, jpg, jpeg.</span
            >
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >First Name</label
          >
          <div class="col-lg-9 col-xl-6">
            <input
              ref="name"
              class="form-control form-control-lg form-control-solid"
              type="text"
              name="fname"
              v-model="fname"
            />
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >Last Name</label
          >
          <div class="col-lg-9 col-xl-6">
            <input
              ref="surname"
              class="form-control form-control-lg form-control-solid"
              type="text"
              name="lname"
              v-model="lname"
            />
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >Company Name</label
          >
          <div class="col-lg-9 col-xl-6">
            <input
              ref="company_name"
              class="form-control form-control-lg form-control-solid"
              type="text"
              name="company"
              v-model="cname"
            />
          </div>
        </div>
        <div class="row">
          <label class="col-xl-3"></label>
          <div class="col-lg-9 col-xl-6">
            <h5 class="font-weight-bold mt-10 mb-6">Contact Info</h5>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >Contact Phone</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-lg input-group-solid">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="la la-phone"></i>
                </span>
              </div>
              <input
                ref="phone"
                type="text"
                name="mob"
                class="form-control form-control-lg form-control-solid"
                placeholder="Phone"
                v-model="mob"
              />
            </div>
            <span class="form-text text-muted"
              >We'll never share your email with anyone else.</span
            >
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >Email Address</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-lg input-group-solid">
              <div class="input-group-prepend">
                <span class="input-group-text">
                  <i class="la la-at"></i>
                </span>
              </div>
              <input
                type="text"
                name="email"
                class="form-control form-control-lg form-control-solid"
                placeholder="Email"
                v-model="email"
              />
            </div>
          </div>
        </div>
        <div class="form-group row">
          <label class="col-xl-3 col-lg-3 col-form-label text-right"
            >Company Site</label
          >
          <div class="col-lg-9 col-xl-6">
            <div class="input-group input-group-lg input-group-solid">
              <input
                ref="company_site"
                type="text"
                name="website"
                class="form-control form-control-lg form-control-solid"
                placeholder="Username"
                v-model="website"
              />
            </div>
          </div>
        </div>
      </div>
      <!--end::Body-->
    </form>
    <!--end::Form-->
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import KTUtil from "@/assets/js/components/util";
import Swal from "sweetalert2";
import formValidation from "@/assets/plugins/formvalidation/dist/es6/core/Core";

// FormValidation plugins
import Trigger from "@/assets/plugins/formvalidation/dist/es6/plugins/Trigger";
import Bootstrap from "@/assets/plugins/formvalidation/dist/es6/plugins/Bootstrap";
import SubmitButton from "@/assets/plugins/formvalidation/dist/es6/plugins/SubmitButton";
import router from "@/router.js";
import axios from "axios";
import Vue from 'vue';
import VueCookies from 'vue-cookies';
// import store from "@/core/services/store/store.js";
Vue.use(VueCookies)

export default {
  name: "PersonalInformation",
  data() {
    return {
      default_photo: Vue.$cookies.get("logo"),
      current_photo: null,
      website: Vue.$cookies.get("company_site"),
      mob: Vue.$cookies.get("contact_number"),
      cname: Vue.$cookies.get("company_name"),
      email: Vue.$cookies.get("email"),
      fname: Vue.$cookies.get("first_name"),
      lname: Vue.$cookies.get("last_name"),
    };
  },
  mounted() {
    const password_change_form = KTUtil.getById("profileinfoForm");

    this.fv = formValidation(password_change_form, {
      fields: {
        email: {
          validators: {
            notEmpty: {
              message: "Current password is required"
            },
            emailAddress: {
                message: 'The value is not a valid email address'
            },
          }
        },
        website: {
          validators: {
            uri: {
                allowEmptyProtocol: true,
                message: 'The website address is not valid'
            }
          }
        },
      },
      plugins: {
        trigger: new Trigger(),
        bootstrap: new Bootstrap(),
        submitButton: new SubmitButton()
      }
    });
      this.fv.on("core.form.valid", () => {
        var data = {
          'fname': this.fname,
          'website': this.website,
          'mob': this.mob,
          'email': this.email,
          'cname': this.cname,
          'lname': this.lname,
        }
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
          axios.defaults.headers.common["Authorization"] =
            "Token " + Vue.$cookies.get("key");
      axios
        .post("api/user/update/profile/", data)
        .then(function (response) {
            Vue.$cookies.set("company_site",response["data"]["website"], -1);
            Vue.$cookies.set("contact_number",response["data"]["mob"], -1);
            Vue.$cookies.set("company_name",response["data"]["cname"], -1);
            Vue.$cookies.set("email",response["data"]["email"], -1);
            Vue.$cookies.set("first_name",response["data"]["fname"], -1);
            Vue.$cookies.set("last_name",response["data"]["lname"], -1);
            Swal.fire({
              title: "Success",
              text: "Profile Updated Successfully.",
              icon: "success",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            }).then(()=>{
              router.go();
            });
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to update profile!",
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
          confirmButtonClass: "btn btn-secondary"
        });
      });
  },
  methods: {
    save() {
      this.fv.validate();
    },
    onFileChange(e) {
      const file = e.target.files[0];
      let data = new FormData();
      data.append('file', file, file.fileName);
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
          axios.defaults.headers.common["Authorization"] =
            "Token " + Vue.$cookies.get("key");
      axios
        .post("api/user/update/ppic/", data,{headers: {
              'accept': 'application/json',
              'Accept-Language': 'en-US,en;q=0.8',
              'Content-Type': `multipart/form-data; boundary=${data._boundary}`,
        }})
        .then(function (response) {
            Vue.$cookies.set("logo","http://127.0.0.1:8000/media/" + response['data']['data'],-1)
            Swal.fire({
              title: "Success",
              text: "Uploaded Imaage to server.",
              icon: "success",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            }).then(()=>{
              router.go();
            });
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to upload Imaage to server!",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            });
          }
        });

      if (typeof FileReader === "function") {
        const reader = new FileReader();

        reader.onload = event => {
          this.current_photo = event.target.result;
        };

        reader.readAsDataURL(file);
      } else {
        alert("Sorry, FileReader API not supported");
      }
    }
  },
  computed: {
    ...mapGetters(["currentUserPersonalInfo"]),
    photo() {
      return this.current_photo == null
        ? this.default_photo
        : this.current_photo;
    }
  }
};
</script>
