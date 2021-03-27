<template>
  <div class="d-flex flex-column-fluid mt-12">
    <!--begin::Container-->
    <div class="container">
      <!--begin::Card-->
      <div class="card card-custom">
        <div class="card-header flex-wrap py-5">
          <div class="card-title">
            <h3 class="card-label">
              Create a new Campaign
              <div class="text-muted pt-2 font-size-sm">
                Follow the steps bellow to create a new campaign
              </div>
            </h3>
          </div>
          <div class="card-toolbar">
            <!--begin::Button-->
            <router-link to="/campaigns" v-slot="{ href, navigate }">
              <a
                :href="href"
                class="btn btn-primary font-weight-bolder"
                @click="navigate"
                >Close
              </a>
            </router-link>
            <!--end::Button-->
          </div>
        </div>
        <div class="card-body">
          <div class="">
            <div class="card-body p-0">
              <!--begin: Wizard-->
              <div
                class="wizard wizard-1"
                id="kt_wizard_v1"
                data-wizard-state="step-first"
                data-wizard-clickable="false"
              >
                <!--begin: Wizard Nav-->
                <div class="wizard-nav border-bottom">
                  <div class="wizard-steps p-8 p-lg-10">
                    <div
                      class="wizard-step"
                      data-wizard-type="step"
                      data-wizard-state="current"
                    >
                      <div class="wizard-label">
                        <i class="wizard-icon flaticon-information"></i>
                        <h3 class="wizard-title">1. Info</h3>
                      </div>
                      <i class="wizard-arrow flaticon2-next"></i>
                    </div>
                    <div class="wizard-step" data-wizard-type="step">
                      <div class="wizard-label">
                        <i class="wizard-icon flaticon-doc"></i>
                        <h3 class="wizard-title">2. Template</h3>
                      </div>
                      <i class="wizard-arrow flaticon2-next"></i>
                    </div>
                    <div class="wizard-step" data-wizard-type="step">
                      <div class="wizard-label">
                        <i class="wizard-icon flaticon-list"></i>
                        <h3 class="wizard-title">3. Select List</h3>
                      </div>
                      <i class="wizard-arrow flaticon2-next"></i>
                    </div>
                    <div class="wizard-step" data-wizard-type="step">
                      <div class="wizard-label">
                        <i class="wizard-icon flaticon2-dashboard"></i>
                        <h3 class="wizard-title">4. Schedule and Submit</h3>
                      </div>
                      <i class="wizard-arrow last flaticon2-next"></i>
                    </div>
                  </div>
                </div>
                <!--end: Wizard Nav-->

                <!--begin: Wizard Body-->
                <div
                  class="row justify-content-center my-10 px-8 my-lg-15 px-lg-10"
                >
                  <div class="col-xl-12 col-xxl-7">
                    <!--begin: Wizard Form-->
                    <v-form
                      class="form"
                      v-model="valid"
                      ref="form"
                      id="kt_form"
                    >
                      <!--begin: Wizard Step 1-->
                      <div
                        class="pb-5"
                        data-wizard-type="step-content"
                        data-wizard-state="current"
                      >
                        <h3 class="mb-10 font-weight-bold text-dark">
                          Set Up Your Campaign
                        </h3>
                        <div class="row">
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Campaign Name</label>
                              <v-text-field
                                class="form-control form-control-solid form-control-lg"
                                :rules="[rules.required]"
                                placeholder="My first Campaign"
                                v-model="name"
                              />
                            </div>
                          </div>
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>E-mail</label>
                              <v-text-field
                                class="form-control form-control-solid form-control-lg"
                                placeholder="email@email.com"
                                v-model="email"
                                disabled
                              />
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Display Name</label>
                              <v-text-field
                                class="form-control form-control-solid form-control-lg"
                                :rules="[rules.required]"
                                placeholder="My first Campaign"
                                v-model="display_name"
                              />
                            </div>
                          </div>
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Reply-To</label>
                              <v-text-field
                                class="form-control form-control-solid form-control-lg"
                                :rules="[rules.required, rules.email]"
                                placeholder="email@email.com"
                                v-model="reply_to"
                              />
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-xl-6"></div>
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Email Client</label>
                              <select
                                v-model="client"
                                :rules="[rules.required]"
                                @change="getmail"
                                class="form-control form-control-solid form-control-lg"
                                id="clientSelect1"
                              ></select>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!--end: Wizard Step 1-->

                      <!--begin: Wizard Step 2-->
                      <div class="pb-5" data-wizard-type="step-content">
                        <h3 class="mb-10 font-weight-bold text-dark">
                          Select a Template or create a new
                        </h3>
                        <div class="row">
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Contact List</label>
                              <select
                                @change="changeTemplate"
                                class="form-control form-control-solid form-control-lg"
                                id="templateSelect"
                              ></select>
                            </div>
                          </div>
                          <div class="col-xl-6"></div>
                        </div>
                        <div class="row">
                          <div class="col-12">
                            <div class="form-group">
                              <label>Subject</label>
                              <v-text-field
                                class="form-control form-control-solid form-control-lg"
                                :rules="[rules.required]"
                                placeholder="My first Campaign"
                                v-model="subject"
                              />
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-12">
                            <div class="form-group">
                              <editor
                                v-model="message"
                                api-key="5m1k2j8b2mllw5ubytknqdgtm2vd7du2jzjdeqf50hvpqcf7"
                                :init="{
                                  height: 450,
                                  paste_data_images: true,
                                  plugins: [
                                    'advlist autolink lists link image charmap preview anchor',
                                    'searchreplace visualblocks code fullscreen',
                                    'insertdatetime media table code help wordcount',
                                  ],
                                  toolbar:
                                    'undo redo | formatselect | bold italic underline forecolor  backcolor | \
                                    alignleft aligncenter alignright alignjustify | \
                                    bullist numlist outdent indent | removeformat ',
                                }"
                              />
                            </div>
                          </div>
                        </div>
                        <div class="form-group row text-center">
                          <div class="col-lg-12">
                            <div class="btn-group" role="group">
                              <button
                                type="button"
                                class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3"
                                v-clipboard:copy="'{ link }'"
                              >
                                <i class="la la-copy"></i>Unsubscribe
                              </button>
                              <button
                                type="button"
                                class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3"
                                v-clipboard:copy="'{ first_name }'"
                              >
                                <i class="la la-copy"></i>First Name
                              </button>
                              <button
                                type="button"
                                class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3"
                                v-clipboard:copy="'{ last_name }'"
                              >
                                <i class="la la-copy"></i>Last Name
                              </button>
                              <button
                                type="button"
                                class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3"
                                v-clipboard:copy="'{ address }'"
                              >
                                <i class="la la-copy"></i>Address
                              </button>
                              <button
                                type="button"
                                class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3"
                                v-clipboard:copy="'{ email }'"
                              >
                                <i class="la la-copy"></i>Email
                              </button>
                              <button
                                type="button"
                                class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3"
                                v-clipboard:copy="'{ bank }'"
                              >
                                <i class="la la-copy"></i>Bank details
                              </button>
                              <button
                                type="button"
                                class="btn btn-transparent-success btn-shadow-hover font-weight-bold mb-3"
                                v-clipboard:copy="'{ contact }'"
                              >
                                <i class="la la-copy"></i>Contact
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!--end: Wizard Step 2-->

                      <!--begin: Wizard Step 3-->
                      <div class="pb-5" data-wizard-type="step-content">
                        <h3 class="mb-10 font-weight-bold text-dark">
                          Select a list of contatcts
                        </h3>
                        <div class="row">
                          <div class="col-xl-3"></div>
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Contact List</label>
                              <select
                                v-model="selectedList"
                                :rules="[rules.required]"
                                class="form-control form-control-solid form-control-lg"
                                id="contactlistSelect"
                              ></select>
                            </div>
                          </div>
                          <div class="col-xl-3"></div>
                        </div>
                      </div>
                      <!--end: Wizard Step 3-->

                      <!--begin: Wizard Step 4-->
                      <div class="pb-5" data-wizard-type="step-content">
                        <h3 class="font-weight-bold text-dark">
                          Almost done just tell us when you want start sending these emails?
                        </h3>
                        <h4 class="mb-10 font-weight-bold text-muted">
                          Leave these field empty to start sending now.
                        </h4>
                        <div class="row">
                          <div class="col-xl-12">
                            <div class="form-group">
                              <label>Set the time between each email</label>
                              <input v-model="time_delta" class="form-control form-control-solid form-control-lg" max="600" type="range"/>
                              <label>{{ time_delta }} sec</label>
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Timezone</label>
                              <select
                                v-model="tzone"
                                :rules="[rules.required]"
                                class="form-control form-control-solid form-control-lg"
                                id="timezoneSelect"
                              ></select>
                            </div>
                          </div>
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Time</label>
                              <b-form-timepicker v-model="time" :rules="[rules.required]" locale="en" class="form-control form-control-solid form-control-lg"></b-form-timepicker>
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-xl-6"></div>
                          <div class="col-xl-6">
                            <div class="form-group">
                              <label>Date</label>
                              <b-form-datepicker v-model="date" :rules="[rules.required]" locale="en" class="form-control form-control-solid form-control-lg"></b-form-datepicker>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!--end: Wizard Step 4-->

                      <!--begin: Wizard Actions -->
                      <div
                        class="d-flex justify-content-between border-top pt-10"
                      >
                        <div class="mr-2">
                          <button
                            class="btn btn-light-primary font-weight-bold text-uppercase px-9 py-4"
                            data-wizard-type="action-prev"
                          >
                            Previous
                          </button>
                        </div>
                        <div>
                          <button
                            @click="submit"
                            class="btn btn-success font-weight-bold text-uppercase px-9 py-4"
                            data-wizard-type="action-submit"
                          >
                            Submit
                          </button>
                          <button
                            class="btn btn-primary font-weight-bold text-uppercase px-9 py-4"
                            data-wizard-type="action-next"
                          >
                            Next Step
                          </button>
                        </div>
                      </div>
                      <!--end: Wizard Actions -->
                    </v-form>
                    <!--end: Wizard Form-->
                  </div>
                </div>
                <!--end: Wizard Body-->
              </div>
            </div>
            <!--end: Wizard-->
          </div>
        </div>
      </div>
      <!--end::Card-->
    </div>
    <!--end::Container-->
  </div>
</template>

<style lang="scss">
@import "@/assets/sass/pages/wizard/wizard-1.scss";
</style>

<script>
import KTUtil from "@/assets/js/components/util";
import store from "@/core/services/store/store.js";
import axios from "axios";
import KTWizard from "@/assets/js/components/wizard";
import Editor from "@tinymce/tinymce-vue";
import Swal from "sweetalert2";
import Vue from "vue";
import VueClipboard from "vue-clipboard2";
Vue.use(VueClipboard);

export default {
  name: "CreateCampaign",
  components: {
    editor: Editor,
  },

  data: () => {
    return {
      rules: {
        required: (value) => !!value || "Required.",
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Invalid e-mail.";
        },
        less_than: (value) => value <= 65535 || "Invalid port number",
        greater_than: (value) => value >= 0 || "Invalid port number",
      },

      valid: true,
      name: "",
      email: "this will be imported from your selected client",
      display_name: "",
      reply_to: "",
      client: "",
      message: "",
      subject: "",
      selectedList: "",
      contactList: [],
      listimported: false,
      templateimported: false,
      timezoneimported: false,
      tzone: "",
      time: "",
      date: "",
      time_delta: "10",
    };
  },
  mounted() {
    axios.defaults.baseURL = "http://127.0.0.1:8000/";
    axios.defaults.headers.post["Content-Type"] = "application/json";
    axios.defaults.headers.common["Authorization"] =
      "Token " + Vue.$cookies.get("key");
    axios
      .get("api/user/get/active/clients/")
      .then(function (response) {
        var elm = document.getElementById("clientSelect1");
        if (response["data"]["outlook"]) {
          elm.options[elm.options.length] = new Option("Outlook", "Outlook");
        }
        if (response["data"]["gmail"]) {
          elm.options[elm.options.length] = new Option("Gmail", "Gmail");
        }
        if (response["data"]["custom"]) {
          elm.options[elm.options.length] = new Option("Custom", "Custom");
        }
        elm.value = "";
      })
      .catch(function (error) {
        if (error.response) {
          Swal.fire({
            title: "Error",
            text: "Failed to connect to service!",
            icon: "error",
            confirmButtonClass: "btn btn-secondary",
            heightAuto: false,
          });
        }
      });

    // Initialize form wizard
    const wizard = new KTWizard("kt_wizard_v1", {
      startStep: 1,
    });

    // Change event
    wizard.on("change", function (wizardObj) {
      if (wizardObj.currentStep == 1 && !this.templateimported) {
        this.templateimported = !this.templateimported;
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
        axios.defaults.headers.post["Content-Type"] = "application/json";
        axios.defaults.headers.common["Authorization"] =
          "Token " + Vue.$cookies.get("key");
        axios
          .get("api/campaign/template/list/")
          .then(function (response) {
            var elm = document.getElementById("templateSelect");
            for (var i = 0; i < response["data"].length; i++) {
              elm.options[elm.options.length] = new Option(
                response["data"][i]["name"],
                response["data"][i]["id"]
              );
            }
            elm.value = "";
          })
          .catch(function (error) {
            if (error.response) {
              Swal.fire({
                title: "Error",
                text: "Failed to connect to service!",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
              });
            }
          });
      } else if (wizardObj.currentStep == 2 && !this.listimported) {
        this.listimported = !this.listimported;
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
        axios.defaults.headers.post["Content-Type"] = "application/json";
        axios.defaults.headers.common["Authorization"] =
          "Token " + Vue.$cookies.get("key");
        axios
          .get("api/contact/list/")
          .then(function (response) {
            var elm = document.getElementById("contactlistSelect");
            for (var i = 0; i < response["data"].length; i++) {
              elm.options[elm.options.length] = new Option(
                response["data"][i]["name"] +
                  " (" +
                  response["data"][i]["ref"] +
                  ")",
                response["data"][i]["id"]
              );
            }
            elm.value = "";
          })
          .catch(function (error) {
            if (error.response) {
              Swal.fire({
                title: "Error",
                text: "Failed to connect to service!",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
              });
            }
          });
      } else if (wizardObj.currentStep == 3 && !this.timezoneimported) {
        this.timezoneimported = !this.timezoneimported;
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
        axios.defaults.headers.post["Content-Type"] = "application/json";
        axios.defaults.headers.common["Authorization"] =
          "Token " + Vue.$cookies.get("key");
        axios
          .get("api/campaign/get/timezone/")
          .then(function (response) {
            var elm = document.getElementById("timezoneSelect");
            for (var i = 0; i < response["data"].length; i++) {
              elm.options[elm.options.length] = new Option(
                response["data"][i],
                response["data"][i]
              );
            }
            elm.value = "";
          })
          .catch(function (error) {
            if (error.response) {
              Swal.fire({
                title: "Error",
                text: "Failed to connect to service!",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
              });
            }
          });
      }
      setTimeout(() => {
        KTUtil.scrollTop();
      }, 500);
    });
  },
  methods: {
    getmail(e){
      console.log(e.target.value)
    },
    changeTemplate(e) {
      let self = this;
      axios.defaults.baseURL = "http://127.0.0.1:8000/";
      axios.defaults.headers.post["Content-Type"] = "application/json";
      axios.defaults.headers.common["Authorization"] =
        "Token " + Vue.$cookies.get("key");
      axios
        .put("api/campaign/get/templateData/" + e.target.value + "/", {})
        .then(function (response) {
          self.message = response["data"]["message"];
          self.subject = response["data"]["subject"];
        })
        .catch(function (error) {
          if (error.response) {
            Swal.fire({
              title: "Error",
              text: "Failed to connect to service!",
              icon: "error",
              confirmButtonClass: "btn btn-secondary",
              heightAuto: false,
            });
          }
        });
    },
    submit: function (e) {
      e.preventDefault();
      if (this.$refs.form.validate()) {
        let data = {
          name: this.name,
          display_name: this.display_name,
          reply_to: this.reply_to,
          client: this.client,
          message: this.message,
          subject: this.subject,
          selectedList: this.selectedList,
          tzone: this.tzone,
          time: this.time,
          date: this.date,
          time_delta: this.time_delta
        }
        axios.defaults.baseURL = "http://127.0.0.1:8000/";
        axios.defaults.headers.post["Content-Type"] = "application/json";
        axios.defaults.headers.common["Authorization"] =
          "Token " + Vue.$cookies.get("key");
        axios
          .post("api/campaign/create/", data)
          .then(function () {
          })
          .catch(function (error) {
            if (error.response) {
              Swal.fire({
                title: "Error",
                text: "Failed to connect to service!",
                icon: "error",
                confirmButtonClass: "btn btn-secondary",
                heightAuto: false,
              });
            }
          });
      } else {
        Swal.fire({
          title: "Form Incomplete",
          text: "Please Fill the correct details before you submit!",
          icon: "error",
          confirmButtonClass: "btn btn-secondary",
        });
      }
    },
  },
  computed: {
    TemplateList() {
      return store.state.TemplateList;
    },
  },
};
</script>
