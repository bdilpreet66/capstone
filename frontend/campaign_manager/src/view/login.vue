<template>
  <div class="d-flex flex-column flex-root">
    <!--begin::Login-->
    <div
      class="login login-5 login-signin-on d-flex flex-row-fluid"
      :class="{
        'login-signin-on': this.state == 'signin',
        'login-signup-on': this.state == 'signup',
        'login-forgot-on': this.state == 'forgot',
      }"
      id="kt_login"
    >
      <div
        class="d-flex flex-center bgi-size-cover bgi-no-repeat flex-row-fluid"
        style="background-image: url(media/bg/bg-2.jpg)"
      >
        <div
          class="login-form text-center text-white p-7 position-relative overflow-hidden"
        >
          <!--begin::Login Header-->
          <div class="d-flex flex-center mb-15">
            <a href="#">
              <img
                src="media/logos/logo-letter-13.png"
                class="max-h-75px"
                alt=""
              />
            </a>
          </div>
          <!--end::Login Header-->
          <!--begin::Login Sign in form-->
          <div class="login-form login-signin">
            <div class="mb-20">
              <h3 class="opacity-40 font-weight-normal">Sign In To App</h3>
              <p class="opacity-40">
                Enter your details to login to your account:
              </p>
            </div>
            <form
              class="form"
              novalidate="novalidate"
              id="kt_login_signin_form"
            >
              <div class="form-group">
                <div
                  id="example-input-group-1"
                  label=""
                  label-for="example-input-1"
                >
                  <input
                    class="form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8"
                    type="text"
                    name="email"
                    placeholder="Username"
                    ref="email"
                    v-model="form.email"
                  />
                </div>
              </div>
              <div class="form-group">
                <div
                  id="example-input-group-2"
                  label=""
                  label-for="example-input-2"
                >
                  <input
                    class="form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8"
                    type="password"
                    name="password"
                    placeholder="Passeord"
                    ref="password"
                    v-model="form.password"
                    autocomplete="off"
                  />
                </div>
              </div>
              <div class="d-flex justify-content-between mt-n5">
                <div class="checkbox-inline">
                  <label
                    class="checkbox checkbox-outline checkbox-white text-white m-0"
                  >
                    <input type="checkbox" name="remember" />
                    <span></span>Remember me</label
                  >
                </div>
                <a
                  class="text-white opacity-30 font-size-h6 font-weight-bolder"
                  id="kt_login_forgot"
                  style="cursor: pointer"
                  @click="showForm('forgot')"
                  >Forgot Password ?</a
                >
              </div>
              <div class="pb-lg-0 pb-5 mt-6">
                <button
                  ref="kt_login_signin_submit"
                  class="btn btn-pill btn-primary opacity-90 px-15 py-3"
                >
                  Sign In
                </button>
              </div>

              <div class="mt-10">
                <span class="opacity-40 mr-4">Don't have an account yet?</span>
                <a
                  id="kt_login_signup"
                  style="cursor: pointer"
                  class="text-white opacity-30 font-weight-normal"
                  @click="showForm('signup')"
                  >Sign Up</a
                >
              </div>
            </form>
          </div>
          <!--end::Login Sign in form-->
          <!--begin::Signup-->
          <div class="login-form login-signup">
            <div class="mb-20">
              <h3 class="opacity-40 font-weight-normal">Create an account</h3>
              <p class="opacity-40">
                Enter all your details to create your account:
              </p>
            </div>
            <form
              class="form"
              novalidate="novalidate"
              id="kt_login_signup_form"
            >
              <div class="form-group">
                <input
                  class="form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8"
                  type="text"
                  placeholder="Fullname"
                  name="fullname"
                  ref="fullname"
                  autocomplete="off"
                />
              </div>
              <div class="form-group">
                <input
                  class="form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8"
                  type="email"
                  placeholder="Email"
                  name="email"
                  ref="remail"
                  autocomplete="off"
                />
              </div>
              <div class="form-group">
                <input
                  class="form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8"
                  type="password"
                  placeholder="Password"
                  name="password"
                  ref="rpassword"
                  autocomplete="off"
                />
              </div>
              <div class="form-group">
                <input
                  class="form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8"
                  type="password"
                  placeholder="Confirm password"
                  name="cpassword"
                  ref="cpassword"
                  autocomplete="off"
                />
              </div>
              <div class="form-group">
                <label
                  class="checkbox checkbox-outline checkbox-white text-white m-0"
                >
                  <input type="checkbox" name="agree" />
                  <span class="mr-2"></span>
                  I Agree the
                  <a
                    href="#"
                    class="ml-2 text-white opacity-30 font-weight-normal"
                    >terms and conditions</a
                  >.
                </label>
              </div>
              <div class="pb-lg-0 pb-5 mt-6">
                <button
                  ref="kt_login_signup_submit"
                  class="btn btn-pill btn-primary opacity-90 px-15 py-3"
                >
                  Submit
                </button>
                <button
                  type="button"
                  id="kt_login_signup_cancel"
                  class="btn btn-pill btn-primary opacity-90 px-15 py-3 ml-6"
                  @click="showForm('signin')"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
          <!--end::Signup-->
          <!--begin::Forgot-->
          <div class="login-form login-forgot">
            <div class="mb-20">
              <h3 class="opacity-40 font-weight-normal">Forgot Password</h3>
              <p class="opacity-40">Enter your username to send reset email:</p>
            </div>
            <!--begin::Form-->
            <form
              class="form"
              novalidate="novalidate"
              id="kt_login_forgot_form"
              ref="kt_login_forgot_form"
            >
              <div class="pb-13 pt-lg-0 pt-5">
                <h3
                  class="font-weight-bolder text-dark font-size-h4 font-size-h1-lg"
                >
                  Forgotten Password ?
                </h3>
                <p class="text-muted font-weight-bold font-size-h4">
                  Enter your email to reset your password
                </p>
              </div>
              <div class="form-group">
                <input
                  class="form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8"
                  type="email"
                  placeholder="Email"
                  name="email"
                  autocomplete="off"
                />
              </div>

              <div class="pb-lg-0 pb-5 mt-6">
                <button
                  type="button"
                  id="kt_login_forgot_submit"
                  class="btn btn-pill btn-primary opacity-90 px-15 py-3"
                >
                  Submit
                </button>
                <button
                  type="button"
                  id="kt_login_forgot_cancel"
                  class="btn btn-pill btn-primary opacity-90 px-15 py-3 ml-6"
                  @click="showForm('signin')"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
          <!--end::Forgot-->
        </div>
      </div>
    </div>
    <!--end::Login-->
  </div>
</template>

<!-- Load login custom page styles -->
<style lang="scss">
@import "@/assets/sass/pages/login/classic/login-5.scss";
</style>

<script>
import formValidation from "@/assets/plugins/formvalidation/dist/es6/core/Core";

// FormValidation plugins
import Trigger from "@/assets/plugins/formvalidation/dist/es6/plugins/Trigger";
import Bootstrap from "@/assets/plugins/formvalidation/dist/es6/plugins/Bootstrap";
import SubmitButton from "@/assets/plugins/formvalidation/dist/es6/plugins/SubmitButton";

import KTUtil from "@/assets/js/components/util";
import { mapGetters, mapState } from "vuex";
import { LOGOUT, REGISTER } from "@/core/services/store/auth.module";
import Swal from "sweetalert2";
import axios from "axios";
import store from "@/core/services/store/store.js"
import router from "@/router.js"

export default {
  name: "login",
  data() {
    return {
      state: "signin",
      // Remove this dummy login info
      form: {
        email: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapState({
      errors: (state) => state.auth.errors,
    }),
    ...mapGetters(["currentUser"]),

    backgroundImage() {
      return (
        process.env.BASE_URL + "media/svg/illustrations/login-visual-1.svg"
      );
    },
  },
  mounted() {
    const signin_form = KTUtil.getById("kt_login_signin_form");
    const signup_form = KTUtil.getById("kt_login_signup_form");
    const forgot_form = KTUtil.getById("kt_login_forgot_form");

    this.fv = formValidation(signin_form, {
      fields: {
        email: {
          validators: {
            notEmpty: {
              message: "Username is required",
            },
          },
        },
        password: {
          validators: {
            notEmpty: {
              message: "Password is required",
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

    this.fv1 = formValidation(signup_form, {
      fields: {
        fullname: {
          validators: {
            notEmpty: {
              message: "Full name is required",
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
        password: {
          validators: {
            notEmpty: {
              message: "Password is required",
            },
          },
        },
        cpassword: {
          validators: {
            notEmpty: {
              message: "Confirm password is required",
            },
            identical: {
              compare: function () {
                return signup_form.querySelector('[name="password"]').value;
              },
              message: "The password and its confirm are not the same",
            },
          },
        },
        agree: {
          validators: {
            notEmpty: {
              message: "You should agree terms and conditions",
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

    this.fv2 = formValidation(forgot_form, {
      fields: {
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
      var data = {
        username: this.form.email,
        password: this.form.password,
      };
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios.post("api/user/account/login/", data)
        .then(function (response) {
          store.dispatch("executeUpdateToken",response["data"]["key"]);
          axios.defaults.headers.common['Authorization'] = 'Token '+response["data"]["key"];
          axios.get('/api/user/account/get_info/')
          .then(function(response) {
                console.log(response)
                store.dispatch("executeUpdateProfile",response["data"]);
                router.replace({ name: 'Dashboard' })
                // this.$router.push({ name: "Dashboard" })
          })
          .catch(function(error) {
              if (error.response) {
                console.log(error.response)
              }
          })
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Please, provide correct details!",
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

    this.fv1.on("core.form.valid", () => {
      const email = this.$refs.remail.value;
      const password = this.$refs.rpassword.value;

      // clear existing errors
      this.$store.dispatch(LOGOUT);

      // set spinner to submit button
      const submitButton = this.$refs["kt_login_signup_submit"];
      submitButton.classList.add("spinner", "spinner-light", "spinner-right");

      // dummy delay
      setTimeout(() => {
        // send register request
        this.$store
          .dispatch(REGISTER, {
            email: email,
            password: password,
          })
          .then(() => this.$router.push({ name: "dashboard" }));

        submitButton.classList.remove(
          "spinner",
          "spinner-light",
          "spinner-right"
        );
      }, 2000);
    });

    this.fv1.on("core.form.invalid", () => {
      Swal.fire({
        title: "",
        text: "Please, provide correct data!",
        icon: "error",
        confirmButtonClass: "btn btn-secondary",
        heightAuto: false,
      });
    });
  },
  methods: {
    showForm(form) {
      this.state = form;
      var form_name = "kt_login_" + form + "_form";
      KTUtil.animateClass(
        KTUtil.getById(form_name),
        "animate__animated animate__backInUp"
      );
    },
  },
};
</script>
